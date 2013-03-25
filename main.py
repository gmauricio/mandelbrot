from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock

import mandelbrot

class Mandelbrot(Widget):
	
	def create(self, p):
		self.p = p
		self.conjunto = mandelbrot.ConjuntoMandelbrot(p)

	def paint(self):
		self.canvas.clear()
		tam = 1
		with self.canvas:
			for x in range(len(self.conjunto.fractal)):
				for y in range(len(self.conjunto.fractal)):
					rgb = self.obtener_rgb_jet( self.conjunto.fractal[x][y]/float(self.conjunto.profundidad))
					Color( rgb[0], rgb[1], rgb[2])
					Rectangle(pos=(x*tam, y*tam), size=(tam, tam))

	def obtener_rgb_jet(self, valor):
		porCuatro = 4 * valor;
		rojo = min(porCuatro - 1.5, -porCuatro + 4.5)
		verde = min(porCuatro - 0.5, -porCuatro + 3.5)
		azul = min(porCuatro + 0.5, -porCuatro + 2.5)
		return [rojo, verde, azul]

	def actualizar(self, dt):
		self.conjunto.profundidad += 1
		self.conjunto.iterar()
		self.paint()

class MandelbrotApp(App):
    def build(self):
    	mandelbrot = Mandelbrot()
    	mandelbrot.create(100)
    	Clock.schedule_interval(mandelbrot.actualizar, 4)
    	return mandelbrot

if __name__ == '__main__':
	MandelbrotApp().run()