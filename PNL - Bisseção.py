# PNL - Bisseção - Grafico
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
xMin = -1.0
xMax = 2.0
yMin = -10.0
yMax = 10.0

# Exibe gráfico f(x) no intervalo fornecido no livro
x_plot = np.linspace(xMin, xMax,100) # 100 pontos no intervalo [0.4,1.8]
f_x_plot = 12*x_plot - 3*x_plot**4 - 2*x_plot**6 # f(x) é declarada considerando o linspace
fig, ax = plt.subplots() # cria figura
ax.grid(True, which = 'both', color = 'grey', linestyle = 'dotted') # configure linhas de grade
ax.axvline(x=0, color ='k')
ax.axhline(y=0, color ='k') # cores dos eixos x e y
ax.axis((xMin, xMax, yMin, yMax)) #limites dos eixos x e y
ax.xaxis.set_minor_locator(AutoMinorLocator(5)) # inclui 5 linhas secundarias para cada linha primaria
ax.yaxis.set_minor_locator(AutoMinorLocator(2)) 
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.plot(x_plot, f_x_plot, color = 'r')
plt.show()

from sympy.core.evalf import evalf
# PNL - Bisseção - Algoritmo
import sympy as sym # biblioteca para matematica simbolica

x = sym.symbols('x') # define variavel
f_x = 12*x - 3*x**4 - 2*x**6 # função f(x)
x_inf = -0 # limite inferior (x sublinhado)
x_sup = 2 # limite superior (x barra)
Epsilon =0.01 # Erro admitido para x*

x_ini = ((x_inf + x_sup)/2) #x_i
Ite = 0
d_f_x = sym.diff(f_x,x) #df(x)\dx
print('Ite ;     df(x)\dx ;     x_inf ;      x_sup; nov x_ini ;  f(x_ini) ;') # imprime cabecalho da tabela
print('%4.d' % Ite, ';             ;', '%9.5f' % x_inf, ';','%9.5f' % x_sup, ';','%9.5f' % x_ini, ';',
      '%10.5f' % f_x.evalf(subs={x:x_ini}),';') # imprime linha de inciação
continuar = True
while continuar: # processo iterativo
  Ite+=1
  valor = d_f_x.evalf(subs={x:x_ini}) # calcula o valor de d_f_x en x=x_ini
  if valor >= 0: #verifica qual limite ajustar
    x_inf = x_ini
  else:
      x_sup = x_ini
  x_ini_novo = ((x_inf + x_sup)/2) #atualizar x_ini
  print('%4.d' % Ite, ';', '%11.5f' % d_f_x.evalf(subs ={x:x_ini}), ';','%9.5f' % x_inf, ';','%9.5f' % x_sup, ';'
        ,'%9.5f' % x_ini_novo, ';','%9.5f' % f_x.evalf(subs={x:x_ini_novo}), ';') # imprime linha de iteração
  x_ini = x_ini_novo
  if (x_sup - x_inf) <= 2*Epsilon: # varifica criterio de parada
    continuar = False
