# 车牌识别License Plate Recognition

​	This is a simple python implementation of the license plate recognition scheme, basically with the realization of the license plate positioning, accurate segmentation and recognition of character numbers and output character recognition results.

​	此为一个简单的车牌识别方案的python实现，基本具有实现车牌定位、字符数字的精确分割与识别和输出字符识别结果的功能。

#  方案

​	使用库opencv4.10

## 彩色图像灰度化

1. 平均法 lightness method： $grayscale=\frac{min(R,G,B)+max{R,G,B}}{2}$
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

关键技术：车牌定位、字符分割、字符识别

图像处理：预处理、车牌定位、倾斜校正、字符分割、字符识别

**图像预处理**是对采集到的图像进行灰度化、边缘检测、去除噪声、二值化等操作。经过预处理的车牌图像能够增强目标图像，提高目标和背景图像的对比度，方便车牌识别的后续工作。

**车牌定位**：从一幅拍摄到的图片定位出车牌的位置，并从图片中提取车牌图像。

**倾斜校正**：检测车牌图像的倾斜角度并校正图像。

**字符分割**：对提取出的车牌图像进行切割，从车牌图像中提取出单个字符的图像。

**字符识别**：对分割的字符进行处理，识别出车牌中的字符。

方法：基于颜色信息的车牌区域提取法；基于形态边缘特征分析的车牌字符识别算法、基于支持向量机的字符识别算法、基于神经网络的车牌定位和识别算法。

中国内地车牌牌编排规则

GA36-2018 中华人民共和国公共安全行业标准-中华人民共和国机动车车牌

挑战：在光照不均匀、大气条件恶劣、背景复杂、车牌不清晰、监控摄像头质量低下等具有挑战性的复杂环境中，准确性收到制约。

**参考文献**

[1]张建洋.基于YOLOv4的车牌识别系统研究[D].中北大学,2023.DOI:10.27470/d.cnki.ghbgc.2023.001002.

[2]WANG D, TIAN Y, GENG W, et al. LPR-Net: Recognizing Chinese license plate in complex environments [J]. Pattern Recognition Letters, 2020, 130: 148-56.

[3]ZHENG D, ZHAO Y, WANG J. An efficient method of license plate location [J]. Pattern Recognition Letters, 2005, 26(15): 2431-8.

https://arxiv.org/pdf/2205.03582

