#!/usr/bin/env python

'''
rename papers with their titles 
'''

from pyPdf import PdfFileWriter, PdfFileReader

def get_pdf_title(pdf_file_path):
    f = open(pdf_file_path)
    pdf_reader = PdfFileReader(f) 
    return pdf_reader.getDocumentInfo().title

title = get_pdf_title('./test.pdf')
