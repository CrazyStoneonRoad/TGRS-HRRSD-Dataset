TGRS-HRRSD-Dataset: *High Resolution Remote Sensing Detection* (HRRSD)
=====================

The dataset contains 13 categories of RSI objects. It contains 21761 color images acquired from Google Earth with the spatial resolution from 0.15-m to 1.2-m, and 4961 color images acquired from Baidu Map with the spatial resolution from 0.6-m to 1.2-m. Image numbers in each subset are 5401 for ‘train’, 5417 for ‘val’, and 10943 for ‘test’. And ‘train-val’ subset is a merge of ‘train’ and ‘val’.


# Folders
+ /OPT2017/Annotations: \*.xml  
+ /OPT2017/labels: \*.txt  
with the form of (class x y width height)  
+ /OPT2017/JPEGImages: \*.jpg  
+ /OPT2017/ImageSets/Main: Division of the dataset.  
  
# Statistics


    airplane & 1226 & 1222 & 2448 & 2451 & 4899 \\
    baseball diamond & 1007 & 1004 & 2011 & 2022 & 4033 \\
    basketball court & 923 & 920 & 1843 & 2033 & 3876 \\
    bridge & 1123 & 1121 & 2244 & 2326 & 4570 \\
    crossroad & 903 & 901 & 1804 & 2219 & 4023 \\
    ground track field & 859 & 856 & 1717 & 2017 & 3734 \\
    harbor & 967 & 964 & 1931 & 1953 & 3884 \\
    parking lot & 1241 & 1237 & 2478 & 2480 & 4958 \\
    ship & 950 & 948 & 1898 & 1988 & 3886 \\
    storage tank & 1099 & 1092 & 2191 & 2215 & 4406 \\
    T junction & 1066 & 1065 & 2131 & 2289 & 4420 \\
    tennis court & 1043 & 1040 & 2083 & 2212 & 4295 \\
    vehicle & 1188 & 1186 & 2374 & 2382 & 4756 \\





ID | NAME | COUNT_ALL | COUNT_TRAIN | COUNT_VAL | COUNT_TRAINVAL | COUNT_TEST | 
 - |   -  |     -     |     -     |     -     |     -     |     -     |
1	 | ship                |  3975  1226 1222 2448 2451
2	 | bridge              |  4651  1007 1004 2011 2022
3	 | ground track field  |  4033  923 920 1843 2033
4	 | storage tank        |  4424 
5	 | basketball court    |  4064
6	 | tennis court        |  4420
7	 | airplane            |  4901
8	 | baseball diamond    |  4042
9	 | harbor              |  3902
10 | vehicle             |  4756
11 | crossroad           |  4436
12 | T junction          |  4575
13 | parking lot         |  4958

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
