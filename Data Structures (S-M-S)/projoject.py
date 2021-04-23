from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tinydb import TinyDB
from tinydb import where
from tinydb import Query
from tkcalendar import Calendar,DateEntry
from pathlib import Path
import datetime
now = datetime.datetime.now()
from projectt.TextFiling import linklist
ll=linklist()
from projectt.Queue import Queue
q=Queue()
from projectt.sorting import sorting
sort=sorting()
from projectt.Stack import stack
stac=stack()
stact=stack()
from projectt.practice import dfs_path_finding,graph

def openingFrom():
    mainf = Tk(className="Welcome")
    mainf.geometry("500x500+400+125")
    mainf.resizable(0,0)
    Pic = PhotoImage(file="schoool.png")
    pic = Pic.subsample(2,2)
    label = Label(mainf, image=pic)
    label.pack()
    root = Toplevel(master=mainf)
    root.geometry("200x160+560+260")
    root.overrideredirect(1)
    root.resizable(0,0)
    root.attributes("-alpha", 0.1)
    btnWelcome = Button(root, width=100, height=100, command=chooseFrom).place(x=0, y=0)
    root.lift(aboveThis=mainf)
    mainf.mainloop()
#----PORTAL FORM
def chooseFrom():
    choosef=Toplevel()
    choosef.geometry("600x580+350+100")
    choosef.resizable(0,0)
    Pic = PhotoImage(file="schoolportal.png")
    pic = Pic.subsample(2,2)
    label = Label(choosef, image=pic)
    label.pack()
    # TEACHER BUTTON
    photo = PhotoImage(file="teacher.png")
    phtt = photo.subsample(3, 3)
    btn_T = Button(choosef, text='Click Me !', width=100, height=100, bg='grey', command=lambda:[choosef.destroy(), tchr_login_portal()],image=phtt).place(x=50, y=300)
    # STUDENT BUTTON
    photo = PhotoImage(file="student.png")
    phts = photo.subsample(3, 3)
    btn_S = Button(choosef, text='Click Me !', width=100, height=100, bg='grey', command=lambda:[choosef.destroy(), st_login_portal()], image=phts).place(x=250, y=300)
    # COURSE BUTTON
    photo = PhotoImage(file="book.png")
    phtc = photo.subsample(3, 3)
    btn_S = Button(choosef, text='Click Me !', width=100, height=100, bg='grey', command=lambda:[choosef.destroy(), courseForm()], image=phtc).place(x=450,y=300)
    # ADMIN BUTTON
    photo = PhotoImage(file="adminnnn.png")
    phta = photo.subsample(3, 3)
    btn_A = Button(choosef, text='Click Me !', relief='flat', width=50, height=50, bg='grey', command=lambda:[choosef.destroy(), adminForm()],image=phta).place(x=10, y=510)
    #Location
    photo = PhotoImage(file="maps.png")
    phtl = photo.subsample(9, 9)
    btn_A = Button(choosef, text='Click Me !', relief='flat', width=50, height=50, bg='grey',command=lambda: [choosef.destroy(), locationForm()], image=phtl).place(x=535, y=510)
    choosef.mainloop()
#----TECHER PORTAL
def teacherFrom():
    teacherf = Toplevel()
    a = ("Welcome",q.NAME())
    teacherf.title(a)
    teacherf.geometry('600x580+350+100')
    teacherf.resizable(0,0)
    photo = PhotoImage(file="teacherportal.png")
    pic = photo.subsample(1,1)
    label = Label(teacherf, image=pic)
    label.pack()
    attendence = Button(teacherf, text="Attendence", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[teacherf.destroy(), techer_attedence()]).place(x=30, y=220)
    query = Button(teacherf, text="Query", relief='solid', width=16, height=1, bg='black', fg='white', font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[teacherf.destroy(), t_query_portal()]).place(x=30, y=270)
    timetable = Button(teacherf, text="Timetable", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[teacherf.destroy(), tch_timetable_portal()]).place(x=30, y=320)
    exam = Button(teacherf, text="Exam", relief='solid', width=16, height=1, fg='white', bg='black', font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[teacherf.destroy(), tch_ExamSchedule_portal()]).place(x=30, y=370)
    teacherf.resizable(0, 0)
    teacherf.mainloop()
#----Student PORTAL
def stdFrom():
    stdf = Toplevel()
    a = ("Welcome", ll.NAME())
    stdf.title(a)
    stdf.geometry('600x580+350+100')
    stdf.resizable(0,0)
    photo = PhotoImage(file="studentportal.png")
    pic = photo.subsample(1,1)
    label = Label(stdf, image=pic)
    label.pack()
    attendence = Button(stdf, text="Attendence", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[stdf.destroy(), std_attedence()]).place(x=30, y=220)
    query = Button(stdf, text="Query", relief='solid', width=16, height=1, bg='black', fg='white',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[stdf.destroy(), std_query_portal()]).place(x=30, y=270)
    timetable = Button(stdf, text="Timetable", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[stdf.destroy(), st_timetable_portal()]).place(x=30, y=320)
    exam = Button(stdf, text="Exam", relief='solid', width=16, height=1, fg='white', bg='black', font=('Lucida Calligraphy', 11, 'italic'), command=lambda:[stdf.destroy(), st_ExamSchedule_portal()]).place(x=30, y=370)
    stdf.resizable(0, 0)
    stdf.mainloop()
#----COURSE PORTAL
def courseForm():
    coursef = Toplevel()
    coursef.geometry('600x580+350+100')
    photo = PhotoImage(file="courseportal.png")
    pho_cp = photo.subsample(2, 2)
    label = Label(coursef, image=pho_cp)
    label.pack()
    Label(coursef, text="Select Class:", width=16, height=2, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic')).place(x=80, y=220)
    global number
    number = IntVar()
    numberChosen = ttk.Combobox(coursef, width=8,textvariable=number,font=('Lucida Calligraphy', 21))
    numberChosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 4
    numberChosen.place(x=320,y=220)
    numberChosen.current(0)
    listB1 = Listbox(coursef,width=30)
    see = Button(coursef, text="See Course", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda: ShowCourses(listB1, coursef)).place(x=200, y=280)
    coursef.resizable(0,0)
    coursef.mainloop()
def ShowCourses(listb,form):
    listb.delete(0,END)
    db = TinyDB("courses/Class " + str(number.get()) + ".json")
    subjects = [r['Subject'] for r in db]
    for i in range(0,len(subjects)):
        listb.insert(i+1,subjects[i])
    listb.place(x=200,y=330)
#Location
def locationForm():
    lf = Toplevel()
    lf.geometry('600x580+350+100')
    photo = PhotoImage(file="map.png")
    pho_lf = photo.subsample(2, 2)
    label = Label(lf, image=pho_lf)
    label.pack()
    Label(lf, text="Select Area:", width=16, height=2, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic')).place(x=80, y=220)
    global fromAdd
    fromAdd = StringVar()
    numberChosen = ttk.Combobox(lf, width=12,textvariable=fromAdd,font=('Lucida Calligraphy', 14))
    numberChosen['values'] = ('Water Pump','Ayesha Manzil','Al noor','Sakhi Hassan','Lasbella','Garden East','Gurumandir','Soldier Bazar','Nazimabad','Liaqatabad','Numaish','KDA','Karimabad','Ziauddin','Kashmir road','Buffer Zone')  # 4
    numberChosen.place(x=320,y=225)
    numberChosen.current(0)
    listB1 = Listbox(lf,height=10,width=70)
    scroll = Scrollbar(lf, command=listB1.yview)
    listB1.configure(yscrollcommand=scroll.set)
    scroll.pack(side=RIGHT, fill=Y)
    see = Button(lf, text="See Route", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda: ShowRoute(listB1)).place(x=200, y=280)
    lf.resizable(0,0)
    lf.mainloop()
def ShowRoute(listb):
    listb.delete(0,END)
    lst = list(dfs_path_finding(graph, fromAdd.get(), 'School'))
    for i in range(0, len(lst)):
        arr = lst[i]
        jagh=0
        cost=0
        listb.insert(END, "***Route To School***")
        for j in range(0, len(arr)):
            jagh+=1
            listb.insert(END,arr[j])
        cost=jagh*100
        listb.insert(END, "Fare of taking this route: ",cost)
    listb.place(x=80,y=330)
#----ADMIN PANNEL
def adminForm():
    adminf = Toplevel()
    adminf.geometry('600x580+350+100')
    photo = PhotoImage(file="adminportal.png")
    pho_ap = photo.subsample(2, 2)
    label = Label(adminf, image=pho_ap)
    label.pack()
    global adminPass
    adminPass = StringVar()
    photo = PhotoImage(file="lock.png")
    pic = photo.subsample(2,2)
    btna_l = Button(adminf, text='Click Me !', relief='flat', width=120, height=130, bg='yellow',command=lambda: AdminLogin(adminf),image=pic).place(x=230, y=250)
    entry3 = Entry(adminf, textvar=adminPass,bg='light yellow',width=25,font=('fb agency',16)).place(x=140, y=450)
    label1 = Label(adminf, text='Enter Password', relief='solid', width=25,height=1,bg='black',fg='white', font=('Harlow Solid Italic', 11,'italic')).place(x=170, y=410)
    adminf.resizable(0,0)
    adminf.mainloop()
def AdminLogin(adminf):
    if adminPass.get() == "admin":
       # print("Mubarak Ho!")
        messagebox.showinfo('Welcome','mubarak ho')
        adminf.destroy()
        adminPortal()
    else:
        adminf.destroy()
#ADMIN PORTAL
def adminPortal():
    adminp = Toplevel()
    adminp.geometry('600x650+350+50')
    photo = PhotoImage(file="admiinp.png")
    pho_adp= photo.subsample(1, 1)
    label = Label(adminp, image=pho_adp)
    label.pack()
    user = Button(adminp, text="User List", relief='solid', width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda :[adminp.destroy(),Admin_User_Portal()]).place(x=30, y=220)
    query = Button(adminp, text="Query", relief='solid', width=16, height=1, bg='black', fg='white',font=('Lucida Calligraphy', 11, 'italic'), command=lambda :[adminp.destroy(), ad_query_portal()]).place(x=30, y=270)
    timetable = Button(adminp, text="TimeTable",relief=SOLID, width=16, height=1, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[adminp.destroy(),ad_timetable_portal()]).place(x=30, y=320)
    Registration = Button(adminp, text="Attendence", relief=SOLID, width=16, height=1, fg='white', bg='black', font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[adminp.destroy(),ad_att_portal()]).place(x=30, y=370)
    Exam = Button(adminp, text="Exam Schedule", relief=SOLID, width=16, height=1, fg='white', bg='black', font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[adminp.destroy(),ad_examschedule_portal()]).place(x=30, y=420)
    #Fine = Button(adminp, text="Fine Implement", relief=SOLID, width=16, height=1, fg='white', bg='black', font=('Lucida Calligraphy', 11, 'italic')).place(x=30, y=470)
    adminp.resizable(0,0)
    adminp.mainloop()
#STUDENT ATTENDENCE PORTAL
def std_attedence():
    stdATT = Toplevel()
    stdATT.geometry('600x580+350+100')
    photo = PhotoImage(file="attndnce.png")
    pho_attdps= photo.subsample(1, 1)
    label = Label(stdATT, image=pho_attdps)
    label.pack()
    Mark = Button(stdATT, text="Mark Your Attendence", relief=SOLID, width=20, height=3, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda:markstd(stdATT)).place(x=180, y=250)
    back= Button(stdATT, text="Back", relief=SOLID, width=12, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[stdATT.destroy(),stdFrom()]).place(x=20, y=150)
    stdATT.resizable(0,0)
    stdATT.mainloop()
def markstd(stATT):
    db = TinyDB("STD " + str(now.day) + " .json")
    if (now.hour==20):
        db.insert({ ll.ID() : "Present"})
        #print("Attendence Marked")
        messagebox.showinfo('Welcome', 'ATTENDENCE MARKED')
        stATT.destroy()
        stdFrom()
    else:
        messagebox.showinfo('Welcome', 'ATTENDENCE CANNOT BE MARKED')
        #print("You cannot Mark your Attendence")
        stATT.destroy()
        stdFrom()
#TEACHER ATTENDENCE PORTAL
def techer_attedence():
    techATT = Toplevel()
    techATT.geometry('600x580+350+100')
    photo = PhotoImage(file="attndnce.png")
    pho_attdps= photo.subsample(1, 1)
    label = Label(techATT, image=pho_attdps)
    label.pack()
    Mark = Button(techATT, text="Mark Your Attendence", relief=SOLID, width=20, height=3, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'), command=lambda :markstaff(techATT)).place(x=180, y=250)
    back = Button(techATT, text="Back", relief=SOLID, width=12, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[techATT.destroy(),teacherFrom()]).place(x=20, y=150)
    techATT.resizable(0,0)
    techATT.mainloop()
def markstaff(tchATT):
    db = TinyDB("STAFF " + str(now.day) + " .json")
    if (now.hour==22):
        db.insert({ q.ID() : "Present"})
        #print("Attendence Marked")
        messagebox.showinfo('Welcome', 'ATTENDENCE MARKED')
        tchATT.destroy()
        teacherFrom()
    else:
        #print("You cannot Mark your Attendence")
        messagebox.showinfo('Welcome', 'ATTENDENCE CANNOT BE MARKED')
        tchATT.destroy()
        teacherFrom()
#ADMIN ATTENDANCE PORTAL
def Admin_User_Portal():
    attp = Toplevel()
    attp.geometry('715x650+350+50')
    attp.title('DE''ROZZZHH')
    photo = PhotoImage(file="attndnce.png")
    pho_aattdps = photo.subsample(1, 1)
    label = Label(attp, image=pho_aattdps)
    label.pack()
    # --------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list_tt = Listbox(attp, height=20, width=42)
    list_tt.place(x=20, y=230)
    tt_std = Button(attp, text="Student", width=16, height=2, fg='white', bg='black', command=lambda :show_std(list_tt),font=('Lucida Calligraphy', 10, 'italic')).place(x=70, y=140)
    check = Button(attp, text="See More", width=13, height=1, fg='white', bg='black', command=lambda: Pmoredetails(list_tt),font=('Lucida Calligraphy', 9)).place(x=85, y=190)
    delete_btn = Button(attp, text="Delete", width=10, height=2, fg='white', bg='black',command= lambda:delete_std(list_tt),font=('Lucida Calligraphy', 9, 'italic')).place(x=5, y=580)
    insert_btn = Button(attp, text="Insert", width=10, height=2, fg='white', bg='black',command= st_signup_portal,font=('Lucida Calligraphy', 9, 'italic')).place(x=230, y=580)
    update_btn = Button(attp, text="Update", width=10, height=2, fg='white', bg='black',command= lambda:update_std(list_tt),font=('Lucida Calligraphy', 9, 'italic')).place(x=120, y=580)
    # --------------------------------------------------------------->TEACHER<-------------------------------------------------------------------
    list2 = Listbox(attp, height=20, width=42)
    list2.place(x=430, y=230)
    tt_tchr = Button(attp, text="Teacher", width=16, height=2, fg='white', bg='black',command=lambda: show_staff(list2), font=('Lucida Calligraphy', 10, 'italic')).place(x=470, y=140)
    check1 = Button(attp, text="See More", width=13, height=1, fg='white', bg='black',command=lambda: Pmoreinfo(list2), font=('Lucida Calligraphy', 9)).place(x=485, y=190)
    deleteT_bttn = Button(attp, text="Delete", width=10, height=2, fg='white', bg='black',command= lambda:delete_staff(list2),font=('Lucida Calligraphy', 9, 'italic')).place(x=600, y=580)
    insertT_bttn = Button(attp, text="Insert", width=10, height=2, fg='white', bg='black',command= tchr_signup_portal,font=('Lucida Calligraphy', 9, 'italic')).place(x=380, y=580)
    updateT_btn = Button(attp, text="Update", width=10, height=2, fg='white', bg='black',command= lambda:update_staff(list2),font=('Lucida Calligraphy', 9, 'italic')).place(x=490, y=580)
    # -------------------------------------------GUI LINE------------------------------------------------------------------------------
    lblU_lin = Label(attp, text='', width=1, height=0, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 3, 'bold')).place(x=350, y=172)
    lblM_lin = Label(attp, text='', width=1, height=82, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 3, 'bold')).place(x=350, y=187)
    lblD_lin = Label(attp, text='', width=1, height=0, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 3, 'bold')).place(x=350, y=613)
    back = Button(attp, text="Back", relief=SOLID, width=12, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[attp.destroy(),adminPortal()]).place(x=10, y=70)
    attp.resizable(0, 0)
    attp.mainloop()
def update_std(lb):
    delete_std(lb)
    st_signup_portal()
    show_std(lb)
def delete_std(lb):
    db=TinyDB("StudentsDB.json")
    user = Query()
    db.remove(user.STDid == lb.selection_get())
    show_std(lb)
def show_std(list):
    list.delete(0,END)
    db=TinyDB("StudentsDB.json")
    stdID = [r['STDid'] for r in db]
    sort.bubble_sort(stdID)
    for i in range(0,len(stdID)):
        list.insert(i+1,stdID[i])
def Pmoredetails(list):
    db = TinyDB("StudentsDB.json")
    idSelect=list.selection_get()
    Line = db.search(where('STDid') == idSelect)
    sTDid = [r['STDid'] for r in Line]
    naam = [r['Name'] for r in Line]
    pas = [r['Password'] for r in Line]
    list.delete(0, END)
    list.insert(1,sTDid)
    list.insert(2,naam)
    list.insert(3,pas)
def update_staff(lb):
    delete_staff(lb)
    tchr_signup_portal()
    show_staff(lb)
def delete_staff(lb):
    db=TinyDB("TeacherDB.json")
    user = Query()
    db.remove(user.StaffID == lb.selection_get())
    show_staff(lb)
def show_staff(list):
    list.delete(0,END)
    db=TinyDB("TeacherDB.json")
    staffID = [r['StaffID'] for r in db]
    n = len(staffID)
    sort.quickSort(staffID,0,n-1)
    for i in range(0,len(staffID)):
        list.insert(i+1,staffID[i])
def Pmoreinfo(list):
    db = TinyDB("TeacherDB.json")
    idSelect=list.selection_get()
    Line = db.search(where('StaffID') == idSelect)
    staffId = [r['StaffID'] for r in Line]
    naam = [r['Name'] for r in Line]
    pas = [r['Password'] for r in Line]
    list.delete(0, END)
    list.insert(1,staffId)
    list.insert(2,naam)
    list.insert(3,pas)
#STUDENT QUERY PORTAL
def std_query_portal():
    stdqp = Toplevel()
    stdqp.geometry('700x650+350+50')
    photo = PhotoImage(file="studentportal.png")
    pho_stqps= photo.subsample(1, 1)
    label = Label(stdqp, image= pho_stqps)
    label.pack()
    global txt_query
    txt_query=StringVar()
    txtb_query = Entry(stdqp,font=('Lucida Calligraphy', 10),textvariable=txt_query)
    txtb_query.place(width=600,height=230)
    txtb_query.place(x=40, y=250)
    query_t = Button(stdqp, text="Submit To admin", width=16, height=1, fg='white', bg='black',command=lambda: sendQadmin(stdqp), font=('Lucida Calligraphy', 10, 'italic')).place(x=450, y=500)
    back = Button(stdqp, text="Back", relief=SOLID, width=12, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[stdqp.destroy(),stdFrom()]).place(x=20, y=170)
    stdqp.resizable(0,0)
    stdqp.mainloop()
def sendQadmin(form):
    db = TinyDB("QueryAdminStd.json")
    db.insert({'ID': ll.ID(),'Query':txt_query.get()})
    form.destroy()
    stdFrom()
#TEACHER QUERY PORTAL
def t_query_portal():
    tqp = Toplevel()
    tqp.geometry('700x650+350+50')
    photo = PhotoImage(file="teacherportal.png")
    pho_tqps= photo.subsample(1, 1)
    label = Label(tqp, image= pho_tqps)
    label.pack()
    global txt_query
    txt_query=StringVar()
    txtb_query = Entry(tqp,font=('Lucida Calligraphy', 10),textvariable=txt_query)
    txtb_query.place(width=600,height=230)
    txtb_query.place(x=40, y=250)
    query_t = Button(tqp, text="Submit To admin", width=16, height=1, fg='white', bg='black',command=lambda: sendTQadmin(tqp), font=('Lucida Calligraphy', 10, 'italic')).place(x=450, y=500)
    back = Button(tqp, text="Back", relief=SOLID, width=12, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[tqp.destroy(),teacherFrom()]).place(x=20, y=150)
    tqp.resizable(0,0)
    tqp.mainloop()
def sendTQadmin(form):
    db = TinyDB("QueryAdminStaff.json")
    db.insert({'ID': q.ID(),'Query':txt_query.get()})
    form.destroy()
    teacherFrom()
#ADMIN QUERY PORTAL
def ad_query_portal():
    ap = Toplevel()
    ap.geometry('715x650+350+30')
    ap.title('DE''ROZZZHH')
    photo = PhotoImage(file="query_portal.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(ap, image=pho_aattdps)
    label.pack()
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list1=Listbox(ap,height=10,width=110,bg='Grey')
    list1.place(x=20,y=240)
    query_t = Button(ap, text="Show Students", width=20, height=2, fg='white', bg='black',command=lambda: showstdQ(list1), font=('Lucida Calligraphy', 10, 'italic')).place(x=250, y=180)
    details = Button(ap, text="Show Student Querry", width=20, height=2, fg='white', bg='black', command=lambda: showmoreQ(list1), font=('Lucida Calligraphy', 10, 'italic')).place(x=450, y=180)
    details = Button(ap, text="Clear File", width=20, height=2, fg='white', bg='black',command=lambda: clearstdQ(list1), font=('Lucida Calligraphy', 10, 'italic')).place(x=50, y=180)
    # --------------------------------------------------------------->TEACHER<-------------------------------------------------------------------
    list2 = Listbox(ap, height=10, width=110,bg='Grey')
    list2.place(x=20, y=480)
    query_s = Button(ap, text="Show Teacher", width=20, height=2, fg='white', bg='black',command=lambda: showStaffQ(list2), font=('Lucida Calligraphy', 10, 'italic')).place(x=250, y=415)
    query_s = Button(ap, text="Show Teacher querry", width=20, height=2, fg='white', bg='black',command=lambda: showmoreTQ(list2), font=('Lucida Calligraphy', 10, 'italic')).place(x=450, y=415)
    details = Button(ap, text="Clear File", width=20, height=2, fg='white', bg='black', command=lambda: clearstaffQ(list2),font=('Lucida Calligraphy', 10, 'italic')).place(x=50, y=415)
    back = Button(ap, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[ap.destroy(),adminPortal()]).place(x=5, y=40)
    ap.resizable(0,0)
    ap.mainloop()
def clearstdQ(lb):
    db = TinyDB("QueryAdminStd.json")
    db.purge()
    lb.delete(0,END)
def clearstaffQ(lb):
    db = TinyDB("QueryAdminStaff.json")
    db.purge()
    lb.delete(0,END)
def showstdQ(listb):
    listb.delete(0,END)
    db = TinyDB("QueryAdminStd.json")
    Ids = [r['ID'] for r in db]
    for i in range(0,len(Ids)):
        stac.push(Ids[i])
    for i in range(0, len(Ids)):
        listb.insert(i,stac.pop())
def showmoreQ(listb):
    db = TinyDB("QueryAdminStd.json")
    Line = db.search(where('ID') == listb.selection_get())
    Query = [r['Query'] for r in Line]
    listb.delete(0,END)
    for i in range(0,len(Query)):
        stac.push((Query[i]))
        listb.insert(i,stac.pop())
def showStaffQ(listb):
    listb.delete(0,END)
    db = TinyDB("QueryAdminStaff.json")
    Ids = [r['ID'] for r in db]
    for i in range(0,len(Ids)):
        stact.push(Ids[i])
    for i in range(0, len(Ids)):
        listb.insert(i,stact.pop())
def showmoreTQ(listb):
    db = TinyDB("QueryAdminStaff.json")
    Line = db.search(where('ID') == listb.selection_get())
    Query = [r['Query'] for r in Line]
    listb.delete(0,END)
    for i in range(0,len(Query)):
        stact.push((Query[i]))
        listb.insert(i,stact.pop())
#STUDENT SIGNUP FORM
def st_signup_portal():
    st_signup = Toplevel()
    st_signup.geometry('700x650+350+50')
    pht_signup = PhotoImage(file="studentportal.png")
    pho_sgnup= pht_signup.subsample(1, 1)
    label = Label(st_signup, image=pho_sgnup)
    label.pack()
    #NAME
    s_name = Label(st_signup, text='NAME : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=200)
    global signupname
    signupname = StringVar()
    sname = Entry(st_signup, textvar=signupname, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=200)
    #PASSWORD
    s_pass = Label(st_signup, text='Password : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=300)
    global signuppass
    signuppass = StringVar()
    spasswordtxt = Entry(st_signup, textvar=signuppass, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=300)
    # CONFIRM PASSWORD
    s_c_pass = Label(st_signup, text='Confirm Pass  :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=400)
    global signupconfirmpassword
    signupconfirmpassword = StringVar()
    sc_passwordtxt = Entry(st_signup, textvar=signupconfirmpassword, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=400)
    # ST_ID
    s_idees = Label(st_signup, text='Id :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=500)
    global signupids
    signupids = StringVar()
    sideestxt = Entry(st_signup, textvar=signupids, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=500)
    s_idees = Label(st_signup, text='Enter the id provided by registration office...', relief='flat', width=30, height=1, bg='dark green', fg='white',font=('calibiri', 11, 'italic')).place(x=370, y=500)
    #BUTTONS
    login = Button(st_signup, text="Login", relief='solid', width=16, height=1, bg='black', fg='white',command=lambda: std_Create(st_signup), font=('Lucida Calligraphy', 11, 'italic')).place(x=500, y=600)
    insert = Button(st_signup, text="Done", relief='solid', width=16, height=1, bg='black', fg='white',command=lambda: std_CreateD(st_signup), font=('Lucida Calligraphy', 11, 'italic')).place(x=300, y=600)
    back = Button(st_signup, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic')).place(x=5, y=40)
    st_signup.resizable(0,0)
    st_signup.mainloop()
#Text Filing sigunp STD
def std_CreateD(st):
    db = TinyDB("StudentsDB.json")
    if(signuppass.get()==signupconfirmpassword.get()):
        db.insert({'STDid': signupids.get(), 'Name': signupname.get(), 'Password': signuppass.get()})
        st.destroy()
    else:
        #print("Pass not match")
        messagebox.showinfo('Welcome', 'PASS MATCHED')
        st.destroy()
        st_signup_portal()
#Text Filing sigunp STD
def std_Create(st):
    db = TinyDB("StudentsDB.json")
    if(signuppass.get()==signupconfirmpassword.get()):
        db.insert({'STDid': signupids.get(), 'Name': signupname.get(), 'Password': signuppass.get()})
        st.destroy()
        st_login_portal()
    else:
        messagebox.showinfo('Welcome', 'PASS NOT MATCH')
        #print("Pass not match")
        st.destroy()
        st_signup_portal()
#STUDENT LOGIN FORM
def st_login_portal():
    st_login= Toplevel()
    st_login.geometry('700x650+350+50')
    pht_login = PhotoImage(file="studentportal.png")
    pho_login= pht_login.subsample(1, 1)
    label = Label(st_login, image=pho_login)
    label.pack()
    # ST_ID
    s_idees = Label(st_login, text='Id :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=80, y=280)
    global idees
    idees = StringVar()
    idees1 = Entry(st_login, textvar=idees, bg='light yellow', width=15, font=('fb agency', 16)).place(x=240, y=280)
    # PASSWORD
    s_pass = Label(st_login, text='Password : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=80, y=380)
    global password
    password = StringVar()
    password1 = Entry(st_login, textvar=password, bg='light yellow', width=15, font=('fb agency', 16)).place(x=240, y=380)
    #BUTTONS
    login= Button(st_login, text="login", relief='solid', width=12, height=1, bg='black', fg='white',command=lambda:std_login(st_login),font=('Lucida Calligraphy', 11, 'italic')).place(x=290, y=500)
    sign_up = Button(st_login, text="Sign up", relief='solid', width=12, height=1, fg='white', bg='black',command=lambda:[st_login.destroy(), st_signup_portal()],font=('Lucida Calligraphy', 11, 'italic'), ).place(x=500, y=500)
    st_login.resizable(0,0)
    st_login.mainloop()
#Liner Search
def std_login(stdlogin):
    db=TinyDB("StudentsDB.json")
    Ids = [r['STDid'] for r in db]
    Line = db.search(where('STDid') == idees.get())
    Name = [r['Name'] for r in Line]
    Passes = [r['Password'] for r in db]
    found=False
    for i in range(0,len(Ids)):
        if Ids[i]==idees.get():
            for j in range(0,len(Passes)):
                if Passes[j]==password.get():
                    found=True
                    ll.insert(idees.get())
                    ll.insert(Name[0])
                    #print("Welcome",ll.NAME())
                    stdlogin.destroy()
                    messagebox.showinfo('Welcome', 'Welcome ' + ll.NAME())
                    stdFrom()
                    break
    if found==False:
        #print("Wrong Credentials")
        stdlogin.destroy()
        messagebox.showwarning('Welcome', 'Wrong Credentials')
        st_login_portal()
#  TEACHER SIGNUP FORM
def tchr_signup_portal():
    tchr_signup = Toplevel()
    tchr_signup.geometry('700x650+350+50')
    pht_signup = PhotoImage(file="teacherportal.png")
    pho_sgnup= pht_signup.subsample(1, 1)
    label = Label(tchr_signup, image=pho_sgnup)
    label.pack()
    #NAME
    s_name = Label(tchr_signup, text='NAME : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=200)
    global Tsname
    Tsname = StringVar()
    name = Entry(tchr_signup, textvar=Tsname, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=200)
    #PASSWORD
    s_pass = Label(tchr_signup, text='Password : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=300)
    global TsPassword
    TsPassword = StringVar()
    password = Entry(tchr_signup, textvar=TsPassword, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=300)
    # CONFIRM PASSWORD
    s_c_pass = Label(tchr_signup, text='Confirm Pass  :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=400)
    global Tcpass
    Tcpass = StringVar()
    c_password = Entry(tchr_signup, textvar=Tcpass, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=400)
    # T_ID
    s_idees = Label(tchr_signup, text='Id :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=20, y=500)
    global TsID
    TsID = StringVar()
    idees = Entry(tchr_signup, textvar=TsID, bg='light yellow', width=15, font=('fb agency', 16)).place(x=180, y=500)
    s_idees = Label(tchr_signup, text='Enter the id provided by registration office...', relief='flat', width=30, height=1, bg='dark green', fg='white',font=('calibiri', 11, 'italic')).place(x=370, y=500)
    #BUTTONS
    login= Button(tchr_signup, text="login", relief='solid', width=16, height=1, bg='black', fg='white',command=lambda :tch_Create(tchr_signup),font=('Lucida Calligraphy', 11, 'italic')).place(x=500, y=600)
    tchr_signup.resizable(0,0)
    tchr_signup.mainloop()
#Text Filing sigunp Teacher
def tch_Create(staff):
    db = TinyDB("TeacherDB.json")
    if(TsPassword.get()==Tcpass.get()):
        db.insert({'StaffID': TsID.get(), 'Name': Tsname.get(), 'Password': TsPassword.get()})
        staff.destroy()
        tchr_login_portal()
    else:
        messagebox.showinfo('Welcome', 'PASS NOT MATCH')
        #print("Pass not match")
        staff.destroy()
        tchr_signup_portal()
#TEACHER LOGIN FORM
def tchr_login_portal():
    tchr_login= Toplevel()
    tchr_login.geometry('700x650+350+50')
    pht_login = PhotoImage(file="teacherportal.png")
    pho_login= pht_login.subsample(1, 1)
    label = Label(tchr_login, image=pho_login)
    label.pack()
    # PASSWORD
    s_pass = Label(tchr_login, text='Password : ', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=80, y=380)
    global Tpassword
    Tpassword = StringVar()
    password = Entry(tchr_login, textvar=Tpassword, bg='light yellow', width=15, font=('fb agency', 16)).place(x=240, y=380)
    # ST_ID
    s_idees = Label(tchr_login, text='Id :', relief='solid', width=15, height=1, bg='black', fg='white',font=('Harlow Solid Italic', 11, 'italic')).place(x=80, y=280)
    global Tidees
    Tidees = StringVar()
    idees = Entry(tchr_login, textvar=Tidees, bg='light yellow', width=15, font=('fb agency', 16)).place(x=240, y=280)
    #BUTTONS
    login= Button(tchr_login, text="login", relief='solid', width=12, height=1, bg='black', fg='white',command=lambda :staff_login(tchr_login),font=('Lucida Calligraphy', 11, 'italic')).place(x=290, y=500)
    sign_up = Button(tchr_login, text="Sign up", relief='solid', width=12, height=1, fg='white', bg='black',command=lambda :[tchr_login.destroy(),tchr_signup_portal()],font=('Lucida Calligraphy', 11, 'italic'), ).place(x=500, y=500)
    tchr_login.resizable(0,0)
    tchr_login.mainloop()
#Binary Search
def staff_login(tchlogin):
    db=TinyDB("TeacherDB.json")
    Ids = [r["StaffID"] for r in db]
    Line = db.search(where('StaffID') == Tidees.get())
    Name = [r['Name'] for r in Line]
    Passes = [r['Password'] for r in db]
    found = False
    for i in range(0, len(Ids)):
        if Ids[i] == Tidees.get():
            for j in range(0, len(Passes)):
                if Passes[j] == Tpassword.get():
                    found = True
                    q.Insert(Tidees.get())
                    q.Insert(Name[0])
                    #print("Welcome",q.NAME())
                    messagebox.showinfo('Welcome Teacher', 'Welcome '+q.NAME())
                    tchlogin.destroy()
                    teacherFrom()
                    break
    if found == False:
        messagebox.showinfo('Welcome', 'Wrong Credentials')
        #print("Wrong Credentials")
        tchlogin.destroy()
        tchr_login_portal()
def showTTadmin(lb,clas):
    lb.delete(0, END)
    db = TinyDB("timetable/Class " + clas + "t.json")
    pre = [r['Period'] for r in db]
    subject = [r['Subject'] for r in db]
    for i in range(0, len(subject)):
        lb.insert(END, "Period:"+pre[i],"Subject: "+subject[i])
#ADMIN TIME TABLE
def ad_timetable_portal():
    att_p = Toplevel()
    att_p.geometry('715x650+350+30')
    att_p.title('DE''ROZZZHH')
    photo = PhotoImage(file="ad_timtble.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(att_p, image=pho_aattdps)
    label.pack()
    global classs
    classs = StringVar()
    numberChosen = ttk.Combobox(att_p, width=10, textvariable=classs, font=('Lucida Calligraphy', 18))
    numberChosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 4
    numberChosen.place(x=250, y=175)
    numberChosen.current(0)
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list_tt = Listbox(att_p, height=20, width=40,bg='grey')
    list_tt.place(x=20, y=230)

    tt_std = Button(att_p, text="Student", width=16, height=2, fg='white', bg='black',command=lambda :showTTadmin(list_tt,classs.get()),font=('Lucida Calligraphy', 10, 'italic')).place(x=50, y=170)
    # --------------------------------------------------------------->TEACHER<-------------------------------------------------------------------
    list2 = Listbox(att_p, height=20, width=40,bg='grey')
    list2.place(x=430, y=230)
    tt_tchr = Button(att_p, text="Teacher", width=16, height=2, fg='white', bg='black',command=lambda :showTTadmin(list2,classs.get()),font=('Lucida Calligraphy', 10, 'italic')).place(x=470, y=170)
    #-------------------------------------------GUI LINE------------------------------------------------------------------------------
    lblU_lin = Label(att_p, text='', width=1,height=0, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 3, 'bold'))
    lblU_lin.place(x=350, y=172)
    lblM_lin = Label(att_p, text='', width=1, height=82, relief=SUNKEN, fg="BLACK", bg='#598234',font=('bebas kai', 3, 'bold'))
    lblM_lin.place(x=350, y=187)
    lblD_lin = Label(att_p, text='', width=1, height=0, relief=SUNKEN, fg="BLACK", bg='#598234',font=('bebas kai', 3, 'bold'))
    lblD_lin.place(x=350, y=613)
    back = Button(att_p, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[att_p.destroy(),adminPortal()]).place(x=5, y=40)
    att_p.resizable(0,0)
    att_p.mainloop()

#Std Timetable Portal
def st_timetable_portal():
    stt = Toplevel()
    stt.geometry('715x650+350+30')
    stt.title('DE''ROZZZHH')
    photo = PhotoImage(file="st_timetable.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(stt, image=pho_aattdps)
    label.pack()
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list1=Listbox(stt,height=20,width=100,bg='grey')
    query_t = Button(stt, text="Show TimeTable ", width=20, height=2, fg='white', bg='black',command=lambda : showTT(list1,ll.ID()),font=('Lucida Calligraphy', 10, 'italic')).place(x=220, y=180)
    back = Button(stt, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[stt.destroy(),stdFrom()]).place(x=5, y=40)
    stt.resizable(0, 0)
    stt.mainloop()
def showTT(lb,Id):
    lb.delete(0, END)
    for i in Id:
        id=str(i)
        break
    db = TinyDB("timetable/Class " + id + "t.json")
    pre = [r['Period'] for r in db]
    subject = [r['Subject'] for r in db]
    for i in range(0, len(subject)):
        lb.insert(END, "Period:"+pre[i],"Subject: "+subject[i])
    lb.place(x=20, y=240)
#Teacher Timetable
def tch_timetable_portal():
    ttt = Toplevel()
    ttt.geometry('715x650+350+30')
    ttt.title('DE''ROZZZHH')
    photo = PhotoImage(file="tch_timtable.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(ttt, image=pho_aattdps)
    label.pack()
    #--------------------------------------------------------------->Teacher<-------------------------------------------------------------------
    list_ttt=Listbox(ttt,height=20,width=100,bg='grey')
    query_t = Button(ttt, text="Show TimeTable ", width=20, height=2, fg='white', bg='black',command=lambda :showTT(list_ttt,q.ID()),font=('Lucida Calligraphy', 10, 'italic')).place(x=220, y=180)
    lbl_head = Label(ttt, text='', width=350, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 3, 'bold'))
    lbl_head.place(x=0, y=660)
    back = Button(ttt, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[ttt.destroy(),teacherFrom()]).place(x=5, y=40)
    ttt.resizable(0, 0)
    ttt.mainloop()
def showstdATT(lb):
    myFile = Path("STD "+day.get()+" .json")
    if myFile.is_file():
        db = TinyDB("STD " + day.get() + " .json")
        read=db.all()
        for i in range(0,len(read)):
            lb.insert(i,read[i])
    else:
        messagebox.showinfo('Welcome', 'FILE NOT FOUND')
        #print("File not found")

def showstaffATT(lb):
    myFile = Path("STAFF "+dayt.get()+" .json")
    if myFile.is_file():
        db = TinyDB("STAFF " + dayt.get() + " .json")
        read=db.all()
        for i in range(0,len(read)):
            lb.insert(i,read[i])
    else:
        messagebox.showinfo('Welcome', 'FILE NOT FOUND')
        #print("File not found")
#ADMIN attandence PORTAL
def ad_att_portal():
    arp = Toplevel()
    arp.geometry('715x650+350+30')
    arp.title('DE''ROZZZHH')
    photo = PhotoImage(file="attndnce.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(arp, image=pho_aattdps)
    label.pack()
    global day
    day = StringVar()
    numberChosen = ttk.Combobox(arp, width=8, textvariable=day, font=('Lucida Calligraphy', 21))
    numberChosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)  # 4
    numberChosen.place(x=370, y=180)
    numberChosen.current(0)
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    listst=Listbox(arp,height=10,width=110)
    listst.place(x=20, y=240)
    query_t = Button(arp, text="Show Attendence(Students)", width=20, height=2, fg='white', bg='black',command=lambda :showstdATT(listst),font=('Lucida Calligraphy', 10, 'italic')).place(x=140, y=180)
    lbl1 = Label(arp, text='', width=57, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold')).place(x=0, y=191)
    lbl2 = Label(arp, text='', width=80, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold')).place(x=570, y=191)
    # --------------------------------------------------------------->TEACHER<-------------------------------------------------------------------
    global dayt
    dayt = StringVar()
    numberChosen = ttk.Combobox(arp, width=8, textvariable=dayt, font=('Lucida Calligraphy', 21))
    numberChosen['values'] = (
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31)  # 4
    numberChosen.place(x=370, y=415)
    numberChosen.current(0)
    list2 = Listbox(arp, height=10, width=110)
    list2.place(x=20, y=480)
    query_s = Button(arp, text="Show Attendence(Teacher)", width=20, height=2, fg='white', bg='black',command=lambda :showstaffATT(list2),font=('Lucida Calligraphy', 10, 'italic')).place(x=140, y=415)
    lbl_head = Label(arp, text='', width=57, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold'))
    lbl_head.place(x=0, y=427)
    lbl_head = Label(arp, text='', width=80, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold'))
    lbl_head.place(x=570, y=427)
    back = Button(arp, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[arp.destroy(),adminPortal()]).place(x=5, y=40)
    arp.resizable(0, 0)
    arp.mainloop()
#STUDENT EXAM SCHEDULE
def st_ExamSchedule_portal():
    ses = Toplevel()
    ses.geometry('715x650+350+30')
    ses.title('DE''ROZZZHH')
    photo = PhotoImage(file="attndnce.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(ses, image=pho_aattdps)
    label.pack()
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list1 = Listbox(ses, height=20, width=120)
    query_t = Button(ses, text="Show TimeTable ", width=20, height=2, fg='white', bg='black',command=lambda :showExamS(list1,ll.ID()),font=('Lucida Calligraphy', 10, 'italic')).place(x=220, y=180)
    back = Button(ses, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[ses.destroy(),stdFrom()]).place(x=5, y=40)
    ses.resizable(0, 0)
    ses.mainloop()
def showExamS(lb,Id):
    lb.delete(0, END)
    for i in Id:
        id=str(i)
        break
    db = TinyDB("Exam/Class " + id + ".json")
    dat = [r['Date'] for r in db]
    mon = [r['Month'] for r in db]
    subject = [r['Subject'] for r in db]
    for i in range(0, len(subject)):
        lb.insert(END, "Date:"+dat[i],"Month: "+mon[i],"Subject: "+subject[i])
    lb.place(x=20, y=240)
#TEACHER EXAM SCHEDULE
def tch_ExamSchedule_portal():
    tes = Toplevel()
    tes.geometry('715x650+350+30')
    tes.title('DE''ROZZZHH')
    photo = PhotoImage(file="attndnce.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(tes, image=pho_aattdps)
    label.pack()
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list1=Listbox(tes,height=20,width=120)
    query_t = Button(tes, text="Show Exam Schedule ", width=20, height=2, fg='white', bg='black',command=lambda :showExamS(list1,q.ID()),font=('Lucida Calligraphy', 10, 'italic')).place(x=220, y=180)
    back = Button(tes, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[tes.destroy(),teacherFrom()]).place(x=5, y=40)
    tes.resizable(0, 0)
    tes.mainloop()
#admin Exam Schedule
def ad_examschedule_portal():
    aes = Toplevel()
    aes.geometry('715x650+350+30')
    aes.title('DE''ROZZZHH')
    photo = PhotoImage(file="attndnce.png")
    pho_aattdps= photo.subsample(1, 1)
    label = Label(aes, image=pho_aattdps)
    label.pack()
    lbl_head = Label(aes, text='Day: ', width=7, bg="Black",fg="white", font=('bebas kai', 16)).place(x=40,y=250)
    global datee
    datee = StringVar()
    dat = Entry(aes, textvar=datee,relief=SUNKEN, bg='light yellow', width=15, font=('fb agency', 16)).place(x=140, y=250)
    lbl_head = Label(aes, text='Month: ', width=7, bg="Black", fg="white", font=('bebas kai', 16)).place(x=350, y=250)
    global Month
    Month = StringVar()
    mon = Entry(aes, textvar=Month, bg='light yellow', width=15, font=('fb agency', 16)).place(x=450, y=250)
    lbl_head = Label(aes, text='Class: ', width=7, bg="Black", fg="white", font=('bebas kai', 16)).place(x=40, y=300)
    global clas
    clas = StringVar()
    dat = Entry(aes, textvar=clas, relief=SUNKEN, bg='light yellow', width=15, font=('fb agency', 16)).place(x=140,y=300)
    lbl_head = Label(aes, text='Subject: ', width=7, bg="Black", fg="white", font=('bebas kai', 16)).place(x=350, y=300)
    global subj
    subj = StringVar()
    mon = Entry(aes, textvar=subj, bg='light yellow', width=15, font=('fb agency', 16)).place(x=450, y=300)
    #--------------------------------------------------------------->STUDENT<-------------------------------------------------------------------
    list1 = Listbox(aes, height=18, width=110)
    query_t = Button(aes, text="Show students examshedule", width=20, height=2, fg='white', command=lambda :showExam(list1),bg='black',font=('Lucida Calligraphy', 10, 'italic')).place(x=250, y=180)
    deleteS_bttn = Button(aes, text="Delete", width=10, height=2, fg='white', bg='black',command=lambda :delExam(list1),font=('Lucida Calligraphy', 9, 'italic')).place(x=460, y=180)
    insertS_bttn = Button(aes, text="Insert", width=10, height=2, fg='white', bg='black',command=createExam,font=('Lucida Calligraphy', 9, 'italic')).place(x=130, y=180)
    lbl_head = Label(aes, text='', width=57, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold'))
    lbl_head.place(x=0, y=191)
    lbl_head = Label(aes, text='', width=80, relief=SUNKEN, fg="BLACK", bg='#598234', font=('bebas kai', 2, 'bold'))
    lbl_head.place(x=570, y=191)
    back = Button(aes, text="Back", relief=SOLID, width=9, fg='white', bg='black',font=('Lucida Calligraphy', 11, 'italic'),command=lambda :[aes.destroy(),adminPortal()]).place(x=5, y=40)
    aes.resizable(0,0)
    aes.mainloop()
def createExam():
    db = TinyDB("Exam/Class " + clas.get() + ".json")
    db.insert({"Date":datee.get(),"Month":Month.get(),"Subject":subj.get()})
    messagebox.showinfo('Welcome', 'EXAM SCHEDULED')
    #print("Exam Scheuled")
def showExam(lb):
    lb.delete(0, END)
    db = TinyDB("Exam/Class " + clas.get() + ".json")
    dat = [r['Date'] for r in db]
    mon = [r['Month'] for r in db]
    subject = [r['Subject'] for r in db]
    for i in range(0, len(subject)):
        lb.insert(END, "Date:"+dat[i],"Month: "+mon[i],subject[i])
    lb.place(x=20, y=340)
def delExam(lb):
    db = TinyDB("Exam/Class " + clas.get() + ".json")
    exam = Query()
    db.remove(exam.Subject == lb.selection_get())
    showExam(lb)

openingFrom()
