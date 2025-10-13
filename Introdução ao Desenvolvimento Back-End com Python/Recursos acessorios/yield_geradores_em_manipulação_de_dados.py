def counter_function():
    yield 1
    yield 2
    yield 3

contador =counter_function()

print(next(contador))

print(next(contador))

print(next(contador))