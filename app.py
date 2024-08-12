# streamlit app for gif converter
import streamlit as st
from moviepy.editor import VideoFileClip

# App title
st.title("Video to GIF Converter")

# Upload video
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    # Display the uploaded video
    st.video(uploaded_file)

    # Create a button to convert video to GIF
    if st.button("Convert to GIF"):
        with st.spinner('Converting...'):
            # Load video using moviepy
            video_clip = VideoFileClip(uploaded_file.name)
            st.markdown(uploaded_file.name)
            # Set the GIF file path

            resized_clip = video_clip.resize(height=720)
            gif_path = uploaded_file.name.split('.')[0] + '_resized.gif'

            # Convert video to GIF (dummy conversion here)
            video_clip.write_gif(gif_path)

            st.success("Conversion Successful!")
            st.write(f"GIF saved as: {gif_path}")

            # Display the GIF
            st.image(gif_path)

else:
    st.info("Please upload a video file.")
