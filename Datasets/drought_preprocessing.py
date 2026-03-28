import pandas as pd

area = pd.read_csv(
    "Drought_Area.csv"
)


population = pd.read_csv(
"Drought_Population.csv",
) 

# Create Date column
area["Date"] = pd.to_datetime(area["MapDate"], format="%Y%m%d")
population["Date"] = pd.to_datetime(population["MapDate"], format="%Y%m%d")

# Rename columns
area.columns = [ "MapDate", "StateAbbreviation", "A_None", "A_D0", "A_D1", "A_D2",
        "A_D3", "A_D4", "ValidStart", "ValidEnd", "StatisticFormatID", "Date"]
population.columns = ["MapDate", "StateAbbreviation", "P_None", "P_D0", "P_D1", "P_D2",
        "P_D3", "P_D4", "ValidStart", "ValidEnd", "StatisticFormatID", "Date"]

# Drop Unnecessary Columns
drought_area = area.drop(["MapDate", "StateAbbreviation", "ValidStart", "ValidEnd", "StatisticFormatID"], axis=1)
drought_population = population.drop(["MapDate", "StateAbbreviation", "ValidStart", "ValidEnd", "StatisticFormatID"], axis=1)

# Merge the two datasets on the Date column
full_Drought = pd.merge(drought_area, drought_population, on="Date", how="inner")
full_Drought = full_Drought[["Date", "A_None", "A_D0", "A_D1", "A_D2", "A_D3", 
                            "A_D4", "P_None", "P_D0", "P_D1", "P_D2", "P_D3", "P_D4"]]

full_Drought.to_csv("./full_Drought.csv", index=False)

