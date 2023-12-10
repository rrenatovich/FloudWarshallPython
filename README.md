# FloudWarshallPython
 
# URL на GitHub 
https://github.com/rrenatovich/FloudWarshallPython.git

Алгоритм нахождения кратчайшего пути между всеми парами вершин

# Основная идея 
Разбиение задачи поиска минимальных путей на фазы/шаги 

перед $k$ фазой считаем что в матрице расстояний сохранины длины кротчайших путей ( где внутренние вершины от 1 до $k-1$) 
Т.е. перед шагом $k$ величина $D[i][j]$ это кртачайший путь из вершины $i$ в вершину $j$ при условии что можно захожить в вершины с номерами до $k-1$

Пусть мы находимся на $k$ фазе и хотим пересчитать матрицу $D$ для $k+1$. Могут возникнуть сл случаи: 

1. Кратчайший путь из вершины i в вершину j, которому разрешено дополнительно проходить через вершины $\{ 1, 2, \ldots, k \}$, совпадает с кратчайшим путём, которому разрешено проходить через вершины множества $\{ 1, 2, \ldots, k-1 \}$
    
    Тогда матрица D не изменится 

2. Новый путь оказался лушче 

    Разобъем путь вершиной $k$:
    
    1.Одна $i \to k$

    2.Вторая $k \to j$

    Длина каждой из этих половинок была посчитана на шаге $k-1$ и мы можем взять сумму $d[i][k] + d[k][j]$ это и будет длина нового кратчайшего пути

Получается что на $k$ фазе можем найти кратчайший путь между всеми парами вершин: 

```
new_D[i][j] = min (D[i][j], D[i][k] + d[k][j])
```
![Рисунок с Википедии пример работы](figure/eexampleOfWork.png)

рисунок с https://neerc.ifmo.ru/wiki/index.php?title=Алгоритм_Флойда

