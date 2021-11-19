import pandas as pd, os, sys
from datetime import datetime as dt


def read_file(filename):
    '''
    receive filename, return read file
    '''
    dataframe = pd.read_excel(filename)

    return dataframe


def write_output_file(file_with_data, output_type):
    '''
    recieves variable with data, writes to a new file
    '''
    if output_type == 'csv':
        output_file_name = r"C:\Users\rohit\Desktop\export in dummp_python database\new_exported_file.csv"
        file_with_data.to_csv(output_file_name, index=False)

    elif output_type == 'xlsx':
        output_file_name = r"C:\Users\rohit\Desktop\export in dummp_python database\new_exported_file.xlsx"
        file_with_data.to_excel(output_file_name, index=False)

    return output_file_name



def main():
    arg1 = sys.argv[1] if sys.argv[1] else 'xlsx'

    file_name = r"C:\Users\rohit\Desktop\export in dummp_python database\Trips report_16nov-Ashift.xlsx"

    file_data = read_file(file_name)

    new_file_name = write_output_file(file_with_data=file_data, output_type=arg1)


if __name__ == '__main__':
    main()