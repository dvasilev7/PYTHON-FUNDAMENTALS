hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())
exam_in_minutes = hour_of_exam * 60 + minutes_of_exam
arrival_in_minutes = hour_of_arrival * 60 + minutes_of_arrival
if arrival_in_minutes > exam_in_minutes:
    print("Late")
if exam_in_minutes - 30 <= arrival_in_minutes <= exam_in_minutes:
    print("On time")
if arrival_in_minutes < exam_in_minutes - 30:
    print("Early")
if exam_in_minutes > arrival_in_minutes > exam_in_minutes - 60:
    print(f"{int(exam_in_minutes - arrival_in_minutes)} minutes before the start")
from math import fabs
new_hours = int(fabs(exam_in_minutes - arrival_in_minutes) // 60)
new_minutes = int(fabs(exam_in_minutes - arrival_in_minutes) % 60)
if arrival_in_minutes <= exam_in_minutes - 60:
    if new_minutes < 10:
        print(f"{new_hours}:0{new_minutes} hours before the start")
    if new_minutes >= 10:
        print(f"{new_hours}:{new_minutes} hours before the start")
if exam_in_minutes < arrival_in_minutes < exam_in_minutes + 60:
    print(f"{int(fabs(exam_in_minutes - arrival_in_minutes))} minutes after the start")
if arrival_in_minutes >= exam_in_minutes + 60:
    if new_minutes < 10:
        print(f"{new_hours}:0{new_minutes} hours after the start")
    if new_minutes >= 10:
        print(f"{new_hours}:{new_minutes} hours after the start")

