def es_numero (valor):
    """
    Verifica si el valor ingresado puede convertirse a float.
    Args:
        valor (str o int o float): Valor a verificar.
    Returns:
        float: El valor convertido a float si es válido.
    Raises:
        ValueError: Si el valor no es un número.
    """
    try:
        return float (valor)
    except (ValueError, TypeError):
        raise ValueError(f"'{valor}' no es un número válido.")

def no_vacio (valor):
    """
    Verifica que el valor no esté vacío.
    Args:
        valor (str o int o float): Valor a verificar.
    Returns:
        valor (str o int o float): Si no está vacío.
    Raises:
        ValueError: Si está vacío.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError("El valor no puede estar vacío.")
    return valor

def validar_division(divisor):
    """
    Verifica que el divisor no sea cero.
    Args:
        divisor (int o float): Número a verificar.
    Returns:
        divisor (float): Si es válido.
    Raises:
        ValueError: Si el divisor es 0.
    """
    if float(divisor) == 0:
        raise ValueError("No se puede dividir entre 0.")
    return float(divisor)
