import user_avito  #импорт библиотеки

a = user_avito.site_status() #статус доступности сайта avito.ru
print(a)


b = user_avito.search_announcements('Nissan', 'sankt-peterburg', 1) #поиск объявлений
print(b)


c = user_avito.get_price('https://www.avito.ru/sankt-peterburg/mototsikly_i_mototehnika/ducati_monster_3016486375') #получить стоимость товара
print(c)

