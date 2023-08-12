from tkinter import *
from tkinter import ttk
import Quiz_Data as qd
import random

root = Tk()
root.geometry("400x250")
root.maxsize(width=400, height=250)
root.minsize(width=400, height=250)
root.title("Quiz")

my_font1 = (("Franklin Gothic Medium"), 15, "bold")
my_font2 = (("Franklin Gothic Medium"), 15)
my_font3 = (("Franklin Gothic Medium"), 10)

frm1 = Frame(root, bg="blue")
frm1.pack(side=LEFT, fill=BOTH, expand=True)

frm2 = Frame(root, bg="blue")
frm2.pack(side=RIGHT, fill=BOTH, expand=True)

visited = set()
q_no = random.randint(0, len(qd.quiz)-1)
visited.add(q_no)
no = 1
score = 0

lb1 = ttk.Label(frm1, text=f"Question {no}/4", background="blue",
                foreground="white", font=my_font1)
lb1.grid(row=0, column=0, pady=20)

question = ttk.Label(
    frm1, text=qd.quiz[q_no]["ques"], wraplength=220, justify=LEFT, background="blue", foreground="white", font=my_font2)
question.grid(row=1, column=0, columnspan=4, pady=5, padx=3)

space = ttk.Label(frm2, background="blue")
space.pack(pady=10)


def show_result(score):
    frm1.destroy()
    frm2.destroy()

    final_frm = Frame(root, bg="blue")
    final_frm.pack(fill=BOTH, expand=True)

    result = ttk.Label(final_frm, text=f"You scored {score} out of 4",
                       font=my_font1, background="blue", foreground="white")
    result.pack(padx=50, pady=100)


def on_click(n):
    global q_no, no, score, visited
    no += 1
    if(n == qd.quiz[q_no]["answer"]):
        score += 1
    if(no > 4):
        show_result(score)

    while True:
        q_no = random.randint(0, len(qd.quiz)-1)
        if q_no not in visited:
            visited.add(q_no)
            break

    lb1.config(text=f"Question {no}/4")
    question.config(text=qd.quiz[q_no]["ques"])
    btn1.config(text=qd.quiz[q_no]["option"][0])
    btn2.config(text=qd.quiz[q_no]["option"][1])
    btn3.config(text=qd.quiz[q_no]["option"][2])
    btn4.config(text=qd.quiz[q_no]["option"][3])


btn1 = Button(
    frm2, text=qd.quiz[q_no]["option"][0], width=50,
    fg="white", bg="blue", font=my_font3, command=lambda: on_click(qd.quiz[q_no]["option"][0]))
btn1.pack(pady=5, padx=10)
btn2 = Button(frm2, text=qd.quiz[q_no]["option"]
              [1], width=50, fg="white", bg="blue", font=my_font3, command=lambda: on_click(qd.quiz[q_no]["option"][1]))
btn2.pack(pady=5, padx=10)
btn3 = Button(frm2, text=qd.quiz[q_no]["option"]
              [2], width=50, fg="white", bg="blue", font=my_font3, command=lambda: on_click(qd.quiz[q_no]["option"][2]))
btn3.pack(pady=5, padx=10)
btn4 = Button(frm2, text=qd.quiz[q_no]["option"]
              [3], width=50, fg="white", bg="blue", font=my_font3, command=lambda: on_click(qd.quiz[q_no]["option"][3]))
btn4.pack(pady=5, padx=10)


root.mainloop()
