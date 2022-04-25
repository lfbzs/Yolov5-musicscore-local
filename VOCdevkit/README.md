# Yolov5-musicscore-local
Through the use of Yolov5 model, the recognition of musical notes. And run it on your local computer


**Using the step：**

**1.make_voc_dir Generate voc format folder. Run only when first used**

  	VOCdevkt
  
       --VOC2007
           --Annotations
           --JPEGImages
           
**2.Add labels and images to VOCdevkt files**

  	xml文件-->Annotations
  
  	image-->JPEGImages
   
**3.voc_to_yolo**

  	Modify the  classes/ TRAIN_RATIO/ file path

  	YOLOLabels files are generated in VOC2007 files to store all tag files
  
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
           
**4.data/voc.yaml**

	train path/ val path/ nc/ name

  	train path-->VOCdevkit/images/train/
  
  	val path--> VOCdevkit/images/val/
  
  	nc-->number of classes
  
  	name-->class names
  
**5.models/.yaml**

	Modify the  anchors/nc

**6.train**

  	weights-->initial weights path
  
  	cfg-->model.yaml path
  
  	data-->data.yaml path
  
  	hyp-->hyperparameters path
  
  	epochs
  
  	batch-size
  
  
**7.runs/train/exp/labels、train_batch、weights**

**8.detect  weights、source、conf-thres、iou-thres**
