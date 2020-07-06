from win32com.client import Dispatch

def init_powerpoint():
    powerpoint = Dispatch("Powerpoint.Application")
    return powerpoint

def ppt2pdf(powerpoint, inputFileName, outputFileName):
    if not outputFileName.endswith(".pdf"):
        outputFileName = outputFileName + ".pdf"
    ppt = powerpoint.Presentations.Open(inputFileName)
    ppt.ExportAsFixedFormat(outputFileName, 2, PrintRange=None)
    ppt.Close()