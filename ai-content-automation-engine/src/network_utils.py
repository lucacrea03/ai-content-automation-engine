"""
Network Utilities
Functions for fetching content from URLs and uploading to WordPress
"""

import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET


def get_urls_from_sitemap(sitemap_url):
    """
    Fetch URLs from sitemap
    
    Args:
        sitemap_url: URL of the sitemap
        
    Returns:
        list: List of URLs from the sitemap
    """
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        print("-"*100)
        return []
    
    print("-"*100)
    print("*"*8, "Fetching URLs from Sitemap", "*"*8)
    print("-"*100)

    if response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            print("-"*100)
            return []
        urls = [loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
        return urls
    else:
        print(f"Failed to fetch sitemap. Status code: {response.status_code}")
        print("-"*100)
        return []


def get_image_mime_type(url):
    """
    Retrieve the MIME type of an image
    
    Args:
        url: URL of the image
        
    Returns:
        str: MIME type or None
    """
    try:
        response = requests.head(url)
        response.raise_for_status()
        return response.headers.get('Content-Type')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching MIME type for image: {e}")
        return None
