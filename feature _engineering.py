import pandas as pd

def add_features(input_file, output_file):
    df = pd.read_csv(input_file)

    # Create new engineered features
    df["energy_per_capita"] = df["energy_consumption_twh"] / df["population_million"]
    df["emissions_per_capita"] = df["co2_emissions_mt"] / df["population_million"]
    df["renewable_share_percent"] = (df["renewable_energy_twh"] / df["energy_consumption_twh"]) * 100

    # Energy efficiency = More renewable energy & lower emissions per capita
    df["energy_efficiency_score"] = df["renewable_share_percent"] / df["emissions_per_capita"]

    # Save final engineered dataset
    df.to_csv(output_file, index=False)
    print(f"Dataset with features saved as {output_file}")

if __name__ == "__main__":
    add_features("data/cleaned_energy_emissions.csv", "data/engineered_energy_data.csv")
