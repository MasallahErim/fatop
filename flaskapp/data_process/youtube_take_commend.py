from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

def get_video_id_from_url(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'www.youtube.com':
        video_id = parse_qs(parsed_url.query).get('v')
        if video_id:
            return video_id[0]
    elif parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    return None

def get_all_video_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    nextPageToken = None
    while True:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText',
            pageToken=nextPageToken
        ).execute()
        for item in response['items']:
            comment_details = {
                'comment_text': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                'like_count': item['snippet']['topLevelComment']['snippet'].get('likeCount', 0),
                'author': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                'published_at': item['snippet']['topLevelComment']['snippet']['publishedAt'],
            }
            comments.append(comment_details)
        nextPageToken = response.get('nextPageToken')
        if not nextPageToken:
            break
    return comments

def get_video_details(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_response = youtube.videos().list(
        part='snippet,statistics',
        id=video_id
    ).execute()

    if video_response['items']:
        video_details = {
            'title': video_response['items'][0]['snippet']['title'],
            'view_count': video_response['items'][0]['statistics'].get('viewCount', 0),
            'like_count': video_response['items'][0]['statistics'].get('likeCount', 0),
            'dislike_count': video_response['items'][0]['statistics'].get('dislikeCount', 0),
            'comment_count': video_response['items'][0]['statistics'].get('commentCount', 0),
        }
        return video_details
    else:
        return None

def fetch_video_info(link):
    api_key = 'yourKey'
    # video_url = link
    video_id = get_video_id_from_url(link)

    if video_id:
        video_comments = get_all_video_comments(api_key, video_id)
        video_details = get_video_details(api_key, video_id)

        if video_details:
            video_info = {
                'video_details': video_details,
                'video_comments': video_comments,
            }
            return video_info
        else:
            return None
    else:
        return None


