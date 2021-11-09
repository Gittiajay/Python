from flask import Flask ,render_template,redirect,request,url_for
import HP_databas as Hdb
from  HP_modul import Doctors
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("/Home.html")

@app.route('/Doctor_List')
def Show_doctors():
    Dr_list=Hdb.get_Dr_list()
    return render_template("/Doctor_lst.html",Dr_list=Dr_list)





@app.route('/savebook',methods=["POST"])
def savedr():
    D_name=request.form['Doctor name']
    D_specail=request.form['DoctorSc']
    D_duty=request.form['Doctor duty']
    D_salary=request.form['Doctor Salary']
    doc=Doctors(name=D_name,spec=D_specail,duty=D_duty,salary=D_salary)
    Hdb.save_Drs(doc)
    return redirect(url_for('Show_doctors'))


@app.route('/updatedoctor',methods=["POST"])
def method_dr():
   D_id=request.form['DoctorId']
   D_name = request.form['Doctor name']
   D_specail=request.form['DoctorSc']
   D_duty = request.form['Doctor duty']
   D_salary=request.form['Doctor Salary']
   dr=Doctors(D_id,D_name ,D_specail,D_duty,D_salary)
   Hdb.Update_Dr(D_id,dr)
   return redirect(url_for('Show_doctors'))


@app.route('/delete_dr/<int:D_id>')
def Delete_dr(D_id):
    Delete=Hdb.Delete_Dr(D_id)
    return redirect('/Doctor_List')

@app.route('/Add_Doctor')
def addoc():
     Drs=Doctors()
     return render_template("/Add_Doctor.html",Drs=Drs,action='Add')

@app.route('/Edit_rd/<int:D_id>')
def Edit_rd(D_id):
    Drs=Hdb.get_Dr_byId(D_id)
    return render_template('Add_Doctor.html',Drs=Drs,action='Edit')

@app.route('/searcdrs',methods=["POST"])
def searcdrs():
     quary=request.args.get('search_name')
     drlist=Hdb.search_name(quary)
     # doclist = Hdb.get_Dr_list()
     #Doclist= list(filter(lambda Doc: str(Doc.D_id)==quary or Doc.D_name.startswith(quary), drlist) )
     return render_template('Doctor_lst.html',drlist=drlist)



# @app.route('/Add_Doctor/<int:D_id>')
# def edit_doc(D_id):
#     Edit=Hdb.Update_Dr(D_id)
#     return render_template('Add_Doctor.html',Edit=Edit)
# @app.route('/updatedr')
# def edit_dr():
#     D_id=request.form["drid"]
#     D_name=request.form["drname"]
#     # D_specail  = request.form["drid"]
#     # D_duty = request.form["drid"]
#     # D_salary = request.form["drid"]
#     dr = Doctors (D_id,D_name)
#     Hdb.Update_Dr(id,dr)
#     return redirect(url_for('Doctor_List'))

if __name__=='__main__':
    app.run(debug=True)