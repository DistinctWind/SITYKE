from sitykelib.imports import *
import os

cwd = os.getcwd()

def main():
    outputFiles = []

    pptfiles = search_ppt(cwd)
    powerpoint = init_powerpoint()
    for pptfile in pptfiles:
        fileName = perfix(pptfile)
        inputFileName = pptfile
        outputFileName = fileName+".pdf"
        inputFilePath = cwd+'\\'+inputFileName
        outputFilePath = cwd+'\\'+outputFileName
        outputFiles.append(outputFilePath)
        ppt2pdf(powerpoint, inputFilePath, outputFilePath)
    os.system("taskkill /im POWERPNT.EXE /f")

    kindles = list_kindle()
    if len(kindles)==1:
        send_to_kindle(outputFiles, kindles[0])
    elif len(kindles)==0:
        print("没有检测到kindle，复制取消")
    else:
        print("请自行复制或退出其他kindle再运行此程序")