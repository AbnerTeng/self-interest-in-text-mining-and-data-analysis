import numpy as np
grades = {}

def student_system():
    while True:
        print(f"--------------")
        print(f"grade management system")
        print(f"--------------")
        print(f"1. manage grades")
        print(f"2. show grades")
        print(f"3. statistical data")
        print(f"4. exit")
        c = input(">= ")

        if c == "1":
            func_1()
        elif c == "2":
            func_2()
        elif c == "3":
            func_3()
        elif c == "4":
            break
        else:
            print(f"invalid input")

def func_1():
    while True:
        print(f"--------------")
        print(f"manage grades")
        print(f"--------------")
        print(f"1. add grade")
        print(f"2. delete grade")
        print(f"3. back to main menu")
        c = input(">= ")

        if c == "1":
            add_grade()
        elif c == "2":
            delete_grade()
        elif c == "3":
            break
        else:
            print(f"invalid input")

def func_2():
    while True:
        print(f"--------------")
        print(f"show grades")
        print(f"--------------")
        print(f"1. By student id")
        print(f"2. show_all_grades")
        print(f"3. back to main menu")
        c = input(">= ")

        if c == "1":
            find_grade()
        elif c == "2":
            show_grades()
        elif c == "3":
            break
        else:
            print(f"invalid input")

def func_3():
    while True:
        print(f"--------------")
        print(f"statistical data")
        print(f"--------------")
        print(f"1. search by student id")
        print(f"2. show all data")
        print(f"3. back to main menu")
        c = input(">= ")

        if c == "1":
            find_data()
        elif c == "2":
            show_all_datas()
        elif c == "3":
            break
        else:
            print(f"invalid input")

def add_grade():
    while True:
        print(f"--------------")
        print(f"add grade")
        print(f"--------------")
        print(f"1. add hw1")
        print(f"2. add hw2")
        print(f"3. add hw3")
        print(f"4. add hw4")
        print(f"5. back to main menu")
        c = input(">= ")

        if c == "1":
            add_hw1()
        elif c == "2":
            add_hw2()
        elif c == "3":
            add_hw3()
        elif c == "4":
            add_hw4()
        elif c == "5":
            break
        else:
            print(f"invalid input")

def delete_grade():
    id = input("student id: ")

    if id in grades.keys():
        del grades[id]
        print(f"grade is deleted")

        ## delete grades from file
        with open("grades.csv", "w") as f:
            for id, grade in grades.items():
                f.write(f"{id}, {grade[0]}, {grade[1]}, {grade[2]}, {grade[3]}, {grade[4]}\n")
    else:
        print(f"grade is not found")

def add_hw1():
    id = input("student id: ")
    name = input("stduent name: ")
    hw1 = input("hw1: ")

    grades[id] = [name, hw1]
        ## save grades to file
    with open("grades.csv", "w") as f:
        for id, grade in grades.items():
            f.write(f"{id}, {grade[0]}, {grade[1]}\n")

def add_hw2():
    id = input("student id: ")
    name = input("stduent name: ")
    hw2 = input("hw2: ")

    grades[id] = [name, hw1, hw2]
        ## save grades to file
    with open("grades.csv", "w") as f:
        for id, grade in grades.items():
            f.write(f"{id}, {grade[0]}, {grade[1]}\n")

def find_grade():
    id = input("student id: ")

    if id in grades.keys():
        grade = grades[id]
        print(f"student id: ", id, ',', grade[0], 'score: hw1=', grade[1], ', hw2=', grade[2], ', hw3=', grade[3], ', hw4=', grade[4])
    else:
        print(f"grade is not found")

def show_grades():
    if len(grades) == 0:
        print(f"no grade")
        return
    
    for id, grade in grades.items():
        print(f"student id: ", id, ',', grade[0], 'score: hw1=', grade[1], ', hw2=', grade[2], ', hw3=', grade[3], ', hw4=', grade[4])

def find_data():
    id = input("student id: ")

    if id in grades.keys():
        grade = grades[id]

def show_all_datas():
    print(f'haven\'t done yet')
        

def add_grade():
    id = input("student id: ")
    name = input("student name: ")
    hw1 = input("hw1: ")
    hw2 = input("hw2: ")
    hw3 = input("hw3: ")
    hw4 = input("hw4: ")

    grades[id] = [name, hw1, hw2, hw3, hw4]
    ## save grades to file
    with open("grades.csv", "w") as f:
        for id, grade in grades.items():
            f.write(f"{id}, {grade[0]}, {grade[1]}, {grade[2]}, {grade[3]}, {grade[4]}\n")
    
    print(f"new grade is added")