import pandas as pd

# ================================
# GLOBAL ENERGY & EMISSION DATASET
# ================================

data = {
    "year": [
        2000,2000,2000,2000,2000,
        2005,2005,2005,2005,2005,
        2010,2010,2010,2010,2010,
        2015,2015,2015,2015,2015,
        2020,2020,2020,2020,2020
    ],
    "country": [
        "India","China","United States","Germany","Brazil",
        "India","China","United States","Germany","Brazil",
        "India","China","United States","Germany","Brazil",
        "India","China","United States","Germany","Brazil",
        "India","China","United States","Germany","Brazil"
    ],
    "energy_consumption_twh": [
        450,1300,2400,550,380,
        600,1800,2550,520,410,
        750,2400,2600,500,450,
        900,2900,2700,480,480,
        1100,3100,2600,460,520
    ],
    "renewable_energy_twh": [
        50,90,380,120,220,
        90,130,420,150,260,
        160,210,520,200,310,
        260,350,620,260,390,
        380,520,700,330,450
    ],
    "co2_emissions_mt": [
        970,3400,5900,820,410,
        1200,4500,6000,760,380,
        1500,7600,5600,720,360,
        1900,9000,5400,680,350,
        2200,10100,4800,620,300
    ],
    "population_million": [
        1050,1260,282,82,174,
        1140,1330,295,82.4,186,
        1230,1360,309,81.7,195,
        1310,1380,320,82.5,204,
        1380,1400,331,83.2,213
    ]
}

df = pd.DataFrame(data)

# Save the dataset
df.to_csv("energy_emissions.csv", index=False)

print("Dataset 'energy_emissions.csv' generated successfully!")