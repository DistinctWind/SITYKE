import os

def perfix(fileName):
    return fileName[:fileName.rfind('.')]

def suffix(fileName):
    return fileName[fileName.rfind('.'):]

def search_ppt(folder):
    files = os.listdir(folder)
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    return pptfiles

def search_doc(folder):
    files = os.listdir(folder)
    docfiles = [f for f in files if f.endswith((".doc", ".docx"))]
    return docfiles