# Manual Técnico para el Analizador Léxico y Sintáctico

---

## 1. Expresiones Regulares para el Analizador Léxico

El Analizador Léxico utiliza expresiones regulares para identificar los patrones léxicos en el código fuente. Estas expresiones regulares se aplican a los caracteres del código fuente para reconocer tokens específicos, como palabras reservadas, números y símbolos especiales. A continuación, se presentan las expresiones regulares utilizadas:

- **Palabras Reservadas y Símbolos Especiales**:
  - **Claves:** `r'Claves'`
  - **Imprimir:** `r'imprimir'`
  - **ImprimirLn:** `r'imprimirln'`
  - **Registros:** `r'Registros'`
  - **Conteo:** `r'conteo'`
  - **Promedio:** `r'promedio'`
  - **ContarSi:** `r'contarsi'`
  - **Datos:** `r'datos'`
  - **Operador Igual:** `r'='`
  - **Corchete Izquierdo:** `r'\['`
  - **Corchete Derecho:** `r'\]'`
  - **Comillas Dobles:** `r'"'`
  - **Coma:** `r','`
  - **Paréntesis Izquierdo:** `r'\('`
  - **Paréntesis Derecho:** `r'\)'`
  - **Punto y Coma:** `r';'`

- **Números Enteros y Decimales**:
  - **Número Entero:** `r'\d+'`
  - **Número Decimal:** `r'\d+\.\d+'`

- **Texto Entre Comillas Dobles**:
  - **Texto:** `r'"[^"]*"'`

---

## 2. Método del Árbol para el Analizador Sintáctico

El Analizador Sintáctico utiliza el Método del Árbol para validar la estructura del código fuente. Este método representa las reglas gramaticales como nodos en un árbol, donde el nodo raíz es la regla de partida y los nodos hijos son las producciones aplicadas. Aquí hay un ejemplo visual:
