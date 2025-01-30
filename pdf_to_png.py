from pdf2image import convert_from_path
import os

def pdf_to_png(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to images
    pages = convert_from_path(pdf_path, 300)  # 300 DPI for better quality

    # Save each page as a PNG file
    for i, page in enumerate(pages):
        output_path = os.path.join(output_folder, f"page_{i+1}.png")
        page.save(output_path, "PNG")
        print(f"Saved page {i+1} as {output_path}")

# Main entry point
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_png.py <input_pdf_path> <output_folder>")
    else:
        pdf_path = sys.argv[1]
        output_folder = sys.argv[2]
        pdf_to_png(pdf_path, output_folder)
