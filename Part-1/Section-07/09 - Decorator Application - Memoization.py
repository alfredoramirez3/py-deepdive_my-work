import marimo

__generated_with = "0.10.15"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""### Decorator Application (Memoization)""")
    return


@app.cell
def _():
    # my imports
    import marimo as mo
    return (mo,)


@app.cell
def _():
    def fib(n):
        print('Calculating fib({0})'.format(n))
        return 1 if n < 3 else fib(n-1) + fib(n-2)
    return (fib,)


@app.cell
def _(fib):
    fib(10)
    return


@app.cell
def _(mo):
    mo.md(r"""Improve efficiency with a dimple class and a dictionary that stores any Fibonacci number already calculated""")
    return


@app.cell
def _():
    class Fib:
        def __init__(self):
            self.cache = {1: 1, 2: 1}

        def fib(self, n):
            if n not in self.cache:
                print('Calculating fib({0})'.format(n))
                self.cache[n] = self.fib(n-1) + self.fib(n-2)
            return self.cache[n]
    return (Fib,)


@app.cell
def _(Fib):
    f = Fib()
    return (f,)


@app.cell
def _(f):
    f.fib(1)
    return


@app.cell
def _(f):
    f.fib(6)
    return


@app.cell
def _(f):
    f.fib(7)
    return


@app.cell
def _(mo):
    mo.md(r"""Rewrite using a closure""")
    return


@app.cell
def _():
    def fn_fib():
        cache = {1: 1, 2: 1}

        def calc_fib(n):
            if n not in cache:
                print('Calculating fib({0})'.format(n))
                cache[n] = calc_fib(n-1) + calc_fib(n-2)
            return cache[n]
        return calc_fib
            
    return (fn_fib,)


@app.cell
def _(fn_fib):
    f_fn = fn_fib()
    return (f_fn,)


@app.cell
def _(f_fn):
    f_fn(10)
    return


@app.cell
def _(mo):
    mo.md(r"""Implement using a decorator""")
    return


@app.cell
def _():
    from functools import wraps

    def memoize_fib(fn):
        cache = dict()
        
        @wraps(fn)
        def inner(n):
            if n not in cache:
                cache[n] = fn(n)
            return cache[n]
        
        return inner
    return memoize_fib, wraps


@app.cell
def _(fib, memoize_fib):
    @memoize_fib
    def fib_deco(n):
        print ('Calculating fib({0})'.format(n))
        return 1 if n < 3 else fib(n-1) + fib(n-2)
    return (fib_deco,)


@app.cell
def _(fib_deco):
    fib_deco(3)
    return


@app.cell
def _(fib_deco):
    fib_deco(10)
    return


@app.cell
def _(fib_deco):
    fib_deco(11)
    return


@app.cell
def _(fib_deco):
    fib_deco(5)
    return


if __name__ == "__main__":
    app.run()
