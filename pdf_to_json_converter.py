#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Author : zayunsna [HK Jeon]
## tech-log : https://zayunsna.github.io/

import os
import glob
import json
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
from konlpy.tag import Kkma

def get_filelists(pdf_dir, json_dir):
    os.chdir(pdf_dir)
    pdf_filelist = set(os.path.splitext(file)[0] for file in glob.glob('*'))
    os.chdir(json_dir)
    json_filelist = set(os.path.splitext(file)[0] for file in glob.glob('*'))

    unique_files = pdf_filelist.symmetric_difference(json_filelist)

    return unique_files

def pdfReader_byPage(file_path):
    extract_texts = []
    count = 1

    for page_layout in extract_pages(file_path):
        page_text = ""
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                page_text += element.get_text()

        sentences = Kkma().sentences(page_text)
        out_sentences = ' '.join(sentences)
        extract_texts.append({"text": out_sentences,'page': count})
        count += 1

    return extract_texts


My_DIR = os.getcwd()
PDF_DIR = My_DIR+'/pdf/'
Json_DIR = My_DIR+'/json/'

filelist = get_filelists(PDF_DIR, Json_DIR)

print("#"*100)
print("PDF file path : ", PDF_DIR)
print("Result will be saved here : ", Json_DIR)
print("#"*100)
print(" The file that already converted and existed in /json/ dir will be skipped. ")
print("#"*100)
print(" Now On-progress, ")
for filename in filelist:
    print(" => ", filename)
    input_filename = PDF_DIR+filename+'.pdf'
    result = pdfReader_byPage(input_filename)
    result_filename = Json_DIR+filename+'.json'
    with open(result_filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

print("#"*100)
print(" Converting has been done !! ")
