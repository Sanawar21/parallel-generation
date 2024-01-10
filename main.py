from src.utils import status, start_vps, close_vps, restore_dirs, paths
from src import audio, video, captions, zoom, b_rolls, content
from src import client
from src.replicate_api import run_test

from moviepy.editor import VideoFileClip
import os

if __name__ == "__main__":
    # restore_dirs()
    # description = None
    # voice = "josh"
    # workflow = {
    #     'VideoTopic': "books",
    #     'TypeOfContent': "informative",
    #     'KeyPoints': "books for inspiration",
    # }
    # # try:
    # content.process_workflow(workflow)
    # status.set(status.generating_audio)
    # if voice not in audio.list_voices().keys():
    #     audio.clone(voice, description)

    # audio.generate(voice)
    # captions.generate_srt()
    # status.set(status.generating_lipsync)

    # session_id = client.upload_files()
    run_test("session_id")

    # video.generate_video()
    # status.set(status.enhancing_video)
    # TODO: use client
    # video.enhance_video()
    # status.set(status.zooming_video)
    # zoomed = zoom.zoom_video_at_intervals()
    # status.set(status.adding_brolls)
    # b_rolled = b_rolls.add_b_rolls(zoomed)
    # status.set(status.generating_subtitles)
    # captioned = captions.add_to_video(b_rolled)
    # status.set(status.combining_audio_video)
    video.merge_audio_and_video(video=VideoFileClip(str(paths.enhanced_video)))
    status.set(status.done)
    # except Exception as e:
    #     return e
