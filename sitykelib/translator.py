from win32com.client import Dispatch

def init_powerpoint():
    powerpoint = Dispatch("Powerpoint.Application")
    return powerpoint

def init_word():
    word = Dispatch("Word.Application")
    return word

def ppt2pdf(powerpoint, inputFileName, outputFileName):
    if not outputFileName.endswith(".pdf"):
        outputFileName = outputFileName + ".pdf"
    ppt = powerpoint.Presentations.Open(inputFileName)
    ppt.ExportAsFixedFormat(outputFileName, 2, PrintRange=None)
    ppt.Close()

def doc2pdf(word, inputFileName, outputFileName):
    if not outputFileName.endswith(".pdf"):
        outputFileName = outputFileName + ".pdf"
    doc = word.Documents.Open(inputFileName)
    doc.ExportAsFixedFormat(outputFileName, 17)
    # 传说，17是wdExportFormatPDF的值
    # 那就这样用吧！
    doc.Close()