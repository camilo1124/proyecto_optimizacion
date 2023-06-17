"""
Project for Optimization
Model Python Formulation for agricultural
aplications in Colombia

Authors:
Subject: Optimization

"""

#Import PuLP modeler functions
from pulp import *

# The variable problem contains the problem data

def modelo():
    problem = LpProblem("Max Profits", LpMaximize)

    x1 = LpVariable("Hectaria_aguacate",0,None,LpInteger)
    x2 = LpVariable("Hectaria_banano",0,None,LpInteger)
    x3 = LpVariable("Hectaria_cacao",0,None,LpInteger)
    x4 = LpVariable("Hectaria_cafe",0,None,LpInteger)

    #The objetctive function is added

    problem += (9000*4000)*x1 + (24000*800)*x2 + (500*11000)*x3 + (1150 * 12700)*x4, "Ganancias totales por hectaria de cultivo"

    #Restrictions are added

    problem += 11791226 * x1 + 8081101 * x2 + 6829041 * x3 + 9107808 * x4 <= 100000000, "Limitación de presupuesto"
    problem += x1 + x2 + x3 + x4 <= 1000, "Limitacion de hectareas"

    problem.writeLP("Max Profits")

    problem.solve()

    print("Estado",LpStatus[problem.status])

    for x in problem.variables():
        print(x.name, "=",x.varValue)

    print("Ganancias maxi ", value(problem.objective))








