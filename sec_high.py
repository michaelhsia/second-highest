def second_highest(students):
    grades = [s[1] for s in students] # 速寫法, 只把成績拿出來, 把students中每一位的成績列入新建的grades清單中
    grades = sorted(grades, reverse=True) # reverse=True去掉會變成由小到大排列
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    # 再下來找誰是這個分數
    # 底下這句話的意思是拿到, 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
    # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student)


second_highest([['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]])