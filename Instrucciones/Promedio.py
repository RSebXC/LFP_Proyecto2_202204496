from Abstract.Abstract import Expression

class Promedio(Expression):

        def __init__(self,campo,  texto, fila, columna):
            self.texto = texto
            self.campo = campo
            super().__init__(fila, columna)

        def setTexto(self,valor):
            self.texto = valor

        def operar(self, arbol):
            pass

        def ejecutarT(self):
            if campo_nombre in lista_elementos:  
                        suma_campos = 0
                        contador_registros = 0
                        posicion = 0
                        for num in lista_elementos:
                            if num == campo_nombre:
                                break
                            posicion += 1

                        for registro in registros:
                            if  isinstance(registro[posicion], (int, float)):
                                suma_campos += registro[posicion]
                                contador_registros += 1

                        if contador_registros > 0:
                            promedio = suma_campos / contador_registros
                            return Promedio(str(promedio), lexema.getFila(), lexema.getColumna())
                        else:
                            # No se encontraron registros válidos para calcular el promedio
                            lista_errores.append(Errores(f"No se encontraron registros válidos para el campo '{campo_nombre}'", "Semántico", campo.getFila(), campo.getColumna()))
                    else:
                        # Error: Campo no existe en los registros
                        lista_errores.append(Errores(f"Campo '{campo_nombre}' no existe en los registros", "Semántico", campo.getFila(), campo.getColumna()))
            return self.texto

        def getFila(self):
            return super().getFila()

        def getColumna(self):
            return super().getColumna()