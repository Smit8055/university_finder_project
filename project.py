import streamlit as st
from datetime import datetime, timedelta
import io

# Expanded university database
universities = {
    "Italy": [
        ("University of Bologna", "€2,000 - €6,000/year", "April 30, 2025"),
        ("Sapienza University of Rome", "€1,000 - €6,000/year", "July 15, 2025"),
        ("University of Padua", "€2,500/year", "May 10, 2025"),
        ("Politecnico di Milano", "€3,500/year", "June 1, 2025"),
        ("University of Trento", "€1,500/year", "June 30, 2025")
    ],
    "Germany": [
        ("Technical University of Munich", "€72-€147/semester", "May 31, 2025"),
        ("Heidelberg University", "No tuition (€171/semester fee)", "June 15, 2025"),
        ("RWTH Aachen University", "€300/semester", "June 30, 2025"),
        ("LMU Munich", "No tuition (€150/semester)", "May 20, 2025"),
        ("University of Stuttgart", "€1,500/semester", "July 1, 2025")
    ],
    "USA": [
        ("Harvard University", "$54,269/year", "January 1, 2025"),
        ("Stanford University", "$58,416/year", "December 5, 2024"),
        ("MIT", "$53,790/year", "January 15, 2025"),
        ("UC Berkeley", "$44,008/year", "November 30, 2024"),
        ("University of Michigan", "$51,200/year", "February 1, 2025")
    ],
    "India": [
        ("IIT Bombay", "₹2-3 lakhs/year", "March 31, 2025"),
        ("University of Delhi", "₹15,000-1.5 lakhs/year", "June 30, 2025"),
        ("IIT Madras", "₹2.2 lakhs/year", "April 15, 2025"),
        ("BITS Pilani", "₹4 lakhs/year", "May 31, 2025"),
        ("IISc Bangalore", "₹30,000 - 70,000/year", "April 25, 2025")
    ]
}

# Helper to calculate timeline
def calculate_timeline(deadline, days_before):
    try:
        deadline_date = datetime.strptime(deadline, "%B %d, %Y")
        return (deadline_date + timedelta(days=days_before)).strftime("%B %d, %Y")
    except:
        return f"{abs(days_before)} days before deadline"

# Set Streamlit layout
st.set_page_config(page_title="University Finder", layout="wide")
st.title("🎓 University Finder (Web Version with Shortlist)")

# Country selection
country = st.selectbox("🌍 Select a Country", [""] + list(universities.keys()))

shortlisted = []

if country:
    st.subheader(f"🔎 Universities in {country}")
    uni_list = universities[country]

    for name, tuition, deadline in uni_list:
        with st.expander(name):
            st.write(f"**Tuition Fees:** {tuition}")
            st.write(f"**Deadline:** {deadline}")
            st.markdown("**📅 Suggested Timeline:**")
            st.markdown(f"- Start research: `{calculate_timeline(deadline, -180)}`")
            st.markdown(f"- Prepare documents: `{calculate_timeline(deadline, -90)}`")
            st.markdown(f"- Submit application: `{calculate_timeline(deadline, -30)}`")
            st.markdown(f"- Final deadline: `{deadline}`")
            if st.checkbox(f"✅ Shortlist {name}", key=name):
                shortlisted.append((name, tuition, deadline, country))

# Shortlist download section
if shortlisted:
    st.markdown("## 📥 Download Your Shortlist")
    output = io.StringIO()
    output.write("MY UNIVERSITY SHORTLIST\n")
    output.write(f"Created on: {datetime.now().strftime('%Y-%m-%d')}\n\n")
    for i, uni in enumerate(shortlisted, 1):
        output.write(f"{i}. {uni[0]} ({uni[3]})\n")
        output.write(f"   Tuition: {uni[1]}\n")
        output.write(f"   Deadline: {uni[2]}\n\n")
    output.write("Good luck with your applications!\n")

    st.download_button("📄 Download Shortlist", output.getvalue(), "my_university_shortlist.txt", "text/plain")
else:
    st.info("You can select universities above and then download your shortlist.")
