# Webscraper Flask API

This folder contains a simple Flask API that wraps the existing `project.py` scraper and a minimal frontend for quick demos.

### Install

From the `personal` folder, install dependencies:

```bash
cd personal
python3 -m venv .venv && source .venv/bin/activate
pip install -r webscraper/requirements.txt
```

### Run the API (development)

```bash
cd personal/webscraper
python3 app.py
# server will be available at http://127.0.0.1:5000
```

Open `http://127.0.0.1:5000/` in your browser to use the minimal frontend.

### API

- GET /scrape?url={url} — Returns JSON scraped data
- POST /scrape with JSON body `{ "url": "https://example.com" }`

Example:

```bash
curl 'http://127.0.0.1:5000/scrape?url=https://example.com'
```

### Tests

From `personal` (so package imports work):

```bash
cd personal
PYTHONPATH=. pytest -q
```

### Notes & Next Steps

- The frontend is intentionally minimal (static HTML + JS). You can replace it with a React/Vue page later.
- The scraper enforces a basic URL validation and request timeout. Add further sanitization or rate limiting if you intend to expose the service publicly.
