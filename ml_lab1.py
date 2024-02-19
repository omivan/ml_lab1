
"""# Imports"""

import pandas as pd
import matplotlib.pyplot as plt



"""
## Constants
"""

pd.set_option('display.float_format', '{:.2f}'.format)
k = 12 # Іван
m = 4

print("1. Відкрити та зчитати файл з даними.")

data = pd.read_csv('Vehicle_Sales.csv')

print("2. Визначити та вивести кількість записів та кількість полів у кожному записі.")

print(f'Кількість записів: {data.shape[0]}')
print(f'Кількість полів: {data.shape[1]}')

print("3. Вивести К+7 перших та 5К-3 останніх записів.")

print(f"Перші K+7: { k +7}")
print(data.head( k +7))

print(f"Останні 5К-3: { 5 * k -3}")
print(data.tail( 5 * k -3))

print("4. Визначити та вивести тип полів кожного запису.")

print(data.dtypes)

print("5. Привести поля, що відповідають обсягам продаж, до числового вигляду (показати, що це виконано).")

# data_test = data['Total Sales New'] = data['Total Sales New'].str.replace('$', '', regex=True)
# print(data_test)
data['Total Sales New'] = data['Total Sales New'].apply(lambda x: float(x.replace('$', '')))
data['Total Sales Used'] = data['Total Sales Used'].apply(lambda x: float(x.replace('$', '')))
print(data.dtypes)

print(data.head(3))

print("6. Ввести нові поля:")
print("a. Сумарний обсяг продаж автомобілів (нових та б/в) у кожний період;")


data['Total Sales Number'] = data['New'] + data['Used']
print(data.head(3))

print("b. Сумарний дохід від продажу автомобілів (нових та б/в) у кожний період;")



data['Total Sales'] = data['Total Sales New'] + data['Total Sales Used']
print(data.head(3))

print("c. Різницю в обсязі продаж нових та б/в автомобілів у кожній період.")

data['Sales Number Diff'] = data['New'] - data['Used']
print(data.head(3))

print("7. Змінити порядок розташування полів таким чином: Рік, Місяць, Сумарний дохід,"
      " Дохід від продажу нових автомобілів, Дохід від продажу б/в автомобілів,"
      " Сумарний обсяг продаж, Обсяг продаж нових автомобілів, "
      "Обсяг продаж б/в автомобілів, Різниця між обсягами продаж нових та б/в автомобілів.")

data = data[['Year', 'Month', 'Total Sales', 'Total Sales New',
             'Total Sales Used', 'Total Sales Number', 'New', 'Used', 'Sales Number Diff']]
print(data.head(3))

print("8. Визначити та вивести:")
print("a. Рік та місяць, у які нових автомобілів було продано менше за б/в;")


data_diff = data[data['Sales Number Diff' ] <0][['Year', 'Month']]
print(data_diff)

print("b. Рік та місяць, коли сумарний дохід був мінімальним;")

data_max_sales = data.loc[[data['Total Sales'].idxmin()], ['Year', 'Month']]
print(data_max_sales)

print("c. Рік та місяць, коли було продано найбільше б/в авто.")

data_max_sales_number = data.loc[[data['Total Sales Number'].idxmax()], ['Year', 'Month']]
print(data_max_sales_number)

print("9. Визначити та вивести:")
print("a. Сумарний обсяг продажу транспортних засобів за кожен рік;")


data_year_sales_number = data.groupby(['Year'])[['Total Sales Number']].sum()
print(data_year_sales_number)

print("b. Середній дохід від продажу б/в транспортних засобів в місяці"
      " М, де М – це порядковий номер у списку підгрупи за абеткою.")

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
average_income_by_month = data[data['Month' ] == months[ m -1]].groupby('Month')['Total Sales Used'].mean().reset_index()
print(average_income_by_month)

print(" 10.  Побудувати стовпчикову діаграму обсягу продаж нових авто у році 20YY"
      ", де дві останні цифри року визначаються як 17 – порядковий "
      "номер у списку підгрупи за абеткою.")

year = 2017 - m
data_2017 = data[data['Year'] == year]

sales_by_month_2017 = data_2017.groupby('Month', sort=False)['Total Sales New'].sum().reset_index()

plt.bar(sales_by_month_2017['Month'], sales_by_month_2017['Total Sales New'])
plt.title(f'Sales of New Cars in {year}')
plt.xlabel('Month')
plt.ylabel('Sales New Cars')
plt.show()

print(" 11.Побудувати кругову діаграму сумарного обсягу продаж за кожен рік.")

temp_data = pd.DataFrame(data_year_sales_number).reset_index()
plt.pie(temp_data['Total Sales Number'], labels=temp_data['Year'], autopct='%1.1f%%')
plt.title('Total Sales Volume by Years')
plt.show()

print("12. Побудувати на одному графіку:")


total_income_new = data.groupby('Year')['Total Sales New'].sum()
total_income_used = data.groupby('Year')['Total Sales Used'].sum()

df_total_income = pd.DataFrame({
    'Total Income New': total_income_new,
    'Total Income Used': total_income_used
}).reset_index()

plt.plot(df_total_income['Year'], df_total_income['Total Income New'], label='Income from New Cars')
plt.plot(df_total_income['Year'], df_total_income['Total Income Used'], label='Income from Used Cars')

plt.title('Total Income from Car Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Income')
plt.legend()

plt.show()
