import csv
from pathlib import Path
from statistics import fmean, pvariance


def load_csv_data(file_path: Path) -> dict[str, list[float]]:
    with file_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        columns = {field_name: [] for field_name in reader.fieldnames or []}

        for row in reader:
            for column_name, value in row.items():
                columns[column_name].append(float(value))

    return columns


def main() -> None:
    file_path = Path(__file__).with_name("all_samples_data.csv")
    columns = load_csv_data(file_path)
    all_values = [value for values in columns.values() for value in values]

    print(f"CSV file: {file_path.name}")
    print(f"Overall mean: {fmean(all_values):.4f}")
    print(f"Overall variance: {pvariance(all_values):.4f}")
    print("\nMean and variance by column:")

    for column_name, values in columns.items():
        print(
            f"{column_name}: "
            f"mean = {fmean(values):.4f}, "
            f"variance = {pvariance(values):.4f}"
        )


if __name__ == "__main__":
    main()
