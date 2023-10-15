import os

def extsort(file_list):

    sorted_files = sorted(file_list, key=lambda x: os.path.splitext(x)[1])
    return sorted_files


file_list = ['file.txt', 'image.png', 'document.doc', 'script.py', 'data.csv']
sorted_files = extsort(file_list)
print(sorted_files)
