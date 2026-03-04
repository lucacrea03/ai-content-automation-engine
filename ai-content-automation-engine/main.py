"""
Main script for Car Blog Scraper
Fetches articles from automotive sitemaps, translates them using Google AI,
and publishes to WordPress
"""

import google.generativeai as genai
import time
import random
import requests
from bs4 import BeautifulSoup

# Import configuration
from config.config import (
    WORDPRESS_API_ENDPOINT,
    WORDPRESS_MEDIA_ENDPOINT,
    WORDPRESS_USERNAME,
    WORDPRESS_PASSWORD,
    GOOGLE_API_KEY,
    AUTHORS,
    WEBSITE_INDEX
)

# Import utilities
from src.categories import category_id, category_name
from src.prompts import title_prompt, content_prompt
from src.network_utils import get_urls_from_sitemap
from src.html_utils import info, get_featured_image_url, get_additional_image_urls
from src.wordpress_utils import (
    publish_on_wordpress,
    upload_featured_image_to_wordpress,
    upload_image_to_wordpress,
    get_image_url_from_media_id
)
from src.content_utils import trim
from src.sitemaps import get_sitemap_url


def main():
    """Main program execution"""
    
    # Create a dictionary to store values for each category
    category_values = {}
    for i in range(len(category_name)):
        category_values[category_name[i]] = category_id[i]

    # Fetch URLs from sitemap
    sitemap_url = get_sitemap_url(WEBSITE_INDEX)
    urls = get_urls_from_sitemap(sitemap_url)

    # Process each URL
    for i, url in enumerate(urls):
        print(f"\n{'='*100}")
        print(f"Processing URL {i+1}/{len(urls)}: {url}")
        print(f"{'='*100}\n")
        
        # Select random author
        random_author = random.choice(list(AUTHORS.keys()))
        author_number = AUTHORS[random_author]
        
        # Fetch and parse the article
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            print("-"*100)
            continue

        soup = BeautifulSoup(r.text, 'html.parser')
        information = info(soup, WEBSITE_INDEX)
        
        # Skip if not car-related
        if not any(category.lower() in information[1].lower() for category in category_name):
            print(f"Skipping URL {url} as content isn't related to cars.")
            print("-"*100)
            continue
        
        # Skip if content is too long (10,000 characters max)
        if len("".join(information)) > 10000:
            print(f"Skipping URL {url} as content length exceeds 10,000 characters.")
            print("-"*100)
            continue
        
        # Trim content
        trimmed_title, trimmed_content = trim(information)
        title_string = str(trimmed_title)
        content_string = str(trimmed_content)
        
        # Configure Google AI
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate translated content
        try:
            print("*"*8, "Generating Title", "*"*8)
            print("-"*100)
            title_response = model.generate_content(f"{title_prompt}: {title_string}")
            time.sleep(5)
                    
            print("*"*8, "Generating Content", "*"*8)
            print("-"*100)
            content_response = model.generate_content(f"{content_prompt}: {content_string}")
            time.sleep(5)
        except requests.exceptions.RequestException as e:
            print("*"*8, f"Error making Google AI API request: {e}", "*"*8)
            print("-"*100)
            continue
        
        # Extract translated content
        try:
            translated_title = title_response.text
            translated_content = content_response.text
        except ValueError:
            print("*"*8, "Google AI API request has blocked the response", "*"*8)
            print("-"*100)
            continue
        
        # Handle images
        featured_image_url = get_featured_image_url(soup)
        media_id = upload_featured_image_to_wordpress(
            featured_image_url,
            WORDPRESS_MEDIA_ENDPOINT,
            WORDPRESS_USERNAME,
            WORDPRESS_PASSWORD
        )
        
        additional_image_urls = get_additional_image_urls(soup, WEBSITE_INDEX)
        uploaded_image_ids = upload_image_to_wordpress(
            additional_image_urls,
            WORDPRESS_MEDIA_ENDPOINT,
            WORDPRESS_USERNAME,
            WORDPRESS_PASSWORD
        )
        
        image_urls = get_image_url_from_media_id(
            uploaded_image_ids,
            WORDPRESS_MEDIA_ENDPOINT,
            WORDPRESS_USERNAME,
            WORDPRESS_PASSWORD
        )
        
        # Format images for WordPress
        img1 = '' if not image_urls else f'<figure class="wp-block-image size-large"><img src="{image_urls[0]}" style="width:50%;height:auto;float:left;margin:15px" /></figure>'
        img2 = '' if len(image_urls) < 2 else f'<figure class="wp-block-image size-large"><img src="{image_urls[1]}" /></figure>'

        # Prepare post data
        trimmed_info = {
            'title': translated_title,
            'content': f'{img1}{translated_content}{img2}',
            'author': author_number
        }

        # Assign categories
        assigned_cat = set()
        for category in category_name:
            if category.lower() in information[1].lower():
                assigned_cat.add(category)

        assigned_cat = list(assigned_cat)
        
        if len(assigned_cat) > 0:
            values_list = [category_values.get(category) for category in assigned_cat]
            trimmed_info['categories'] = values_list
        
        if media_id:
            trimmed_info['featured_media'] = media_id
        
        # Publish to WordPress
        publish_on_wordpress(
            WORDPRESS_API_ENDPOINT,
            trimmed_info,
            WORDPRESS_USERNAME,
            WORDPRESS_PASSWORD
        )

        # Print results
        print("-"*100)
        print("*"*8, "Translated Content", "*"*8)
        print()
        print("*"*8, "Title", "*"*8)
        print()
        print(translated_title)
        print()
        print("*"*8, "Content", "*"*8)
        print()
        print(translated_content)
        print()
        print("-"*100)
        
        # Delay between requests
        time.sleep(5)


if __name__ == "__main__":
    main()
