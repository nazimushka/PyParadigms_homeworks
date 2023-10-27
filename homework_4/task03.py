import math

def pearson_correlation(X, Y):
    if len(X) != len(Y):
        raise ValueError("Массивы X и Y должны иметь одинаковую длину")

    n = len(X)
    mean_X = sum(X) / n
    mean_Y = sum(Y) / n

    numerator = sum(map(lambda x, y: (x - mean_X) * (y - mean_Y), X, Y))
    denominator = math.sqrt(sum(map(lambda x: (x - mean_X)**2, X))) * math.sqrt(sum(map(lambda y: (y - mean_Y)**2, Y)))

    if denominator == 0:
        raise ValueError("Знаменатель равен нулю, деление на ноль невозможно")

    return numerator / denominator


X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]
correlation = round(pearson_correlation(X, Y), 2)
print(correlation) # 1.0


# Массивы разной длины
'''
X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8]  
correlation = pearson_correlation(X, Y) #ValueError: Массивы X и Y должны иметь одинаковую длину
print(correlation)
'''