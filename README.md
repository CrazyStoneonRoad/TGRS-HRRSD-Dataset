TGRS-HRRSD-Dataset: *High Resolution Remote Sensing Detection* (HRRSD)
=====================

The dataset contains 13 categories of RSI objects. It contains 21761 color images acquired from Google Earth with the spatial resolution from 0.15-m to 1.2-m, and 4961 color images acquired from Baidu Map with the spatial resolution from 0.6-m to 1.2-m. Image numbers in each subset are 5401 for ‘train’, 5417 for ‘val’, and 10943 for ‘test’. And ‘train-val’ subset is a merge of ‘train’ and ‘val’.


# Folders
+ /OPT2017/Annotations: \*.xml  
+ /OPT2017/labels: \*.txt  
with the form of (class x y width height)  
+ /OPT2017/JPEGImages: \*.jpg  
+ /OPT2017/ImageSets/Main: Division of the dataset.  
  
# Categories
1	ship  
2	bridge  
3	ground track field  
4	storage tank  
5	basketball court  
6	tennis court  
7	airplane  
8	baseball diamond  
9	harbor  
10	vehicle  
11	crossroad  
12	T junction  
13	parking lot  

# Numbers of Different Categories
1	3975  
2	4651  
3	4033  
4	4424  
5	4064  
6	4420  
7	4901  
8	4042  
9	3902  
10	4756  
11	4436  
12	4575  
13	4958  



# Citation
If you find HRRSD dataset useful in your research, please consider citing:

```
@article{zhang2019hierarchical,
  title={Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection},
  author={Zhang, Yuanlin and Yuan, Yuan and Feng, Yachuang and Lu, Xiaoqiang},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  year={2019},
  publisher={IEEE}
}
```
