import csv
import pandas as pd
import openpyxl


def head():
    header = ['Brand', 'Model', 'Color', 'Year', 'Millage']

    with open('d_base.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(header)


class Car:

    def __init__(self, brand, model, color, year, millage):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.millage = millage


def c_base():

    cars = Car(input('Brand: '), input('Model: '), input('Color: '),
                input('Year: '), input('Millage: '))

    c = (cars.brand, cars.model, cars.color, cars.year, cars.millage)

    with open('d_base.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(c)


def del_row():
    edit_data = pd.read_csv('d_base.csv')
    edit_data.index += 1
    print(edit_data)
    num = int(input('Choose A Vehicle Index To Edit: '))

    if 0 < num <= (len(edit_data)):
        updated_edit_data = edit_data.drop(edit_data.index[num - 1])
        updated_edit_data.to_csv('d_base.csv', index=False)

    else:
        print('Incorrect Input!')
        del_row()


def view_data():
    print_data = pd.read_csv('d_base.csv')
    print_data.index += 1
    print(print_data)


def ex_data():
    xl_data = pd.read_csv('d_base.csv')
    xl_data.index += 1
    xl_data.to_excel('exl_data.xlsx', index=None, header=True)
    xl_data.to_json('j_data.json')
