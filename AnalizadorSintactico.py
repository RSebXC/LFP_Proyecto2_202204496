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
global n_linea
global n_columna
global lista_lexemas_sintacticos
global instrucciones_sintacticas
lista_errores = []

def calcular_promedio(registros, campo):
    try:
        valores = [registro.get(campo) for registro in registros]
        valores_numericos = [float(valor) for valor in valores if isinstance(valor, (int, float))]
        if valores_numericos:
            promedio = sum(valores_numericos) / len(valores_numericos)
            return promedio
        else:
            raise ValueError("No hay valores numéricos en el campo especificado.")
    except KeyError:
        raise KeyError(f"El campo '{campo}' no existe en los registros.")
    except Exception as e:
        raise Exception(f"Error al calcular el promedio: {str(e)}")
    
def calcular_suma(registros, campo):
    try:
        valores = [registro.get(campo) for registro in registros]
        valores_numericos = [float(valor) for valor in valores if isinstance(valor, (int, float))]
        if valores_numericos:
            promedio = sum(valores_numericos)
            return promedio
        else:
            raise ValueError("No hay valores numéricos en el campo especificado.")
    except KeyError:
        raise KeyError(f"El campo '{campo}' no existe en los registros.")
    except Exception as e:
        raise Exception(f"Error al calcular el promedio: {str(e)}")

def instrucciones_sintactico(lista_lexemas):

    global lista_errores

    instrucciones_sintacticas = []
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
                            return DeclaracionClaves(palabra_reservada.lexema, lista_elementos, lex.getFila(), lex.getColumna())
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
                            
                        elif type(llave_izq.operar(None)) in [int,str,float]:
                            valor = llave_izq.lexema
                            valores_registro[contador]=valor
                            
                            contador += 1
                            
                        elif llave_izq.operar(None) == ']':
                            print("Termino el registro")
                            break
                            
                        else:
                            lista_errores.append(Errores(llave_izq.lexema, "Sintáctico", llave_izq.getFila(), llave_izq.getColumna()))
                    
                else:
                    lista_errores.append(Errores(corchete_izq.lexema, "Sintáctico", corchete_izq.getFila(), corchete_izq.getColumna()))
            else:
                lista_errores.append(Errores(igual.lexema, "Sintáctico", igual.getFila(), igual.getColumna()))


        if lexema.operar(None) == 'imprimir':
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
                                return ImprimirLn(texto.lexema + "\n", lexema.getFila(), lexema.getColumna())


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
            print("encontramos promedio")
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                print("el primer parentesis se logro")
                lexema = lista_lexemas.pop(0)
                if lexema.tipo == 'TEXTO':
                    if lexema.operar(None) == ')':
                        lexema = lista_lexemas.pop(0)
                        print("ya pasmos los parentesis")
                        campo = lexema.lexema.strip('"')  # Elimina las comillas del campo
                        print("eliminamos comillas")
                        try:
                            resultado = calcular_promedio(valores_registro, campo)
                            return resultado
                        except Exception as e:
                            # Error al calcular el promedio
                            lista_errores.append(Errores(str(e), "Sintáctico", lexema.getFila(), lexema.getColumna()))
                    
                else:
                    # Error: formato incorrecto para el campo
                    lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))
            else:
                # Error: falta paréntesis derecho
                lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))


        elif lexema.operar(None) == 'suma':
            print("Si encontramos suma")
            lexema = lista_lexemas.pop(0)
            if lexema.operar(None) == '(':
                lexema = lista_lexemas.pop(0)
                print("Lista de lexemas después de procesar 'promedio(':")
                print(lexema.tipo)
                if lexema.tipo == 'TEXTO':
                    campo = lexema.lexema
                    lexema = lista_lexemas.pop(0)
                    if lexema.tipo == '"':
                        lexema = lista_lexemas.pop(0) 
                        if lexema.operar(None) == ')':
                            try:
                                resultado = calcular_promedio(registros, campo)
                                return resultado
                            except Exception as e:
                                # Error al calcular el promedio
                                lista_errores.append(Errores(str(e), "Sintáctico", lexema.getFila(), lexema.getColumna()))
                        else:
                            # Error: falta paréntesis derecho
                            lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))
                    else:
                        # Error: falta paréntesis derecho
                        lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))
                else:
                    # Error: el contenido debe estar entre comillas
                    lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))
            else:
                # Error: falta paréntesis izquierdo
                lista_errores.append(Errores(lexema.lexema, "Sintáctico", lexema.getFila(), lexema.getColumna()))


        
        elif lexema.operar(None) == 'contarsi':
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                texto = lista_lexemas.pop(0)
                coma = lista_lexemas.pop(0)
                valor = lista_lexemas.pop(0)
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    instruccion = f"FuncionContarSi: {texto.lexema}, {valor.lexema}"
                    instrucciones_sintacticas.append(instruccion)
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))


        elif lexema.operar(None) == 'datos':
            print("encontramos datos")
            parentesis_izq = lista_lexemas.pop(0)
            if parentesis_izq.operar(None) == '(':
                parentesis_der = lista_lexemas.pop(0)
                if parentesis_der.operar(None) == ')':
                    # Crear una lista con los elementos de lista_elementos
                    print(lista_elementos)
                    print(registros)
                    elementos = []
                    print("recorremos elementos")
                    for elemento in lista_elementos:
                        elementos.append(elemento)
                        
                    # Crear un diccionario con los valores de valores_registro
                    print("recorremos registros")
                    valores = []
                    for value in registros:
                        value = registros
                        
                    print("Guardamos los datos")
                    return Datos(elementos, valores, parentesis_der.getFila(), parentesis_der.getColumna())
                    
                else:
                    # Error: Falta paréntesis derecho
                    lista_errores.append(Errores(parentesis_der.lexema, "Sintáctico", parentesis_der.getFila(), parentesis_der.getColumna()))
            else:
                # Error: Falta paréntesis izquierdo
                lista_errores.append(Errores(parentesis_izq.lexema, "Sintáctico", parentesis_izq.getFila(), parentesis_izq.getColumna()))