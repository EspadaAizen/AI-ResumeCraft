import streamlit as st
import requests
import json  # ✅ required for resume file
from reportlab.lib.pagesizes import  LETTER
from reportlab.pdfgen import canvas
import io

st.title("✨ AI ResumeCraft")

# File uploader
uploaded_file = st.file_uploader("Upload your resume JSON", type=["json"])

# Tabs
tab1, tab2, tab3 = st.tabs(["Resume Rewriter", "Ping Test", "Resume Builder"])

with tab1:
    st.header("✍️ Resume Editor (from JSON)")

    # Load uploaded file
    if uploaded_file and "resume" not in st.session_state:
        data = json.load(uploaded_file)
        st.session_state["resume"] = data

    if "resume" in st.session_state:
        resume = st.session_state["resume"]

        # Basics
        st.subheader("👤 Basics")
        resume["basics"]["name"] = st.text_input("Name", resume["basics"].get("name", ""))
        resume["basics"]["email"] = st.text_input("Email", resume["basics"].get("email", ""))
        resume["basics"]["headline"] = st.text_input("Headline", resume["basics"].get("headline", ""))

        # Skills
        st.subheader("🛠 Skills")
        skills_text = st.text_area("Skills (comma separated)", ", ".join(resume.get("skills", [])))
        resume["skills"] = [s.strip() for s in skills_text.split(",") if s.strip()]

        # Experience
        st.subheader("💼 Experience")
        for idx, job in enumerate(resume.get("experience", [])):
            job["company"] = st.text_input(f"Company {idx + 1}", job.get("company", ""))
            job["position"] = st.text_input(f"Position {idx + 1}", job.get("position", ""))
            job["startDate"] = st.text_input(f"Start Date {idx + 1}", job.get("startDate", ""))
            job["endDate"] = st.text_input(f"End Date {idx + 1}", job.get("endDate", ""))
            highlights_text = st.text_area(f"Highlights {idx + 1}", "\n".join(job.get("highlights", [])))
            job["highlights"] = [h.strip() for h in highlights_text.split("\n") if h.strip()]

        # Preview
        st.subheader("👀 Resume Preview")
        st.write(f"### {resume['basics']['name']}")
        st.write(f"📧 {resume['basics']['email']}")
        st.write(f"💼 {resume['basics']['headline']}")
        st.write("#### Skills")
        st.write(", ".join(resume.get("skills", [])))

        for job in resume.get("experience", []):
            st.write(f"**{job['position']} @ {job['company']}** ({job['startDate']} – {job['endDate']})")
            for h in job["highlights"]:
                st.write(f"- {h}")

        # Download Updated JSON
        resume_json_str = json.dumps(resume, indent=2)
        st.download_button(
            "💾 Download Updated Resume JSON",
            data=resume_json_str,
            file_name="updated_resume.json",
            mime="application/json"
        )

        # -------------
        # PDF Export
        # -------------
        def generate_pdf(resume_data):
            buffer = io.BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=LETTER)
            width, height = LETTER

            y = height - 50
            pdf.setFont("Helvetica-Bold", 16)
            pdf.drawString(50, y, resume_data["basics"]["name"])
            pdf.setFont("Helvetica", 12)
            y -= 20
            pdf.drawString(50, y, f"Email:{resume_data['basics']['email']}")
            y -= 20
            pdf.drawString(50, y, f"Headline:{resume_data['basics']['headline']}")

            # Skills
            y -= 40
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, y, "Skills")
            pdf.setFont("Helvetica", 12)
            y -= 20
            pdf.drawString(50, y, ", ".join(resume_data.get("Skills", [])))

            #Experience
            for job in resume_data.get("experience", []):
                y -= 40
                pdf.setFont("Helvetica-Bold", 14)
                pdf.drawString(50, y, f"{job['position']} @ {job['company']}")
                pdf.setFont("Helvetica-Bold", 12)
                y -= 20
                pdf.drawString(40, y, f"{job['startDate']} - {job['endDate']}")

                for h in job.get("highlights",[]):
                    y -= 20
                    pdf.drawString(70, y, f". {h}")

            pdf.save()
            buffer.seek(0)
            return buffer
        pdf_buffer = generate_pdf(resume)
        st.download_button(
            "📄 Download Resume as PDF",
            data=pdf_buffer,
            file_name="resume.pdf",
            mime="application/pdf"
        )

        # Clear button
        if st.button("🗑️ Clear Resume"):
            st.session_state.pop("resume", None)  # remove key safely
            st.success("Resume cleared. Upload or create a new one.")
            st.rerun()  # ✅ force UI refresh

    else:
        st.info("📌 Upload a JSON resume to edit.")




with tab2:
    st.write("Backend ping test:")
    if st.button("Ping Backend"):
        try:
            res = requests.get("http://localhost:8000/ping")
            st.json(res.json())
        except Exception as e:
            st.error(f"Backend not reachable: {e}")


with tab3:
    st.header("Create a simple Resume JSON")

    with st.form("resume_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        headline = st.text_input("Headline (e.g., Full-stack developer)")

        skills = st.text_area("Skills (comma separated)", "Python, Java, MERN")

        st.subheader("Experience")
        company = st.text_input("company")
        position = st.text_input("Position")
        start_date = st.text_input("Start Date (YYYY-MM)")
        end_date = st.text_input("End Date (YYYY-MM)")
        highlights_text = st.text_area("Highlights (one per line)", "Worked on ...\nBuilt ...")

        submitted = st.form_submit_button("Generate Resume JSON")
    if submitted:
        resume_data = {
            "basics":{
                "name": name,
                "email": email,
                "headline": headline
            },
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "experience":[
                {
                    "company": company,
                    "position": position,
                    "startDate": start_date,
                    "endDate": end_date,
                    "highlights": [h.strip() for h in highlights_text.split("\n") if h.strip()]
                }
            ]
        }

        st.subheader(" Generated Resume JSON:")
        st.json(resume_data)

        #Download button
        resume_json_str = json.dumps(resume_data, indent=2)
        st.download_button(
            label="💾 Download Resume JSON",
            data=resume_json_str,
            file_name="simple_resume.json",
            mime="application/json"
        )


