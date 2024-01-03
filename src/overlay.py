from moviepy.editor import VideoClip
from moviepy.editor import VideoClip, VideoFileClip, TextClip, ImageClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import numpy as np
from moviepy.editor import VideoFileClip, VideoClip, CompositeVideoClip, TextClip


def overlay_video_with_text_and_objects(background_path, overlay_path, output_path):
    # Load the background video
    background_clip = VideoFileClip(background_path, audio=False)

    # Load the transparent overlay video
    overlay_clip = VideoFileClip(overlay_path, audio=False)

    # Composite the transparent video with the background
    final_clip = CompositeVideoClip(
        [background_clip, overlay_clip])

    # Write the final video to the output file
    final_clip.write_videofile(
        output_path, codec='libx264', fps=25, threads=os.cpu_count())


def overlay_gif_on_video(video_path, gif_path, output_path):
    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Load transparent GIF
    gif_clip = VideoFileClip(gif_path, has_mask=True)

    # Overlay the GIF onto the video
    result_clip = video_clip.set_mask(gif_clip.to_mask()).set_pos('center')

    # Write the result to the output file
    result_clip.write_videofile(
        output_path, codec="libx264", audio_codec="aac", fps=video_clip.fps)


# Example usage
video_path = 'path/to/your/video.mp4'
gif_path = 'path/to/your/transparent.gif'
output_path = 'path/to/output/result.mp4'

# overlay_gif_on_video("base.mp4", "overlay.gif", "output_video_.mp4")

# Example usage:
# overlay_video_with_text_and_objects(
#     "overlay.gif", "base.mp4", "output_video_.mp4")


def create_transparent_video(output_path, resolution=(640, 480), duration=5, fps=25):
    # Create a VideoClip with a transparent background
    clip = VideoClip(make_frame=lambda t: (255 * (t / duration)
                                           ).astype('uint8')[None, None, None, :], duration=duration)

    # Set the resolution of the video
    clip = clip.set_size(resolution)

    # Save the video with a transparent background
    clip.write_videofile(output_path, codec="libvpx",
                         fps=fps, audio=False, threads=os.cpu_count())


# Example usage
# create_transparent_video("output_transparent.webm",
#                          resolution=(2160, 3840), duration=22)


# Set the duration and size of the video
duration = 22
width, height = (2160, 3840)
fps = 25

# Create a function to generate frames with transparency


def make_frame(t):
    # Calculate the intensity based on time
    intensity = int(255 * (t / duration))

    # Create an RGB image with a gradient
    frame = np.ones((height, width, 3), dtype='uint8') * intensity

    # Set the alpha channel (transparency)
    alpha_channel = np.ones((height, width, 1), dtype='uint8') * intensity
    frame_with_alpha = np.concatenate((frame, alpha_channel), axis=2)

    return frame_with_alpha


# # Create VideoClip with the make_frame function
clip = VideoClip(make_frame=make_frame, duration=duration)
clip.write_videofile("composition.avi", codec='hap_alpha', ffmpeg_params=[
                     '-c:v', 'hap', '-format', 'hap_alpha', '-vf', 'chromakey=black:0.1:0.1'], audio=False, fps=fps)
# # Set the output file with a codec that supports transparency (QuickTime with Animation codec)
# # You can change the file extension to match the desired format
# output_file = "transparent_video.gif"

# # Write the video with the 'ffmpeg' codec (supports transparency)
# # clip.write_videofile(output_file, codec='libx264', fps=fps,
# #                      audio=False, threads=os.cpu_count())
# clip.write_gif(output_file, fps=fps,
#                #  progress_bar=True
#                )
