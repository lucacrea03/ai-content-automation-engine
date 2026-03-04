"""
Configuration file - COPY FROM config_example.py
This file is gitignored - never commit your actual credentials
"""

# WordPress API Configuration
WORDPRESS_API_ENDPOINT = 'https://www.mundoautomotor.com.ar/wp-json/wp/v2/posts'
WORDPRESS_MEDIA_ENDPOINT = 'https://www.mundoautomotor.com.ar/wp-json/wp/v2/media'
WORDPRESS_USERNAME = 'mundos'
WORDPRESS_PASSWORD = 'FLjs mvAo 16bj z3s7 mHPw Xz15'

# Google AI Configuration
GOOGLE_API_KEY = 'AIzaSyBoHaMo9Rf5iwTxuc99obiiUzEl_n-nmGM'

# Author Configuration
AUTHORS = {
    'Luca': 6,
    'Matheo': 7,
    'Eduardo': 4
}

# Website Selection
# 0 = autoblog, 1 = carblog, 2 = 16valvulas
WEBSITE_INDEX = 0
