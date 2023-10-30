from Errores.Errores import *
from Instrucciones.DeclaracionClaves import *
from Instrucciones.Imprimir import *
from Instrucciones.Registros import *
from Instrucciones.ImprimirLn import *
from Instrucciones.Comentario import *
from Instrucciones.Cadena import *
from Instrucciones.Conteo import *
from Instrucciones.Promedio import * 
from Instrucciones.Contarsi import *
from Instrucciones.Datos import * 
from Instrucciones.Suma import*
from Instrucciones.Min import*
from Instrucciones.Max import*
from Instrucciones.Reporte import*
global n_linea
global n_columna
global lista_lexemas_sintacticos
global instrucciones_sintacticas
lista_errores = []


def instrucciones_sintactico(lista_lexemas):

    global lista_errores
    lista_elementos = []
    valores_registro = {}
    registros = []
    while lista_lexemas:
        
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Claves':
            
            palabra_reservada = lexema
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        if lex.operar(None) == '"':
                            continue
                        elif lex.operar(None) == ',':
                            continue
                        elif lex.operar(None) == ']':
                            print ("Terminamos: " + palabra_reservada.lexema)
                            ele = DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
                            return ele
                        else:

                            lista_elementos.append(lex.lexema)
            else: #! para detectar errores sintácticos
                print("Error sintáctico en la declaración de claves")
                lista_errores.append(Errores(igual.lexema,"Sintáctico", igual.getFila(), igual.getColumna()))
                while lista_lexemas:
                    lex = lista_lexemas.pop(0)
                    lista_errores.append(Errores(lex.lexema, "Sintáctico",lex.getFila(), lex.getColumna()))
                    if lex.operar(None) == ']':
                        print("Final de la declaración de claves")
                        break


        elif lexema.operar(None) == 'Registros':
            igual = lista_lexemas.pop(0)
            if igual.operar(None) == '=':
                corchete_izq = lista_lexemas.pop(0)
                if corchete_izq.operar(None) == '[':
                    
                    
                    contador = 0
                    while lista_lexemas:
                        llave_izq = lista_lexemas.pop(0)
                        if llave_izq.operar(None) == '{':
                            continue
                        elif llave_izq.operar(None) == ',' or llave_izq.operar(None) == '"':
                            continue
                        elif llave_izq.operar(None) == '}':
                            registro = Registros('Registros',valores_registro, llave_izq.getFila(), llave_izq.getColumna())
                            registros.append(registro) 
                            contador = 0
                            valores_registro = {}

                        elif llave_izq.operar(None) == ']':
                            print("Termino el registro")
                            rrr = Registros('Registros',registros, llave_izq.getFila(), llave_izq.getColumna())
                            return rrr
                            
                        elif type(llave_izq.operar(None)) in [int,str,float]:
                            valor = llave_izq.lexema
                            valores_registro[contador]=valor
                            
                            contador += 1
                            

                        
                            
                        else:
                            lista_errores.append(Errores(llave_izq.lexema, "Sintáctico", llave_izq.getFila(), llave_izq.getColumna()))
                    
                else:
                    lista_errores.append(Errores(corchete_izq.lexema, "Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
            else:
                lista_errores.append(Errores(igual.lexema, "Sintáctico", igual.getFila(), igual.getColumna()))


        elif lexema.operar(None) == 'imprimir':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return Imprimir(texto.lexema, lexema.getFila(), lexema.getColumna())
                            

        elif lexema.operar(None) == 'imprimirln':
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                comillas = lista_lexemas.pop(0)
                if comillas.operar(None) == '"':
                    texto = lista_lexemas.pop(0)
                    comillas = lista_lexemas.pop(0)
                    if comillas.operar(None) == '"':
                        parentesis = lista_lexemas.pop(0)
                        if parentesis.operar(None) == ')':
                            punto_coma = lista_lexemas.pop(0)
                            if punto_coma.operar(None) == ';':
                                return ImprimirLn( '\n' +texto.lexema , lexema.getFila(), lexema.getColumna())


        elif lexema.operar(None) == 'comentario':
            return None  # Ignorar comentarios de una línea

        elif lexema.operar(None) == 'comentario multilinea':
            return None #Ignorar comentarios multilinea

        
        if lexema.operar(None) == 'conteo':
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    # Realiza el conteo de llaves de apertura dentro de la entrada de registro
                    count_llaves = 0
                    for lexema in lista_lexemas:
                        if lexema.operar(None) == '{':
                            count_llaves += 1
                    return Conteo(str(count_llaves), lexema.getFila(), lexema.getColumna())
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))

        elif lexema.operar(None) == 'promedio':
            parentesis_izq = lista_lexemas.pop(0)
            print(parentesis_izq.operar(None))
            if parentesis_izq.operar(None) == '(':
                print("primer parentesis")
               
                lista_lexemas.pop(0)
                campo = lista_lexemas.pop(0)
                lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    
                    campo_nombre = campo.lexema
                    print("despues de las comillas")
                    # Verificar si el campo existe en los registros y calcular el promedio
                    return Promedio(campo_nombre," ",None, campo.getFila(), campo.getColumna())
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))

        elif lexema.operar(None) == 'suma':
            parentesis_izq = lista_lexemas.pop(0)
            print(parentesis_izq.operar(None))
            if parentesis_izq.operar(None) == '(':
                print("primer parentesis")
               
                lista_lexemas.pop(0)
                campo = lista_lexemas.pop(0)
                lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    
                    campo_nombre = campo.lexema
                    print("despues de las comillas")
                    # Verificar si el campo existe en los registros y calcular el promedio
                    return Suma(campo_nombre," ",None, campo.getFila(), campo.getColumna())
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))


        elif lexema.operar(None) == 'max':
            parentesis_izq = lista_lexemas.pop(0)
            print(parentesis_izq.operar(None))
            if parentesis_izq.operar(None) == '(':
                print("primer parentesis")
               
                lista_lexemas.pop(0)
                campo = lista_lexemas.pop(0)
                lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    
                    campo_nombre = campo.lexema
                    print("despues de las comillas")
                    # Verificar si el campo existe en los registros y calcular el promedio
                    return Max(campo_nombre," ",None, campo.getFila(), campo.getColumna())
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))

        elif lexema.operar(None) == 'min':
            parentesis_izq = lista_lexemas.pop(0)
            print(parentesis_izq.operar(None))
            if parentesis_izq.operar(None) == '(':
                print("primer parentesis")
               
                lista_lexemas.pop(0)
                campo = lista_lexemas.pop(0)
                lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    
                    campo_nombre = campo.lexema
                    print("despues de las comillas")
                    # Verificar si el campo existe en los registros y calcular el promedio
                    return Min(campo_nombre," ",None, campo.getFila(), campo.getColumna())
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))

        elif lexema.operar(None) == 'contarsi':
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                campo = lista_lexemas.pop(0)
                coma = lista_lexemas.pop(0)
                valor = lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    campo_nombre = campo.lexema.strip('"')
                    valor_buscar = valor.lexema

                    # Verificar si el campo existe en los registros y contar las ocurrencias del valor especificado
                    if campo_nombre in registros[0]:  # Suponiendo que el primer registro tiene todas las claves posibles
                        contador_ocurrencias = 0
                        for registro in registros:
                            if campo_nombre in registro and str(registro[campo_nombre]) == valor_buscar:
                                contador_ocurrencias += 1

                        return Contarsi(str(contador_ocurrencias), lexema.getFila(), lexema.getColumna())
                    else:
                        # Error: Campo no existe en los registros
                        lista_errores.append(Errores(f"Campo '{campo_nombre}' no existe en los registros", "Semántico", campo.getFila(), campo.getColumna()))
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))
        
        
        elif lexema.operar(None) == 'datos':
            
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    # Crear una lista con los elementos de lista_elementos
                    
                       
                    print("Guardamos los datos")
                    return Datos(lista_elementos, registros, parentesis_der.getFila(), parentesis_der.getColumna())
                    
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))

        elif lexema.operar(None) == 'Reporte de HTML de abarroteria':
            
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    # Crear una lista con los elementos de lista_elementos
                    
                       
                    print("Guardamos los datos")
                    return Reporte(lista_elementos, registros, parentesis_der.getFila(), parentesis_der.getColumna())
                    
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))