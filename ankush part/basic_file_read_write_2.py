import pandas as pd, os, shutil
from datetime import datetime as dt


def read_file(filename):
    '''
    receive filename, return read file
    '''
    dataframe = pd.read_excel(filename)

    return dataframe


def write_output_file(file_with_data, output_type='xlsx'):
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


def move_file(source, destination):
    ''' takes a file path, moves to another file path
    :param source:          string
    :param destination:     string
    :return:
    '''
    file_name = os.path.basename(source)
    destination_path_with_filename = os.path.join(destination, file_name)

    shutil.move(source, destination_path_with_filename)

def send_mail(receipient, sender, subject, source_file, destination_path, move_after_send=True):



    if move_after_send:
        move_file(source_file, destination_path)


def main():
    file_name = r"C:\Users\rohit\Desktop\export in dummp_python database\Trips report_16nov-Ashift.xlsx"
    file_data = read_file(file_name)
    new_file_name = write_output_file(file_data)

    archive_file_path = r"C:\Users\rohit\Desktop\export in dummp_python database\moved"
    send_mail('ankush', 'rohit', 'gm', new_file_name, archive_file_path)


    move_file(new_file_name, destination_path)


if __name__ == '__main__':
    main()