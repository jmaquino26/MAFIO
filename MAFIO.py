import os

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

    while True:
        for frame in frame_list:

            api.update_status()

            # desired sleep time

            # mb add this to line 34

            # when tweeted dump the frame into another folder
            utils.record_tweeted_frames(frame_list.popleft())


    # API.UPDATE_STATUS()

    # THEN 
    pass


if __name__ == '__main__':
    main()
