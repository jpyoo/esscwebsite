import requests
from .models import InstagramPost
import time
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, '/esscwebsite/.env')

load_dotenv(dotenv_path=dotenv_path)

def get_instagram_posts():
    api_version = 'v19.0'
    access_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
    user_id = os.getenv('INSTAGRAM_USER_ID')
    fields = 'id,media_type,media_url,caption,timestamp,username'
    api_url = f'https://graph.instagram.com/{api_version}/{user_id}/media?fields={fields}&access_token={access_token}'


    response = ''
    while response == '':
        try:
            response = requests.get(api_url)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    data = response.json()
    posts = []
    for i in range(min(len(data.get('data', [])),6)):
        post = data['data'][i]
        thumbnail_url = post.get('media_url', '')
        caption = post.get('caption', '')
        # print('caption:', caption)
        instagram_post = InstagramPost.objects.create(thumbnail_url=thumbnail_url, caption=caption)
        posts.append(instagram_post)

    if not posts:
        print('no posts found')

    return posts