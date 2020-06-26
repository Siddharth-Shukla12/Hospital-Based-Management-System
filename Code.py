from tkinter import *
import random
import time
import sqlite3
from tkinter import messagebox
r=Tk()
r.title("Hospital management System")
r.geometry("250x500")
r.configure(bg='black')
conn=sqlite3.connect('details2.db')
c=conn.cursor()
#c.execute("""CREATE TABLE details1 (first_name text,last_name text,address text,phone text,result text)""")
conn.commit()
conn.close()
def quit():
	messagebox.showinfo("Greetings","Thank you for Visiting")
	r.destroy()
def ab():
	p=Tk()
	p.title("Details")
	p.geometry("900x400")
	p.configure(bg="black")
	pl1=Label(p,font=('aria',15,'bold'),text='1.This is our project to demonstrate our designing skills\n2.This is based on how a hospital works.\n3.There are records and databases too.\n4.This is how we work efficiently and swiftly',fg='blue',bg='black')
	pl1.grid(row=0,column=0)
	p.mainloop()
def pro():
	z=Tk()
	z.geometry("500x800")
	z.title("Patient details")
	z.configure(bg="black")
	def reset():
		ze1.delete(0,END)
		ze2.delete(0,END)
		ze3.delete(0,END)
		ze4.delete(0,END)
	def submit():
		x=Tk()
		x.title("Reception")
		x.configure(bg="black")
		def price():

                    g=Tk()
                    g.title("Price details")
                    g.configure(bg='black')
                    i1 = Label(g, font=('aria', 15, 'bold'), text="Facilities", fg="blue", bg='black', bd=5)
                    i1.grid(row=0, column=0)
                    i2 = Label(g, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
                    i2.grid(row=0, column=2)
                    i3 = Label(g, font=('aria', 15, 'bold'), text="Cost", fg='blue', bg='black', anchor=W)
                    i3.grid(row=0, column=3)
                    i4 = Label(g, font=('aria', 15, 'bold'), text="rooms", fg="blue", bg='black', anchor=W)
                    i4.grid(row=1, column=0)
                    i5 = Label(g, font=('aria', 15, 'bold'), text="810", fg="blue", bg='black', anchor=W)
                    i5.grid(row=1, column=3)
                    i6 = Label(g, font=('aria', 15, 'bold'), text="Complicated Surgeries", fg="blue", bg='black', anchor=W)
                    i6.grid(row=2, column=0)
                    i7 = Label(g, font=('aria', 15, 'bold'), text="9000", fg="blue", bg='black', anchor=W)
                    i7.grid(row=2, column=3)
                    i8 = Label(g, font=('aria', 15, 'bold'), text="Weak Medicines", fg="blue", bg='black', anchor=W)
                    i8.grid(row=3, column=0)
                    i9 = Label(g, font=('aria', 15, 'bold'), text="50", fg="blue", bg='black', anchor=W)
                    i9.grid(row=3, column=3)
                    i10 = Label(g, font=('aria', 15, 'bold'), text="Strong medicines", fg="blue", bg='black', anchor=W)
                    i10.grid(row=4, column=0)
                    i11 = Label(g, font=('aria', 15, 'bold'), text="200", fg="blue", bg='black', anchor=W)
                    i11.grid(row=4, column=3)
                    i12 = Label(g, font=('aria', 15, 'bold'), text="Minor Surgeries", fg="blue", bg='black', anchor=W)
                    i12.grid(row=5, column=0)
                    il3 = Label(g, font=('aria', 15, 'bold'), text="4500", fg="blue", bg='black', anchor=W)
                    il3.grid(row=5, column=3)
                    i14 = Label(g, font=('aria', 15, 'bold'), text="X-rays", fg="blue", bg='black', anchor=W)
                    i14.grid(row=6, column=0)
                    il5 = Label(g, font=('aria', 15, 'bold'), text="500", fg="blue", bg='black', anchor=W)
                    il5.grid(row=6, column=3)
                    i16 = Label(g, font=('aria', 15, 'bold'), text="CAT scans", fg="blue", bg='black', anchor=W)
                    i16.grid(row=7, column=0)
                    il7 = Label(g, font=('aria', 15, 'bold'), text="9500", fg="blue", bg='black', anchor=W)
                    il7.grid(row=7, column=3)
                    i18 = Label(g, font=('aria', 15, 'bold'), text="Standard checkups", fg="blue", bg='black', anchor=W)
                    i18.grid(row=8, column=0)
                    il3 = Label(g, font=('aria', 15, 'bold'), text="150", fg="blue", bg='black', anchor=W)
                    il3.grid(row=8, column=3)
                    g.mainloop()



		def re():

			e1.delete(0,END)
			e2.delete(0,END)
			e3.delete(0,END)
			e4.delete(0,END)
			e5.delete(0,END)
			e6.delete(0,END)
			e7.delete(0,END)
			e8.delete(0,END)		
		def su():
			y=Tk()
			y.title("Result")
			y.configure(bg="black")
			a=int(e1.get())*810+int(e2.get())*9000+int(e3.get())*50+int(e4.get())*200+int(e5.get())*4500+int(e6.get())*500+int(e7.get())*9500+int(e8.get())*150
			result1=Label(y,text="Result ")
			result1.grid(row=0,column=0)

			entry1=Entry(y,width=15,borderwidth=5)
			
			entry1.delete(0,END)
			entry1.insert(0,str(a))
			entry1.grid(row=0,column=1)
			conn=sqlite3.connect('details2.db')
			c=conn.cursor()
			c.execute("INSERT INTO details1 VALUES(:f_name, :l_name, :address, :phone, :result)",
				   {
				   		'f_name' :ze1.get(),
				   		'l_name':ze2.get(),
				   		'address':ze3.get(),
				   		'phone':ze4.get(),
				   		'result':entry1.get()
				   })
			conn.commit()
			conn.close()
			x.destroy()
			y.mainloop()
			
		def di():
			v=Tk()
			v.title("List")
			v.configure(bg="black")
			conn=sqlite3.connect('details2.db')
			c=conn.cursor()
			c.execute("Select *,oid FROM details1")
			records=c.fetchall()
			print_r=''
			for record in records:
				print_r+=str(record[5])+" "+str(record[0])+" "+str(record[1])+" cost "+str(record[4])+"\n"
			print(print_r)
			label1=Label(v,text=print_r)
			label1.grid(row=0,column=0)
			conn.commit()
			conn.close()

			v.mainloop()



			

		frame1=LabelFrame(x,padx=50,pady=50,bg="black")
		frame1.pack(padx=10,pady=10)
		lblinfo1 = Label(frame1, font=('aria', 20), text=localtime, fg="red", bg='black', anchor='w', pady=10)
		lblinfo1.grid(row=1,column=0,columnspan=4)
		z1=Label(frame1,font=('aria',30,'bold'),text="Hospital Management System",fg="green",bg="black",pady=40,anchor='w')
		z1.grid(row=0,column=0,columnspan=4)
		z2=Label(frame1,text="rooms",fg="blue",bg="black",anchor='w',padx=10)
		z2.grid(row=2,column=0)
		z3=Label(frame1,text="Complicated Surgeries",fg="blue",bg="black",anchor='w')
		z3.grid(row=3,column=0)
		z4=Label(frame1,text="Weak medicines",fg="blue",bg="black",anchor='w')
		z4.grid(row=4,column=0)
		z5=Label(frame1,text="Strong medicines",fg="blue",bg="black",anchor='w')
		z5.grid(row=5,column=0)
		z6=Label(frame1,text="Minor surgeries",fg="blue",bg="black",anchor='w')
		z6.grid(row=2,column=2)
		z7=Label(frame1,text="X-rays",fg="blue",bg="black",anchor='w')
		z7.grid(row=3,column=2)
		z8=Label(frame1,text="CAT scans",fg="blue",bg="black",anchor='w')
		z8.grid(row=4,column=2)
		z9=Label(frame1,text="Standard check ups",fg="blue",bg="black",anchor='w')
		z9.grid(row=5,column=2)
		e1=Entry(frame1,width=20,borderwidth=5,justify='right')
		e1.grid(row=2,column=1,pady=25,padx=30)
		e2=Entry(frame1,width=20,borderwidth=5,justify='right')
		e2.grid(row=3,column=1,pady=25,padx=30)
		e3=Entry(frame1,width=20,borderwidth=5,justify='right')
		e3.grid(row=4,column=1,pady=25,padx=30)
		e4=Entry(frame1,width=20,borderwidth=5,justify='right')
		e4.grid(row=5,column=1,pady=25,padx=30)
		e5=Entry(frame1,width=20,borderwidth=5,justify='right')
		e5.grid(row=2,column=3,pady=25,padx=30)
		e6=Entry(frame1,width=20,borderwidth=5,justify='right')
		e6.grid(row=3,column=3,pady=25,padx=30)
		e7=Entry(frame1,width=20,borderwidth=5,justify='right')
		e7.grid(row=4,column=3,pady=25,padx=30)
		e8=Entry(frame1,width=20,borderwidth=5,justify='right')
		e8.grid(row=5,column=3,pady=25,padx=30)
		Prices=Button(frame1,text=' Prices',padx=20,pady=20,command=price,fg='blue',bg='black')
		Submit=Button(frame1,text=' Submit',padx=20,pady=20,command=su,fg='blue',bg='black')
		Reset=Button(frame1,text='  Reset',padx=20,pady=20,command=re,fg='blue',bg='black')
		Display=Button(frame1,text='Display Patients',padx=20,pady=20,command=di,fg='blue',bg='black')
		Prices.grid(row=6,column=0)
		Submit.grid(row=6,column=1)
		Reset.grid(row=6,column=2)
		Display.grid(row=6,column=3)


	localtime = time.asctime(time.localtime(time.time()))

	frame=LabelFrame(z,padx=50,pady=50,bg="black")
	frame.pack(padx=10,pady=10)
	lblinfo = Label(frame, font=('aria', 20), text=localtime, fg="red", bg='black', anchor=W, pady=10)
	lblinfo.grid(row=1,column=0,columnspan=4)
	zl1=Label(frame,font=('aria',30,'bold'),text="Welcome to fortis",fg="green",bg="black",pady=40)
	zl1.grid(row=0,column=0,columnspan=4)
	zl2=Label(frame,text="Patient First Name",fg="blue",bg="black")
	zl2.grid(row=2,column=0,columnspan=2)
	zl3=Label(frame,text="Patient Last Name",fg="blue",bg="black")
	zl3.grid(row=3,column=0,columnspan=2)
	zl4=Label(frame,text="Address",fg="blue",bg="black")
	zl4.grid(row=4,column=0,columnspan=2)
	ze1=Entry(frame,width=25,borderwidth=5)
	ze1.grid(row=2,column=2,columnspan=2,pady=25)	
	ze2=Entry(frame,width=25,borderwidth=5)
	ze2.grid(row=3,column=2,columnspan=2,pady=25)	
	ze3=Entry(frame,width=25,borderwidth=5)
	ze3.grid(row=4,column=2,columnspan=2,pady=25)
	zl4=Label(frame,text="Phone number",fg="blue",bg="black")
	zl4.grid(row=5,column=0,columnspan=2)
	ze4=Entry(frame,width=25,borderwidth=5)
	ze4.grid(row=5,column=2,columnspan=2,pady=25)
	zb1=Button(frame,text="Submit",fg='blue',bg='black',command=submit)
	zb1.grid(row=6,column=0,columnspan=2)
	zb2=Button(frame,text="Reset",fg="blue",bg="black",command=reset)
	zb2.grid(row=6,column=2,columnspan=2)


	z.mainloop()
def branch():
    

    s=Tk()
    s.title("Branches")

    s.geometry("200x500")
    
    s.configure(bg='black')
    def IN():
    	j=Tk()
    	j.title("Branches in India")
    	j.configure(bg="black")
    	lbl1 = Label(j, font=('aria', 15, 'bold'), text="State", fg="red", bg='black', bd=5)
    	lbl1.grid(row=0, column=0)
    	lbl2 = Label(j, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
    	lbl2.grid(row=0, column=2)
    	lbl3 = Label(j, font=('aria', 15, 'bold'), text="no of branches", fg='red', bg='black', anchor=W)
    	lbl3.grid(row=0, column=3)
    	lbl4 = Label(j, font=('aria', 15, 'bold'), text="Maharashtra", fg="red", bg='black', anchor=W)
    	lbl4.grid(row=1, column=0)
    	lbl5 = Label(j, font=('aria', 15, 'bold'), text="3", fg="red", bg='black', anchor=W)
    	lbl5.grid(row=1, column=3)
    	lbl6 = Label(j, font=('aria', 15, 'bold'), text="Delhi", fg="red", bg='black', anchor=W)
    	lbl6.grid(row=2, column=0)
    	lbl7 = Label(j, font=('aria', 15, 'bold'), text="2", fg="red", bg='black', anchor=W)
    	lbl7.grid(row=2, column=3)
    	lbl8 = Label(j, font=('aria', 15, 'bold'), text="Assam", fg="red", bg='black', anchor=W)
    	lbl8.grid(row=3, column=0)
    	lbl9 = Label(j, font=('aria', 15, 'bold'), text="2", fg="red", bg='black', anchor=W)
    	lbl9.grid(row=3, column=3)
    	lbl10 = Label(j, font=('aria', 15, 'bold'), text="Goa", fg="red", bg='black', anchor=W)
    	lbl10.grid(row=4, column=0)
    	lbl11 = Label(j, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    	lbl11.grid(row=4, column=3)
    	lbl12 = Label(j, font=('aria', 15, 'bold'), text="West Bengal", fg="red", bg='black', anchor=W)
    	lbl12.grid(row=5, column=0)
    	lbl3 = Label(j, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    	lbl3.grid(row=5, column=3)
    	j.mainloop()
    def AM():
    	k=Tk()
    	k.title("Branches in America")
    	k.configure(bg="black")
    	labl1 = Label(k, font=('aria', 15, 'bold'), text="State", fg="red", bg='black', bd=5)
    	labl1.grid(row=0, column=0)
    	labl2 = Label(k, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
    	labl2.grid(row=0, column=2)
    	labl3 = Label(k, font=('aria', 15, 'bold'), text="no of branches", fg='red', bg='black', anchor=W)
    	labl3.grid(row=0, column=3)
    	labl4 = Label(k, font=('aria', 15, 'bold'), text="Texas", fg="red", bg='black', anchor=W)
    	labl4.grid(row=1, column=0)
    	labl5 = Label(k, font=('aria', 15, 'bold'), text="4", fg="red", bg='black', anchor=W)
    	labl5.grid(row=1, column=3)
    	labl6 = Label(k, font=('aria', 15, 'bold'), text="Alaska", fg="red", bg='black', anchor=W)
    	labl6.grid(row=2, column=0)
    	labl7 = Label(k, font=('aria', 15, 'bold'), text="14", fg="red", bg='black', anchor=W)
    	labl7.grid(row=2, column=3)
    	labl8 = Label(k, font=('aria', 15, 'bold'), text="Arizona", fg="red", bg='black', anchor=W)
    	labl8.grid(row=3, column=0)
    	labl9 = Label(k, font=('aria', 15, 'bold'), text="10", fg="red", bg='black', anchor=W)
    	labl9.grid(row=3, column=3)
    	labl10 = Label(k, font=('aria', 15, 'bold'), text="New York", fg="red", bg='black', anchor=W)
    	labl10.grid(row=4, column=0)
    	labl11 = Label(k, font=('aria', 15, 'bold'), text="8", fg="red", bg='black', anchor=W)
    	labl11.grid(row=4, column=3)
    	labl12 = Label(k, font=('aria', 15, 'bold'), text="London", fg="red", bg='black', anchor=W)
    	labl12.grid(row=5, column=0)
    	labl3 = Label(k, font=('aria', 15, 'bold'), text="4", fg="red", bg='black', anchor=W)
    	labl3.grid(row=5, column=3)
    	k.mainloop()
    def Ch():
    	l=Tk()
    	l.title("Branches in China")
    	l.configure(bg='black')
    	lb1 = Label(l, font=('aria', 15, 'bold'), text="State", fg="red", bg='black', bd=5)
    	lb1.grid(row=0, column=0)
    	lb2 = Label(l, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
    	lb2.grid(row=0, column=2)
    	lb3 = Label(l, font=('aria', 15, 'bold'), text="no of branches", fg='red', bg='black', anchor=W)
    	lb3.grid(row=0, column=3)
    	lb4 = Label(l, font=('aria', 15, 'bold'), text="Shandong", fg="red", bg='black', anchor=W)
    	lb4.grid(row=1, column=0)
    	lb5 = Label(l, font=('aria', 15, 'bold'), text="7", fg="red", bg='black', anchor=W)
    	lb5.grid(row=1, column=3)
    	lb6 = Label(l, font=('aria', 15, 'bold'), text="Jiangsu", fg="red", bg='black', anchor=W)
    	lb6.grid(row=2, column=0)
    	lb7 = Label(l, font=('aria', 15, 'bold'), text="20", fg="red", bg='black', anchor=W)
    	lb7.grid(row=2, column=3)
    	lb8 = Label(l, font=('aria', 15, 'bold'), text="Sichuan", fg="red", bg='black', anchor=W)
    	lb8.grid(row=3, column=0)
    	lb9 = Label(l, font=('aria', 15, 'bold'), text="4", fg="red", bg='black', anchor=W)
    	lb9.grid(row=3, column=3)
    	lb10 = Label(l, font=('aria', 15, 'bold'), text="Hunan", fg="red", bg='black', anchor=W)
    	lb10.grid(row=4, column=0)
    	lb11 = Label(l, font=('aria', 15, 'bold'), text="12", fg="red", bg='black', anchor=W)
    	lb11.grid(row=4, column=3)
    	lb12 = Label(l, font=('aria', 15, 'bold'), text="Yunnan", fg="red", bg='black', anchor=W)
    	lb12.grid(row=5, column=0)
    	lb13 = Label(l, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    	lb13.grid(row=5, column=3)
    	l.mainloop()
    def Jp():
    	m=Tk()
    	m.title("Branches in Japan")
    	m.configure(bg='black')
    	ll1 = Label(m, font=('aria', 15, 'bold'), text="State", fg="red", bg='black', bd=5)
    	ll1.grid(row=0, column=0)
    	ll2 = Label(m, font=('aria', 15, 'bold'), text="______", fg="black", bg='black', anchor=W)
    	ll2.grid(row=0, column=2)
    	ll3 = Label(m, font=('aria', 15, 'bold'), text="no of branches", fg='red', bg='black', anchor=W)
    	ll3.grid(row=0, column=3)
    	ll4 = Label(m, font=('aria', 15, 'bold'), text="Hiroshima", fg="red", bg='black', anchor=W)
    	ll4.grid(row=1, column=0)
    	ll5 = Label(m, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    	ll5.grid(row=1, column=3)
    	ll6 = Label(m, font=('aria', 15, 'bold'), text="Nagasaki", fg="red", bg='black', anchor=W)
    	ll6.grid(row=2, column=0)
    	ll7 = Label(m, font=('aria', 15, 'bold'), text="9", fg="red", bg='black', anchor=W)
    	ll7.grid(row=2, column=3)
    	ll8 = Label(m, font=('aria', 15, 'bold'), text="Fukushima", fg="red", bg='black', anchor=W)
    	ll8.grid(row=3, column=0)
    	ll9 = Label(m, font=('aria', 15, 'bold'), text="6", fg="red", bg='black', anchor=W)
    	ll9.grid(row=3, column=3)
    	ll10 = Label(m, font=('aria', 15, 'bold'), text="Saitama", fg="red", bg='black', anchor=W)
    	ll10.grid(row=4, column=0)
    	ll11 = Label(m, font=('aria', 15, 'bold'), text="2", fg="red", bg='black', anchor=W)
    	ll11.grid(row=4, column=3)
    	ll12 = Label(m, font=('aria', 15, 'bold'), text="Yamagata", fg="red", bg='black', anchor=W)
    	ll12.grid(row=5, column=0)
    	lll3 = Label(m, font=('aria', 15, 'bold'), text="1", fg="red", bg='black', anchor=W)
    	lll3.grid(row=5, column=3)
    	m.mainloop()
    l1=Label(s,font=('aria', 15, 'bold'),text="Countries",fg="blue",bg='black',anchor=W,pady=40)
    b1=Button(s,font=('aria', 15, 'bold'),text="India  ",fg="blue",bg='black',padx=60,pady=30,command=IN,anchor=W)
    b2=Button(s,font=('aria', 15, 'bold'),text="America",fg="blue",bg='black',padx=57,pady=30,command=AM,anchor=W)
    b3=Button(s,font=('aria', 15, 'bold'),text="China  ",fg="blue",bg='black',padx=57,pady=30,command=Ch,anchor=W)
    b4=Button(s,font=('aria', 15, 'bold'),text="Japan  ",fg="blue",bg='black',padx=57,pady=30,command=Jp,anchor=W)
    l1.grid(row=0,column=0) 
    b1.grid(row=1,column=0)
    b2.grid(row=2,column=0)
    b3.grid(row=3,column=0)
    b4.grid(row=4,column=0) 
    s.mainloop() 
    

    
rl1=Label(r,text="FORTIS",fg='green',bg='black',font=("Helvetica",30))
rl1.grid(row=0,column=0,columnspan=3)
rl2=Label(r,text="      ",fg='black',bg='black')
rl2.grid(row=1,column=0,columnspan=3)
rl3=Label(r,text="      ",fg='black',bg='black')
rl3.grid(row=2,column=0,columnspan=3)
rl4=Label(r,text="      ",fg='black',bg='black')
rl4.grid(row=4,column=0,columnspan=3)
rl5=Label(r,text="      ",fg='black',bg='black')
rl5.grid(row=5,column=0,columnspan=3)

rl6=Label(r,text="      ",fg='black',bg='black')
rl6.grid(row=7,column=0,columnspan=3)

rl7=Label(r,text="      ",fg='black',bg='black')
rl7.grid(row=8,column=0,columnspan=3)
rl10=Label(r,text="      ",fg='black',bg='black')
rl10.grid(row=10,column=0,columnspan=3)
rl11=Label(r,text="      ",fg='black',bg='black')
rl11.grid(row=11,column=0,columnspan=3)
rb4=Button(r,text="branches",fg='blue',bg='black',padx=20,pady=20,command=branch)
rb4.grid(row=12,column=0)
rb1=Button(r,text="about",fg='blue',bg='black',padx=20,pady=20,command=ab)
rb1.grid(row=3,column=0)
rb2=Button(r,text="Proceed",fg='blue',bg='black',padx=16,pady=20,command=pro)
rb2.grid(row=6,column=0)
rb3=Button(r,text="Quit",fg='blue',bg='black',padx=23,pady=23,command=quit)
rb3.grid(row=9,column=0)

r.mainloop()



