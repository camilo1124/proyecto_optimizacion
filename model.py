"""
Project for Optimization
Model Python Formulation for agricultural
aplications in Colombia


Subject: Optimization

"""

#Import PuLP modeler functions
from pulp import *

from data_processing import get_field
import data_processing as dp
import pandas as pd






def max_prod_model(hectareas,dinero,res_tiempo,indexes,prices):
    n_var = 0
    dinero = dinero*1000000
    cultivos = dp.get_field("Cultivo")
    costos = dp.get_field("Costos con administracion")
    problem = LpProblem("Max Production", LpMaximize)
    cultivos = get_field("Cultivo")
    prod = get_field("Produccion(ton/ha)")

    x = []

    for i in range(len(indexes)):
        x.append(LpVariable("Hectareas de " + cultivos[indexes[i]], 0, None, LpInteger))

    equation = 0
    for i in range(len(indexes)):
        coef = prod[indexes[i]]
        equation += (x[i] * coef)

    problem += equation, "Produción por hectaria de cultivo"

    equation_1 = 0
    equation_2 = 0
    for i in range(len(indexes)):
        coef = costos[indexes[i]]
        equation_1 += (x[i]*coef)
        equation_2 += x[i]

    problem += equation <= dinero, "Limitación de presupuesto"
    problem += equation_2 <= hectareas,"Limitación de hectareas"




    problem.writeLP("Max Profits")

    problem.solve()

    print("Estado", LpStatus[problem.status])
    resultado = []

    for x in problem.variables():
        resultado.append(str(x.name) +  "=" + str( x.varValue))
        print(x.name, "=", x.varValue)
    fo = "Toneladas maxi "+str( value(problem.objective))

    print("Toneladas maxi ", value(problem.objective))

    return resultado,fo

def min_cost_model(hectareas,toneladas,res_tiempo,indexes,prices):
    n_var = 0
    cultivos = dp.get_field("Cultivo")
    costos = dp.get_field("Costos con administracion")
    problem = LpProblem("Min Costs", LpMinimize)
    cultivos = get_field("Cultivo")
    prod = get_field("Produccion(ton/ha)")

    x = []

    for i in range(len(indexes)):
        x.append(LpVariable("Hectareas de " + cultivos[indexes[i]], 0, None, LpInteger))

    equation = 0
    for i in range(len(indexes)):
        coef = costos[indexes[i]]
        equation += (x[i] * coef)

    problem += equation, "Costos por hectaria de cultivo"

    equation_1 = 0
    equation_2 = 0
    for i in range(len(indexes)):
        coef = prod[indexes[i]]
        equation_1 += x[i]*coef
        equation_2 += x[i]
    problem += equation_1 >= toneladas, "Toneladas minimas deseadas"
    problem += equation_2 <= hectareas,"Limitación de hectareas"




    problem.writeLP("Min Costos")

    problem.solve()

    print("Estado", LpStatus[problem.status])

    resultado = []

    for x in problem.variables():
        resultado.append((str(x.name)+ "="+str( x.varValue)))
        print(x.name, "=", x.varValue)
    fo = "Costo minimo " + str( value(problem.objective))

    print("Costo minimo ", value(problem.objective))

    return resultado, fo

def max_profit_model(hectareas,dinero,res_tiempo,indexes,prices):
    n_var = 0
    dinero = dinero*1000000
    cultivos = dp.get_field("Cultivo")
    costos = dp.get_field("Costos con administracion")
    problem = LpProblem("Max Production", LpMaximize)
    cultivos = get_field("Cultivo")
    prod = get_field("Produccion(ton/ha)")

    x = []

    for i in range(len(indexes)):
        x.append(LpVariable("Hectareas de " + cultivos[indexes[i]], 0, None, LpInteger))


    equation = 0
    for i in range(len(indexes)):
        coef = prices[i]*1000*prod[indexes[i]]
        equation += (x[i] * coef)

    problem += equation, "Ganancias por hectaria de cultivo"

    equation_1 = 0
    equation_2 = 0
    for i in range(len(indexes)):
        coef = costos[indexes[i]]
        equation_1 += (x[i]*coef)
        equation_2 += x[i]

    problem += equation <= dinero, "Limitación de presupuesto"
    problem += equation_2 <= hectareas,"Limitación de hectareas"




    problem.writeLP("Max Profits")

    problem.solve()

    print("Estado", LpStatus[problem.status])

    resultado = []
    fo = " "
    for x in problem.variables():
        resultado.append(str(x.name)+ "=" + str( x.varValue))
        print(x.name, "=", x.varValue)
    fo = "Ganancias maximas " + str( value(problem.objective))

    print("Ganancias maximas ", value(problem.objective))

    return resultado, fo

def max_util_model(hectareas,dinero,res_tiempo,indexes,prices):
    n_var = 0
    dinero = dinero*1000000
    cultivos = dp.get_field("Cultivo")
    costos = dp.get_field("Costos con administracion")
    problem = LpProblem("Max Production", LpMaximize)
    cultivos = get_field("Cultivo")
    prod = get_field("Produccion(ton/ha)")

    x = []

    for i in range(len(indexes)):
        x.append(LpVariable("Hectareas de " + cultivos[indexes[i]], 0, None, LpInteger))

    equation = 0
    for i in range(len(indexes)):
        coef = prices[i]*1000*prod[indexes[i]]
        coef_n = costos[indexes[i]]
        equation += (x[i] * (coef - coef_n))

    problem += equation, "Ganancias por hectaria de cultivo"

    equation_1 = 0
    equation_2 = 0
    for i in range(len(indexes)):
        coef = costos[indexes[i]]
        equation_1 += (x[i]*coef)
        equation_2 += x[i]

    problem += equation <= dinero, "Limitación de presupuesto"
    problem += equation_2 <= hectareas,"Limitación de hectareas"




    problem.writeLP("Max Profits")

    problem.solve()

    print("Estado", LpStatus[problem.status])

    resultado = []
    fo = " "
    for x in problem.variables():
        resultado.append(str(x.name)+ " = ", str(x.varValue))
        print(x.name, "=", x.varValue)
    fo = "utilidades maxi " +  str(value(problem.objective))

    print("Utilidades maxi ", value(problem.objective))

    return resultado, fo











