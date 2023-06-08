# Библиотека Python для парсинга Avito.ru

### Установка:
> - git clone https://github.com/Sudox00/user_avito & cd user_avito & python3 setup.py install
### Импорт:
> import user_avito
### Функции:
search - текст для поиска

city - город (по умолчанию все города России)(пример: 'moskva')

delivery - доставка (по умолчанию без доставки)(режимы: 1 - с доставкой, 2 - без доставки)

link - ссылка на объявление


#### Функция поиска объявлений (ответ в виде ссылок):
> user_avito.search_announcements(search, city, delivery)
#### Получить цену товара (ответ в виде числа):
> user_avito.get_price(link)
#### Статус сайта:
> user_avito.site_status()


### [Открыть пример](https://github.com/Sudox00/user_avito/blob/main/examples/func.py) • [Телеграм разработчика](https://github.com/Sudox00/user_avito/blob/main/examples/func.py)
