import pandas as pd

def process_data(file_path):
    """Reads and processes CSV data."""
    df = pd.read_csv(file_path)
    df['amount'] = df['amount'] * 1.1  # Example transformation: Add 10% to amount
    return df

if __name__ == "__main__":
    df = process_data("data/sample.csv")
    print(df.head())
