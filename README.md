# (НЕАКТУАЛЬНО)
# Библиотека Python для парсинга Avito.ru

### Установка:
> pip install pars-avito
### Импорт:
> import pars_avito
### Функции:
search - текст для поиска

city - город (по умолчанию все города России)(пример: 'moskva')

delivery - доставка (по умолчанию без доставки)(режимы: 1 - с доставкой, 2 - без доставки)

link - ссылка на объявление


#### Функция поиска объявлений (ответ в виде ссылок):
> pars_avito.search_announcements(search, city, delivery)
#### Получить цену товара (ответ в виде числа):
> pars_avito.get_price(link)
#### Статус сайта:
> pars_avito.site_status()


### [Открыть пример](https://github.com/Sudox00/user_avito/blob/main/examples/func.py) • [Телеграм разработчика](https://t.me/soketpy2)
