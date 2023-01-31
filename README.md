# Yolov5 demo

YOLOv5 is a family of object detection architectures and models
pretrained on the COCO dataset.

This demo runs YOLOv5 object detection and classification ML inference 
using provided source video and outputs it to your browser at a smooth 30 frames per second. 
with bounding boxes showing classification confidence and inference latency in milliseconds. We may also add 60FPS examples.

![MedleyYOLO-jutah](https://user-images.githubusercontent.com/8238588/215856385-28b084ad-08f7-4a65-82be-a558d7d3203a.gif)

## Download the demo repository
> $ git clone https://github.com/AmpereComputingAI/yolov5-demo.git  
\$ cd yolov5-demo


## Install docker
Follow the instructions from this link,
https://docs.docker.com/engine/install/ubuntu/

## Install compose plugin
Follow the instructions from this link,
https://docs.docker.com/compose/install/linux/#install-using-the-repository

## Open the required ports
> sudo firewall-cmd --zone public --permanent --add-port \<port>/tcp  
sudo firewall-cmd --reload

## Start the demo
start-yolo-demo.sh contains few video sources.  Please select the video source and then run the script
> $ ./start-yolo-demo.sh

Console log should like this,
> yolo-demo  |  * Running on all addresses (0.0.0.0)  
yolo-demo  |  * Running on http://127.0.0.1:5001  
yolo-demo  |  * Running on http://10.0.88.232:5001

Open your favorite browser and type in the following URL.
> http://127.0.0.1:5001/app

## Stop the demo
> $ ./stop-yolo-demo.sh

## Select another video file as source
Edit start-yolodemo.sh to select a different video source file by uncommenting it.

## Reference
https://github.com/ultralytics/yolov5
