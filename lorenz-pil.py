# -*- encoding: utf-8 -*-
# Lorenz Attractor (projected onto XY-plane)
# http://en.wikipedia.org/wiki/Lorenz_attractor
# Basado en http://code.activestate.com/recipes/577814-lorenz-attractor/

import random
from PIL import Image
imgx = 1024
imgy = 768
imagen = Image.new("RGBA", (imgx, imgy))

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print fib(5)

maxIt = 100000 # Números de pixels a dibujar
size = 30
xa = -size
xb = size
ya = -size
yb = size

# estados iniciales
x = random.random() * size * 2 - 1
y = random.random() * size * 2 - 1
z = random.random() * size * 2 - 1

# dx/dt = delta * (y - x)
# dy/dt = r * x - y - x * z
# dz/dt = x * y - b * z
delta = float(10) # Número de Prandtl https://es.wikipedia.org/wiki/N%C3%BAmero_de_Prandtl
r = float(28)
b = float(8) / 3
h = 1e-3 # tiempo del paso
def Lorenz(x, y, z):
    dx_dt = delta * (y - x)
    dy_dt = r * x - y - x * z
    dz_dt = x * y - b * z
    x += dx_dt * h
    y += dy_dt * h
    z += dz_dt * h
    return (x, y, z)

for i in range(maxIt):
    (x, y, z) = Lorenz(x, y, z)#; imprime x, y, z
    xi = int((imgx - 1) * (x - xa) / (xb - xa))
    yi = int((imgy - 1) * (y - ya) / (yb - ya))
    if xi >=0 and xi < imgx and yi >= 0 and yi < imgy:
        imagen.putpixel((xi, yi), (0, 0, 0))
    

nombre = "Lorenz_%i.gif" % size;
print nombre
imagen.save( nombre, "GIF", transparency=0)
