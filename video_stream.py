import cv2 as cv
import queue, time
from dataclasses import dataclass
from multiprocessing import Process, Queue
from util import FPS, LOGGER

@dataclass
class VideoStream:
    framesq: Queue
    src: str
    stream: object = None
    ps: object = None
    stopped: bool = True

    def start(self):
        self.ps = Process(target=self.get, daemon=True)
        self.stopped = False
        self.ps.start()
        #self.ps.join()

    def get(self):
        #print(f'Entering {__name__}', flush=True)
        self.stream = cv.VideoCapture(self.src)
        self.stream.set(cv.CAP_PROP_BUFFERSIZE, 3)
        while not self.stopped:
            try:
                ret, frame = self.stream.read()
                if not ret:
                    print(f'Can"t receive frame (stream end?).  Exiting...')
                    break
                self.framesq.put_nowait(frame)
                time.sleep(FPS)

            except queue.Full as err:
                LOGGER.debug(f'framesq: put: {err}')
                time.sleep(FPS)

            except Exception as err:
                LOGGER.debug(f'get_video: other: {err}')
                time.sleep(FPS)


    def stop(self):
        LOGGER.info(f'video_stream stop called')
        self.stopped = True
        time.sleep(1)
        try:
            self.stream.release()
            time.sleep(1)
            self.clearq()
            #self.ps.join()
        except:
            pass

    def clearq(self):
        ## clear the queue
        pass