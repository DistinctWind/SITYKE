import os

def show_ppt_list(ppt_list):
    if len(ppt_list)==0:
        print("没有找到演示文稿")
        return
    print("检索演示文稿：")
    for ppt_file_name in ppt_list:
        print(ppt_file_name)

def show_word_list(word_list):
    if len(word_list)==0:
        print("没有找到文字文稿")
        return
    print("检索文字文稿：")
    for word_file_name in word_list:
        print(word_file_name)

def show_kindle_list(kindles):
    print("Send to Kindles: ", end='')
    for i in range(0, len(kindles)):
        print(kindles[i].rstrip(':\\'), end='')
        if i != len(kindles)-1:
            print('|', end='')
    print('\n')

def delete_files(outputFiles):
    for outputFile in outputFiles:
        os.system("del "+'"'+outputFile+'"')