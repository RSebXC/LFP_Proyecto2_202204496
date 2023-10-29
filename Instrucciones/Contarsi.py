from Abstract.Abstract import Expression

class Contarsi(Expression):

        def __init__(self, campo,texto, valor, fila, columna):
            self.texto = texto
            super().__init__(fila, columna)

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            return self.texto

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()