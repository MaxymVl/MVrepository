#!/usr/bin/python3
from datetime import timedelta
import datetime
year=timedelta(365)
name1=str(input("Введите имя, фамилию: \n"))
name=str(name1)
db=input("Введите дату рождения:  (yyyy-mm-dd) \n")
dd=input("Введите дату смерти: (yyyy-mm-dd) \n")
d_birth=datetime.datetime.strptime(db, '%Y-%m-%d').date()
d_death=datetime.datetime.strptime(dd, '%Y-%m-%d').date()
age_d=(d_death-d_birth)
age_day=int(age_d.days)
age_year=age_d.days//365
print(f'Name: {name}')
print(f'Age: {age_year}')
