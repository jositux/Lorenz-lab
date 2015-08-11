# -*- encoding: utf-8 -*-
# Lorenz Attractor (projected onto XY-plane)
# http://en.wikipedia.org/wiki/Lorenz_attractor
# Basado en http://code.activestate.com/recipes/577814-lorenz-attractor/

import random
from random import randint
from PIL import Image
imgx = 1024
imgy = 768
imagen = Image.new("RGBA", (imgx, imgy))

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
delta = float(10) # Número de Prandtl
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
        imagen.putpixel((xi, yi), (randint(50,255), randint(0,255), randint(0,255)))
    

nombre = "Lorenz_%i.gif" % size;
print nombre
imagen.save( nombre, "GIF", transparency=0)
