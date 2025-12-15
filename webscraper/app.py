from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse

# Import the existing scraper function from project.py
try:
    # Support running as a package (e.g., `python -m webscraper.app` or pytest import)
    from .project import scrape_website
except Exception:
    # Fallback when running the module directly
    from project import scrape_website

app = Flask(__name__, static_folder='static')
CORS(app)


@app.route('/scrape', methods=['GET', 'POST'])
def scrape():
    """Scrape a URL supplied via GET (query param `url`) or POST JSON {'url': '...'}.

    Returns JSON with scraped fields or an error.
    """
    url = None
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        url = data.get('url')
    else:
        url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Missing `url` parameter'}), 400

    # Basic validation: reasonable length and structure
    if len(url) > 2048:
        return jsonify({'error': 'URL too long'}), 400

    parsed = urlparse(url if url.startswith(('http://', 'https://')) else 'https://' + url)
    if not parsed.scheme or not parsed.netloc:
        return jsonify({'error': 'Invalid URL provided'}), 400

    # Ensure http(s) present for requests
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        result = scrape_website(url)
    except Exception as e:
        # Log minimal detail to console; avoid exposing internals to clients
        print(f"Error while scraping: {e}")
        return jsonify({'error': 'Internal error while scraping'}), 500

    if not result:
        return jsonify({'error': 'Failed to fetch or parse website'}), 502

    return jsonify(result)


@app.route('/')
def index():
    # Serve the minimal frontend from static/index.html
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
