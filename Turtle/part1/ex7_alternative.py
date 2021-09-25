import turtle
import math

turtle.speed(0)
phi = 0
dphi = 4
while True:
	r = phi
	phi_rad = phi * math.pi / 180
	turtle.goto(r * math.cos(phi_rad), r * math.sin(phi_rad))
	phi += dphi