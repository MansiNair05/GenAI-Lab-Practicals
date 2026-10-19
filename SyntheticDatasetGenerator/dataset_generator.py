import pandas as pd
from pathlib import Path

# Step 1: Define the courses
courses = ["MCA", "BCA", "BBA", "BSc", "BCom"]

# Step 2: Generate 30 synthetic student records
records = []

for i in range(30):
    record = {
        "student_id": 1001 + i,
        "name": f"Student_{i + 1:02d}",
        "age": 18 + (i % 8),
        "course": courses[i % len(courses)],
        "marks": (55 + i * 7) % 46 + 50,
        "attendance": float(60 + (i * 11) % 41)
    }

    records.append(record)

# Step 3: Convert records into a DataFrame
df = pd.DataFrame(records)

# Step 4: Define the expected dataset columns
expected_columns = [
    "student_id",
    "name",
    "age",
    "course",
    "marks",
    "attendance"
]

# Step 5: Validate the dataset structure
missing_columns = [
    col for col in expected_columns
    if col not in df.columns
]

extra_columns = [
    col for col in df.columns
    if col not in expected_columns
]

# Step 6: Check missing values and duplicate rows
missing_values = int(df.isnull().sum().sum())
duplicate_rows = int(df.duplicated().sum())

# Step 7: Validate data types
type_checks = {
    "student_id": pd.api.types.is_integer_dtype(df["student_id"]),
    "name": pd.api.types.is_string_dtype(df["name"]),
    "age": pd.api.types.is_integer_dtype(df["age"]),
    "course": pd.api.types.is_string_dtype(df["course"]),
    "marks": pd.api.types.is_integer_dtype(df["marks"]),
    "attendance": pd.api.types.is_float_dtype(df["attendance"])
}

# Step 8: Check value ranges and consistency
valid_ranges = (
    df["age"].between(18, 25).all()
    and df["marks"].between(0, 100).all()
    and df["attendance"].between(0, 100).all()
    and df["course"].isin(courses).all()
    and df["student_id"].is_unique
    and df["name"].str.len().gt(0).all()
)

correct_record_count = len(df) == 30

schema_valid = (
    not missing_columns
    and not extra_columns
    and all(type_checks.values())
)

# Step 9: Determine overall validation status
is_valid = (
    correct_record_count
    and schema_valid
    and missing_values == 0
    and duplicate_rows == 0
    and valid_ranges
)

# Step 10: Export the dataset into CSV and JSON files
df.to_csv("synthetic_students.csv", index=False)
df.to_json(
    "synthetic_students.json",
    orient="records",
    indent=4
)

# Step 11: Generate the validation report
report = f"""
SYNTHETIC DATASET VALIDATION REPORT
-----------------------------------
Total records: {len(df)}
Expected records: 30
Record count valid: {correct_record_count}
Missing values: {missing_values}
Duplicate rows: {duplicate_rows}
Missing columns: {missing_columns}
Extra columns: {extra_columns}
Data type checks: {type_checks}
Value ranges and consistency valid: {valid_ranges}
Schema valid: {schema_valid}
Overall validation: {"PASS" if is_valid else "FAIL"}
"""

Path("validation_report.txt").write_text(
    report,
    encoding="utf-8"
)

# Step 12: Display the report and sample records
print(report)

print("First five records:")
print(df.head().to_string(index=False))

print("\nFiles generated:")
print("- synthetic_students.csv")
print("- synthetic_students.json")
print("- validation_report.txt")