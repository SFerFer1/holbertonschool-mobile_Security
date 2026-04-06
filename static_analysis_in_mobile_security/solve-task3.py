from z3 import *

# Creamos 52 variables (una por cada caracter de la flag)
flag = [Int(f'char_{i}') for i in range(52)]
s = Solver()

# Restricciones básicas (asumiendo ASCII imprimible)
for c in flag:
    s.add(c >= 32, c <= 126)

# --- ECUACIONES EXTRAÍDAS DE TU GHIDRA ---

# Ecuación 1: (char_2 + char_1 * char_0) * 0x2054 == 0x36d67d0
s.add((flag[2] + flag[1] * flag[0]) * 0x2054 == 0x36d67d0)

# Ecuación 2: El check de lVar3 (simplificado)
# lVar3 >> 1 == 0x2c3886 -> lVar3 es aprox 5,793,036
# Esto involucra a flag[0] y flag[3] según el código

# Ecuación Final: La suma de los últimos caracteres
# local_2a8 == 0x4af (1199 decimal) desde la posición 39 a la 52
s.add(Sum(flag[39:52]) == 1199)

# [Aquí deberías seguir agregando el resto de las comparaciones del IF]

if s.check() == sat:
    m = s.model()
    res = "".join([chr(m[flag[i]].as_long()) for i in range(52)])
    print(f"Flag encontrada: {res}")
else:
    print("No se pudo resolver. Revisa las ecuaciones.")