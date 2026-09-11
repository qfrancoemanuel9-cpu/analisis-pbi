import requests
import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    pd.options.display.float_format = "{:,.0f}".format

    url = "https://api.worldbank.org/v2/country/ARG/indicator/NY.GDP.MKTP.CD?format=json&date=2000:2025&per_page=100"
    respuesta = requests.get(url)
    datos = respuesta.json()

    registros = datos[1]

    df = pd.DataFrame(registros)
    df = df[["date", "value"]]
    df.columns = ["año", "pbi"]
    df = df.sort_values("año")
    df = df.reset_index(drop=True)
    df["variacion_%"] = df["pbi"].pct_change() * 100
    df.to_csv("pbi_argentina.csv", index=False)
    df.to_excel("pbi_argentina.xlsx", index=False)
    print(df)

    plt.plot(df["año"], df["pbi"])
    plt.title("PBI de Argentina (USD corrientes)")
    plt.xlabel("Año")
    plt.ylabel("PBI (USD)")
    plt.show()