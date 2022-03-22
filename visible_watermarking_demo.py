from visible_watermarking import VisibleWatermarking

visible_watermaking_maker = VisibleWatermarking(orig_image_path='fox.jpg',
                                                watermark_path='logo.png',
                                                alpha=0.5)
watermarked_image = visible_watermaking_maker.visible_watermarking()
cv.imwrite('watermarked.jpg', watermarked_image)
