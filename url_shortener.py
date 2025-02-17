from flask import Flask, request, jsonify, redirect
import hashlib
import random
import string

app = Flask(__name__)
url_mapping = {}


def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:6]
    
    # Ensure uniqueness
    while short_url in url_mapping:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    return short_url


@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("url")
    custom_alias = data.get("alias")
    
    if not long_url:
        return jsonify({"error": "URL is required"}), 400
    
    if custom_alias:
        if custom_alias in url_mapping:
            return jsonify({"error": "Alias already in use"}), 400
        short_url = custom_alias
    else:
        short_url = generate_short_url(long_url)
    
    url_mapping[short_url] = long_url
    
    return jsonify({"short_url": request.host_url + short_url})


@app.route('/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "Short URL not found"}), 404


@app.route('/stats', methods=['GET'])
def get_stats():
    return jsonify({"total_shortened_urls": len(url_mapping), "url_mapping": url_mapping})


if __name__ == '__main__':
    app.run(debug=True)
