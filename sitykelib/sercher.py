import os

def search_ppt(powerpoint, folder):
    files = os.listdir()
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    return pptfiles

