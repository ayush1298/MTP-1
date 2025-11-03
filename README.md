# NyayaFinder - FIR Analysis System

An intelligent FIR (First Information Report) analysis system that uses NLP and ML to identify relevant IPC sections from complaint text or images.

## 📋 Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **Tesseract OCR** (for image processing)
- **pip** (Python package manager)

## 🚀 Installation & Setup

### 1. Install Tesseract OCR

**For macOS:**
```bash
brew install tesseract
brew install tesseract-lang  # For Hindi language support
```

**For Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-hin  # For Hindi
```

**For Windows:**
Download and install from [GitHub Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

### 2. Clone the Repository
```bash
git clone <repository-url>
cd MTP-1
```

### 3. Navigate to the App Directory
```bash
cd App
```

### 4. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Update it to your actual path if different.

## 🏃 Running the Application

### Start the Flask Server
```bash
cd App
python app.py
```

The application will start on `http://localhost:5000`

### Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
MTP-1/
├── App/                          # Main Flask application
│   ├── app.py                    # Flask server
│   ├── SER.py                    # Semantic search using sentence transformers
│   ├── fine_tuned_llama2.py      # LLM query generation
│   ├── requirements.txt          # Python dependencies
│   ├── static/                   # CSS and static files
│   └── templates/                # HTML templates
├── Dataset/                      # Training and reference data
│   ├── ipc_sections.csv          # IPC sections database
│   └── TranslateData.csv         # Translated FIR data
├── Dataset_Scrapping/            # Web scraping scripts
│   ├── PDFDownload.py            # Download FIR PDFs
│   ├── PDF_to_text.py            # Extract text from PDFs
│   └── txt_to_xls.py             # Convert text to Excel
├── main.py                       # IPC section scraper
├── similarity.py                 # Text similarity functions
└── Summerizer.py                 # Text summarization
```

## 🔧 Features

- **Text Input:** Analyze FIR complaints in text format (Hindi/English)
- **Image Input:** Upload image of FIR document with OCR processing
- **Translation:** Automatic Hindi to English translation
- **IPC Section Identification:** Uses semantic search to find relevant IPC sections
- **LLM Analysis:** Generate detailed legal analysis using fine-tuned LLaMA 2

## 🛠️ Troubleshooting

### Issue: "Module not found" errors
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Tesseract not found
Make sure Tesseract is in your system PATH or update the path in the code.

### Issue: Excel file not found
Update the `excel_filepath` in [`App/SER.py`](App/SER.py) to match your file location.

### Issue: CUDA/GPU warnings
The application works on CPU. GPU is optional for faster processing.

## 📝 Usage

1. Open the application in your browser
2. Select input method (Text or Image)
3. Enter FIR complaint text or upload an image
4. Click "Process" to analyze
5. View identified IPC sections and legal analysis

## 🧪 Dataset Scraping (Optional)

To collect new FIR data:

```bash
cd Dataset_Scrapping
python PDFDownload.py      # Download FIR PDFs
python PDF_to_text.py      # Extract text from PDFs
python txt_to_xls.py       # Convert to Excel format
```

## 📊 Data Processing

To scrape IPC sections:
```bash
python main.py
```

To summarize FIR texts:
```bash
python Summerizer.py
```