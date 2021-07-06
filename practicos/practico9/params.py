#params: posicionales, args, nominados, kwargs
def foo(p1, p2, *args, n1='uno', n2='dos', **kwargs):
    print(p1, p2, args, n1, n2, kwargs)

foo(1, 2, 3, 4, d1=11, d2='doce')
foo(1, 2, 3, d1=11, d2='doce')
foo(1, 2, d1=11, d2='doce')
foo(1, 2, n1='sobreUno', otro='Otro')

