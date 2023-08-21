import turtle
import math

tatita = turtle.Turtle()

def desenha_casa(x):
    # desenhar parede
    tatita.fillcolor("purple")
    tatita.begin_fill() 
    for _ in range(2):
        tatita.forward(7 * x / 3)
        tatita.left(90)
        tatita.forward(x)
        tatita.left(90)
    tatita.end_fill()
    
    # posicionar p desenhar porta
    tatita.forward(x/3)
    tatita.left(90)
    
    # desenhar porta
    tatita.fillcolor("grey")
    tatita.begin_fill() 
    tatita.forward(2*x/3)
    tatita.right(90)
    tatita.forward(x/3)
    tatita.right(90)
    tatita.forward(2*x/3)
    tatita.end_fill() 
    
    # posicionar 1 janela
    tatita.up() # para n riscar enquanto anda
    tatita.left(90)
    tatita.forward(x/3)
    tatita.left(90)
    tatita.forward(x/3)
    tatita.down() # volta a riscar
    
    # desenha 1 janela
    tatita.fillcolor("yellow")
    tatita.begin_fill()
    for _ in range(4):
        tatita.forward(x/3)
        tatita.right(90)
    tatita.end_fill()
        
    # posicionar 2 janela
    tatita.up()
    tatita.right(90)
    tatita.forward(2*x/3)
    tatita.down()
    
    # desenha 2 janela
    tatita.fillcolor("green")
    tatita.begin_fill()
    for _ in range(4):
        tatita.forward(x/3)
        tatita.left(90)
    tatita.end_fill()
    
    # posicionar telhado
    tatita.up()
    tatita.left(90)
    tatita.forward(2*x/3)
    tatita.right(90)
    tatita.down()
    
    #desenha telhado
    tatita.fillcolor("red")
    tatita.begin_fill()
    tatita.forward(x)
    tatita.left(135)
    tatita.forward(x * math.sqrt(4.5))
    tatita.left(90)
    tatita.forward(x * math.sqrt(4.5))
    tatita.left(135)
    tatita.forward(9*x/3)
    tatita.end_fill()
    
    # indica conclusão
    turtle.done()  
dimencao = 100
# dimencao = int(input('Qual será a dimenção base da casinha? '))
desenha_casa(dimencao)

'''Pintar a casa;
Incluir beirais no telhado;
Incluir uma segunda janela ao lado da primeira
reposicionando a primeira para que haja simetria na casa.'''