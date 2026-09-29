def load_data1():
    return [3, 17, 8, 25, 6, 12, 25, 9, 14]
def filter_above(values, threshold=10):
    m=[]
    for i in values:
        if i > threshold:
            m.append(i)
    return m
def mean(values):
    return sum(values) / len(values)
if __name__ == '__main__':
    print('Самопроверка:', mean([1, 2, 3]))
