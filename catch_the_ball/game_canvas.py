import tkinter

def paint(event):
    """ Обработчик события для холста
    :param event:
    :return:
    """
    print(event.x,event.y)
    if event.widget !=canvas:
        print('Странно, ведь paint() привязывали только к canvas...')
        return
    canvas.coords(line,0,0,event.x,event.y)
root=tkinter.Tk()

canvas = tkinter.Canvas(root)
canvas.bind("<Motion>",paint)
canvas.pack()

line = canvas.create_line(0,0,10,10)


root.mainloop()
print("Эта строка будет достигнута только при выходе из приложения.")
