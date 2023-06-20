import cv2
import numpy as np
import json
import os

folder_path = "/Users/jay/Documents/python_ws/poc210/inputs"  # 替换为你要遍历的文件夹路径
category_types = ["unlabeled","rug","ground","unknwon"]


def json2mask(json_path):
    mask = np.zeros([360, 640, 1], np.uint8)
    with open(json_path,"r") as f: #json文件路径
        label = json.load(f)

    shapes = label["shapes"]
    for shape in shapes:
        category = shape["label"]
        points = shape["points"]
        #填充
        points_array = np.array(points,dtype=np.int32)
        mask = cv2.fillPoly(mask, [points_array], category_types.index(category))
        # if category == "unknwon":    #高亮显示其中一个标签图像
        #     mask = cv2.fillPoly(mask, [points_array], 255)
        # else:
        #     mask = cv2.fillPoly(mask,[points_array],category_types.index(category))
    save_path = json_path.split(".")[0] + ".jpg"
    cv2.imwrite(save_path,mask)


# 遍历文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        if file_name.endswith(".json"):  # 仅处理以 ".json" 结尾的文件
            file_path = os.path.join(root, file_name)
            json2mask(file_path)

