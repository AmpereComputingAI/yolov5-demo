#!/bin/bash

export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT=5001
export NUM_THREADS=48

# Select one of the following
export VIDEO_SRC='examples/Driving-NYC-360p-jutah.mp4'
#export VIDEO_SRC='examples/Driving-Vegas-360p-jutah.mp4'
#export VIDEO_SRC='examples/Driving-Medley-jutah.mp4'
#export VIDEO_SRC='examples/video-small-640.mp4'
#export VIDEO_SRC='examples/ParisMorningRain-jutah.mp4'
#export VIDEO_SRC='https://www.youtube.com/watch?v=1EiC9bvVGnk'

docker compose up app-yolo-live
