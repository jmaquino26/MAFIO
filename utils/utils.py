import os

MISS_AMERICANA_FRAMES_FOLDER = 'C:\\Users\\franc\\OneDrive\\Pictures\\MissAmericana'  # noqa
CWD = os.getcwd()
PROGRESS_FOLDER = os.path.join(CWD, 'saved_progress')
RECORDED_FRAMES_FILE = os.path.join(PROGRESS_FOLDER, 'recorded_frames.txt')


def list_all_frames(path: str) -> list:
    """List all photos inside the path"""
    return os.listdir(path)


def _ensure_folder():
    """Ensure folder and files are created"""
    if not os.path.exists(PROGRESS_FOLDER):
        os.mkdir(PROGRESS_FOLDER)


def record_tweeted_frames(frame_number) -> None:

    _ensure_folder()

    with open(RECORDED_FRAMES_FILE, 'a') as f:
        f.write(str(frame_number))
        f.write('\n')


def get_last_recorded_tweet():
    _ensure_folder()
    frames = []
    with open(RECORDED_FRAMES_FILE) as f:

        for num in f.read().split('\n'):
            frames.append(num)
    return frames[-2]


if __name__ == '__main__':
    for frame in list_all_frames(MISS_AMERICANA_FRAMES_FOLDER):
        record_tweeted_frames(str(frame[:-4]))