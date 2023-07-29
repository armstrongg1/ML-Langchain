from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PdfReader(pdf_file_obj)


    page = pdf_reader.pages[1]
    text = page.extract_text()
    print(text)
    #for page_num in range(len(pdf_reader.pages)):
        #page_obj = pdf_reader.getPage(page_num)
        #text += page_num.extractText()
        #print(page_num.extract_text())

    #pdf_file_obj.close()
    #return text

# Use a função para extrair o texto de um PDF
file_path = r"C:\trabalho_upwork\langchan_course\pdf_files\pdfs\FINAL_DRAFT_WITH_WITHOUT_REMOVAL_DEPRECIATION_REPORT_20230708_2 (1).pdf"
print(extract_text_from_pdf(file_path))