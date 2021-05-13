import os
import time
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

    # WHILE TRUE:
    frame_list = utils.list_all_frames()

    frame_num = 0

    while frame_num == len(frame_list):
        frame = frame_list.popleft()

        api.update_status(f"Miss Americana - Frame {frame[:-4]} "
                          f"out of {frame_list[-1][:-4]}",
                          # upload the image
                          api.media_upload(utils.get_frame(frame)))

        # when tweeted dump the frame into another folder
        utils.record_tweeted_frames(frame)

        # desired sleep time
        time.sleep(900)




if __name__ == '__main__':
    main()
