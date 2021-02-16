from sitykelib.sercher import perfix
import os

def get_pdf_name(original_name):
    return perfix(original_name)+'.pdf'

def cut_ppt(pptfiles):
    new_pptfiles = list()
    arg = ' -mode copy -w 1364 -h 1016 -o [Cut]%s '
    for pptfile in pptfiles:
        pdfname = get_pdf_name(pptfile)
        os.system('k2pdfopt'+arg+'"'+pdfname+'"')
        new_pptfiles.append('[Cut]'+pptfile)
    return new_pptfiles

def reform_doc(docfiles):
    new_docfiles = list()
    arg = ' -o [Reformed]%s '
    for docfile in docfiles:
        pdfname = get_pdf_name(docfile)
        os.system('k2pdfopt'+arg+'"'+pdfname+'"')
        new_docfiles.append('[Reformed]'+docfile)
    return new_docfiles
