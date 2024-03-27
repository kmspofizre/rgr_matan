import random
import time


def get_partition(a, b, n):
    interval_length = abs(a - b)
    partition = (interval_length / n)
    return partition


def rectangle_method(a, b, n, partition, mode, function):
    left_edge = min(a, b)
    current_left = left_edge
    current_right = current_left + partition
    integral_sum = 0
    start_time = time.time()
    for i in range(n):
        if mode == 1:
            integral_sum += (eval(function, {"x": current_left})) * (current_right - current_left)
        elif mode == 2:
            integral_sum += (eval(function, {"x": current_right})) * (current_right - current_left)
        elif mode == 3:
            integral_sum += (eval(function,
                                 {"x": random.uniform(current_left, current_right)})) * (current_right - current_left)
        current_left = current_right
        current_right = current_left + partition
    print(f"Время выполнения методом прямоугольников: {time.time() - start_time}")
    return integral_sum


def trapezoidal_method(a, b, n, partition, function):
    left_edge = min(a, b)
    current_left = left_edge
    current_right = current_left + partition
    integral_sum = 0
    start_time = time.time()
    for i in range(n):
        fl = eval(function, {"x": current_left})
        fr = eval(function, {"x": current_right})
        integral_sum += (fl + fr) * ((current_right - current_left) / 2)
        current_left = current_right
        current_right = current_left + partition
    print(f"Время выполнения методом трапеций: {time.time() - start_time}")
    return integral_sum


def simpson_method(a, b, n, partition, function):
    left_edge = min(a, b)
    current_left = left_edge
    current_right = current_left + partition
    integral_sum = 0
    start_time = time.time()
    for i in range(n):
        fl = eval(function, {"x": current_left})
        fr = eval(function, {"x": current_right})
        fm = eval(function, {"x": ((current_left + current_right) / 2)})
        integral_sum += (fl + 4 * fm + fr) * ((current_right - current_left) / 6)
        current_left = current_right
        current_right = current_left + partition
    print(f"Время выполнения методом Симпсона: {time.time() - start_time}")
    return integral_sum
