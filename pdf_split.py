import os
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

parser = argparse.ArgumentParser()
parser.add_argument("path", help="pdf file name and path", type=str)
args = parser.parse_args()

path = args.path

def pdf_split(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = "{}_page_{}.pdf".format(fname, page+1)
        with open(output_filename, "wb") as out:
            pdf_writer.write(out)
        print("Create:{}".format(output_filename))
if __name__ == "__main__":
    pdf_split(path)
