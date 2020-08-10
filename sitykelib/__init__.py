from sitykelib.imports import *
import os

cwd = os.getcwd()

def delete_output_files(outputFiles):
    for outputFile in outputFiles:
        os.system("del "+'"'+outputFile+'"')

def main():
    outputFiles = []

    pptfiles = search_ppt(cwd)
    show_ppt_list(pptfiles)
    if pptfiles!=[]:
        powerpoint = init_powerpoint()
        for pptfile in tqdm(pptfiles):
            fileName = perfix(pptfile)
            inputFileName = pptfile
            outputFileName = fileName+".pdf"
            inputFilePath = cwd+'\\'+inputFileName
            outputFilePath = cwd+'\\'+outputFileName
            outputFiles.append(outputFilePath)
            ppt2pdf(powerpoint, inputFilePath, outputFilePath)
        os.system("taskkill /im POWERPNT.EXE")

    docfiles = search_doc(cwd)
    show_word_list(docfiles)
    if docfiles!=[]:
        word = init_word()
        for docfile in tqdm(docfiles):
            fileName = perfix(docfile)
            inputFileName = docfile
            outputFileName = fileName+".pdf"
            inputFilePath = cwd+'\\'+inputFileName
            outputFilePath = cwd+'\\'+outputFileName
            outputFiles.append(outputFilePath)
            doc2pdf(word, inputFilePath, outputFilePath)
        os.system("taskkill /im WINWORD.EXE")

    if outputFiles==[]:
        print("请把需要转化的文件放到该目录下")
        exit()

    kindles = list_kindle()
    show_kindle_list(kindles)
    for kindle in kindles:
        send_to_kindle(outputFiles, kindle)
    delete_output_files(outputFiles)