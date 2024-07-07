from pypdf import PdfWriter,PdfReader
from file_process import process
import os

class pdfprocess(object):
    def __init__(self):
        self.data_list = process("pdf-data").final_name()
        self.writer_model = PdfWriter
        self.reader_model = PdfReader

    
    def merge(self,af_name):
        for pdf in self.data_list:
            self.writer_model.append(pdf)
        self.writer_model.write("{}.pdf".format(af_name))
        self.writer_model.close()


    def pdf_rot(self,rot:int,input_pdf:str,output_pdf:str):

        reader = self.reader_model(input_pdf)
        writer = self.writer_model()

        for i in range(len(reader.pages)):
            writer.add_page(reader.pages[i])
            # print(writer.pages[i])
            writer.pages[i].rotate(rot)
            
        with open(output_pdf, "wb") as fp:
            writer.write(fp)

    def pdf_narrow(self,page_num:int):
        

        pass

if __name__ == "__main__":
    pdfprocess().pdf_rot(rot=90,input_pdf=r"pdf-data\1.pdf",output_pdf=r"tmp-1.pdf")


    pass








