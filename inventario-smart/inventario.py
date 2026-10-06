#!/usr/bin/env python3
"""
InventarioSmart - Sistema simple de control de inventario
Para empresas de retail (ejemplo: TechStore Panamá)
Autor: [Tu Nombre]
Fecha: Octubre 2026
"""

import csv
import os
from datetime import datetime

ARCHIVO_INVENTARIO = "inventario.csv"
UMBRAL_MINIMO = 10  # Alerta cuando el stock es menor o igual a este valor


def inicializar_inventario():
    """Crea el archivo CSV si no existe."""
    if not os.path.exists(ARCHIVO_INVENTARIO):
        with open(ARCHIVO_INVENTARIO, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "categoria", "cantidad", "precio_unitario", "ultima_actualizacion"])
            # Datos de ejemplo
            writer.writerow([1, "Laptop HP 15", "Computadoras", 25, 650.00, datetime.now().strftime("%Y-%m-%d")])
            writer.writerow([2, "Mouse Logitech", "Periféricos", 8, 25.50, datetime.now().strftime("%Y-%m-%d")])
            writer.writerow([3, "Monitor Samsung 24", "Monitores", 15, 180.00, datetime.now().strftime("%Y-%m-%d")])
            writer.writerow([4, "Teclado Mecánico", "Periféricos", 5, 75.00, datetime.now().strftime("%Y-%m-%d")])
            writer.writerow([5, "SSD 1TB", "Almacenamiento", 30, 95.00, datetime.now().strftime("%Y-%m-%d")])
        print("✓ Inventario inicializado con datos de ejemplo.")


def cargar_inventario():
    """Lee el inventario desde el CSV y lo retorna como lista de diccionarios."""
    productos = []
    with open(ARCHIVO_INVENTARIO, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            productos.append({
                "id": int(fila["id"]),
                "nombre": fila["nombre"],
                "categoria": fila["categoria"],
                "cantidad": int(fila["cantidad"]),
                "precio_unitario": float(fila["precio_unitario"]),
                "ultima_actualizacion": fila["ultima_actualizacion"]
            })
    return productos


def guardar_inventario(productos):
    """Guarda la lista de productos en el CSV."""
    with open(ARCHIVO_INVENTARIO, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nombre", "categoria", "cantidad", "precio_unitario", "ultima_actualizacion"])
        for p in productos:
            writer.writerow([
                p["id"], p["nombre"], p["categoria"], p["cantidad"],
                p["precio_unitario"], p["ultima_actualizacion"]
            ])


def mostrar_inventario(productos):
    """Muestra el inventario de forma legible."""
    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'NOMBRE':<25} {'CATEGORÍA':<15} {'STOCK':<8} {'PRECIO':<10} {'ACTUALIZADO'}")
    print("=" * 80)
    for p in productos:
        alerta = " ⚠ BAJO" if p["cantidad"] <= UMBRAL_MINIMO else ""
        print(f"{p['id']:<5} {p['nombre']:<25} {p['categoria']:<15} {p['cantidad']:<8} ${p['precio_unitario']:<9.2f} {p['ultima_actualizacion']}{alerta}")
    print("=" * 80)
    print(f"Total de productos: {len(productos)}")


def alertas_stock_bajo(productos):
    """Muestra solo los productos con stock bajo."""
    bajos = [p for p in productos if p["cantidad"] <= UMBRAL_MINIMO]
    if not bajos:
        print("\n✓ No hay productos con stock bajo.")
        return
    print("\n⚠ PRODUCTOS CON STOCK BAJO (≤ {} unidades):".format(UMBRAL_MINIMO))
    for p in bajos:
        print(f"  - {p['nombre']}: {p['cantidad']} unidades (Categoría: {p['categoria']})")


def actualizar_stock(productos):
    """Permite sumar o restar unidades de un producto."""
    mostrar_inventario(productos)
    try:
        id_prod = int(input("\nIngrese el ID del producto a actualizar: "))
        producto = next((p for p in productos if p["id"] == id_prod), None)
        if not producto:
            print("✗ ID no encontrado.")
            return
        print(f"Producto seleccionado: {producto['nombre']} (Stock actual: {producto['cantidad']})")
        operacion = input("¿Desea sumar (+) o restar (-)? ").strip()
        cantidad = int(input("Cantidad: "))
        if operacion == "+":
            producto["cantidad"] += cantidad
        elif operacion == "-":
            if cantidad > producto["cantidad"]:
                print("✗ No hay suficiente stock.")
                return
            producto["cantidad"] -= cantidad
        else:
            print("✗ Operación no válida.")
            return
        producto["ultima_actualizacion"] = datetime.now().strftime("%Y-%m-%d")
        guardar_inventario(productos)
        print(f"✓ Stock actualizado. Nuevo stock: {producto['cantidad']}")
    except ValueError:
        print("✗ Entrada no válida. Use solo números.")


def valor_total_inventario(productos):
    """Calcula el valor total del inventario."""
    total = sum(p["cantidad"] * p["precio_unitario"] for p in productos)
    print(f"\n💰 Valor total del inventario: ${total:,.2f}")


def menu():
    """Menú principal del sistema."""
    inicializar_inventario()
    while True:
        print("\n" + "─" * 40)
        print("   INVENTARIOSMART - TechStore Panamá")
        print("─" * 40)
        print("1. Ver inventario completo")
        print("2. Ver alertas de stock bajo")
        print("3. Actualizar stock (entrada/salida)")
        print("4. Ver valor total del inventario")
        print("5. Salir")
        opcion = input("\nSeleccione una opción: ").strip()

        productos = cargar_inventario()

        if opcion == "1":
            mostrar_inventario(productos)
        elif opcion == "2":
            alertas_stock_bajo(productos)
        elif opcion == "3":
            actualizar_stock(productos)
        elif opcion == "4":
            valor_total_inventario(productos)
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("✗ Opción no válida.")


if __name__ == "__main__":
    menu()
