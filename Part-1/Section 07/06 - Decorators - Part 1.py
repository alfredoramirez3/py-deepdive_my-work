import marimo

__generated_with = "0.10.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""### Decorators""")
    return


@app.cell
def _():
    def counter(fn):
        count = 0

        def inner(*args, **kwargs):
            nonlocal count
            count += 1
            print('Function {0} was called {1} times'.format(fn.__name__, count))
            return fn(*args, **kwargs)
        return inner
    return (counter,)


@app.cell
def _():
    def add(a, b=0):
        """
        returns the sum of a and b
        """
        return a + b
    return (add,)


@app.cell
def _(add):
    help(add)
    return


@app.cell
def _(add):
    id(add)
    return


@app.cell
def _(add, counter):
    counter_add = counter(add)
    return (counter_add,)


@app.cell
def _(counter_add):
    counter_add(1,2)
    return


@app.cell
def _(counter_add):
    counter_add(2,2)
    return


@app.cell
def _(counter):
    # shorthand decorating a function
    @counter
    def mult(a: float, b: float=1, c: float=1) -> float:
        """
        returns product of a, b, and c
        """
        return a * b *c
    return (mult,)


@app.cell
def _(mult):
    mult(1, 2, 3)
    return


@app.cell
def _(mult):
    mult(2, 2, 2)
    return


@app.cell
def _(mo):
    mo.md(r"""Introspection of the two decorated functions""")
    return


@app.cell
def _(counter_add):
    counter_add.__name__
    return


@app.cell
def _(mult):
    mult.__name__
    return


@app.cell
def _(counter_add):
    help(counter_add)
    return


@app.cell
def _(mult):
    help(mult)
    return


@app.cell
def _(mo):
    mo.md("""Lost docstring and parameter annotations.""")
    return


@app.cell
def _():
    import inspect
    return (inspect,)


@app.cell
def _(counter_add, inspect):
    inspect.getsource(counter_add)
    return


@app.cell
def _(inspect, mult):
    inspect.getsource(mult)
    return


@app.cell
def _(add, inspect):
    inspect.signature(add)
    return


@app.cell
def _(inspect, mult):
    inspect.signature(mult)
    return


@app.cell
def _(add, inspect):
    inspect.signature(add).parameters
    return


@app.cell
def _():
    import wat
    return (wat,)


@app.cell
def _(counter_add, wat):
    wat.code / counter_add
    return


@app.cell
def _(mo):
    mo.md("""Use special function in functools module, called wraps, to metadata""")
    return


@app.cell
def _():
    from functools import wraps
    return (wraps,)


@app.cell
def _(wraps):
    def rev_counter(fn):
        count = 0

        @wraps(fn)
        def inner(*args, **kwargs):
            nonlocal count
            count += 1
            print("{0} was called {1} times".format(fn.__name__, count))
            return fn(*args, **kwargs)
            
        return inner
    return (rev_counter,)


@app.cell
def _(rev_counter):
    @rev_counter
    def add_v2(a: int, b: int=10) -> int:
        """
        returns sum of two integers
        """
        return a + b
    return (add_v2,)


@app.cell
def _(add_v2):
    help(add_v2)
    return


@app.cell
def _(add_v2, inspect):
    inspect.getsource(add_v2)
    return


@app.cell
def _(add, inspect):
    inspect.signature(add).parameters
    return


@app.cell
def _(add_v2, wat):
    wat.code / add_v2
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
