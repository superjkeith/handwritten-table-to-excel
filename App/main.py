from App.utils.file_io import load_image, save_image
from App.Capture.crop import crop_image
from App.Capture.straighten import straighten_image
from App.Capture.quality_check import check_image_quality
from App.excel_export import export_to_excel

def main():
    input_path = "data/raw/sample.jpg"
    processed_image_path = "data/processed/cleaned_sample.jpg"
    excel_output_path = "data/processed/output.xlsx"
    image = load_image(input_path)
    print("after load:", type(image))

    image = crop_image(image)
    print("after crop:", type(image))

    image = straighten_image(image)
    print("after straighten:", type(image))

    quality = check_image_quality(image)
    print("Quality check: ", quality)
    save_image(image, processed_image_path)
    sample_rows = [["Name", "Hours", "Pay"],
                   ["Justin", "10", "250"],
                   ["Mike", "8", "200"]]
    export_to_excel(sample_rows, excel_output_path)
    print(f"""Saved cleaned image to: {processed_image_path}
               saved excel file to: {excel_output_path}""")

if __name__ == "__main__":
    main()
    