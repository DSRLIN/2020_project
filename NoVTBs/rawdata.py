import requests
import json


def video_raw_data(params):
    res = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params=params
    )
    result = json.dumps(res.json(), indent=4, ensure_ascii=False)
    return json.loads(result)


def channel_raw_data(params):
    res = requests.get(
        "https://www.googleapis.com/youtube/v3/channels",
        params=params
    )
    result = json.dumps(res.json(), indent=4, ensure_ascii=False)
    return json.loads(result)


def comment_raw_data(params):
    res = requests.get(
        "https://www.googleapis.com/youtube/v3/commentThreads",
        params=params
    )
    result = json.dumps(res.json(), indent=4, ensure_ascii=False)
    return json.loads(result)
