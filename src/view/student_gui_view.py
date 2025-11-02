import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk #draw horizontal
from functools import partial  #bind two arguments
from src.utils.grading import grade_for, average_mark, is_pass_final
from src.controllers.student_gui_controller import login,register,password_confirm
from src.controllers.subject_gui_controller import subject_enrol,subject_remove
class MainGUI:
    #static variables need init after class MainGUI init
 
    def __init__(self):#initial the frame of main GUI, or it will run(open window) at begin
        MainGUI.bg1="#1E00E2"
        MainGUI.bg2="#B205F1"
        MainGUI.bg3="#1ee71b"
        MainGUI.fg1="white"
        MainGUI.root=tk.Tk()
        MainGUI.root.geometry("900x500")
        MainGUI.root.title('Welcome to UTS')
        MainGUI.root.configure(bg=self.bg1)
        MainGUI.root.resizable(True,True)
        MainGUI.main_frame(MainGUI)#use static variables at whole process, need pass self(MainGUI)
        
    def main_frame(self):    
        self.clear_frame(self.root)
        self.box=tk.LabelFrame(self.root,text='Login your account',bg=self.bg1,fg=self.fg1,font=('Times New Roman',14))
        self.box.place(rely=0.5,relx=0.5,anchor='center')
        #create Label  emailLbl
        emailLbl=tk.Label(self.box, text='Email/Student ID:',justify='left',bg=self.bg2,fg=self.fg1,font=('Times New Roman', 16,'bold'))
        #locate Label  emailLbl
        emailLbl.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
        self.emailText = tk.StringVar()
        #create Entry  emailField
        emailField = tk.Entry(self.box, textvariable=self.emailText,font=('Times New Roman', 16,'bold'))
        #locate emailField
        emailField.grid(column=1, row=0, padx=10, pady=10)
        #cursor focus
        emailField.focus()
        
        passwordLbl=tk.Label(self.box, text='Password:',bg=self.bg2,fg=self.fg1,font=('Times New Roman',16,'bold'))
        passwordLbl.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
        self.passwordText = tk.StringVar()
        passwordField = tk.Entry(self.box, textvariable=self.passwordText, show='*',font=('Times New Roman',16,'bold'))
        passwordField.grid(column=1, row=1, padx=10, pady=10)

        quitBtn = tk.Button(self.box, text='Quit', command=self.root.destroy,font=('Times New Roman',16,'bold'))
        quitBtn.grid(column=0, row=3, sticky=tk.W, padx=10, pady=20)
        registerBtn = tk.Button(self.box,text='Register', command=RegisterGUI,font=('Times New Roman',16,'bold'))
        registerBtn.grid(column=0, row=3, padx=10, pady=20, sticky=tk.E)
        loginBtn = tk.Button(self.box,text='Login', command=partial(login,MainGUI,on_success=lambda student: SubjectGUI(student),
                on_failure=lambda msg: mb.showerror(title='Login Error', message=msg)),font=('Times New Roman',16,'bold'))
        loginBtn.grid(column=1, row=3, padx=10, pady=10)

    @classmethod  #static function
    def clear_frame(self,frame):
        #clear all widgets
        for widget in frame.winfo_children():
            widget.destroy()
           
class RegisterGUI:
    def __init__(self):#initial the frame of Register GUI
        MainGUI.clear_frame(MainGUI.root)
        self.box=tk.LabelFrame(MainGUI.root,text='Welcome to Register',bg=MainGUI.bg1,fg=MainGUI.fg1,font=('Times New Roman',14))
        self.box.place(rely=0.5,relx=0.5,anchor='center')

        nameLbl=tk.Label(self.box, text='Name: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        nameLbl.grid(column=0, row=0, padx=20, pady=10, sticky=tk.W)  
        self.nameText = tk.StringVar()
        nameField = tk.Entry(self.box, textvariable=self.nameText,font=('Times New Roman',16))
        nameField.grid(column=1, row=0, padx=10, pady=10)
        nameField.focus()
        
        emailLbl=tk.Label(self.box, text='Email: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        emailLbl.grid(column=0, row=1, padx=20, pady=10, sticky=tk.W)
        self.emailText = tk.StringVar()
        emailField = tk.Entry(self.box, textvariable=self.emailText,font=('Times New Roman',16))
        emailField.grid(column=1, row=1, padx=10, pady=10)

        passwordLbl=tk.Label(self.box, text='Password: ', bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman',16,'bold'))
        passwordLbl.grid(column=0, row=2, padx=20, pady=10, sticky=tk.W)
        self.passwordText = tk.StringVar()
        passwordField = tk.Entry(self.box, textvariable=self.passwordText, show='*',font=('Times New Roman',16))
        passwordField.grid(column=1, row=2, padx=10, pady=10)

        password2Lbl=tk.Label(self.box, text='Password Again: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        password2Lbl.grid(column=0, row=3, padx=20, pady=10, sticky=tk.W)
        self.password2Text = tk.StringVar()
        password2Field = tk.Entry(self.box, textvariable=self.password2Text, show='*',font=('Times New Roman',16))
        password2Field.grid(column=1, row=3, padx=10, pady=10)
        
        quitBtn = tk.Button(self.box, text='Quit', command=MainGUI.root.destroy,font=('Times New Roman',16,'bold'))
        quitBtn.grid(column=0, row=4, sticky=tk.W, padx=10, pady=10)
        backBtn = tk.Button(self.box, text='Back', command=partial(MainGUI.main_frame,MainGUI),font=('Times New Roman',16,'bold'))
        backBtn.grid(column=0, row=4, sticky=tk.E, padx=10, pady=10)
        registerBtn = tk.Button(self.box,text='Register', command=partial(register,self,on_success=lambda msg: mb.showinfo(title='Regesiter Success', message=msg),
                on_failure=lambda msg: mb.showerror(title='Register Error', message=msg)),font=('Times New Roman',16,'bold'))
        registerBtn.grid(column=1, row=4, padx=10, pady=10)
   
class SubjectGUI:#initial the frame of Subject GUI (student enrol ,remove subject and change password)
    def __init__(self,student=None):
        MainGUI.clear_frame(MainGUI.root)
        self.student=student
        #left frame, menu, include Manage Subject(view, enrol and remove subject) and Change Password
        menu_frame = tk.Frame(MainGUI.root, width=200, relief=tk.RAISED, borderwidth=3, bg=MainGUI.bg3)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10,5), pady=20)
        #right frame
        self.content_frame = tk.Frame(MainGUI.root, width=700, relief=tk.SUNKEN, borderwidth=3, bg=MainGUI.bg2)
        self.content_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10,5), pady=20)

        studentMsg=tk.Message(menu_frame, text=f'Welcome:\n{self.student.id}\n{self.student.name}',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        studentMsg.grid(column=0, row=0, padx=10, pady=20)
        subjectBtn = tk.Button(menu_frame,text='Manage Subject',width=13, command=self.subject_view,font=('Times New Roman',16,'bold'))
        subjectBtn.grid(column=0, row=1, padx=10, pady=20)
        passwordBtn = tk.Button(menu_frame,text='Change Password',width=13, command=self.password_change,font=('Times New Roman',16,'bold'))
        passwordBtn.grid(column=0, row=2, padx=10, pady=20)
        
        backBtn = tk.Button(menu_frame, text='Back',width=13, command=partial(MainGUI.main_frame,MainGUI),font=('Times New Roman',16,'bold'))
        backBtn.grid(column=0, row=5, padx=10, pady=20)
        quitBtn = tk.Button(menu_frame, text='Quit',width=13, command=MainGUI.root.destroy,font=('Times New Roman',16,'bold'))
        quitBtn.grid(column=0, row=6,  padx=10, pady=20)
        
    def subject_view(self):#The frame of subject view GUI, include enrol and remove subject
        MainGUI.clear_frame(self.content_frame)
        rownum=0
        idLbl=tk.Label(self.content_frame, width=10, text="Subject.ID",justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        idLbl.grid(column=0, row=rownum, padx=5, pady=5)
        markLbl=tk.Label(self.content_frame, width=10, text="Mark",justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        markLbl.grid(column=1, row=rownum, padx=5, pady=5)
        gradeLbl=tk.Label(self.content_frame, width=10, text="Grade",justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        gradeLbl.grid(column=2, row=rownum, padx=5, pady=5)
        operateLbl=tk.Label(self.content_frame, width=15, text="Operation",justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        operateLbl.grid(column=3, row=rownum, padx=5, pady=5)
            
        for subject in self.student.subjects:
            rownum+=1
            idLbl=tk.Label(self.content_frame, width=10, text=subject['id'],justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16))
            idLbl.grid(column=0, row=rownum, padx=5, pady=5)
            markLbl=tk.Label(self.content_frame, width=10, text=subject['mark'],justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16))
            markLbl.grid(column=1, row=rownum, padx=5, pady=5)
            gradeLbl=tk.Label(self.content_frame, width=10, text=subject['grade'],justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16))
            gradeLbl.grid(column=2, row=rownum, padx=5, pady=5)
            removeBtn = tk.Button(self.content_frame,width=15, text='Remove Subject', command=partial(subject_remove,self,subject['id'],on_success=lambda msg: (mb.showinfo(title='Remove Success', message=msg),self.subject_view())),font=('Times New Roman',16))
            removeBtn.grid(column=3, row=rownum, padx=5, pady=5)
        
        #draw horizontal
        rownum+=1
        separator=ttk.Separator(self.content_frame, orient='horizontal')
        separator.grid(column=0, row=rownum, columnspan=4, sticky='ew', padx=10)
        rownum+=1
        if self.student.subjects:
            avg=average_mark(self.student.subjects)
            avg_grade=grade_for(int(round(avg)))
        else:
            avg=0
            avg_grade="N/A"
        if len(self.student.subjects)<4:
            pass_or_fail='In Progress'
        elif is_pass_final(self.student.subjects):
            pass_or_fail='PASS'
        else:
            pass_or_fail='FAIL'
        idLbl=tk.Label(self.content_frame, width=10, text="Average",justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        idLbl.grid(column=0, row=rownum, padx=5, pady=5)
        markLbl=tk.Label(self.content_frame, width=10, text=avg,justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        markLbl.grid(column=1, row=rownum, padx=5, pady=5)
        gradeLbl=tk.Label(self.content_frame, width=10, text=avg_grade,justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        gradeLbl.grid(column=2, row=rownum, padx=5, pady=5)
        categoryLbl=tk.Label(self.content_frame, width=10, text=pass_or_fail,justify='right',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        categoryLbl.grid(column=3, row=rownum, padx=5, pady=5)
        
        rownum+=1
        enrolBtn = tk.Button(self.content_frame,text='Enrol Subject',width=12, command=partial(subject_enrol,self,on_success=lambda msg: (mb.showinfo(title='Enrol Success', message=msg),self.subject_view())
            ,on_failure=lambda msg: mb.showerror(title='Enrol Error', message=msg)),font=('Times New Roman',16)) #go to subject_view again
        enrolBtn.grid(column=1, row=rownum, columnspan=2, padx=12, pady=20)
        
    def password_change(self):#The frame of password change GUI
        MainGUI.clear_frame(self.content_frame)
        self.box=tk.LabelFrame(self.content_frame,text='Change Password',bg=MainGUI.bg1,fg=MainGUI.fg1,font=('Times New Roman',14))
        self.box.place(rely=0.5,relx=0.5,anchor='center')
        currentLbl=tk.Label(self.box, text='Current Password: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        currentLbl.grid(column=0, row=0, padx=20, pady=10, sticky=tk.W)
        self.currentText = tk.StringVar()
        currentField = tk.Entry(self.box, textvariable=self.currentText, show='*',font=('Times New Roman',16))
        currentField.grid(column=1, row=0, padx=10, pady=10)
        currentField.focus()
        newLbl=tk.Label(self.box, text='New Password: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        newLbl.grid(column=0, row=1, padx=20, pady=10, sticky=tk.W)
        self.newText = tk.StringVar()
        newField = tk.Entry(self.box, textvariable=self.newText, show='*',font=('Times New Roman',16))
        newField.grid(column=1, row=1, padx=10, pady=10)
        new2Lbl=tk.Label(self.box, text='Password Again: ',justify='left',bg=MainGUI.bg2,fg=MainGUI.fg1,font=('Times New Roman', 16,'bold'))
        new2Lbl.grid(column=0, row=2, padx=20, pady=10, sticky=tk.W)
        self.new2Text = tk.StringVar()
        new2Field = tk.Entry(self.box, textvariable=self.new2Text, show='*',font=('Times New Roman',16))
        new2Field.grid(column=1, row=2, padx=10, pady=10)
        changeBtn = tk.Button(self.box,text='Change Password', command=partial(password_confirm,self,on_success=lambda msg: mb.showinfo(title='Change Password Success', message=msg),
                on_failure=lambda msg: mb.showerror(title='Change Password Error', message=msg)),font=('Times New Roman',16))
        changeBtn.grid(column=1, row=3, padx=10, pady=20)
        
        
def run_student_gui_main(): 
    MainGUI()
    MainGUI.root.mainloop()


