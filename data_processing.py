import pandas as pd
def get_field(field):
    data_cultivos_general = pd.read_excel(io="Data/general_data.xlsx",\
                                          sheet_name="Cultivos permanentes",\
                                          dtype={"Cultivo":str,"Costos sin administracion":int,\
                                                 "Costos con administracion":int,\
                                                 "Produccion(ton/ha)":float,\
                                                 "check de precio":str,\
                                                 "ciclo de cultivo min (meses)":float,\
                                                 "col precio":str,\
                                                 "hoja":float,\
                                                 "first index":int,\
                                                 "last index":int} \
                                          )

    return data_cultivos_general[field]

def get_prices(index):

    data_id_precios = pd.read_excel(io="Data/general_data.xlsx", \
                                          sheet_name="Cultivos permanentes", \
                                          dtype={"Cultivo": str, "Costos sin administracion": int, \
                                                 "Costos con administracion": int, \
                                                 "Produccion(ton/ha)": float, \
                                                 "check de precio": str, \
                                                 "ciclo de cultivo min (meses)": float, \
                                                 "hoja": float, \
                                                 "first index": int, \
                                                 "last index": int}, \
                                          )

    hoja = str(data_id_precios["hoja"][index])
    fi = int(data_id_precios["fi"][index])
    li = int(data_id_precios["li"][index])


    data_precios = pd.read_excel(io="Data/pr_venta_por_kilo.xlsx",sheet_name=hoja,usecols="E")
    lista = []
    for x in data_precios[fi:li + 1].values.tolist():
        lista.append(int(x[0]))
    return (lista)


def get_markets(index):
    data_id_markets = pd.read_excel(io="Data/general_data.xlsx", \
                                    sheet_name="Cultivos permanentes", \
                                    dtype={"Cultivo": str, "Costos sin administracion": int, \
                                           "Costos con administracion": int, \
                                           "Produccion(ton/ha)": float, \
                                           "check de precio": str, \
                                           "ciclo de cultivo min (meses)": float, \
                                           "hoja": float, \
                                           "first index": int, \
                                           "last index": int}, \
                                    )

    hoja = str(data_id_markets["hoja"][index])
    fi = int(data_id_markets["fi"][index])
    li = int(data_id_markets["li"][index])

    data_markets = pd.read_excel(io="Data/pr_venta_por_kilo.xlsx",sheet_name=hoja, usecols="B")
    lista = []
    for x in data_markets[fi:li+1].values.tolist():
        lista.append(str(x[0]))
    return (lista)








