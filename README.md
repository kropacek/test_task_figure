# Обзор

Этот проект представляет собой веб-приложение на основе Django, предназначенное для управления и анализа разгрузки руды самосвалами в складскую зону, ограниченную полигоном. Проект включает создание ORM моделей, разработку представлений. Цель — вычисление и отображение изменений объема и качества руды в складской зоне на основе координат разгрузки, введенных пользователем.

## Структура проекта
### 1. ORM модели
Определены следующие модели для представления данных:

Truck: Представляет самосвал с полями для бортового номера, модели, максимальной грузоподъемности, текущего груза и координат разгрузки.

Warehouse: Представляет складскую зону с полями для объема и качественных характеристик руды.

### 2. Представления и шаблоны
Главная страница: Отображает таблицу с информацией о каждом самосвале и позволяет пользователю вводить координаты разгрузки.

Для запуска проекта следует сделать следующее:
1) Установить зависимости
```
pip install -r requirements.txt
```
2) Запустить приложение командой
```
python manage.py runserver
```
3) Перейти в браузер на http://127.0.0.1:8000/
4) Ввести данные и проверить работоспособность (например координаты 35 30)
