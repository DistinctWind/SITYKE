import os

def perfix(fileName):
    return fileName[:fileName.rfind('.')]

def suffix(fileName):
    return fileName[fileName.rfind('.'):]

def search_ppt(folder):
    files = os.listdir(folder)
    pptfiles = [f for f in files if f.endswith((".ppt", ".pptx")) and not f.startswith("~$")]
    return pptfiles

def search_doc(folder):
    files = os.listdir(folder)
    docfiles = [f for f in files if f.endswith((".doc", ".docx")) and not f.startswith("~$")]
    return docfiles

def search_ppt_with_args(folder, args):
    files = os.listdir(folder)
    pptfiles = list()
    print('Searching for .ppt(x) files...')
    for file in files:
        if not file.endswith(('.ppt', '.pptx')):
            continue
        if file.startswith('~$'):
            continue
        if args.ignore_translated_files and os.path.isfile(perfix(file)+'.pdf'):
            print('[Ignored]'+file)
            continue
        print(file)
        pptfiles.append(file)
    return pptfiles
        
def search_doc_with_args(folder, args):
    files = os.listdir()
    docfiles = list()
    print('Searching for .doc(x) files...')
    for file in files:
        if not file.endswith(('.doc', '.docx')):
            continue
        if file.startswith('~$'):
            continue
        if args.ignore_translated_files and os.path.isfile(perfix(file)+'.pdf'):
            print('[Ignored]'+file)
            continue
        print(file)
        docfiles.append(file)
    return docfiles