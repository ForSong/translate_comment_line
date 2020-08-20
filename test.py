import os
import re


def test_position():
    mid2 = '#'
    # This is the first test
    i = '   # jiji'
    j = '    # '
    print(j[1:])
    s = re.findall('#', i, re.S)
    head = i.split('#')[0]
    tail = i.split('#')[-1]
    if s:
        # This is the second test
        print("yes")
        print(head)
        print(tail)
        content = ' ' + head + mid2 + tail
        print(content)
        print(i)
    else:
        print("no")


def test_file():
    file = open('translate_block.py', 'r')
    lines = file.readlines()
    print(lines)
    # This is the third test
    for line in lines:
        if re.findall('#', line, re.S):
            print(line)

    def file_name(self, path, all_files):
        # First traverse all files and folders in the current directory
        file_list = os.listdir(path)
        # Prepare to loop to determine whether each element is a folder or a file. If it is a file, pass the name to
        # the list. If it is a folder, recursively
        for file in file_list:
            # Use the os.path.join() method to get the full name of the path and store it in the cur_path variable,
            # otherwise you can only traverse one level of directory each time
            cur_path = os.path.join(path, file)
            # Determine whether it is a folder
            if os.path.isdir(cur_path):
                self.file_name(cur_path, all_files)
            else:
                all_files.append(cur_path)
        return all_files


def test_split():
    i = "#\n"

    if not (i.split('#')[-1].replace('\n', '').strip() is ''):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    test_split()
    print(str(__file__).split('/')[-1].split('.')[0])
