# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple


def input_data():
    number_company = int(input('Введите количество предприятий для анализа (целое положительное число): '))


    companies = []
    Company = namedtuple('Company', 'name, profit', defaults=['Имя предприятия', [0, 0, 0, 0]])

    for i in range(1, number_company + 1):
        tmp_name = input(f'Введите название {i} компании: ')
        tmp_profit = [0, 0, 0, 0]
        for q in range(4):
            tmp_profit[q] = int(input(f'Введите прибыль компании {tmp_name} '
                                      f'за {q+1} квартал: '))
        current_company = Company(tmp_name, tmp_profit)
        companies.append(current_company)
    return companies


def get_avg_profit(companies):
    all_profit = 0
    for current_company in companies:
        all_profit += sum(current_company.profit)
    return all_profit / len(companies)


def get_companies_by_profit(companies, avg_profit):
    above = []
    below = []
    for current_company in companies:
        sum_profit = sum(current_company.profit)
        if sum_profit > avg_profit:
            above.append(current_company)
        elif sum_profit < avg_profit:
            below.append(current_company)

    return above, below



companies_data = input_data()
print('\n', '*' * 50, '\n')


avg_year_profit = get_avg_profit(companies_data)
print(f'Средняя прибыль компаний за год = {avg_year_profit}\n')


company_above, company_below = get_companies_by_profit(companies_data, avg_year_profit)

print(f'Предприятия с прибылью выше среднего:')
for company in company_above:
    print(company.name, sep='\n')

print(f'Предприятия с прибылью ниже среднего:')
for company in company_below:
    print(company.name, sep='\n')