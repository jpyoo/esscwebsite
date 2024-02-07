import requests
from .models import InstagramPost
import time
    
def get_instagram_posts():
    api_version = 'v19.0'
    access_token = 'IGQWRNd0FBUHBXeU4ycGtYMjI4VHNwMzVQLTdlQXBwTVNVY21CVFZAoM2JMeGtyRVc3OUV1TEF6NmtMWVJLcEllUzkzeWxoVVhLalI2QlFZAMTFZAcVBOZAjJhNmxXamRhWlVsdTA0MlpuNnZA0SUR6WEhTanBvSFJXc0UZD'
    user_id = '6898103826982187'
    fields = 'id,media_type,media_url,caption,timestamp,username'
    # api_url = f'https://graph.instagram.com/{api_version}/{user_id}/media?access_token={access_token}'
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
    print('data:', data)
    posts = []
        
    for post in data.get('data', []):
        thumbnail_url = post.get('media_url', '')
        caption = post.get('caption', '')
        print('caption:', caption)
        instagram_post = InstagramPost.objects.create(thumbnail_url=thumbnail_url, caption=caption)
        posts.append(instagram_post)

    if not posts:
        print('no posts found')

    return posts