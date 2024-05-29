import cv2

def resize_image_to_fixed_height(image, fixed_height=900):
    original_height, original_width = image.shape[:2]
    ratio = fixed_height / original_height
    new_width = int(original_width * ratio)
    resized_image = cv2.resize(image, (new_width, fixed_height), interpolation=cv2.INTER_AREA)

    return resized_image
