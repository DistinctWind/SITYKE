import os
import string

def list_disk():
    disks = []
    for possibleDriveLetter in string.ascii_uppercase:
        if os.path.isdir(possibleDriveLetter+':\\'):
            disks.append(possibleDriveLetter)
    return disks
