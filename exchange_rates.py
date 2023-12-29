
from forex_python.converter import CurrencyRates

c = CurrencyRates()
currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'SEK', 'NZD', 'MXN', 'SGD', 'HKD', 'NOK', 'KRW', 'TRY', 'INR', 'BRL', 'ZAR', 'DKK', 'PLN', 'THB', 'MYR']

with open('currency_list.txt', 'w') as f:
    # Записываем список валют в файл
    f.write('\n'.join(currencies))

with open('graph_edges.txt', 'w') as f:
    # Записываем курсы валют в файл
    for base_currency in currencies:
        for target_currency in currencies:
            rate = c.get_rate(base_currency, target_currency)
            f.write(f'{currencies.index(base_currency)} {currencies.index(target_currency)} {rate}\n')

print('Файлы currency_list.txt и graph_edges.txt успешно заполнены.')