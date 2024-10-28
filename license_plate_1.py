import cv2
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']  # 这里选择合适的中文字体
rcParams['axes.unicode_minus'] = False  # 解决负号 '-' 显示为方块的问题

# 读取图像默认BGR
image = cv2.imread('F:/20241022222909.png')
plt.figure()
# 检查图像是否成功加载
if image is None:
    print("Error: Could not load image. Check the file path.")
else:
    # 图像加载成功，继续处理
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 显示原图像
    plt.subplot(3,2,1)
    plt.imshow(image_rgb)
    plt.title("车牌图像")

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(3,2,2)
plt.imshow(gray)
plt.title("灰度图")
# 使用高斯模糊来减少噪声
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
plt.subplot(3,2,3)
plt.imshow(blurred)
plt.title("高斯模糊")

# 使用Canny边缘检测
edged = cv2.Canny(blurred, 30, 150)

# 找到轮廓
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 假设车牌是面积最大的矩形
contour_img = image.copy()
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
plate_contour = None

# 遍历轮廓，寻找可能的车牌
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    if len(approx) == 4:  # 车牌大多是矩形
        plate_contour = approx
        break

if plate_contour is not None:
    cv2.drawContours(contour_img, [plate_contour], -1, (0, 255, 0), 3)
    plt.subplot(3,2,4)
    plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
    plt.title('定位结果')

    
# 提取车牌区域
if plate_contour is not None:
    x, y, w, h = cv2.boundingRect(plate_contour)
    plate_image = gray[y:y+h, x:x+w]

    # 二值化处理
    _, thresh = cv2.threshold(plate_image, 150, 255, cv2.THRESH_BINARY_INV)

    # 显示二值化图像
    plt.subplot(3,2,5)
    plt.imshow(thresh, cmap='gray')
    plt.title("二值化车牌")

    # 使用轮廓分割字符
    character_contours, _ = cv2.findContours(~thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 打印字符轮廓的数量
    print(f'找到的字符数量: {len(character_contours)}')
    # 显示找到的轮廓
    contour_image = cv2.cvtColor(~thresh, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_image, character_contours, -1, (0, 255, 0), 1)
    plt.subplot(3,2,6)
    plt.imshow(contour_image)
    plt.title("找到的轮廓")
    plt.axis('off')
    plt.show()
    # 设置最小和最大轮廓面积阈值
    min_area = 100  # 最小轮廓面积
    max_area = 4000  # 最大轮廓面积（可以根据需要调整）

    # 过滤轮廓
    filtered_contours = [
    contour for contour in character_contours 
    if min_area < cv2.contourArea(contour) < max_area
    ]
    # 再次打印过滤后的字符数量
    print(f'过滤后的字符数量: {len(filtered_contours)}')
    '''
    # 替换为你的模板路径
    template_path = 'F:/character_templates/'
    # 字符集
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789豫'
    # 存储模板的字典
    templates = {}
    # 创建一个绘图窗口
    plt.figure(figsize=(12, 8))

    import pytesseract
    for i, char in enumerate(characters):
        # 直接拼接字符模板图像的路径
        img_path = template_path + char + '.png'  # 使用字符串拼接构建路径
        img = cv2.imread(img_path)  # 读取字符模板图像
        if img is not None:  # 检查图像是否成功加载
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
            img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # 二值化模板图像
            templates[char] = img  # 存储模板
            # 显示模板图像
            plt.subplot(5, 10, i + 1)  # 设定子图的布局（例如：5行10列）
            plt.imshow(img, cmap='gray')
            plt.title(char)
            plt.axis('off')  # 不显示坐标轴
        else:
            print(f"Warning: Could not load image for character '{char}'.")
    # 调整布局并显示所有模板图像
    plt.tight_layout()
    plt.show()
    '''
    # 模板匹配识别字符
    recognized_text = ""
    plate_text=""
    # 加载字符模板，假设模板保存在 templates/ 文件夹下
    templates = {}
      
    
    for i, contour in enumerate(filtered_contours):
        (x, y, w, h) = cv2.boundingRect(contour)
        character = thresh[y:y+h, x:x+w]
        # 可选: 进一步调整字符图像的大小以便更好地进行识别
        character = cv2.resize(character, (20, 20))  # 例如调整为 20x20 的大小
        plt.subplot(1, len(filtered_contours), i+1)
        plt.imshow(character, cmap='gray')
        plt.title(f'字符 {i+1}')
        # 在模板中进行匹配（未实现）
        best_match = None
        max_value = 0

        for char, template in templates.items():
            
            result = cv2.matchTemplate(~character, template, cv2.TM_CCOEFF_NORMED)
            _, value, _, _ = cv2.minMaxLoc(result)

            if value > max_value:
                max_value = value
                best_match = char
        config = '--psm 8 -l chi_sim -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789京沪粤川渝鄂皖晋冀辽吉黑苏浙赣鲁豫湘桂琼甘蒙贵陕藏宁新' # 逐字符识别
        if best_match is not None:
            recognized_text += best_match
    plt.show()
    print(f"识别的车牌字符: {recognized_text}")
    

