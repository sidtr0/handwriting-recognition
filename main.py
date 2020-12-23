# adds image processing capabilities
from PIL import Image, ImageEnhance
# will convert the image to text string
import pytesseract

img = Image.open("/mnt/c/Users/sidtr/Documents/PythonProjects/handwriting-recognition/images_test/image1.jpg")

# adding some sharpness and contrast to the image 
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)

img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

img_edit.save("edited_image.png")

result = pytesseract.image_to_string(img_edit)

with open("image1_text.txt", mode ='w') as file:
    file.write(result)
    print('ready!')
    