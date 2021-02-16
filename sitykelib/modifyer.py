from sitykelib.sercher import perfix
import os

def get_pdf_name(original_name):
    return perfix(original_name)+'.pdf'

def cut_ppt(pptfiles):
    new_pptfiles = list()
    arg = ' -fc- -odpi 300 -mode copy -w 1364 -h 1016 -o [Cut]%s '
    for pptfile in pptfiles:
        pdfname = get_pdf_name(pptfile)
        os.system('k2pdfopt'+arg+'"'+pdfname+'"')
        new_pptfiles.append('[Cut]'+pptfile)
    return new_pptfiles

def reform_doc(docfiles):
    new_docfiles = list()
    arg = ' -fc- -odpi 300 -o [Reformed]%s '
    for docfile in docfiles:
        pdfname = get_pdf_name(docfile)
        os.system('k2pdfopt'+arg+'"'+pdfname+'"')
        new_docfiles.append('[Reformed]'+docfile)
    return new_docfiles

def dark_mode(pdffiles):
    arg = ' -fc- -odpi 300 -mode copy -neg -o [Dark]%s '
    for file in pdffiles:
        pdfname = get_pdf_name(file)
        os.system('k2pdfopt'+arg+'"'+pdfname+'"')