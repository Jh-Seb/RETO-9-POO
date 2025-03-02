# RETO-9-POO
Sistema de Geometría en Python

Este repositorio contiene un proyecto en Python que implementa un paquete para trabajar con figuras geométricas. El sistema utiliza herencia, propiedades, métodos de clase y un decorador personalizado para medir el tiempo de ejecución de ciertos cálculos, proporcionando una base sólida para la manipulación y análisis de figuras geométricas.

## Características

- **Propiedades y Encapsulación**:  
  - Uso de `@property` para acceder y modificar de forma controlada los atributos protegidos de las figuras (como vértices, aristas y ángulos internos).

- **Métodos de Clase**:  
  - Implementación de un método de clase (`@classmethod`) en la clase base que permite definir y cambiar el tipo de figura a nivel de clase.

- **Decorador Personalizado**:  
  - Se utiliza un decorador personalizado para medir el tiempo de ejecución de métodos clave, como el cálculo del área, proporcionando información útil para optimización y depuración.

- **Estructura Modular**:  
  - Clases para representar diferentes tipos de figuras geométricas: *Rectangle*, *Square* y *Triangle*.  
  - Clases auxiliares para representar puntos (`Point`) y líneas (`Line`), utilizadas para calcular vértices, aristas y distancias.

## Estructura del Proyecto

El proyecto se organiza en los siguientes archivos:

- **base_shape.py**:  
  Define la clase base `Shape`, que contiene las propiedades protegidas y métodos abstractos para calcular área, perímetro y ángulos internos. Incluye también un método de clase para definir el tipo de figura y un decorador personalizado para medir tiempos de ejecución.

- **line.py**:  
  Contiene la clase `Line`, que representa una línea entre dos puntos y calcula su longitud.

- **point.py**:  
  Define la clase `Point` para representar coordenadas 2D y calcular la distancia entre dos puntos.

- **rectangle.py**:  
  Implementa la clase `Rectangle`, heredada de `Shape`, con métodos para calcular área, perímetro, vértices, ángulos internos y aristas. Utiliza el decorador para medir el tiempo de ejecución del cálculo del área.

- **square.py**:  
  La clase `Square` hereda de `Rectangle` y representa un cuadrado (figura regular con lados iguales). Se define el tipo de figura como "Square" mediante un método de clase.

- **triangle.py**:  
  Implementa la clase `Triangle`, que hereda de `Shape`, e incluye métodos para calcular área, perímetro, vértices, aristas y ángulos internos, con un decorador para medir el tiempo del cálculo del área.

- **main.py**:  
  Archivo de ejemplo que crea instancias de `Square`, `Rectangle` y `Triangle`, y muestra sus áreas, perímetros y el tipo de figura definido. Cada cálculo relevante (por ejemplo, el área) muestra el tiempo de ejecución medido por el decorador.
