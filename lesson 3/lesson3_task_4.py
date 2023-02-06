from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

#лицо кролика
color('black')
pensize(5)
circle(radius=100)#face

#левый глаз
pu()
goto(-45,92)
pd()
begin_fill()
color((0,0,0),(0,0,0.1))
circle(radius=15)

#правый глаз
pu()
goto(45,92)
pd()
circle(radius=15)
color('red')
end_fill()

#нос
pu()
goto(20,60)
color('pink')
pd()
begin_fill()
goto(-20,60)
goto(0,45)
goto(20,60)
color('pink')
end_fill()

#рот
goto(0,45)
goto(0,40)
seth(-90)
color('black')
circle(10,120)
pu()
goto(0,40)
seth(-90)
pd()
circle(-10,120)

#левое ухо
color('black')
pu()
goto(-60,180)
seth(200)
pd()
circle(radius=350,extent=90)
goto(-98,110)

#правое ухо
pu()
goto(60,180)
seth(-20)
pd()
circle(radius=-350,extent=90)
goto(98,110)

#тело
pu()
goto(20,3)
seth(-25)
pd()
circle(radius=-250,extent=25)
circle(radius=-135,extent=260)
seth(50)
circle(radius=-250,extent=25)

#левая рука
pu()
seth(180)
goto(-30,-3)
pd()
circle(radius=248,extent=30)
circle(radius=29,extent=185)

#правая рука
pu()
seth(0)
goto(30,-3)
pd()
circle(radius=-248,extent=30)
circle(radius=-27,extent=184)

#левая нога
pu()
goto(-162,-260)
pd()
seth(0)
circle(radius=41)

#правая нога
pu()
goto(164,-260)
pd()
circle(radius=41)

done()
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()