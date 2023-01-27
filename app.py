from flask import Flask, Response, render_template, redirect
from multiprocessing import Queue
import os, pafy, psutil, re

from display_frames import DisplayFrames
from video_stream import VideoStream
from process_frames import ProcessFrames
from util import LOGGER

if __name__ == '__main__':
    def setup():
        nthreads = os.environ['NUM_THREADS']
        os.environ['AIO_NUM_THREADS'] = nthreads
        os.environ['OMP_NUM_THREADS'] = nthreads

        framesq = Queue(64)
        displayq = Queue()
        LOGGER.info(f'created framesq: {framesq}')
        LOGGER.info(f'created displayq: {displayq}')

        src = get_url()
        stream = VideoStream(framesq, src)
        process_frames = ProcessFrames(framesq, displayq)
        display_frames = DisplayFrames(displayq)

        return stream, process_frames, display_frames

    #stream, process_frames, display_frames = setup()

    def get_url():
        src = os.environ['VIDEO_SRC']
        if 'https://www.youtube.com' in src: # Youtube URL
            v = pafy.new(src)
            streams = v.videostreams if v.videostreams else v.streams
            t = [ i for i, y in enumerate(streams) if re.search('640', y.resolution) and re.search('mp4', y.extension) ]
            src = streams[t[0]].url
            print(f'+++ stream mediatype: {streams[t[0]].mediatype} resolution: {streams[t[0]].resolution}')
            print(f'{src}')

        return src

    app = Flask(__name__)
    print(f'created flask app: {app}')

    @app.route('/<app_id>')
    def index(app_id):
        return render_template('index.html', appid=app_id)

    @app.route("/<app_id>/yolo")
    def yolo(app_id):
        LOGGER.info(f'Flask /yolo called')
        global stream, process_frames, display_frames
        stream, process_frames, display_frames = setup()
        stream.start()
        process_frames.start()
        display_frames.start()

        return Response(display_frames.display(), mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route("/stop")
    def yolo_reset():
        LOGGER.info(f'Flask /reset called')
        stream.stop()
        process_frames.stop()
        display_frames.stop()
        return f'App stop called'
        #return redirect('/')

    try:
        flask_host = os.environ['FLASK_RUN_HOST']
        flask_port = os.environ['FLASK_RUN_PORT']
        app.run(host=flask_host, port=flask_port, debug=False, use_reloader=False)
    except Exception as err:
        print(f'+++ Exception: Flask: {err}')