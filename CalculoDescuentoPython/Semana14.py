def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el monto del descuento basado en el porcentaje proporcionado.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (predeterminado es 15%).
    :return: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


#Programa principal
def main():
    #función con solo el monto total
    monto_total_1 = 200
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Monto total: ${monto_total_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}")

    #función con el monto total y un porcentaje de descuento específico
    monto_total_2 = 150
    porcentaje_descuento_2 = 15
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"\nMonto total: ${monto_total_2}")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
