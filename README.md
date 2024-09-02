# sarvamTask
The PDF Unicode Extractor is a Flask-based web application that allows users to upload a PDF file and extract detailed information about character in the document. The extracted data is then sent to Google’s Gemini AI for further analysis and it returns the character's font, size, color, position, and Unicode value, and the results are displayed on the web page.



### Files
```
├── st1.py              # Main Flask application
├── templates/
│   └── index.html      # HTML template for the web interface
├── uploads/            # Directory where uploaded PDFs are stored
├── requirements.txt    # List of Python dependencies
└── README.md           # Project README file
```


## How to Run Locally

Clone the repository:

   ```bash
   git clone https://github.com/AmanVerma2202/sarvamTaskModified.git
   cd sarvamTaskModified
   pip install -r requirements.txt
   python st1.py
 ```

## Demo



## Photos
![Alt text of the image](https://github.com/AmanVerma2202/sarvamTaskModified/blob/main/Screenshot%20(97).png)
![Alt text of the image](https://github.com/AmanVerma2202/sarvamTaskModified/blob/main/Screenshot%20(98).png)
![Alt text of the image](https://github.com/AmanVerma2202/sarvamTaskModified/blob/main/Screenshot%20(99).png)


## Tech Stack

 **Python,Html,Flask,Fitz(PyMuPdf),Gemini API Key**

## Approach
Process PDF documents and analyze their content. The application starts by allowing users to upload a PDF file through a web interface built with Flask. Once the PDF is uploaded, the application leverages PyMuPDF (fitz) to parse the document and extract  each characters. This extracted data is then compiled into a structured format and sent to Google Gemini AI for further analysis. The AI model processes the data, providing insights into the characters' attributes such as its font, size, color, position, and Unicode value, which are then displayed on the web page in an organized manner. This approach integrates robust PDF processing with advanced AI capabilities, offering users a seamless experience to analyze document contents with precision.




## Features
**PDF Upload**: Users can upload any PDF file through the web interface.
**Character Extraction**: The application extracts each character from the PDF along with its associated metadata, such as font style, size, color, position, and Unicode value.
**AI Analysis**: The extracted data is sent to Google Gemini AI, which analyzes the text and provides additional insights.
**User-Friendly UI**: The results from the AI analysis are displayed in a clean and organized manner for easy understanding.



## Contributing
Feel free to submit issues, fork the repository, and send pull requests if you want to contribute.
