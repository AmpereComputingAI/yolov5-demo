# syntax=docker/dockerfile
FROM aio-pytorch-1.11.0:1.3.0

ENV FLASK_RUN_HOST=${FLASK_RUN_HOST}
ENV FLASK_RUN_PORT=${FLASK_RUN_PORT}
ENV NUM_THREADS=${NUM_THREADS}
ENV VIDEO_SRC=${VIDEO_SRC}

WORKDIR /workspace/yolo-flask

RUN <<EOF
apt update -y
apt install -y libgl-dev libglib2.0-0 ffmpeg
EOF

RUN pip uninstall -y opencv-contrib-python-headless

RUN pip install -U pip
RUN pip install --no-cache-dir wheel "yolov5<6.2" flask
RUN pip install --no-cache-dir pafy "youtube-dl==2020.12.2"

COPY . .

#ENTRYPOINT ["nohup", "python", "app-flask.py", "&"]
#ENTRYPOINT ["/bin/bash", "-c"]
#ENTRYPOINT ["/bin/bash", "-l"]
#CMD ["python", "app-flask.py"]

RUN apt-get clean

ENTRYPOINT ["python"]
CMD ["app.py"]