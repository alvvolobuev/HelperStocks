import requests  # для URL запроса
import time  # для установки задержки в цикле программы

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup  # для работы с HTML

import SQLighter

# sleep = 3  # время задержки

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

# link = SQLighter.get_link_stocks(name)
# update_price_stocks(link, name)


def update_technical_analysis(name_stock):
    # Отключает изображения в гуглхроме
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    # Выключает отображение бразуера
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    link = "https://ru.investing.com/technical/%D0%A2%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BE%D0%B1%D0%B7%D0%BE%D1%80-%D0%B0%D0%BA%D1%86%D0%B8%D0%B9-%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"

    # Страницы какие мы парсим. А вдруг их будет много, поэтому запихиваем в переменную.
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    tr = SQLighter.parsing(name_stock)

    min_5 = browser.find_element(By.XPATH, f"/html/body/div[5]/section/div[7]/table/tbody/tr[{tr}]/td[2]").text
    min_15 =browser.find_element(By.XPATH, f"/html/body/div[5]/section/div[7]/table/tbody/tr[{tr}]/td[3]").text
    min_60 = browser.find_element(By.XPATH, f"/html/body/div[5]/section/div[7]/table/tbody/tr[{tr}]/td[4]").text
    day = browser.find_element(By.XPATH, f"/html/body/div[5]/section/div[7]/table/tbody/tr[{tr}]/td[5]").text

    browser.quit()

    return min_5, min_15, min_60, day

def start_prog(name):
    technical_analysis = update_technical_analysis(name)
    link = SQLighter.get_link_stocks(name)
    update_price_stocks(link, name)
    SQLighter.update_technical_analysis(name, technical_analysis)
