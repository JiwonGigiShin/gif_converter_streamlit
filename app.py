import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

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
            try:
                # Save the uploaded file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_file_path = temp_file.name

                # Load video using moviepy from the temp file path
                video_clip = VideoFileClip(temp_file_path)

                # Resize video to 720x1280 or compatible size
                resized_clip = video_clip.resize(0.1)

                # Set the GIF file path
                gif_path = temp_file_path.split('.')[0] + '_resized.gif'

                # Convert video to GIF
                resized_clip.write_gif(gif_path)

                st.success("Conversion Successful!")
                st.write(f"GIF saved as: {gif_path}")

                # Display the GIF
                st.image(gif_path)

            except Exception as e:
                st.error(f"An error occurred during the conversion: {e}")
else:
    st.info("Please upload a video file.")
