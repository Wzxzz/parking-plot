import random


def merge_and_shuffle_txt_files(file1, file2, file3 , output_filename):
    """
    合并两个TXT文件的内容，并随机排序，然后保存到一个新的TXT文件中。

    :param file1: 第一个输入文件路径
    :param file2: 第二个输入文件路径
    :param output_filename: 输出TXT文件名
    """
    all_lines = []

    # 从第一个文件读取内容并加入列表
    with open(file1, 'r') as f1:
        all_lines.extend(f1.readlines())

    # 从第二个文件读取内容并加入列表
    with open(file2, 'r') as f2:
        all_lines.extend(f2.readlines())

    with open(file3, 'r') as f3:
        all_lines.extend(f3.readlines())

    # 对列表进行随机排序
    random.shuffle(all_lines)

    # 将随机排序后的内容写入输出文件
    with open(output_filename, 'w') as outfile:
        for line in all_lines:
            outfile.write(line)

    print(f"Merged and shuffled {file1} and {file2} and {file3} into {output_filename}")


# 使用方法：
file1_path = "data/real/foggy_labels.txt"
file2_path = "data/real/rainy_labels.txt"
file3_path = "data/real/snowy_labels.txt"
output_file = "data/real/all_weather_labels.txt"
merge_and_shuffle_txt_files(file1_path, file2_path, file3_path, output_file)
# import random
#
# from utils.foggy import add_fog
# from utils.rainy import add_rain
# from utils.snowy import add_snow
# import os
# import cv2
# import numpy as np
#
# weather = "snowy"
# def add_weather(weather: str):
#     '''
#     生成天气图像并记录标签数据
#     :param weather:
#     :return:
#     '''
#     image_folder = 'data/real/snowy'
#     output_file = 'data/real/snowy_labels.txt'
#
#     # 获取图片文件夹中的所有文件
#     image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
#     out_list = []
#
#     for image_name in image_files:
#         # 构建完整的图片文件路径
#         image_path = os.path.join(image_folder, image_name)
#
#         # 从文件加载图像
#         image = cv2.imread(image_path)
#
#         # 确保图像是 NumPy 数组并具有正确的数据类型
#         image = image.astype(np.uint8)
#
#         # 在这里执行你的处理操作，例如加雪、加雾等
#         if weather == "foggy":
#
#             labelW = 0
#         elif weather == "rainy":
#
#             labelW = 1
#         elif weather == "snowy":
#
#             labelW = 2
#
#         # 把图片信息写进txt
#         label_info = weather + "/" + image_name
#         if "busy" in label_info:
#             labelP = 1
#         else:
#             labelP = 0
#
#         out_list.append((label_info, labelP, labelW))
#
#         output_img_info = "data/real/" + weather + "/" + image_name
#
#         cv2.imwrite(output_img_info, image)
#
#     count = len(out_list)
#     random.shuffle(out_list)
#     with open(output_file, 'w') as file:
#         for label_info, labelP, labelW in out_list:
#             file.write("{}\t{}\t{}\n".format(label_info, labelP, labelW))
#
#     print("当前处理{}天气完毕，图像数量：{}".format(weather, count))
#
#     return out_list
#
#
# if __name__ == '__main__':
#     mix_out_list = []
#     for weather in ["snowy"]:
#         mix_out_list.extend(add_weather(weather))
#     # 将混合天气标签打乱并写入文件
#     random.shuffle(mix_out_list)
#     with open("data/real/all_weather_labels.txt", 'w') as file:
#         for label_info, labelP, labelW in mix_out_list:
#             file.write("{}\t{}\t{}\n".format(label_info, labelP, labelW))
