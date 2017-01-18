from Tkinter import *
import tkFont, ttk, sys
import tkMessageBox
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename
from ttk import Combobox
fn=b0=ln=s0=b2=s2=cl=gc=ln=gen=""
d=m=y=y0=p0=y2=p2=yg=pg=0

def cancel_alert(t):
	tkMessageBox.askyesno("Quit","Are you sure, you want to quit?")
	if 'yes':
		t.destroy()


def  askonopenfile():
	name = askopenfilename(filetypes=(("Image Files", "*.jpg; *.png")))
	print name
	
	imag = Image.open(name)
	photo = ImageTk.PhotoImage(imag)
	img = Label(top,image=photo,width=20,height=20,padx=10,pady=10)
	img.grid(row=3,column=5)


top = Tk()
top.title("Personal/Academic Information")
top.resizable(width=FALSE,height=FALSE)
helv36 = tkFont.Font(family="Helvetica",size=10,weight="bold")
g = StringVar()

Label(top,text="PERSONAL INFORMATION",font="helv36").grid(row=0,columnspan=3)

Label(top,text="FIRST NAME",pady=10,padx=5).grid(row=1,column=0)

first_name = Entry(top,width=20)

first_name.grid(row=1,column=1,columnspan=2)

Label(top,text="LAST NAME",pady=10,padx=5).grid(row=2,column=0)

last_name = Entry(top,width=30)
last_name.grid(row=2,column=1,columnspan=2)

img = Canvas(top,bg="black",width=50, height=50)
img.grid(row=3,column=5)

photo_upload = Button(top,text="Upload Photo",command=askonopenfile)
photo_upload.grid(row=4,column=5)

Label(top,text="DATE OF BIRTH",pady=10,padx=5).grid(row=3,column=0)

day = Spinbox(top,from_=1,to=31,width=2)
day.grid(row=3,column=1)



month = Spinbox(top,from_=1,to=12,width=2)
month.grid(row=3,column=2)


year = Spinbox(top,from_=1900,to=2016,width=4)
year.grid(row=3,column=3)


Label(top,text="GENDER",pady=10,padx=5).grid(row=4,column=0,rowspan=3)

genderm = Radiobutton(top,text="Male",value="male",indicatoron = 0,variable=g)
genderm.grid(row=4,column=1)

genderf = Radiobutton(top,text="Female",value="female",indicatoron = 0,variable=g)
genderf.grid(row=5,column=1)

gendero = Radiobutton(top,text="Others",value="others",indicatoron = 0,variable=g)
gendero.grid(row=6,column=1)

Label(top,text="ACADEMIC QUALIFICATION",font="helv36").grid(row=7,columnspan=4,rowspan=3)

Label(top,text="HIGH SCHOOL").grid(row=10,column=2,rowspan=2)

yearof10pass = Spinbox(top,from_=1950,to=2016,width=4)
yearof10pass.grid(row=12,column=0)



Label(top,text="Year of Passing").grid(row=13,column=0)

board_10 = Combobox(top,values ="CBSE UP_BOARD ICSE")
board_10.grid(row=12,column=1)

Label(top,text="Board").grid(row=13,column=1)

perc10 = Spinbox(top,from_=1,width=2, to=99)
perc10.grid(row=12,column=2)


Label(top,text="Percentage").grid(row=13,column=2)

school10_name = Entry(top)

school10_name.grid(row=12,column=3)

Label(top,text="School Name").grid(row=13,column=3)

Label(top,text="INTERMEDIATE").grid(row=14,column=2,rowspan=2)

yearof12pass = Spinbox(top,from_=1950,to=2016,width=4)
yearof12pass.grid(row=16,column=0)
y2 = int(yearof12pass.get())

Label(top,text="Year of Passing").grid(row=17,column=0)

board_12 = Combobox(top,values="CBSE UP_BOARD ICSE")
board_12.grid(row=16,column=1)

Label(top,text="Board").grid(row=17,column=1)

perc12 = Spinbox(top,width=2,from_=1,to=99)
perc12.grid(row=16,column=2)
p2 = perc12.get()


Label(top,text="Percentage").grid(row=17,column=2)

school12_name = Entry(top)
school12_name.grid(row=16,column=3)

Label(top,text="School Name").grid(row=17,column=3)

Label(top,text="GRADUATION").grid(row=19,column=2,rowspan=2)

yearofgradpass = Spinbox(top,from_=1950,to=2020,width=4)
yearofgradpass.grid(row=21,column=0)
yg = int(yearofgradpass.get())

Label(top,text="Year of Passing").grid(row=22,column=0)

course_list = Combobox(top,values ="B.Tech B.Sc B.Com B.A.")
course_list.grid(row=21,column=1)

Label(top,text="Course").grid(row=22,column=1)

percgrad = Spinbox(top,from_=1,to=99,width=2)
percgrad.grid(row=21,column=2)
pg = percgrad.get()

Label(top,text="Percentage").grid(row=22,column=2)

grad_college_name = Entry(top)
grad_college_name.grid(row=21,column=3)

Label(top,text="College/University Name").grid(row=22,column=3)





def ask_tech_page():
	
	month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
	next = tkMessageBox.askyesno("Proceed for More details","Are you done with the details, Proceed to next page")
	d = int(day.get())
	m = int(month.get())
	y = int(year.get())
	 
	
	if 'yes':

		if y%4 == 0:
			if y%100 != 0 or y%400 == 0:
				month_days[m-1] = 29


		if first_name.get().isspace() or first_name.get()=="":
			tkMessageBox.showwarning("Error","First Name space left blank!")

		
			
	
		elif first_name.get().isalpha() == False:

			tkMessageBox.showwarning("Error","Only Characters allowed in First Name!")
	
		
	
		elif last_name.get().isspace() or last_name.get()=="":
	
			tkMessageBox.showwarning("Error","Last Name space left blank!")
	
		elif last_name.get().isalpha() == False:
	
			tkMessageBox.showwarning("Error","Only Characters allowed in Last Name!")
	
		
	
		elif perc10.get().isspace() or perc10.get()=="":
	
			tkMessageBox.showwarning("Error","10th Percentage space left blank!")
	

		elif perc10.get().isdigit() == False:
	
			tkMessageBox.showwarning("Error","Only Numbers allowed in Percentage!")
	
	
		elif perc12.get().isspace() or perc12.get() == "":
	
			tkMessageBox.showwarning("Error","12th Percentage space left blank!")
	
		elif perc12.get().isdigit() == False:
	
			tkMessageBox.showwarning("Error","Only Numbers allowed in Percentage!")
	


		elif percgrad.get().isspace() or percgrad.get() == "":
	
			tkMessageBox.showwarning("Error","Graduation Percentage space left blank!")
	

		elif percgrad.get().isdigit() == False:
	
			tkMessageBox.showwarning("Error","Only Numbers allowed in Percentage!")
	
	
		elif school10_name.get().isspace() or school10_name.get() == "":
	

			tkMessageBox.showwarning("Error","10th School Name space left blank!")
	

		elif school10_name.get().isalpha() == False:
	
			tkMessageBox.showwarning("Error","Only Characters allowed in School Name!")

	
		elif school12_name.get().isspace() or school12_name.get() == "":
	
			tkMessageBox.showwarning("Error","12th School Name space left blank!")
	
		elif school12_name.get().isalpha() == False:
	
			tkMessageBox.showwarning("Error","Only Characters allowed in School Name!")
	
	
		elif grad_college_name.get().isspace() or grad_college_name.get() == "":
	
			tkMessageBox.showwarning("Error","Graduation College Name space left blank!")
	
		elif grad_college_name.get().isalpha() == False:
	
			tkMessageBox.showwarning("Error","Only Characters allowed in College Name!")

		
		elif 	d > month_days[m-1]:
			tkMessageBox.showwarning("Error","Wrong Number of days selected for respective month!")

		else:
			ln = last_name.get()
			fn = first_name.get()
			b0 = board_10.get()
			course_list1 = course_list.get()
			gen = g.get()
			y0 = int(yearof10pass.get())
			p0 = int(perc10.get())
			s0 = school10_name.get()
			y2 = int(yearof12pass.get())
			b2 = board_12.get()
			s2 = school12_name.get()
			p2 = int(perc12.get())
			yg = int(yearofgradpass.get())
			pg = int(percgrad.get())
			gc = grad_college_name.get()
			d = int(day.get())
			m = int(month.get())
			y = int(year.get())

			tech_window(fn,ln,gen,d,m,y,y0,b0,s0,p0,y2,b2,s2,p2,yg,course_list1,pg,gc)	
		


		



		

next_page = Button(top,text="Next",command=ask_tech_page)
next_page.grid(row=25,padx=10,column=5)
cancel_but = Button(top,text="Cancel",command=lambda: cancel_alert(top))
cancel_but.grid(row=25,column=6)

def tech_window(first_name,last_name,gen,d,m,y,y0,board_10,school10_name,perc10,y2,board_12,school12_name,perc12,yg,course_list1,percgrad,grad_college_name):
	
	print first_name,last_name,gen,d,m,y,y0,board_10,school10_name,perc10,y2,board_12,school12_name,perc12,yg,course_list1,percgrad,grad_college_name
	top.destroy()
	top_1 = Tk()
	top_1.title("Technical/Project Information")

	top_1.resizable(width=FALSE,height=FALSE)

	Label(top_1,text="TECHNICAL PERFORMA/WORK",font=helv36).grid(row=0,column=2)
	Label(top_1,text="PROJECT WORK").grid(row=2,column=2)
	project_work = Text(width=30,height=5)
	project_work.grid(row=4,column=2)
	Label(top_1,text="INDUSTRIAL TRAINING").grid(row=6,column=2)
	indus_train = Text(width=30,height=5)
	indus_train.grid(row=8,column=2)
	Label(top_1,text="CERTIFICATIONS").grid(row=10,column=2)
	certi = Text(width=30,height=5)
	certi.grid(row=12,column=2)
	cancel_but = Button(top_1,text="Cancel",command=lambda: cancel_alert(top_1))
	cancel_but.grid(row=14,column=6)
	next_page = Button(top_1,text="Next")
	next_page.grid(row=14,padx=10,column=5)

	top_1.mainloop()

top.mainloop()

