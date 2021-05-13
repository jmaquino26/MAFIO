import os
import shutil

from collections import deque

# CONSTANTS
MISS_AMERICANA_FRAMES_FOLDER = 'C:\\Users\\Wetpa\\Desktop\\a\\capture'  # noqa
TWEETED_FRAMES_FOLDER = 'C:\\Users\\franc\\OneDrive\\Pictures\\MissAmericanaTweetedFrames'  # noqa


# MISS_AMERICANA_FRAMES_FOLDER = 'D:\\Captures'  # noqa

CWD = os.getcwd()
PROGRESS_FOLDER = os.path.join(CWD, 'saved_progress')
RECORDED_FRAMES_FILE = os.path.join(PROGRESS_FOLDER, 'recorded_frames.txt')


def list_all_frames() -> deque:
    """List all photos inside the path"""
    return deque(os.listdir(MISS_AMERICANA_FRAMES_FOLDER))


def _ensure_folder():
    """Ensure folder and files are created"""
    if not os.path.exists(PROGRESS_FOLDER):
        os.mkdir(PROGRESS_FOLDER)

    if not os.path.exists(TWEETED_FRAMES_FOLDER):
        os.mkdir(TWEETED_FRAMES_FOLDER)


def record_tweeted_frames(frame_number) -> None:

    _ensure_folder()

    with open(RECORDED_FRAMES_FILE, 'a') as f:
        if isinstance(frame_number, list):

            for frame in frame_number:  # (s)
                num, _ = os.path.splitext(frame)
                f.write(str(num))
                f.write('\n')
        else:
            f.write(str(frame_number))
            f.write('\n')

    # moves the frame to other folder when finished tweeting
    # so it will not load/list the frames again from 0000
    shutil.move(f'{MISS_AMERICANA_FRAMES_FOLDER}\\{frame_number}',
                f'{TWEETED_FRAMES_FOLDER}\\{frame_number}')


def recorded_tweet_list() -> list:
    """Returns the list of frame numbers that's already been tweeted
    NOTE: the last index is always an empty string ('')

    Returns:
        list: list of frames in the `RECORDED_FRAMES_FILE: CONSTANT`
    """
    with open(RECORDED_FRAMES_FILE) as f:
        frames = [frame for frame in f.read().split('\n')]
    return frames


def get_last_recorded_tweet():
    """Gets the last Recorded Tweet

    Returns:
        str: Returns the last/`index[-2]` of `recorded_tweet_list`
    """
    _ensure_folder()
    frames = recorded_tweet_list()
    return frames[-2]


if __name__ == '__main__':
    frames = list_all_frames()
    for frame in frames:
        print(frame)