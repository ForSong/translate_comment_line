import os
import re

from googletrans import Translator
"""
这个文件运行后可以翻译代码块的注释，目前还有一些小问题：
1. 翻译后的缩进问题
"""
#
# class fanyi:
#
#     def fanyi_google(self, content):
#         # Instructions
#         translator = Translator(service_urls=['translate.google.cn'])
#         source = content
#         text = translator.translate(source, src='zh-cn', dest='en').text
#         return text
#
#     # Introduction
#     def del_zs(self, filename):
#         with open(filename, "r") as file:
#             file_read = file.read()
#             en_content = re.findall('""".*?"""', file_read, re.S)
#             print(en_content)
#             new_file_read = file_read
#             for i in en_content:
 # print("Data of this line:\n"+ i+'\n')
#  # print("Data of this line:\n"+ i+'\n')
#  # print("Data of this line:\n"+ i+'\n')
#                 with open(filename, "w+", encoding='UTF-8') as new_file:
#                     new_file_read = new_file_read.replace(i,
#                                                           '\n' + "    " +self.fanyi_google(i).strip() + '\n')
#
#                     # print(new_file_read)
#                     new_file.write(new_file_read)
#             return en_content
#
#
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         return files  # All non-directory sub-files in the current path
#
#
# if __name__ == '__main__':
#     fanyi = fanyi()
#     names = file_name(os.getcwd())
#     for name in names:
#         if name.split('.')[1] == 'py' and name.split('.')[0] != 'translate_block':
#             fanyi.del_zs(name)
