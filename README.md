# Yolov5 demo

YOLOv5 is a family of object detection architectures and models
pretrained on the COCO dataset.

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

## Reference
https://github.com/ultralytics/yolov5
