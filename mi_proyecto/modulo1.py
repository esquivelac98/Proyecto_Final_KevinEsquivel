import csv, pandas as pd

def ingresar_ventas(ventas):
    while True:
        try:
            curso = input('Ingrese el nombre del curso: ').upper()
            cantidad = int(input('Ingrese la cantidad de cursos: '))
            fecha = input('Ingrese la fecha de la venta (YYYY-MM-DD): ')
            precio = float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entrdas no valida, por favor intentelo nuevamente!')
            continue
        
        venta = {
            'Curso': curso,
            'Cantidad': cantidad,
            'Fecha': fecha,
            'Precio': precio,
            'Cliente': cliente
        }
        ventas.append(venta)
        
        continuar = input('¿Desea ingresar otra venta s/n: ').lower()
        if continuar == 's':
            print('\n***Ingresando una venta nueva en el sistema***\n')
        elif continuar == 'n':
            break
        else:
            print('Opción no válida, saliendo del módulo de ventas.')
            
def guardar_ventas(ventas):
    if not ventas:
        print('No hay información para almacenar.')
    else:
        try:
            with open('ventas.csv', 'w', newline='') as archivo:
                guardar = csv.DictWriter(archivo, fieldnames=['Curso', 'Cantidad', 'Fecha', 'Precio', 'Cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
            print('La información ha sido guardada con éxito.')
            pass
        except Exception as e:
            print(f'Error al guardar el archivo {e}.')
            
def analizar_ventas():
    df = pd.read_csv('ventas.csv')
    print('\n *** Resumen de Ventas ***')
    df['Monto_total'] = df['Cantidad'] * df['Precio']
    print(f'El total de ventas es de: {df['Monto_total'].sum():.2f}')
    
    if not df.empty:
        curso_mas_vendido = df.groupby('Curso')['Cantidad'].sum().idxmax()
        print(f'El curso más vendido es: {curso_mas_vendido}')
        cliente_top = df.groupby('Cliente')['Monto_total'].sum().idxmax()
        print(f'El cliente top es: {cliente_top}')
    else:
        print('No existen datos para analizar, por favor registre ventas.')
    
    print('\nVentas por fecha:')
    print(df.groupby('Fecha')['Monto_total'].sum().round(2))