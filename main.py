import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import filedialog, messagebox
import subprocess
from AnalizadorLexico import *
from AnalizadorSintactico import *


class InterfazGrafica:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Proyecto2-202204496")

        # Navbar
        self.navbar = tk.Menu(self.ventana, bg="red", fg="white")
        self.ventana.config(menu=self.navbar)

        # Menú Archivo
        self.menu_archivo = tk.Menu(self.navbar, tearoff=0, bg="red", fg="white")
        self.menu_archivo.add_command(label="Cargar archivo", command=self.cargar_archivo)
        self.navbar.add_cascade(label="Archivo", menu=self.menu_archivo)

        # Menú Reportes
        self.menu_reportes = tk.Menu(self.navbar, tearoff=0, bg="red", fg="white")
        self.menu_reportes.add_command(label="Reporte de Tokens", command=self.generar_reporte_tokens)
        self.menu_reportes.add_command(label="Reporte de Errores", command=self.generar_reporte_errores)
        self.menu_reportes.add_command(label="Árbol de derivación", command=self.generar_arbol_derivacion)
        self.navbar.add_cascade(label="Reportes", menu=self.menu_reportes)

        # Botón Analizar archivo
        self.navbar.add_command(label="Analizar texto", command=self.analizar_archivo)

        # Barra de números de línea
        self.line_number_bar = tk.Text(ventana, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        # Área de texto principal
        self.area_texto = tkst.ScrolledText(self.ventana, wrap=tk.WORD,fg="yellow", bg="black", insertbackground="white")
        self.area_texto.pack(expand=True, fill='both',side=tk.LEFT)

        self.area_texto.bind('<Key>', self.update_line_numbers)
        self.area_texto.bind('<MouseWheel>', self.update_line_numbers)

        # Consola de salida
        self.consola = tkst.ScrolledText(self.ventana, wrap=tk.WORD,fg="aqua", bg="black", insertbackground="white")
        self.consola.pack(expand=True, fill='both',side=tk.LEFT)
        self.consola.config(state='disabled')

        self.current_line = 1


    def cargar_archivo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos .bizdata", "*.bizdata")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.area_texto.delete(1.0, tk.END)
                self.area_texto.insert(tk.END, content)
            self.update_line_numbers()

    def update_line_numbers(self, event=None):
        line_count = self.area_texto.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count

    def analizar_archivo(self):
        # Obtén el código del área de texto
        code = self.area_texto.get(1.0, tk.END)
        imprimir_consola = ''
        try:
            # Ejecuta el análisis léxico
            instrucciones_lexico = instruccion(code)
            lista_instrucciones = []
            while True:
                instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
                if instrucciones_lenguaje:
                    lista_instrucciones.append(instrucciones_lenguaje)
                else:
                    break

            # Ejecutar instrucciones

            for elemento in lista_instrucciones:
                if isinstance(elemento, DeclaracionClaves):
                    continue
                elif isinstance(elemento, Imprimir):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, ImprimirLn):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, Comentario):
                    continue
                elif isinstance(elemento, Cadena):
                    continue
                elif isinstance(elemento, Registros):
                    continue
                elif isinstance(elemento, Conteo):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, Promedio):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, Contarsi):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, Datos):
                    imprimir_consola += elemento.ejecutarT()
            print(imprimir_consola)

                    # Muestra el resultado en la consola de salida
            self.consola.config(state='normal')
            self.consola.delete(1.0, tk.END)
            self.consola.insert(tk.END, imprimir_consola)
            self.consola.config(state='disabled')
            messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")

        except Exception as e:
            messagebox.showerror("Error",f"Ocurrió un error al analizar el código: {str(e)}")
            print("Ocurrió un error al analizar el código: ", e)


    def run_analysis(self, code):
        # Aquí puedes realizar el análisis del código, por ejemplo, usando subprocess
        try:
            # Ejemplo: Ejecutar un comando de consola y capturar la salida
            result = subprocess.check_output(["python", "-c", code], universal_newlines=True, stderr=subprocess.STDOUT)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def generar_reporte_tokens(self):
        # Implementar lógica para generar el reporte de tokens
        pass

    def generar_reporte_errores(self):
        # Implementar lógica para generar el reporte de errores
        pass

    def generar_arbol_derivacion(self):
        # Implementar lógica para generar el árbol de derivación
        pass

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazGrafica(ventana_principal)
    ventana_principal.mainloop()
