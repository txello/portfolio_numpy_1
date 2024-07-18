from data_loader import load_stock_data
from analyzer import calculate_mean, calculate_median, calculate_std
from tickers import install_ticker

def main():
    df = install_ticker()
    data, columns = load_stock_data(df) # Получаем данные из файла
    
    open, close = columns.get_loc('Open'), columns.get_loc('Close')
    
    mean_1 = calculate_mean(data, open) # Получаем среднее значение цен
    mean_2 = calculate_mean(data, close) # Получаем среднее значение цен
    
    median_1 = calculate_median(data, open) # Получаем медиану цен
    median_2 = calculate_median(data, close)
    
    std_1 = calculate_std(data, open) # Получаем стандартное отклонение цен
    std_2 = calculate_std(data, close)
    
    print("Средняя цена(Открытие):", mean_1)
    print("Медиана цен(Открытие):", median_1)
    print("Стандартное отклонение цен(Открытие):", std_1)
    print()
    print("Средняя цена(Закрытие):", mean_2)
    print("Медиана цен(Закрытие):", median_2)
    print("Стандартное отклонение цен(Закрытие):", std_2)

if __name__ == "__main__":
    main()
