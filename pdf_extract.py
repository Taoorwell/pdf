import os
import argparse
from PyPDF2 import PdfFileReader,PdfFileWriter, PdfFileMerger

parser = argparse.ArgumentParser()
parser.add_argument("path", help="pdf path and name, string", type=str)
parser.add_argument("start_page", help="start page extracted", type=int)
parser.add_argument("end_page", help="end page extracted", type=int)
args = parser.parse_args()

path = args.path
start_page = args.start_page
end_page = args.end_page


def pdf_extract(path, start_page, end_page):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for page in range(start_page-1, end_page):
        pdf_writer.addPage(pdf.getPage(page))
    output_filename = "{}_page_{}-{}.pdf".format(fname, start_page, end_page)
    with open('merge/'+ output_filename, "wb") as out:
        pdf_writer.write(out)
    print("Create:{}".format(output_filename))

if __name__ == "__main__":
    try:
        pdf_extract(path, start_page, end_page)
    except:
        print("Please Check Function Help, 'python pdf_extract.py -h'")

