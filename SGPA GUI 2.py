from tkinter import *

root = Tk()
root.minsize(950,400)

#***Functions***

      
def errors(ISA1,ISA2,ESA,ASSIGN=DoubleVar(root,value=0.0)):
    for i in (ISA1,ISA2,ESA,ASSIGN):
        try:
            i = float(i.get())
        except:
            message = Toplevel()
            message.minsize(50,50)
            error1 = Label(message, text="   PLEASE ENTER ONLY NUMERIC DATA! / DONT LEAVE ANY CELL BLANK  ").pack()
            return 0;
    """
    The variables ma_isa1 etc are all Vairable() objects and hence in order to access the value in them we must use
    the .get() method
    additionally, the data accepted by the variable() object implicitly takes it as a string just as we would when using
    the input function
    """
    ISA1 = float(ISA1.get())
    ISA2 = float(ISA2.get())
    ESA  = float(ESA.get())
    ASSIGN = float(ASSIGN.get())
    
    for i in (ISA1,ISA2):
        if i > 40: 
            message = Toplevel()
            message.minsize(50,50)
            message.title('Error')
            error1 = Label(message, text=" ISA MARKS ARE OUT OF 40 ").pack()
            return 0;
        
    if ESA > 100.0:
        message = Toplevel()
        message.minsize(100,100)
        message.title('Error')
        error1 = Label(message, text=" ESA MARKS ARE OUT OF 100 ").pack()
        return 0;
    
    if ASSIGN > 10.0:
        message = Toplevel()
        message.title('Error')
        message.minsize(100,100)
        error1 = Label(message, text=" ASSIGNMENT MARKS ARE OUT OF 10 ").pack()
        return 0; 
    

    return 1;

def sub_gpa(credits,ISA1,ISA2,ESA,text_box,ASSIGN=Variable(value=0.0),inc = True):
    
    ISA1 = float(ISA1.get())
    ISA2 = float(ISA2.get())
    ESA  = float(ESA.get())
    ASSIGN = float(ASSIGN.get())
    
    if inc:
        ISA1 = (ISA1/40)*15
        ISA2 = (ISA2/40)*15
        pre_final = ISA1+ISA2+ASSIGN
    else:
        ISA1 = (ISA1/40)*20
        ISA2 = (ISA2/40)*20
        pre_final = ISA1+ISA2
    ESA = (ESA/100)*60
    sub_final = pre_final + ESA
    return sub_final 

def result_cal(res_show):
    math_marks = sub_gpa(credits=4,ISA1=ma_isa1,ISA2=ma_isa2,ESA=ma_esa,text_box=txt,ASSIGN=ma_assign)
    res_show = res_show + 'Math marks are ' + str(math_marks) + '\n'
    computer_marks = sub_gpa(credits=4,ISA1=c_isa1,ISA2=c_isa2,text_box=txt,ESA=c_esa,inc=False)
    res_show = res_show + 'Computer marks are ' + str(computer_marks) + '\n'
    ec_eee_marks = sub_gpa(credits=4,ISA1=e_isa1,ISA2=e_isa2,ESA=e_esa,text_box=txt,ASSIGN=e_assign,)
    res_show = res_show + 'EEE/EC marks are ' + str(ec_eee_marks) + '\n'
    bio_cad_marks = sub_gpa(credits=2,ISA1=bc_isa1,ISA2=bc_isa2,text_box=txt,ESA=bc_esa,inc=False)
    res_show = res_show + 'Biology/CAD marks are ' + str(bio_cad_marks) + '\n'
    total = computer_marks + math_marks + ec_eee_marks + bio_cad_marks
    return (total,res_show,1);


def show(text_box,res):
     text_box.config(state='normal')
     text_box.delete('1.0',END) 
     if errors(ISA1=ma_isa1,ISA2=ma_isa2,ESA=ma_esa,ASSIGN=ma_assign) and errors(ISA1=c_isa1,ISA2=c_isa2,ESA=c_esa) and errors(ISA1=e_isa1,ISA2=e_isa2,ESA=e_esa,ASSIGN=e_assign) and errors(ISA1=m_isa1,ISA2=m_isa2,ESA=m_esa,ASSIGN=m_assign) and errors(ISA1=bc_isa1,ISA2=bc_isa2,ESA=bc_esa):
        final = result_cal(res)
        res = final[1] + 'The total score is ' + str(final[0]) 
        text_box.insert(chars=str(res),index='1.0')
        text_box.config(state='disable')


        
# ***GUI Contruction***
"""
When using the grid() method in tkinter the row number only signifies the order the widgets are stacked in.
Hence a widget in row 200 will be directly under a widget in row 1. This does not apply to columns. 
In order to add splazing between widgets we used the padx and pady arguments in the grid  method
"""
header = Label(root,text="Approximate SGPA Calculator - PES University",fg="blue").grid(row=0,columnspan=6,pady=25)
root.title('SGPA Calculator')

#Main headings
hr = 2
subject = Label(root,text="Subject").grid(row=hr,column=0)
credits = Label(root,text="Credits Assigned").grid(row=hr,column=1)
marks1 = Label(root,text="Marks Obtained in ISA1\nMax marks:40").grid(row=hr,column=2)
marks2 = Label(root,text="Marks Obtained in ISA2\nMax marks:40").grid(row=hr,column=3)
marks3 = Label(root,text="Marks Obtained in ESA\nMax marks:100").grid(row=hr,column=4)
marks4 = Label(root,text="Assesment Marks\nMax marks:10").grid(row=hr,column=5)


# Mathematics
mr = 3
ma_isa1 = Variable(value=0.0)
ma_isa2 = Variable(value=0.0)
ma_esa  = Variable(value=0.0)
ma_assign = Variable(value=0.0)
maths = Label(root,text="Maths").grid(row=mr,column=0)
ma_credits = Label(root,text="4").grid(row=mr,column=1)
ma1_entry = Entry(root,textvariable=ma_isa1).grid(row=mr,column=2)
ma2_entry = Entry(root,textvariable=ma_isa2).grid(row=mr,column=3)
ma2_entry = Entry(root,textvariable=ma_esa).grid(row=mr,column=4)
ma3_entry = Entry(root,textvariable=ma_assign).grid(row=mr,column=5)



#Electrical / Electronics
er = 4
e_isa1 = Variable(value=0.0)
e_isa2 = Variable(value=0.0)
e_esa  = Variable(value=0.0)
e_assign = Variable(value=0.0)
e_label  = Label(root,text="Electrical").grid(row=er,column=0)
e_credits = Label(root,text="4").grid(row=er,column=1)
e1_entry = Entry(root,textvariable=e_isa1).grid(row=er,column=2)
e2_entry = Entry(root,textvariable=e_isa2).grid(row=er,column=3)
e3_entry = Entry(root,textvariable=e_esa).grid(row=er,column=4)
e4_entry = Entry(root,textvariable=e_assign).grid(row=er,column=5)

#Mechanical / Mechanics
mmr = 5
m_isa1 = Variable(value=0.0)
m_isa2 = Variable(value=0.0)
m_esa  = Variable(value=0.0)
m_assign = Variable(value=0.0)
m_label  = Label(root,text="Mechanical").grid(row=mmr,column=0)
m_credits = Label(root,text="4").grid(row=5,column=1)
m1_entry = Entry(root,textvariable=m_isa1).grid(row=mmr,column=2)
m2_entry = Entry(root,textvariable=m_isa2).grid(row=mmr,column=3)
m3_entry = Entry(root,textvariable=m_esa).grid(row=mmr,column=4)
m4_entry = Entry(root,textvariable=m_assign).grid(row=mmr,column=5)

#Computer Science
cr = 6
c_isa1 = Variable(value=0.0)
c_isa2 = Variable(value=0.0)
c_esa  = Variable(value=0.0)
comp  = Label(root,text="Computer Science").grid(row=cr,column=0)
c_credits = Label(root,text="4").grid(row=cr,column=1)
c1_entry = Entry(root,textvariable=c_isa1).grid(row=cr,column=2)
c2_entry = Entry(root,textvariable=c_isa2).grid(row=cr,column=3)
c3_entry = Entry(root,textvariable=c_esa).grid(row=cr,column=4)
                                                  
#CAD / Biology  
bcr = 7
bc_isa1 = Variable(value=0.0)
bc_isa2 = Variable(value=0.0)
bc_esa  = Variable(value=0.0)
bc_label = Label(root,text="CAD / Biology").grid(row=bcr,column=0)
bc_credits = Label(root,text="2").grid(row=bcr,column=1)
bc1_entry = Entry(root,textvariable=bc_isa1).grid(row=bcr,column=2)
bc2_entry = Entry(root,textvariable=bc_isa2).grid(row=bcr,column=3)
bc3_entry = Entry(root,textvariable=bc_esa).grid(row=bcr,column=4)

                                                  
#Lab_marks = Label(root,text="Final Lab Assesment Marks").grid(row=8,column=2)

#clr = 9
#compL  = Label(root,text="Computer Laboratory").grid(row=clr,column=0)
#cl_credits = Label(root,text="1").grid(row=clr,column=1)
#cl1_entry = Entry(root).grid(row=clr,column=2)

#cpr = 10
#Lab  = Label(root,text="Physics Laboratory").grid(row=cpr,column=0)
#Lab_credits = Label(root,text="1").grid(row=cpr,column=1)
#Lab1_entry = Entry(root).grid(row=cpr,column=2)

report = str()
button_calc = Button(root,text='Calculate',command=lambda: show(txt,report)).grid(row=11,column = 5)


txt = Text(root,height = 6,width=70)
txt.grid(row=12, column=1,columnspan=3)


root.mainloop()






