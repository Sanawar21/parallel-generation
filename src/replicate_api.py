from dotenv import load_dotenv
from .utils import paths
# from utils import paths

import os
import replicate

load_dotenv(paths.env_path)


def run_test(session_id):
    os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE")
    output = replicate.run(
        "musayyab-naveed/parallel-generation:9154628832a8c0eff65ed69cdd6b45ca05092ecf83d33308796758360ffd56eb",
        input={
            "session_id": session_id,
        }
    )
    print(output)
    with open("output.txt", "w") as file:
        file.write(output)


if __name__ == "__main__":
    run_test()
