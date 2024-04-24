import os

def batch_rename_images(directory, prefix1="free", prefix2="busy",prefix="foggy"):
    # 获取文件夹内所有文件名，并排序
    files = sorted(os.listdir(directory))

    # 定义一个计数器
    count1 = 1
    count2 = 1
    # 遍历所有文件
    for filename in files:
        # 确保处理的是图片文件 (根据需求可以增加或修改文件类型)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # 根据定义的规则构造新的
            if 'free' in filename:
               new_name = f"{prefix1}_{count1}.jpg"
               count1 += 1
            else:
               new_name = f"{prefix2}_{count2}.jpg"
               count2 += 1
            # 定义原文件和新文件的完整路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            # 执行重命名操作
            os.rename(old_path, new_path)
            # 打印出已重命名的文件
            print(f"Renamed {filename} -> {new_name}")
            # 更新计数器


# 使用方法：
directory_path = "data/real/mix_foggy_50"
batch_rename_images(directory_path)
