import tkinter as tk   # python3
from tkinter import *
from teststuff import readCSV
from teststuff import staffCSV
from tkinter.messagebox import showerror
import string
#import Tkinter as tk   # python

TITLE_FONT = ("Helvetica", 18, "bold")

class TutoringDatabase(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, StudentInterface, TutorInterface, AdminInterface, StudentManager):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tutoring Database", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Student Login", width=12,
                            command=lambda: controller.show_frame("StudentInterface"))
        button2 = tk.Button(self, text="Tutor Login", width=12,
                            command=lambda: controller.show_frame("TutorInterface"))
        button3 = tk.Button(self, text="Admin Login", width=12,
                            command=lambda: controller.show_frame("AdminInterface"))
        button1.pack(pady=5)
        button2.pack(pady=5)
        button3.pack(pady=5)


'''class StudentLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Student Login Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Back", pady=5, width=10,
                           command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(self, text="Login", pady=5, width=10,
                           command=lambda: controller.show_frame("StudentInterface"))
        button1.pack(pady=5)
        button2.pack(pady=5)


class TutorLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Tutor Login Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Back", pady=5, width=10,
                           command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(self, text="Login", pady=5, width=10,
                           command=lambda: controller.show_frame("TutorInterface"))
        button1.pack(pady=5)
        button2.pack(pady=5)

class AdminLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Admin Login Page", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Back", pady=5, width=10,
                           command=lambda: controller.show_frame("LoginPage"))
        button2 = tk.Button(self, text="Login", pady=5, width=10,
                           command=lambda: controller.show_frame("AdminInterface"))
        button1.pack(pady=5)
        button2.pack(pady=5)'''

class StudentInterface(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def loginSubmit():
            for item in storedStudents:
                if userInput.get() == item[0] and passInput.get() == storedStudents[storedStudents.index(item)][1][0][8]:
                    loadStudentInterface(storedStudents.index(item))
                    return
            showerror("Login error", "Incorrect username or password")

        storedStudents = readCSV("student_lists.csv")
        labelTitle = tk.Label(self, text="Student Interface", font=TITLE_FONT)
        labelUser = tk.Label(self, text="Username")
        labelPass = tk.Label(self, text="Password")
        userInput = tk.Entry(self)
        passInput = tk.Entry(self, show="*")
        logButton = tk.Button(self, text="Login", command=loginSubmit)
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("LoginPage"))
        labelTitle.grid(column=1)
        labelUser.grid(row=1, column=0, sticky=E)
        userInput.grid(row=1, column=1)
        logButton.grid(row=3, column=1)
        backButton.grid(row=3, column=0)
        labelPass.grid(row=2, column=0, sticky=E)
        passInput.grid(row=2, column=1)

        def loadStudentInterface(x):
            labelUser.grid_forget()
            labelPass.grid_forget()
            userInput.grid_forget()
            passInput.grid_forget()
            logButton.grid_forget()
            backButton.grid_forget()      
            label1 = tk.Label(self, text="Student Code: ")
            label2 = tk.Label(self, text="Surname: ")
            label3 = tk.Label(self, text="Forename: ")
            label4 = tk.Label(self, text="Middlename(s): ")
            label5 = tk.Label(self, text="Tutor: ")
            label6 = tk.Label(self, text="Course Code: ")
            label7 = tk.Label(self, text="Academic Year: ")
            label8 = tk.Label(self, text="Univeristy Email: ")

            labelCode = tk.Label(self, text=storedStudents[x][1][0][0])
            labelSur = tk.Label(self, text=storedStudents[x][1][0][1])
            labelFore1 = tk.Label(self, text=storedStudents[x][1][0][2])
            labelFore2 = tk.Label(self, text=storedStudents[x][1][0][3])
            labelTutor = tk.Label(self, text=storedStudents[x][1][0][4])
            labelCourse = tk.Label(self, text=storedStudents[x][1][0][5])
            labelYear = tk.Label(self, text=storedStudents[x][1][0][6])
            labelMail = tk.Label(self, text=storedStudents[x][1][0][7])

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)
            label5.grid(row=5, column=0, sticky=E)
            label6.grid(row=6, column=0, sticky=E)
            label7.grid(row=7, column=0, sticky=E)
            label8.grid(row=8, column=0, sticky=E)
            labelCode.grid(row=1, column=1, sticky=W, padx=10)
            labelSur.grid(row=2, column=1, sticky=W, padx=10)
            labelFore1.grid(row=3, column=1, sticky=W, padx=10)
            labelFore2.grid(row=4, column=1, sticky=W, padx=10)
            labelTutor.grid(row=5, column=1, sticky=W, padx=10)
            labelCourse.grid(row=6, column=1, sticky=W, padx=10)
            labelYear.grid(row=7, column=1, sticky=W, padx=10)
            labelMail.grid(row=8, column=1, sticky=W, padx=10)

            button = tk.Button(self, text="Logout", padx=5, width=10,
                           command=lambda: controller.show_frame("LoginPage"))
            button.grid(row=9, column=0, pady=5)

class TutorInterface(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def loginSubmit():
            for item in storedStaff:
                if userInput.get() == item[0] and passInput.get() == storedStaff[storedStaff.index(item)][1][0][8]:
                    loadStaffInterface(storedStaff.index(item))
                    return
            showerror("Login error", "Incorrect username or password")

        storedStaff = readCSV("staff_lists.csv")
        labelTitle = tk.Label(self, text="Tutor Interface", font=TITLE_FONT)
        labelUser = tk.Label(self, text="Username")
        labelPass = tk.Label(self, text="Password")
        userInput = tk.Entry(self)
        passInput = tk.Entry(self, show="*")
        logButton = tk.Button(self, text="Login", command=loginSubmit)
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("LoginPage"))
        labelTitle.grid(column=1)
        labelUser.grid(row=1, column=0, sticky=E)
        userInput.grid(row=1, column=1)
        logButton.grid(row=3, column=1)
        backButton.grid(row=3, column=0)
        labelPass.grid(row=2, column=0, sticky=E)
        passInput.grid(row=2, column=1)

        def loadStaffInterface(x):
            labelUser.grid_forget()
            labelPass.grid_forget()
            userInput.grid_forget()
            passInput.grid_forget()
            logButton.grid_forget()
            backButton.grid_forget()      
            label1 = tk.Label(self, text="Staff Code: ")
            label2 = tk.Label(self, text="Surname: ")
            label3 = tk.Label(self, text="Forename: ")
            label4 = tk.Label(self, text="Middlename(s): ")
            label5 = tk.Label(self, text="Tutor Group: ")
            label6 = tk.Label(self, text="Course: ")
            label7 = tk.Label(self, text="Room: ")
            label8 = tk.Label(self, text="Univeristy Email: ")

            labelCode = tk.Label(self, text=storedStaff[x][1][0][0])
            labelSur = tk.Label(self, text=storedStaff[x][1][0][1])
            labelFore1 = tk.Label(self, text=storedStaff[x][1][0][2])
            labelFore2 = tk.Label(self, text=storedStaff[x][1][0][3])
            labelTutor = tk.Label(self, text=storedStaff[x][1][0][4])
            labelCourse = tk.Label(self, text=storedStaff[x][1][0][5])
            labelYear = tk.Label(self, text=storedStaff[x][1][0][6])
            labelMail = tk.Label(self, text=storedStaff[x][1][0][7])

            label1.grid(row=1, column=0, sticky=E)
            label2.grid(row=2, column=0, sticky=E)
            label3.grid(row=3, column=0, sticky=E)
            label4.grid(row=4, column=0, sticky=E)
            label5.grid(row=5, column=0, sticky=E)
            label6.grid(row=6, column=0, sticky=E)
            label7.grid(row=7, column=0, sticky=E)
            label8.grid(row=8, column=0, sticky=E)
            labelCode.grid(row=1, column=1, sticky=W, padx=10)
            labelSur.grid(row=2, column=1, sticky=W, padx=10)
            labelFore1.grid(row=3, column=1, sticky=W, padx=10)
            labelFore2.grid(row=4, column=1, sticky=W, padx=10)
            labelTutor.grid(row=5, column=1, sticky=W, padx=10)
            labelCourse.grid(row=6, column=1, sticky=W, padx=10)
            labelYear.grid(row=7, column=1, sticky=W, padx=10)
            labelMail.grid(row=8, column=1, sticky=W, padx=10)

            button = tk.Button(self, text="Logout", padx=5, width=10,
                           command=lambda: controller.show_frame("LoginPage"))
            button.grid(row=9, column=0, pady=5)


class AdminInterface(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def loginSubmit():
            adminAccess = "power2theAdmin"
            if passInput.get() == adminAccess:
                loadAdminInterface()
                return
            showerror("Login error", "Incorrect password")

        labelTitle = tk.Label(self, text="Admin Interface", font=TITLE_FONT)
        labelPass = tk.Label(self, text="Password")
        passInput = tk.Entry(self, show="*")
        logButton = tk.Button(self, text="Login", command=loginSubmit)
        backButton = tk.Button(self, text="Back", command=lambda: controller.show_frame("LoginPage"))
        labelTitle.grid(column=1)
        logButton.grid(row=3, column=1)
        backButton.grid(row=3, column=0)
        labelPass.grid(row=2, column=0, sticky=E)
        passInput.grid(row=2, column=1)

        def loadAdminInterface():
            labelPass.grid_forget()
            passInput.grid_forget()
            logButton.grid_forget()
            backButton.grid_forget()
            label1 = tk.Label(self, text="ADMIN ACCESS GRANTED")
            label1.grid(row=1, column=1)

            logout = tk.Button(self, text="Logout", padx=5, width=15,
                           command=lambda: controller.show_frame("LoginPage"))
            studentManager = tk.Button(self, text="Student Manager", padx=5, width=15,
                           command=lambda: controller.show_frame("StudentManager"))
            tutorManager = tk.Button(self, text="Tutor Manager", padx=5, width=15,
                           command=lambda: controller.show_frame(""))
            groupManager = tk.Button(self, text="Group Manager", padx=5, width=15,
                           command=lambda: controller.show_frame(""))
            viewGroups = tk.Button(self, text="View Groups", padx=5, width=15,
                           command=lambda: controller.show_frame(""))

            logout.grid(row=2, column=1, pady=5)
            studentManager.grid(row=3, column=1, pady=5)
            tutorManager.grid(row=4, column=1, pady=5)
            groupManager.grid(row=5, column=1, pady=5)
            viewGroups.grid(row=6, column=1, pady=5)


class StudentManager(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        storedStudents = readCSV("student_lists.csv")

        def displayStudent(selection):
            tester = str(studentList.curselection())
            tester1 = studentList.get(studentList.curselection())
            print(tester1)

        labelTitle = tk.Label(self, text="Student Management Page", font=TITLE_FONT)
        studentList = Listbox(self)

        for item in storedStudents:
            x=storedStudents[storedStudents.index(item)][1][0][0]
            studentList.insert(0, x)

        labelTitle.grid(row=0, column=1)
        studentList.grid(row=1, column=1)
        studentList.bind('<<ListboxSelect>>', displayStudent)



if __name__ == "__main__":
    app = TutoringDatabase()
    app.configure(background="")
    app.mainloop()