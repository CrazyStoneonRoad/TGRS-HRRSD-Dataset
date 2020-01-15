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

# labels

Contain ground truth labels of ```*.txt``` files.

1. In each file, a row represents a proposal, namely a candidate box. 

2. For the columns, the first column represents category and the others represent normalized bounding box ```(x_left, y_bottom, x_right, y_top)```.
