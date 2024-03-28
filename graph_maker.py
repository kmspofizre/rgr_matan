from math_funtions import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


I = 7 / 3


def make_mean_squared_error_graph(a, b, start_n, end_n, mode, function, rectangle_mode=1):
    integrals = []
    ns = []
    if mode == "1":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(rectangle_method(a, b, i, partition, rectangle_mode, function, print_mode=False))
            ns.append(i)
    elif mode == "2":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(trapezoidal_method(a, b, i, partition, function, print_mode=False))
            ns.append(i)
    elif mode == "3":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(simpson_method(a, b, i, partition, function, print_mode=False))
            ns.append(i)
    integrals_np = np.array(integrals)
    integral_np = np.array([I] * len(integrals_np))
    sub = integral_np - integrals_np
    mse = np.vectorize(lambda x: x ** 2)
    sub = mse(sub)
    plt.plot(ns, sub, color="red", label="MSE")
    plt.legend()
    plt.show()
    return np.mean((integral_np - integrals_np) ** 2)


def make_mean_absolute_error_graph(a, b, start_n, end_n, mode, function, rectangle_mode=1):
    integrals = []
    ns = []
    if mode == "1":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(rectangle_method(a, b, i, partition, rectangle_mode, function, print_mode=False))
            ns.append(i)
    elif mode == "2":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(trapezoidal_method(a, b, i, partition, function, print_mode=False))
            ns.append(i)
    elif mode == "3":
        for i in range(start_n, end_n + 1):
            partition = get_partition(a, b, i)
            integrals.append(simpson_method(a, b, i, partition, function, print_mode=False))
            ns.append(i)
    integrals_np = np.array(integrals)
    integral_np = np.array([I] * len(integrals_np))
    sub = integral_np - integrals_np
    mae = np.vectorize(lambda x: abs(x))
    sub = mae(sub)
    plt.plot(ns, sub, color="red", label="MAE")
    plt.legend()
    plt.show()
    return np.mean(abs(integral_np - integrals_np))

