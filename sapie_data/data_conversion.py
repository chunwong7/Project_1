import pandas as pd
years = range(3, 19)
for year in years:
    year = str(year)
    if len(year) == 1:
        year = f'0{year}'
    read_file = pd.read_excel (f'est{year}all.xls')
    read_file.to_csv (f'../sapie_data_csv/est{year}all.csv', index = None, header=True)