# 1. Найти тариф стоимости доставки для каждого склада
# 2. Найти суммарное количество , суммарный доход , суммарный расход и суммарную прибыль для каждого товара (представить как таблицу со столбцами
# 'product', 'quantity', 'income', 'expenses', 'profit')
# 3. Составить табличку со столбцами 'order_id' (id заказа) и 'order_profit' (прибыль полученная с заказа). А также вывести среднюю прибыль заказов
# 4. Составить табличку типа 'warehouse_name' , 'product','quantity', 'profit', 'percent_profit_product_of_warehouse' (процент прибыли продукта заказанного из определенного склада к прибыли этого склада)
# 5. Взять предыдущую табличку и отсортировать 'percent_profit_product_of_warehouse' по убыванию, после посчитать накопленный процент. Накопленный процент - это новый столбец в этой табличке, который должен называться
# 'accumulated_percent_profit_product_of_warehouse'. По своей сути это постоянно растущая сумма отсортированного по убыванию столбца 'percent_profit_product_of_warehouse'.
# 6. Присвоить A,B,C - категории на основании значения накопленного процента ('accumulated_percent_profit_product_of_warehouse'). Если значение накопленного процента меньше или равно 70, то категория A.
# Если от 70 до 90 (включая 90), то категория Б. Остальное - категория C. Новый столбец обозначить в таблице как 'category'




# 1. Найти тариф стоимости доставки для каждого склада

# import os
# import json
# import pandas as pd

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file = "trial_task.json"
# json_path = os.path.join(current_dir, json_file)

# df = pd.read_json(json_path)

# total_quantities = []
# for products_list in df['products']:
#     total_quantity = 0
#     for product in products_list:
#         total_quantity += product['quantity']
#     total_quantities.append(total_quantity)

# df['total_quantity'] = total_quantities
# df['unit_cost'] = df['highway_cost'] / df['total_quantity']

# print(df[['warehouse_name', 'unit_cost']])





# 2. Найти суммарное количество , суммарный доход , суммарный расход и суммарную прибыль для каждого товара (представить как таблицу со столбцами
# 'product', 'quantity', 'income', 'expenses', 'profit')





# import os
# import json
# import pandas as pd

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file = "trial_task.json"
# json_path = os.path.join(current_dir, json_file)

# with open(json_path, 'r') as f:
#     data = json.load(f)

# df = pd.json_normalize(data, record_path='products', meta=['order_id', 'warehouse_name', 'highway_cost'])

# grouped_data = df.groupby('product').agg(
#     total_quantity=('quantity', 'sum'),
#     total_income=('price', 'sum'),
#     total_expenses=('highway_cost', 'sum')
# )

# В данной строке используем + вместо - так как value от highway_cost изначально отрицательное 
# grouped_data['total_profit'] = grouped_data['total_income'] + grouped_data['total_expenses']

# result_table = grouped_data.reset_index()
# print(result_table)





# 3. Составить табличку со столбцами 'order_id' (id заказа) и 'order_profit' (прибыль полученная с заказа). А также вывести среднюю прибыль заказов





# import os
# import json
# import pandas as pd

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file = "trial_task.json"
# json_path = os.path.join(current_dir, json_file)

# with open(json_path, 'r') as f:
#     data = json.load(f)

# df = pd.json_normalize(data, record_path='products', meta=['order_id', 'warehouse_name', 'highway_cost'])

# df['order_profit'] = df['quantity'] * df['price'] + df['highway_cost']
# order_table = df.groupby('order_id')['order_profit'].sum().reset_index()
# total_profit = order_table['order_profit'].sum()
# average_profit = order_table['order_profit'].mean()

# print(order_table)
# print("\nОбщая прибыль: ", total_profit)
# print("Средняя прибыль заказов: ", average_profit)





# 4. Составить табличку типа 'warehouse_name' , 'product','quantity', 'profit', 'percent_profit_product_of_warehouse' (процент прибыли продукта заказанного из определенного склада к прибыли этого склада)





# import os
# import json
# import pandas as pd

# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file = "trial_task.json"
# json_path = os.path.join(current_dir, json_file)

# with open(json_path, 'r') as f:
#     data = json.load(f)

# df = pd.json_normalize(data, record_path='products', meta=['order_id', 'warehouse_name', 'highway_cost'])

# df['product_profit'] = df['quantity'] * df['price']

# warehouse_product_data = df.groupby(['warehouse_name', 'product']).agg(
#     quantity=('quantity', 'sum'),
#     profit=('product_profit', 'sum'),
#     total_warehouse_profit=('highway_cost', 'sum')
# ).reset_index()

# warehouse_product_data['percent_profit_product_of_warehouse'] = warehouse_product_data['profit'] / warehouse_product_data['total_warehouse_profit'] * -100

# # СОРТИРОВКА ПО УБЫВАНИЮ С НАКОПЛЕННЫМ ПРОЦЕНТОМ
# # ЗАДАЧА 5


# warehouse_product_data = warehouse_product_data.sort_values(by='percent_profit_product_of_warehouse', ascending=False)
# warehouse_product_data['accumulated_percent_profit_product_of_warehouse'] = warehouse_product_data['percent_profit_product_of_warehouse'].cumsum()


# # Присваиваем категории A, B и C на основании значения накопленного процента
# # ЗАДАЧА 6


# warehouse_product_data['category'] = pd.cut(
#     warehouse_product_data['accumulated_percent_profit_product_of_warehouse'],
#     bins=[-float('inf'), 70, 90, float('inf')],
#     labels=['A', 'B', 'C']
# )


# print(warehouse_product_data)