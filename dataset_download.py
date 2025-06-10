import kaggle
import os

kaggle.api.authenticate()

data_folder = 'data'
os.makedirs(data_folder, exist_ok=True)

kaggle.api.dataset_download_files('camnugent/california-housing-prices', path=data_folder, unzip=True)
