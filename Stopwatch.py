from tkinter import *

root = Tk()

root.geometry('300x300')

label = Label(root, text='00: 00: 00')
label.pack()

b = 1


def start():
    global b
    root.after(1000, fun1, sec, minute, hr)
    start_b.configure(command=stop_func, text="Stop")
    b = 1


sec = 1
minute = 0
hr = 0


def stop_func():
    global b
    b = 0
    start_b.configure(text="Start", command=start)


def fun1(secs, minute_1, hour_1):
    global b

    if b:
        hours = hour_1
        minutes = minute_1
        seconds = secs

        current_time = f"{hours}: {minutes}: {seconds}"

        label.config(text=current_time)
        secs += 1

        if minute_1 == secs == 59:
            minute_1 = 0
            secs = 0
            hour_1 += 1

        if secs == 59:
            secs = 0
            minute_1 += 1

        global sec
        global minute
        global hr

        sec = secs
        minute = minute_1
        hr = hour_1

        root.after(1000, fun1, secs, minute_1, hour_1)


start_b = Button(root, text='Start', command=start)
start_b.pack()


def reset():
    global b
    global sec
    global minute
    global hr

    b = 0
    start_b.configure(text="Start", command=start)
    sec = 1
    minute = 0
    hr = 0

    label.config(text='00: 00: 00')


reset_b = Button(root, text='Reset', command=reset)
reset_b.pack()

root.mainloop()
