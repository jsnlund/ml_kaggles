import pandas as pd

melborne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'

melborn_data = pd.read_csv(melborne_file_path)
print(melborn_data.describe())