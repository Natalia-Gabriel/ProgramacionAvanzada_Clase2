class Figura:
    pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado*self.lado

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2
    
    def area(self):
        return self.lado1*self.lado2


class Triangulo(Figura):
    def __init__(self, lado1,lado2,lado3):
        self.lado1 = lado1 
        self.lado2 = lado2 
        self.lado3 = lado3 
         
    
    

# Pruebas
c1 = Cuadrado(2)
c2 = Cuadrado(3)
print(c1.perimetro(),"cm")
print(c2.perimetro(),"cm")
print(c1.area(),"cm2")

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print(r1.perimetro(),"cm")
print(r2.perimetro(),"cm")
print(r2.area(),"cm2")


