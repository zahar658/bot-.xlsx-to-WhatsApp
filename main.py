import pandas

# excel_data_df = pandas.read_excel('records.xlsx', sheet_name='Employees')
#
# # print whole sheet data
# print(excel_data_df)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    excel_data_df = pandas.read_excel('lol.xlsx', sheet_name='Лист1')

    # print whole sheet data
    print(excel_data_df)
    print("\n")
    print(excel_data_df.columns.name)
    print_hi('PyCharm')

