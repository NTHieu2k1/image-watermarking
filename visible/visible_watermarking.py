import cv2 as cv
import numpy as np


class VisibleWatermarking:
    def __init__(self, orig_image_path, watermark_path, alpha=1.0):
        self.image = cv.imread(orig_image_path)
        self.watermark = cv.imread(watermark_path)
        self._alpha = alpha
        self.image_shape = self.image.shape
        self.watermark_shape = self.watermark.shape

    @property
    def alpha(self) -> float:
        return self._alpha

    @alpha.setter
    def alpha(self, new_alpha: float):
        self._alpha = new_alpha

    def visible_watermarking(self) -> np.ndarray:
        """
        Implement visible watermarking on an original image.
        :return: ndarray: A watermarked image.
        """
        # Retrieve height and width of original image and watermark
        image_height, image_width = self.image_shape[:2]
        watermark_height, watermark_width = self.watermark_shape[:2]
        # Extract a region of the image as a patch, which has the same size of the watermark
        patch = self.image[-20-watermark_height:-20, -20-watermark_width:-20, :]
        # Implement visible watermarking on the patch extracted first
        watermark_patch = cv.addWeighted(self.watermark, self.alpha, patch, 1 - self.alpha, 0)
        # Apply watermarked patch to the image
        final_image = self.image.copy()
        final_image[-20-watermark_height:-20, -20-watermark_width:-20, :] = watermark_patch
        return final_image
