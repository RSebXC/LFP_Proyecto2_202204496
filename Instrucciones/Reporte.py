from Abstract.Abstract import Expression

class Reporte(Expression):

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
        
        clave_str = " ".join(self.clave[0])
        
        return "\n"+ clave_str + " \n" + registros_str

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
    
    def generarHTML(self):
        registros_str = ""
        clave_str = " ".join(self.clave[0])  # Convertir la lista de claves a una cadena

        # Construir las filas de la tabla HTML con los registros
        for info in self.registros:
            registros_str += "<tr>"
            for dato in info.ejecutarT():
                registros_str += "<td>{}</td>".format(dato)
            registros_str += "</tr>"

        # Crear la tabla HTML completa con claves y registros
        tabla_html = """
        <table border="1">
            <thead>
                <tr>{}</tr>
            </thead>
            <tbody>
                {}
            </tbody>
        </table>
        """.format(clave_str, registros_str)

        return tabla_html