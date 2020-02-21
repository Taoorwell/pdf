import os
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

parser = argparse.ArgumentParser()
parser.add_argument("output_path", help="output pdf file name and path", type=str)
parser.add_argument("paths", help="pdf file folder path, contained 2 or above pdf file needed extract",
type=str)
args = parser.parse_args()

output_path = args.output_path
paths = args.paths

def pdf_merger(output_path, paths):
    input_paths = os.listdir(paths)
    pdf_merger = PdfFileMerger()
    file_hands = []
    for path in input_paths:
        pdf_merger.append(path)
    with open(output_path, "wb") as fileobj:
        pdf_merger.write(fileobj)
    print("Mergering Finish: {}".format(output_path))

if __name__ == "__main__":
    pdf_merger(output_path, paths)


