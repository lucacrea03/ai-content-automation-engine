# Ai Content Automation Engine

A Python application that scrapes automotive articles from various sources, translates them to Spanish using Google AI, and publishes them to a WordPress blog.

## Features

- 🚗 Automates AI-driven content aggregation from multiple news sources.
- 🌐 Translates content from English/Portuguese to Spanish using Google Generative AI
- 📝 Automatically formats content with proper HTML tags
- 🖼️ Handles featured and additional images
- 📊 Categorizes posts based on content
- 👤 Randomly assigns authors to posts
- 🔄 Publishes directly to WordPress via REST API

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ai-content-automation-engine
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your credentials:
```bash
cp config/config_example.py config/config.py
```

4. Edit `config/config.py` with your actual credentials:
   - WordPress API endpoint and credentials
   - Google AI API key
   - Author mappings

## Configuration

### config/config.py

```python
# WordPress API Configuration
WORDPRESS_API_ENDPOINT = 'https://your-site.com/wp-json/wp/v2/posts'
WORDPRESS_MEDIA_ENDPOINT = 'https://your-site.com/wp-json/wp/v2/media'
WORDPRESS_USERNAME = 'your_username'
WORDPRESS_PASSWORD = 'your_app_password'

# Google AI Configuration
GOOGLE_API_KEY = 'your_google_ai_key'

# Author Configuration
AUTHORS = {
    'Author1': 1,
    'Author2': 2,
    'Author3': 3
}

# Website Selection (0=blog1, 1=blog2, 2=blog3)
WEBSITE_INDEX = 0
```

## Usage

Run the main script:

```bash
python main.py
```

The script will:
1. Fetch URLs from the configured sitemap
2. Extract article content and images
3. Translate content to Spanish using Google AI
4. Upload images to WordPress media library
5. Publish the formatted post with categories and featured image

## Project Structure

```
ai-content-automation-engine/
├── config/
│   ├── __init__.py
│   ├── config.py           # Your actual config (gitignored)
│   └── config_example.py   # Template for configuration
├── src/
│   ├── __init__.py
│   ├── categories.py       # WordPress category management
│   ├── content_utils.py    # Content processing utilities
│   ├── html_utils.py       # HTML parsing utilities
│   ├── network_utils.py    # Network request utilities
│   ├── prompts.py          # AI prompts for translation
│   ├── sitemaps.py         # Sitemap configuration
│   └── wordpress_utils.py  # WordPress API utilities
├── docs/                   # Documentation
├── .gitignore
├── main.py                 # Main execution script
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- google-generativeai

## Security Notes

⚠️ **Important**: Never commit your `config/config.py` file to Git. It contains sensitive credentials and is automatically ignored via `.gitignore`.

## WordPress Setup

1. Enable WordPress REST API
2. Create an Application Password for authentication
3. Ensure your WordPress user has appropriate permissions to create posts and upload media

## Google AI Setup

1. Create a project in Google Cloud Console
2. Enable the Generative AI API
3. Generate an API key
4. Add the key to your `config/config.py`

## License

MIT License
