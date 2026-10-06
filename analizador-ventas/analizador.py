#!/usr/bin/env python3
"""
Analizador de Ventas - Generador de reportes para empresas
Ideal para alimentar dashboards de Power BI o reportes gerenciales
Autor: [Tu Nombre]
Fecha: Octubre 2026
"""

import csv
import os
from collections import defaultdict
from datetime import datetime

ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_REPORTE = "reporte_ventas.txt"


def inicializar_datos():
    """Crea archivo de ventas de ejemplo si no existe."""
    if not os.path.exists(ARCHIVO_VENTAS):
        with open(ARCHIVO_VENTAS, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fecha", "producto", "categoria", "cantidad", "precio_unitario", "vendedor", "region"])
            # Datos de ejemplo (octubre 2026)
            datos = [
                ["2026-10-01", "Laptop HP 15", "Computadoras", 2, 650.00, "Ana López", "Panamá"],
                ["2026-10-01", "Mouse Logitech", "Periféricos", 5, 25.50, "Carlos Ruiz", "Colón"],
                ["2026-10-02", "Monitor Samsung 24", "Monitores", 3, 180.00, "Ana López", "Panamá"],
                ["2026-10-02", "SSD 1TB", "Almacenamiento", 4, 95.00, "María Torres", "Chiriquí"],
                ["2026-10-03", "Teclado Mecánico", "Periféricos", 2, 75.00, "Carlos Ruiz", "Colón"],
                ["2026-10-03", "Laptop Dell XPS", "Computadoras", 1, 1200.00, "Ana López", "Panamá"],
                ["2026-10-04", "Mouse Logitech", "Periféricos", 8, 25.50, "María Torres", "Chiriquí"],
                ["2026-10-04", "Monitor LG 27", "Monitores", 2, 250.00, "Carlos Ruiz", "Colón"],
                ["2026-10-05", "SSD 1TB", "Almacenamiento", 6, 95.00, "Ana López", "Panamá"],
                ["2026-10-05", "Laptop HP 15", "Computadoras", 1, 650.00, "María Torres", "Chiriquí"],
                ["2026-10-05", "Teclado Mecánico", "Periféricos", 3, 75.00, "Carlos Ruiz", "Colón"],
                ["2026-10-05", "Auriculares Sony", "Audio", 4, 120.00, "Ana López", "Panamá"],
            ]
            writer.writerows(datos)
        print("✓ Archivo de ventas de ejemplo creado (ventas.csv).")


def cargar_ventas():
    """Carga las ventas desde el CSV."""
    ventas = []
    with open(ARCHIVO_VENTAS, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            ventas.append({
                "fecha": fila["fecha"],
                "producto": fila["producto"],
                "categoria": fila["categoria"],
                "cantidad": int(fila["cantidad"]),
                "precio_unitario": float(fila["precio_unitario"]),
                "vendedor": fila["vendedor"],
                "region": fila["region"],
                "total": int(fila["cantidad"]) * float(fila["precio_unitario"])
            })
    return ventas


def generar_reporte(ventas):
    """Genera un reporte completo y lo guarda en archivo de texto."""
    if not ventas:
        print("No hay datos de ventas.")
        return

    # Totales generales
    total_ventas = sum(v["total"] for v in ventas)
    total_unidades = sum(v["cantidad"] for v in ventas)
    ticket_promedio = total_ventas / len(ventas)

    # Por categoría
    por_categoria = defaultdict(lambda: {"unidades": 0, "monto": 0.0})
    for v in ventas:
        por_categoria[v["categoria"]]["unidades"] += v["cantidad"]
        por_categoria[v["categoria"]]["monto"] += v["total"]

    # Por vendedor
    por_vendedor = defaultdict(lambda: {"unidades": 0, "monto": 0.0})
    for v in ventas:
        por_vendedor[v["vendedor"]]["unidades"] += v["cantidad"]
        por_vendedor[v["vendedor"]]["monto"] += v["total"]

    # Por región
    por_region = defaultdict(lambda: {"unidades": 0, "monto": 0.0})
    for v in ventas:
        por_region[v["region"]]["unidades"] += v["cantidad"]
        por_region[v["region"]]["monto"] += v["total"]

    # Producto más vendido
    por_producto = defaultdict(int)
    for v in ventas:
        por_producto[v["producto"]] += v["cantidad"]
    producto_top = max(por_producto.items(), key=lambda x: x[1])

    # Construir el reporte
    lineas = []
    lineas.append("=" * 70)
    lineas.append("       REPORTE DE VENTAS - TechStore Panamá")
    lineas.append(f"       Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lineas.append("=" * 70)
    lineas.append("")
    lineas.append("▶ RESUMEN GENERAL")
    lineas.append(f"   Total de transacciones : {len(ventas)}")
    lineas.append(f"   Unidades vendidas      : {total_unidades}")
    lineas.append(f"   Ingresos totales       : ${total_ventas:,.2f}")
    lineas.append(f"   Ticket promedio        : ${ticket_promedio:,.2f}")
    lineas.append(f"   Producto más vendido   : {producto_top[0]} ({producto_top[1]} uds)")
    lineas.append("")
    lineas.append("▶ VENTAS POR CATEGORÍA")
    for cat, datos in sorted(por_categoria.items(), key=lambda x: x[1]["monto"], reverse=True):
        lineas.append(f"   {cat:<20} {datos['unidades']:>5} uds   ${datos['monto']:>10,.2f}")
    lineas.append("")
    lineas.append("▶ DESEMPEÑO POR VENDEDOR")
    for vend, datos in sorted(por_vendedor.items(), key=lambda x: x[1]["monto"], reverse=True):
        lineas.append(f"   {vend:<20} {datos['unidades']:>5} uds   ${datos['monto']:>10,.2f}")
    lineas.append("")
    lineas.append("▶ VENTAS POR REGIÓN")
    for reg, datos in sorted(por_region.items(), key=lambda x: x[1]["monto"], reverse=True):
        lineas.append(f"   {reg:<20} {datos['unidades']:>5} uds   ${datos['monto']:>10,.2f}")
    lineas.append("")
    lineas.append("=" * 70)
    lineas.append("Este reporte puede importarse fácilmente a Power BI, Excel o Google Sheets.")
    lineas.append("=" * 70)

    reporte_texto = "\n".join(lineas)

    # Mostrar en consola
    print(reporte_texto)

    # Guardar en archivo
    with open(ARCHIVO_REPORTE, "w", encoding="utf-8") as f:
        f.write(reporte_texto)
    print(f"\n✓ Reporte guardado en: {ARCHIVO_REPORTE}")


def exportar_para_powerbi(ventas):
    """Exporta un CSV limpio listo para Power BI."""
    archivo_pb = "ventas_powerbi.csv"
    with open(archivo_pb, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Fecha", "Producto", "Categoria", "Cantidad", "PrecioUnitario", "Total", "Vendedor", "Region"])
        for v in ventas:
            writer.writerow([
                v["fecha"], v["producto"], v["categoria"], v["cantidad"],
                v["precio_unitario"], v["total"], v["vendedor"], v["region"]
            ])
    print(f"✓ Archivo listo para Power BI generado: {archivo_pb}")


def menu():
    """Menú principal."""
    inicializar_datos()
    while True:
        print("\n" + "─" * 45)
        print("   ANALIZADOR DE VENTAS - TechStore Panamá")
        print("─" * 45)
        print("1. Generar reporte completo")
        print("2. Exportar datos para Power BI / Excel")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ").strip()

        ventas = cargar_ventas()

        if opcion == "1":
            generar_reporte(ventas)
        elif opcion == "2":
            exportar_para_powerbi(ventas)
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("✗ Opción no válida.")


if __name__ == "__main__":
    menu()
