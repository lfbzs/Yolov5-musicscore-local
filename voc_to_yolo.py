import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
from shutil import copyfile



classes=[
    'Sharp',
    'Flat',
    'Natural',
    'Gclef',
    'Fclef',
    'Cclef',
    'TimeSig',
    'Rests1',
    'Rests2',
    'Rests4',
    'Rests8',
    'Rests16',
    'Rests32',
    'Rests64',
    'Rests128',
    'Bass',
    'Guit',
    'Tpt',
    'Hn',
    'Tbn',
    'Tba',
    'Fl',
    'Ob',
    'Cl',
    'Bsn',
    'Vln',
    'Vla',
    'Vlc',
    'Pno',
    'Wh',
    's',
    'm',
    'Trb',
    'p',
    'f',
    'Sax',
    'Hrp',
    'Cb',
    'Rec',
    '1_-10',
    '1_-9',
    '1_-8',
    '1_-7',
    '1_-6',
    '1_-5',
    '1_-4',
    '1_-3',
    '1_-2',
    '1_-1',
    '1_0',
    '1_1',
    '1_2',
    '1_3',
    '1_4',
    '1_5',
    '1_6',
    '1_7',
    '1_8',
    '1_9',
    '1_10',
    '1_11',
    '1_12',
    '1_13',
    '1_14',
    '1_15',
    '1_16',
    '1_17',
    '1_18',
    '1_19',
    '1_20',
    '2_-10',
    '2_-9',
    '2_-8',
    '2_-7',
    '2_-6',
    '2_-5',
    '2_-4',
    '2_-3',
    '2_-2',
    '2_-1',
    '2_0',
    '2_1',
    '2_2',
    '2_3',
    '2_4',
    '2_5',
    '2_6',
    '2_7',
    '2_8',
    '2_9',
    '2_10',
    '2_11',
    '2_12',
    '2_13',
    '2_14',
    '2_15',
    '2_16',
    '2_17',
    '2_18',
    '2_19',
    '2_20',
    '4_-10',
    '4_-9',
    '4_-8',
    '4_-7',
    '4_-6',
    '4_-5',
    '4_-4',
    '4_-3',
    '4_-2',
    '4_-1',
    '4_0',
    '4_1',
    '4_2',
    '4_3',
    '4_4',
    '4_5',
    '4_6',
    '4_7',
    '4_8',
    '4_9',
    '4_10',
    '4_11',
    '4_12',
    '4_13',
    '4_14',
    '4_15',
    '4_16',
    '4_17',
    '4_18',
    '4_19',
    '4_20',
    '8_-10',
    '8_-9',
    '8_-8',
    '8_-7',
    '8_-6',
    '8_-5',
    '8_-4',
    '8_-3',
    '8_-2',
    '8_-1',
    '8_0',
    '8_1',
    '8_2',
    '8_3',
    '8_4',
    '8_5',
    '8_6',
    '8_7',
    '8_8',
    '8_9',
    '8_10',
    '8_11',
    '8_12',
    '8_13',
    '8_14',
    '8_15',
    '8_16',
    '8_17',
    '8_18',
    '8_19',
    '8_20',
    '16_-10',
    '16_-9',
    '16_-8',
    '16_-7',
    '16_-6',
    '16_-5',
    '16_-4',
    '16_-3',
    '16_-2',
    '16_-1',
    '16_0',
    '16_1',
    '16_2',
    '16_3',
    '16_4',
    '16_5',
    '16_6',
    '16_7',
    '16_8',
    '16_9',
    '16_10',
    '16_11',
    '16_12',
    '16_13',
    '16_14',
    '16_15',
    '16_16',
    '16_17',
    '16_18',
    '16_19',
    '16_20',
    '32_-10',
    '32_-9',
    '32_-8',
    '32_-7',
    '32_-6',
    '32_-5',
    '32_-4',
    '32_-3',
    '32_-2',
    '32_-1',
    '32_0',
    '32_1',
    '32_2',
    '32_3',
    '32_4',
    '32_5',
    '32_6',
    '32_7',
    '32_8',
    '32_9',
    '32_10',
    '32_11',
    '32_12',
    '32_13',
    '32_14',
    '32_15',
    '32_16',
    '32_17',
    '32_18',
    '32_19',
    '32_20',
    '64_-10',
    '64_-9',
    '64_-8',
    '64_-7',
    '64_-6',
    '64_-5',
    '64_-4',
    '64_-3',
    '64_-2',
    '64_-1',
    '64_0',
    '64_1',
    '64_2',
    '64_3',
    '64_4',
    '64_5',
    '64_6',
    '64_7',
    '64_8',
    '64_9',
    '64_10',
    '64_11',
    '64_12',
    '64_13',
    '64_14',
    '64_15',
    '64_16',
    '64_17',
    '64_18',
    '64_19',
    '64_20',
    '128_-6',
    '128_-5',
    '128_-4',
    '128_-3',
    '128_-2',
    '128_-1',
    '128_0',
    '128_1',
    '128_2',
    '128_3',
    '128_4',
    '128_5',
    '128_6',
    '128_7',
    '128_8',
    '128_9',
    '128_10',
    '128_11',
    '128_12',
    '128_13',
    '128_14',
    '128_15',
    '128_16',
    '128_17',
    '128_18',
]

TRAIN_RATIO = 90


def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('VOCdevkit/VOC2007/Annotations/%s.xml' % image_id,'rb')
    out_file = open('VOCdevkit/VOC2007/YOLOLabels/%s.txt' % image_id, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()


wd = os.getcwd()
wd = os.getcwd()
data_base_dir = os.path.join(wd, "VOCdevkit/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)
work_sapce_dir = os.path.join(data_base_dir, "VOC2007/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)
annotation_dir = os.path.join(work_sapce_dir, "Annotations/")
if not os.path.isdir(annotation_dir):
    os.mkdir(annotation_dir)
clear_hidden_files(annotation_dir)
image_dir = os.path.join(work_sapce_dir, "JPEGImages/")
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)
clear_hidden_files(image_dir)
yolo_labels_dir = os.path.join(work_sapce_dir, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
    os.mkdir(yolo_labels_dir)
clear_hidden_files(yolo_labels_dir)
yolov5_images_dir = os.path.join(data_base_dir, "images/")
if not os.path.isdir(yolov5_images_dir):
    os.mkdir(yolov5_images_dir)
clear_hidden_files(yolov5_images_dir)
yolov5_labels_dir = os.path.join(data_base_dir, "labels/")
if not os.path.isdir(yolov5_labels_dir):
    os.mkdir(yolov5_labels_dir)
clear_hidden_files(yolov5_labels_dir)
yolov5_images_train_dir = os.path.join(yolov5_images_dir, "train/")
if not os.path.isdir(yolov5_images_train_dir):
    os.mkdir(yolov5_images_train_dir)
clear_hidden_files(yolov5_images_train_dir)
yolov5_images_test_dir = os.path.join(yolov5_images_dir, "val/")
if not os.path.isdir(yolov5_images_test_dir):
    os.mkdir(yolov5_images_test_dir)
clear_hidden_files(yolov5_images_test_dir)
yolov5_labels_train_dir = os.path.join(yolov5_labels_dir, "train/")
if not os.path.isdir(yolov5_labels_train_dir):
    os.mkdir(yolov5_labels_train_dir)
clear_hidden_files(yolov5_labels_train_dir)
yolov5_labels_test_dir = os.path.join(yolov5_labels_dir, "val/")
if not os.path.isdir(yolov5_labels_test_dir):
    os.mkdir(yolov5_labels_test_dir)
clear_hidden_files(yolov5_labels_test_dir)

train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')
list_imgs = os.listdir(image_dir)  # list image_one files
prob = random.randint(1, 100)
print("Probability: %d" % prob)
for i in range(0, len(list_imgs)):
    path = os.path.join(image_dir, list_imgs[i])
    if os.path.isfile(path):
        image_path = image_dir + list_imgs[i]
        voc_path = list_imgs[i]
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
        (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
        annotation_name = nameWithoutExtention + '.xml'
        annotation_path = os.path.join(annotation_dir, annotation_name)
        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(yolo_labels_dir, label_name)
    prob = random.randint(1, 100)
    print("Probability: %d" % prob)
    if (prob < TRAIN_RATIO):  # train dataset
        if os.path.exists(annotation_path):
            train_file.write(image_path + '\n')
            convert_annotation(nameWithoutExtention)  # convert label
            copyfile(image_path, yolov5_images_train_dir + voc_path)
            copyfile(label_path, yolov5_labels_train_dir + label_name)
    else:  # test dataset
        if os.path.exists(annotation_path):
            test_file.write(image_path + '\n')
            convert_annotation(nameWithoutExtention)  # convert label
            copyfile(image_path, yolov5_images_test_dir + voc_path)
            copyfile(label_path, yolov5_labels_test_dir + label_name)
train_file.close()
test_file.close()