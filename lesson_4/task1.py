from sys import argv

script_name, hours, rate, premium = argv
hours = int(hours)
rate = float(rate)
premium = float(premium)
print("Размер ЗП сотрудника: ", str(hours*rate+premium))

