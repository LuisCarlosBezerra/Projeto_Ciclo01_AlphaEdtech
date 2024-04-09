import cv2
import pytesseract as pt
import matplotlib.pyplot as plt


class TextExtractor:
    """
    TextExtractor is a class designed to extract text from images using pytesseract and OpenCV.

    Attributes:
        tessdata_dir (str): The directory containing the Tesseract data files.
        language (str): The language used for text recognition.
        psm (int): Page segmentation mode (PSM) for Tesseract.
    """

    def __init__(self, tessdata_dir="tessdata", language="por", psm=6):
        """
        Initialize the TextExtractor object.

        Args:
            tessdata_dir (str, optional): Directory containing the Tesseract data files.
                Defaults to "tessdata".
            language (str, optional): Language used for text recognition. Defaults to "por" (Portuguese).
            psm (int, optional): Page segmentation mode (PSM) for Tesseract. Defaults to 6.
        """
        self.tessdata_dir = tessdata_dir
        self.language = language
        self.psm = psm

    def process_image(self, image_path):
        """
        Process the given image for better text extraction.

        Args:
            image_path (str): Path to the input image file.

        Returns:
            numpy.ndarray: Processed image.
        """
        # Read image
        img = cv2.imread(image_path, 0)

        # Apply Laplacian filter
        img_filtered = cv2.Laplacian(img, cv2.CV_8U)
        img_filtered = img_filtered + 20

        # Enhance image by subtracting Laplacian result from original image
        img_enhanced = cv2.subtract(img, img_filtered)

        return img_enhanced

    def extract_text_from_processed_image(self, processed_image):
        """
        Extract text from the processed image.

        Args:
            processed_image (numpy.ndarray): Processed image.

        Returns:
            str: Extracted text from the image.
        """
        # Configure Tesseract
        config_tess = f"--tessdata-dir {self.tessdata_dir} --psm {self.psm}"

        # Extract text using pytesseract
        extracted_text = pt.image_to_string(
            processed_image, lang=self.language, config=config_tess
        )

        return extracted_text

    def show_image_and_histogram(self, img):
        """
        Display image and its histogram side by side.

        Args:
            img (numpy.ndarray): Input image.
        """
        plt.figure(figsize=(12, 12))
        plt.subplot(121), plt.imshow(img, "gray"), plt.title("Image")
        plt.subplot(122), plt.hist(img.ravel(), 256, [0, 256]), plt.title("Histogram")
        plt.show()


# Example usage:
if __name__ == "__main__":
    text_extractor = TextExtractor()
    # image_path = "imagens-teste/print_livro2.png"
    image_path = "imagens-teste/imagem-baixada.jpg"

    # Process the image
    processed_image = text_extractor.process_image(image_path)

    # Extract text from the processed image
    extracted_text = text_extractor.extract_text_from_processed_image(processed_image)

    text_extractor.show_image_and_histogram(processed_image)

    print("Extracted Text:")
    print(extracted_text)
