"""
Sitemap Configuration
Maps website indices to their sitemap URLs
"""

# Website sitemap mapping
SITEMAPS = {
    0: 'https://www.autoblog.com/google-news-feed48.xml',
    1: 'https://www.car.blog.br/sitemap.xml?page=1',
    2: 'https://www.16valvulas.com.ar/post-sitemap.xml'
}

WEBSITE_NAMES = {
    0: 'autoblog',
    1: 'carblog',
    2: '16valvulas'
}


def get_sitemap_url(website_index):
    """
    Get sitemap URL for the specified website
    
    Args:
        website_index: Index of the website (0, 1, or 2)
        
    Returns:
        str: Sitemap URL
    """
    return SITEMAPS.get(website_index, SITEMAPS[0])


def get_website_name(website_index):
    """
    Get website name for the specified index
    
    Args:
        website_index: Index of the website (0, 1, or 2)
        
    Returns:
        str: Website name
    """
    return WEBSITE_NAMES.get(website_index, 'autoblog')
