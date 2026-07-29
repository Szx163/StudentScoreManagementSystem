# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5．列出所有学生：遍历所有学生信息并输出。
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7．退出系统。
# "Mate80":{'a':6999,'b':4999,'c':7999}
from itertools import count

inform="""
   ~ 欢迎使用教务管理系统 ~
     1,按录入学生信息
     2,修改学生信息
     3,删除学生信息
     4,查询学生信息
     5,列出所有学生信息
     6,统计班级成绩
     7,退出系统  
"""
stu_information={}
# stu_information["Mate60"]={"a":6999,"b":4999,"c":7999}
# stu_information["Mate80"]={"a":7999,"b":5999,"c":8999}
# print(stu_information)
while 1:
    print(inform)
    in_fun = input("请输入可选功能(1~7):")
    if not in_fun.isdigit():
        print("请输入有效数字!")
        continue
    if not (1<=int(in_fun)<=7):
        print("请输入有效范围(1~7)!")

    match int(in_fun):
        case 1:
            # 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
            stu_name=input("请输入学生姓名:")
            if stu_name in stu_information:
                print("所输入学生信息已存在!")
                continue
            stu_Chi_score=int(input("请输入学生语文成绩:"))
            stu_Mat_score = int(input("请输入学生数学成绩:"))
            stu_Eng_score = int(input("请输入学生英语成绩:"))
            # 字典存储 注意角标 'stu_name'
            stu_information[stu_name]= {"Chi":stu_Chi_score, "Mat":stu_Mat_score, "Eng":stu_Eng_score}
            print(f"{stu_name}成绩:{stu_information[stu_name]}存储成功!")
        case 2:
            # 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
            stu_name=input("请输入需要修改信息的学生姓名:")
            if stu_name not in stu_information:
                print("所输入学生姓名不在系统内!")
                continue
            stu_Chi_score = int(input("请输入需要修改学生的语文成绩:"))
            stu_Mat_score = int(input("请输入需要修改学生的数学成绩:"))
            stu_Eng_score = int(input("请输入需要修改学生的英语成绩:"))
            stu_information[stu_name]={"Chi":stu_Chi_score, "Mat":stu_Mat_score, "Eng":stu_Eng_score}
        case 3:
            # 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
            stu_name=input("请输入需要修改信息的学生姓名:")
            if stu_name not in stu_information:
                print("所输入学生姓名不在系统内!")
                continue
            del stu_information[stu_name]
            print("删除成功!")
        case 4:
            # 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
            stu_name=input("请输入要查询学生姓名:")
            if stu_name not in stu_information:
                print("所输入学生姓名不在系统内!")
                continue
            print(f"{stu_name}成绩:{stu_information[stu_name]}")
        case 5:
             # 5．列出所有学生：遍历所有学生信息并输出。
            print(stu_information[stu_name])
            for stu in stu_information.keys():
                print(f"{stu}语文成绩:{stu_information[stu]['Chi']}数学成绩:{stu_information[stu]['Mat']}"
                      f"英语成绩:{stu_information[stu]['Eng']}\n")

        case 6:
            # 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，
            # 以及语文、数学、英语最高分和最低分的学员姓名。
            (Chi_Averge,Mat_Averge,Eng_Averge,Chi_Max,
             Mat_Max,Eng_Max,Chi_Min,Mat_Min,Eng_Min)=0,0,0,0,0,0,0,0,0
            ChiMaxName=""
            MatMaxName=""
            EngMaxName=""
            count=0
            for stu in stu_information.keys():
               Chi_Averge+=stu_information[stu]['Chi']
               Mat_Averge+=stu_information[stu]['Mat']
               Eng_Averge+=stu_information[stu]['Eng']
                # 初始化避免最小值 'Min'为 0
               Chi_Min=int(stu_information[stu]['Chi'])
               Mat_Min=int(stu_information[stu]['Mat'])
               Eng_Min=int(stu_information[stu]['Eng'])
               if Chi_Max <int(stu_information[stu]['Chi']):
                   Chi_Max=int(stu_information[stu]['Chi'])
                   ChiMaxName=stu
               if Chi_Min >int(stu_information[stu]['Chi']):
                   Chi_Min=int(stu_information[stu]['Chi'])
               if Mat_Max <int(stu_information[stu]['Mat']):
                   Mat_Max=int(stu_information[stu]['Mat'])
                   MatMaxName=stu
               if Mat_Min >int(stu_information[stu]['Mat']):
                   Mat_Min=int(stu_information[stu]['Mat'])
               if Eng_Max <int(stu_information[stu]['Eng']):
                   Eng_Max=int(stu_information[stu]['Eng'])
                   EngMaxName=stu
               if Eng_Min >int(stu_information[stu]['Eng']):
                   Eng_Min=int(stu_information[stu]['Eng'])
               count+=1
            Chi_Averge=Chi_Averge/count
            Mat_Averge=Mat_Averge/count
            Eng_Averge=Eng_Averge/count
            print(f"{ChiMaxName}语文分最高:{Chi_Max};\t班级语文最低分:{Chi_Min}\n"
                  f"{MatMaxName}数学分最高分:{Mat_Max};\t班级数学最低分:{Mat_Max}\n"
                  f"{EngMaxName}英语分最高:{Eng_Max};\t班级英语最低分:{Eng_Max}\n"
                  f"语文平均分:{Chi_Averge};\t数学平均分:{Mat_Averge};\t英语平均分:{Eng_Averge}\n")
        case 7:
            break













