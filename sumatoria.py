def sumatoria_cubica(n):
	suma=0
	for i in range(1,n+1):   #loop de 1 a 5
		for j in range(1,i+1):	#loop de 1 a i
			for k in range(j,i+j+1):
				suma=suma+1
	return suma

def sumatoria_constante(n):
	return ((4*(n**3))+(12*(n**2))+(8*n))/12
