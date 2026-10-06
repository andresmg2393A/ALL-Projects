# InventarioSmart 📦

**Sistema simple de control de inventario para empresas de retail**

Desarrollado como proyecto de demostración para el portafolio profesional digital.

\---

## ¿Qué problema resuelve?

Las pequeñas y medianas empresas (PYMES) de retail, especialmente tiendas de tecnología y electrónicos, suelen manejar el inventario en hojas de cálculo o de forma manual. Esto genera:

* Errores de stock (sobreventa o falta de productos)
* Falta de alertas oportunas cuando un producto está por agotarse
* Dificultad para conocer el valor real del inventario en tiempo real

**InventarioSmart** ofrece una solución ligera, sin necesidad de bases de datos complejas ni servidores, que permite:

* Consultar el inventario completo
* Recibir alertas automáticas de stock bajo
* Registrar entradas y salidas de mercancía
* Calcular el valor total del inventario

Ideal para tiendas pequeñas o como prototipo de un sistema más robusto.

\---

## Tecnologías utilizadas

|Tecnología|Uso|
|-|-|
|**Python 3.8+**|Lenguaje principal|
|**csv** (biblioteca estándar)|Almacenamiento de datos|
|**datetime**|Registro de fechas de actualización|
|**os**|Verificación de existencia de archivos|

No requiere dependencias externas (`pip install` no es necesario).

\---

## Cómo instalar y ejecutar

### Requisitos

* Python 3.8 o superior instalado

### Pasos

1. Clona o descarga este repositorio:

```bash
   git clone https://github.com/TU\_USUARIO/inventario-smart.git
   cd inventario-smart
   ```

2. Ejecuta el programa:

```bash
   python inventario.py
   ```

3. La primera vez se creará automáticamente el archivo `inventario.csv` con 5 productos de ejemplo.



### Uso del menú

```
1. Ver inventario completo
2. Ver alertas de stock bajo
3. Actualizar stock (entrada/salida)
4. Ver valor total del inventario
5. Salir
```

\---

## Estructura del proyecto

```
inventario-smart/
├── inventario.py      # Código principal
├── inventario.csv     # Se genera automáticamente (datos)
└── README.md          # Esta documentación
```

\---

## Ejemplo de salida

```
================================================================================
ID    NOMBRE                    CATEGORÍA       STOCK    PRECIO     ACTUALIZADO
================================================================================
1     Laptop HP 15              Computadoras    25       $650.00    2026-10-05
2     Mouse Logitech            Periféricos     8        $25.50     2026-10-05 ⚠ BAJO
3     Monitor Samsung 24        Monitores       15       $180.00    2026-10-05
...
```

\---

## Posibles mejoras futuras

* Interfaz gráfica con Tkinter o Streamlit
* Exportación a Excel / Power BI
* Integración con códigos de barras
* Autenticación de usuarios
* Base de datos SQLite

\---

## Autor

By Andres Llerena ID: 8-875-252

Proyecto desarrollado como parte del **Proyecto N°1 - Marca Personal Profesional en la Era Digital**  
Universidad Tecnológica de Panamá  
Asignatura: Sistemas Colaborativos  
Octubre 2026

