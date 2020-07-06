import os
import string

def list_disk():
    disks = []
    for possibleDriveLetter in string.ascii_uppercase:
        if os.path.isdir(possibleDriveLetter+':\\'):
            disks.append(possibleDriveLetter)
    return disks

def judge_kindle(disk):
    allDir = os.listdir(disk)
    judgement = "documents"
    return judgement in allDir