import os
import comtypes.client

def init_powerpoint():
    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    return powerpoint

def ppt2pdf(powerpoint, inputFileName, outputFileName):
    if not outputFileName.endswith(".pdf"):
        outputFileName = outputFileName + ".pdf"
    ppt = powerpoint.Presentations.Open(inputFileName)
    ppt.ExportAsFixedFormat(outputFileName, 2)

def search_ppt(powerpoint, folder):
    files = os.listdir()
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx"))]
    return pptfiles
