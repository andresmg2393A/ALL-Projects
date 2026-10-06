# Analizador de Ventas 📊

**Herramienta de análisis de ventas y generación de reportes para empresas**

Desarrollado como proyecto de demostración para el portafolio profesional digital.

\---

## ¿Qué problema resuelve?

Las empresas de retail y distribución necesitan reportes rápidos y claros sobre:

* ¿Cuánto se vendió en un período?
* ¿Qué categorías y productos son los más rentables?
* ¿Cómo se desempeñan los vendedores?
* ¿Qué regiones generan más ingresos?

Muchas veces estos datos están dispersos en archivos CSV o Excel y se requiere tiempo para consolidarlos.

**Analizador de Ventas** automatiza la generación de un reporte ejecutivo y, además, exporta un archivo limpio listo para importar en **Power BI**, Excel o Google Sheets.

\---

## Tecnologías utilizadas

|Tecnología|Uso|
|-|-|
|**Python 3.8+**|Lenguaje principal|
|**csv**|Lectura y escritura de datos|
|**collections.defaultdict**|Agrupaciones eficientes|
|**datetime**|Fecha de generación del reporte|

Sin dependencias externas. Solo biblioteca estándar de Python.

\---

## Cómo instalar y ejecutar

### Requisitos

* Python 3.8 o superior

### Pasos

1. Clona el repositorio:

```bash
   git clone https://github.com/TU\_USUARIO/analizador-ventas.git
   cd analizador-ventas
   ```

2. Ejecuta el programa:

```bash
   python analizador.py
   ```

3. La primera ejecución crea automáticamente `ventas.csv` con datos de ejemplo (12 transacciones de octubre 2026).

### Opciones del menú

```
1. Generar reporte completo          → Crea reporte\_ventas.txt y lo muestra en pantalla
2. Exportar datos para Power BI      → Genera ventas\_powerbi.csv listo para importar
3. Salir
```

\---

## Cómo usar el archivo en Power BI

1. Abre Power BI Desktop
2. Selecciona **Obtener datos → Texto/CSV**
3. Elige el archivo `ventas\_powerbi.csv`
4. Crea visualizaciones (gráficos de barras por categoría, mapa por región, ranking de vendedores, etc.)

\---

## Estructura del proyecto

```
analizador-ventas/
├── analizador.py          # Código principal
├── ventas.csv             # Datos de ejemplo (se genera automáticamente)
├── reporte\_ventas.txt     # Se genera al ejecutar la opción 1
├── ventas\_powerbi.csv     # Se genera al ejecutar la opción 2
└── README.md              # Esta documentación
```

\---

## Ejemplo de reporte generado

```
======================================================================
       REPORTE DE VENTAS - TechStore Panamá
       Generado: 2026-10-05 21:45:12
======================================================================

▶ RESUMEN GENERAL
   Total de transacciones : 12
   Unidades vendidas      : 41
   Ingresos totales       : $8,XXX.XX
   Ticket promedio        : $XXX.XX
   Producto más vendido   : Mouse Logitech (13 uds)

▶ VENTAS POR CATEGORÍA
   Computadoras             XX uds   $X,XXX.XX
   Periféricos              XX uds   $X,XXX.XX
   ...
```

\---

## Posibles mejoras futuras

* Lectura de múltiples archivos CSV (consolidación)
* Gráficos con matplotlib o plotly
* Conexión directa a base de datos o Google Sheets
* Filtros por rango de fechas
* Envío automático del reporte por correo

\---

## Autor

By Andres Llerena 8-875-252

Proyecto desarrollado como parte del **Proyecto N°1 - Marca Personal Profesional en la Era Digital**  
Universidad Tecnológica de Panamá  
Asignatura: Sistemas Colaborativos  
Octubre 2026

