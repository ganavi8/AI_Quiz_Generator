from pypdf import PdfReader



# ---------------- READ PDF ---------------- #

def read_pdf(uploaded_file):

    text = ""


    try:

        pdf = PdfReader(uploaded_file)


        for page in pdf.pages:

            page_text = page.extract_text()


            if page_text:

                text += page_text + "\n"



        return text



    except Exception as e:

        raise Exception(
            f"PDF reading error: {e}"
        )





# ---------------- READ TXT ---------------- #

def read_txt(uploaded_file):


    try:

        text = uploaded_file.read()


        return text.decode(
            "utf-8"
        )



    except Exception as e:

        raise Exception(
            f"TXT reading error: {e}"
        )