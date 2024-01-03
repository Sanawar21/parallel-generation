import subprocess
import os

subprocess.run(
    ["git", "clone", "https://github.com/linto-ai/whisper-timestamped"])
os.chdir("whisper-timestamped")
subprocess.run(["python3", "setup.py", "install"])
subprocess.run(["pip3", "install", "openai-whisper==20231117",
               "ffmpeg-python", "dtw-python", "moviepy", "fuzzywuzzy"])
os.chdir("..")
os.rename("whisper-timestamped", "whisper_timestamped")
with open("whisper_timestamped/__init__.py", "w") as file:
    pass
