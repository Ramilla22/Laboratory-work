SALES = [
    (101, 'хлеб', 2, 45.0),
    (101, 'молоко', 1, 89.0),
    (102, 'молоко', 3, 89.0),
    (103, 'сыр', 1, 620.0),
    (104, 'хлеб', 1, 45.0),
    (105, 'сыр', 2, 620.0),
    (106, 'молоко', 2, 89.0),
    (107, 'йогурт', 4, 55.0),
]
def load_sales():
    "возвращает данные"
    return SALES
def revenue_per_item(sales):
    "словарь «товар → суммарная выручка»"
    goods={}
    for number, product, quantity, price  in sales:
        goods[product]=goods.get(product,0)+ quantity*price 
    return goods
def best_item(revenues):
    "принимает результат  и возвращает пару «товар, выручка» с максимумом"
    return max(revenues.items(),key=lambda kv: kv[1] )
def items_report(sales):
    "список пар «товар → выручка», отсортированный по убыванию выручки"
    return sorted(sales.items(), key=lambda kv: kv[1], reverse=True)
def total_revenue(sales):
    "итоговая выручка магазина"
    return sum(price for product, price in sales.items())
if __name__ == '__main__':
    print('Самопроверка:', load_sales())
