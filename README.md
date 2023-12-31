[![GitHub contributors](https://img.shields.io/github/contributors/BUBLET/Conversion_arbitrage_bot.svg)](https://github.com/BUBLET/Conversion_arbitrage_bot/graphs/contributors)
![Last commit](https://img.shields.io/github/last-commit/BUBLET/Conversion_arbitrage_bot.svg)
![Python version](https://img.shields.io/badge/Python-3.6-blue.svg)

# Conversion Arbitrage Bot

Conversion Arbitrage Bot - Бот использует алгоритм Беллмана-Форда для поиска отрицательных циклов в графе обменных курсов и выявления прибыльных конверсий валют.

## Принцип работы

1. **Модуль обменных курсов**: Программа импортирует модуль `exchange_rates`, который предоставляет актуальные обменные курсы валют. Этот модуль используется для получения списка валют и соответствующих обменных курсов.

2. **Построение графа**: Программа считывает информацию из файла `graph_edges.txt` и создает граф, представляющий обменные курсы между различными валютами. Каждая валюта представлена вершиной в графе, а обменный курс между двумя валютами - ребром с весом, вычисляемым как отрицательный логарифм обменного курса.

3. **Алгоритм Беллмана-Форда**: Программа использует алгоритм Беллмана-Форда для поиска кратчайших путей в графе. Она выполняет итерации по всем ребрам графа и обновляет расстояния до каждой вершины, чтобы найти наименьшие расстояния от исходной вершины до всех остальных вершин.

4. **Поиск отрицательных циклов**: После завершения алгоритма Беллмана-Форда, программа проверяет каждое ребро графа еще раз. Если обнаруживается ребро, для которого можно улучшить расстояние до вершины, это означает наличие отрицательного цикла. Такие циклы указывают на арбитражные возможности в обменных курсах.

5. **Вывод результатов**: При обнаружении отрицательного цикла, программа выводит информацию о профитной конверсии валют. Она показывает путь в цикле, обозначая конверсию между валютами и соответствующий обменный курс. Также выводится общий вес цикла, который указывает на прибыльность конверсии.

## Использование

1. Установите все зависимости, указанные в файле `requirements.txt`.

2. Убедитесь, что у вас есть файл `graph_edges.txt` с правильной структурой и информацией об обменных курсах валют.

3. Запустите программу, выполнив файл `conversion_arbitrage_bot.py`.

4. Результаты выполнения программы будут выведены в консоль. Они будут содержать информацию о профитных конверсиях валют и общем весе отрицательного цикла.

## Примечания

- Если файл `graph_edges.txt` не найден или имеет неправильный формат данных, программа выведет соответствующую ошибку.

- Если модуль `exchange_rates` не может получить актуальные обменные курсы валют, программа также выведет ошибку.

- Убедитесь, что ваши валюты и обменные курсы корректно представлены в коде программы, чтобы Conversion Arbitrage Bot работал правильно.
