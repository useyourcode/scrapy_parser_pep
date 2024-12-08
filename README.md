# Scrapy Parser PEP

## Парсинг документов PEP
Асинхронный парсер собирающий данные о Python Enhancement Proposals (PEP) с сайта `https://www.python.org/`.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет
несколько файлов в формате `.csv` в папке `results/...`:
* Список PEP (номер, название и статус);
* Подсчитывает общее количество каждого статуса и сумму всех статусов.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:useyourcode/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

## Запуск парсера
```
scrapy crawl pep
```