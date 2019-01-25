# human_motion_forecast_srnn_ros
En|[中文](README_CHINESE.md)

## Summary
   This repository is to realize a human motion predicion experient from paper called "Structural-RNN: Deep Learning on Spatio-Temporal Graphs" in CVPR-2016. S-RNN architecture follows the Spatio-Temporal-graph(st-graph). According to the st-graph, the spine interacts with all the body parts, and the arms and legs interact with each other. The st-graph is automatically transformed to S-RNN.

See their project page for more infomation: [Structural-RNN: Deep Learning on Spatio-Temporal Graphs](http://asheshjain.org/srnn)

## Quickstart
### Requirements
> It is recommended to install python requirements in a virtual environment created by [conda](https://conda.io/docs/).
* ROS (Kinetic Kame on Ubuntu 16.04 or Melodic Morenia on Ubuntu 18.04)
  
  See [the official install guide](http://www.ros.org/install) to learn how to install ROS.
* Python (2.7)
* Theano (>=0.6)
* matplotlib
* Neural Models (https://github.com/asheshjain399/NeuralModels)

### Download dataset and pre-trained models
* [H3.6m](http://www.cs.stanford.edu/people/ashesh/h3.6m.zip)
* [pre-trained models](https://drive.google.com/drive/folders/0B7lfjqylzqmMZlI3TUNUUEFQMXc)
> You may need to create folders to to put this files.

### Build and run the demo
* Clone the project code
  ```bash
  > git clone https://github.com/kafe6/human_motion_forecast_srnn_ros.git src/human_motion_forecast_srnn
  ```
* Build
  ```bash
  > catkin_make catkin_make -DCATKIN_WHITELIST_PACKAGES="human_motion_forecast_srnn" -D-DCMAKE_BUILD_TYPE=Debug
  ```
* Run the forecast node, wait it completely loaded because it may take a long time. "cp_path" is a ros parameter of your checkpoint file path.
  ```bash
  > roslaunch human_motion_forecast_srnn forecast.launch cp_path:=YOUR_CHECKPOINT_PATH/checkpoint.pik
  ```
* Run the publisher after the forecast node has loaded the checkpoint. "ds_path" is a ros parameter of your motion dataset path.
  ```bash
  > roslaunch human_motion_forecast_srnn publisher.launch ds_path:=YOUR_DATASET_PATH/walking_1.txt
  ```
* Run the visualization node to see the predicted result in rviz.
  ```bash
  > roslaunch human_motion_forecast_srnn fc_visualize.launch
  ```
Then you can see rviz run, and one skeletos walking in it.
   
