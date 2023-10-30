from Abstract.Abstract import Expression

class Datos(Expression):

    def __init__(self, clave, registros, fila, columna):
        self.clave = clave
        self.registros = registros
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def serRegistros(self, dato):
        self.registros = dato

    def serClaves(self, dato):
        self.clave = dato

    def ejecutarT(self):
        registros_str = " "
        clave_str = " " 
        
        for info in self.registros:
            
            registros_str += str(info.ejecutarT()[0]) + " " + str(info.ejecutarT()[1]) + " " + str(info.ejecutarT()[2]) + " " + str(info.ejecutarT()[3]) + " " + str(info.ejecutarT()[4]) + "\n "
        
        clave_str = " ".join(self.clave)
        
        return "\n"+ clave_str + " \n" + registros_str

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
    
    