import cv2 as cv
import queue, time
from dataclasses import dataclass
from multiprocessing import Queue
from util import FPS, LOGGER
from PIL import Image

@dataclass
class DisplayFrames:
    displayq: Queue
    stopped: bool = True

    def start(self):
        LOGGER.info(f'Entering {__name__}')
        self.stopped = False

    def display(self):
        LOGGER.info(f'Entering {__name__}')
        while not self.stopped:
            try:
                frame = self.displayq.get_nowait()
                time.sleep(FPS) # Move all the sleep to finally ?
                #_, frame = cv.imencode('.jpeg', frame)
                yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
            except queue.Empty as err:
                LOGGER.debug(f'displayq: get: {err}')
                time.sleep(FPS)
            except Exception as err:
                LOGGER.debug(f'display_frames: {err}')
                time.sleep(FPS)

    def stop(self):
        LOGGER.info(f'display_frames stop called')
        self.stopped = True
        time.sleep(1)
        self.clearq()
        LOGGER.info(f'displayq: size: {self.displayq.qsize()}')


    def clearq(self):
        ## clear display queue
        while True:
            try:
                frame = self.displayq.get_nowait()
            except queue.Empty as err:
                qsize = self.displayq.qsize()
                LOGGER.info(f'displayq: empty {qsize}')
                if qsize == 0:
                    break