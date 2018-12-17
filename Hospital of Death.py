from tkinter import *
from functools import partial
from tkcalendar import Calendar
import pyodbc

# SideNotes:
# 00A288 Green , #FFFF9C Yellow
# patient's image is always 280x280

global admins,room_value, u, patient_store, nurse_store, doctor_store, Patient, Nurses, Patients, Doctors, patientid
admins = [['admin', '123']]


# ---------------------------------
def retrivePatients(docorid):  # Used to show all patients in DoctorSplashScreen
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Patient where Patient.doctor_id=?', docorid)
    u = cursor.fetchall()
    print(u)
def retriveDoc():
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Handsa3.dbo.Doctor')
    u = cursor.fetchall()
    cnxn.commit()
def retriveSP(patientid):
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('select * from Patient where id=1')
    u = cursor.fetchall()
    patientid = u[0][0]

    cursor.execute('select code from Room where Room.id=?', patientid)
    x = cursor.fetchall()
    u.append(x)
    cnxn.commit()

# Nurse
def Nurse2(patientid):
    global Nurse, diag, side
    Nurse = Toplevel(screen)
    Nurse.configure(background="#00A288")
    Nurse.geometry("1440x810")
    bg = Label(master=Nurse, background="#FFFF9C")
    bg.place(relx=0.0, rely=0.25, relwidth=1, relheight=1)

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('select * from Patient where id=?', patientid)
    u = cursor.fetchall()
    cursor.execute('select code from Room where Room.id=?', u[0][14])
    x = cursor.fetchall()
    cnxn.commit()

    #
    # photo2=PhotoImage(file=Patient[patientid][4])
    # img=Label(master=Nurse,borderwidth=0,image=photo2,background="#00A288")
    # img.photo=photo2
    # img.place(relx=0.75,rely=0.12)


    title2 = Label(master=Nurse, text="Name: " + u[0][1], font=("Ariel", "40", "bold"), background="#00A288",
                   foreground="#FFFF9C")
    title2.place(relx=0.05, rely=0.07)
    age = Label(master=Nurse, text=("Age: %d" % u[0][4]), font=("Ariel", "10", ""), background="#00A288",
                foreground="#FFFF9C")
    age.place(relx=0.052, rely=0.22)
    disease = Label(master=Nurse, text="Disease: " + u[0][7], font=("Ariel", "10", ""), background="#00A288",
                    foreground="#FFFF9C")
    disease.place(relx=0.2, rely=0.22)
    room = Label(master=Nurse, text="Room: " + x[0][0], font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")
    room.place(relx=0.394, rely=0.22)

    diagnose = Label(master=Nurse, text="Diagnoses:", background="#FFFF9C", foreground="#00A288",
                     font=("Ariel", "16", ""))
    diagnose.place(relx=0.05, rely=0.258)
    lbl = Label(master=Nurse, background="#00A288")
    lbl.place(relx=0.0538, rely=0.30, relwidth=0.52, relheight=0.22)
    diag = Label(master=Nurse, text=u[0][15], font=("Ariel", "12", "bold"), background="#00A288", foreground="#FFFF9C")
    diag.place(relx=0.0598, rely=0.31)

    sidenote = Label(master=Nurse, text="Side Notes:", background="#FFFF9C", foreground="#00A288",
                     font=("Ariel", "16", ""))
    sidenote.place(relx=0.05, rely=0.57)
    lbl = Label(master=Nurse, background="#00A288")
    lbl.place(relx=0.0538, rely=0.62, relwidth=0.52, relheight=0.22)
    side = Label(master=Nurse, text=u[0][16], font=("Ariel", "12", "bold"), background="#00A288", foreground="#FFFF9C")
    side.place(relx=0.0598, rely=0.63)

    # fnc=partial(close,Nurse)
    btn = Button(master=Nurse, text="Exit", font=(" ", " 14 ", "bold"), command=Nurse.destroy, relief=FLAT,
                 activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
    btn.place(rely=0.92, relx=0.44)
def NurseSplashScreen(Nurseid):
    global Nurse, diag, side
    dsc = Toplevel(screen)
    dsc.configure(background="#00A288")
    dsc.geometry("500x300")
    login.destroy()
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute(
        'SELECT * FROM Patient JOIN Nurses_WardBoys ON (Nurses_WardBoys.room_id = patient.room_id) WHERE Nurses_WardBoys.id=?;',
        Nurseid)
    u = cursor.fetchall()
    cnxn.commit()

    welcomemsg = "Please select one of your patients "
    msg = Label(dsc, text=welcomemsg, font=("Ariel", "10", "bold"), background="#00A288", foreground="#FFFF9C")
    msg.place(relx=0.08, rely=0.05, relwidth=0.84, relheight=0.1)
    bgn = Label(dsc, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    o = ((1 - 0.24) / len(u)) / 1
    for i in range(len(u)):
        gooo = partial(Nurse2, u[i][0])
        btn = Button(master=dsc, text=u[i][1], font=(" ", " 10 ", "bold"), command=gooo, relief=FLAT,
                     activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
        btn.place(rely=0.24 + o * i, relx=0.34)

# Patient
def PatientSplashScreen(patientid):
    patients = Toplevel(screen)
    patients.configure(background="#00A288")
    patients.geometry("1440x810")
    # Kareem Ibrahim Allam','22',"ElGomla Station. Gamal Abdel-Nasser St." ,'Heart Cancer', '401',"patient.gif","Ahmed Hamouda","300 L.E","18. 4. 2014
    login.destroy()
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('select * from Patient where id=?', patientid)
    u = cursor.fetchall()
    cursor.execute('select code from Room where Room.id=?', u[0][14])
    x = cursor.fetchall()
    cursor.execute('select name from Doctor where id=?', u[0][13])
    z = cursor.fetchall()
    u[0][13] = z[0][0]
    cnxn.commit()

    msg = Label(patients, text=u[0][1] + "'s Document", font=("Ariel", "26", "bold"), background="#00A288",
                foreground="#FFFF9C")
    msg.place(relx=0.08, rely=0.055, relwidth=0.84, relheight=0.1)
    bgn = Label(patients, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.6)

    # photo=PhotoImage(file=u[patientid][5])
    # img=Label(master=patients,background="#FFFF9C",image=photo)
    # img.photo=photo
    # img.place(relx=0.1,rely=0.3)

    name = Label(master=patients, text="Name: " + u[0][1], font=("", "12", "bold"), background="#FFFF9C",
                 foreground="#00A288")
    name.place(relx=0.34, rely=0.35)
    age = Label(master=patients, text=("Age: %d" % u[0][4]), font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    age.place(relx=0.34, rely=0.42)
    dis = Label(master=patients, text="Address: " + u[0][6], font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dis.place(relx=0.34, rely=0.49)
    dis = Label(master=patients, text="Room: " + x[0][0], font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dis.place(relx=0.34, rely=0.56)

    dis = Label(master=patients, text="Disease: " + u[0][7], font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dis.place(relx=0.54, rely=0.35)
    name = Label(master=patients, text="Doctor: " + u[0][13], font=("", "12", "bold"), background="#FFFF9C",
                 foreground="#00A288")
    name.place(relx=0.54, rely=0.42)
    age = Label(master=patients, text=("Bill: %d" % u[0][12]), font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    age.place(relx=0.54, rely=0.49)
    dis = Label(master=patients, text="Register Date: " + u[0][10], font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dis.place(relx=0.54, rely=0.56)

    dis = Label(master=patients, text="BLood Type: " + u[0][5], font=("", "12", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dis.place(relx=0.74, rely=0.35)

# Doctor_Screen
def uped(patiendid):
    date = '%s' % cal.selection_get()
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('UPDATE Patient SET exit_date=? WHERE id=?;', date, patiendid)
    cursor.execute('SELECT DATEDIFF(day,entry_date,exit_date)*10 from Patient where id =?', patiendid)
    opp=cursor.fetchall()
    opp=opp[0][0]
    cursor.execute('UPDATE Patient SET bill=? WHERE id=?;', opp, patiendid)
    cnxn.commit()

def lsed(patientid):
    global year, day, month
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('select exit_date from Patient where id = ?', patientid)
    zi = cursor.fetchall()
    print(zi)
    zi = zi[0][0].split('-')
    year = int(zi[0])
    month = int(zi[1])
    day = int(zi[2])
    cnxn.commit()
def editdiagnoses(patientid):
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('UPDATE Patient SET diagnose=? WHERE id=?;', diag.get(1.0, END), patientid)
    cnxn.commit()
def editsidenotes(patientid):
    print(type(patientid))
    print(type(side.get(1.0, END)))
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('UPDATE Patient SET sidenotes=? WHERE id=?;', side.get(1.0, END), patientid)
    cnxn.commit()
def Doctor(patientid):
    global doctor, diag, side, cal, day, year, month, bill
    doctor = Toplevel(screen)
    doctor.configure(background="#00A288")
    doctor.geometry("1440x810")
    bg = Label(master=doctor, background="#FFFF9C")
    bg.place(relx=0.0, rely=0.25, relwidth=1, relheight=1)

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('SELECT DATEDIFF(day,entry_date,exit_date)*10 from Patient where id =?', patientid)
    u = cursor.fetchall()
    bill = u[0][0]
    cursor.execute('SELECT cure_price from Patient where id =?', patientid)
    u = cursor.fetchall()
    bill += u[0][0]
    cursor.execute('select * from Patient where id=?', patientid)
    u = cursor.fetchall()
    cursor.execute('select code from Room where Room.id=?', u[0][14])
    x = cursor.fetchall()
    cnxn.commit()

    # x = txt.get()
    # photo2=PhotoImage(file=Patient[patientid][4])
    # img=Label(master=doctor,borderwidth=0,image=photo2,background="#00A288")
    # img.photo=photo2
    # img.place(relx=0.75,rely=0.12)
    lsed(patientid)

    title2 = Label(master=doctor, text="Name: " + u[0][1], font=("Ariel", "40", "bold"), background="#00A288",
                   foreground="#FFFF9C")
    title2.place(relx=0.05, rely=0.07)
    age = Label(master=doctor, text=("Age: %d" % u[0][4]), font=("Ariel", "10", ""), background="#00A288",
                foreground="#FFFF9C")
    age.place(relx=0.052, rely=0.22)
    disease = Label(master=doctor, text="Disease: " + u[0][7], font=("Ariel", "10", ""), background="#00A288",
                    foreground="#FFFF9C")
    disease.place(relx=0.2, rely=0.22)
    room = Label(master=doctor, text="Room: " + x[0][0], font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")
    room.place(relx=0.394, rely=0.22)

    diagnose = Label(master=doctor, text="Diagnoses:", background="#FFFF9C", foreground="#00A288",
                     font=("Ariel", "16", ""))
    diagnose.place(relx=0.05, rely=0.258)

    diag = Text(master=doctor, font=("Ariel", "8", ""), foreground="#00A288")
    diag.insert(INSERT, u[0][15])
    diag.place(relx=0.0538, rely=0.30, relwidth=0.65, relheight=0.26)
    edddig = partial(editdiagnoses, u[0][0])

    lobtn = Button(master=doctor, text="Update Diagnose", font=(" ", "10 ", "bold"), command=edddig, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", activeforeground="#00A288", foreground="#00A288")
    lobtn.place(relx=0.32, rely=0.54)

    sidenote = Label(master=doctor, text="Side Notes:", background="#FFFF9C", foreground="#00A288",
                     font=("Ariel", "16", ""))
    sidenote.place(relx=0.05, rely=0.57)
    side = Text(master=doctor, font=("Ariel", "8", ""), foreground="#00A288")
    side.insert(INSERT, u[0][16])
    side.place(relx=0.0538, rely=0.61, relwidth=0.65, relheight=0.3)
    edsid = partial(editsidenotes, patientid)
    sideup = Button(doctor, text="Update Side Notes", font=(" ", "10 ", "bold"), command=edsid, relief=FLAT,
                    activebackground="#FFFF9C", background="#FFFF9C", activeforeground="#00A288", foreground="#00A288")
    sideup.place(relx=0.32, rely=0.89)
    btn = Button(master=doctor, text="Exit", font=(" ", " 14 ", ""), command=doctor.destroy, relief=FLAT,
                 activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
    btn.place(rely=0.82, relx=0.84)

    dat = Label(master=doctor, text="Select Exit Date: ", font=(" ", "10 ", "bold"), background="#FFFF9C",
                foreground="#00A288")
    dat.place(relx=0.738, rely=0.60)

    cal = Calendar(master=doctor, width=10, background='#00A288', foreground='#FFFF9C', borderwidth=0, year=year,
                   month=month, day=day)
    cal.place(relx=0.74, rely=0.63)

    Op = partial(uped, patientid)
    exitbtn = Button(master=doctor, text="Update Exit Date", font=(" ", "10 ", "bold"), command=Op, relief=FLAT,
                     activebackground="#FFFF9C", background="#FFFF9C", activeforeground="#00A288", foreground="#00A288")
    exitbtn.place(relx=0.74, rely=0.875)
def DoctorSplashScreen(doctorid):  # Selects 0ne of his patients to view his profile
    global doctor, diag, side, txt2
    login.destroy()
    dsc = Toplevel(screen)
    dsc.configure(background="#00A288")
    dsc.geometry("500x300")

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Patient where Patient.doctor_id=?', doctorid)
    u = cursor.fetchall()
    cnxn.commit()

    welcomemsg = "Please select one of your patients"
    msg = Label(dsc, text=welcomemsg, font=("Ariel", "10", "bold"), background="#00A288", foreground="#FFFF9C")
    msg.place(relx=0.08, rely=0.05, relwidth=0.84, relheight=0.1)
    bgn = Label(dsc, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    o = ((1 - 0.24) / (len(u) + 0.01)) / 1
    for i in range(len(u)):
        gooo = partial(Doctor, u[i][0])
        btn = Button(master=dsc, text=u[i][1], font=(" ", " 10 ", "bold"), command=gooo, relief=FLAT,
                     activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
        btn.place(rely=0.24 + o * i, relx=0.34, relwidth=0.2)
def login_user(string, event=None):
    # handling which splashscreen to go to
    if string == "Patient":
        splashscreen = PatientSplashScreen
        cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        cursor.execute('SELECT id,username,password FROM Patient')
        u = cursor.fetchall()
        # print(u)
        cnxn.commit()
    if string == "Doctor":
        splashscreen = DoctorSplashScreen
        # retriveDoc()
        cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        cursor.execute('SELECT id,username,password FROM Doctor')
        u = cursor.fetchall()
        # print(u)
        cnxn.commit()
    if string == "Nurse":
        splashscreen = NurseSplashScreen
        # retriveDoc()
        cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        cursor.execute('SELECT id,username,password FROM Nurses_WardBoys')
        u = cursor.fetchall()
        # print(u)
        cnxn.commit()

    username_info = user_username.get()
    password_info = user_password.get()
    # username_entry.delete(0,END)
    # password_entry.delete(0,END)
    c = 0
    for i in range(len(u)):
        if username_info == u[i][1] and password_info == u[i][2]:
            c = 1
            success = Label(master=login, text="Login Success", font=(" ", " 8 ", "bold"), background="#FFFF9C",
                            foreground="#00A288")
            success.place(relx=0.106, rely=0.68, relwidth=0.8, relheight=0.07)
            print(username_info, password_info)
            # screen1.destroy()
            splashscreen2 = partial(splashscreen, u[i][0])
            lobtn = Button(login, text="Continue", font=(" ", " 8 ", "bold"), command=splashscreen2, relief=FLAT,
                           activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
            lobtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
            break
    if c == 0:
        failed = Label(master=login, text="Login Failed. Please enter valid info", background="#FFFF9C",
                       foreground="#00A288", font=("calibri", 11))
        failed.place(relx=0.15, rely=0.66, relwidth=0.7, relheight=0.08)
        splashscreen2 = partial(login_user, string)
        lobtn = Button(login, text="Login", font=(" ", " 8 ", "bold"), command=splashscreen2, relief=FLAT,
                       activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
        lobtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
def admin1():
    global admin_username
    global admin_password
    global username_entry
    global password_entry
    global admin
    admin = Toplevel(screen)
    # admin=Tk()
    admin.configure(background="#00A288")
    admin.geometry("400x250")
    admin.title("Register")
    admin_username = StringVar()
    admin_password = StringVar()

    msg = Label(admin, text="Please enter your Username and Password, Admin", font=("Ariel", "10", "bold"),
                background="#00A288", foreground="#FFFF9C")
    msg.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)
    bgn = Label(admin, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    usrnm = Label(admin, text="username:", background="#FFFF9C", foreground="#00A288")
    usrnm.place(relx=0.2, rely=0.4)
    username_entry = Entry(admin, textvariable=admin_username)
    username_entry.place(relx=0.36, rely=0.4, relwidth=0.4)

    psrd = Label(admin, text="Password:", background="#FFFF9C", foreground="#00A288")
    psrd.place(relx=0.2, rely=0.55)
    username_entry = Entry(admin, textvariable=admin_password)
    username_entry.place(relx=0.36, rely=0.55, relwidth=0.4)

    adbtn = Button(admin, text="Login", font=(" ", " 8 ", "bold"), command=login_admin, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    adbtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
    print("login session")
    # admin.protocol("WM_DELETE_WINDOW", command= lambda: on_closing(admin))
def login(string):
    global user_username
    global user_password
    global username_entry
    global password_entry
    global login
    # screen.withdraw()
    # login=Tk()
    login = Toplevel(screen)
    login.configure(background="#00A288")
    login.geometry("400x250")
    login.title("User Login")
    user_username = StringVar()
    user_password = StringVar()

    welcomemsg = "Please enter your Username and Password, " + string
    msg = Label(login, text=welcomemsg, font=("Ariel", "10", "bold"), background="#00A288", foreground="#FFFF9C")
    msg.place(relx=0.08, rely=0.05, relwidth=0.84, relheight=0.1)
    bgn = Label(login, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    usrnm = Label(login, text="Username:", background="#FFFF9C", foreground="#00A288")
    usrnm.place(relx=0.2, rely=0.4)
    username_entry = Entry(login, textvariable=user_username)

    wheretogo = partial(login_user, string)
    username_entry.place(relx=0.36, rely=0.4, relwidth=0.4)
    username_entry.bind("<Return>", wheretogo)
    psrd = Label(login, text="Password:", background="#FFFF9C", foreground="#00A288")
    psrd.place(relx=0.2, rely=0.55)
    password_entry = Entry(login, textvariable=user_password)
    password_entry.place(relx=0.36, rely=0.55, relwidth=0.4)
    password_entry.bind("<Return>", wheretogo)
    lobtn = Button(login, text="Login", font=(" ", " 8 ", "bold"), command=wheretogo, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    lobtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
    # login.protocol("WM_DELETE_WINDOW",main_screen)
    print("login session")


# ---------------------------------
def room_create():
    global room_type
    global room_code
    global room_code_entry
    room = Toplevel(screen)
    room.configure(background="#00A288")
    room.geometry("800x800")
    room.title("Room Creation")
    room_type = StringVar()
    room_code = StringVar()
    rgmsg = "Please enter room information to create"
    rglb = Label(master=room, text=rgmsg, font=("Ariel", "10", ""), background="#00A288", foreground="#FFFF9C")

    rglb.place(relx=.3, rely=.05)
    bgn = Label(room, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.15, relwidth=1, relheight=1)
    rm_code = Label(room, text="code:", background="#FFFF9C", foreground="#00A288")
    rm_code.place(relx=0.1, rely=0.2)
    room_code_entry = Entry(room, textvariable=room_code)
    room_code_entry.place(relx=0.2, rely=0.20, relwidth=0.2)

    '''pat_pw = Label(room, text="Type:", background="#FFFF9C", foreground="#00A288")
    pat_pw.place(relx=0.1, rely=0.3)
    patient_password_entry = Entry(room, textvariable=patient_password)
    patient_password_entry.place(relx=0.2, rely=0.30, relwidth=0.2)'''

    rm_type = Label(room, text="Type:", background="#FFFF9C", foreground="#00A288")
    rm_type.place(relx=.10, rely=.30)

    R1 = Radiobutton(room, text="Care", variable=room_type, value="care")
    R1.place(relx=0.2, rely=0.30, relwidth=0.2)

    R2 = Radiobutton(room, text="ICU", variable=room_type, value="icu")
    R2.place(relx=0.2, rely=0.4, relwidth=0.2)
    R3 = Radiobutton(room, text="Operations", variable=room_type, value="operations")
    R3.place(relx=0.2, rely=0.5, relwidth=0.2)

    ptbtn = Button(room, text="Create", font=(" ", " 8 ", "bold"), command=store_room, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.90, relheight=0.1, relwidth=0.18)
def store_patient():
    patient_store = []
    # patient_username, patient_password, patient_name, patient_age, patient_id, patient_room_id
    # patient_address, patient_cell, patient_disease, patient_treatment, patient_cure_price
    # patient_bill, patient_exit_date, patient_entry_date, patient_diagnose, patient_side_notes
    patient_store.append(patient_username.get())
    patient_store.append(patient_password.get())
    patient_store.append(patient_name.get())
    patient_store.append(patient_age.get())
    patient_store.append(patient_doctor_id.get())
    patient_store.append(patient_room_id.get())
    patient_store.append(patient_address.get())
    patient_store.append(patient_cell.get())
    patient_store.append(patient_disease.get())
    patient_store.append(patient_treatment.get())
    patient_store.append(patient_cure_price.get())
    patient_store.append(patient_bill.get())
    patient_store.append(patient_exit_date.get())
    patient_store.append(patient_entry_date.get())
    patient_store.append(patient_diagnose.get())
    patient_store.append(patient_side_notes.get())
    for i in range(len(patient_store)):
        print(patient_store[i])
    # username,password,name,age,id,room_id,address,cell,disease,entry_date,exit_date,diagnose,sidenotes

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute(
        " insert into Patient (username, password, name, age,doctor_id,room_id, address,cell, disease, treatment,cure_price ,bill,exit_date,entry_date,diagnose,sidenotes) values %s;" % (
        tuple(patient_store),))
    cnxn.commit()
def store_nurse(room_value):
    # nurse_username, nurse_password, nurse_name, nurse_id, nurse_room_id
    nurse_store = []
    nurse_store.append(nurse_username.get())
    nurse_store.append(nurse_password.get())
    nurse_store.append(nurse_name.get())
    nurse_store.append(nurse_type.get())
    nurse_store.append(room_value.get())

    for i in range(len(nurse_store)):
        print(nurse_store[i])

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("insert into Nurses_WardBoys (username,password,name,type,room_id) values %s;" % (tuple(nurse_store),))

    cnxn.commit()
def store_doctor():
    doctor_store = []
    # doctor_username,doctor_password,doctor_name,doctor_id,doctor_depart
    doctor_store.append(doctor_username.get())
    doctor_store.append(doctor_password.get())
    doctor_store.append(doctor_name.get())
    # doctor_store.append(doctor_id.get())
    doctor_store.append(doctor_depart.get())
    for i in range(len(doctor_store)):
        print(doctor_store[i])
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute(" insert into Doctor (username,password,name,department) values %s;" % (tuple(doctor_store),))
    cnxn.commit()

    # cursor.execute(" select * from Handsa3.dbo.Doctor")
    # x= cursor.fetchall()
    # print(x)
def store_room():
    # room_type , room_code
    room_store = []
    room_store.append(1)
    room_store.append(room_type.get())
    room_store.append(room_code.get())

    for i in range(len(room_store)):
        print(room_store[i])

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute(" insert into Room (empty, type, code) values %s;" % (tuple(room_store),))

    cnxn.commit()
def update_patient(id):
    global patient_username_entry, patient_password_entry, patient_name_entry, patient_age_entry
    global patient_doctor_id_entry, patient_room_id_entry, patient_address_entry, patient_cell_entry
    global patient_disease_entry, patient_treatment_entry, patient_cure_price_entry
    global patient_bill_entry, patient_exit_date_entry, patient_entry_date_entry, patient_patient_diagnose_entry
    global patient_patient_side_notes_entry
    print('Hello World')

    Updaaate = [patient_doctor_id_entry.get(1.0, END),
                patient_room_id_entry.get(1.0, END), patient_age_entry.get(1.0, END),
                patient_password_entry.get(1.0, END), patient_name_entry.get(1.0, END),
                patient_cell_entry.get(1.0, END),
                patient_address_entry.get(1.0, END),
                patient_disease_entry.get(1.0, END), patient_treatment_entry.get(1.0, END),
                patient_cure_price_entry.get(1.0, END)]

    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("UPDATE Patient SET doctor_id=?  where id=?;", (Updaaate[0], id))
    cursor.execute("UPDATE Patient SET room_id=?    where id=?;", (Updaaate[1], id))
    cursor.execute("UPDATE Patient SET age=?        where id=?;", (Updaaate[2], id))
    cursor.execute("UPDATE Patient SET password=?   where id=?;", (Updaaate[3], id))
    cursor.execute("UPDATE Patient SET name=?       where id=?;", (Updaaate[4], id))
    cursor.execute("UPDATE Patient SET cell=?       where id=?;", (Updaaate[5], id))
    cursor.execute("UPDATE Patient SET address=?    where id=?;", (Updaaate[6], id))
    cursor.execute("UPDATE Patient SET disease=?    where id=?;", (Updaaate[7], id))
    cursor.execute("UPDATE Patient SET treatment=?  where id=?;", (Updaaate[8], id))
    cursor.execute("UPDATE Patient SET cure_price=? where id=?;", (Updaaate[9], id))

    # for i in range(0,2):
    #     Update(list1[i],Updaaate[i])
    # for i in range(3,9):
    #     Update(list1[i],Updaaate[i])
    cnxn.commit()
all_room=[]
emt_room=[]
def retrive_empty_room():
    temp_list=[]
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("select id from Handsa3.dbo.room where empty = 1;")
    u=cursor.fetchall()
    for i in u:
        temp_list.append(i)
    for j in temp_list:
        print(j[0])
        emt_room.append(j[0])
def retrive_room():
    temp_list=[]
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("select id from Handsa3.dbo.room ;")
    u=cursor.fetchall()
    for i in u:
        temp_list.append(i)
    for j in temp_list:
        print(j[0])
        all_room.append(j[0])
def fill_room_id(id):
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("update Room set empty = 0 where id = ? ;", id)
    cnxn.commit()


# Registeration
def patient_register():
    global patient_username, patient_password, patient_name, patient_age, patient_doctor_id, patient_room_id
    global patient_address, patient_cell, patient_disease, patient_treatment, patient_cure_price
    global patient_bill, patient_exit_date, patient_entry_date, patient_diagnose, patient_side_notes
    global patient_username_entry, patient_password_entry, patient_name_entry, patient_age_entry
    global patient_doctor_id_entry, patient_room_id_entry, patient_address_entry, patient_cell_entry
    global patient_disease_entry, patient_treatment_entry, patient_cure_price_entry
    global patient_bill_entry, patient_exit_date_entry, patient_entry_date_entry, patient_patient_diagnose_entry
    global patient_patient_side_notes_entry
    patient_register = Toplevel(screen)
    patient_register.configure(background="#00A288")
    patient_register.geometry("800x800")
    patient_register.title("Patient Register")
    patient_username = StringVar()
    patient_password = StringVar()
    patient_name = StringVar()
    patient_age = StringVar()
    patient_doctor_id = StringVar()
    patient_room_id = StringVar()
    patient_address = StringVar()
    patient_cell = StringVar()
    patient_disease = StringVar()
    patient_treatment = StringVar()
    patient_cure_price = StringVar()
    patient_bill = StringVar()
    patient_entry_date = StringVar()
    patient_exit_date = StringVar()
    patient_diagnose = StringVar()
    patient_side_notes = StringVar()

    rgmsg = "Please enter patient information to register"
    rglb = Label(master=patient_register, text=rgmsg, font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")

    rglb.place(relx=.3, rely=.05)
    bgn = Label(patient_register, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.15, relwidth=1, relheight=1)
    pat_user = Label(patient_register, text="username:", background="#FFFF9C", foreground="#00A288")
    pat_user.place(relx=0.1, rely=0.2)
    patient_username_entry = Entry(patient_register, textvariable=patient_username)
    patient_username_entry.place(relx=0.2, rely=0.20, relwidth=0.2)

    pat_pw = Label(patient_register, text="Password:", background="#FFFF9C", foreground="#00A288")
    pat_pw.place(relx=0.1, rely=0.3)
    patient_password_entry = Entry(patient_register, textvariable=patient_password)
    patient_password_entry.place(relx=0.2, rely=0.30, relwidth=0.2)

    pat_name = Label(patient_register, text="name:", background="#FFFF9C", foreground="#00A288")
    pat_name.place(relx=0.1, rely=0.4)
    patient_name_entry = Entry(patient_register, textvariable=patient_name)
    patient_name_entry.place(relx=0.2, rely=0.4, relwidth=0.2)

    pat_room_id = Label(patient_register, text="room_id:", background="#FFFF9C", foreground="#00A288")
    pat_room_id.place(relx=0.08, rely=0.5)
    patient_room_id_entry = Entry(patient_register, textvariable=patient_room_id)
    patient_room_id_entry.place(relx=0.2, rely=0.5, relwidth=0.2)

    pat_doctor_id = Label(patient_register, text="doctor_id:", background="#FFFF9C", foreground="#00A288")
    pat_doctor_id.place(relx=0.12, rely=0.6)
    patient_doctor_id_entry = Entry(patient_register, textvariable=patient_doctor_id)
    patient_doctor_id_entry.place(relx=0.2, rely=0.6, relwidth=0.2)

    pat_age = Label(patient_register, text="age:", background="#FFFF9C", foreground="#00A288")
    pat_age.place(relx=0.12, rely=0.7)
    patient_age_entry = Entry(patient_register, textvariable=patient_age)
    patient_age_entry.place(relx=0.2, rely=0.7, relwidth=0.2)

    pat_address = Label(patient_register, text="address:", background="#FFFF9C", foreground="#00A288")
    pat_address.place(relx=0.12, rely=0.8)
    patient_address_entry = Entry(patient_register, textvariable=patient_address)
    patient_address_entry.place(relx=0.2, rely=0.8, relwidth=0.2)

    pat_cell = Label(patient_register, text="cell:", background="#FFFF9C", foreground="#00A288")
    pat_cell.place(relx=0.12, rely=0.9)
    patient_cell_entry = Entry(patient_register, textvariable=patient_cell)
    patient_cell_entry.place(relx=0.20, rely=0.9, relwidth=0.2)

    pat_disease = Label(patient_register, text="disease:", background="#FFFF9C", foreground="#00A288")
    pat_disease.place(relx=0.6, rely=0.2)
    patient_disease_entry = Entry(patient_register, textvariable=patient_disease)
    patient_disease_entry.place(relx=0.7, rely=0.20, relwidth=0.2)

    pat_treatment = Label(patient_register, text="treatment:", background="#FFFF9C", foreground="#00A288")
    pat_treatment.place(relx=0.6, rely=0.3)
    patient_treatment_entry = Entry(patient_register, textvariable=patient_treatment)
    patient_treatment_entry.place(relx=0.7, rely=0.30, relwidth=0.2)

    pat_cure_price = Label(patient_register, text="cure_price:", background="#FFFF9C", foreground="#00A288")
    pat_cure_price.place(relx=0.6, rely=0.4)
    patient_cure_price_entry = Entry(patient_register, textvariable=patient_cure_price)
    patient_cure_price_entry.place(relx=0.7, rely=0.4, relwidth=0.2)

    pat_bill = Label(patient_register, text="bill:", background="#FFFF9C", foreground="#00A288")
    pat_bill.place(relx=0.65, rely=0.5)
    patient_bill_entry = Entry(patient_register, textvariable=patient_bill)
    patient_bill_entry.place(relx=0.7, rely=0.5, relwidth=0.2)

    pat_entry_date = Label(patient_register, text="entry_date:", background="#FFFF9C", foreground="#00A288")
    pat_entry_date.place(relx=0.6, rely=0.6)
    patient_entry_date_entry = Entry(patient_register, textvariable=patient_entry_date)
    patient_entry_date_entry.place(relx=0.7, rely=0.6, relwidth=0.2)

    pat_exit_date = Label(patient_register, text="exit_date:", background="#FFFF9C", foreground="#00A288")
    pat_exit_date.place(relx=0.6, rely=0.7)
    patient_exit_date_entry = Entry(patient_register, textvariable=patient_exit_date)
    patient_exit_date_entry.place(relx=0.7, rely=0.7, relwidth=0.2)

    pat_patient_diagnose = Label(patient_register, text="diagnose:", background="#FFFF9C", foreground="#00A288")
    pat_patient_diagnose.place(relx=0.6, rely=0.8)
    patient_patient_diagnose_entry = Entry(patient_register, textvariable=patient_diagnose)
    patient_patient_diagnose_entry.place(relx=0.7, rely=0.8, relwidth=0.2)

    pat_patient_side_notes = Label(patient_register, text="side_notes:", background="#FFFF9C", foreground="#00A288")
    pat_patient_side_notes.place(relx=0.6, rely=0.9)
    patient_patient_side_notes_entry = Entry(patient_register, textvariable=patient_side_notes)
    patient_patient_side_notes_entry.place(relx=0.7, rely=0.9, relwidth=0.2)
    ptbtn = Button(patient_register, text="register", font=(" ", " 8 ", "bold"), command=store_patient, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.90, relheight=0.1, relwidth=0.18)
def nurse_register():
    global nurse_username, nurse_password, nurse_name, nurse_type, nurse_room_id,all_room,emt_room
    global nurse_username_entry, nurse_password_entry, nurse_name_entry, nurse_id_entry, nurse_room_id_entry

    nurse_register = Toplevel(screen)
    nurse_register.configure(background="#00A288")
    nurse_register.geometry("800x800")
    nurse_register.title("Nurse Register")
    nurse_username = StringVar()
    nurse_password = StringVar()
    nurse_name = StringVar()
    nurse_room_id = StringVar()
    nurse_type = StringVar()
    rgmsg = "Please enter nurse information to register"
    rglb = Label(master=nurse_register, text=rgmsg, font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")
    rglb.place(relx=.3, rely=.05)
    bgn = Label(nurse_register, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.15, relwidth=1, relheight=1)
    nur_user = Label(nurse_register, text="username:", background="#FFFF9C", foreground="#00A288")
    nur_user.place(relx=0.2, rely=0.2)
    nurse_username_entry = Entry(nurse_register, textvariable=nurse_username)
    nurse_username_entry.place(relx=0.30, rely=0.20, relwidth=0.2)

    nur_pw = Label(nurse_register, text="Password:", background="#FFFF9C", foreground="#00A288")
    nur_pw.place(relx=0.2, rely=0.3)
    nurse_password_entry = Entry(nurse_register, textvariable=nurse_password)
    nurse_password_entry.place(relx=0.30, rely=0.30, relwidth=0.2)

    nur_name = Label(nurse_register, text="name:", background="#FFFF9C", foreground="#00A288")
    nur_name.place(relx=0.2, rely=0.4)
    nurse_name_entry = Entry(nurse_register, textvariable=nurse_name)
    nurse_name_entry.place(relx=0.30, rely=0.4, relwidth=0.2)

    nur_room_id = Label(nurse_register, text="Room ID:", background="#FFFF9C", foreground="#00A288")
    nur_room_id.place(relx=0.18, rely=0.5)
    # nurse_room_id_entry = Entry(nurse_register, textvariable=nurse_room_id)
    # nurse_room_id_entry.place(relx=0.30, rely=0.5, relwidth=0.2)

    nur_type = Label(nurse_register, text="Type:", background="#FFFF9C", foreground="#00A288")
    nur_type.place(relx=0.22, rely=0.6)
    R1 = Radiobutton(nurse_register, text="Nurse", variable=nurse_type, value="nurse")
    R1.place(relx=0.3, rely=0.6, relwidth=0.2)

    R2 = Radiobutton(nurse_register, text="Ward_boy", variable=nurse_type, value="ward")
    R2.place(relx=0.3, rely=0.65, relwidth=0.2)

    choices = []
    for i in all_room:
        choices.append(i)
    # Add a grid
    mainframe = Frame(nurse_register)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.place(relx=0.30, rely=0.5, relwidth=0.2)
    # Create a Tkinter variable
    room_value = IntVar()

    # Dictionary with options
    room_value.set(emt_room[0])  # set the default option

    popupMenu = OptionMenu(mainframe, room_value, *choices)
    popupMenu.grid(row=2, column=1)

    # on change dropdown value
    def change_dropdown(*args):
        print(room_value.get())

    # link function to change dropdown
    room_value.trace('w', change_dropdown)

    strr=partial(store_nurse,room_value)
    ptbtn = Button(nurse_register, text="register", font=(" ", " 8 ", "bold"), command=strr, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.70, relheight=0.1, relwidth=0.18)



def doctor_register():
    global doctor_username, doctor_password, doctor_name, doctor_id, doctor_depart
    global doctor_username_entry, doctor_password_entry, doctor_name_entry, doctor_id_entry, doctor_depart_entry
    doctor_register = Toplevel(screen)
    doctor_register.configure(background="#00A288")
    doctor_register.geometry("800x800")
    doctor_register.title("doctor Register")
    doctor_username = StringVar()
    doctor_password = StringVar()
    doctor_name = StringVar()
    doctor_depart = StringVar()
    doctor_id = StringVar()
    rgmsg = "Please enter doctor information to register"
    rglb = Label(master=doctor_register, text=rgmsg, font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")
    rglb.place(relx=.3, rely=.05)
    bgn = Label(doctor_register, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.15, relwidth=1, relheight=1)
    doc_user = Label(doctor_register, text="username:", background="#FFFF9C", foreground="#00A288")
    doc_user.place(relx=0.2, rely=0.2)
    doctor_username_entry = Entry(doctor_register, textvariable=doctor_username)
    doctor_username_entry.place(relx=0.30, rely=0.20, relwidth=0.2)

    doc_pw = Label(doctor_register, text="Password:", background="#FFFF9C", foreground="#00A288")
    doc_pw.place(relx=0.2, rely=0.3)
    doctor_password_entry = Entry(doctor_register, textvariable=doctor_password)
    doctor_password_entry.place(relx=0.30, rely=0.30, relwidth=0.2)

    doc_name = Label(doctor_register, text="name:", background="#FFFF9C", foreground="#00A288")
    doc_name.place(relx=0.2, rely=0.4)
    doctor_name_entry = Entry(doctor_register, textvariable=doctor_name)
    doctor_name_entry.place(relx=0.30, rely=0.4, relwidth=0.2)

    doc_depar = Label(doctor_register, text="department:", background="#FFFF9C", foreground="#00A288")
    doc_depar.place(relx=0.18, rely=0.5)
    doctor_depart_entry = Entry(doctor_register, textvariable=doctor_depart)
    doctor_depart_entry.place(relx=0.30, rely=0.5, relwidth=0.2)

    # doc_id = Label(doctor_register, text="id:", background="#FFFF9C", foreground="#00A288")
    # doc_id.place(relx=0.22, rely=0.6)
    # doctor_id_entry = Entry(doctor_register, textvariable=doctor_id)
    # doctor_id_entry.place(relx=0.30, rely=0.6, relwidth=0.2)
    ptbtn = Button(doctor_register, text="register", font=(" ", " 8 ", "bold"), command=store_doctor, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.90, relheight=0.1, relwidth=0.18)
def patient_update(id):
    global BePat
    id = Exis.get(1.0, 1.999)
    id = int(id)
    BePat.destroy()
    global patient_username, patient_password, patient_name, patient_age, patient_doctor_id, patient_room_id
    global patient_address, patient_cell, patient_disease, patient_treatment, patient_cure_price
    global patient_bill, patient_exit_date, patient_entry_date, patient_diagnose, patient_side_notes

    global patient_username_entry, patient_password_entry, patient_name_entry, patient_age_entry
    global patient_doctor_id_entry, patient_room_id_entry, patient_address_entry, patient_cell_entry
    global patient_disease_entry, patient_treatment_entry, patient_cure_price_entry
    global patient_bill_entry, patient_exit_date_entry, patient_entry_date_entry, patient_patient_diagnose_entry
    global patient_patient_side_notes_entry

    patient_register = Toplevel(screen)
    patient_register.configure(background="#00A288")
    patient_register.geometry("800x800")
    patient_register.title("Patient Register")

    # Username,Exitdate,Diagnose,Sidenotes,
    cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    cursor.execute("select password,name,doctor_id,room_id,age,address,cell,disease,treatment,cure_price from Patient where id=?;",id)
    uparray = cursor.fetchall()
    cnxn.commit()

    rgmsg = "Please enter patient information to register"
    rglb = Label(master=patient_register, text=rgmsg, font=("Ariel", "10", ""), background="#00A288",
                 foreground="#FFFF9C")
    rglb.place(relx=.3, rely=.05)
    bgn = Label(patient_register, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.15, relwidth=1, relheight=1)

    pat_pw = Label(patient_register, text="Password:", background="#FFFF9C", foreground="#00A288")
    pat_pw.place(relx=0.1, rely=0.3)
    patient_password_entry = Text(patient_register)
    patient_password_entry.place(relx=0.2, rely=0.30, relwidth=0.05, relheight=0.03)
    patient_password_entry.insert(INSERT, uparray[0][0])

    pat_name = Label(patient_register, text="name:", background="#FFFF9C", foreground="#00A288")
    pat_name.place(relx=0.1, rely=0.4)
    patient_name_entry = Text(patient_register)
    patient_name_entry.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.03)
    patient_name_entry.insert(INSERT, uparray[0][1])

    pat_room_id = Label(patient_register, text="room_id:", background="#FFFF9C", foreground="#00A288")
    pat_room_id.place(relx=0.08, rely=0.5)
    patient_room_id_entry = Text(patient_register)
    patient_room_id_entry.place(relx=0.2, rely=0.5, relwidth=0.05, relheight=0.03)
    patient_room_id_entry.insert(INSERT, uparray[0][2])

    pat_doctor_id = Label(patient_register, text="doctor_id:", background="#FFFF9C", foreground="#00A288")
    pat_doctor_id.place(relx=0.12, rely=0.6)
    patient_doctor_id_entry = Text(patient_register)
    patient_doctor_id_entry.place(relx=0.2, rely=0.6, relwidth=0.05, relheight=0.03)
    patient_doctor_id_entry.insert(INSERT, uparray[0][3])

    pat_age = Label(patient_register, text="age:", background="#FFFF9C", foreground="#00A288")
    pat_age.place(relx=0.12, rely=0.7)
    patient_age_entry = Text(patient_register)
    patient_age_entry.place(relx=0.2, rely=0.7, relwidth=0.05, relheight=0.03)
    patient_age_entry.insert(INSERT, uparray[0][4])

    pat_address = Label(patient_register, text="address:", background="#FFFF9C", foreground="#00A288")
    pat_address.place(relx=0.12, rely=0.8)
    patient_address_entry = Text(patient_register)
    patient_address_entry.place(relx=0.2, rely=0.8, relwidth=0.2, relheight=0.03)
    patient_address_entry.insert(INSERT, uparray[0][5])

    pat_cell = Label(patient_register, text="cell:", background="#FFFF9C", foreground="#00A288")
    pat_cell.place(relx=0.12, rely=0.9)
    patient_cell_entry = Text(patient_register)
    patient_cell_entry.place(relx=0.20, rely=0.9, relwidth=0.05, relheight=0.03)
    patient_cell_entry.insert(INSERT, uparray[0][6])

    pat_disease = Label(patient_register, text="disease:", background="#FFFF9C", foreground="#00A288")
    pat_disease.place(relx=0.6, rely=0.2)
    patient_disease_entry = Text(patient_register)
    patient_disease_entry.place(relx=0.7, rely=0.20, relwidth=0.2, relheight=0.03)
    patient_disease_entry.insert(INSERT, uparray[0][7])

    pat_treatment = Label(patient_register, text="treatment:", background="#FFFF9C", foreground="#00A288")
    pat_treatment.place(relx=0.6, rely=0.3)
    patient_treatment_entry = Text(patient_register)
    patient_treatment_entry.place(relx=0.7, rely=0.30, relwidth=0.2, relheight=0.03)
    patient_treatment_entry.insert(INSERT, uparray[0][8])

    pat_cure_price = Label(patient_register, text="cure_price:", background="#FFFF9C", foreground="#00A288")
    pat_cure_price.place(relx=0.6, rely=0.4)
    patient_cure_price_entry = Text(patient_register)
    patient_cure_price_entry.place(relx=0.7, rely=0.4, relwidth=0.05, relheight=0.03)
    patient_cure_price_entry.insert(INSERT, uparray[0][9])

    def updatte():
        cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-57I0EL1;Database=Handsa3;Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        if len(patient_doctor_id_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET doctor_id=?  where id=?;",
                           (int(patient_doctor_id_entry.get(1.0, 1.999)), id))

        if len(patient_room_id_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET room_id=?    where id=?;",
                           (int(patient_room_id_entry.get(1.0, 1.999)), id))

        if len(patient_age_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET age=?        where id=?;", (int(patient_age_entry.get(1.0, 1.999)), id))

        if len(patient_treatment_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET treatment=? where id=?;", (patient_treatment_entry.get(1.0, END), id))

        if len(patient_name_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET name=?       where id=?;", (patient_name_entry.get(1.0, END), id))

        if len(patient_cell_entry.get("1.0", "end-1c")) != 0:
            print(patient_cell_entry.get(1.0, END))
            cursor.execute("UPDATE Patient SET cell=?       where id=?;", (patient_cell_entry.get("1.0", "1.10"), id))

        if len(patient_address_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET address=?    where id=?;", (patient_address_entry.get(1.0, END), id))

        if len(patient_disease_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET disease=?    where id=?;", (patient_disease_entry.get(1.0, END), id))

        if len(patient_password_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET password=?  where id=?;", (patient_password_entry.get(1.0, END), id))

        if len(patient_cure_price_entry.get("1.0", "end-1c")) != 0:
            cursor.execute("UPDATE Patient SET cure_price=? where id=?;",
                           (float(patient_cure_price_entry.get(1.0, 1.99999)), id))

        cursor.execute('SELECT DATEDIFF(day,entry_date,exit_date)*10 from Patient where id =?', id)
        uo = cursor.fetchall()
        cursor.execute("UPDATE Patient SET bill=?  where id=?;", uo[0][0] , id)

        cnxn.commit()

    ptbtn = Button(patient_register, text="Update", font=(" ", " 12 ", "bold"), command=updatte, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.70, relheight=0.1, relwidth=0.18)
def BeforePatient():
    global Exis,BePat,register
    register.destroy()
    BePat = Toplevel(screen)
    # admin=Tk()
    BePat.configure(background="#00A288")
    BePat.geometry("400x250")
    BePat.title("Register")

    Exis = Text(BePat)
    Exis.place(relx=0.701, rely=0.55, relwidth=0.1, relheight=0.107)
    # Exis.bind("<Return>",Up1)

    Up1 = partial(patient_update, Exis.get(1.0, CURRENT))

    baw = Button(BePat, command=patient_register, text="Add a New Patient:", relief=FLAT, activebackground="#FFFF9C",
                 background="#FFFF9C", foreground="#00A288")
    baw.place(relx=0.2, rely=0.4, relwidth=0.6)

    tr = Button(BePat, text="Update an Existing Patient with ID :", command=Up1, relief=FLAT,
                activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    tr.place(relx=0.2, rely=0.55, relwidth=0.47)
def AdminSplashScreen(Adminid):
    admin.destroy()
    global register
    register = Toplevel(screen)
    register.configure(background="#00A288")
    register.geometry("500x500")
    register.title("register")
    rgmsg = "Please Choose Which account type you would like to register"
    rglb = Label(master=register, text=rgmsg, font=("Ariel", "10", "bold"), background="#00A288", foreground="#FFFF9C")
    rglb.place(relx=.1, rely=0.1)
    bgn = Label(register, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)
    drbtn = Button(register, text="Doctor", font=(" ", " 14 ", ""), command=doctor_register, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    drbtn.place(relx=0.2, rely=.5, relheight=0.1, relwidth=0.18)
    nrbtn = Button(register, text="Nurse", font=(" ", " 14 ", ""), command=nurse_register, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    nrbtn.place(relx=0.4, rely=.5, relheight=0.1, relwidth=0.18)
    ptbtn = Button(register, text="Patient", font=(" ", " 14 ", ""), command=BeforePatient, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.6, rely=.5, relheight=0.1, relwidth=0.18)
    ptbtn = Button(register, text="Room", font=(" ", " 14 ", ""), command=room_create, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    ptbtn.place(relx=0.4, rely=.6, relheight=0.1, relwidth=0.18)
def admin1():
    global admin_username
    global admin_password
    global username_entry
    global password_entry
    global admin
    admin = Toplevel(screen)
    # admin=Tk()
    admin.configure(background="#00A288")
    admin.geometry("400x250")
    admin.title("Register")
    admin_username = StringVar()
    admin_password = StringVar()

    msg = Label(admin, text="Please enter your Username and Password, Admin", font=("Ariel", "10", "bold"),
                background="#00A288", foreground="#FFFF9C")
    msg.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)
    bgn = Label(admin, background="#FFFF9C")
    bgn.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)

    usrnm = Label(admin, text="username:", background="#FFFF9C", foreground="#00A288")
    usrnm.place(relx=0.2, rely=0.4)
    username_entry = Entry(admin, textvariable=admin_username)
    username_entry.place(relx=0.36, rely=0.4, relwidth=0.4)

    psrd = Label(admin, text="Password:", background="#FFFF9C", foreground="#00A288")
    psrd.place(relx=0.2, rely=0.55)
    username_entry = Entry(admin, textvariable=admin_password)
    username_entry.place(relx=0.36, rely=0.55, relwidth=0.4)

    adbtn = Button(admin, text="Login", font=(" ", " 8 ", "bold"), command=login_admin, relief=FLAT,
                   activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
    adbtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
    print("login session")
    # admin.protocol("WM_DELETE_WINDOW", command= lambda: on_closing(admin))
def login_admin():

    splashscreen = partial(AdminSplashScreen, "1")
    username_info = admin_username.get()
    password_info = admin_password.get()
    # username_entry.delete(0,END)
    # password_entry.delete(0,END)
    c = 0
    for i in range(len(admins)):
        if username_info == admins[i][0] and password_info == admins[i][1]:
            c = 1
            success = Label(master=admin, text="Login Success", font=(" ", " 8 ", "bold"), background="#FFFF9C",
                            foreground="#00A288")
            success.place(relx=0.106, rely=0.68, relwidth=0.8, relheight=0.07)
            print(username_info, password_info)
            # screen1.destroy()
            # splashscreen=partial(splashscreen,i)
            lobtn = Button(admin, text="Continue", font=(" ", " 8 ", "bold"), command=splashscreen, relief=FLAT,
                           activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
            lobtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)
            break
        else:
            failed = Label(master=admin, text="Login Failed. Please enter valid info", background="#FFFF9C",
                           foreground="#00A288", font=("calibri", 11))
            failed.place(relx=0.15, rely=0.66, relwidth=0.7, relheight=0.08)
            lobtn = Button(master=admin, text="Login", font=(" ", " 8 ", "bold"), command=login_admin, relief=FLAT,
                           activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288")
            lobtn.place(relx=0.4, rely=0.75, relheight=0.1, relwidth=0.2)


# ----------------------------------------

# Splash_Screen
def main_screen():
    global screen
    screen = Tk()
    screen.configure(background="#00A288")
    screen.geometry("565x600")
    screen.title("Hospital of Death")

    photo = PhotoImage(file='./StLukesGeisinger.gif')
    img = Label(master=screen, borderwidth=0, image=photo, background="#00A288")
    img.place(relx=0.0, rely=0.00, relwidth="1.0", relheight="0.56")

    title = Label(master=screen, text="Welcome to Hospital of Death's Database Mangement System.",
                  font=("Ariel", "10", "bold"), background="#00A288", foreground="#FFFF9C")
    title.place(relx=0.1, rely=0.59, relwidth="0.8", relheight="0.04")
    title = Label(master=screen, text="Plesae Specifiy your account type: ", font=("Ariel", "10", "bold"),
                  background="#00A288", foreground="#FFFF9C")
    title.place(relx=0.1, rely=0.63, relwidth="0.8", relheight="0.04")
    doctorfn = partial(login, "Doctor")
    doclog = Button(master=screen, text="Doctor", command=doctorfn, relief=FLAT, activebackground="#FFFF9C",
                    background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
    doclog.place(relx=0.08, rely=0.7, relwidth="0.407", relheight="0.1")
    nurfn = partial(login, "Nurse")
    nurlog = Button(master=screen, text="Nurse / Ward", command=nurfn, relief=FLAT, activebackground="#FFFF9C",
                    background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
    nurlog.place(relx=0.50, rely=0.7, relwidth="0.405", relheight="0.1")
    patfn = partial(login, "Patient")
    patlog = Button(master=screen, text="Patient", command=patfn, relief=FLAT, activebackground="#FFFF9C",
                    background="#FFFF9C", foreground="#00A288", activeforeground="#00A288")
    patlog.place(relx=0.08, rely=0.82, relwidth="0.407", relheight="0.1")
    adminlog = Button(master=screen, text="Admin", font=(" ", " 8 ", "bold"), command=admin1, relief=FLAT,
                      activebackground="#FFFF9C", background="#FFFF9C", foreground="#00A288",
                      activeforeground="#00A288")
    adminlog.place(relx=0.50, rely=0.82, relwidth="0.405", relheight="0.1")

    screen.mainloop()

retrive_room()
retrive_empty_room()
main_screen()
