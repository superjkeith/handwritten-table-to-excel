from App.utils.file_io import load_image, save_image
from App.Capture.crop import crop_image
from App.Capture.straighten import straighten_image
from App.Capture.quality_check import check_image_quality
from App.excel_export import export_to_excel

def main():
    input_path = "data/raw/sample.jpg"
    processed_image_path = "data/processed/cleaned_sample.jpg"
    