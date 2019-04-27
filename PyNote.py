# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk
from tkinter import ttk
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
import os
from pynput.mouse import Controller
import keyboard
import tempfile
import win32api
import win32print
from Font import Font_size

location = os.path.dirname(os.path.realpath(__file__))
icon_location = location+"/icon/"

def disable_event():
	pass

class Createsearch_online:

	def __init__(self,app_name,note):

		self.app_name = app_name
		app_name.bind("<Shift-Alt-Y>",self.new_window)
		self.note = note

	def new_window(self,Event):
		self.Entry = tk.Entry(self.app_name,width=800,bg="gray10",fg="white",font=("Segoe UI",20),insertbackground="white")
		self.Entry.place(x=0,y=0)
		self.Entry.focus()
		self.Entry.bind("<Return>",self.double_click)
		self.Entry.bind("<Leave>",self.double_click)

	def double_click(self,Event):
		get_text_val = self.Entry.get()
		if get_text_val == "":
			print("")
		else:
			os.startfile("https://www.google.com/search?client=firefox-b-d&q={}".format(get_text_val))
		self.Entry.destroy()

class Scrollbar:
	#use Scrollbar(Textboxname)
 	def __init__(self,text):
 		self.frame = text.master
 		self.text = text
 		self.text.configure(wrap='none')
 		self.for_x_view()
 		self.for_y_view()

 	def for_x_view(self):

 		self.scroll_x = ttk.Scrollbar(self.frame, orient='horizontal',command=self.text.xview)
 		self.scroll_x.config(command=self.text.xview)
 		self.text.configure(xscrollcommand=self.scroll_x.set)
 		self.scroll_x.pack(side='bottom', fill='x', anchor='w')
 		return

 	def for_y_view(self):

 		self.scroll_y = tk.Scrollbar(self.frame)
 		self.scroll_y.config(command=self.text.yview)
 		self.text.configure(yscrollcommand=self.scroll_y.set)
 		self.scroll_y.pack(side='right', fill='y')  
 		return

class main_frame:

	def __init__(self):

		User = os.getenv("username")
		self.ops_path = 'C:/Users/{}/'.format(User)

		batch_ = open(self.ops_path + 'operation.bat','w')
		batch_.write("")
		batch_.close()

		lap = tk.Tk()
		lap.title('untitled')
		self.lap = lap

		self.menubar = Menu(self.lap)
		self.filemenu = Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New       Ctrl+N", command=self.new)
		self.filemenu.add_command(label="Open     Ctrl+O", command=self.opentxt)
		self.filemenu.add_command(label="Save       Ctrl+S" , command=self.save)
		self.filemenu.add_command(label="Save as" , command=self.saveas)
		self.filemenu.add_command(label="Print       Ctrl+P" , command=self.print_)

		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit        Ctrl+Q", command=self.end__)
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.editmenu = Menu(self.menubar, tearoff=0)

		self.editmenu.add_command(label="Cut      Ctrl+X", command=self.cut_content)
		self.editmenu.add_command(label="Copy    Ctrl+C", command=self.copy_content)
		self.editmenu.add_command(label="Paste    Ctrl+V", command=self.paste_content)
		self.editmenu.add_command(label="Delete", command=self.delete_content)

		self.editmenu.add_separator()

		self.editmenu.add_command(label="Select All   CTRL+A", command=self.select_all_content)

		self.menubar.add_cascade(label="Edit", menu=self.editmenu)
		self.theme = Menu(self.menubar, tearoff=0)

		self.theme.add_command(label="Default", command=self.default_theme)

		self.theme.add_separator()

		self.theme.add_command(label="DeepBlue", command=self.DeepBlue)
		self.theme.add_command(label="PowerMad", command=self.PowerMad)
		self.theme.add_command(label="NightPole", command=self.nightcrawl)
		self.theme.add_command(label="RockMan", command=self.rockman)
		self.menubar.add_cascade(label="Theme", menu=self.theme)

		note_entry = tk.Text(lap,font=("segoe ui",20),selectbackground="lightblue1")

		self.note_entry = note_entry
		Scrollbar(self.note_entry)
		note_entry.pack(expand=True,fill=BOTH)
		self.rightclick_event()
		Createsearch_online(self.lap,self.note_entry)
		self.note_entry.focus()

		self.Format = Menu(self.menubar, tearoff=0)
		self.Font_size_val = Font_size(self.menubar,self.note_entry)
		self.Format.add_cascade(label="Font size", menu=self.Font_size_val)
		self.Format.add_command(label="Search", command=self.search)
		self.menubar.add_cascade(label="Format", menu=self.Format)

		self.helpmenu = Menu(self.menubar, tearoff=0)
		self.helpmenu.add_command(label="Help   Ctrl+H", command=self.help_)
		self.helpmenu.add_command(label="About   Ctrl+I", command=self.page)
		self.menubar.add_cascade(label="Help", menu=self.helpmenu)

		self.default_theme()

		lap.config(menu=self.menubar)
		lap.geometry('800x800+250+50')
		lap.bind_all('<Key>', self.keypress)
		lap.wm_attributes('-alpha',0.9)
		lap.iconbitmap(icon_location+"icon.ico")
		lap.protocol('WM_DELETE_WINDOW',self.quit_func)
		lap.mainloop()

	def rightclick_event(self):

		self.menu__ = Menu(self.lap, tearoff=0)

		self.Font_size_val = Font_size(self.menu__,self.note_entry)
		self.menu__.add_cascade(label="Font Size",menu=self.Font_size_val, underline=0)

		self.menu__.add_separator()

		self.menu__.add_command(label="Cut",command=self.cut_content)
		self.menu__.add_command(label="Copy",command=self.copy_content)
		self.menu__.add_command(label="Paste",command=self.paste_content)
		self.menu__.add_command(label="Select All",command=self.select_all_content)

		self.submenu = Menu(self.menu__, tearoff=0)

		self.submenu.add_command(label='DeepBlue', command=self.DeepBlue, underline=0)
		self.submenu.add_command(label='PowerMad', command=self.PowerMad, underline=0)
		self.submenu.add_command(label='Nightcrawl', command=self.nightcrawl, underline=0)
		self.submenu.add_command(label='RockMan', command=self.rockman, underline=0)

		self.menu__.add_separator()

		self.menu__.add_cascade(label="Theme", menu=self.submenu, underline=0)

		self.menu__.add_command(label="Search", command=self.search)

		self.lap.bind("<Button-3>", self.showMenu)

	def showMenu(self, e):
		self.menu__.post(e.x_root, e.y_root)

	def search(self):
		keyboard.press_and_release('shift+alt+y')

	def keypress(self,event):
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("S"):
			self.save()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("N"):
			self.new()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("O"):
			self.opentxt()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("Q"):
			self.quit_func()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("X"):
			self.cut_content()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("C"):
			self.copy_content()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("V"):
			self.paste_content()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("A"):
			self.select_all_content()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("H"):
			self.help_()
		if keyboard.is_pressed("CTRL") and keyboard.is_pressed("I"):
			self.page()

	def end__(self):
		self.lap.quit()

	def quit_func(self):
		try:
			text_val = self.note_entry.get('1.0',END)
			if text_val != "":
				message1 = "Save-PyNote"
				message2 = "Do you want to save changes"
				quit__ = tk.Tk()
				quit__.iconbitmap(icon_location+"icon.ico")
				quit__.configure(bg="gray20")
				quit__.title(message1)
				quit__.geometry("+500+450")
				label = tk.Label(quit__, text=message2,bg="gray20",fg='white'
	                ,font=("Banschrift",15))
				label.pack()

				def destroy_button():
					self.note_entry.config(state=NORMAL)
					quit__.destroy()
					try:
						self.lap.wm_attributes('-alpha',0.92)
						self.lap.protocol("WM_DELETE_WINDOW", self.quit_func)
					except:
						pass

				def destroy_PyNote():
					quit__.destroy()
					try:
						self.lap.destroy()
					except:
						pass

				def save_button():
					quit__.destroy()
					try:
						self.saveas()
						self.lap.destroy()
					except:
						pass

				cancel = tk.Button(quit__, text="Cancel",width="15", height="2", bg="gray60",fg='gray1'
	                ,borderwidth=0,highlightthickness=0,command=destroy_button)
				cancel.pack(side=RIGHT)
				Dont_save = tk.Button(quit__, text="Don't_save",width="15", height="2", bg="gray70",fg='gray1'
	                ,borderwidth=0,highlightthickness=0,command=destroy_PyNote)
				Dont_save.pack(side=RIGHT)
				save = tk.Button(quit__, text="Save",width="15", height="2", bg="gray80",fg='gray1'
	                ,borderwidth=0,highlightthickness=0,command=save_button)
				save.pack(side=RIGHT)

				self.lap.wm_attributes('-alpha',0.7)
				quit__.wm_attributes('-alpha',0.95)
				self.note_entry.config(state=DISABLED)
				self.lap.protocol("WM_DELETE_WINDOW", disable_event)
				quit__.protocol('WM_DELETE_WINDOW',destroy_button)
				quit__.resizable(width=0,height=0)
				quit__.mainloop()
		except:
			text_val = self.note_entry.get('1.0',END)
			if text_val != "":
				x = tk.messagebox.askyesnocancel("Save", "Do you want to save changes")
				if x == NO:
					self.lap.destroy()
				if x == YES:
					self.lap.saveas()
					self.lap.destroy()

	def opentxt(self):
		try:
			fileloc_ = filedialog.askopenfilename(initialdir = "/",title = "Select file"
				,filetypes = (("Text files","*.txt"),("all files","*.*")))
			with open(fileloc_, 'r') as file:
				data = file.read()
				self.note_entry.delete('1.0',END)
				self.note_entry.insert(END,data)
				self.lap.title(fileloc_+"/-PyNote")
		except:
			pass

	def new(self):
		try:
			self.note_entry.delete('1.0',END)
			self.lap.title("untitled")
			batch_ = open(self.ops_path+'operation.bat','w')
			batch_.write("")
			batch_.close()
		except:
			pass

	def save(self):
		try:
			try:
				batch_ = open(self.ops_path+'operation.bat','r')
			except:
				raise KeyError
			try:
				text = batch_.read()
				if text=="":
					raise KeyError
				text_val = self.note_entry.get('1.0',END)
				save = open(text,'w')
				save.write('{}'.format(text_val))
			except:
				raise KeyError

		except KeyError:
			save = filedialog.asksaveasfile(mode='w',defaultextension = '.txt')
			text_val = self.note_entry.get('1.0',END)
			word = open('{}'.format(save.name),'w')
			word.write("{}".format(text_val))
			word.close()
			self.lap.title(save.name)
			batch = open(self.ops_path+'operation.bat','w')
			batch.write(save.name)
			batch.close()

	def saveas(self):
		try:
			save = filedialog.asksaveasfile(mode='w'
					,defaultextension = '.txt')
			text_val = self.note_entry.get('1.0',END)
			word = open('{}'.format(save.name),'w')
			word.write("{}".format(text_val))
			word.close()
			self.lap.title(save.name)
		except:
			pass

	def print_(self):
		text_val = self.note_entry.get('1.0',END)
		filename = tempfile.mktemp(".txt")
		open (filename, "w").write(text_val)
		win32api.ShellExecute(
		  0,
		  "print",
		  filename,
		  '/d:"%s"' % win32print.GetDefaultPrinter(),
		  ".",
		  0
		  )

	def cut_content(self):
		keyboard.press_and_release('ctrl+x')

	def copy_content(self):
		keyboard.press_and_release('ctrl+c')

	def paste_content(self):
		keyboard.press_and_release('ctrl+v')

	def delete_content(self):
		keyboard.press_and_release('del')

	def select_all_content(self):
		self.note_entry.tag_add(SEL,'1.0',END)

	def DeepBlue(self):
		self.note_entry.config(bg='lightblue2', fg="gray10"
			, font=("segoe ui",20),selectbackground="lightblue4",insertbackground="black")
		self.filemenu.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.editmenu.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.theme.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.helpmenu.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.menu__.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.Font_size_val.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.submenu.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')
		self.Format.config(tearoff=0,background='powder blue',foreground='black',activebackground='lightSteelBlue', activeforeground='white')

	def PowerMad(self):
		self.note_entry.config(bg='red', fg="white"
			, font=("segoe ui",20),selectbackground="coral3",insertbackground="white")
		self.filemenu.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.editmenu.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.theme.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.helpmenu.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.menu__.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.Font_size_val.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.submenu.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')
		self.Format.config(tearoff=0,background='coral1',foreground='black',activebackground='gray80', activeforeground='white')

	def nightcrawl(self):
		self.note_entry.config(bg='black', fg="white"
			, font=("segoe ui",20),selectbackground="white",insertbackground="white")
		self.filemenu.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.editmenu.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.theme.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.helpmenu.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.menu__.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.Font_size_val.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.submenu.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")
		self.Format.config(tearoff=0,background='gray',foreground='white',activebackground='gray30', activeforeground="light cyan")

	def rockman(self):
		self.note_entry.config(bg='azure', fg="red"
			, font=("segoe ui",20),selectbackground="coral",insertbackground="red")
		self.filemenu.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.editmenu.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.theme.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.helpmenu.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.menu__.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.Font_size_val.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.submenu.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')
		self.Format.config(tearoff=0,background='white',foreground='red',activebackground='gray80', activeforeground='white')

	def default_theme(self):
		self.note_entry.config(bg='white', fg="black"
			, font=("segoe ui",20),selectbackground="lightblue1",insertbackground="black")
		self.filemenu.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.editmenu.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.theme.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.helpmenu.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.menu__.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.Font_size_val.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.submenu.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')
		self.Format.config(tearoff=0,background='white',foreground='black',activebackground='lightblue1', activeforeground='black')

	def help_(self):
		os.startfile("https://www.github.com/roshanpoduval1998/PyNote")

	def page(self):
		try:
			message1 = "About"
			message2 = "PyNote is written in python language\nDeveloped by Roshan Poduval\nversion: 1.0.1"
			about_ = tk.Tk()
			about_.iconbitmap(icon_location+"icon.ico")
			about_.configure(bg="gray20")
			about_.title(message1)
			about_.geometry("+500+450")
			label = tk.Label(about_, text=message2,bg="gray20",fg='white'
	            ,font=("Banschrift",13))
			label.pack()
			def destroy_button():
				self.note_entry.config(state=NORMAL)
				about_.destroy()
				try:
					self.lap.wm_attributes('-alpha',0.92)
					self.lap.protocol("WM_DELETE_WINDOW", self.quit_func)
				except:
					pass
			button = tk.Button(about_, text="Close",width="15", bg="gray80",fg='gray1'
	            ,borderwidth=0,highlightthickness=0,command=destroy_button)
			button.pack()
			self.lap.wm_attributes('-alpha',0.7)
			about_.wm_attributes('-alpha',0.95)
			self.note_entry.config(state=DISABLED)
			self.lap.protocol("WM_DELETE_WINDOW", disable_event)
			about_.protocol('WM_DELETE_WINDOW',destroy_button)
			about_.resizable(width=0,height=0)
			about_.mainloop()
		except:
			messagebox.showinfo("PyNote--","PyNote is written in python language\nDeveloped by Roshan Poduval\nversion: 1.0.1")

if __name__ == "__main__":
	main_frame()
