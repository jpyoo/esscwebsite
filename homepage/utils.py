import requests

def get_instagram_posts():
    access_token = 'YOUR_INSTAGRAM_ACCESS_TOKEN'
    user_id = 'YOUR_INSTAGRAM_USER_ID'
    api_url = f'https://graph.instagram.com/v12.0/{user_id}/media?access_token={access_token}'

    response = requests.get(api_url)
    data = response.json()

    posts = []
    for post in data.get('data', []):
        thumbnail_url = post.get('thumbnail_url', '')
        caption = post.get('caption', '')
        posts.append({'thumbnail_url': thumbnail_url, 'caption': caption})

    return posts