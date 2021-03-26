import random

total_student = 30
total_teams = 6

student = range(total_student)

list_student = list(student)

random.shuffle(list_student)

project_team = []
for i in range(total_teams):
    num_of_members = int(total_student/total_teams)
    index = i * num_of_members
    project_team.append(list_student[index:index+num_of_members])
    
for i in project_team:
    print(i)
