def calcular_salario_base(independiente):
    # Acceder al atributo 'salairo_base' del objeto Independiente
    salairo_base = independiente.salairo_base
    return salairo_base

def calcular_ibc(independiente):
    salairo_base = calcular_salario_base(independiente)
    # Supongamos que el IBC es un porcentaje del salario base, por ejemplo, el 40%
    ibc = salairo_base * 0.4
    return ibc

def calcular_salud(independiente):
    ibc = calcular_ibc(independiente)
    # Supongamos que la salud es el 12.5% del IBC
    salud = ibc * 0.125
    return salud

def calcular_pension(independiente):
    ibc = calcular_ibc(independiente)
    # Supongamos que la pensión es el 16% del IBC
    pension = ibc * 0.16
    return pension

def calcular_arl(independiente):
    ibc = calcular_ibc(independiente)
    # Supongamos que la ARL es el 0.522% del IBC
    arl = ibc * 0.00522
    return arl

def calcular_ccf(independiente):
    ibc = calcular_ibc(independiente)
    # Supongamos que el CCF es el 4% del IBC
    ccf = ibc * 0.04
    return ccf
