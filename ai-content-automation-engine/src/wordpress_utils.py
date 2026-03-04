"""
WordPress API Utilities
Functions for interacting with WordPress REST API
"""

import requests
from requests.auth import HTTPBasicAuth
from .network_utils import get_image_mime_type


def publish_on_wordpress(api_endpoint, data, username, password):
    """
    Publish content on WordPress via API with basic authentication
    
    Args:
        api_endpoint: WordPress API endpoint
        data: Post data dictionary
        username: WordPress username
        password: WordPress application password
    """
    auth = HTTPBasicAuth(username, password)
    try:
        response = requests.post(api_endpoint, json=data, auth=auth)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error publishing content on WordPress: {e}")
        print("-"*100)
        return

    if response.status_code == 201:
        print("*"*8, "Content published successfully!", "*"*8)
    else:
        print(f"Failed to publish content. Status code: {response.status_code}")


def upload_featured_image_to_wordpress(featured_image_url, api_endpoint_media, username, password):
    """
    Upload featured image to WordPress media library and retrieve the image ID
    
    Args:
        featured_image_url: URL of the featured image
        api_endpoint_media: WordPress media API endpoint
        username: WordPress username
        password: WordPress application password
        
    Returns:
        int: Media ID or None
    """
    auth = HTTPBasicAuth(username, password)
    
    try:
        if featured_image_url:
            image_content = requests.get(featured_image_url).content
            mime_type = requests.head(featured_image_url).headers['Content-Type']

            files = {'file': (f'file.{mime_type.split("/")[-1]}', image_content, mime_type)}

            response = requests.post(api_endpoint_media, files=files, auth=auth)
            response.raise_for_status()
            media_id = response.json().get('id')
            
            print("*"*8, "Fetching featured image id", "*"*8)
            print("-"*100)
            
            return media_id
        else:
            print("*"*8, "No featured image URL provided. Skipping image upload.", "*"*8)
            print("-"*100)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error uploading image to WordPress media library: {e}")
        print("-"*100)
        return None


def upload_image_to_wordpress(additional_image_urls, api_endpoint_media, username, password):
    """
    Upload multiple images to WordPress media library and retrieve their IDs
    
    Args:
        additional_image_urls: List of image URLs
        api_endpoint_media: WordPress media API endpoint
        username: WordPress username
        password: WordPress application password
        
    Returns:
        list: List of media IDs
    """
    auth = HTTPBasicAuth(username, password)
    uploaded_image_ids = []

    valid_urls = [url for url in additional_image_urls if url]

    for url in valid_urls:
        try:
            image_content = requests.get(url).content
            mime_type = get_image_mime_type(url)

            if mime_type:
                files = {'file': (f'file.{mime_type.split("/")[-1]}', image_content, mime_type)}

                response = requests.post(api_endpoint_media, files=files, auth=auth)
                response.raise_for_status()
                media_id = response.json().get('id')
                uploaded_image_ids.append(media_id)

        except requests.exceptions.RequestException as e:
            print(f"Error uploading image to WordPress: {e}")

    if not uploaded_image_ids:
        print("*"*8, "No featured image URL provided or all uploads failed. Skipping image upload.", "*"*8)
        print("-"*100)
    else:
        print("*"*8, "Fetching additional image ids", "*"*8)
        print("-"*100)

    return uploaded_image_ids


def get_image_url_from_media_id(uploaded_image_ids, api_endpoint_media, username, password):
    """
    Get image URLs from WordPress media library using media IDs
    
    Args:
        uploaded_image_ids: List of media IDs
        api_endpoint_media: WordPress media API endpoint
        username: WordPress username
        password: WordPress application password
        
    Returns:
        list: List of image URLs
    """
    auth = HTTPBasicAuth(username, password)
    img_urls = []
    
    try:
        if not uploaded_image_ids:
            print("*"*8, "No uploaded image IDs. Skipping fetching image URLs.", "*"*8)
            print("-"*100)
            return img_urls
        
        for media_id in uploaded_image_ids:
            media_details_url = f"{api_endpoint_media}/{media_id}"
            
            response = requests.get(media_details_url, auth=auth)
            response.raise_for_status()
            
            image_url = response.json().get('media_details', {}).get('sizes', {}).get('full', {}).get('source_url')
            img_urls.append(image_url)
        
        print("*"*8, "Fetching additional image URLs", "*"*8)
        print("-"*100)
        
        return img_urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image URL from WordPress media library: {e}")
        return None
