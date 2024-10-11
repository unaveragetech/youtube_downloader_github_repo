# from pytubefix import YouTube
# import os
# import requests
# import re
# from datetime import datetime

# # Function to download video by resolution
# def download_video(video_url, resolution, output_path):
#     try:
#         yt = YouTube(video_url)
#         stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
#         if stream:
#             timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#             video_filename = f"video_{timestamp}.mp4"
#             stream.download(output_path=output_path, filename=video_filename)
#             print(f"Video download completed in {resolution} resolution!")
#             return os.path.join(output_path, video_filename)
#         else:
#             print(f"No stream found for {resolution} resolution")
#             return None
#     except Exception as e:
#         print(f"An error occurred while downloading video: {e}")
#         return None

# # Function to download audio stream
# def download_audio(video_url, output_path):
#     try:
#         yt = YouTube(video_url)
#         stream_audio = yt.streams.filter(only_audio=True)[-1]
#         if stream_audio:
#             timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#             audio_filename = f"audio_{timestamp}.mp3"
#             stream_audio.download(output_path=output_path, filename=audio_filename)
#             print("Audio download completed!")
#             return os.path.join(output_path, audio_filename)
#         else:
#             print("No audio stream found")
#             return None
#     except Exception as e:
#         print(f"An error occurred while downloading audio: {e}")
#         return None

# # Function to merge video and audio using ffmpeg
# def merge_video_audio(video_path, audio_path, output_path):
#     try:
#         final_filename = f"final_video_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
#         final_path = os.path.join(output_path, final_filename)
#         os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}"')
#         print(f"Video and audio merged successfully into {final_path}")
#         os.remove(video_path)
#         print(f"Deleted the non-audio video file: {video_path}")
#     except Exception as e:
#         print(f"An error occurred while merging video and audio: {e}")

# # Function to get YouTube links based on user query
# def yt_link_videos(query):
#     query = query.replace(' ', '+')
#     search_url = f'https://www.youtube.com/results?search_query={query}'
#     print(f"Search URL: {search_url}")
    
#     response = requests.get(search_url)
#     if response.status_code != 200:
#         raise Exception("Failed to load YouTube search results page")
    
#     folder_path = 'youtube_search_responses'
#     file_path = os.path.join(folder_path, 'response.txt')
#     os.makedirs(folder_path, exist_ok=True)
    
#     with open(file_path, 'w+', encoding='utf-8') as file:
#         file.write(response.text)
    
#     print(f'Response written to: {file_path}')
    
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
    
#     video_ids = re.findall(r'videoId":"(.*?)"', content)
#     print(f"Extracted Video IDs: {video_ids[:10]}")  # Print only the first 10 video IDs
    
#     youtube_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids[:10]]
#     return youtube_links

# # Main Program
# query = input("Enter the video or movie name to search on YouTube: ")
# youtube_links = yt_link_videos(query)

# # Print the generated YouTube links
# print("Generated YouTube Links:")
# for index, link in enumerate(youtube_links, start=1):
#     print(f"{index}: {link}")

# # Allow user to select a video link
# choice = int(input("Select a video to download (1-10): ")) - 1
# if 0 <= choice < len(youtube_links):
#     video_url = youtube_links[choice]
# else:
#     print("Invalid selection.")
#     exit()

# # Select resolution
# print("Select resolution:")
# print("1) 360p")
# print("2) 720p")
# print("3) 1080p")
# resolution_choice = input("Enter a corresponding resolution:")

# resolution_map = {
#     "1": "360p",
#     "2": "720p",
#     "3": "1080p"
# }

# resolution = resolution_map.get(resolution_choice)

# output_path = "d:\\youtube_video"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)

# if resolution:
#     video_path = download_video(video_url, resolution, output_path)
#     audio_path = download_audio(video_url, output_path)
    
#     if video_path and audio_path:
#         merge_video_audio(video_path, audio_path, output_path)
# else:
#     print("Invalid resolution, please select a valid resolution.")




## next version update completed and user friendly ##

# from pytubefix import YouTube
# import os
# import requests
# import re
# from datetime import datetime

# # Function to download video by resolution
# def download_video(video_url, resolution, output_path, custom_name):
#     try:
#         yt = YouTube(video_url)
#         stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
#         if stream:
#             video_filename = f"{custom_name}_video.mp4"
#             stream.download(output_path=output_path, filename=video_filename)
#             print(f"Video download completed in {resolution} resolution!")
#             return os.path.join(output_path, video_filename)
#         else:
#             print(f"No stream found for {resolution} resolution")
#             return None
#     except Exception as e:
#         print(f"An error occurred while downloading video: {e}")
#         return None

# # Function to download audio stream
# def download_audio(video_url, output_path, custom_name):
#     try:
#         yt = YouTube(video_url)
#         stream_audio = yt.streams.filter(only_audio=True)[-1]
#         if stream_audio:
#             audio_filename = f"{custom_name}_audio.mp3"
#             stream_audio.download(output_path=output_path, filename=audio_filename)
#             print("Audio download completed!")
#             return os.path.join(output_path, audio_filename)
#         else:
#             print("No audio stream found")
#             return None
#     except Exception as e:
#         print(f"An error occurred while downloading audio: {e}")
#         return None

# # Function to merge video and audio using ffmpeg
# def merge_video_audio(video_path, audio_path, output_path):
#     try:
#         final_filename = f"{title}{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
#         final_path = os.path.join(output_path, final_filename)
#         os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}"')
#         print(f"Video and audio merged successfully into {final_path}")
#         os.remove(video_path)
#         print(f"Deleted the non-audio video file: {video_path}")
#     except Exception as e:
#         print(f"An error occurred while merging video and audio: {e}")

# # Function to get YouTube links based on user query
# def yt_link_videos(query):
#     query = query.replace(' ', '+')
#     search_url = f'https://www.youtube.com/results?search_query={query}'
#     print(f"Search URL: {search_url}")
    
#     response = requests.get(search_url)
#     if response.status_code != 200:
#         raise Exception("Failed to load YouTube search results page")
    
#     folder_path = 'youtube_search_responses'
#     file_path = os.path.join(folder_path, 'response.txt')
#     os.makedirs(folder_path, exist_ok=True)
    
#     with open(file_path, 'w+', encoding='utf-8') as file:
#         file.write(response.text)
    
#     print(f'Response written to: {file_path}')
    
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
    
#     video_ids = re.findall(r'videoId":"(.*?)"', content)
#     video_ids=list(set(video_ids))
#     print(f"Extracted Video IDs: {video_ids[:5]}")  # Print only the first 10 video IDs
    
#     youtube_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids[:5]]
#     yt_result={}
    
#     for i in youtube_links:
#         video=YouTube(i)
#         yt_result[video.title]=i
#     return yt_result
        
#     # return youtube_links

# # Main Program
# query = input("Enter the video or movie name to search on YouTube: ")
# youtube_links = yt_link_videos(query)

# # Print the generated YouTube links
# print("Generated YouTube Links:")
# for index, title in enumerate(youtube_links, start=1):
#     print(f"{index}: {title}")

# # Allow user to select a video link
# choice = int(input("Select a video to download (1-5): ")) - 1
# if 0 <= choice < len(youtube_links):    ## youtube_link
#     video_url = list(youtube_links.values())[choice]
# else:
#     print("Invalid selection.")
#     exit()

# # Get custom name from user
# #custom_name = input("Enter a custom name for the video files (without spaces): ")

# # Select resolution
# print("Select resolution:")
# print("1) 360p")
# print("2) 720p")
# print("3) 1080p")
# resolution_choice = input("Enter a corresponding resolution:")

# resolution_map = {
#     "1": "360p",
#     "2": "720p",
#     "3": "1080p"
# }

# resolution = resolution_map.get(resolution_choice)

# output_path = "d:\\youtube_video"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)

# if resolution:
#     video_path = download_video(video_url, resolution, output_path,title)
#     audio_path = download_audio(video_url, output_path,title)
    
#     if video_path and audio_path:
#         merge_video_audio(video_path, audio_path, output_path)
# else:
#     print("Invalid resolution, please select a valid resolution.")



## new update code for only longer video ## 

from pytubefix import YouTube
import os
import requests
import re
from datetime import datetime

# Function to download video by resolution
def download_video(video_url, resolution, output_path, title):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
        if stream:
            video_filename = f"{title}_video.mp4"
            stream.download(output_path=output_path, filename=video_filename)
            print(f"Video download completed in {resolution} resolution!")
            return os.path.join(output_path, video_filename)
        else:
            print(f"No stream found for {resolution} resolution")
            return None
    except Exception as e:
        print(f"An error occurred while downloading video: {e}")
        return None

# Function to download audio stream
def download_audio(video_url, output_path, custom_name):
    try:
        yt = YouTube(video_url)
        stream_audio = yt.streams.filter(only_audio=True)[-1]
        if stream_audio:
            audio_filename = f"{custom_name}_audio.mp3"
            stream_audio.download(output_path=output_path, filename=audio_filename)
            print("Audio download completed!")
            return os.path.join(output_path, audio_filename)
        else:
            print("No audio stream found")
            return None
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")
        return None

# Function to merge video and audio using ffmpeg
def merge_video_audio(video_path, audio_path, output_path, title):
    try:
        final_filename = f"{title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
        final_path = os.path.join(output_path, final_filename)
        os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}"')
        print(f"Video and audio merged successfully into {final_path}")
        os.remove(video_path)
        os.remove(audio_path)
        print(f"Deleted the non-audio video and audio files.")
    except Exception as e:
        print(f"An error occurred while merging video and audio: {e}")

# Function to get YouTube links based on user query
def yt_link_videos(query):
    # Construct the search URL
    query = query.replace(' ', '+')
    search_url = f'https://www.youtube.com/results?search_query={query}'
    print(f"Search URL: {search_url}")
    
    # Fetch the search results page
    response = requests.get(search_url)
    if response.status_code != 200:
        raise Exception("Failed to load YouTube search results page")
    
    # Extract video IDs directly from the HTML content
    content = response.text
    video_ids = re.findall(r'videoId":"(.*?)"', content)
    video_ids = list(dict.fromkeys(video_ids))  # Remove duplicates while preserving order

    # Get the first video ID and use it as a reference
    if not video_ids:
        print("No video IDs found.")
        return {}

    # Filter and only include videos longer than 60 seconds
    yt_result = {}
    youtube_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]
    
    for url in youtube_links:
        try:
            video = YouTube(url)
            if video.length > 60:  # Only include videos longer than 60 seconds
                yt_result[video.title] = url
                if len(yt_result) == 5:
                    break  # Stop after getting 5 videos
        except Exception as e:
            print(f"Error fetching video details for {url}: {e}")
    
    return yt_result

# Main Program
query = input("Enter the video or movie name to search on YouTube: ")
youtube_links = yt_link_videos(query)

# Print the generated YouTube links with titles (filtered by length > 60 seconds)
print("Generated YouTube Links (videos longer than 60 seconds):")
for index, title in enumerate(youtube_links, start=1):
    print(f"{index}: {title}")

# Allow user to select a video link
choice = int(input("Select a video to download (1-5): ")) - 1
if 0 <= choice < len(youtube_links):
    video_url = list(youtube_links.values())[choice]
    title = list(youtube_links.keys())[choice]
else:
    print("Invalid selection.")
    exit()

# Select resolution
print("Select resolution:")
print("1) 360p")
print("2) 720p")
print("3) 1080p")
resolution_choice = input("Enter a corresponding resolution:")

resolution_map = {
    "1": "360p",
    "2": "720p",
    "3": "1080p"
}

resolution = resolution_map.get(resolution_choice)

# Define output path
output_path = "d:\\youtube_video"
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Download video and audio and merge if resolution is valid
if resolution:
    video_path = download_video(video_url, resolution, output_path, title)
    audio_path = download_audio(video_url, output_path, title)
    
    if video_path and audio_path:
        merge_video_audio(video_path, audio_path, output_path, title)
else:
    print("Invalid resolution, please select a valid resolution.")
