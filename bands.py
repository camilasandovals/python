import requests
import json
from collections import Counter

def get_posts(access_token, user_id):
    url = f"https://graph.instagram.com/{user_id}/media?fields=caption&access_token={access_token}"
    response = requests.get(url)
    data = json.loads(response.text)
    return [post['caption'] for post in data['data']]

def count_band_mentions(captions, bands):
    counter = Counter()
    for caption in captions:
        words = caption.lower().split()
        for word in words:
            if word in bands:
                counter[word] += 1
    return counter.most_common(10)

access_token = 'your-access-token'
user_id = 'your-user-id'
bands = ['band1', 'band2', 'band3', 'band4', 'band5', 'band6', 'band7', 'band8', 'band9', 'band10']

captions = get_posts(access_token, user_id)
top_bands = count_band_mentions(captions, bands)

print(top_bands)
