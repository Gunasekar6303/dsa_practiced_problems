# (1) Task: Given a list of employee records containing nested lists/dictionaries,
# return the names of employees who have the skill "Python" AND a performance rating above 4.0
def employees_list(employees):
    result = []
    for item in employees:
        if item["rating"] > 4.0 and "Python" in item["skills"]:
            result.append(item["name"])
    return result


employees = [
    {"name": "Rahul", "rating": 4.5, "skills": ["Python", "Docker"]},
    {"name": "Anita", "rating": 3.8, "skills": ["Python", "SQL"]},
    {"name": "Suresh", "rating": 4.2, "skills": ["Java", "C++"]},
    {"name": "Priya", "rating": 4.9, "skills": ["Python", "Machine Learning"]}
]
print(employees_list(employees))

#(2)Aggregation & Mapping (Intermediate)
# Task: Given a list of student records, return a list of dictionaries containing
# only the name and status ("Pass" if score >= 60, else "Fail") for students who are enrolled ("enrolled": True)
# Expected Output: [{"name": "Karan", "status": "Pass"}, {"name": "Meera", "status": "Fail"}]

def pass_fail(students):
    result = []
    for item in students:
        if item["score"] >= 60:
            status = "Pass"
        else:
            status = "Fail"
        if item["enrolled"] == True and item["score"] >= 60:
            result.append({"name": item["name"], "status": status})
    return result


students = [
    {"name": "Karan", "score": 85, "enrolled": True},
    {"name": "Meera", "score": 77, "enrolled": True},
    {"name": "Vikram", "score": 90, "enrolled": False}
]
print(pass_fail(students))