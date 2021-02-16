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

    if args.modify_pdf:
        assert(os.path.isfile('k2pdfopt.exe'))
        if args.cut_ppt:
            pptfiles = cut_ppt(pptfiles)
        if args.reform_doc:
            docfiles = reform_doc(docfiles)
        if args.dark_mode:
            dark_mode(pptfiles+docfiles)

    kindles = list_kindle()
    show_kindle_list(kindles)
    for kindle in kindles:
        send_to_kindle(kindle)
    
    if args.delete_output_files:
        delete_output_files(outputFiles)

    os.system("pause")