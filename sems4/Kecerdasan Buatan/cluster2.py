!pip install bing_image_downloader

!mkdir sample_data

from bing_image_downloader import downloader
downloader.download('Microphone condenser', limit=135, output_dir='dataset_Mic', adult_filter_off=True)

import shutil
from google.colab import files

# Lokasi folder yang ingin di-zip
folder_path = '/content/dataset_Mic/Microphone condenser'

# Nama file zip yang akan dihasilkan
output_filename = '/content/Microphone condenser.zip'

# Membuat file zip
shutil.make_archive(output_filename.replace('.zip', ''), 'zip', folder_path)

# Mengunduh file zip
files.download(output_filename)
