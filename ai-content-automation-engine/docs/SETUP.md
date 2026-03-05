# Setup Guide

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-content-automation-engine
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install requests beautifulsoup4 google-generativeai
```

### 3. Configure Your Credentials

The repository comes with a `config_example.py` file. You need to create your actual configuration:

```bash
# Option 1: Copy the example file
cp config/config_example.py config/config.py

# Option 2: Edit the existing config.py file
nano config/config.py  # or use your preferred editor
```

### 4. Update Configuration Values

Edit `config/config.py` with your actual credentials:

```python
# WordPress API Configuration
WORDPRESS_API_ENDPOINT = 'https://your-wordpress-site.com/wp-json/wp/v2/posts'
WORDPRESS_MEDIA_ENDPOINT = 'https://your-wordpress-site.com/wp-json/wp/v2/media'
WORDPRESS_USERNAME = 'your_username'
WORDPRESS_PASSWORD = 'your_application_password'  # Not your login password!

# Google AI Configuration
GOOGLE_API_KEY = 'your_google_ai_api_key_here'

# Author Configuration - Map names to WordPress user IDs
AUTHORS = {
    'Author1': 1,
    'Author2': 2,
    'Author3': 3
}

# Website Selection
# 0 = autoblog (US)
# 1 = carblog (Brazil)
# 2 = 16valvulas (Argentina)
WEBSITE_INDEX = 0
```

### 5. WordPress Application Password

⚠️ **Important**: You need a WordPress Application Password, not your regular login password.

To create one:
1. Log into your WordPress admin panel
2. Go to Users → Profile
3. Scroll down to "Application Passwords"
4. Enter a name (e.g., "AI content automation engine")
5. Click "Add New Application Password"
6. Copy the generated password and use it in your config

### 6. Google AI API Key

To get a Google AI API key:
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and add it to your config

### 7. Find WordPress User IDs

To find author user IDs:
1. Go to WordPress admin → Users
2. Click on a user
3. Look at the URL: `user-edit.php?user_id=X` - X is the user ID
4. Add these IDs to the `AUTHORS` dictionary in config

## Running the Script

```bash
python main.py
```

## Troubleshooting

### Import Errors
If you get import errors, make sure you're running from the project root directory:
```bash
cd /path/to/ai-content-automation-engine
python main.py
```

### Authentication Errors
- Double-check your WordPress username and application password
- Ensure your WordPress user has permission to create posts and upload media
- Verify the API endpoints are correct

### Google AI Errors
- Verify your API key is correct
- Check you haven't exceeded your quota
- Ensure the Generative AI API is enabled in your Google Cloud project

### Category Errors
The script fetches categories from your WordPress site. Make sure:
- Your WordPress site is accessible
- The categories endpoint is available at `/wp-json/wp/v2/categories`

## Git Best Practices

### Before Your First Commit

```bash
# Initialize git (if not already done)
git init

# Verify .gitignore is working
git status

# You should NOT see config/config.py in the list
# If you do, check your .gitignore file
```

### First Commit

```bash
git add .
git commit -m "Initial commit - ai content automation engine"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### Updating

```bash
git add .
git commit -m "Your commit message"
git push
```

## Security Checklist

- [ ] `config/config.py` is listed in `.gitignore`
- [ ] No credentials are hardcoded in any Python files
- [ ] `config_example.py` contains only placeholder values
- [ ] You've verified `config/config.py` doesn't appear in `git status`

## Next Steps

1. Test with a single article first (modify the loop in main.py)
2. Monitor the WordPress site to ensure posts are published correctly
3. Check image uploads are working
4. Verify categories are being assigned properly
5. Scale up to process multiple articles
