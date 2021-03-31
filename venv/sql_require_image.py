#1.0 导包
import urllib.request
import pymysql
import cv2
import cv2 as cv
from venv.Median_segementation import *
from venv.image_tone_calculate import recognition



def url_to_image(url):
    resp = urllib.request.urlopen(url)
    # asarray 复制数据，将结构化数据转换成ndarray
    image = np.asarray(bytearray(resp.read()), dtype="uint8")    # bytearray将数据转换成（返回）一个新的字节数组
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv.imshow("image1",image)
    cv2.waitKey(0)
    return image

def dispose_image(image):
    picture_num=1            #同时读取图片个数
    maxColor = 7
    pixData = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    theme=MMCQ(pixData, maxColor).quantize()
    dict=recognition(maxColor,theme)
    print(theme)
    print(dict)


def query():
    # 2.0 链接数据库
    connc = pymysql.Connect(
        host='localhost',
        user="root",
        password="hao19970929..",
        database='data_test',
        port=3306,
        charset="utf8",
    )
    # 3.0 创建游标对象
    cur = connc.cursor()
    if not cur:
        raise Exception("数据库连接失败！")
    try:
        # 4.0 编写SQL语句
        sql = 'select * from src_all_pictures limit 1,3;'
        # 5.0 使用游标对象去调用SQL
        cur.execute(sql)
        # 6.0 获取查询结果--
        result = cur.fetchall()
        # print(result)
        #7.0 将数据转化成list
        data_list=[]
        for row in result:
            data_list.append(row[2])
            print("开始：")
            dispose_image(url_to_image(row[2]))
        # print(data_list)
    except Exception as e:
        print(e)
    finally:
        # 8.0 关闭游标
        cur.close()
        # 9.0 关闭连接
        connc.close()

    return data_list

