#!/usr/bin/env python

'''
rename papers with their titles 
'''

from PyPDF2 import PdfFileReader
import os

def get_pdf_title(pdf_file_path):
    f = open(pdf_file_path)
    pdf_reader = PdfFileReader(f) 
    filename = os.path.splitext(pdf_file_path)[0]
    if pdf_reader.isEncrypted:
	print "%s encypted" %filename
	return None
    else:
        return pdf_reader.getDocumentInfo().title

def rename_title(path):
    i = 0
    filelist = os.listdir(path)
    for files in filelist:
	print i
	i = i + 1 
	olddir = os.path.join(path,files)
	if os.path.isdir(olddir):
	    continue
	filename = get_pdf_title(olddir)
	print filename
	if filename == None:
	    pass
	else:
	    filetype = os.path.splitext(files)[1]
	    newdir = os.path.join(path,filename+filetype)
	    os.rename(olddir,newdir)
	    continue


if __name__=="__main__":
    path = "../Projector/"
    rename_title(path)



