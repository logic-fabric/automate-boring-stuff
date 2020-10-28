"""Module implementing utility functions to :
- combine PDF pages
- rotate PDF pages
- watermark PDF pages
- encrypt a PDF
"""

import PyPDF2


def combine_pdf(pdf_file_1, pdf_file_2, combined_pdf_file='combined.pdf'):
    """Create a new PDF with the pdf_file_1 pages befor padf_file_2 pages.
    """
    try:
        with open(pdf_file_1, 'rb') as pdf_1:
            with open(pdf_file_2, 'rb') as pdf_2:
                pdf_reader_1 = PyPDF2.PdfFileReader(pdf_1)
                pdf_reader_2 = PyPDF2.PdfFileReader(pdf_2)

                pdf_writer = PyPDF2.PdfFileWriter()

                for page_nb in range(pdf_reader_1.numPages):
                    page = pdf_reader_1.getPage(page_nb)
                    pdf_writer.addPage(page)

                for page_nb in range(pdf_reader_2.numPages):
                    page = pdf_reader_2.getPage(page_nb)
                    pdf_writer.addPage(page)

                with open(combined_pdf_file, 'wb') as combined_pdf:
                    pdf_writer.write(combined_pdf)

    except FileNotFoundError:
        print(f"Check that '{pdf_file_1}' and '{pdf_file_2}' are in the current folder.")

def rotate_pdf_pages(pdf_file, angle=90, pages=None):
    """Clockwise rotate every pages of a PDF that are in the list 'pages'.
    If 'pages' is None, all pages are rotated.
    """
    pass

def watermark_pdf_pages(pdf_file, watermark_file, pages=None):
    """Merge every pages of a PDF that are in the list 'pages' with a watermark given in another PDF.
    If 'pages' is None, all pages are watermarked.
    """
    pass

def encrypt_pdf(pdf_file, user_password, owner_password=None):
    """Encrypt a PDF: a 'user_password' is needed to read it and a 'owner_password' is needed for other operations.
    If no 'owner_password' is passed, it will be the same as the 'user_password'.
    """
    pass


if __name__ == '__main__':
    combine_pdf('watermark.pdf', 'minutes.pdf')
