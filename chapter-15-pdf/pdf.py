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
        print(f"Check that '{pdf_file_1}' and '{pdf_file_2}' are in the current folder to combine them.")

def rotate_pdf_pages(pdf_file, angle=90, pages=None):
    """Clockwise rotate every pages of a PDF that are in the list 'pages'.
    If 'pages' is None, all pages are rotated.
    """
    if angle % 90:
        raise ValueError(f"'angle' must be a multiple of 90 to rotate '{pdf_file}' pages.")

    try:
        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfFileReader(pdf)

            if pages is None:
                pages = [n for n in range(pdf_reader.numPages)]
            else:
                pages = [n - 1 for n in pages]
            
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_nb in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_nb)

                if page_nb in pages:
                    page.rotateClockwise(angle)

                pdf_writer.addPage(page)
            
            with open(f'rotated-{pdf_file}', 'wb') as rotated_pdf:
                pdf_writer.write(rotated_pdf)

    except FileNotFoundError:
        print(f"Check that '{pdf_file}' is in the current folder to rotate its pages.'")

def watermark_pdf_pages(pdf_file, watermark_file, pages=None):
    """Merge every pages of a PDF that are in the list 'pages' with a watermark given as the first page of another PDF.
    If 'pages' is None, all pages are watermarked.
    """
    try:
        with open(pdf_file, 'rb') as pdf:
            with open(watermark_file, 'rb') as watermark:
                pdf_reader = PyPDF2.PdfFileReader(pdf)
                watermark_reader = PyPDF2.PdfFileReader(watermark)
                watermark = watermark_reader.getPage(0)

                if pages is None:
                    pages = [n for n in range(pdf_reader.numPages)]
                else:
                    pages = [n - 1 for n in pages]

                pdf_writer = PyPDF2.PdfFileWriter()
                
                for page_nb in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_nb)

                    if page_nb in pages:
                        page.mergePage(watermark)

                    pdf_writer.addPage(page)
                
                with open(f'watermarked-{pdf_file}', 'wb') as watermarked_pdf:
                    pdf_writer.write(watermarked_pdf)

    except FileNotFoundError:
        print(f"Check that '{pdf_file}' and '{watermark_file}' are in the current folder to do the watermarking.")

def encrypt_pdf(pdf_file, user_password, owner_password=None):
    """Encrypt a PDF: a 'user_password' is needed to read it and a 'owner_password' is needed for other operations.
    If no 'owner_password' is passed, it will be the same as the 'user_password'.
    """
    if not user_password:
        raise ValueError(f"'user_password' must be a non empty string to encrypt '{pdf_file}'.")

    try:
        with open(pdf_file, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            pdf_writer = PyPDF2.PdfFileWriter()
            
            for page_nb in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_nb)
                pdf_writer.addPage(page)
            
            if owner_password is None:
                owner_password = user_password
            
            pdf_writer.encrypt(user_password, owner_password)

            with open(f'encrypted-{pdf_file}', 'wb') as encrypted_pdf:
                pdf_writer.write(encrypted_pdf)

    except FileNotFoundError:
        print(f"Check that '{pdf_file}' is in the current folder to be encrypted.")


if __name__ == '__main__':
    encrypt_pdf('minutes.pdf', '')
