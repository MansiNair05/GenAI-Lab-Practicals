
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Synthetic Dataset Generator", page_icon="📊")

st.title("📊 Synthetic Dataset Generator")
st.write("Generate artificial student records and validate the dataset.")

num_records = st.slider("Number of student records", 5, 100, 30)

if st.button("Generate Dataset"):
    courses = ["MCA", "BCA", "BBA", "BSc", "BCom"]
    records = []

    for i in range(num_records):
        records.append({
            "student_id": 1001 + i,
            "name": f"Student_{i + 1:02d}",
            "age": 18 + (i % 8),
            "course": courses[i % len(courses)],
            "marks": (55 + i * 7) % 46 + 50,
            "attendance": float(60 + (i * 11) % 41)
        })

    df = pd.DataFrame(records)

    st.subheader("Generated Dataset")
    st.dataframe(df, use_container_width=True)

    st.subheader("Dataset Validation")
    checks = {
        "Correct record count": len(df) == num_records,
        "No missing values": int(df.isnull().sum().sum()) == 0,
        "No duplicate rows": int(df.duplicated().sum()) == 0,
        "Marks between 0 and 100": df["marks"].between(0, 100).all(),
        "Attendance between 0 and 100": df["attendance"].between(0, 100).all(),
        "Valid course names": df["course"].isin(courses).all()
    }

    for check, passed in checks.items():
        st.write(("✅ " if passed else "❌ ") + check)

    st.success("Dataset generation and validation completed.")

    st.download_button(
        "Download CSV",
        df.to_csv(index=False).encode("utf-8"),
        "synthetic_students.csv",
        "text/csv"
    )

    st.download_button(
        "Download JSON",
        df.to_json(orient="records", indent=4),
        "synthetic_students.json",
        "application/json"
    )

    st.caption("This demo generates synthetic data using Python and pandas. It does not call a Generative AI API.")
