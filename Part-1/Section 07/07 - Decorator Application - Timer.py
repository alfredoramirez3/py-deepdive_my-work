import marimo

__generated_with = "0.10.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Decorators Application (Timing)

        Capture function execution time
        """
    )
    return


@app.cell
def _():
    def timed(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start

            args_ = [str(a) for a in args]
            kwargs_ =['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
            all_args = args_ + kwargs_
            args_str = ','.join(all_args)
            print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, 
                                                          args_str,
                                                          elapsed))
            return result

        return inner
            
    return (timed,)


@app.cell
def _(mo):
    mo.md(
        r"""
         Implement functions that calculates n-th Fibonacci number:
             1. recursion
             2. a loop
             3. functional programming (reduce)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""Using Recursion""")
    return


@app.cell
def _():
    def calc_recursive_fib(n):
        if n <= 2:
            return 1
        else:
            return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)
    return (calc_recursive_fib,)


@app.cell
def _(calc_recursive_fib):
    calc_recursive_fib(3)
    return


@app.cell
def _(calc_recursive_fib):
    calc_recursive_fib(6)
    return


@app.cell
def _(calc_recursive_fib, timed):
    @timed
    def fib_recursed(n):
        return calc_recursive_fib(n)
    return (fib_recursed,)


@app.cell
def _(fib_recursed):
    fib_recursed(33)
    return


@app.cell
def _(fib_recursed):
    fib_recursed(34)
    return


@app.cell
def _(fib_recursed):
    fib_recursed(35)
    return


@app.cell
def _(mo):
    mo.md(r"""Using a loop""")
    return


@app.cell
def _():
    def calc_fib_loop(n):
        fib_1 = 1
        fib_2 = 1
        for i in range(3, n+1):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return fib_2
    return (calc_fib_loop,)


@app.cell
def _(calc_fib_loop, timed):
    @timed
    def fib_loop(n):
        return calc_fib_loop(n)
    return (fib_loop,)


@app.cell
def _(fib_loop):
    fib_loop(3)
    return


@app.cell
def _(fib_loop):
    fib_loop(6)
    return


@app.cell
def _(fib_loop):
    fib_loop(33)
    return


@app.cell
def _(fib_loop):
    fib_loop(34)
    return


@app.cell
def _(fib_loop):
    fib_loop(35)
    return


@app.cell
def _(mo):
    mo.md(r"""This method is much more efficient!""")
    return


@app.cell
def _(mo):
    mo.md(r"""Using Reduce """)
    return


@app.cell
def _():
    from functools import reduce

    def calc_fib_reduce(n):
        initial = (1, 0)
        dummy = range(n-1)
        fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                       dummy, 
                       initial)
        return fib_n[0]
    return calc_fib_reduce, reduce


@app.cell
def _(calc_fib_reduce, timed):
    @timed
    def fib_reduced(n):
        return calc_fib_reduce(n)
    return (fib_reduced,)


@app.cell
def _(fib_reduced):
    fib_reduced(33)
    return


@app.cell
def _(fib_reduced):
    fib_reduced(34)
    return


@app.cell
def _(fib_reduced):
    fib_reduced(35)
    return


@app.cell
def _(fib_loop, fib_recursed, fib_reduced):
    fib_recursed(35)
    fib_loop(35)
    fib_reduced(35)
    return


@app.cell
def _(fib_loop, fib_recursed, fib_reduced):
    timings = []
    timings.append(fib_recursed(35))
    timings.append(fib_loop(35))
    timings.append(fib_reduced(35))
    print(timings)
    return (timings,)


@app.cell
def _(fib_loop, fib_recursed, fib_reduced):
    print(fib_recursed(35))
    print(fib_loop(35))
    print(fib_reduced(35))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
