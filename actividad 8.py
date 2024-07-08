#8

nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.21
precio_con_iva = precio + iva
print("Producto:", nombre_producto)
print("Precio sin IVA:", precio)
print("IVA:", iva)
print("Precio con IVA:", precio_con_iva)
