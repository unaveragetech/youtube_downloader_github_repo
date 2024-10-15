# import streamlit as st
# from pytubefix import YouTube
# import re
# import requests
# import os
# from datetime import datetime

# # Streamlit UI
# st.title("YouTube Video Downloader")

# # Create a directory for downloads if it doesn't exist
# output_path = "d:/youtube_video"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)

# # Input for search query
# query = st.text_input("Enter the video name to search on YouTube:")
# resolution_choice = st.selectbox("Select resolution:", ["360p", "720p", "1080p"])

# # Function to download video 
# def download_video(video_url, resolution, output_path, title):
#     try:
#         yt = YouTube(video_url)
#         # Use adaptive=True for higher resolutions
#         stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
#         # if not stream:
#             # stream = yt.streams.filter(subtype='mp4', res=resolution, progressive=True).first()
#         if stream:
#             video_filename = f"{title}_{resolution}_video.mp4"
#             stream.download(output_path=output_path, filename=video_filename)
#             return os.path.join(output_path, video_filename)
#         else:
#             st.warning(f"No video found for the selected resolution: {resolution}.")
#             return None
#     except Exception as e:
#         st.error(f"Error downloading video: {e}")
#         return None
    
# # function to download audio in stream #
# def download_audio(video_url,output_path,title):
#     try:
#         yt=YouTube(video_url)
#         stream=yt.streams.filter(only_audio=True)[-1]
#         if stream:
#             audio_filename=f"{title}_audio.mp3"
#             stream.download(output_path=output_path,filename=audio_filename)
#             return os.path.join(output_path,audio_filename)
#         else:
#             st.warning(" audio not found in stream ")
#             return None
#     except Exception as e:
#             st.error(f" an error occured downloding for this mp3{e}")
#             return None
        
# # Function to merge video and audio using ffmpeg
# def merge_video_audio(video_path, audio_path, output_path,title):
#     try:
#         final_filename = f"{title}{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
#         final_path = os.path.join(output_path, final_filename)
#         os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}"')
#         print(f"Video and audio merged successfully into {final_path}")
#         os.remove(video_path)
#         print(f"Deleted the non-audio video file: {video_path}")
#     except Exception as e:
#         st.error(f"An error occurred while merging video and audio: {e}")

# # Function to search YouTube videos
# def yt_link_videos(query):
#     query = query.replace(' ', '+')
#     search_url = f'https://www.youtube.com/results?search_query={query}'
    
#     try:
#         response = requests.get(search_url)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         st.error(f"Error fetching YouTube search results: {e}")
#         return {}

#     content = response.text
#     video_ids = re.findall(r'videoId":"(.*?)"', content)
#     video_ids = list(set(video_ids))

#     youtube_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids[:5]]
#     yt_result = {YouTube(link).title: link for link in youtube_links}
#     return yt_result

# # Ensure session state for YouTube results and selected video
# if 'yt_result' not in st.session_state:
#     st.session_state['yt_result'] = {}
# if 'selected_video' not in st.session_state:
#     st.session_state['selected_video'] = None

# # Search button action
# if st.button("Search"):
#     if query:
#         st.session_state['yt_result'] = yt_link_videos(query)
#         st.session_state['selected_video'] = None  # Reset the selected video when a new search is made

# # Display search results and download option if there are results
# youtube_links = st.session_state['yt_result']
# if youtube_links:
#     st.write("Generated YouTube Links:")
#     selected_video = st.selectbox("Select a video to download:", options=list(youtube_links.keys()))
#     st.session_state['selected_video'] = selected_video

# # Download the selected video if a selection has been made
# if st.session_state['selected_video']:
#     video_url = youtube_links[st.session_state['selected_video']]
#     if st.button("Download"):
#         with st.spinner('Downloading video...'):
#             video_path = download_video(video_url, resolution_choice, output_path, st.session_state['selected_video'])

#             if video_path:
#                 st.success('Video downloaded successfully!')
#                 st.video(video_path)  # Display the video
#             else:
#                 st.error('Failed to download video.')


## update version ## 

# import streamlit as st
# from pytubefix import YouTube
# import re
# import requests
# import os
# from datetime import datetime
# from pytube.cli import on_progress

# # Streamlit UI
# st.title("YouTube Video Downloader")

# # Create a directory for downloads if it doesn't exist
# output_path = "d:/youtube_video"
# if not os.path.exists(output_path):
#     os.makedirs(output_path)

# # Input for search query
# query = st.text_input("Enter the video name to search on YouTube:")
# resolution_choice = st.selectbox("Select resolution:", ["360p", "720p", "1080p"])

# # Function to download video with progress bar
# def download_video(video_url, resolution, output_path, title):
#     try:
#         yt = YouTube(video_url, on_progress_callback=on_progress)
#         stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
#         if stream:
#             video_filename = f"{title}_{resolution}_video.mp4"
#             video_progress = st.progress(0)  # Initialize progress bar for video

#             def video_progress_callback(stream, chunk, bytes_remaining):
#                 total_size = stream.filesize
#                 bytes_downloaded = total_size - bytes_remaining
#                 percentage_of_completion = bytes_downloaded / total_size
#                 video_progress.progress(int(percentage_of_completion * 100))
                
#             yt.register_on_progress_callback(video_progress_callback)
#             stream.download(output_path=output_path, filename=video_filename)
#             video_progress.progress(100)  # Ensure progress bar completes
#             return os.path.join(output_path, video_filename)
#         else:
#             st.warning(f"No video found for the selected resolution: {resolution}.")
#             return None
#     except Exception as e:
#         st.error(f"Error downloading video: {e}")
#         return None

# # Function to download audio without progress bar
# def download_audio(video_url, output_path, title):
#     try:
#         yt = YouTube(video_url)
#         stream_audio = yt.streams.filter(only_audio=True).first()
#         if stream_audio:
#             audio_filename = f"{title}_audio.mp3"
#             stream_audio.download(output_path=output_path, filename=audio_filename)
#             return os.path.join(output_path, audio_filename)
#         else:
#             st.warning("Audio not found in stream.")
#             return None
#     except Exception as e:
#         st.error(f"An error occurred while downloading audio: {e}")
#         return None

# # Function to merge video and audio using ffmpeg
# def merge_video_audio(video_path, audio_path, output_path, title):
#     try:
#         final_filename = f"{title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
#         final_path = os.path.join(output_path, final_filename)
#         os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}" -y')
#         os.remove(video_path)
#         os.remove(audio_path)
#         return final_path
#     except Exception as e:
#         st.error(f"An error occurred while merging video and audio: {e}")
#         return None

# # Function to search YouTube videos
# def yt_link_videos(query):
#     query = query.replace(' ', '+')
#     search_url = f'https://www.youtube.com/results?search_query={query}'
    
#     try:
#         response = requests.get(search_url)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         st.error(f"Error fetching YouTube search results: {e}")
#         return {}

#     content = response.text
#     video_ids = re.findall(r'videoId":"(.*?)"', content)
#     video_ids = list(set(video_ids))

#     youtube_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids[:5]]
#     yt_result = {YouTube(link).title: link for link in youtube_links}
#     return yt_result

# # Ensure session state for YouTube results and selected video
# if 'yt_result' not in st.session_state:
#     st.session_state['yt_result'] = {}
# if 'selected_video' not in st.session_state:
#     st.session_state['selected_video'] = None

# # Search button action
# if st.button("Search"):
#     if query:
#         st.session_state['yt_result'] = yt_link_videos(query)
#         st.session_state['selected_video'] = None  # Reset the selected video when a new search is made

# # Display search results and download option if there are results
# youtube_links = st.session_state['yt_result']
# if youtube_links:
#     # st.write("Generated YouTube Links:")
#     selected_video = st.selectbox("Select a video to download:", options=list(youtube_links.keys()))
#     st.session_state['selected_video'] = selected_video

# # Download the selected video if a selection has been made
# if st.session_state['selected_video']:
#     video_url = youtube_links[st.session_state['selected_video']]
#     if st.button("Download"):
#         with st.spinner('Downloading video...'):
#             video_path = download_video(video_url, resolution_choice, output_path, st.session_state['selected_video'])
#             audio_path = download_audio(video_url, output_path, st.session_state['selected_video'])

#             if video_path and audio_path:
#                 merged_video_path = merge_video_audio(video_path, audio_path, output_path, st.session_state['selected_video'])
#                 if merged_video_path:
#                     st.success('Video download successfully!')
#                     st.video(merged_video_path)
#                     st.write(f'Downloaded video saved at: {merged_video_path}')
#                 else:
#                     st.error('Failed to merge video and audio.')
#             else:
#                 st.error('Failed to download video or audio. Please check the resolution and try again.')



### update 3.0 version ###
#auto install req
from pipin import install_requirements
install_requirements()

import streamlit as st
from pytubefix import YouTube
import re
import requests
import os
from datetime import datetime
from pytube.cli import on_progress



# Streamlit UI
st.title("YouTube Video Downloader")

# Create a directory for downloads if it doesn't exist
output_path = "d:/youtube_video"
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Input for search query
query = st.text_input("Enter the video name to search on YouTube:")
resolution_choice = st.selectbox("Select resolution:", ["360p", "720p", "1080p"])

# Function to download video with progress bar
def download_video(video_url, resolution, output_path, title):
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        stream = yt.streams.filter(subtype='mp4', res=resolution, only_video=True).first()
        if stream:
            video_filename = f"{title}_{resolution}_video.mp4"
            video_progress = st.progress(0)  # Initialize progress bar for video

            def video_progress_callback(stream, chunk, bytes_remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - bytes_remaining
                percentage_of_completion = bytes_downloaded / total_size
                video_progress.progress(int(percentage_of_completion * 100))
                
            yt.register_on_progress_callback(video_progress_callback)
            stream.download(output_path=output_path, filename=video_filename)
            video_progress.progress(100)  # Ensure progress bar completes
            return os.path.join(output_path, video_filename)
        else:
            st.warning(f"No video found for the selected resolution: {resolution}.")
            return None
    except Exception as e:
        st.error(f"Error downloading video: {e}")
        return None

# Function to download audio without progress bar
def download_audio(video_url, output_path, title):
    try:
        yt = YouTube(video_url)
        stream_audio = yt.streams.filter(only_audio=True).first()
        if stream_audio:
            audio_filename = f"{title}_audio.mp3"
            stream_audio.download(output_path=output_path, filename=audio_filename)
            return os.path.join(output_path, audio_filename)
        else:
            st.warning("Audio not found in stream.")
            return None
    except Exception as e:
        st.error(f"An error occurred while downloading audio: {e}")
        return None

# Function to merge video and audio using ffmpeg
def merge_video_audio(video_path, audio_path, output_path, title):
    try:
        final_filename = f"{title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
        final_path = os.path.join(output_path, final_filename)
        os.system(f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{final_path}" -y')
        os.remove(video_path)
        os.remove(audio_path)
        return final_path
    except Exception as e:
        st.error(f"An error occurred while merging video and audio: {e}")
        return None

# Function to search YouTube videos and filter results
def yt_link_videos(query):
    query = query.replace(' ', '+')
    search_url = f'https://www.youtube.com/results?search_query={query}'
    
    try:
        response = requests.get(search_url)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Error fetching YouTube search results: {e}")
        return {}

    content = response.text
    video_ids = re.findall(r'videoId":"(.*?)"', content)
    video_ids = list(dict.fromkeys(video_ids))  # Remove duplicates while preserving order

    yt_result = {}
    for video_id in video_ids:
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        try:
            video = YouTube(video_url)
            if video.length > 60:  # Exclude videos shorter than 60 seconds
                yt_result[video.title] = video_url
                if len(yt_result) == 5:  # Stop once we have 5 videos
                    break
        except Exception as e:
            st.warning(f"Error processing video: {e}")
    
    return yt_result

# Ensure session state for YouTube results and selected video
if 'yt_result' not in st.session_state:
    st.session_state['yt_result'] = {}
if 'selected_video' not in st.session_state:
    st.session_state['selected_video'] = None

# Search button action
if st.button("Search"):
    if query:
        st.session_state['yt_result'] = yt_link_videos(query)
        st.session_state['selected_video'] = None  # Reset the selected video when a new search is made

# Display search results and download option if there are results
youtube_links = st.session_state['yt_result']
if youtube_links:
    selected_video = st.selectbox("Select a video to download:", options=list(youtube_links.keys()))
    st.session_state['selected_video'] = selected_video

# Download the selected video if a selection has been made
if st.session_state['selected_video']:
    video_url = youtube_links[st.session_state['selected_video']]
    if st.button("Download"):
        with st.spinner('Downloading video...'):
            video_path = download_video(video_url, resolution_choice, output_path, st.session_state['selected_video'])
            audio_path = download_audio(video_url, output_path, st.session_state['selected_video'])

            if video_path and audio_path:
                merged_video_path = merge_video_audio(video_path, audio_path, output_path, st.session_state['selected_video'])
                if merged_video_path:
                    st.success('Video downloaded successfully!')
                    st.video(merged_video_path)
                    st.write(f'Downloaded video saved at: {merged_video_path}')
                else:
                    st.error('Failed to merge video and audio.')
            else:
                st.error('Failed to download video or audio. Please check the resolution and try again.')
