# Análisis PBI Argentina

Script en Python que obtiene el PBI de Argentina (en USD corrientes) desde la API del Banco Mundial, calcula la variación porcentual año a año, y exporta los resultados a CSV, Excel y un gráfico.

## Qué hace

1. Consulta la API del Banco Mundial (`NY.GDP.MKTP.CD`) para Argentina.
2. Ordena los datos por año y calcula la variación porcentual del PBI respecto al año anterior.
3. Exporta el resultado a `pbi_argentina.csv` y `pbi_argentina.xlsx`.
4. Genera un gráfico de la evolución del PBI (`crecimiento del PBI nacional (2020-2025).png`).

## Requisitos

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) para gestionar dependencias y entorno virtual

## Instalación

```bash
uv sync
```

## Uso

```bash
uv run analisis-pbi
```

Esto imprime la tabla de resultados en consola, genera los archivos `pbi_argentina.csv` / `pbi_argentina.xlsx` y muestra el gráfico de evolución del PBI.

## Datos

| año  | pbi (USD)         | variación % |
|------|--------------------|-------------|
| 2021 | 486,564,085,480    | —           |
| 2022 | 633,993,756,301    | 30.30       |
| 2023 | 649,461,687,959    | 2.44        |
| 2024 | 638,365,455,340    | -1.71       |
| 2025 | 683,097,891,619    | 7.01        |

Fuente: [World Bank Open Data](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?locations=AR)
