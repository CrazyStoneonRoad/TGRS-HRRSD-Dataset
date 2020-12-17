
## ImageSets/Main

- cls: object category names.

- set: train, val, trainval, or test.

1. In ```{$cls}_{$set}.txt```, each row is in the form: ```Image_Id``` ```Contain_{$cls}```. 
For example, ```00053 -1``` in ```tennis court_val.txt``` means that 00053.jpg doesn't contain tennis court. 

2. In ```{$set}.txt```, each row is name of images selected for the current set.

3. Trainval is a gather of train and val.

## JPEGImages

Contain images of ```*.jpg``` files. 

## Annotations

Contain ground truth labels of ```*.xml``` files.

Candidate boxes are organized with tree.

## avr_std_detection_sets.py

This file is used to calculate `mean` value and `standard deviation` for dataset images. 

These two groups of values will be needed for training better models. 

Usage :

```bash
python ./ImagesPath/ 500
```

500 refers to number of the images used to calculate `mean` and ` standard deviation`.

