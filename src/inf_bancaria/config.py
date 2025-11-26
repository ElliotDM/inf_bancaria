from pathlib import Path

data_dir = Path('../data/raw')
data_path = data_dir / "Inf_Bancaria_Base_datos.csv"

processed_data_dir = Path("../data/processed")
processed_data_path = processed_data_dir / "processed_df.csv"

clean_data_dir = Path("../data/clean")
clean_data_path = clean_data_dir / "clean_df.csv"
