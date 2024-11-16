import os
import io
from rembg import remove
from PIL import Image

# Đường dẫn đến thư mục chứa ảnh đầu vào và đầu ra
input_folder = r'C:\Users\Puppy_z4nx\Downloads\gg'
output_folder = r'C:\Users\Puppy_z4nx\Downloads\gg2'

# Đảm bảo thư mục đầu ra tồn tại
os.makedirs(output_folder, exist_ok=True)

# Lặp qua tất cả các file trong thư mục đầu vào
for img_file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, img_file)
    
    if not os.path.isfile(input_path):
        continue
    
    try:

        with open(input_path, 'rb') as file:
            img_data = remove(file.read())
        
        img = Image.open(io.BytesIO(img_data)).convert("RGBA")
        
        white_background = Image.new("RGB", img.size, (255, 255, 255))
        
        img_with_white_bg = Image.alpha_composite(white_background.convert("RGBA"), img).convert("RGB")
        
        # save
        output_filename, ext = os.path.splitext(img_file)
        output_path = os.path.join(output_folder, f"{output_filename}.jpg")
        img_with_white_bg.save(output_path, format="JPEG")
        
        print(f"Đã xử lý: {img_file} -> {output_path}")
    except Exception as e:
        print(f"Lỗi khi xử lý file {img_file}: {e}")