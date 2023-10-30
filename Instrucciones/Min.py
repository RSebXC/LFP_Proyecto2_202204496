from Abstract.Abstract import Expression

class Min(Expression):

        def __init__(self,campo,  texto,Res, fila, columna):
            self.texto = texto
            self.campo = campo
            self.Res = Res

            super().__init__(fila, columna)

        def setTexto(self,valor):
            self.texto = valor

        def setRes(self,valor):
            self.Res = valor

        def operar(self, arbol):
            pass

        def ejecutarT(self):
                print(self.campo)
                print(self.texto)
                print(self.Res)
                if self.campo in self.texto:
                    suma_campos = 0
                    contador_registros = 0
                    posicion = 0
                    for num in self.texto:
                        if num == self.campo:
                            break
                        posicion += 1

                    result = float("inf")  # Inicializar result como el valor positivo infinito
                    for registro in self.Res:
                        if isinstance(registro.ejecutarT()[posicion], (int, float)):
                            suma_campos = registro.ejecutarT()[posicion]
                            contador_registros += 1

                            if suma_campos < result:
                                result = suma_campos

                    return '\n' + str(result)

                return " "

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()