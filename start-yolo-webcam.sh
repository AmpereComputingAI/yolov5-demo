#!/bin/bash

export FLASK_RUN_HOST="0.0.0.0"
export FLASK_RUN_PORT=5000
export NUM_THREADS=32
export HOST_PORT=5010
export VIDEO_SRC=0

cont_name="cont-webcam"
docker compose -p $cont_name up -d app-yolo-live
