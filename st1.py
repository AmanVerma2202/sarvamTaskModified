# import fitz  # PyMuPDF
#
#
# def extract_text_fonts_and_unicode(pdf_path):
#     doc = fitz.open(pdf_path)
#     text_with_fonts_and_unicode = []
#
#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num)
#         blocks = page.get_text("dict")["blocks"]  # Extract as dictionary
#
#         for block in blocks:
#             if "lines" in block:
#                 for line in block["lines"]:
#                     for span in line["spans"]:
#                         for char in span["text"]:
#                             text_with_fonts_and_unicode.append({
#                                 "char": char,
#                                 "font": span["font"],
#                                 "unicode_value": ord(char),
#                                 "size": span["size"],
#                                 "color": span["color"]
#                             })
#     return text_with_fonts_and_unicode
#
#
# def write_output_to_file(output_path, text_with_fonts_and_unicode):
#     with open(output_path, 'w', encoding='utf-8') as f:
#         for entry in text_with_fonts_and_unicode:
#             char = entry["char"]
#             font = entry["font"]
#             unicode_value = entry["unicode_value"]
#
#             f.write(
#                 f"Character: '{char}', Font: {font}, Unicode: {unicode_value}, Size: {entry['size']}, Color: {entry['color']}\n")
#
#
# def analyze_pdf_for_wrong_characters(pdf_path, output_path):
#     text_with_fonts_and_unicode = extract_text_fonts_and_unicode(pdf_path)
#     write_output_to_file(output_path, text_with_fonts_and_unicode)
#
#
# # Example usage
# pdf_path = "Apple_font_mapping_issue.pdf"
# output_path = "output.txt"
# analyze_pdf_for_wrong_characters(pdf_path, output_path)


# import os
# import fitz  # PyMuPDF
# import google.generativeai as genai
#
# # Path to your PDF file
# pdf_path = 'Apple_font_mapping_issue.pdf'
# output_path = "output.txt"
#
# # Configure the GenAI API directly with the API key
# genai.configure(api_key='AIzaSyCnbkJvCvFgaIzNfAkSnomJRXBLDO5aAxk')  # Replace with your actual API key
#
#
# def extract_text_fonts_and_unicode(pdf_path):
#     """Extracts text, fonts, Unicode, size, and color information from a PDF."""
#     doc = fitz.open(pdf_path)
#     text_with_fonts_and_unicode = []
#
#     for page_num in range(doc.page_count):
#         page = doc.load_page(page_num)
#         blocks = page.get_text("dict")["blocks"]  # Extract as dictionary
#
#         for block in blocks:
#             if "lines" in block:
#                 for line in block["lines"]:
#                     for span in line["spans"]:
#                         for char in span["text"]:
#                             text_with_fonts_and_unicode.append({
#                                 "char": char,
#                                 "font": span["font"],
#                                 "unicode_value": ord(char),
#                                 "size": span["size"],
#                                 "color": span["color"],
#                                 "bbox": span["bbox"],  # Add bounding box (position) info
#                                 "page_num": page_num + 1  # 1-based page number
#                             })
#     return text_with_fonts_and_unicode
#
#
# def write_output_to_file(output_path, text_with_fonts_and_unicode):
#     """Writes the extracted data into a text file."""
#     with open(output_path, 'w', encoding='utf-8') as f:
#         for entry in text_with_fonts_and_unicode:
#             char = entry["char"]
#             font = entry["font"]
#             unicode_value = entry["unicode_value"]
#
#             f.write(
#                 f"Character: '{char}', Font: {font}, Unicode: {unicode_value}, "
#                 f"Size: {entry['size']}, Color: {entry['color']}, "
#                 f"Position: {entry['bbox']}, Page: {entry['page_num']}\n"
#             )
#
#
# def send_text_to_gemini(text_data):
#     """Sends the extracted text and metadata to Gemini AI for further analysis."""
#     content = [
#         {
#             "text": "Analyze the following text and provide the Unicode, font style, color, and position of each character."},
#         {"text": text_data}
#     ]
#
#     # Create the model configuration
#     generation_config = {
#         "temperature": 1,
#         "top_p": 0.95,
#         "top_k": 64,
#         "max_output_tokens": 8192,
#         "response_mime_type": "text/plain",
#     }
#
#     # Initialize the model
#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-flash-8b-exp-0827",
#         generation_config=generation_config,
#     )
#
#     # Start a chat session
#     try:
#         chat_session = model.start_chat(history=[])
#         response = chat_session.send_message(content=content)
#         return response.text
#     except Exception as e:
#         print(f"Error during chat session: {e}")
#         return None
#
#
# def analyze_pdf_for_wrong_characters(pdf_path, output_path):
#     """Extracts text and metadata from the PDF, sends it to Gemini AI for analysis, and writes the results to a file."""
#     text_with_fonts_and_unicode = extract_text_fonts_and_unicode(pdf_path)
#
#     # Prepare text data for Gemini AI
#     text_data = ""
#     for entry in text_with_fonts_and_unicode:
#         text_data += (
#             f"Character: '{entry['char']}', Font: {entry['font']}, Unicode: {entry['unicode_value']}, "
#             f"Size: {entry['size']}, Color: {entry['color']}, Position: {entry['bbox']}, Page: {entry['page_num']}\n"
#         )
#
#     # Send extracted text data to Gemini AI
#     gemini_response = send_text_to_gemini(text_data)
#
#     if gemini_response:
#         # Write Gemini AI's response to the output file
#         with open(output_path, 'a', encoding='utf-8') as f:
#             f.write("\n\nGemini AI Analysis:\n")
#             f.write(gemini_response)
#     else:
#         print("Failed to get a response from Gemini AI.")
#
#     # Also write the initial extraction to the file
#     write_output_to_file(output_path, text_with_fonts_and_unicode)
#
#
# # Example usage
# analyze_pdf_for_wrong_characters(pdf_path, output_path)





import os
import fitz  # PyMuPDF
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Configure the GenAI API directly with the API key
genai.configure(api_key='AIzaSyCnbkJvCvFgaIzNfAkSnomJRXBLDO5aAxk')  # Replace with your actual API key


def extract_text_fonts_and_unicode(pdf_path):
    doc = fitz.open(pdf_path)
    text_with_fonts_and_unicode = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]  # Extract as dictionary

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        for char in span["text"]:
                            text_with_fonts_and_unicode.append({
                                "char": char,
                                "font": span["font"],
                                "unicode_value": ord(char),
                                "size": span["size"],
                                "color": span["color"],
                                "bbox": span["bbox"],
                                "page_num": page_num + 1
                            })
    return text_with_fonts_and_unicode


def send_text_to_gemini(text_data):
    content = [
        {"text": "Analyze the following text and provide the prper and correct Unicode, font style, color, and position of each character."},
        {"text": text_data}
    ]

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-8b-exp-0827",
        generation_config=generation_config,
    )

    try:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(content=content)
        return response.text
    except Exception as e:
        print(f"Error during chat session: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        if 'pdf_file' not in request.files:
            return redirect(request.url)

        file = request.files['pdf_file']
        if file.filename == '':
            return redirect(request.url)

        if file:
            # Save the file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Process the PDF
            text_with_fonts_and_unicode = extract_text_fonts_and_unicode(file_path)

            # Prepare text data for Gemini AI
            text_data = ""
            for entry in text_with_fonts_and_unicode:
                text_data += (
                    f"Character: '{entry['char']}', Font: {entry['font']}, Unicode: {entry['unicode_value']}, "
                    f"Size: {entry['size']}, Color: {entry['color']}, Position: {entry['bbox']}, Page: {entry['page_num']}\n"
                )

            # Send to Gemini AI
            gemini_response = send_text_to_gemini(text_data)

            # Render results in the UI
            return render_template('index.html', response=gemini_response, filename=file.filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
