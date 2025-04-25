from PyPDF2 import PdfMerger

def combine_pdfs(pdf_list):
    """
    Combines multiple PDF files into a single PDF file.
    
    Args:
        pdf_list (list): List of paths to the PDF files to be combined.
    """
    if not pdf_list:
        print("No PDF files provided.")
        return
    
    merger = PdfMerger()
    
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error appending {pdf}: {e}")
            continue
    
    # Specify the output file name
    first_file_name = pdf_list[0].split("/")[-1].split(".")[0]
    output_file = first_file_name + "_combined.pdf"
    
    try:
        merger.write(output_file)
        merger.close()
        print(f"Combined PDF saved as {output_file}")
    except Exception as e:
        print(f"Error writing combined PDF: {e}")
    
if __name__ == "__main__":
    # Example usage
    pdf_files = []
    while True:
        pdf_files.append(input("Enter the path of PDF files to combine, leave blank to combine:"))
        if not pdf_files[-1]:
            pdf_files.pop()
            break
    if len(pdf_files) < 2:
        print("Not enough PDF files provided.")
        exit(1)
        
    # Remove any leading/trailing whitespace from file paths
    pdf_files = [pdf.strip() for pdf in pdf_files]
    
    # Combine the PDF files
    combine_pdfs(pdf_files)
    
    print("PDF files combined successfully.")
