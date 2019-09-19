TGRS-HRRSD-Dataset: *High Resolution Remote Sensing Detection* (HRRSD)
=====================

# NOTE: JPEG files are available on [BaiduCloud](https://pan.baidu.com/s/1ainmXaL_Mu5XASk3ydhqKA#list/path=%2F&parentPath=%2F) and [GoogleDrive](https://drive.google.com/open?id=1bffECWdpa0jg2Jnm7V0oCyFFh0N-EIkr)

- HRRSD contains **21,761 images** acquired from Google Earth and Baidu Map with the spatial resolution from 0.15-m to 1.2-m. 

- There are **55,740 object instances** in HRRSD.

- HRRSD contains **13 categories** of RSI objects. 

Moreover, this dataset is divided as several subsets, image numbers in each subset are **5401 for ‘train’, 5417 for ‘val’, and 10943 for ‘test’**. And ‘train-val’ subset is a merge of ‘train’ and ‘val’.


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

# FAQ
If any question is met, please contanct me with the e-mail: 1153463027@qq.com.

Qestion 1: AP for the "T junction" class is always NAN or 0, why?

Anwser Q1: In some object detection frameworks, there may be a piece of code like "cls_names = lower( cls_names )". 
This will set class names to lower case, but class names in xml files contain "T junction" where "T" is uppercase. 
This actually will cause several problems. 
The solution is using debug sofwares to find the code of changing word cases and correct it. 
For the dataset, I won't change the "T junction" labels in xmls currently for lacking time. 


# Citation
If you find HRRSD dataset useful in your research, please consider citing:

```
@article{zhang2019hierarchical,
  title={Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection},
  author={Zhang, Yuanlin and Yuan, Yuan and Feng, Yachuang and Lu, Xiaoqiang},
  journal={IEEE Transactions on Geoscience and Remote Sensing},
  volume={57},
  number={8},
  pages={5535--5548},
  year={2019},
  publisher={IEEE}
}
```
