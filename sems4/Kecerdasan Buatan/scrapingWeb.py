import shutil
from google.colab import files

!pip install bing_image_downloader

!mkdir dataset_GelasPutih

from bing_image_downloader import downloader
downloader.download('gelas putih', limit= 135 , output_dir='dataset_GelasPutih', adult_filter_off=True)

# Lokasi folder yang ingin di-zip
folder_path = '/content/dataset_GelasPutih/gelas putih'

# Nama file zip yang akan dihasilkan
output_filename = '/content/gelas putih.zip'
