"""
HTML Parsing Utilities
Functions for extracting content and images from HTML
"""

from bs4 import BeautifulSoup

# CSS class mappings for different websites
# USA = 0, BR = 1, ARG = 2
CONTENT_CLASSES = ['post-body', 'post-body entry-content', 'entry-inner']
IMAGE_CLASSES = ['story', 'post-body entry-content', 'entry-inner']


def get_featured_image_url(soup):
    """
    Fetch the featured image URL from the article
    
    Args:
        soup: BeautifulSoup object of the article page
        
    Returns:
        str: URL of the featured image or None
    """
    featured_image_tag = soup.find('meta', property='og:image')
    
    print("*"*8, "Fetching the featured image URL", "*"*8)
    print("-"*100)
    
    return featured_image_tag['content'] if featured_image_tag else None


def get_additional_image_urls(soup, website_index):
    """
    Retrieve the URLs of images in the article
    
    Args:
        soup: BeautifulSoup object of the article page
        website_index: Index of the website (0=USA, 1=BR, 2=ARG)
        
    Returns:
        list: List of image URLs
    """
    urls = []
    
    body = soup.find(class_=IMAGE_CLASSES[website_index])
    
    if not body:
        print("*"*8, "No image container found", "*"*8)
        print("-"*100)
        return urls

    # Find all 'img' tags within the 'body' content
    images = body.find_all('img')
    img_length = len(images)
    
    if img_length > 1: 
        for i in range(min(2, img_length)):
            img_src = images[i].get('src', '')

            # Split the src attribute using ';'
            src_parts = img_src.split(';')

            # Extract the second URL (assuming it's always the last part)
            second_url = src_parts[-1].lstrip('/')

            # Add the second URL to the list
            urls.append(second_url)
    elif img_length == 1:
        img_src = images[0].get('src', '')
        urls.append(img_src)
    
    print("*"*8, "Fetching additional image URLs", "*"*8)
    print("-"*100)
    
    return urls


def info(soup, website_index):
    """
    Extract the Title and Content of the post
    
    Args:
        soup: BeautifulSoup object of the article page
        website_index: Index of the website (0=USA, 1=BR, 2=ARG)
        
    Returns:
        list: [title, content]
    """
    content = []
    
    header = soup.find('h1')
    header_text = header.get_text() if header else ''
    content.append(header_text)
    
    text = soup.find(class_=CONTENT_CLASSES[website_index]) 
    content_text = text.get_text() if text else ''
    content.append(content_text)
        
    print("*"*8, "Extracting Title and Content", "*"*8)
    print("-"*100)

    return content
