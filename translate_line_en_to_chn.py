# -*- coding: utf-8 -*-
"""
@ time:2020.8.19
@ author:Song Zhizhuo
"""
import os
from googletrans import Translator
import re

"""

这个文件运行可以直接翻译当前文件夹和子文件夹中的所有代码文件中的注释
支持python,java,c++语言的代码文件翻译

"""


def is_contain_chinese(check_str):
    """
    辅助方法：判断字符串中是否含有中文
    :param check_str: 需要判断的字符串
    :return: 布尔值，如果包含中文返回true不包含返回false
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def fanyi_google(content):
    """
    辅助方法：用于翻译字符串
    注意：这里的translate方法中的src是源文件的语言，dest是需要翻译成什么语言
    :param content: 需要翻译的字符串
    :return: 翻译好的字符串
    """
    # Instructions
    translator = Translator(service_urls=['translate.google.cn'])
    source = content
    text = translator.translate(source, src='en', dest='zh-cn').text
    return text


def translate_file(file_name):
    """
    辅助方法：翻译传入的文件
    :param file_name: 需要翻译的文件的路径
    :return: 无返回值
    """
    try:
        fn = file_name
        print(file_name)
    except IndexError as e:
        print('请正确的输入文件名):')
        return
    # 判断文件是否为代码文件，而且不以.开头
    if (('.py' or '.java' or '.c') in file_name) and (not file_name.split('/')[-1].startswith('.')):
        # _file是文件后缀，用于后面判断是那种类型的代码，方便识别对应的注释符号
        _file = fn.split('.')[1]
    else:
        return

    try:
        # 打开文件
        f = open(str(fn), 'r')
    except FileNotFoundError as e:
        print('没有找到该文件，请重试):')
        return

    result = []
    mid1 = ' // '
    mid2 = ' # '
    # readlines的结果返回的是一个列表，每个元素是每行的内容
    tmp_lines = lines = f.readlines()

    import re
    # 定义一个计数器，用于记录索引
    num = int()

    # if _file == 'java' or _file == 'c' or _file == 'cpp' or _file == 'js':
    # 判断文件是否是java或者c或者c++
    if _file == 'java' or _file == 'c' or _file == 'cpp':
        for i in lines:
            s = re.findall('//', i, re.S)
            # s = re.findall('#', i, re.S)
            if is_contain_chinese(i) and s:
                # 处理注释行
                head = i.split('//')[0]
                tail = i.split('//')[-1]
                tail = fanyi_google(tail)
                content = head + mid2 + tail
                content = content[1:]
                result.append(content + '\n')
                tmp_lines[num] = content + '\n'

            num += 1
    # 判断是否是python代码
    elif _file == 'py':
        # 遍历每行文字
        for i in lines:
            # 判断行中是否包含#
            s = re.findall('#', i, re.S)
            if s == []:
                pass
            elif not (i.split('#')[-1].replace('\n', '').strip() is ''):
                # num = tmp_num
                head = i.split('#')[0]
                tail = i.split('#')[-1]
                print(tail)
                tail = fanyi_google(tail)
                content = head + mid2 + tail
                result.append(content + '\n')
                tmp_lines[num] = content + '\n'

            num += 1

    # 其他情况直接跳过
    else:
        pass

    f.close()
    if not result:
        print('文件中无中文注释')
        return 1
    else:
        print('注释翻译完成，正在替换内容...')

    f2 = open(str(fn), 'w')
    for i in tmp_lines:
        f2.write(i)

    f2.close()

    print('替换完成，已保存至文件{}'.format(fn.split('/')[-1]))


class AutoTrans:
    """
    自动翻译类，包含了所有自动翻译的方法。
    在翻译之前需要首先进行实例化
    """

    # def file_name(self, file_dir):
    #     files = []
    #     for root, dirs, files in os.walk(file_dir):
    #         # print(dirs.append(files))
    #         for filename in files:
    #             print(os.path.join(root, filename))
    #             files.append(os.path.join(root, filename))
    #     return files  # All non-directory sub-files in the current path

    def file_name(self, path, all_files):
        # First traverse all files and folders in the current directory
        file_list = os.listdir(path)
        # Prepare to loop to determine whether each element is a folder or a file. If it is a file, pass the name to
        # the list. If it is a folder, recursively
        for file in file_list:
            # Use the os.path.join() method to get the full name of the path and store it in the cur_path variable,
            # otherwise you can only traverse one level of directory each time
            cur_path = os.path.join(path, file)
            # 判断是否是一个文件夹
            if os.path.isdir(cur_path):
                self.file_name(cur_path, all_files)
            else:
                all_files.append(cur_path)
        return all_files

    def auto_trans_files(self, root_path):
        file_names = self.file_name(root_path, [])
        for file_name in file_names:
            if 'translate_line_en_to_chn' not in file_name:
                translate_file(file_name)


if __name__ == '__main__':
    auto_translator = AutoTrans()
    auto_translator.auto_trans_files(
        os.getcwd())  # auto_translator.auto_trans_files('/Users/songzhizhuo/Desktop/pythoncode02/pythonProject/test')
