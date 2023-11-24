text = tuple(input())

symbols = sorted(set(text))

for symbol in symbols:
    print(f"{symbol}: {text.count(symbol)} time/s")

