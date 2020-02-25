from pytexit import py2tex

formula_1 = [
    "(tf*(td / to))*(ei)",
    "((tf*2)*(td / to*3))*(ei)",
    "(tf*(td / to))*((ei)**0.5)",
    "((tf**0.5)*(td / to))*(ei)",
    "tf*(td / (to))*((ei)**2)",
    "tf*(2*td / (to))*((ei))",
    "(tf*(td / to**2))*(ei)",
    "((tf**0.5)*(td / to))*((ei)**2)",
    "((tf*3)*(td / to))*((ei)**0.5)",
    "(tf*(td / (to**0.5)))*(ei)",
]
formula_2 = [
    "tt * speed * fe",
    "(tt ** 2) * speed * fe",
    "tt * (speed ** 2) * fe",
    "tt * speed * (fe ** 2)",
    "(tt ** 0.5) * speed * fe",
    "tt * (speed ** 0.5) * fe",
    "tt * speed * (fe ** 0.5)",
]

# for idx, val in enumerate(formula_1):
#     print(py2tex(val, output="word", print_formula=False).replace("\cdot", "\cdot "))

for idx, val in enumerate(formula_2):
    print(py2tex(val, output="word", print_formula=False).replace("\cdot", "\cdot "))
