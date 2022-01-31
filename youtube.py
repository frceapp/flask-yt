import json
from youtube_search import YoutubeSearch

def search(x):
    ytb = YoutubeSearch(x).to_json()
    return len(json.loads(ytb)['videos']), json.loads(ytb)['videos']