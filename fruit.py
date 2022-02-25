import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
df_product = pd.read_csv('product.csv')
x = df_product['COUNTRY']
y = height=df_product['QUANTITY']
# print(f" {df_product[' Sale Price ']}   {df_product['Country']}")
def bargraph():
    plt.figure(figsize=(10, 10))
    plt.bar(x, y,  color='#C70039')
    plt.title('Car Sales by Country')
    plt.xlabel = 'Country'
    plt.ylabel = 'Quantity (per year) 1000x'
    plt.xticks(rotation=45)

def subgraph():
    plt.subplots(figsize=(10, 6))
    plt.xlabel = 'Country'
    plt.ylabel = 'Quantity (per year) 1000x'
    plt.plot(x,y)
    plt.title('Car Sales by Country')
    plt.xticks(rotation=45)

def stackgraph():
    plt.figure(figsize=(10, 6))
    plt.stackplot(x, y, colors='#ebc034')
    plt.xlabel = 'Country'
    plt.ylabel = 'Quantity (per year) 1000x'
    plt.plot(x, y)
    plt.title('Car Sales by Country')
    plt.xticks(rotation=45)


def scatter():
    plt.figure(figsize=(10, 10))
    plt.scatter(x, y, color ='red',)
    plt.title('Car Sales by country')
    plt.xlabel('contry')
    plt.ylabel('Quantity')
    plt.title('Car Sales by Country')
    plt.xticks(rotation=45)
    plt.legend()
def piegraph():
    country_list = df_product['COUNTRY'].values.tolist()
    car_list = df_product['QUANTITY'].values.tolist()
    cars = sum(car_list)
    perc_list = []

    for c in car_list:
        perc = round(c / cars * 100)
        perc_list.append(perc)

    colors = ['r', 'g', 'b', 'c', 'm','#ebc034', '#eb34de', '#345eeb', '#12db29', '#1c1919']
    plt.pie(perc_list, labels = country_list, explode=(0.2,0,0,0.1,0,0,0,0,0),  colors = colors,
            startangle = 90, shadow = True, autopct ='%1.1f%%')
    plt.title('Car Sales by country')

def rungraph():
    scatter()
    bargraph()
    subgraph()
    stackgraph()
    piegraph()
    plt.show()

rungraph()