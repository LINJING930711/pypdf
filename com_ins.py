#!/usr/bin/env python

'''
Combine pdf files and insert bookmarks. 
'''

import os, sys, codecs
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def getfilenames(filepath='', filelist_out=[], file_ext='all'):
    for fpath, dirs, fs in os.walk(filepath):
	for f in fs:
	    fi_d = os.path.join(fpath, f)
	    if file_ext == 'all':
		filelist_out.append(fi_d)
	    elif os.path.splitext(fi_d)[1] == file_ext:
		filelist_out.append(fi_d)
	    else:
		pass
    return filelist_out


def mergerfiles(path, output_filename, import_bookmarks=False):
    merger = PdfFileMerger()
    filelist = getfilenames(filepath=path, file_ext='.pdf')
    if len(filelist) == 0:
	print "No files found"
	sys.exit()
    for filename in filelist:
	f = codecs.open(filename, 'rb')
	file_rd = PdfFileReader(f)
        short_filename = os.path.basename(os.path.splitext(filename)[0])
	if file_rd.isEncrypted == True:
	    print "File Encrypted: %s" %(filename)
	    continue
        merger.append(file_rd, bookmark=short_filename, import_bookmarks=import_bookmarks)
	print "Combine file: %s" %(filename)
	f.close()
    out_filename = os.path.join(os.path.abspath(path), output_filename)
    merger.write(out_filename)
    print "Combined files' name: %s" %(out_filename)
    merger.close()

if __name__=="__main__":
    path = "./"
    output_filename = "Test"
    mergerfiles(path, output_filename, import_bookmarks=True)











