# Yolov5 demo

YOLOv5 is a family of object detection architectures and models
pretrained on the COCO dataset.

## Starting the container and running the demo

Login to cloud instance or local server
> $ ssh -i \<key\> user@server

Find the docker image,
> $ docker images | grep yolov5-pytorch-aio-demo

For cloud based environments,
> $ ./start-docker-cloud.sh  
Starting YOLOv5 demo container  
Docker container ID: 592441933d5b  

Webapp and Notebook URLs will be printed,
> Getting Webapp URL ........  
Webapp URL: http://\<ipaddr\>:7860/  
>
> Getting Jupyter Notebook URL ..  
Jupyter Notebook URL: or http://\<ipaddr\>:8888/lab?token=77a18bd0a9c278df710f0b2c83a052ddaa245d7ee9c5b8cd  

For non-cloud environments,  
> $ ./start-docker-local.sh

Open your favorite browser and type in the above URLs.

## Reference
https://github.com/ultralytics/yolov5
