import re
from collections import defaultdict
import pandas as pd
import PyPDF2

def extract_memecoins_from_pdf(pdf_path):
    memecoins = []
    pattern = r'(\d+)\.\s*(.*?)\s*:\s*(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)'
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            for match in re.finditer(pattern, text):
                index, name, date = match.groups()
                memecoins.append((name.strip(), date))
    
    return memecoins

def extract_memecoins_from_excel(excel_path):
    df = pd.read_excel(excel_path)
    
    # Assuming the Excel file has columns 'Name' and 'Creation Date'
    # Adjust these column names if they're different in your Excel file
    memecoins = list(zip(df['Name'], df['Creation Date']))
    
    return memecoins

def find_missing_memecoins(pdf_memecoins, excel_memecoins):
    pdf_set = set(name for name, _ in pdf_memecoins)
    excel_set = set(name for name, _ in excel_memecoins)
    
    missing_memecoins = pdf_set - excel_set
    
    return list(missing_memecoins)

# File paths
pdf_path = 'c:\Users\Admin\Desktop\scraper\Memecoins with Creation Dates.pdf'  # Replace with your PDF file path
excel_path = 'c:\Users\Admin\Downloads\Memecoins_Creation_Dates.csv'  # Replace with your Excel file path

try:
    # Extract memecoins from PDF
    pdf_memecoins = extract_memecoins_from_pdf(pdf_path)
    print(f"Number of memecoins found in PDF: {len(pdf_memecoins)}")
    
    # Extract memecoins from Excel
    excel_memecoins = extract_memecoins_from_excel(excel_path)
    print(f"Number of memecoins found in Excel: {len(excel_memecoins)}")
    
    # Find missing memecoins
    missing_memecoins = find_missing_memecoins(pdf_memecoins, excel_memecoins)
    
    # Print results
    print("\nMemecoins present in PDF but absent in Excel:")
    for coin in missing_memecoins:
        print(coin)
    
    print(f"\nTotal number of missing memecoins: {len(missing_memecoins)}")

except FileNotFoundError as e:
    print(f"Error: File not found. {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")