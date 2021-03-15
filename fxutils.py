import pandas as pd

def load_duka_data(file_path,  index_name):
  data = pd.read_csv(file_path)

  # reset column names
  data.columns = [index_name, 'Open', 'High', 'Low', 'Close', 'Volume']

  # parse dates
  data[index_name] = pd.to_datetime(data[index_name], format='%d.%m.%Y %H:%M:%S.%f')

  # set index
  data.index = pd.DatetimeIndex(data[index_name])

  # drop Date Column
  data = data.iloc[:, 1:6]

  return data
