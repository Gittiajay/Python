from HP_modul import Doctors,Staff
import HP_databas as Hdb
choice = 0          #name=None,spec=None,duty=0,salary=0
while (choice!=5):
    print('1.  Add New Doctor ')
    print('10  Add New Staff')
    print('2   Show Doctor list ')
    print('20  Show Staff list ')
    print('3   Delete Doctor ')
    print('30  Delete Staff ')
    print('4   Update Doctor ')
    print('40  Update Staff ')
    print('5   Exit ')

    choice = int(input('Enter your Doctor_opr and Staff_opr Choice: '))
    #choice= float(input("Enter you Staff_opr Choice"))

    if choice==1:
        Name=input("Enter Doctor  name:")
        Special=input("Enter Doctor specialization: ")
        Duty=int(input("Enter Doctor duty timing: "))
        Salary=float(input("Enter Doctor Salary: "))

        DR=Doctors(name=Name,spec=Special,duty=Duty,salary=Salary)
        Hdb.save_Drs(DR)
        print("Doctor added successfully",end='\n\n')

    elif choice== 10:
        Name_S=input("Enter Staff name: ")
        Duty_S=int(input("Enter Staff Duty: "))
        Salary_S=int(input("Enter Staff Salary: "))
        Job_Roll=input("Enter Job roll of staff: ")
        ST=Staff(name=Name_S,duty=Duty_S,salary=Salary_S, Job_roll=Job_Roll)
        Hdb.save_Stf(ST)
        print("Staff Added successfully")

    elif choice==2:  # here i am facing problem
        # Doclist = Hdb.get_Dr_list()
        # for doc in Doclist:
        #     print(doc)
        # else:
        #     print("__" * 15)
        Doclist = Hdb.get_Dr_list()
        print(17 * '-', 'Doctors  List', 17 * '-')
        for emp in Doclist:
            print(emp)
            print('-' * 35)
        else:
            print()

    elif choice==20:
        STFlist=Hdb.get_Stf_lst()
        print(17 * '-', 'Staff list ', 17 * '-')
        for St in STFlist:
            print(St)

        else:
            print()


    elif choice==3:
        id=int(input("Enter delete doctor Id: "))
        Hdb.Delete_Dr(id)

    elif choice==30:
        id_s=int(input("Enter Delete staff id: "))
        Hdb.Delete_stf(id_s)

    elif choice==4:
        Id=int(input("Enter id for update doctors: "))
        Name=input("Enter updated Doctor name: ")
        Spec=input("Enter updated specalization of Doctor:  ")
        Duty=int(input("Enter updated Duty: "))
        Salary=float(input("Enter updated salary: "))
        dr=Doctors(id=Id, name=Name, spec=Spec, duty=Duty, salary=Salary)
        Hdb.Update_Dr(Id,dr)

    elif choice==40:
        Id_S=int(input("Enter id for update Staffs: "))
        name_S= input("Enter update staff: ")
        duty_S= int(input("Enter updated Duty: "))
        salary_S=int(input("Enter Upadted salary: "))
        job_Roll = input("Enter updated job roll: ")
        stf=Staff(id=Id_S, name=name_S, duty=duty_S, salary=salary_S,Job_roll=job_Roll)
        Hdb.Update_stf(Id_S,stf)