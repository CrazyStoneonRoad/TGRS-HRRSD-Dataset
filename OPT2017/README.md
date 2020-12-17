# ImageSets/Main

- cls: object category names.

- set: train, val, trainval, or test.

1. In ```{$cls}_{$set}.txt```, each row is in the form: ```Image_Id``` ```Contain_{$cls}```. 
For example, ```00053 -1``` in ```tennis court_val.txt``` means that 00053.jpg doesn't contain tennis court. 

2. In ```{$set}.txt```, each row is name of images selected for the current set.

3. Trainval is a gather of train and val.

# JPEGImages

Contain images of ```*.jpg``` files. 

# Annotations

Contain ground truth labels of ```*.xml``` files.

Candidate boxes are organized with tree.

# avr_std_detection_sets.py

This file is used to calculate mean value and standard deviation for images in object detection datasets. These two values will be needed for training better models. 

Put this file under root of the datasets, where there is a 'JPEGImages' folder containing images.

If you want to calculate the ```avr``` and ```std``` from 100 randomly selected images, run :
```shell
$ cd your_HRRSD_path/OPT2017
$ python avr_std_detection_sets.py 100
```

If you run ```$ python avr_std_detection_sets.py```, 500 images will be randomly selected.
