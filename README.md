# Gestión de Países en Python — TPI Programación 1

Trabajo Práctico Integrador de la materia **Programación 1** de la Tecnicatura Universitaria en Programación a Distancia — UTN.

**Integrantes:** Ivan Mendoza · Adrian Candas  
**Cursada:** 2026

---

## Descripción

Sistema de consola en Python para gestionar un dataset de países almacenado en un archivo CSV. Permite agregar, actualizar y buscar países, aplicar filtros y ordenamientos, y consultar estadísticas.

---

## Requisitos

- Python 3.x
- No requiere librerías externas

---

## Estructura del proyecto

```
├── Trabajo_Practico_Integrador.py   # Programa principal
└── paises.csv                       # Dataset de países
```

---

## Uso

1. Colocar ambos archivos en la misma carpeta.
2. Abrir `Trabajo_Practico_Integrador.py` y verificar que la constante `ARCHIVO_CSV` apunte a la ruta correcta del archivo `paises.csv`.
3. Ejecutar:

```bash
python3 Trabajo_Practico_Integrador.py
```

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Mostrar todos los países |
| 2 | Agregar un nuevo país |
| 3 | Actualizar población y superficie de un país |
| 4 | Buscar país por nombre (parcial o exacto) |
| 5 | Filtrar por continente |
| 6 | Filtrar por rango de población |
| 7 | Filtrar por rango de superficie |
| 8 | Ordenar por nombre (A→Z) |
| 9 | Ordenar por población (menor→mayor) |
| 10 | Ordenar por superficie ascendente |
| 11 | Ordenar por superficie descendente |
| 12 | Estadísticas (mayor/menor población, promedios, conteo por continente) |
| 0 | Salir |

---

## Formato del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
...
```

El dataset incluye 50 países de los continentes: América, Europa, Asia, Africa y Oceania.

---

## Conceptos aplicados

- Listas y diccionarios de Python
- Funciones con responsabilidad única (PEP 8 / snake_case)
- Lectura y escritura de archivos CSV con `open()` y `split()`
- Validación de entrada con bucles `while`
- Algoritmo de ordenamiento por selección (Selection Sort)
- Estadísticas básicas: máximo, mínimo, promedio y conteo

---

## Integrantes

| Nombre | Rol |
|--------|-----|
| Ivan Mendoza | Filtros, ordenamientos, estadísticas, integración general |
| Adrian Candas | Alta de país, actualización, búsqueda por nombre , integracion general|
