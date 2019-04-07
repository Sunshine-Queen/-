

import docx  # pip install python-docx
import shutil
import os

# 以下3行解决在部分电脑上将中文显示为乱码的问题
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 文件内容数组 [第1行，第2行....]
text_list = []
# 文件相似度阈值
s_value = 0.9
print("文件相似度阈值:", s_value)
# 相似度较高的学生
stu_names = []


def file_extension(path):
    # 获取文件后缀名
    return os.path.splitext(path)[1]


def change_filename(dir_path):
    """
    1.将docx文件名改为上级目录名
    2.将改名后的文件放入查重目录D:/TEST中
    :param
        file_path: 要读取文件的路径
            ex:    D:/1/张三/实验1.docx 改名为 D:/TEST/张三.docx
    :return:
        null
    """
    # 要判断dir_path是目录还是文件，如果是文件则直接返回
    if not os.path.isdir(dir_path):
        return
    # 要判断传递的file_path末尾是否包含路径分隔符，如果没有则加入
    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path+os.path.sep
    # 遍历获取当前目录下所有的子目录名（返回列表类型）
    dir_names = os.listdir(dir_path)
    # 拼接目录
    for dir_name in dir_names:
        sub_path = os.path.join(dir_path, dir_name)
        if not sub_path.endswith(os.path.sep):
            docx_path = sub_path+os.path.sep
        doc_names = os.listdir(docx_path)
        for doc_name in doc_names:
            if file_extension(os.path.join(docx_path, doc_name)) == ".docx":
                os.rename(os.path.join(docx_path, doc_name), os.path.join(
                    "D:/TEST/", dir_name+".docx"))  # 剪切文件
        # os.remove(os.path.join(docx_path,"作业结果及评论.html"))    #删除其他文件
        # os.remove(docx_path)                #删除目录
        shutil.rmtree(docx_path)


def read_docx(file_path):
    """
    读取第一个文件放入text_list
    :param
        file_path: 要读取文件的路径
            ex:    D:/TEST/张三.docx
    :return:
        打印文件内容
    """
    text_list = []
    try:
        data = docx.Document(file_path)
        for para in data.paragraphs:
            # print(index, para.text)
            text_list.append(para.text)
            # print(text_list)
    except EOFError:  # 锁定是哪种异常
        print('ERROR INPUT !')  # 出现异常的处理方法
        pass
    else:
        # 返回读取的文件内容
        return text_list


def get_files(dir_path):
    """
    :param
        dir_path: 要读取目录的路径
            e.g:    D:/TEST
    :return:
    """
    file_name_1 = ""
    file_name_2 = ""
    # 由于不存在根目录，所以不需要再次判断是否文件夹
    # 要判断传递的dir2末尾是否包含路径分隔符，如果没有则加入
    # "D:/TEST"  + "/"  = "D:/TEST/"
    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path+os.path.sep
    # 遍历获取目录下所有的子目录以及文件名（返回列表类型）
    # names = [张三.docx,李四.docx,...]
    names = os.listdir(dir_path)
    for index, name in enumerate(names):
        # 合并路径和名字 D:/TEST/ + 1.docx
        sub_path = os.path.join(dir_path, name)
        # 循环读取每个文件
        text_list = read_docx(sub_path)
        # print("读取的文件", name, "的内容", sub_path, text_list)
        # 将文件相互比较
        for index, name_2 in enumerate(names):
            sub_path = os.path.join(dir_path, name_2)
            text_list_tmp = read_docx(sub_path)
            if len(text_list) >= len(text_list_tmp):
                diff = list(set(text_list).difference(set(text_list_tmp)))
                pre = (len(text_list)-len(diff))/len(text_list)
            else:
                diff = list(set(text_list_tmp).difference(set(text_list)))
                pre = (len(text_list_tmp)-len(diff))/len(text_list_tmp)
            # 找出相似度大于阈值的文件并输出
            # file_name_2 != name and file_name_1 != name_2 目的是重复的信息只显示一遍
            name = name.replace(".docx", "")
            name_2 = name_2.replace(".docx", "")
            if name != name_2 and file_name_2 != name and file_name_1 != name_2 and pre > s_value:
                # if name!=name_2 and file_name_2!=name and file_name_1!=name_2 :
                # print("文件", name, "和", name_2, "的不同点", diff)
                print("文件", name, "和", name_2, "的相似度", format(pre, '.0%'))
                file_name_1 = name
                file_name_2 = name_2
                # 如果学生不在重复名单内，则加入重复名单
                if name not in stu_names:
                    stu_names.append(name)
                if name_2 not in stu_names:
                    stu_names.append(name_2)

    print("共检查作业", index+1, "份", "其中相似度较高的学生有", stu_names)


if __name__ == "__main__":
    change_filename("D:/1")
    get_files("D:/TEST")
