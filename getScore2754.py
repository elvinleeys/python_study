grade = input()
score = 0
if grade == "A+":
    score = 4.3
elif grade == "A0":
    score = 4.0
elif grade == "A-":
    score = 3.7
elif grade == "B+":
    score = 3.3
elif grade == "B0":
    score = 3.0
elif grade == "B-":
    score = 2.7
elif grade == "C+":
    score = 2.3
elif grade == "C0":
    score = 2.0
elif grade == "C-":
    score = 1.7
elif grade == "D+":
    score = 1.3
elif grade == "D0":
    score = 1.0
elif grade == "D-":
    score = 0.7
elif grade == "F":
    score = 0.0
print(score)

# dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
#        'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
#        'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
#        'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
#        'F':'0.0'}
# grade = input()
# print(dic[grade])