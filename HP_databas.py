from HP_modul import Doctors,Staff
import pymysql
con=pymysql.connect(host='localhost',user='root',passwd='', db='hopital_manegment')
print("connection successful")

cursor1=con.cursor()

print("_"*5,"welcome to Hospital managment system","_"*10)

def save_Drs(dr):
    try:
        sqlquary = 'insert into doctors(name,spec,duty,salary) values(%s,%s,%s,%s)'
        cursor1.execute(sqlquary,(dr.D_name,dr.D_specail,dr.D_duty,dr.D_salary))
        con.commit()
    except Exception as e:
        print("__"*20,"error",e,"__"*20)

def save_Stf(st):
    try:
        sqlquaeryS= 'insert into staff(name,duty,salary,Job_Roll) values (%s,%s,%s,%s)'
        cursor1.execute(sqlquaeryS,(st.S_name, st.S_duty, st.S_salary,st.S_job))
        con.commit()
    except Exception as e:
        print("__" * 20, "error", e, "__" * 20)


def get_Dr_list():
    Dr_list = []
    try:
        sqlquery = " select * from doctors  "
        cursor1.execute(sqlquery)
        rows = cursor1.fetchall()
        con.commit()
        for row in rows:
            # here we ceating object each row of table
            All_Dr = Doctors(row[0],row[1], row[2], row[3], row[4])
            Dr_list.append(All_Dr)
        else:
            return Dr_list
    except Exception as e:
        print("_" * 5, "Error", "_" * 10)
        print(e)

def get_Dr_byId(id):
    try:
        sqlquery='select * from doctors where id=%s'
        cursor1.execute(sqlquery,(id))
        row=cursor1.fetchone()
        Doc=Doctors(row[0],row[1],row[2],row[3],row[4])
        con.commit()
        return Doc
    except  Exception as e:
        print("__"*20,"Error","__"*20)
        print(e)




# def shot():
#     dr_list=[]
#     sqlquery='select * from doctors '
#     cursor1.execute(sqlquery)
#     rows =cursor1.fetchall
#     con.commit()
#     for row in rows:
#         all_dr=Doctors(row[0],row[1], row[2], row[3], row[4])
#         dr_list.append(all_dr)
#     else:
#         return dr_list

def search_name(query):
    D_list=[]
    sqlquery = ' select * from doctors where id=%s or name=%s'
    cursor1.execute(sqlquery,(query,query))
    rows = cursor1.fetchall()
    con.commit()
    for row in rows:
        # here we ceating object each row of table
        All_Dr = Doctors(row[0], row[1], row[2], row[3], row[4])
        D_list.append(All_Dr)
    else:
        return D_list

def get_Stf_lst():
    try:
        Staff_list=[]
        sqlqueryS= 'select * from staff'
        cursor1.execute(sqlqueryS)
        rows1=cursor1.fetchall()
        con.commit()
        for row in rows1:
            All_stf= Staff(row[0],row[1],row[2],row[3],row[4])
            Staff_list.append(All_stf)
        else:
            return Staff_list
    except Exception as e:
             print("_" * 5, "Error", "_" * 10)
             print(e)


def Delete_Dr(id):
    try:
        sqlquery='delete from doctors where id=%s'
        cursor1.execute(sqlquery, (id))
        print("doctor deleted successfully")
        con.commit()
    except Exception as e:
         print("__" * 20, "error", e, "__" * 20)

def Delete_stf(id):
    try:
        sqlquerys= 'delete from staff where id=%s'
        cursor1.execute(sqlquerys,(id))
        con.commit()
        print("Staff Deleted successfully")
    except  Exception as e:
        print("__"*20,"Error",e,"__"*20,)


def Update_Dr(id,dr):   #self.D_id,{self.D_name},{self.D_specail},{self.D_duty},{self.D_salary
    try:
        sqlquery= 'Update doctors set name=%s , spec=%s ,duty=%s ,salary=%s  where id=%s'
        cursor1.execute(sqlquery,(dr.D_name, dr.D_specail, dr.D_duty, dr.D_salary,id))
        con.commit()
        print("Doctor Updated successfully")
    except  Exception as e:
        print("__"*20,"Error","__"*20)
        print(e)
def Update_stf(id,st):
    try:
        sqlqueryS='Update staff set name=%s,duty=%s,salary=%s , Job_Roll=%s where id=%s'
        cursor1.execute(sqlqueryS,(st.S_name, st.S_duty, st.S_salary, st.S_job, id ))
        con.commit()
        print("Staff updated successfully")
    except Exception as e:
        print("__" * 20, "Error", "__" * 20)
        print(e)







