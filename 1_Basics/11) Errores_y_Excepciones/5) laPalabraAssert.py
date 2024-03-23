def calcular_impuesto(precio, tasa):
    assert precio >= 0, "El precio debe ser mayor o igual a cero"
    assert 0 <= tasa <= 1, "La tasa debe ser un valor entre 0 y 1"
    
    impuesto = precio * tasa
    return impuesto
calcular_impuesto(-7, 0.9) #Este codigo lanzar un error
