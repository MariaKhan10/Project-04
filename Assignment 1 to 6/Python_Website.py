import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.header("📂 Smart File Transfer")
st.write("Transform files between CSV and Excel formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the uploaded file
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")
        
        # Data Preview
        st.subheader("📜 Data Preview")
        st.dataframe(df.head())

         # Data Summary
        st.subheader("📜 Data Summary")
        st.dataframe(df.describe())
        
        # Data Cleaning Options
        st.subheader(f"🛠 Data Cleaning for {file.name}")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates Removed!")
            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing Values Filled!")
        
        # Column Selection
        st.subheader(f"🎯 Select Columns for {file.name}")
        selected_columns = st.multiselect(f"Choose Columns:", df.columns, default=df.columns)
        df = df[selected_columns]

     # Data Visualization
        st.subheader(f"📊 Data Visualization for {file.name}")
        if st.checkbox(f"Show Charts for {file.name}"):
            col1, col2 = st.columns(2)  # Define columns first

            # Ensure there are numerical columns; otherwise, use dummy data
            numeric_df = df.select_dtypes(include='number')
            if numeric_df.empty or numeric_df.shape[1] < 2:
                numeric_df = pd.DataFrame({
                    "Sample X": [1, 2, 3, 4, 5],
                    "Sample Y": [10, 20, 15, 30, 25]
                })

            with col1:
                st.bar_chart(numeric_df)

            with col2:
                st.line_chart(numeric_df)


        
        # File Conversion
        st.subheader(f"🔄 Convert File: {file.name}")
        convert_option = st.radio(f"Convert to:", ["CSV", "Excel"], key=file.name)
        
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if convert_option == "CSV":
                df.to_csv(buffer, index=False)
                converted_file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            else:
                df.to_excel(buffer, index=False)
                converted_file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)
            
            st.download_button(
                label=f"📥 Download {convert_option} File",
                data=buffer,
                file_name=converted_file_name,
                mime=mime_type
            )

    st.success("✅ All files processed successfully! Keep growing! ")