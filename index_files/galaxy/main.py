from PIL import Image
import pyheif

def convert_heic_to_jpeg(heic_path, output_path):
    # 读取HEIC文件
    heif_file = pyheif.read(heic_path)
    
    # 创建一个Pillow图像
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # 将图像保存为JPEG格式
    image.save(output_path, "JPEG")

# 使用示例
convert_heic_to_jpeg("202403____IMG_0845.heic", "姫路城.jpg")

