from sitykelib.imports import *
import os

cwd = os.getcwd()

def main():
    allFiles = []
    pptfiles = search_ppt(cwd)
    powerpoint = init_powerpoint()
    for pptfile in pptfiles:
        fullpath = os.path.join(cwd, pptfile)
        allFiles.append(fullpath)
        ppt2pdf(powerpoint, fullpath, fullpath)
    kindles = list_kindle()
    if len(kindles)==1:
        send_to_kindle(allFiles, kindles[0])
    