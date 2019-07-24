#!/usr/bin/python3

import cv2

def adjust_hue(imgSrc):

    # RGB三通道分离
    imgRGB = imgSrc.copy()

    # 求原始图像的RGB分量的均值
    B = cv2.mean(cv2.split(imgSrc)[0])[0]
    G = cv2.mean(cv2.split(imgSrc)[1])[0]
    R = cv2.mean(cv2.split(imgSrc)[2])[0]
 
    # 需要调整的RGB分量的增益
    total = R + G + B
    R = 1 if R ==0 else R
    G = 1 if G ==0 else G
    B = 1 if B ==0 else B

    KB = total / (3 * B)
    KG = total / (3 * G)
    KR = total / (3 * R)
 
    # 调整RGB三个通道各自的值
    imgRGB[0] = imgRGB[0] * KB
    imgRGB[1] = imgRGB[1] * KG
    imgRGB[2] = imgRGB[2] * KR
 
	# RGB三通道图像合并
    ##img = cv2.merge(imgRGB, img)
    cv2.imshow("白平衡调整后", imgRGB)
    cv2.waitKey(3)


'''
@description: 获取摄像头参数
@param {type} 
@return: 
'''
def get_camera_info(capture):
    print("########################################")
    print("视频编码器格式:", capture.get(cv2.cv2.CAP_PROP_FOURCC))
    print("宽:", capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    print("高:", capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("帧率:", capture.get(cv2.CAP_PROP_FPS))
    print("亮度:", capture.get(cv2.CAP_PROP_BRIGHTNESS))
    print("对比度:", capture.get(cv2.CAP_PROP_CONTRAST))
    print("饱和度:", capture.get(cv2.CAP_PROP_SATURATION))
    print("色度:", capture.get(cv2.CAP_PROP_HUE))
    print("曝光:", capture.get(cv2.CAP_PROP_EXPOSURE))
    print("增益:", capture.get(cv2.CAP_PROP_GAIN))
    #print(capture.get(cv2.CAP_PROP_WHITE_BALANCE))
    print("自动曝光:", capture.get(cv2.CAP_PROP_AUTO_EXPOSURE))
    print("WB:", capture.get(cv2.CAP_PROP_AUTO_WB))


'''
@description: 打开摄像头
@param {type} 
@return: 
'''
def open_camera():

    i = 0
    while True:
        capture = cv2.VideoCapture(0)
        if(capture != None):
            break
        if(i > 10):
            return
        i +=1

    get_camera_info(capture)

    # 设置摄像头参数
    #capture.set(cv2.CAP_PROP_AUTO_WB, 0);       # 色调
    capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1); # 关闭自动曝光

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500); # 宽度 
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500);# 高度
    capture.set(cv2.CAP_PROP_FPS, 30);          # 帧率
    capture.set(cv2.CAP_PROP_BRIGHTNESS, 1);    # 亮度 1
    capture.set(cv2.CAP_PROP_CONTRAST,40);      # 对比度 40
    capture.set(cv2.CAP_PROP_SATURATION, 50);   # 饱和度 50
    capture.set(cv2.CAP_PROP_HUE, 0);           # 色调 50
    capture.set(cv2.CAP_PROP_EXPOSURE, 250);     # 曝光 50

    get_camera_info(capture)


    # 读摄像头
    cv2.namedWindow("video")
    while (capture.isOpened()):
        ret,frame = capture.read()
        if ret == True:
            cv2.imshow("video",frame)
            adjust_hue(frame)

        if (cv2.waitKey(30) == 27): # Esc键退出
            break

    # 释放摄像头
    capture.release()
    # 删除全部窗口
    cv2.destroyAllWindows()

open_camera()