from math_funtions import *
from graph_maker import make_mean_squared_error_graph, make_mean_absolute_error_graph

a = 1
b = 2
n = 10000
left_mode = 1  # способ выбора кси при вычислении методом прямоугольников 1 - левая граница,
# 2 - правая граница, 3 - случайный выбор из промежутка
right_mode = 2
random_mode = 3
mode = "1"  # вид рассчетов для передачи в функцию с графиком 1 - метод прямоугольников,
# 2 - метод трапеций, 3 - метод Симпсона


if __name__ == '__main__':
    partition = get_partition(a, b, n)
    print(
        f"Результат, полученный прямоугольников (берется левая граница в каждом промежутке): "
        f" {rectangle_method(a, b, n, partition, left_mode, 'x ** 2')}")
    print()
    print(
        f"Результат, полученный методом прямоугольников (берется правая граница в каждом промежутке): "
        f" {rectangle_method(a, b, n, partition, right_mode, 'x ** 2')}")
    print()
    print(
        f"Результат, полученный прямоугольников (берется случаное значение из каждого промежутка): "
        f" {rectangle_method(a, b, n, partition, random_mode, 'x ** 2')}")
    print()
    print(f"Результат, полученный методом трапеций: {trapezoidal_method(a, b, n, partition, 'x ** 2')}")
    print()
    print(f"Результат, полученный методом Симпсона: {simpson_method(a, b, n, partition, 'x ** 2')}")
    print()
    print(f"MSE: {make_mean_squared_error_graph(a, b, 10, 1000, '2', 'x ** 2')}")
    print(f"MAE: {make_mean_absolute_error_graph(a, b, 10, 1000, '2', 'x ** 2')}")
