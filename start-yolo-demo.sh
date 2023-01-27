#!/bin/bash

export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT=5001
export NUM_THREADS=32

# Select one of the following
#export VIDEO_SRC='examples/Driving-NYC-360p.mp4'
export VIDEO_SRC='examples/Driving-Vegas-360p.mp4'
#export VIDEO_SRC='examples/3-640x360-600k.mp4'
#export VIDEO_SRC='examples/video-small-640.mp4'
#export VIDEO_SRC='examples/video-test.mp4'
#export VIDEO_SRC='examples/ParisMorningRain.mp4'
#export VIDEO_SRC='https://www.youtube.com/watch?v=1EiC9bvVGnk'

docker compose up yolo-demo
