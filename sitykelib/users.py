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
    print("文件将复制到kindle: ", end='')
    for kindle in kindles:
        print(kindle.rstrip(":\\"), end='|')
    print('\n')