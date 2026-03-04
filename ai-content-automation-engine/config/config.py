"""
Configuration file for Car Blog Scraper
"""

# WordPress API Configuration
WORDPRESS_API_ENDPOINT = 'https://your-wordpress-site.com/wp-json/wp/v2/posts'
WORDPRESS_MEDIA_ENDPOINT = 'https://your-wordpress-site.com/wp-json/wp/v2/media'
WORDPRESS_USERNAME = 'your_username'
WORDPRESS_PASSWORD = 'your_application_password'

# Google AI Configuration
GOOGLE_API_KEY = 'your_google_ai_api_key_here'

# Author Configuration
AUTHORS = {
    'Author1': 1,
    'Author2': 2,
    'Author3': 3
}

# Website Selection
# 0 = autoblog, 1 = carblog, 2 = 16valvulas
WEBSITE_INDEX = 0
