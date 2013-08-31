import os
import sys
from cStringIO import StringIO

from PIL import Image

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pipeline import Pipeline
from pipeline.utils import StopPipeline

from imgproc import soura_handler, ayat_handler, layout_handler, DATA_DIRECTORY

OUTPUT_DIRECTORY = os.path.join(DATA_DIRECTORY, 'output')


def open_pdf_file(pdf_file, password=''):
    # Create a PDF parser object associated with the file object.
    pdf_file_parser = PDFParser(pdf_file)
    # Create a PDF document object that stores the document structure.
    pdf_file_document = PDFDocument()
    # Connect the parser and document objects.
    pdf_file_parser.set_document(pdf_file_document)
    pdf_file_document.set_parser(pdf_file_parser)
    # Supply the password for initialization.
    # (If no password is set, give an empty string.)
    pdf_file_document.initialize(password)
    return pdf_file_document


def retrive_page_as_image(pdf_file_document):
    '''
    recursively get the image from the pdf page resources, extract binary, &
    wrap it into StringIO, open as PIL
    '''
    index = 0
    for page in pdf_file_document.get_pages():
        raw_img = page.resources['XObject']['Im0'].resolve().get_rawdata()
        pil_img = Image.open(StringIO(raw_img))
        layout = pil_img.copy()
        yield pil_img, index, layout, page
        index += 1


def pipeline_provider(image_generator):
    try:
        return image_generator.next(), image_generator
    except:
        raise StopPipeline("file ended")


def pipeline_validator((image, index, layout, page)):
    '''
    return False for pages that should not be processed, else return True
    '''
    if index > 4 and index < 607:
        return True
    else:
        return False


def pipeline_consumer((image, index, layout, page)):
    # TODO: write the edited images directly to the pdf file instead of just
    # writing them to the disk
    layout.save(OUTPUT_DIRECTORY + '/' + str(index).zfill(3) + '.jpg', 'JPEG')
    return


def main(input_file_path, output_file_path):
    pdf_file = open_pdf_file(open(input_file_path, 'rwb'))

    image_processor = Pipeline(pipeline_provider,
                               [layout_handler, ayat_handler, soura_handler],
                               pipeline_consumer, pipeline_validator)
    image_processor.follow(retrive_page_as_image(pdf_file))
    print 'success'


if __name__ == '__main__':
    try:
        input_file_path = sys.argv[1]
    except IndexError:
        print "please enter the pdf file path"
        input_file_path = raw_input()

    output_file_path = input_file_path.split('/')
    output_file_path[-1] = "output_" + output_file_path[-1]
    output_file_path = '/'.join(output_file_path)

    main(input_file_path, output_file_path)
