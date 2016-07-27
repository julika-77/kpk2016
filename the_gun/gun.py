from tkinter import *
from random import choice,randint

screen_width = 400
screen_height = 300

class Ball:
    initial_number=20
    minimal_radius=15
    maximal_radius=40
    available_colors=['green','blue','red']

    def __init__(self):
        """
        Создаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius,Ball.maximal_radius)
        x = randint(0,screen_width-1-2*R)
        y = randint(0,screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x,y,x+2*R,y+2*R,width=1,
                           fill=fillcolor,outline=fillcolor)

        self._Vx = randint(-2,+2)
        self._Vy = randint(-2,+2)

def init_game():
    """
    Создаем необходимое для игры количество шариков а также объект - пушку
    :return:
    """
    global balls
    balls = [Ball() for i in range(Ball.initial_number)]
    #FIXME еще нужно создать пушку

def init_main_window():
    global root,canvas, scores_text, scores_value
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    canvas = Canvas(root,width=screen_width, height = screen_height,
                    bg = "white")
    scores_text = Entry(root, textvariable=scores_value)
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    canvas.bind('<Button-1>', click_event_handler)

    #FIXME

if __name__=="__main__":
    init_main_window()
    init_game()
    root.mainloop()