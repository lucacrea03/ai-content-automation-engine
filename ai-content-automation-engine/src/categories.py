"""
WordPress Categories Management
Fetches and stores category IDs and names from WordPress API
"""

import requests

category_id = []
category_name = []

url = 'https://mundoautomotor.com.ar/wp-json/wp/v2/categories?per_page=100'

try:
    response = requests.get(url)
    response.raise_for_status()
    
    if response.status_code == 200:
        categories = response.json()
        for category in categories:
            category_id.append(category['id'])
            category_name.append(category['name'])
    else:
        print(f'Failed to retrieve categories. Status code: {response.status_code}')
        
except requests.exceptions.RequestException as e:
    print(f'Error fetching categories: {e}')
