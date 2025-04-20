import pyttsx3 
import speech_recognition as sr 
import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',passwd='Av@2910200fouR',database='sms')
mycursor=mycon.cursor()

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)

def talk(text):
        engine.say(text)
        engine.runAndWait()

def take_command():
        with sr.Microphone() as source:
                print("I'M LISTENING")
                print(100 * '-')
                listener.pause_threshold = 1
                voice = listener.listen(source)
                print("RECOGNISING......")
                print(100 * '=')
        try:
                command = listener.recognize_google(voice)
                a= command.upper()
                print("USER SAID : ", a)
                print(100 * '=')
        except Exception as e:
                print("SAY THAT AGAIN PLEASE")
                print(100 * '=')
                return 'None'
        return command

def voice_command():
        print(100 * '=')
        print("                                      SCHOOL MANAGEMENT SYSTEM                                      ")
        print(100 * '=')
        print("TO DISPLAY ALL RECORDS                                                                              ")
        print(100 * '-')
        print('          1. SAY "DISPLAY ALL RECORDS" TO DISPLAY ALL THE RECORDS                                   ')
        print(100 * '=')
        print("TO SEARCH RECORDS BY ROLL NUMBER                                                                    ")
        print(100 * '-')
        print('          1. SAY "SEARCH BY ROLL NUMBER" TO SEARCH AND DISPLAY SAID RECORD                          ')
        print(48* '-', 'OR', 48*'-')
        print('          2. SAY "SEARCH MY ROLL NUMBER" TO SEARCH AND DISPLAY SAID RECORD                          ')
        print(100 * '=')
        print("TO SEARCH RECORDS BY NAME                                                                           ")
        print(100 * '-')
        print('          1. SAY "SEARCH BY NAME" TO SEARCH AND DISPLAY SAID RECORD                                 ')
        print(48* '-', 'OR', 48*'-')
        print('          2. SAY "SEARCH MY NAME" TO SEARCH AND DISPLAY SAID RECORD                                 ')
        print(100 * '=')
        print("TO DELETE RECORDS                                                                                   ")
        print(100 * '-')
        print('          1. SAY "DELETE RECORD" TO SEARCH AND DELETE SAID RECORD                                   ')
        print(100 * '=')
        print("TO END THE PROGRAM                                                                                  ")
        print(100 * '-')
        print('          1. SAY "EXIT" TO END THE PROGRAM                                                          ')
        print(48* '-', 'OR', 48*'-')
        print('          2. SAY "END" TO END THE PROGRAM                                                           ')
        print(100 * '=')
        
        talk("read the instructions properly to know how to use voice command")

        def displayallrecords():
                query="select * from studentdetails"
                mycursor.execute(query)
                data=mycursor.fetchall()
                count = 1
                for i in data:
                        engine.setProperty('rate',230)
                        talk("record number")
                        talk(count)
                        talk("Roll Number"), talk(i[0])
                        talk("Admission Number"), talk(i[1])
                        talk("Student Name"), talk(i[2])
                        talk("Class"), talk(i[3])
                        talk("Date of Birth"), talk(i[4])
                        talk("Gender") ,talk(i[5])
                        talk("Father Name"), talk(i[6])
                        talk("Mother Name"), talk(i[7])
                        talk("Phone Number"), talk(i[8])
                        talk("Aadhaar Number"), talk(i[9])
                        talk("Email"), talk(i[10])
                        talk("Stream"), talk(i[11])
                        talk("Percentage"), talk(i[12])
                        talk("Blood Group"), talk(i[13])
                        talk("Address"), talk(i[14])
                        count +=1

        def searchrollno():
                talk("say the roll number to search")
                roll=take_command()
                roll=str(roll)
                roll=roll.upper()
                fn=0
                query = "select * from studentdetails"
                mycursor.execute(query)
                r=mycursor.fetchall()
                for i in r:
                        if i[0] == roll:
                                engine.setProperty('rate',230)
                                talk("Roll Number"), talk(i[0])
                                talk("Admission Number"), talk(i[1])
                                talk("Student Name"), talk(i[2])
                                talk("Class"), talk(i[3])
                                talk("Date of Birth"), talk(i[4])
                                talk("Gender") ,talk(i[5])
                                talk("Father Name"), talk(i[6])
                                talk("Mother Name"), talk(i[7])
                                talk("Phone Number"), talk(i[8])
                                talk("Aadhaar Number"), talk(i[9])
                                talk("Email"), talk(i[10])
                                talk("Stream"), talk(i[11])
                                talk("Percentage"), talk(i[12])
                                talk("Blood Group"), talk(i[13])
                                talk("Address"), talk(i[14])
                                fn=1
                if fn==0:
                        talk("Record doesn't exist")
                        
        def searchname():
                talk("say the name to search")
                name=take_command()
                name=str(name)
                name=name.upper()
                fn=0
                query = "select * from studentdetails"
                mycursor.execute(query)
                s=mycursor.fetchall()
                for i in s:
                        if i[2] == name:
                                engine.setProperty('rate',230)
                                talk("Roll Number"), talk(i[0])
                                talk("Admission Number"), talk(i[1])
                                talk("Student Name"), talk(i[2])
                                talk("Class"), talk(i[3])
                                talk("Date of Birth"), talk(i[4])
                                talk("Gender") ,talk(i[5])
                                talk("Father Name"), talk(i[6])
                                talk("Mother Name"), talk(i[7])
                                talk("Phone Number"), talk(i[8])
                                talk("Aadhaar Number"), talk(i[9])
                                talk("Email"), talk(i[10])
                                talk("Stream"), talk(i[11])
                                talk("Percentage"), talk(i[12])
                                talk("Blood Group"), talk(i[13])
                                talk("Address"), talk(i[14])
                                fn=1
                if fn == 0:
                        talk("record doesn't exist")
                        
        def deleterecord():
                talk("say the roll number to delete")
                delete=take_command()
                delete=str(delete)
                delete=delete.upper()
                fn=0
                q="select * from studentdetails"
                mycursor.execute(q)
                d=mycursor.fetchall()
                for i in d:
                        if i[0]==delete:
                                print("ROLL NUMBER : ", i[0])
                                print("ADMISSION NUMBER : ", i[1])
                                print("STUDENT NAME : ", i[2])
                                print("CLASS : ", i[3])
                                print("DATE OF BIRTH (MM/DD/YYYY) : ", i[4])
                                print("GENDER : ", i[5])
                                print("FATHER NAME : ", i[6])
                                print("MOTHER NAME : ", i[7])
                                print("PHONE NUMBER : ", i[8])
                                print("AADHAAR NUMBER : ", i[9])
                                print("EMAIL : ", i[10])
                                print("STREAM : ", i[11])
                                print("PERCENTAGE : ", i[12])
                                print("BLOOD GROUP : ", i[13])
                                print("ADDRESS : ", i[14])
                                print(100 * '=')
                                talk("do you want to delete said record? say yes or no")
                                deletee = take_command()
                                deletee = str(deletee)
                                deletee = deletee.upper()
                                if deletee == 'YES':
                                        query="delete from studentdetails where rollno =%s"
                                        us=(delete,)
                                        mycursor.execute(query,us)
                                        mycon.commit()
                                        fn=1
                                        talk("record deleted")
                                else:
                                        talk("record not deleted")
                                        return
                if fn == 0:
                        talk("record doesn't exist")

        while True:
                command = take_command()
                if 'display all records' in command:
                        displayallrecords()
                        continue
                elif 'search by roll number' in command or 'search my roll number' in command:
                        searchrollno()
                        continue
                elif 'search by name' in command or 'search my name' in command:
                        searchname()
                        continue
                elif 'delete record' in command:
                        deleterecord()
                        continue
                elif 'exit' in command :
                        print(45 * " ", "THE END", 46 * " ")
                        print(100 * '=')
                        talk("have a good day")
                        break
                elif 'end' in command:
                        print(45 * " ", "THE END", 46 * " ")
                        print(100 * '=')
                        talk("have a good day")
                        break
                else:
                        talk("i didn't get you, can you say it again please")
                        continue

def enter_details_manually():
        class student(object):
                def __int__(s):
                        s.roll = ""
                        s.admnno = 0
                        s.name = ""
                        s.cls = ""
                        s.dob = ""
                        s.gender = ""
                        s.fname = ""
                        s.mname = ""
                        s.phone = 0
                        s.aadhaar = 0
                        s.email = ""
                        s.stream=""
                        s.per=0
                        s.bloodgroup = ""
                        s.address = ""
                        
                def add_rec(s):
                        s.roll = int(input("ENTER ROLL NUMBER : "))
                        s.roll = str(s.roll)
                        s.roll = s.roll.upper()
                        fn = 0
                        query= "select * from studentdetails"
                        mycursor.execute(query)
                        r=mycursor.fetchall()
                        for i in r:
                                if s.roll == i[0]:
                                        print(100 * '=')
                                        print("##ROLL NUMBER ALREADY EXISTS, PLEASE TRY ANOTHER ROLL NUMBER##")
                                        fn=1
                                        return
                        if fn == 0:
                                s.admnno = int(input("ENTER ADMISSION NUMBER : "))
                                s.admnno = str(s.admnno)
                                s.admnno = s.admnno.upper()
                                s.name = input("ENTER STUDENT NAME : ")
                                s.name = s.name.upper()
                                def classs():
                                        s.cls = input("ENTER CLASS : ")
                                        s.cls = s.cls.upper()
                                        if s.cls == '1-A' or s.cls == '1-B' or s.cls == '1-C' or s.cls == '2-A' or s.cls == '2-B' or s.cls == '2-C':
                                                return
                                        elif s.cls == '3-A' or s.cls == '3-B' or s.cls == '3-C' or s.cls == '4-A' or s.cls == '4-B' or s.cls == '4-C':
                                                return
                                        elif s.cls == '5-A' or s.cls == '5-B' or s.cls == '5-C' or s.cls == '6-A' or s.cls == '6-B' or s.cls == '6-C':
                                                return
                                        elif s.cls == '7-A' or s.cls == '7-B' or s.cls == '7-C' or s.cls == '8-A' or s.cls == '8-B' or s.cls == '8-C':
                                                return
                                        elif s.cls == '9-A' or s.cls == '9-B' or s.cls == '9-C' or s.cls == '10-A' or s.cls == '10-B' or s.cls == '10-C':
                                                return
                                        elif s.cls == '11-A' or s.cls == '11-B' or s.cls == '11-C' or s.cls == '12-A' or s.cls == '12-B' or s.cls == '12-C':
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID CLASS##")
                                                print(100 * '-')
                                                c=classs()
                                classs()
                                print("ENTER DOB")
                                def dob():
                                        date=""
                                        month=""
                                        year=""
                                        def monthh():
                                                global month
                                                month=int(input("           ENTER MONTH (MM) : "))
                                                if month <= 12:
                                                        month = str(month)
                                                        month = month.upper()
                                                        return
                                                else:
                                                        print(100 * '-')
                                                        print("##ENTER A VALID MONTH##")
                                                        print(100 * '-')
                                                        c=monthh()
                                        monthh()
                                        def datee():
                                                global date
                                                date=int(input("           ENTER DATE (DD) : "))
                                                if date <= 31:
                                                        date = str(date)
                                                        date = date.upper()
                                                        return
                                                else:
                                                        print(100 * '-')
                                                        print("##ENTER A VALID DATE##")
                                                        print(100 * '-')
                                                        c=datee()
                                        datee()
                                        def yearr():
                                                global year
                                                year=int(input("           ENTER YEAR (YYYY) : "))
                                                if year <= 2022 and year >=1963:
                                                        year=str(year)
                                                        year=year.upper()
                                                        return
                                                else:
                                                        print(100 * '-')
                                                        print("##ENTER A VALID YEAR##")
                                                        print(100 * '-')
                                                        c=yearr()
                                        yearr()
                                dob()
                                def add_all():
                                        s.dob = month + '.' + date + '.' + year
                                        return
                                add_all()
                                def gender():
                                        s.gender = input("ENTER GENDER : ")
                                        s.gender = s.gender.upper()
                                        if s.gender == 'MALE':
                                                return
                                        elif s.gender == 'FEMALE':
                                                return
                                        elif s.gender == 'OTHERS':
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID GENDER##")
                                                print(100 * '-')
                                                c=gender()
                                gender()
                                s.fname = input("ENTER FATHER NAME : ")
                                s.fname = s.fname.upper()
                                s.mname = input("ENTER MOTHER NAME : ")
                                s.mname = s.mname.upper()
                                def phonenumber():
                                        s.phone=int(input("ENTER PHONE NUMBER (XXXXXXXXXX) : "))
                                        b=str(s.phone)
                                        if len(b)==10:
                                                return
                                        else :
                                                print(100 * '-')
                                                print("##ENTER A VALID PHONE NUMBER##")
                                                print(100 * '-')
                                                c=phonenumber()
                                phonenumber()
                                def aadhaarnumber():
                                        s.aadhaar=int(input("ENTER AADHAAR NUMBER (XXXXXXXXXXXX) : "))
                                        b=str(s.aadhaar)
                                        if len(b)==12:
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID AADHAAR NUMBER##")
                                                print(100 * '-')
                                                c=aadhaarnumber()
                                aadhaarnumber()
                                s.email = input("ENTER EMAIL ADDRESS : ")
                                def streamm():
                                        s.stream=input("ENTER STREAM : ")
                                        s.stream=s.stream.upper()
                                        if s.stream == 'SCIENCE' or s.stream == 'COMMERCE':
                                                return
                                        elif s.stream == 'HINDI' or s.stream == 'SANSKRIT':
                                                return
                                        elif s.stream == 'DEFAULT':
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID STREAM##")
                                                print(100 * '-')
                                                c=streamm()
                                streamm()
                                def percentage():
                                        s.per=int(input("ENTER PERCENTAGE : "))
                                        if s.per <= 100:
                                                s.per = str(s.per)
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID PERCENTAGE##")
                                                print(100 * '-')
                                                c=percentage()
                                percentage()
                                def bloodgroup():
                                        s.bloodgroup = input("ENTER BLOOD GROUP : ")
                                        s.bloodgroup=s.bloodgroup.upper()
                                        if s.bloodgroup == 'A+' or s.bloodgroup == 'A-' or s.bloodgroup == 'B+' or s.bloodgroup == 'B-':
                                                return
                                        elif s.bloodgroup == 'O+' or s.bloodgroup == 'O-' or s.bloodgroup == 'AB+' or s.bloodgroup == 'AB-':
                                                return
                                        else:
                                                print(100 * '-')
                                                print("##ENTER A VALID BLOOD GROUP##")
                                                print(100 * '-')
                                                c=bloodgroup()
                                bloodgroup()
                                s.address = input("ENTER ADDRESS : ")
                                s.address=s.address.upper()
                                
                                query1="insert into studentdetails values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')".format(s.roll,s.admnno,s.name,s.cls,s.dob,s.gender,s.fname,s.mname,s.phone,s.aadhaar,s.email,s.stream,s.per,s.bloodgroup,s.address)
                                mycursor.execute(query1)
                                mycon.commit()
                                print("##RECORD ADDED##")
                                
                def display_rec(s):
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        data=mycursor.fetchall()
                        for r in data:
                                print(r[0],'-',r[1],'-',r[2],'-',r[3],'-',r[4],'-',r[5],'-',r[6],'-',r[7],'-',r[8],'-',r[9],'-',r[10],'-',r[11],'-',r[12],'-',r[13],'-',r[14])
                                print(100 * '-')
                                
                def disp_roll_rec(s):
                        n = input("ENTER ROLL NUMBER TO SEARCH RECORD: ")
                        n=n.upper()
                        fn=0
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==n:
                                        print(100 * '-')
                                        print("ROLL NUMBER : ", i[0])
                                        print("ADMISSION NUMBER : ", i[1])
                                        print("STUDENT NAME : ", i[2])
                                        print("CLASS : ", i[3])
                                        print("DATE OF BIRTH (MM/DD/YYYY) : ", i[4])
                                        print("GENDER : ", i[5])
                                        print("FATHER NAME : ", i[6])
                                        print("MOTHER NAME : ", i[7])
                                        print("PHONE NUMBER : ", i[8])
                                        print("AADHAAR NUMBER : ", i[9])
                                        print("EMAIL : ", i[10])
                                        print("STREAM : ", i[11])
                                        print("PERCENTAGE : ", i[12])
                                        print("BLOOD GROUP : ", i[13])
                                        print("ADDRESS : ", i[14])
                                        fn=1
                        if fn==0:
                                print(100 * '=')
                                print("##RECORD DOESN'T EXIST##")
                                
                def disp_name_rec(s):
                        n = input("ENTER NAME TO SEARCH RECORD: ")
                        n=n.upper()
                        fn=0
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[2]==n:
                                        print(100 * '-')
                                        print("ROLL NUMBER : ", i[0])
                                        print("ADMISSION NUMBER : ", i[1])
                                        print("STUDENT NAME : ", i[2])
                                        print("CLASS : ", i[3])
                                        print("DATE OF BIRTH (MM/DD/YYYY) : ", i[4])
                                        print("GENDER : ", i[5])
                                        print("FATHER NAME : ", i[6])
                                        print("MOTHER NAME : ", i[7])
                                        print("PHONE NUMBER : ", i[8])
                                        print("AADHAAR NUMBER : ", i[9])
                                        print("EMAIL : ", i[10])
                                        print("STREAM : ", i[11])
                                        print("PERCENTAGE : ", i[12])
                                        print("BLOOD GROUP : ", i[13])
                                        print("ADDRESS : ", i[14])
                                        fn=1
                        if fn==0:
                                print(100 * '=')
                                print("##RECORD DOESN'T EXIST##")
                        
                def modify_rec(s):
                        a=input("ENTER ROLL NUMBER TO MODIFY RECORD : ")
                        a=a.upper()
                        fn=0
                        q="select * from studentdetails"
                        mycursor.execute(q)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==a:
                                        print(100 * '-')
                                        print("ROLL NUMBER : ", i[0])
                                        print("ADMISSION NUMBER : ", i[1])
                                        print("STUDENT NAME : ", i[2])
                                        print("CLASS : ", i[3])
                                        print("DATE OF BIRTH (MM/DD/YYYY) : ", i[4])
                                        print("GENDER : ", i[5])
                                        print("FATHER NAME : ", i[6])
                                        print("MOTHER NAME : ", i[7])
                                        print("PHONE NUMBER : ", i[8])
                                        print("AADHAAR NUMBER : ", i[9])
                                        print("EMAIL : ", i[10])
                                        print("STREAM : ", i[11])
                                        print("PERCENTAGE : ", i[12])
                                        print("BLOOD GROUP : ", i[13])
                                        print("ADDRESS : ", i[14])
                                        print(100 * '=')
                                        ans='y'
                                        ans=input("DO YOU WANT TO MODIFY THE ABOVE DISPLAYED RECORD? (Y/N) : ")
                                        if ans == 'y':
                                                print(100 * '-')
                                                s.roll = int(input("ENTER ROLL NUMBER : "))
                                                s.roll = str(s.roll)
                                                s.roll = s.roll.upper()
                                                s.admnno = int(input("ENTER ADMISSION NUMBER : "))
                                                s.admnno = str(s.admnno)
                                                s.name = input("ENTER STUDENT NAME : ")
                                                s.name = s.name.upper()
                                                def classs():
                                                        s.cls = input("ENTER CLASS : ")
                                                        s.cls = s.cls.upper()
                                                        if s.cls == '1-A' or s.cls == '1-B' or s.cls == '1-C' or s.cls == '2-A' or s.cls == '2-B' or s.cls == '2-C':
                                                                return
                                                        elif s.cls == '3-A' or s.cls == '3-B' or s.cls == '3-C' or s.cls == '4-A' or s.cls == '4-B' or s.cls == '4-C':
                                                                return
                                                        elif s.cls == '5-A' or s.cls == '5-B' or s.cls == '5-C' or s.cls == '6-A' or s.cls == '6-B' or s.cls == '6-C':
                                                                return
                                                        elif s.cls == '7-A' or s.cls == '7-B' or s.cls == '7-C' or s.cls == '8-A' or s.cls == '8-B' or s.cls == '8-C':
                                                                return
                                                        elif s.cls == '9-A' or s.cls == '9-B' or s.cls == '9-C' or s.cls == '10-A' or s.cls == '10-B' or s.cls == '10-C':
                                                                return
                                                        elif s.cls == '11-A' or s.cls == '11-B' or s.cls == '11-C' or s.cls == '12-A' or s.cls == '12-B' or s.cls == '12-C':
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID CLASS##")
                                                                print(100 * '-')
                                                                c=classs()
                                                classs()
                                                print("ENTER DOB")
                                                def dob():
                                                        date=""
                                                        month=""
                                                        year=""
                                                        def monthh():
                                                                global month
                                                                month=int(input("           ENTER MONTH (MM) : "))
                                                                if month <= 12:
                                                                        month = str(month)
                                                                        month = month.upper()
                                                                        return
                                                                else:
                                                                        print(100 * '-')
                                                                        print("##ENTER A VALID MONTH##")
                                                                        print(100 * '-')
                                                                        c=monthh()
                                                        monthh()
                                                        def datee():
                                                                global date
                                                                date=int(input("           ENTER DATE (DD) : "))
                                                                if date <= 31:
                                                                        date = str(date)
                                                                        date = date.upper()
                                                                        return
                                                                else:
                                                                        print(100 * '-')
                                                                        print("##ENTER A VALID DATE##")
                                                                        print(100 * '-')
                                                                        c=datee()
                                                        datee()
                                                        def yearr():
                                                                global year
                                                                year=int(input("           ENTER YEAR (YYYY) : "))
                                                                if year <= 2022 and year >=1963:
                                                                        year=str(year)
                                                                        year=year.upper()
                                                                        return
                                                                else:
                                                                        print(100 * '-')
                                                                        print("##ENTER A VALID YEAR##")
                                                                        print(100 * '-')
                                                                        c=yearr()
                                                        yearr()
                                                dob()
                                                def add_all():
                                                        s.dob = month + '.' + date + '.' + year
                                                        return
                                                add_all()
                                                def gender():
                                                        s.gender = input("ENTER GENDER : ")
                                                        s.gender = s.gender.upper()
                                                        if s.gender == 'MALE':
                                                                return
                                                        elif s.gender == 'FEMALE':
                                                                return
                                                        elif s.gender == 'OTHERS':
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID GENDER##")
                                                                print(100 * '-')
                                                                c=gender()
                                                gender()
                                                s.fname = input("ENTER FATHER NAME : ")
                                                s.fname = s.fname.upper()
                                                s.mname = input("ENTER MOTHER NAME : ")
                                                s.mname = s.mname.upper()
                                                def phonenumber():
                                                        s.phone=int(input("ENTER PHONE NUMBER (XXXXXXXXXX) : "))
                                                        b=str(s.phone)
                                                        if len(b)==10:
                                                                return
                                                        else :
                                                                print(100 * '-')
                                                                print("##ENTER A VALID PHONE NUMBER##")
                                                                print(100 * '-')
                                                                c=phonenumber()
                                                phonenumber()
                                                def aadhaarnumber():
                                                        s.aadhaar=int(input("ENTER AADHAAR NUMBER (XXXXXXXXXXXX) : "))
                                                        b=str(s.aadhaar)
                                                        if len(b)==12:
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID AADHAAR NUMBER##")
                                                                print(100 * '-')
                                                                c=aadhaarnumber()
                                                aadhaarnumber()
                                                s.email = input("ENTER EMAIL ADDRESS : ")
                                                def streamm():
                                                        s.stream=input("ENTER STREAM : ")
                                                        s.stream=s.stream.upper()
                                                        if s.stream == 'SCIENCE' or s.stream == 'COMMERCE':
                                                                return
                                                        elif s.stream == 'HINDI' or s.stream == 'SANSKRIT':
                                                                return
                                                        elif s.stream == 'DEFAULT':
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID STREAM##")
                                                                print(100 * '-')
                                                                c=streamm()
                                                streamm()
                                                def percentage():
                                                        s.per=int(input("ENTER PERCENTAGE : "))
                                                        if s.per <= 100:
                                                                s.per = str(s.per)
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID PERCENTAGE##")
                                                                print(100 * '-')
                                                                c=percentage()
                                                percentage()
                                                def bloodgroup():
                                                        s.bloodgroup = input("ENTER BLOOD GROUP : ")
                                                        s.bloodgroup=s.bloodgroup.upper()
                                                        if s.bloodgroup == 'A+' or s.bloodgroup == 'A-' or s.bloodgroup == 'B+' or s.bloodgroup == 'B-':
                                                                return
                                                        elif s.bloodgroup == 'O+' or s.bloodgroup == 'O-' or s.bloodgroup == 'AB+' or s.bloodgroup == 'AB-':
                                                                return
                                                        else:
                                                                print(100 * '-')
                                                                print("##ENTER A VALID BLOOD GROUP##")
                                                                print(100 * '-')
                                                                c=bloodgroup()
                                                bloodgroup()
                                                s.address = input("ENTER ADDRESS : ")
                                                s.address=s.address.upper()
                                        
                                                query1="delete from studentdetails where rollno =%s"
                                                us=(a,)
                                                mycursor.execute(query1,us)
                                                mycon.commit()
                                        
                                                query2="insert into studentdetails values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')".format(s.roll,s.admnno,s.name,s.cls,s.dob,s.gender,s.fname,s.mname,s.phone,s.aadhaar,s.email,s.stream,s.per,s.bloodgroup,s.address)
                                                mycursor.execute(query2)
                                                mycon.commit()
                                                fn=1
                                        
                                                print(100 * '=')
                                                print("##RECORD MODIFIED##")
                                        else:
                                                print(100 * '-')
                                                print("##RECORD NOT MODIFIED##")
                                                return
                        if fn==0:
                                print(100 * '=')
                                print("##RECORD DOESN'T EXIST##")

        def write_record():
                try:
                        rec=student()
                        rec.add_rec()
                except:
                        pass

        def display_all():
                try:
                        rec = student()
                        rec.display_rec()
                except :
                        pass

        def search_roll():
                try:
                        rec=student()
                        rec.disp_roll_rec()
                except:
                        pass

        def search_name():
                try:
                        rec=student()
                        rec.disp_name_rec()
                except:
                        pass

        def modify_record():
                try:
                        rec=student()
                        rec.modify_rec()
                except:
                        pass
                
        def delete_roll():
                try:
                        a=input("ENTER ROLL NUMBER TO DELETE RECORD: ")
                        a=a.upper()
                        fn=0
                        q="select * from studentdetails"
                        mycursor.execute(q)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==a:
                                        print("ROLL NUMBER : ", i[0])
                                        print("ADMISSION NUMBER : ", i[1])
                                        print("STUDENT NAME : ", i[2])
                                        print("CLASS : ", i[3])
                                        print("DATE OF BIRTH (MM/DD/YYYY) : ", i[4])
                                        print("GENDER : ", i[5])
                                        print("FATHER NAME : ", i[6])
                                        print("MOTHER NAME : ", i[7])
                                        print("PHONE NUMBER : ", i[8])
                                        print("AADHAAR NUMBER : ", i[9])
                                        print("EMAIL : ", i[10])
                                        print("STREAM : ", i[11])
                                        print("PERCENTAGE : ", i[12])
                                        print("BLOOD GROUP : ", i[13])
                                        print("ADDRESS : ", i[14])
                                        print(100 * '=')
                                        ans='y'
                                        ans=input("DO YOU WANT TO DELETE THE ABOVE DISPLAYED RECORD? (Y/N) : ")
                                        if ans == 'y':
                                                query="delete from studentdetails where rollno =%s"
                                                us=(a,)
                                                mycursor.execute(query,us)
                                                mycon.commit()
                                                fn=1
                                                print(100 * '=')
                                                print("##RECORD DELETED##")
                                        else :
                                                print(100 * '-')
                                                print("##RECORD NOT DELETED##")
                                                return
                        if fn==0:
                                print(100 * '=')
                                print("##RECORD DOESN'T EXIST##")
                except:
                        pass

        def customised_search():
                def s_name_order():
                        alphabet = input('ENTER "ALPHABET" TO CLASSIFY AND DISPLAY STUDENT NAMES FROM STUDENT RECORDS : ')
                        alphabet = alphabet.upper()
                        print(100 * '=')

                        while True:
                                if alphabet == 'A':
                                        query = "select * from studentdetails where studentname like 'A%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'B':
                                        query = "select * from studentdetails where studentname like 'B%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'C':
                                        query = "select * from studentdetails where studentname like 'C%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'D' :
                                        query = "select * from studentdetails where studentname like 'D%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'E' :
                                        query = "select * from studentdetails where studentname like 'E%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'F' :
                                        query = "select * from studentdetails where studentname like 'F%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'G' :
                                        query = "select * from studentdetails where studentname like 'G%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'H' :
                                        query = "select * from studentdetails where studentname like 'H%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'I':
                                        query = "select * from studentdetails where studentname like 'I%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'J':
                                        query = "select * from studentdetails where studentname like 'J%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'K':
                                        query = "select * from studentdetails where studentname like 'K%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'L':
                                        query = "select * from studentdetails where studentname like 'L%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'M':
                                        query = "select * from studentdetails where studentname like 'M%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                return
                                elif alphabet == 'N':
                                        query = "select * from studentdetails where studentname like 'N%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'O':
                                        query = "select * from studentdetails where studentname like 'O%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'P':
                                        query = "select * from studentdetails where studentname like 'P%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'Q':
                                        query = "select * from studentdetails where studentname like 'Q%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'R':
                                        query = "select * from studentdetails where studentname like 'R%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'S':
                                        query = "select * from studentdetails where studentname like 'S%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'T':
                                        query = "select * from studentdetails where studentname like 'T%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'U':
                                        query = "select * from studentdetails where studentname like 'U%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'V':
                                        query = "select * from studentdetails where studentname like 'V%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'W':
                                        query = "select * from studentdetails where studentname like 'W%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'X':
                                        query = "select * from studentdetails where studentname like 'X%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'Y':
                                        query = "select * from studentdetails where studentname like 'Y%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif alphabet == 'Z':
                                        query = "select * from studentdetails where studentname like 'Z%'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID ALPHABET" TO CLASSIFY AND DISPLAY STUDENT NAMES FROM STUDENT RECORDS##')
                                        return

                def class_order():
                        cls = input('ENTER "CLASS" TO CLASSIFY AND DISPLAY RECORDS FROM STUDENT RECORDS : ')
                        cls = cls.upper()
                        print(100 * '=')

                        while True :
                                if '1-A' == cls:
                                        query = "select * from studentdetails where class = '1-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '1-B' == cls:
                                        query = "select * from studentdetails where class = '1-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '1-C' == cls:
                                        query = "select * from studentdetails where class = '1-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '2-A' == cls:
                                        query = "select * from studentdetails where class = '2-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '2-B' == cls:
                                        query = "select * from studentdetails where class = '2-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '2-C' == cls:
                                        query = "select * from studentdetails where class = '2-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '3-A' == cls:
                                        query = "select * from studentdetails where class = '3-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '3-B' == cls:
                                        query = "select * from studentdetails where class = '3-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '3-C' == cls:
                                        query = "select * from studentdetails where class = '3-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '4-A' == cls:
                                        query = "select * from studentdetails where class = '4-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '4-B' == cls:
                                        query = "select * from studentdetails where class = '4-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                return
                                elif '4-C' == cls:
                                        query = "select * from studentdetails where class = '4-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '5-A' == cls:
                                        query = "select * from studentdetails where class = '5-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                return
                                elif '5-B' == cls:
                                        query = "select * from studentdetails where class = '5-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '5-C' == cls:
                                        query = "select * from studentdetails where class = '5-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '6-A' == cls:
                                        query = "select * from studentdetails where class = '6-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '6-B' == cls:
                                        query = "select * from studentdetails where class = '6-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '6-C' == cls:
                                        query = "select * from studentdetails where class = '6-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '7-A' == cls:
                                        query = "select * from studentdetails where class = '7-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '7-B' == cls:
                                        query = "select * from studentdetails where class = '7-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '7-C' == cls:
                                        query = "select * from studentdetails where class = '7-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '8-A' == cls:
                                        query = "select * from studentdetails where class = '8-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '8-B' == cls:
                                        query = "select * from studentdetails where class = '8-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '8-C' == cls:
                                        query = "select * from studentdetails where class = '8-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '9-A' == cls:
                                        query = "select * from studentdetails where class = '9-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '9-B' == cls:
                                        query = "select * from studentdetails where class = '9-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '9-C' == cls:
                                        query = "select * from studentdetails where class = '9-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '10-A' == cls:
                                        query = "select * from studentdetails where class = '10-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '10-B' == cls:
                                        query = "select * from studentdetails where class = '10-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '10-C' == cls:
                                        query = "select * from studentdetails where class = '10-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '11-A' == cls:
                                        query = "select * from studentdetails where class = '11-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '11-B' == cls:
                                        query = "select * from studentdetails where class = '11-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '11-C' == cls:
                                        query = "select * from studentdetails where class = '11-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '12-A' == cls:
                                        query = "select * from studentdetails where class = '12-A'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '12-B' == cls:
                                        query = "select * from studentdetails where class = '12-B'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif '12-C' == cls:
                                        query = "select * from studentdetails where class = '12-C'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID CLASS" TO CLASSIFY AND DISPLAY RECORDS FROM STUDENT RECORDS##')
                                        return

                def gender_viewer():
                        gender = input('ENTER "GENDER" TO CLASSIFY AND DISPLAY RECORDS FROM STUDENT RECORDS : ')
                        gender = gender.upper()
                        print(100 * '=')
                        while True:
                                if gender == 'MALE':
                                        query = "select * from studentdetails where gender = 'MALE'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c = mycursor.rowcount
                                        if c == 0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif gender == 'FEMALE':
                                        query = "select * from studentdetails where gender = 'FEMALE'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c = mycursor.rowcount
                                        if c == 0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif gender == 'OTHERS':
                                        query = "select * from studentdetails where gender = 'OTHERS'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c = mycursor.rowcount
                                        if c == 0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID GENDER" TO CLASSIFY AND DISPLAY RECORDS FROM STUDENT RECORDS##')
                                        return

                def stream_order():
                        stream = input('ENTER "STREAM" TO CLASSIFY AND DISPLAY STREAM RECORDS FROM STUDENT RECORDS : ')
                        stream = stream.upper()
                        print( 100 * '=')

                        while True:
                                if stream == 'SCIENCE':
                                        query = "select * from studentdetails where stream = 'SCIENCE'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif stream == 'COMMERCE':
                                        query = "select * from studentdetails where stream = 'COMMERCE'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif stream == 'HINDI':
                                        query = "select * from studentdetails where stream = 'HINDI'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif stream == 'SANSKRIT':
                                        query = "select * from studentdetails where stream = 'SANSKRIT'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID STREAM" TO CLASSIFY AND DISPLAY STREAM RECORDS FROM STUDENT RECORDS##')
                                        return

                def percentage_order():
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 0 TO 10, PRESS "0"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 11 TO 20, PRESS "1"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 21 TO 30, PRESS "2"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 31 TO 40, PRESS "3"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 41 TO 50, PRESS "4"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 51 TO 60, PRESS "5"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 61 TO 70, PRESS "6"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 71 TO 80, PRESS "7"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 81 TO 90, PRESS "8"')
                        print('TO DISPLAY STUDENTS PERCENTAGE RANGING BETWEEN 91 TO 100, PRESS "9"')
                        print(100 * '-')
                        per = input("ENTER YOUR CHOICE : ")
                        per = per.upper()
                        print(100 * '=')
                        
                        while True:
                                if per == '0':
                                        query = "select * from studentdetails where percentage between 0 and 10"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '1':
                                        query = "select * from studentdetails where percentage between 11 and 20"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '2':
                                        query = "select * from studentdetails where percentage between 21 and 30"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '3':
                                        query = "select * from studentdetails where percentage between 31 and 40"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '4':
                                        query = "select * from studentdetails where percentage between 41 and 50"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '5':
                                        query = "select * from studentdetails where percentage between 51 and 60"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '6':
                                        query = "select * from studentdetails where percentage between 61 and 70"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '7':
                                        query = "select * from studentdetails where percentage between 71 and 80"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '8':
                                        query = "select * from studentdetails where percentage between 81 and 90"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif per == '9':
                                        query = "select * from studentdetails where percentage between 91 and 100"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID RANGE" TO CLASSIFY AND DISPLAY STUDENT PERCENTAGE FROM STUDENT RECORDS##')
                                        return

                def blood_group():
                        bg = input('ENTER "BLOOD GROUP" TO CLASSIFY AND DISPLAY STUDENT BLOOD GROUP FROM STUDENT RECORDS : ')
                        bg = bg.upper()
                        print( 100 * '=')

                        while True:
                                if bg == 'A+':
                                        query = "select * from studentdetails where bloodgroup = 'A+'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'A-':
                                        query = "select * from studentdetails where bloodgroup = 'A-'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'B+':
                                        query = "select * from studentdetails where bloodgroup = 'B+'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'B-':
                                        query = "select * from studentdetails where bloodgroup = 'B-'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'O+':
                                        query = "select * from studentdetails where bloodgroup = 'O+'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'O-':
                                        query = "select * from studentdetails where bloodgroup = 'O-'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'AB+':
                                        query = "select * from studentdetails where bloodgroup = 'AB+'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                elif bg == 'AB-':
                                        query = "select * from studentdetails where bloodgroup = 'AB-'"
                                        mycursor.execute(query)
                                        r = mycursor.fetchall()
                                        c= mycursor.rowcount
                                        if c==0:
                                                print("##RECORD DOESN'T EXIST##")
                                                break
                                        else:
                                                print(r)
                                                print(100 * '-')
                                                print("NUMBER OF DISPLAYED RECORDS ARE : ", c)
                                                return
                                else:
                                        print('##ENTER A "VALID BLOOD GROUP" TO CLASSIFY AND DISPLAY STUDENT BLOOD GROUP FROM STUDENT RECORDS##')
                                        return

                print("                                      SCHOOL MANAGEMENT SYSTEM                                      ")
                print( 100 * '=')
                print("                                         CUSTOMISED SEARCH                                          ")
                print("                                        -------------------                                         ")
                print('TO SEARCH STUDENT NAMES IN ALPHABETICAL ORDER, PRESS "A"')
                print('TO SEARCH RECORD BY CLASSIFYING CLASS, PRESS "C"')
                print('TO SEARCH RECORDS BY CLASSIFYING STREAM, PRESS "S"')
                print('TO SEARCH RECORDS BY CLASSIFYING PERCENTAGE OF THE STUDENTS, PRESS "P"')
                print('TO SEARCH RECORDS BY CLASSIFYING BLOOD GROUP OF THE STUDENT, PRESS "B"')
                print(100 * '=')

                a=input("ENTER A VALID OPTION TO CONTINUE CUSTOMISED SEARCH : ")
                print(100 * '-')
                a=a.upper()
                
                if a == 'A':
                        s_name_order()
                elif a == 'C':
                        class_order()
                elif a == 'S':
                        stream_order()
                elif a == 'P':
                        percentage_order()
                elif a == 'B':
                        blood_group()
                else:
                        print("##INVALID CHOICE##")

        while True:
                print(100 * '=')
                print("                                      SCHOOL MANAGEMENT SYSTEM                                      ")
                print(100 * '=')
                print("                                             MAIN MENU                                              ")
                print("                                            -----------                                             ")
                print("                                           1. ADD RECORD                                            ")
                print("                                       2. DISPLAY ALL RECORDS                                       ")
                print("                                      3. SEARCH BY ROLL NUMBER                                      ")
                print("                                         4. SEARCH BY NAME                                          ")
                print("                                  5. MODIFY RECORD BY ROLL NUMBER                                   ")
                print("                                  6. DELETE RECORD BY ROLL NUMBER                                   ")
                print("                                        7. CUSTOMISED SEARCH                                        ")
                print("                                              8. EXIT                                               ")
                print(100 * "=")
                ch = input("ENTER YOUR CHOICE : ")
                print(100 * "=")
                if ch == '1':
                        write_record()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '2':
                        display_all()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '3':
                        search_roll()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '4':
                        search_name()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '5':
                        modify_record()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '6':
                        delete_roll()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '7':
                        customised_search()
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")
                elif ch == '8':
                        print(45 * " ", "THE END", 46 * " ")
                        print(100 * "=")
                        break
                else:
                        print("##INVALID CHOICE##")
                        print(100 * '=')
                        input("PRESS ANY KEY TO CONTINUE.... ")

def runentireprogram():
        while True:

                print(100 * '=')
                print("                                      SCHOOL MANAGEMENT SYSTEM                                      ")
                print(100 * '=')
                
                talk("do you want to proceed by voice command or by entering details manually")
                print('FOR "VOICE COMMAND", PRESS 1                                                                        ')
                talk("for voice command, press 1")
                print(100 * '-')
                print('FOR "ENTERING DETAILS MANUALLY", PRESS 2                                                            ')
                talk("for entering details manually, press 2")
                print(100 * '=')
                
                programdefiner=input('ENTER 1 FOR "VOICE COMMAND" AND 2 TO "ENTERING DETAILS MANUALLY" : ')
                if programdefiner=='1':
                        print(100 * "=")
                        print("VOICE COMMAND ACTIVATED")
                        talk("voice command activated")
                        voice_command()
                        return
                elif programdefiner=='2':
                        print(100 * '=')
                        print("ENTERING DETAILS MANUALLY ACTIVATED")
                        enter_details_manually()
                        return
                else :
                        print(100 * '=')
                        print("##INVALID CHOICE##")

runentireprogram()
