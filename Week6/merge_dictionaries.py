# Dictionary 1
student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}

# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}

# Dictionary 3
student3 = {
    "name": "Michazwel",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}



# Check condition for name starting with "azw"
merged_students = {**{k: v for k, v in student1.items() if k == 'name' and 'ex' in str(v)},
                   **{k: v for k, v in student2.items() if k == 'name' and 'ex' in str(v)},
                   **{k: v for k, v in student3.items() if k == 'name' and 'ex' in str(v)}}
print(merged_students)