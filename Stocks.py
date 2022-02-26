import requests  # для URL запроса
import time  # для установки задержки в цикле программы

from bs4 import BeautifulSoup  # для работы с HTML

import SQLighter

sleep = 3  # время задержки
name = "Gazprom"


# Получение и обновление цены
def update_price_stocks(link_stock, name_stock):
    # ссылка на тикер https://ru.investing.com/equities/sberbank_rts
    link = "https://ru.investing.com/" \
           "equities/" \
           + link_stock

    # заголовки для URL запроса.(добавляется к ссылке при URL запросе)
    # чтобы запрос не был воспринят гуглом как БОТ- запрос
    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36"}

    # запрашиваем страницу по ссылке и помещаем в переменную html
    html = requests.get(link, headers)
    # парсим данные в переменную soup
    soup = BeautifulSoup(html.content, 'html.parser')
    convert = soup.findAll('span', {'class': 'text-2xl'})

    # считываем 1й элемент как текст.
    # Делаем срез и избавляемся от знака ₽ в начале строки,
    # конвертируем строку в число типа float
    price = float((convert[0].text[0:]).replace(',', '.'))

    SQLighter.update_price_stocks(name_stock, price)

    print(f"Цена акции {name_stock}: ", price)

    # # устанавливаем задержку
    # time.sleep(sleep)
    # update_price_stocks(link_stock)  # вызываем эту же функцию снова


link = SQLighter.get_link_stocks(name)
update_price_stocks(link, name)
