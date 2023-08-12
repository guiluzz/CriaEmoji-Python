import cairo
import math

# Criação do arquivo svg e defincição do tamanho da imagem a ser gerada
WIDTH, HEIGHT = 200, 200

surface = cairo.SVGSurface("emoji.svg", WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Gera a circunferência na cor amarela
ctx.arc(100, 100, 80, 0, 2*math.pi)
ctx.set_source_rgb(1, 1, 0)
ctx.fill()

# Desenha as linhas representando os olhos
ctx.move_to(70, 80)
ctx.line_to(90, 80)
ctx.move_to(110, 80)
ctx.line_to(130, 80)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Utilização da curva de Bezier cúbica
ctx.move_to(60, 130)
ctx.curve_to(90, 150, 110, 150, 140, 130)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

surface.finish()

