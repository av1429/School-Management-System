import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',passwd='Av@2910200fouR',database='sms')
mycursor=mycon.cursor()

def enter_details_manually():
        class student(object):
                def __int__(s):
                        s.roll = ""
                        s.admnno = 0
                        s.name = ""
                        s.cls = ""
                        s.dob = ""
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
                        s.roll = input("Enter Roll Number : ")
                        s.roll = s.roll.upper()
                        s.admnno = int(input("Enter Admission Number : "))
                        s.admnno = str(s.admnno)
                        s.name = input("Enter Name : ")
                        s.name = s.name.upper()
                        s.cls = input("Enter Class : ")
                        s.cls = s.cls.upper()
                        s.dob = input("Enter Date Of Birth (DD-MM-YYYY) : ")
                        s.dob = s.dob.upper()
                        s.fname = input("Enter Father Name : ")
                        s.fname = s.fname.upper()
                        s.mname = input("Enter Mother Name : ")
                        s.mname = s.mname.upper()
                        def phonenumber():
                                s.phone=int(input("enter phone number : "))
                                b=str(s.phone)
                                if len(b)==10:
                                        return

                                else :
                                        print(50 * '-')
                                        print("enter a valid phone number")
                                        print(50 * '-')
                                        c=phonenumber()
                        phonenumber()

                        def aadhaarnumber():
                                s.aadhaar=int(input("enter aadhaar number : "))
                                b=str(s.aadhaar)
                                if len(b)==12:
                                        return
                        
                                else:
                                        print(50 * '-')
                                        print("enter a valid aadhaar number")
                                        print(50 * '-')
                                        c=aadhaarnumber()
                        aadhaarnumber()
                        s.email = input("Enter Email Address : ")
                        s.stream=input("enter stream : ")
                        s.stream=s.stream.upper()
                        s.per=int(input("enter percentage : "))
                        s.per = str(s.per)
                        s.bloodgroup = input("Enter Blood Group : ")
                        s.bloodgroup=s.bloodgroup.upper()
                        s.address = input("Enter Address : ")
                        s.address=s.address.upper()
                        query="insert into studentdetails values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(s.roll,s.admnno,s.name,s.cls,s.dob,s.fname,s.mname,s.phone,s.aadhaar,s.email,s.stream,s.per,s.bloodgroup,s.address)
                        mycursor.execute(query)
                        mycon.commit()

                def display_rec(s):
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        data=mycursor.fetchall()
                        for row in data:
                                print(row)
        
                def disp_roll_rec(s):
                        n = input("Enter roll no search : ")
                        n=n.upper()
                        fn=0
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==n:
                                        print("Roll Number : ", i[0])
                                        print("Admission Number : ", i[1])
                                        print("Student Name : ", i[2])
                                        print("Class : ", i[3])
                                        print("Date of Birth : ", i[4])
                                        print("Father Name : ", i[5])
                                        print("Mother Name : ", i[6])
                                        print("Phone Number : ", i[7])
                                        print("Aadhaar Number : ", i[8])
                                        print("Email : ", i[9])
                                        print("Stream : ", i[10])
                                        print("Percentage : ", i[11])
                                        print("Blood Group : ", i[12])
                                        print("Address : ", i[13])
                                        fn=1
                        if fn==0:
                                print("##Record doesn't exist##")

                def disp_name_rec(s):
                        n = input("Enter Name to search : ")
                        n=n.upper()
                        fn=0
                        query="select * from studentdetails"
                        mycursor.execute(query)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[2]==n:
                                        print("Roll Number : ", i[0])
                                        print("Admission Number : ", i[1])
                                        print("Student Name : ", i[2])
                                        print("Class : ", i[3])
                                        print("Date of Birth : ", i[4])
                                        print("Father Name : ", i[5])
                                        print("Mother Name : ", i[6])
                                        print("Phone Number : ", i[7])
                                        print("Aadhaar Number : ", i[8])
                                        print("Email : ", i[9])
                                        print("Stream : ", i[10])
                                        print("Percentage : ", i[11])
                                        print("Blood Group : ", i[12])
                                        print("Address : ", i[13])
                                        fn=1
                        if fn==0:
                                print("##Record doesn't exist##")
                        
                def modify_rec(s):
                        a=input("enter roll no to modify record : ")
                        a=a.upper()
                        fn=0
                        q="select * from studentdetails"
                        mycursor.execute(q)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==a:
                                        print("Roll Number : ", i[0])
                                        print("Admission Number : ", i[1])
                                        print("Student Name : ", i[2])
                                        print("Class : ", i[3])
                                        print("Date of Birth : ", i[4])
                                        print("Father Name : ", i[5])
                                        print("Mother Name : ", i[6])
                                        print("Phone Number : ", i[7])
                                        print("Aadhaar Number : ", i[8])
                                        print("Email : ", i[9])
                                        print("Stream : ", i[10])
                                        print("Percentage : ", i[11])
                                        print("Blood Group : ", i[12])
                                        print("Address : ", i[13])

                                        print(50 * '=')

                                        s.roll = input("Enter Roll Number : ")
                                        s.roll = s.roll.upper()
                                        s.admnno = int(input("Enter Admission Number : "))
                                        s.admnno = str(s.admnno)
                                        s.name = input("Enter Name : ")
                                        s.name = s.name.upper()
                                        s.cls = input("Enter Class : ")
                                        s.cls = s.cls.upper()
                                        s.dob = input("Enter Date Of Birth (DD-MM-YYYY) : ")
                                        s.dob = s.dob.upper()
                                        s.fname = input("Enter Father Name : ")
                                        s.fname = s.fname.upper()
                                        s.mname = input("Enter Mother Name : ")
                                        s.mname = s.mname.upper()
                                        def phonenumber():
                                                s.phone=int(input("enter phone number : "))
                                                b=str(s.phone)
                                                if len(b)==10:
                                                        return

                                                else :
                                                        print(50 * '-')
                                                        print("enter a valid phone number")
                                                        print(50 * '-')
                                                        c=phonenumber()
                                        phonenumber()

                                        def aadhaarnumber():
                                                s.aadhaar=int(input("enter aadhaar number : "))
                                                b=str(s.aadhaar)
                                                if len(b)==12:
                                                        return
                                        
                                                else:
                                                        print(50 * '-')
                                                        print("enter a valid aadhaar number")
                                                        print(50 * '-')
                                                        c=aadhaarnumber()
                                        aadhaarnumber()
                                        s.email = input("Enter Email Address : ")
                                        s.stream=input("enter stream : ")
                                        s.stream=s.stream.upper()
                                        s.per=int(input("enter percentage : "))
                                        s.per = str(s.per)
                                        s.bloodgroup = input("Enter Blood Group : ")
                                        s.bloodgroup=s.bloodgroup.upper()
                                        s.address = input("Enter Address : ")
                                        s.address=s.address.upper()
                                        query1="delete from studentdetails where rollno =%s"
                                        us=(a,)
                                        mycursor.execute(query1,us)
                                        mycon.commit()
                                        
                                        
                                        query2="insert into studentdetails values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(s.roll,s.admnno,s.name,s.cls,s.dob,s.fname,s.mname,s.phone,s.aadhaar,s.email,s.stream,s.per,s.bloodgroup,s.address)
                                        mycursor.execute(query2)
                                        mycon.commit()
                                        fn=1
                                        print("##record modified##")
                        if fn==0:
                                print("##record doesn't exist##")

        def write_record():
                try:
                        rec=student()
                        rec.add_rec()
                        print(50*'=')
                        print("##record added in file##")
                        print(50*'=')
                        input("press any key to continue....")
                except:
                        pass

        def display_all():
                try:
                        rec = student()
                        rec.display_rec()
                        print(50 * '=')
                        input("press any key to continue....")
                except :
                        pass

        def search_roll():
                try:
                        rec=student()
                        rec.disp_roll_rec()
                        print(50 * '=')
                        input("press any key to continue....")
                except:
                        pass

        def search_name():
                try:
                        rec=student()
                        rec.disp_name_rec()
                        print(50 * '=')
                        input("press any key to continue....")
                except:
                        pass

        def modify_record():
                try:
                        rec=student()
                        rec.modify_rec()
                        print(50*'=')
                        input("press any key to continue....")
                except:
                        pass
                
        def delete_roll():
                try:
                        a=input("enter roll no to delete : ")
                        a=a.upper()
                        fn=0
                        q="select * from studentdetails"
                        mycursor.execute(q)
                        r=mycursor.fetchall()
                        for i in r:
                                if i[0]==a:
                                        query="delete from studentdetails where rollno =%s"
                                        us=(a,)
                                        mycursor.execute(query,us)
                                        mycon.commit()
                                        fn=1
                                        print("##record deleted##")
                                        print(50 * '=')
                                        input("press any key to continue....")
                        if fn==0:
                                print(50 * '=')
                                print("record doesn't exist")
                                print(50 * '=')
                                input("press any key to continue....")

                except:
                        pass

        while True:
                print(50 * "=")
                print("             SCHOOL MANAGEMENT SYSTEM             ")
                print(50 * "=")
                print("                    MAIN MENU                     ")
                print("                   -----------                    ")
                print("                  1. ADD RECORD                   ")
                print("              2. DISPLAY ALL RECORDS              ")
                print("              3. SEARCH BY ROLL NO.               ")
                print("                4. SEARCH BY NAME                 ")
                print("           5. MODIFY RECORD BY ROLL NO.           ")
                print("           6. DELETE RECORD BY ROLL NO.           ")
                print("                     7. EXIT                      ")
                print(50 * "=")
                ch = input("Enter your choice : ")
                print(50 * "=")
                if ch == '1':
                    write_record()
                elif ch == '2':
                    display_all()
                elif ch == '3':
                    search_roll()
                elif ch == '4':
                    search_name()
                elif ch == '5':
                    modify_record()
                elif ch == '6':
                    delete_roll()
                elif ch == '7':
                    print("End")
                    break
                else:
                    print("Invalid choice")

enter_details_manually()
