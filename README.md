# Репозиторий для обновления базы авиаперевозок и отладки SQL запросов

[Ссылка на архив с исходными CSV](https://storage.yandexcloud.net/airtrans-small/airtrans.zip)  
База подогнана под MySql и построена в соответствии со [схемой](https://docs.google.com/document/d/1yMQPb-vb5inoBrzqTvxySjssvGjCzX28kbCAWvnSSFk/edit#heading=h.pdif82p685tc).
## Инфо для команды, разрабатывающей контест SQL-advanced

### Как поменять настройки генерации таблиц
Отредактировать `sql/CREATE_TABLES.sql` 
```bash
python3 prepare_init_script.py
```
После этого в `sql/INIT_DB.sql` будет записан итоговый код, создающий и заполняющий базу данных

### Как добавить/изменить данные, которыми заполняются таблицы
Отредактировать нужный csv файл в папке `airtrans_new`
```bash
python3 prepare_init_script.py
```
После этого в `sql/INIT_DB.sql` будет записан итоговый код, создающий и заполняющий базу данных

### Как протестировать инициализацию и заполнение БД и отладить SQL скрипты

1. [Поднять](https://docs.oracle.com/en/java/java-components/advanced-management-console/2.20/install-guide/mysql-database-installation-and-configuration-advanced-management-console.html#GUID-12323233-07E3-45C2-B77A-F35B3BBA6592) сервер с MySql
2. Отредактировать и запустить `test_database.py`. База создается при помощи `sql/INIT_DB.sql`

## Изменения по сравнению со старой версией базы
1. Во всех таблицах, которые содержали тип данных `JSONB` (aircrafts, airports, tickets), этот тип заменен на `VARCHAR` и вместо `JSON` вставлен его элемент. Например, в таблице aircrafts вхождение
`"{""en"": ""Airbus A321-200"", ""ru"": ""Аэробус A321-200""}"` 
заменено на
`"Airbus A321-200"`
2. В таблице tickets контактные данные пассажира заменены на номер телефона пассажира
Это упрощение связано с тем, что в программе курса не затрагивается `JSON`. Не считаю нужным добавлять работу с `JSON` в контест
3. Сокращены размеры таблиц. Теперь суммарно во всех таблицах менее 3К записей, против 1М+ записей в старой версии
4. В таблицах, содержащих тип данных `TIMISTAMPTZ` (bookings, flights), поля этого типа заменены на `TIMESTAMP` и в данных обрезан часовой пояс. Это необходимо для совместимости с MySql
5. В таблице flights тип данных колонки flight_id изменен с `SERIAL` на `INTEGER`, так как необходимо использовать эту колонку в качестве внешнего ключа, а flight_id в таблице ticket_flights имеет тип `INTEGER`
6. В таблице airports изменен формат координат для совместимости с MySql
7. В таблице flights вместо пропусков вставлены `NULL`
