import pandas as pd

def clean_energy_data(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values using recommended methods
    df = df.ffill().bfill()

    # Convert data types
    df['year'] = df['year'].astype(int)
    df['population_million'] = df['population_million'].astype(float)

    # Save cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved as {output_file}")

if __name__ == "__main__":
    clean_energy_data("data/energy_emissions.csv", "data/cleaned_energy_emissions.csv")