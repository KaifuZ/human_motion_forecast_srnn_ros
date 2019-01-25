# human_motion_forecast_srnn_ros
[En](README.md)|中文

## 摘要
   该库根据2016年的CVPR会议中的“Structural-RNN: Deep Learning on Spatio-Temporal Graphs”一文中实现人体运动预测的实验。S-RNN结构时空图，简称为ST图。根据ST图，人体骨骼与身体所有部位相互作用，手臂和腿相互作用。实验中将ST图自动转换为S-RNN。
更多信息请参见他们的项目页面：【Structural-RNN: Deep Learning on Spatio-Temporal Graphs】（http://asheshjain.org/srnn）
## 快速上手
### 依赖与要求
> 建议使用[conda](https://conda.io/docs/)创建虚拟环境，在虚拟环境中安装python依赖。

* ROS (Kinetic Kame on Ubuntu 16.04 or Melodic Morenia on Ubuntu 18.04)
  
  访问[官方安装教程](http://www.ros.org/install)了解如何安装ROS。
* Python (2.7)
* Theano (>=0.6)
* matplotlib
* Neural Models (https://github.com/asheshjain399/NeuralModels)

### 下载数据集与预训练模型

* [H3.6m](http://www.cs.stanford.edu/people/ashesh/h3.6m.zip)
* [pre-trained models](https://drive.google.com/drive/folders/0B7lfjqylzqmMZlI3TUNUUEFQMXc)

> 你可能需要创建一些目录来存放这些文件。

### 编译与运行示例程序
* 克隆项目的代码
  ```bash
  > git clone https://github.com/kafe6/human_motion_forecast_srnn_ros.git src/human_motion_forecast_srnn
  ```
* 编译
  ```bash
  > catkin_make catkin_make -DCATKIN_WHITELIST_PACKAGES="human_motion_forecast_srnn" -D-DCMAKE_BUILD_TYPE=Debug
  ```
*运行预测节点(forecast node)，等待它完全加载，因为它可能需要很长时间。”cp_path“是一个ROS参数,是checkpoint文件的路径。
  ```bash
  > roslaunch human_motion_forecast_srnn forecast.launch cp_path:=YOUR_CHECKPOINT_PATH/checkpoint.pik
  ```
* 在forecast节点加载checkpoint后运行发布节点(publisher node)。““ds_path”是dataset路径的ROS参数。
  ```bash
  > roslaunch human_motion_forecast_srnn publisher.launch ds_path:=YOUR_DATASET_PATH/walking_1.txt
  ```
* 运行可视化节点(visualization node)来在rviz上观察预测的结果。  ```bash
  > roslaunch human_motion_forecast_srnn fc_visualize.launch
  ```
然后你就可以看到一个人体骨架在rviz上运动。   
