import pandas as pd
from src.generate_report import generate_summary

def test_generate_summary(tmp_path):
    input_path = tmp_path / "input.csv"
    output_path = tmp_path / "output.csv"

    input_path.write_text("Name,Department,Salary\nA,Engineering,100\nB,Engineering,300")

    generate_summary(input_path, output_path)

    df = pd.read_csv(output_path)
    assert df.loc[0, "Average_Salary"] == 200
