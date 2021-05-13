import os
from utils.utils import MISS_AMERICANA_FRAMES_FOLDER, list_all_frames
import tweepy

# load environmental variables
from dotenv import load_dotenv
from utils import utils

load_dotenv()


# API KEYS
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def main():
    """Main function"""

    # THIS IS WHERE THE WHILE LOOP IS GONNA RUN!

    # implement a queue

    # WHILE TRUE:
    frame_list = utils.list_all_frames()

    for frame in frame_list:

        api.update_status(f"Miss Americana - Frame {frame} out of {frame_list[-1]}", api.media_upload())

        # desired sleep time

        # mb add this to line 34

        # when tweeted dump the frame into another folder
        utils.record_tweeted_frames(frame_list.popleft())


    # API.UPDATE_STATUS()

    # THEN 
    pass


if __name__ == '__main__':
    main()

x = list_all_frames(MISS_AMERICANA_FRAMES_FOLDER)
i = 0
print(x)
# while i <= len(x):
    # api.update_status("Miss Americana - Frame XXXXX of XXXXX", api.media_upload())

