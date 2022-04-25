# Yolov5-musicscore-local
通过使用Yolov5模型，进行乐谱音符的识别。并在本地电脑上运行


使用步骤：

1.make_voc_dir 生成voc格式的文件夹。只需第一次使用时运行

  VOCdevkt
  
       --VOC2007
           --Annotations
           --JPEGImages
           
2.添加标签和图像至VOCdevkt文件

  xml文件-->Annotations
  image-->JPEGImages
   
3.voc_to_yolo  修改classes/ TRAIN_RATIO/ file path

  在VOC2007文件中生成YOLOLabels文件，存储所有的标记文件
  
    VOCdevkt
       --VOC2007
           --Annotations
           --JPEGImages
           --YOLOLabels
       --images
           --train
           --val
       --labels
           --train
           --val
           
4.data/voc.yaml  train path/ val path/ nc/ name

  train path-->VOCdevkit/images/train/
  val path--> VOCdevkit/images/val/
  nc-->number of classes
  name-->class names
  
5.models/.yaml 修改anchors/nc

5.train  

  weights-->initial weights path
  cfg-->model.yaml path
  data-->data.yaml path
  hyp-->hyperparameters path
  epochs
  batch-size
  
6.runs/train/exp/labels、train_batch、weights

7.detect  weights、source、conf-thres、iou-thres
