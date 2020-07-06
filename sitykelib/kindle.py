import os
import string

def list_disk():
    # 盘符只可能是从A到Z
    # 直接枚举吧
    disks = []
    for possibleDriveLetter in string.ascii_uppercase:
        possibleDrivePath = possibleDriveLetter+":\\"
        if os.path.isdir(possibleDrivePath):
            disks.append(possibleDrivePath)
    return disks

def judge_kindle(disk):
    # 貌似所有的kindle都会有这个文件夹呢
    # 话说连这个都没有的话那要怎么拷贝文件呢?
    allDir = os.listdir(disk)
    judgement = "documents"
    return judgement in allDir

def list_kindle():
    
    kindles = []
    disks = list_disk()
    for disk in disks:
        if judge_kindle(disk):
            kindles.append(disk)
    return kindles

def send_to_kindle(files, kindle):
    destination = kindle+"documents\\"
    assert(os.path.isdir(destination))
    for f in files:
        os.system("copy"+' "'+f+'" '+destination)