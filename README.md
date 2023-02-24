# Yolov5 demo

YOLOv5 is a family of object detection architectures and models
pretrained on the COCO dataset.

This demo for Ampere Altra/Max systems runs YOLOv5 object detection and classification ML inference 
using provided source video and outputs it to your browser at a smooth 30 frames per second. 
with bounding boxes showing classification confidence and inference latency in milliseconds. We may also add 60FPS examples.

![MedleyYOLO-jutah](https://user-images.githubusercontent.com/8238588/215856385-28b084ad-08f7-4a65-82be-a558d7d3203a.gif)

## Download the demo repository
```shell
$ git clone https://github.com/AmpereComputingAI/yolov5-demo.git
$ cd yolov5-demo
```


## Install docker
Follow the instructions from this link,
https://docs.docker.com/engine/install/ubuntu/

## Install compose plugin
Follow the instructions from this link,
https://docs.docker.com/compose/install/linux/#install-using-the-repository

## Open the required ports
```shell
$ sudo firewall-cmd --zone public --permanent --add-port 5000-5010/tcp
$ sudo firewall-cmd --reload
```

## Start the demo
There are two start scripts provided, one (start-yolo-cpu.sh) to run on CPU and the other one (start-yolo-gpu.sh) to run on GPU.  Please select the video source (on the start script) and then run the script

```shell
$ ./start-yolo-cpu.sh
[+] Running 2/2
 ⠿ Network cont-1_default            Created                                               0.3s
 ⠿ Container cont-1-app-yolo-live-1  Started                                               0.5s
```

```docker
$ docker ps
CONTAINER ID   IMAGE                                            COMMAND           CREATED         STATUS         PORTS                                       NAMES
d220bd759eb5   ghcr.io/amperecomputingai/yolo-live-demo:1.2.7   "python app.py"   5 seconds ago   Up 4 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   cont-1-app-yolo-live-1
```

Open your favorite browser and type in the following URL.
```
http://<server-IP>:5000/app
```

## Stop the demo
There are two stop scripts provided, one (stop-yolo-cpu.sh) to stop the CPU container and the other one (stop-yolo-gpu.sh) to stop the GPU container.  Please use the appropriate one.
```shell
$ ./stop-yolo-cpu.sh
```

## Select another video file as source
Edit start-yolo-cpu.sh (or start-yolo-gpu.sh) to select a different video source file by uncommenting it.

## Reference
https://github.com/ultralytics/yolov5
