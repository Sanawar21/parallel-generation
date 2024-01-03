from dotenv import load_dotenv
# from .utils import paths
from utils import paths

import os
import replicate

load_dotenv(paths.env_path)


def __run_test():
    os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE")
    output = replicate.run(
        "musayyab-naveed/new-content-creation:ee8965217c6952261a1464134e14de8f390a7f9f2a7ef3d4fea664bfd954c663",
        input={"input_video": open(paths.input_video, "rb"),
               "voice_name": "josh",
               'VideoTopic': "books",
               'TypeOfContent': "informative",
               'KeyPoints': "books for inspiration",
               }
    )
    print(output)
    with open("output.txt", "w") as file:
        file.write(output)


if __name__ == "__main__":
    __run_test()
