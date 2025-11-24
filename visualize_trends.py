import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD CLEANED DATA
# ==========================

df = pd.read_csv("data/cleaned_energy_emissions.csv")

# Check required columns
required_cols = [
    "year",
    "energy_consumption_twh",
    "renewable_energy_twh",
    "co2_emissions_mt"
]

for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col} in cleaned dataset.")

# ==========================
# GLOBAL YEARLY TRENDS
# ==========================

yearly = df.groupby("year").sum().reset_index()

# -------- ENERGY CONSUMPTION TREND --------
plt.figure(figsize=(10, 5))
plt.plot(yearly["year"], yearly["energy_consumption_twh"], marker="o")
plt.xlabel("Year")
plt.ylabel("Energy Consumption (TWh)")
plt.title("Global Energy Consumption Trend")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/global_energy_trend.png")
plt.close()

# -------- RENEWABLE ENERGY TREND --------
plt.figure(figsize=(10, 5))
plt.plot(yearly["year"], yearly["renewable_energy_twh"], marker="o")
plt.xlabel("Year")
plt.ylabel("Renewable Energy (TWh)")
plt.title("Global Renewable Energy Trend")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/global_renewable_trend.png")
plt.close()

# -------- CO₂ EMISSIONS TREND --------
plt.figure(figsize=(10, 5))
plt.plot(yearly["year"], yearly["co2_emissions_mt"], marker="o")
plt.xlabel("Year")
plt.ylabel("CO₂ Emissions (Mt)")
plt.title("Global CO₂ Emission Trend")
plt.grid(True)
plt.tight_layout()
plt.savefig("data/global_emission_trend.png")
plt.close()

print("All trend graphs saved inside: data/")
