year = input()
p = int(input())
h = int(input())
weekends_in_Sofia = 48 - h
vacation_days_in_Sofia = p * 2 / 3
volleyball_weekends_sofia =  weekends_in_Sofia * 3/4
playdaytes = vacation_days_in_Sofia + volleyball_weekends_sofia + h
if year == "leap":
    playdaytes *= 1.15
from math import floor
print(floor(playdaytes))