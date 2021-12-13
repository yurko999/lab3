from numpy import NaN
import pandas as pd
import matplotlib.pyplot as plt

def parseHeightToMeters(cell):
    splitedCell = cell.split("-")
    return round(float(splitedCell[0]) / 3.281 + float(splitedCell[1]) / 39.37, 3)

# input data
employeesDf = pd.read_csv('employees.csv', sep = ',')
nbaDf = pd.read_csv('nba.csv', sep = ',')
pd.set_option('display.max_columns', 50)

print("employees input:")
print(employeesDf)
print("nba input:")
print(nbaDf)

# pre-treatment

print("employeesDf rows with NaN:")
print(employeesDf[employeesDf.isna().any(axis=1)])

employeesDf = employeesDf.dropna()
nbaDf = nbaDf.dropna()

nbaDf["Weight"] = nbaDf["Weight"] / 2.205

nbaDf["Height"] = nbaDf["Height"].apply(parseHeightToMeters)


print("nba pre-treatment:")
print(nbaDf)

print("employeesDf pre-treatment:")
print(employeesDf)

# aggregation

print(f'Avarage NBA salary {round(nbaDf["Salary"].mean())}')
print(f'Avarage NBA height {round(nbaDf["Height"].mean(), 2)}')
print(f'Avarage NBA weight {round(nbaDf["Weight"].mean(), 2)}')

print()

print(f'Avarage male employees salary   {round(employeesDf[employeesDf["Gender"] == "Male"]["Salary"].mean())}')
print(f'Avarage female employees salary {round(employeesDf[employeesDf["Gender"] == "Female"]["Salary"].mean())}')

print(f'Avarage Senior Management salary     {round(employeesDf[employeesDf["Senior Management"] == True]["Salary"].mean())}')
print(f'Avarage not Senior Management salary {round(employeesDf[employeesDf["Senior Management"] == False]["Salary"].mean())}')

# plots

nbaDf.groupby("Height")["Salary"].mean().reset_index().plot(kind="line", x="Height", y="Salary")
plt.show()

employeesDf.groupby("Team")["Salary"].mean().reset_index().plot(kind="bar", x="Team", y="Salary")
plt.show()

# updated data saving

nbaDf.to_csv("nbaDfNew.csv", index=False)
employeesDf.to_csv("employeesDfNew.csv", index=False)