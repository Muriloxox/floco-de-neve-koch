import turtle

def koch(n, tam):

    if n == 0:
        t.forward(tam)
    else:
        cores = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082"]
        t.pencolor(cores[n % len(cores)])

        koch(n-1, tam/3) #comandos
        t.left(60)
        koch(n-1, tam/3)
        t.right(120)
        koch(n-1, tam/3)
        t.left(60)
        koch(n-1, tam/3)

try:
    L = float(input('Comprimento do segmento (L): '))
    k = int(input('Quantidade de iterações (k): '))
except:
    print('Valores inválidos. (Usando L = 900 e k = 6)')
    L, k = 900, 6

#configuração
t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.penup()
altura = (L * (3**0.5)) / 6  #altura do triângulo equilátero/3
t.goto(-L/2, altura)
t.pendown()

    #desenha o floco
for _ in range(3):
    koch(k, L)
    t.right(120)

turtle.update()
turtle.exitonclick()
