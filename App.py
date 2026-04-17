# app.py
import streamlit as st
import pandas as pd

st.title("College Rankings & Details Dump")

st.write("Upload a CSV with College Names. The app will enrich with NAAC, NBA, NIRF, and other details.")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV with College Names", type=["csv"])

if uploaded_file is not None:
    df_input = pd.read_csv(uploaded_file)

    if "College Name" not in df_input.columns:
        st.error("CSV must have a column named 'College Name'")
    else:
        colleges = df_input["College Name"].tolist()

        if st.button("Generate CSV"):
            data = []
            for college in colleges:
                # Placeholder values — replace with actual scraped/verified data
                data.append({
                    "College Name": college,
                    "NAAC": "A++",  
                    "NBA": "Yes",   
                    "NIRF": "89",   
                    "Other Rankings": "Top Engineering Colleges",
                    "Year of Foundation": "1963",
                    "Type": "Autonomous (VTU affiliated, Private)",
                    "Website": f"https://{college.replace(' ', '').lower()}.edu.in",
                    "Google Search": college
                })

            df = pd.DataFrame(data)

            # Show table
            st.dataframe(df)

            # Download CSV
            csv = df.to_csv(index=False).encode
