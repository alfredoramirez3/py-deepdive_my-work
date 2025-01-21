import marimo

__generated_with = "0.10.15"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""### Decorators Application (Logger, Stacked Decorators)""")
    return


@app.cell
def _():
    # my imports
    import marimo as mo
    import wat
    return mo, wat


@app.cell
def _():
    def logged(fn):
        """
        Utility decorator that logs function calls to the console
        """
        from functools import wraps
        from datetime import datetime, timezone

        @wraps(fn)
        def inner(*args, **kwargs):
            run_dt = datetime.now(timezone.utc)
            result = fn(*args, **kwargs)
            print('logged: {0} called {1}'.format(fn.__name__, run_dt))
            return result

        return inner
        
    return (logged,)


@app.cell
def _(logged):
    @logged
    def func_1():
        pass
    return (func_1,)


@app.cell
def _(logged):
    @logged
    def func_2():
        pass
    return (func_2,)


@app.cell
def _(func_1):
    func_1()
    return


@app.cell
def _(func_2):
    func_2()
    return


@app.cell
def _():
    def timed(fn):
        from functools import wraps
        from time import perf_counter
        
        @wraps(fn)
        def inner(*args, **kwargs):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            print('timed: {0} ran for {1:.6f}s'.format(fn.__name__, end-start))
            return result
        
        return inner
            
    return (timed,)


@app.cell
def _(logged, timed):
    @timed
    @logged
    def factorial(n):
        """
        Returns the factorial of n
        Essentially, factorial = timed(logged(factorial))
            timed gets executed first, then logged
        """
        from operator import mul
        from functools import reduce
        
        return reduce(mul, range(1, n+1))
    return (factorial,)


@app.cell
def _(factorial):
    factorial(10)
    return


@app.cell
def _(factorial, wat):
    # wat.code output provides richer output versus inspect.getsource
    wat.code / factorial
    return


@app.cell
def _(factorial, wat):
    wat.code(factorial)
    return


@app.cell
def _():
    import inspect
    return (inspect,)


@app.cell
def _(factorial, inspect):
    inspect.getsource(factorial)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
