import cv2 as cv
import time

from venv.Median_segementation import MMCQ


def getPixData(imgfile='imgs/avatar_282x282.jpg'):
    return cv.cvtColor(cv.imread(imgfile, 1), cv.COLOR_BGR2RGB)

def testMMCQ(pixDatas, maxColor):
    start  = time.process_time()
    themes = list(map(lambda d: MMCQ(d, maxColor).quantize(), pixDatas))   #return两个返回值，count
    print("MMCQ Time cost: {0}".format(time.process_time() - start))
    return themes

def recognition(maxColor,theme):
    clall = 0
    for i in range(maxColor):
        w_distance = pow((pow(255 - theme[i][0], 2) + pow(255 - theme[i][1], 2) + pow(255 - theme[i][2], 2)),
                                 1 / 3)
        c_distance = pow((pow(theme[i][0], 2) + pow(theme[i][1], 2) + pow(theme[i][2], 2)), 1 / 3)
        if (theme[i][0] > 127):
            if (theme[i][1] < 127):
                cla = theme[i][3] * w_distance
            else:
                cla = (1 / w_distance) * theme[i][3]
        else:
            if (theme[i][1] > 127):
                cla = -theme[i][3] * c_distance
            else:
                cla = -(1 / c_distance) * theme[i][3]
        clall += cla
    if (clall > 0):
            dict= "暖色调"
    else:
        dict = "冷色调"
    return dict

def testvs():
    picture_num=1;            #同时读取图片个数
    maxColor = 7
    imgs = map(lambda i: 'image/image%s.jpg' % i, range(1,picture_num+1))
    pixDatas = list(map(getPixData, imgs))
    # cv.imshow(pixDatas)
    theme = testMMCQ(pixDatas, maxColor)
    dict=recognition(maxColor,theme)
    print(theme)
    print(dict)
