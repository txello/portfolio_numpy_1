import pandas as pd
def load_stock_data(df:pd.DataFrame):
    data = df.to_numpy(copy=True)
    return data[:, 1:6], df.columns  # Предполагается, что первая колонка - даты, остальные - цены акций разных компаний