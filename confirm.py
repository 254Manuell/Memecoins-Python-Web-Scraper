import PyPDF2
import re
from collections import defaultdict
from pprint import pprint

def extract_memecoins_from_pdf(pdf_path):
    memecoins = []
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"--- Content of page {i+1} ---")
            print(text)
            print("--- End of page ---\n")
            
            # Use regex to find memecoin names and dates
            matches = re.findall(r'(\w+(?:\s\w+)*)\s+(\d{4}-\d{2}-\d{2})', text)
            memecoins.extend(matches)
    
    return memecoins

def get_duplicates(coin_list):
    coin_dict = defaultdict(list)
    
    for coin, date in coin_list:
        coin_dict[coin].append(date)
    
    duplicates = {coin: dates for coin, dates in coin_dict.items() if len(dates) > 1}
    
    return duplicates

# Use raw string notation for the file path
pdf_path = r'c:\Users\Admin\Desktop\scraper\Memecoins with Creation Dates.pdf'

try:
    # Extract memecoins from the PDF
    memecoins = extract_memecoins_from_pdf(pdf_path)

    print(f"Number of memecoins found: {len(memecoins)}")
    print("First few memecoins found (if any):")
    pprint(memecoins[:5])

    # Get the duplicates
    duplicate_memecoins = get_duplicates(memecoins)

    # Print the results
    print("\nDuplicate memecoins and their creation dates:")
    pprint(duplicate_memecoins)

    # Print the count of unique memecoins
    unique_memecoins = len(set(coin for coin, _ in memecoins))
    print(f"\nNumber of unique memecoins: {unique_memecoins}")

except FileNotFoundError:
    print(f"Error: The file '{pdf_path}' was not found.")
except PyPDF2.errors.PdfReadError:
    print(f"Error: Unable to read the PDF file. Make sure it's a valid PDF.")
except Exception as e:
    print(f"An error occurred: {str(e)}")