# 车牌识别

​	设计车牌识别方案、画出程序实现流程。编程实现车牌定位、字符数字的精确分割与识别，并输出字符识别结果。

## 彩色图像灰度化

1. 平均法 lightness method 
   $$
   grayscale=\frac{min(R,G,B)+max{R,G,B}}{2}
   $$
   
2. 亮度法 average method
   $$
   grayscale = \frac{R+G+B}{3}
   $$
   
3. 光度法 luminosity method
   $$
   grayscale=0.3R+0.59G+0.11B
   $$
   

彩色图像存储(height, width, channels)（RGB）

参考：https://www.baeldung.com/cs/convert-rgb-to-grayscale

车牌识别数据集：https://aistudio.baidu.com/datasetdetail/56280

字符识别：
1. OCR *Optical Character Recognition*
2. 模版匹配

车牌识别参考：[https://www.cnblogs.com/silence-hust/p/4191732.html](https://www.cnblogs.com/silence-hust/p/4191732.html)
