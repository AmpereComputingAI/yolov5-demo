#!/bin/bash

# Select one of the following
#export VIDEO_SRC='examples/Driving-NYC-360p-jutah.mp4'
#export VIDEO_SRC='examples/Driving-Vegas-360p-jutah.mp4'
#export VIDEO_SRC='examples/Driving-Medley-jutah.mp4'
#export VIDEO_SRC='examples/video-small-640.mp4'
#export VIDEO_SRC='examples/ParisMorningRain-jutah.mp4'
#export VIDEO_SRC='https://www.youtube.com/watch?v=1EiC9bvVGnk'

export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT=5000
export NUM_THREADS=32
export HOST_PORT=5000
export VIDEO_SRC='examples/Driving-NYC-360p-jutah.mp4'

cont_name="cont-1"
docker compose -p $cont_name up -d app-yolo-live
