# import os
# import cv2
# import numpy as np
#
# def fog(img):
#     fog = np.zeros_like(img, dtype='uint8')
#     fog = np.random.randint(200, 256, size=img.shape, dtype=np.uint8)
#
#     fog = cv2.GaussianBlur(fog, (101, 101), 0)
#     fog = fog.astype(img.dtype)  # 将雾的数据类型与图像一致
#     img_with_fog = cv2.addWeighted(img, 0.004, fog, 0.996, 0)
#     return img_with_fog
#
# def add_fog(image):
#     return fog(image)
#
#
# if __name__ == '__main__':
#     # 指定图片文件夹的路径
#     image_folder = 'data/real/temp'
#     output_file = 'data/foggy_labels.txt'
#     # 获取图片文件夹中的所有文件
#     image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
#
#     # with open(output_file, 'w') as file:
#
#     for image_file in image_files:
#         # 构建完整的图片文件路径
#         image_path = os.path.join(image_folder, image_file)
#         # print(image_file)
#
#         # 从文件加载图像
#         image = cv2.imread(image_path)
#
#         # 确保图像是 NumPy 数组并具有正确的数据类型
#         image = image.astype(np.uint8)
#
#         # 在这里执行你的处理操作，例如加雪、加雾等
#         image_with_fog = add_fog(image)
#
#         # img_info = "foggy/" + image_file
#         # # print(img_info)
#         # if "busy" in img_info:
#         #     label = 1
#         # else:
#         #     label = 0
#         #
#         # file.write("{}\t{}\t{}\n".format(img_info, label, 0))
#
#         # cv2.imshow("", image_with_fog)
#         # cv2.waitKey(0)
#         # cv2.destroyWindow()
#
#         # 保存处理后的图像到指定文件夹
#         output_folder = 'data/real/strong'
#         output_path = os.path.join(output_folder, image_file)
#         print(output_path)
#         cv2.imwrite(output_path, image_with_fog)
#
#     # img_show()

# import os
# import random
#
# if __name__ == '__main__':
#     image_folder = 'data/real/mix_foggy_0'
#     output_file = 'data/real/mix_foggy_0_labels.txt'
#     image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
#
#     # 创建包含图像路径和标签的元组列表
#     image_label_pairs = []
#     for image_file in image_files:
#         img_info = "mix_foggy_0/" + image_file
#         label = 1 if "busy" in img_info else 0
#         image_label_pairs.append((img_info, label, 0))
#
#     # 随机打乱列表
#     random.shuffle(image_label_pairs)
#
#     # 写入文件
#     with open(output_file, 'w') as file:
#         for img_info, label, _ in image_label_pairs:
#             file.write("{}\t{}\t{}\n".format(img_info, label, 0))



import os
import cv2
import numpy as np

def fog(img, intensity=0.9):
    # 随机生成雾
    fog = np.zeros_like(img, dtype='uint8')
    fog = np.random.randint(200, 256, size=img.shape, dtype=np.uint8)

    # 应用高斯模糊来模拟雾的外观
    fog = cv2.GaussianBlur(fog, (101, 101), 0)
    fog = fog.astype(img.dtype)  # 确保雾的数据类型与图像一致

    # 随机雾浓度
    alpha = 0.1 + 0.9 * np.random.rand() * intensity  # alpha 的值在 0.1 到 intensity 之间变化
    img_with_fog = cv2.addWeighted(img, 1 - alpha, fog, alpha, 0)
    return img_with_fog

def add_fog(image, intensity=0.9):
    return fog(image, intensity=intensity)


if __name__ == '__main__':
    # 指定图片文件夹的路径
    image_folder = 'data/real/temp'
    output_folder = 'data/real/strong'

    # 获取图片文件夹中的所有文件
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

    for image_file in image_files:
        # 构建完整的图片文件路径
        image_path = os.path.join(image_folder, image_file)

        # 从文件加载图像
        image = cv2.imread(image_path)

        image = image.astype(np.uint8)  # 确保图像是 NumPy 数组并具有正确的数据类型

        # 在图片上随机添加雾
        image_with_fog = add_fog(image, intensity=0.9)  # 可以调整 intensity 来改变雾的浓度

        # 保存处理后的图像到指定文件夹
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, image_with_fog)

