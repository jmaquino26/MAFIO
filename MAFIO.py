import os
import time
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
    while frame_num <= len(frame_list):
        frame = frame_list.popleft()
        media = api.media_upload(utils.get_frame(frame))

        api.update_status(status=f"Miss Americana - Frame {frame[:-4]} "
                          f"out of {frame_list[-1][:-4]}",
                          media_ids=[media.media_id])

        # when tweeted dump the frame into another folder
        utils.record_tweeted_frames(frame)

        # desired sleep time
        time.sleep(15)


if __name__ == '__main__':
    main()
