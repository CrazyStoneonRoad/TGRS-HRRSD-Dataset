TGRS-HRRSD-Dataset: *High Resolution Remote Sensing Detection* (HRRSD)
=====================

The dataset contains 13 categories of RSI objects. It contains 21761 color images acquired from Google Earth with the spatial resolution from 0.15-m to 1.2-m, and 4961 color images acquired from Baidu Map with the spatial resolution from 0.6-m to 1.2-m. Image numbers in each subset are 5401 for ‘train’, 5417 for ‘val’, and 10943 for ‘test’. And ‘train-val’ subset is a merge of ‘train’ and ‘val’.


# Folders
## Labels
+ /OPT2017/Annotations: \*.xml  
+ /OPT2017/labels: \*.txt  *with the form of (class x y width height)*
## Images
+ /OPT2017/JPEGImages: \*.jpg  
## Dataset Division
+ /OPT2017/ImageSets/Main: Division of the dataset.  
  
# Statistics

Label|Name|N_Train|N_Val|N_Trainval|N_Test|N_All|Mean Resized Scale /pixel|Resized Scale Std /pixel
:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: |:-: 
1|  ship                |950|948|1898|1988|3886|167.44|110.37
2|  bridge              |1123|1121|2244|2326|4570|246.10|110.53
3|  ground track field  |859|856|1717|2017|3734|276.50|100.65
4|  storage tank        |1099|1092|2191|2215|4406|125.60|68.41
5|  basketball court    |923|920|1843|2033|3876|108.19|57.46
6|  tennis court        |1043|1040|2083|2212|4295|102.71|38.80
7|  airplane            |1226|1222|2448|2451|4899|113.21|67.98
8|  baseball diamond    |1007|1004|2011|2022|4033|231.61|117.85
9|  harbor              |967|964|1931|1953|3884|163.96|94.16
10|  vehicle             |1188|1186|2374|2382|4756|41.96|9.99
11|  crossroad           |903|901|1804|2219|4023|220.54|59.24
12|   T junction         |1066|1065|2131|2289|4420|198.71|54.88
13|   parking lot        |1241|1237|2478|2480|4958|122.85|54.45

In this table, N_* refers to numbers of objects. 'Train', 'Val', 'Test' are three subsets of the dataset. 'Mean Resized Scale' shows average scale of each category. 'Resized Scale Std' is the standard deviation of category scale.

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
