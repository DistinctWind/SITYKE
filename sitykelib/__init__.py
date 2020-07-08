from sitykelib.imports import *
import os

cwd = os.getcwd()

def delete_output_files(outputFiles):
    for outputFile in outputFiles:
        os.system("del "+'"'+outputFile+'"')

def main():
    outputFiles = []

    pptfiles = search_ppt(cwd)
    if pptfiles!=[]:
        os.system("taskkill /im POWERPNT.EXE /f")
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

    docfiles = search_doc(cwd)
    if docfiles!=[]:
        os.system("taskkill /im WINWORD.EXE /f")
        word = init_word()
        for docfile in docfiles:
            fileName = perfix(docfile)
            inputFileName = docfile
            outputFileName = fileName+".pdf"
            inputFilePath = cwd+'\\'+inputFileName
            outputFilePath = cwd+'\\'+outputFileName
            outputFiles.append(outputFilePath)
            doc2pdf(word, inputFilePath, outputFilePath)
        os.system("taskkill /im WINWORD.EXE /f")

    if outputFiles==[]:
        print("请把需要转化的文件放到该目录下")
        exit()

    kindles = list_kindle()
    if len(kindles)==1:
        send_to_kindle(outputFiles, kindles[0])
        delete_output_files(outputFiles)
    elif len(kindles)==0:
        print("没有检测到kindle，复制取消")
    else:
        print("请自行复制或退出其他kindle再运行此程序")