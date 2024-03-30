# python 3.12
from functools import wraps
from typing import Callable, TypeVar, ParamSpec, Any
F_Spec = ParamSpec('F_Spec')
F_Return = TypeVar('F_Return')


def decorate_1(arg1):
    ''' Декоратор принимаючий арнусент '''
    def over_sum(func):
        @wraps(func) # Нужен для правильной работы сторонних библтльек не обязателен
        def wrapper(*args, **kwargs):

            # код перед выполняемой фонкции
            print(f'{'-'*50} decorator {'-'*50}')
            print(f'args: {args} kwargs: {kwargs} arg1: {arg1}')

            # Вызов переданной функции
            result = func(*args, **kwargs)

            # код после выполняемой функции
            if arg1:
                result = result ** arg1
            print(f'{'-' * 111}')

            return result
        return wrapper
    return over_sum


def custon_decorate(
        func: Callable[F_Spec, F_Return] | None = None,
        *,
        arg1: Any | None = None
) -> Callable[[Callable[F_Spec, F_Return]], Callable[F_Spec, F_Return]] | Callable[F_Spec, F_Return]:
    ''' Позволяет использовать декоратор Шредингера с/без аргументов '''
    tmp_decorate = decorate_1(arg1)
    if func is None:
        return tmp_decorate
    else:
        return tmp_decorate(func)


class Decorate_2:

    def __init__(self, func):
        ''' Выполняется при декорировании '''
        if not isinstance(func, Decorate_2):
            self.original_call = func
        else:
            self.original_call = func.original_call

    def __call__(self, *args, **kwargs):
        ''' Выполняется при вызове '''
        # код перед выполняемой фонкции
        print(f'{'-' * 50} decorator {'-' * 50}')
        print(f'args: {args} kwargs: {kwargs}')

        # Вызов переданной функции
        result = self.original_call(*args, **kwargs)

        # код после выполняемой функции
        result += result
        print(f'{'-' * 111}')

        return result


''' Примеры использования '''


def sumy1(x, y):
    print(''' обычная функция ''')
    return x+y


@decorate_1(arg1=2)
def sumy2(x, y):
    print(''' декарируемая функция с аргументом ''')
    return x+y


@custon_decorate
def sumy3(x, y):
    print(''' декарируемая Шредингера функция без аргументом ''')
    return x+y


@custon_decorate(arg1=2)
def sumy4(x, y):
    print(''' декарируемая Шредингера функция с аргументом ''')
    return x+y


@Decorate_2
def sumy5(x, y):
    print(''' декарируемая функция при помощи класса ''')
    return x+y


if __name__ == '__main__':
    print(f'result: {sumy1(1, 2)}')
    print(f'result: {sumy2(2, 3)}')
    print(f'result: {sumy3(4, 5)}')
    print(f'result: {sumy4(6, 7)}')
    print(f'result: {sumy5(6, 7)}')
