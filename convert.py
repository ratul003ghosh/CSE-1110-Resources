import os
import glob
from pdf2docx import Converter

repo_dir = r'd:\UIU\uiu stuff\uga\CSE-1110-Resources'
pdf_files = glob.glob(os.path.join(repo_dir, '**', '*.pdf'), recursive=True)

for pdf_file in pdf_files:
    docx_file = pdf_file.replace('.pdf', '.docx')
    print(f'Converting {pdf_file} to {docx_file}')
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        os.remove(pdf_file)
    except Exception as e:
        print(f'Error converting {pdf_file}: {e}')
