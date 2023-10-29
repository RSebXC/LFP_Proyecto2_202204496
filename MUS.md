**Manual de Usuario para el Analizador Léxico y Sintáctico**

---

### 1. **Introducción**

Este manual proporciona una guía completa sobre el uso del Analizador Léxico y Sintáctico para un lenguaje de programación específico. El analizador está dividido en dos partes: el **Analizador Léxico**, que identifica y clasifica los tokens en el código fuente, y el **Analizador Sintáctico**, que valida la estructura sintáctica del código.

---

### 2. **Requisitos**

Antes de comenzar, asegúrate de tener instalado un entorno de ejecución de Python en tu sistema.

---

### 3. **Descarga e Instalación**

1. **Descarga del Código**: Descarga los archivos del Analizador Léxico y Sintáctico desde el repositorio.

2. **Ejecución del Analizador Léxico**:
   ```bash
   python analizador_lexico.py <archivo_de_entrada>
   ```
   Reemplaza `<archivo_de_entrada>` con la ruta al archivo que deseas analizar léxicamente.

3. **Ejecución del Analizador Sintáctico**:
   ```bash
   python analizador_sintactico.py <archivo_de_entrada>
   ```
   Reemplaza `<archivo_de_entrada>` con la ruta al archivo que deseas analizar sintácticamente.

---

### 4. **Uso del Analizador Léxico**

El Analizador Léxico procesa el código fuente y genera una lista de tokens clasificados. Asegúrate de tener tu archivo de código fuente listo antes de ejecutar el analizador.

#### Ejemplo de Código Fuente:

```python
Claves = ["nombre", "edad", "ciudad"];
Registros = [
    {"nombre": "Alice", "edad": 30, "ciudad": "New York"},
    {"nombre": "Bob", "edad": 25, "ciudad": "Los Angeles"}
];
imprimir("¡Hola, Mundo!");
```

#### Resultado del Analizador Léxico:

```
[('CLAVES', 'Claves'), ('IGUAL', '='), ('CORIZQ', '['), ('COMILLA', '"'), ('TEXTO', 'nombre'), ('COMILLA', '"'), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'edad'), ('COMILLA', '"'), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'ciudad'), ('COMILLA', '"'), ('CORDER', ']'), ('PUNTOYCOMA', ';'), ('REGISTROS', 'Registros'), ('IGUAL', '='), ('CORIZQ', '['), ('LLAVEAPERTURA', '{'), ('COMILLA', '"'), ('TEXTO', 'nombre'), ('COMILLA', '"'), ('IGUAL', '='), ('COMILLA', '"'), ('TEXTO', 'Alice'), ('COMILLA', '"'), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'edad'), ('COMILLA', '"'), ('IGUAL', '='), ('NUMERO', 30), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'ciudad'), ('COMILLA', '"'), ('IGUAL', '='), ('COMILLA', '"'), ('TEXTO', 'New York'), ('COMILLA', '"'), ('LLAVECIERRE', '}'), ('COMA', ','), ('LLAVEAPERTURA', '{'), ('COMILLA', '"'), ('TEXTO', 'nombre'), ('COMILLA', '"'), ('IGUAL', '='), ('COMILLA', '"'), ('TEXTO', 'Bob'), ('COMILLA', '"'), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'edad'), ('COMILLA', '"'), ('IGUAL', '='), ('NUMERO', 25), ('COMA', ','), ('COMILLA', '"'), ('TEXTO', 'ciudad'), ('COMILLA', '"'), ('IGUAL', '='), ('COMILLA', '"'), ('TEXTO', 'Los Angeles'), ('COMILLA', '"'), ('LLAVECIERRE', '}'), ('CORDER', ']'), ('PUNTOYCOMA', ';'), ('IMPRIMIR', 'imprimir'), ('PARIZQ', '('), ('COMILLA', '"'), ('TEXTO', '¡Hola, Mundo!'), ('COMILLA', '"'), ('PARDER', ')'), ('PUNTOYCOMA', ';')]
```

---

### 5. **Uso del Analizador Sintáctico**

El Analizador Sintáctico valida la estructura del código fuente basándose en las reglas sintácticas del lenguaje. Debes tener tu archivo de código fuente listo antes de ejecutar el analizador.

#### Ejemplo de Código Fuente:

```python
Claves = ["nombre", "edad", "ciudad"];
Registros = [
    {"nombre": "Alice", "edad": 30, "ciudad": "New York"},
    {"nombre": "Bob", "edad": 25, "ciudad": "Los Angeles"}
];
imprimir("¡Hola, Mundo!");
```

#### Resultado del Analizador Sintáctico:

```
El análisis sintáctico se completó con éxito. No se encontraron errores sintácticos en el código fuente.
```

---

### 6. **Manejo de Errores**

Si hay errores léxicos o sintácticos en el código fuente, el analizador proporcionará mensajes de error detallados indicando la línea y columna donde se encontraron los errores.

#### Ejemplo de Error Léxico:

```python
Claves = ["nombre", "edad", 123];
```

Resultado del Analizador Léxico:
```
Error léxico en la línea 1, columna 20: Carácter no reconocido '1'.
```

#### Ejemplo de Error Sintáctico:

```python
Claves = ["nombre", "edad", "ciudad";
```

Resultado del Analizador Sintáctico:
```
Error sintáctico en la línea 1, columna 28: Se esperaba ']'.
```

---

Este manual proporciona una visión general del proceso de análisis léxico y sintáctico. Asegúrate de revisar los mensajes de error en caso de problemas y verifica que el código fuente cumpla con las reglas del lenguaje especificado.