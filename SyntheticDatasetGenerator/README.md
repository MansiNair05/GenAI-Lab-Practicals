# Synthetic Dataset Generator

## 1. Aim
To generate synthetic student data using Python and pandas, validate the dataset, and export it into CSV and JSON formats.

## 2. Technologies Used
- Python
- Pandas

## 3. Dataset Details
The program generates 30 artificial student records with these fields:
- `student_id`: Unique student identifier
- `name`: Student name
- `age`: Student age
- `course`: Course name
- `marks`: Student marks
- `attendance`: Attendance percentage

## 4. Features
- Generates 30 synthetic student records.
- Checks the number of records and dataset columns.
- Validates data types, missing values, and duplicate rows.
- Checks value ranges and data consistency.
- Exports data into CSV and JSON files.
- Creates a validation report.

## 5. How to Run
Install pandas:
```bash
python -m pip install pandas
```

Run the program:
```bash
python dataset_generator.py
```

## 6. Output Files
- `synthetic_students.csv`
- `synthetic_students.json`
- `validation_report.txt`

## 7. Validation Results
- Total records: 30
- Missing values: 0
- Duplicate rows: 0
- Schema validation: PASS
- Overall validation: PASS

## 8. Conclusion
This practical demonstrates synthetic dataset generation, data validation, and exporting data into commonly used file formats.

**Note:** This version generates data using Python and pandas; it does not directly call a Generative AI API.
