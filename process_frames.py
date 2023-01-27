import cv2 as cv
import queue, time
from dataclasses import dataclass
from multiprocessing import Process, Queue
from util import FPS, LOGGER
from yolov5 import YOLOv5

@dataclass
class ProcessFrames:
    framesq: Queue
    displayq: Queue
    ps: object = None
    stopped: bool = True

    def start(self):
        LOGGER.info(f'Entering {__name__}')
        self.ps = Process(group=None, target=self.process_frames, daemon=True)
        self.stopped = False
        self.ps.start()
        #self.ps.join()

    def process_frames(self):
        yolo = YOLOv5('yolov5n-frozen-640.torchscript', 'cpu')
        times = []
        while not self.stopped:
            try:
                frame = self.framesq.get_nowait()
                t = time.time()
                out = yolo.predict(frame).render()
                times.append(time.time() - t)
                times = times[-20:] # Rolling 20

                inf_time = sum(times) / len(times) * 1000
                #inf_time = 20
                frame = cv.putText(out[0], f'Latency: {inf_time:.1f} msec', (0, 30),
                    cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

                #_, frame = cv.imencode('.jpeg', out[0])
                _, frame = cv.imencode('.jpeg', frame)
                self.displayq.put_nowait(frame)

            except queue.Empty as err:
                LOGGER.debug(f'framesq: get: {err}')
                time.sleep(FPS)

            except queue.Full as err:
                LOGGER.debug(f'displayq: put: {err}')
                time.sleep(FPS)

            except Exception as err:
                LOGGER.debug(f'process_frames: {err}')
                time.sleep(FPS)

    def stop(self):
        LOGGER.info(f'process_frames stop called')
        self.stopped = True
        time.sleep(1)
        self.clearq()
        #self.ps.join()
        LOGGER.info(f'framesq: size: {self.framesq.qsize()}')

    def clearq(self):
        ## clear display queue
        while True:
            try:
                frame = self.framesq.get_nowait()
            except queue.Empty:
                qsize = self.framesq.qsize()
                LOGGER.info(f'framesq: empty {qsize}')
                if qsize == 0:
                    break