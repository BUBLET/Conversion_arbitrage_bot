import urllib3
import sys

def get_exchange(curr_from, curr_to, api_key):
    # Формирование URL для получения курса обмена
    url = 'https://www.exchangerate-api.com/{a}/{b}?k={key}'.format(a=curr_from, b=curr_to, key=api_key)

    try:
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        rate = response.data.decode('utf-8').strip()
        return rate

    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_rate():
    # Получение списка доступных валют из файла
    currencies = []
    with open("currency_codes.txt", 'r') as curr:
        for line in curr:
            codes = line.split('\t')
            currencies.append(codes[2].strip('\n'))

    return currencies

# Получение списка доступных валют и вывод на экран
currencies = get_rate()
print(currencies)