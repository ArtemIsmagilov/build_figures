# Build figures

## Задание1:

> Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и
> треугольника по трем сторонам. Дополнительно к работоспособности оценим:
>
> - Юнит-тесты
> - Легкость добавления других фигур
> - Вычисление площади фигуры без знания типа фигуры в compile-time
> - Проверку на то, является ли треугольник прямоугольным

## Решение

```bash
git clone https://github.com/ArtemIsmagilov/build_figures.git
cd build_figures/
python3 main.py -v
```

## Задание2:

> В базе данных MS SQL Server есть продукты и категории. Одному продукту может соответствовать много категорий,
> в одной категории может быть много продуктов. Напишите SQL запрос для выбора всех пар «Имя продукта – Имя категории».
> Если у продукта нет категорий, то его имя все равно должно выводиться.

## Решение

```bash
python3 db_queries.py
```

# Источники информации

- Категории продуктов https://www.trustradius.com/categories
- Тесты doctest https://docs.python.org/3/library/doctest.html
- SQL JOIN(s) https://www.w3schools.com/sql/sql_join_left.asp
- Геометрические фигуры https://skysmart.ru/articles/mathematic/osnovnye-geometricheskie-figury
