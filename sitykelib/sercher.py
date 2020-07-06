import os

def perfix(fileName):
    return fileName[:fileName.rfind('.')]

def suffix(fileName):
    return fileName[fileName.rfind('.'):]

def search_ppt(folder):
    files = os.listdir()
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    return pptfiles

