


def grade(name, homework, assessment, final_exam):
    
    total_score = homework + assessment + final_exam
    percent + round(total_score / 175) * 100
    info = { 
    "name" name,
    "score" percent
    }
    return info

student_score_homework = int(input("Homework: "))
student_score_assessment = int(input("Assessment: "))
student_score_final_exam = int(input("Final Exam: "))
student_name = input("Your Name: ")

score = grade(student_name,student_score_homework, student_score_assessment,student_score_final_exam)

if score['name']:
    print(f"{score['name']} got {score['score']}% overall")
else:
    print(score)