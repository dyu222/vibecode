import pytest

try:
    # package-style import (when run from repo root)
    from webscraper.app import app
    import webscraper.project as project
except Exception:
    # fallback for other import patterns
    from app import app
    import project as project


@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_missing_url(client):
    rv = client.get('/scrape')
    assert rv.status_code == 400


def test_failed_scrape_returns_502(client, monkeypatch):
    monkeypatch.setattr(project, 'scrape_website', lambda url: None)
    rv = client.get('/scrape?url=example.invalid')
    assert rv.status_code == 502


def test_success_scrape(client, monkeypatch):
    sample = {'url': 'https://example.com', 'title': 'Example Site'}
    # Monkeypatch the function used by the running app (app.scrape_website)
    import webscraper.app as app_mod
    monkeypatch.setattr(app_mod, 'scrape_website', lambda url: sample)
    rv = client.get('/scrape?url=https://example.com')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['title'] == 'Example Site'


def test_invalid_url_format(client):
    rv = client.get('/scrape?url=not-a-valid-url')
    assert rv.status_code == 400


def test_too_long_url(client):
    long_url = 'http://' + ('a' * 5000) + '.com'
    rv = client.get(f'/scrape?url={long_url}')
    assert rv.status_code == 400
