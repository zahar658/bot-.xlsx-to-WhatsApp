import pandas
class Person:
    name = -1
    lastname = -1
    surname = -1



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    excel_data_df = pandas.read_excel('Общая таблица НФИ плюс БИ.xlsx', sheet_name='Лист1')

    a = excel_data_df['ФИО клиента']
    print(a)
    pop = []
    for p in a:
        hery = Person()
        hery.name = p
        pop.append(hery)
        print(p)
    print('\n')
    print(pop[5].name)


    # print whole sheet data
    # print(excel_data_df)
    # print("\n")
    # print(excel_data_df.columns.name)
    # print_hi('PyCharm')

