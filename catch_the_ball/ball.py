import tkinter

def button1_command():
    print('Button 1 default command')

def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x,event.y)
    #print(event.x_root,event.y_root)
    me=event.widget
    if me==button1:
        print('Hello!')
    elif me ==button2:
        print('You pressed button2')
    else:
        raise VallueError()

root=tkinter.Tk()

button1=tkinter.Button(root,text="Button1",command=button1_command)
button1             .bind("<Button>",print_hello)
button1.pack()

button2=tkinter.Button(root,text="Button2")
button2.bind("<Button>",print_hello)
button2.pack()
root.mainloop()
