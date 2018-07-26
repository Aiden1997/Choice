import tkinter as tk

from tkinter import messagebox



attributes_string = ''
attributes = []
dict_entry = {}
importance = []

window = tk.Tk()
window.title('Welcome to Choice')
window.geometry('450x300')

canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,30,anchor='nw',image=image_file)
canvas.pack(side='top')

def help():
	window_help = tk.Toplevel(window)
	window_help.geometry('350x200')
	window_help.title('Help')
	tk.Label(window_help,text='Ask Aiden.').pack()

def first_step():
	def all_right():
		global attributes_string
		attributes_string = entry_a.get()
		global attributes
		attributes = attributes_string.split()
		new_string = 'You care about '
		for i in range(len(attributes)-1):
			new_string += attributes[i] + ', '
		new_string += attributes[-1] + '. Right?'
		var = tk.StringVar()
		var.set(new_string)
		tk.Label(window_first,font=("Arial", "14","bold italic"),textvariable=var).place(x=300,y=240,anchor='center')
		tk.Button(window_first,text='Next Step',font=("Arial", "14") ,command=second_step).place(x=400,y=300)
	
	window.destroy()
	window_first = tk.Tk()
	window_first.geometry('600x400')
	window_first.title('First Step')
	
	var = tk.StringVar()
	tk.Label(window_first,text='What attributes do you want to consider?',font=("Arial", "12")).place(x=300,y=50,anchor='center')
	tk.Label(window_first,text="Use ' ' to seperate.",font=("Arial", "12")).place(x=300,y=80,anchor='center')
	entry_a = tk.Entry(window_first,width = 60)
	entry_a.place(x=300,y=120,anchor='center')
	
	tk.Button(window_first,text='All right!',font=("Arial", "14") ,command=all_right).place(x=300,y=160,anchor='center')
	


def second_step():
	global dict
	window_second = tk.Tk()
	window_second.geometry('800x720')
	window_second.title('Second Step')
	
	def get_importance():
		global importance
		for i in range(len(attributes)*len(attributes)):
			importance.append(dict_entry[i].get())
			
		print(importance)
	
	var2 = tk.StringVar()
	for i in range(len(attributes)):
		tk.Label(window_second,text='Campared with '+ attributes[i] +', the importance of each are:',font=("Arial", "12")).place(x=50,y=40+150*i)
		for j in range(len(attributes)):
			tk.Label(window_second,text=attributes[j],font=("Arial", "14")).place(x=60+160*j,y=80+150*i)
			dict_entry[len(attributes)*(i)+j] = tk.Entry(window_second)
			dict_entry[len(attributes)*(i)+j].place(x=60+160*j,y=120+150*i)
			
	
	tk.Button(window_second,text='All right!',font=("Arial", "16","bold italic"),command=get_importance).place(x=160*i+100,y=150*i+200)
	











button_begin = tk.Button(window,text='Begin',font=("Arial", "14") ,command=first_step)
button_begin.place(x=150,y=200)

button_help = tk.Button(window,text='Help',font=("Arial", "14"),command=help)
button_help.place(x=250,y=200)

window.mainloop()
