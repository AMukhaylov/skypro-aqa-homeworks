X = int(input("Размер вклада (валюта руб.): "))
Y = int(input("Срок рамещеня (в годах): "))

def bank(X, Y):
    for z in range(0, Y):
        X =  X * 1.1
    return round(X)

print("Будет", bank(X, Y), "руб.")