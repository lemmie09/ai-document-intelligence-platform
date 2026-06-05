from pypdf import PdfReader


class PDFLoader:
    def load(self, file_path: str) -> str:
        """
        Load a PDF and return all extracted text.
        """

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text