import cv2

def load_image(path: str):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Could not load image from: {path}")
    return image
def save_image(image, path: str):
    success = cv2.imwrite(path, image)
    if not success:
        raise ValueError(f"Could nt save image to: {path}")


