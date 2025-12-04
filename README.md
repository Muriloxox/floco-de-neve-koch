# Floco de Neve de Koch

Uma visualização gráfica do famoso fractal matemático usando Python e a biblioteca Turtle.

📖 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de Cálculo III, com o objetivo de ilustrar conceitos de limites, séries infinitas e geometria fractal.

O algoritmo gera o Floco de Neve de Koch, uma curva matemática famosa por apresentar um paradoxo fascinante:

. Perímetro Infinito: A cada iteração, o comprimento total aumenta, tendendo ao infinito.

. Área Finita: Apesar do perímetro infinito, a área delimitada pela curva converge para um valor finito ($1,6 \times$ a área do triângulo original).

O código utiliza recursividade para desenhar as iterações do fractal, alterando as cores com base na profundidade da recursão.


🧮 A Lógica Matemática (Recursão)

O código baseia-se na função recursiva koch(n, tam). A regra de formação é:

1. Se n == 0 (caso base), desenha uma reta simples.

2. Se n > 0, o segmento é dividido em 4 partes equivalentes a $1/3$ do tamanho original, seguindo os ângulos:

- Avança;

- Vira 60° à esquerda;

- Avança;

- Vira 120° à direita;

- Avança;

- Vira 60° à esquerda;

- Avança.

Isso é repetido 3 vezes em um loop externo para formar o triângulo fechado (o floco de neve).
