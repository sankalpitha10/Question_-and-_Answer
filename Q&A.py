
import tkinter as tk
from tkinter import messagebox as mbox

input='1) 2007' , '2) ctrl c','3) Kilobyte','4) No', '5) Charles Babbage','6) Hypertext transfer protocol','7) Pirrer Omidyar','8) Hotmail','9) Web browser','10) Twttr' 

def check_answer():
    mbox.showinfo('Answers', input)    

window=tk.Tk()
window.geometry('600x600')
window.title('Questions and Answers')      
            
label= tk.Label(window, text='General Questions and Answers', font=('Arial', 14))
label.pack() 

question1= tk.Label(window, text='1) What year was the very first model of the iphone released?', font=('arial', 12)).place(x=0, y=40)
answer1_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 60)
question2=tk.Label(window, text='2) What is the shortcut for the copy function?', font=('Arial', 12)).place(x=0,y= 80)
answer2_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 100)
question3=tk.Label(window, text='3) what is the smallest unit of memory?', font=('Arial', 12)).place(x=0,y= 120)
answer3_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 140)
question4=tk.Label(window, text='4) is java a type of OS?', font=('Arial', 12)).place(x=0,y= 160)
answer4_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 180)
question5=tk.Label(window, text='5) Who is called father of the Computer?', font=('Arial', 12)).place(x=0,y= 200)
answer5_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 220)
question6=tk.Label(window, text='6) What does HTTP stand for?', font=('Arial', 12)).place(x=0,y= 240)
answer6_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 260)
question7=tk.Label(window, text='7) What is the name of man who launched eBay back in 1995?', font=('Arial', 12)).place(x=0,y= 280)
answer7_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 300)
question8=tk.Label(window, text='8) Which email services is owned by Microsoft?', font=('Arial', 12)).place(x=0,y= 320)
answer8_entry= tk.Text(window, height=1,font=('Arial', 10),bg='azure').place(x=0, y= 340)
question9=tk.Label(window, text='9) Google Chrome, Firefox are different types of what?', font=('Arial', 12)).place(x=0,y= 360)
answer9_entry= tk.Text(window, height=1,font=('Arial', 10),bg='azure').place(x=0, y= 380)
question10=tk.Label(window, text='10) what was Twitters original name?', font=('Arial', 12)).place(x=0,y= 400)
answer10_entry= tk.Text(window,height=1, font=('Arial', 10),bg='azure').place(x=0, y= 420)


button= tk.Button(window, text='Answers', command = check_answer, font=('Arial,', 13)).place(x=80,y=500)

window.mainloop()




    