from sitykelib.imports import *
import os

cwd = os.getcwd()

def main():
    allFiles = []
    pptfiles = search_ppt(cwd)
    powerpoint = init_powerpoint()

    for pptfile in pptfiles:
        fileName = perfix(pptfile)
        allFiles.append(fileName+".pdf")
        ppt2pdf(powerpoint, pptfile, fileName+".pdf")

    kindles = list_kindle()
    if len(kindles)==1:
        send_to_kindle(allFiles, kindles[0])
    