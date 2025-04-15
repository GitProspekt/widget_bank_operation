# "C:\Users\kdo_k\PycharmProjects\widget_bank_operation\transactions_excel.xlsx"
# "C:\Users\kdo_k\PycharmProjects\widget_bank_operation\transactions.csv"
import pandas as pd


def read_csv_file_transactions(csv_path):
    """ Считывает финансовые операции из CSV-файла и возвращает список словарей с транзакциями"""
    # Читаем CSV-файл с указанием разделителя ';'
    df = pd.read_csv(csv_path, delimiter=';')

    # Заменяем NaN на None для корректного преобразования в словарь
    df = df.where(pd.notnull(df), None)

    transactions = df.to_dict('records')

    return transactions

# transactions = read_csv_file_transactions('C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\transactions.csv')
# for transaction in transactions[:5]:
#     print(transaction)


def read_excel_file_transactions(file_path):
    """ Считывает финансовые операции из Excel-файла и возвращает список словарей с транзакциями"""
    # Читаем Excel-файл в DataFrame
    df = pd.read_excel(file_path)
    df = df.where(pd.notnull(df), None)
    transactions = df.to_dict('records')

    return transactions


# if __name__ == "__main__":
#
#     file_path = 'C:\\Users\\kdo_k\\PycharmProjects\\widget_bank_operation\\transactions_excel.xlsx'
#     transactions = read_excel_file_transactions(file_path)
#     for i, transaction in enumerate(transactions[:5], 1):
#         print(f"Транзакция {i}: {transaction}")
