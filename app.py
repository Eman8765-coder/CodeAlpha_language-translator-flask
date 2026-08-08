# ============================================================
# app.py — This is your BACKEND (the server)
# Written in Python using Flask framework
#
# WHAT IS FLASK?
# Flask is a lightweight Python library that lets you create
# a web server in just a few lines of code.
# Your server will run on YOUR computer and listen for requests
# from the browser (your frontend HTML/JS).
# ============================================================

# ---- IMPORTS ----
# "import" means: bring in an external tool/library we need

from flask import Flask, request, jsonify, render_template
# Flask      → the main framework to create our server
# request    → lets us READ data the browser sends us
# jsonify    → converts Python dictionary → JSON response
# render_template → sends our HTML file to the browser

from flask_cors import CORS
# CORS = Cross-Origin Resource Sharing
# By default, browsers BLOCK JavaScript from talking to a
# server on a different address (security rule called Same-Origin Policy).
# Our HTML runs on one port, Flask runs on another port.
# CORS tells Flask: "it's okay, allow our frontend to talk to you."

import requests
# This is Python's library for making HTTP requests (like fetch() in JS).
# We use it to call the MyMemory API FROM our Python server.

import os
# os = operating system tools
# We use it to read environment variables (like secret API keys)
# so we don't write secrets directly in our code.


# ============================================================
# CREATE THE FLASK APP
# ============================================================
app = Flask(__name__)
# Flask(__name__) creates the app.
# __name__ is a special Python variable that tells Flask
# where to find files like templates/ folder.

CORS(app)
# Enable CORS for all routes — allows our frontend to talk to this server.


# ============================================================
# WHAT IS A ROUTE?
# A route is a URL path that our server "listens" on.
# When someone visits that URL, Flask runs the function below it.
#
# Example:
# @app.route("/")         → listens at http://localhost:5000/
# @app.route("/translate")→ listens at http://localhost:5000/translate
# ============================================================


# ---- ROUTE 1: Serve the homepage ----
@app.route("/")
def home():
    # When browser visits http://localhost:5000/
    # Flask looks for index.html inside a folder called "templates/"
    # and sends it to the browser.
    return render_template("index.html")


# ---- ROUTE 2: The Translation API Endpoint ----
@app.route("/translate", methods=["POST"])
# methods=["POST"] means this route ONLY accepts POST requests.
# POST is used when you're SENDING data to the server (not just fetching a page).
# Our JavaScript will send: { text: "Hello", source: "en", target: "ur" }

def translate():
    """
    This function:
    1. Receives text from the browser
    2. Validates it
    3. Calls the MyMemory API
    4. Returns the translation back to the browser
    """

    # ---- STEP 1: Read the data sent from browser ----
    data = request.get_json()
    # request.get_json() reads the JSON body that our JavaScript sent.
    # data is now a Python dictionary like:
    # { "text": "Hello", "source": "en", "target": "ur" }

    if not data:
        # If no data was sent, return an error
        return jsonify({"error": "No data received"}), 400
        # jsonify() converts a Python dict to a JSON response
        # 400 = HTTP status code for "Bad Request"


    # ---- STEP 2: Extract values from the data ----
    text   = data.get("text", "").strip()
    source = data.get("source", "en")
    target = data.get("target", "ur")
    # .get("key", "default") safely reads a key from dict.
    # If "text" doesn't exist, it returns "" instead of crashing.
    # .strip() removes extra spaces from start/end.


    # ---- STEP 3: Validate the input ----
    if not text:
        return jsonify({"error": "Text cannot be empty"}), 400

    if len(text) > 500:
        return jsonify({"error": "Text too long. Maximum 500 characters."}), 400

    if source == target:
        return jsonify({"error": "Source and target language cannot be the same"}), 400


    # ---- STEP 4: Build the MyMemory API URL ----
    api_url = "https://api.mymemory.translated.net/get"
    # Instead of building a messy URL string, we pass parameters separately.
    # The requests library combines them cleanly.

    params = {
        "q": text,                          # the text to translate
        "langpair": f"{source}|{target}",   # e.g. "en|ur"
    }
    # f"..." is a Python f-string — works like JS template literals.
    # f"{source}|{target}" with source="en", target="ur" → "en|ur"

    # Optional: add your email to get 10,000 free words/day instead of 500
    # params["de"] = "your-email@gmail.com"


    # ---- STEP 5: Call the API ----
    try:
        response = requests.get(api_url, params=params, timeout=10)
        # requests.get() sends a GET request to the API URL.
        # timeout=10 means: if the API doesn't respond in 10 seconds, stop waiting.

        response.raise_for_status()
        # raise_for_status() automatically throws an error if
        # the API returned a 4xx or 5xx HTTP status code.
        # This saves us from manually checking response.status_code.

        api_data = response.json()
        # .json() converts the API's text response into a Python dictionary.
        # Same idea as JavaScript's response.json()


        # ---- STEP 6: Extract the translation ----
        if api_data.get("responseStatus") == 200:
            translated_text = api_data["responseData"]["translatedText"]

            # Send the result back to the browser as JSON
            return jsonify({
                "success": True,
                "translation": translated_text,
                "source": source,
                "target": target,
                "original": text
            })
            # The browser's JavaScript will receive this object
            # and display the translation on screen.

        else:
            error_detail = api_data.get("responseDetails", "Unknown error")
            return jsonify({"error": f"Translation failed: {error_detail}"}), 502
            # 502 = Bad Gateway (our server got a bad response from the API)

    except requests.exceptions.Timeout:
        # This runs if the API took longer than 10 seconds
        return jsonify({"error": "Translation service timed out. Try again."}), 504

    except requests.exceptions.ConnectionError:
        # This runs if there's no internet connection
        return jsonify({"error": "Cannot connect to translation service. Check your internet."}), 503

    except requests.exceptions.RequestException as e:
        # This catches ANY other request error
        return jsonify({"error": f"Request failed: {str(e)}"}), 500
        # 500 = Internal Server Error


# ---- ROUTE 3: Health Check ----
@app.route("/health")
def health():
    # A simple route to check if the server is running.
    # Visit http://localhost:5000/health in your browser.
    # Useful for debugging.
    return jsonify({"status": "Server is running!", "version": "1.0"})


# ============================================================
# START THE SERVER
# ============================================================
if __name__ == "__main__":
    # __name__ == "__main__" means:
    # Only run this block if we start THIS file directly.
    # If another file imports app.py, this block is skipped.

    print("=" * 50)
    print("  LinguaSwift Flask Server Starting...")
    print("  Open: http://localhost:5000")
    print("  Health check: http://localhost:5000/health")
    print("=" * 50)

    app.run(
        debug=True,
        # debug=True means:
        # 1. Shows detailed error messages in the browser
        # 2. Auto-restarts server when you save changes
        # IMPORTANT: Set debug=False before deploying to production!

        port=5000,
        # The port number our server listens on.
        # http://localhost:5000 — 5000 is the port.

        host="0.0.0.0"
        # 0.0.0.0 means: accept connections from any device on the network.
        # "localhost" or "127.0.0.1" would only allow YOUR computer.
    )
