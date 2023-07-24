from rembg import remove
from PIL import Image

#open the input image
input_path = "C:\\Users\\yashr\\Projects\\Python_projetcs\\image.jpg"

input_image = Image.open(input_path)

output_image = remove(input_image)

output_path = "C:\\Users\\yashr\\Projects\\Python_projetcs\\out.png"

output_image.save(output_path)