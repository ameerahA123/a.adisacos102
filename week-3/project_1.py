girls_name = ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_age = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_score = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

boys_name = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_age = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_height = [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7]
boys_score = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

students = []
for i in girls_name,girls_height,girls_age,girls_score:
    students.append({'Name':girls_name[i],
                     'Age':girls_age[i],
                     'Height':girls_height[i],
                     'Score':girls_score[i]})
    
for i in range(len(boys_name)):
    students.append({'Name':boys_name[i],
                     'Age':boys_age[i],
                     'Height':boys_height[i],
                     'Score':boys_score[i]})
    
print(f"{"Name":>10}{"Age":>10}{"Height":>10}{"Score":>10}")   
print("-"*40)
for student in students:
    print(f"{student['Name']:>10}{student['Age']:>10}{student['Height']:>10}{student['Score']:>10}")

    
