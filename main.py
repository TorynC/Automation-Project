
import logging
import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
videos = "C:/Users/PC/OneDrive/Desktop/Media/Video"
images = "C:/Users/PC/OneDrive/Desktop/Media/Images"
audio = "C:/Users/PC/OneDrive/Desktop/Media/Audio"
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # fetching the list of all the files
        files = os.listdir(origin)

        # moves files of each file type to the specific folder
        for f in files:
            if (f.lower().endswith('png') or f.lower().endswith('jpg') or f.lower().endswith('webp')
                    or f.lower().endswith('jpeg')):
                shutil.move(os.path.join(origin, f), os.path.join(images, f))
                logging.info("File sorted: " + f)
            elif f.lower().endswith('mp3'):
                shutil.move(os.path.join(origin, f), os.path.join(audio, f))
                logging.info("File sorted: " + f)
            elif f.lower().endswith('mp4'):
                shutil.move(os.path.join(origin, f), os.path.join(videos, f))
                logging.info("File sorted: " + f)
if __name__ == "__main__":
    origin = "C:/Users/PC/Downloads"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=origin, recursive=False)
    observer.start()
    # creates the directories needed
    try:
        os.makedirs("C:/Users/PC/OneDrive/Desktop/Media/Video")
        os.makedirs("C:/Users/PC/OneDrive/Desktop/Media/Images")
        os.makedirs("C:/Users/PC/OneDrive/Desktop/Media/Audio")
    except FileExistsError:
        pass
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
    except Exception as e:
        logging.error("An error occurred: " + str(e))
