from sitykelib.imports import *
import os

cwd = os.getcwd()

if __name__ == "__main__":
    pptfiles = search_ppt(cwd)
    powerpoint = init_powerpoint()
    for pptfile in pptfiles:
        fullpath = os.path.join(cwd, pptfile)
        ppt2pdf(powerpoint, fullpath, fullpath)