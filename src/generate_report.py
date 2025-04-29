import pandas as pd

def generate_summary(input_path, output_path):
    df = pd.read_csv(input_path)
    summary = df.groupby("Department")["Salary"].mean().reset_index()
    summary.columns = ["Department", "Average_Salary"]
    summary.to_csv(output_path, index=False)

if __name__ == "__main__":
    generate_summary("data/input.csv", "reports/summary_report.csv")
