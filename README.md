# Solucionador de Relaciones de Recurrencia Lineales
### con coeficientes constantes · Python + SymPy

---

## Estructura del proyecto (5 módulos)

```
recurrencia/
├── main.py          # Menú principal (CLI)
├── parser_rec.py    # Lectura y validación interactiva de la recurrencia
├── homogeneo.py     # Resolución del caso homogéneo
├── heterogeneo.py   # Resolución del caso heterogéneo (monomio c·nᵖ)
└── ejemplos.py      # 8 ejemplos predefinidos (4 homogéneos + 4 heterogéneos)
```

---

## Requisitos

```bash
pip install sympy
```

---

## Ejecución

```bash
cd recurrencia/
python main.py
```

---

## Casos soportados

### Homogéneo
Relaciones de la forma:
```
a(n) = a₁·a(n-1) + a₂·a(n-2) + ... + aₖ·a(n-k)
```
- Orden arbitrario k ≥ 1
- Raíces simples y múltiples
- Condiciones iniciales enteras o fraccionarias

### Heterogéneo (término monomio)
```
a(n) = a₁·a(n-1) + ... + aₖ·a(n-k)  +  c·nᵖ
```
- Se detecta automáticamente si r=1 es raíz y con qué multiplicidad m
- La forma supuesta de la solución particular se ajusta: aₚ(n) = nᵐ·(d₀ + d₁n + ... + dₚnᵖ)

---

## Ejemplos incluidos

| # | Tipo | Relación | Descripción |
|---|------|----------|-------------|
| H1 | Homogéneo | a(n) = a(n-1)+a(n-2) | Fibonacci / Fórmula de Binet |
| H2 | Homogéneo | a(n) = 4a(n-1)-4a(n-2) | Raíz doble r=2 |
| H3 | Homogéneo | a(n) = 6a(n-1)-11a(n-2)+6a(n-3) | Orden 3, raíces 1,2,3 |
| H4 | Homogéneo | a(n) = 3a(n-1) | Orden 1, crecimiento geométrico |
| X1 | Heterogéneo | a(n) = 2a(n-1)+n | r=1 no es raíz |
| X2 | Heterogéneo | a(n) = a(n-1)+n² | r=1 raíz simple |
| X3 | Heterogéneo | a(n) = 5a(n-1)-6a(n-2)+4 | término constante |
| X4 | Heterogéneo | a(n) = 2a(n-1)-a(n-2)+3n | r=1 raíz doble |

---

## Método matemático

**Caso homogéneo:**
1. Construir la ecuación característica `rᵏ - a₁rᵏ⁻¹ - ... - aₖ = 0`
2. Calcular raíces con multiplicidades
3. Escribir la solución general: para cada raíz `r` de multiplicidad `m` → `(C₁ + C₂n + ... + Cₘnᵐ⁻¹)rⁿ`
4. Resolver el sistema lineal con las condiciones iniciales

**Caso heterogéneo (monomio `c·nᵖ`):**
- Primero se resuelve la parte homogénea asociada → `aₕ(n)`
- Se propone `aₚ(n) = nᵐ·(d₀ + d₁n + ... + dₚnᵖ)` donde `m` es la multiplicidad de `r=1`
- Se sustituye en la recurrencia y se igualan coeficientes para hallar `dᵢ`
- Solución final: `a(n) = aₕ(n) + aₚ(n)`, luego se aplican condiciones iniciales
