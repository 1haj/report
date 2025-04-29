import os
import pandas as pd
from src.generate_report import generate_summary

def test_generate_summary_creates_file(tmp_path):
    # Arrange
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "summary.csv"

    # Create sample input CSV
    input_csv.write_text("Department,Salary\nIT,5000\nHR,4000\nIT,6000")

    # Act
    generate_summary(str(input_csv), str(output_csv))

    # Assert
    assert output_csv.exists(), "Output file was not created"

    df = pd.read_csv(output_csv)
    assert "Department" in df.columns and "Average_Salary" in df.columns
    assert df.shape[0] == 2  # 2 departments
