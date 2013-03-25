class ConjuntoMandelbrot():

	def __init__(self, profundidad):
		self.fractal = []
		inicio = -2 
		fin = 1
		paso = 0.005
		self.profundidad = profundidad
		self.inicializar(inicio, fin, paso)

		for i in range(self.profundidad):
			self.iterar()

	def inicializar(self, inicio, fin, paso):
		self.zs = []
		self.z0 = []
		self.fractal = []
		lado = int((fin - inicio) / paso)
		for x in range(lado):
			self.zs.append([])
			self.z0.append([])
			self.fractal.append([])
			for y in range(lado):
				z = complex(inicio + x * paso, inicio + y * paso)
				self.fractal[x].append(0)
				self.zs[x].append(z)
				self.z0[x].append(z)

	def iterar(self):
		for x in range(len(self.zs)):
			for y in range(len(self.zs)):
				if abs(self.zs[x][y]) < 2 :
					self.zs[x][y] = (self.zs[x][y]**2) + self.z0[x][y]
					self.fractal[x][y]+=1
		return self.fractal