class Cadenas:

    def __mensaje(self):
        return "Buenas tardes"

    def saludo(self,curso):
        return "EXamen "+curso+" "+self.__mensaje()

class Persona:

    def __init__(self,cedula,nombre,edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad

    def getDatos(self):
        return self.cedula+" "+self.nombre\
               +" "+str(self.edad)

class Empleado(Persona):

    def __init__(self,cedula,nombre,edad,sueldo):
        super().__init__(cedula,nombre,edad)
        self.__sueldo = sueldo

    def setSueldo(self,sueldo):
        self.__sueldo= sueldo

    def getSueldo(self):
        return self.__sueldo

    def getDatos(self):
        return super().getDatos()+" "+str(self.__sueldo)

class Profesor(Persona,Cadenas):

    def __init__(self,cedula,nombre,edad,gestoria):
        super().__init__(cedula,nombre,edad)
        self.gestoria = gestoria

    def getDatos(self):
        return super().getDatos()+" "+self.gestoria
    def saludo(self,curso):
        return "ISTG "+curso

obE = Empleado("12345","SOFIA RAMIREZ",21,700)
obE.cedula="0986534"
obE.__sueldo = 234
obE.setSueldo(1800)

print("Edad modificada por separado ",obE.__sueldo)
print(obE.getDatos())
""" 
obP = Profesor("12345","SOFIA RAMIREZ",21,"PPP")
print(obP.getDatos())
print(obP.saludo("Jose"))
"""
obC = Cadenas()
#obC.__mensaje()
#print(obC.saludo("Complexivo"))


