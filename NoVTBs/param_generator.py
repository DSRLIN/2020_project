# youtube part
video_params_base = {"part": "id,snippet,statistics",
                     "id": "",
                     "key": ""}

channel_params_base = {"part": "id,snippet,statistics",
                       "id": "",
                       "key": ""}

comment_params_base = {"part": "id,snippet",
                       "videoId": "",
                       "key": "",
                       "order": "relevance"}


def gen_video_param(video_id, key):
    ret_res = video_params_base
    ret_res["id"] = video_id
    ret_res["key"] = key
    return ret_res


def gen_channel_param(channel_id, key):
    ret_res = channel_params_base
    ret_res["id"] = channel_id
    ret_res["key"] = key
    return ret_res


def gen_comment_param(video_id, key):
    ret_res = comment_params_base
    ret_res.update({"maxResults": 1})
    ret_res["videoId"] = video_id
    ret_res["key"] = key
    return ret_res


# twitter part
