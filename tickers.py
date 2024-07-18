import yfinance as yf
import pandas as pd
import config as cfg
import pathlib

def install_ticker():
    file_path = f'{cfg.QUOTE}.csv'
    
    if pathlib.Path(file_path).is_file():
        return pd.read_csv(file_path)
    
    df:pd.DataFrame = yf.download(
        cfg.QUOTE,
        start=cfg.DATES["start"] if hasattr(cfg, 'DATES') else None,
        end=cfg.DATES["end"] if hasattr(cfg, 'DATES') else None
    )
    
    df.to_csv(file_path)
    
    return pd.read_csv(file_path)