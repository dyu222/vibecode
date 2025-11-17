> **🎵 Vibe Coding Projects** - These projects were/will be built entirely using GitHub Copilot's (or similarly trained LLM's) natural language capabilities. No manual code writing—just chat-based development! I only write code manually if Copilot can't accomplish what I need.

# Web Scraper

A simple Python web scraper that extracts useful information from websites.

## Features

- Fetches webpage content using HTTP requests
- Extracts titles, headings, paragraphs, links, and images
- Displays results in a readable format
- Handles errors gracefully

## Installation

1. Clone or download this project
2. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

Run the script:

```bash
python3 project.py
```

Then enter a website URL when prompted. The scraper will extract and display:
- Page title
- Headings (H1, H2, H3)
- Links
- Images

## Example

```
Welcome to the Web Scraper!
Enter a website URL: github.com
Scraping website...
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4

## Notes

- URLs without `http://` or `https://` will automatically be prefixed with `https://`
- The scraper extracts the first 5 paragraphs, 10 links, and 5 images
- Includes a user-agent header to avoid being blocked by some websites