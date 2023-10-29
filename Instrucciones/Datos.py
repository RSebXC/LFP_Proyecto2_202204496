from Abstract.Abstract import Expression

class Datos(Expression):

    def __init__(self, clave, registros, fila, columna):
        self.clave = clave
        self.registros = registros
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        clave_str = ", ".join(map(str, self.clave))
        registros_str = ", ".join(map(str, self.registros))
        return f"Clave: {clave_str}, Registros: [{registros_str}]"

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()