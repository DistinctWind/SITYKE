from sitykelib.argparser import start_argparse
from sitykelib.imports import *
import os

cwd = os.getcwd()
args = start_argparse()

def main():
    outputFiles = []

    pptfiles = search_ppt_with_args(cwd, args)
    if pptfiles!=[]:
        powerpoint = init_powerpoint()
        for pptfile in tqdm(pptfiles, ncols=50):
            fileName = perfix(pptfile)
            inputFileName = pptfile
            outputFileName = fileName+".pdf"
            #inputFilePath = cwd+'\\'+inputFileName
            #outputFilePath = cwd+'\\'+outputFileName
            inputFilePath = os.sep.join([cwd, inputFileName])
            outputFilePath = os.sep.join([cwd, outputFileName])
            outputFiles.append(outputFilePath)
            ppt2pdf(powerpoint, inputFilePath, outputFilePath)

    docfiles = search_doc_with_args(cwd, args)
    if docfiles!=[]:
        word = init_word()
        for docfile in tqdm(docfiles, ncols=50):
            fileName = perfix(docfile)
            inputFileName = docfile
            outputFileName = fileName+".pdf"
            #inputFilePath = cwd+'\\'+inputFileName
            #outputFilePath = cwd+'\\'+outputFileName
            inputFilePath = os.sep.join([cwd, inputFileName])
            outputFilePath = os.sep.join([cwd, outputFileName])
            outputFiles.append(outputFilePath)
            doc2pdf(word, inputFilePath, outputFilePath)

    if len(outputFiles)==0:
        print("复制.pdf文件")
    kindles = list_kindle()
    show_kindle_list(kindles)
    for kindle in kindles:
        send_to_kindle(kindle)
    
    if args.delete_output_files:
        delete_output_files(outputFiles)

    os.system("pause")