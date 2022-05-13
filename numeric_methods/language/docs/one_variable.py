HALF_METHOD_DOCS = {
    "ENGLISH": """
    This method is implementing the half division's method of root searching.

    Algorithm:
        repeat while x_(i - 1)  -  x_(i) >= epsilon
            x = (a + b) / 2
            y = function(x)
            return step, a, b, x, y
            # -- [a] -- x -- [b] -->
            if function(a) * function(x) < 0 then
                # -- [a] -- [x] -- b -->
                a = a and b = x
            else if function(x) * function(b) < 0 then
                a = x and b = b
                # -- a -- [x] -- [b] -->
            else if function(x) == 0 then
                return x
                STOP
            else
                ERROR

    Conditions of using:
        [Automatic] Must be truth or ArithmeticError will raise: function(a_0) * function(b_0) < 0
        [Manually] Must be truth or some kind of exception will raise: function is continuous in [a_0, b_0]
    
    Example:
        | from numeric_methods.one_variable import half_method
        |
        |
        | # x ** 5 = 2
        | for line in half_method(lambda x: x ** 5 - 2, 1, 2, 0.001):
        |     print(line)

    :param function: Lambda or defined function which must support type of number and be continuity
    :param a: Begin of the slice where root is
    :param b: End of the slice where root is
    :param epsilon: Required precision of the `function(x) = 0` root
    :return: Root of the `function(x) = 0` with indicated precision
    """,
    "RUSSIAN": """
    Данный метод реализует нахождение корня методом половинного деления. 
    
    Алгоритм:
        repeat while x_(i - 1)  -  x_(i) >= epsilon
            x = (a + b) / 2
            y = function(x)
            return step, a, b, x, y
            # -- [a] -- x -- [b] -->
            if function(a) * function(x) < 0 then
                # -- [a] -- [x] -- b -->
                a = a and b = x
            else if function(x) * function(b) < 0 then
                a = x and b = b
                # -- a -- [x] -- [b] -->
            else if function(x) == 0 then
                return x
                STOP
            else
                ERROR

    Условия использования:
        [Автоматически] Должно быть истинной или будет вызвана ArithmeticError: function(a_0) * function(b_0) < 0
        [Вручную] Должно быть истинно или будет вызвано исключение какого-то вида: функция непрерывна на [a_0, b_0]

    Пример:
        | from numeric_methods.one_variable import half_method
        |
        |
        | # x ** 5 = 2
        | for line in half_method(lambda x: x ** 5 - 2, 1, 2, 0.001):
        |     print(line)

    :param function: Лямбда-функция или заранее определенная функция, которая должна поддерживать данный тип числа и быть непрерывной
    :param a: Начало отрезка, в котором находится корень
    :param b: Конец отрезка, в котором находится корень
    :param epsilon: Требуемая точность корня уравнения `function(x) = 0`
    :return: Корень уравнения `function(x) = 0` с указанной точностью
    """
}

ITER_METHOD_DOCS = {
    "ENGLISH": """
    This method is implementing the simple iterations' method of root searching.

    Algorithm:
        x_(i + 1) = function(x_(i))
        return step, x_(i + 1)
        repeat while |x_(i + 1) - x_(i)| >= (1 - c_criterion) / c_criterion * epsilon
            x_(i) = x_(i + 1)
            x_(i + 1) = function(x_(i))
            return step, x_(i + 1)
        return x_(i + 1)
        STOP

    Conditions of using:
        [Manually] Must be truth or ArithmeticError will raise or algorithm will execute forever: |function'(x_(i))| < 1

    Example:
        | from math import sin
        |
        | from numeric_methods.one_variable import iter_method
        |
        |
        | # sin(x) / x = x
        | for line in iter_method(lambda x: sin(x) / x, 1, 0.001):
        |     print(line)

    :param function: Lambda or defined function which must support type of number, be continuity and represents left part of equation `function(x) = x`
    :param x: Start value of x (x_0)
    :param epsilon: Required precision of the `function(x) = x` root
    :param c_criterion: Convergence criterion
    :return: Root of the `function(x) = 0` with indicated precision
    """,
    "RUSSIAN": """
    Данный метод реализует нахождение корня методом простых итераций.

    Алгоритм:
        x_(i + 1) = function(x_(i))
        return step, x_(i + 1)
        repeat while |x_(i + 1) - x_(i)| >= (1 - c_criterion) / c_criterion * epsilon
            x_(i) = x_(i + 1)
            x_(i + 1) = function(x_(i))
            return step, x_(i + 1)
        return x_(i + 1)
        STOP

    Условия использования:
        [Вручную] Должно быть истинной или будет вызвана ArithmeticError will или алгоритм будет исполнятся вечно: |function'(x_(i))| < 1

    Пример:
        | from math import sin
        |
        | from numeric_methods.one_variable import iter_method
        |
        |
        | # sin(x) / x = x
        | for line in iter_method(lambda x: sin(x) / x, 1, 0.001):
        |     print(line)

    :param function: Лямбда-функция или заранее определенная функция, которая должна поддерживать данный тип числа, быть непрерывной и представлять левую часть уравнения `function(x) = x`
    :param x: Начальное значение x (x_0)
    :param epsilon: Требуемая точность корня уравнения `function(x) = x`
    :param c_criterion: Критерий сходимости
    :return: Корень уравнения `function(x) = x` с указанной точностью
    """,
}
