#Import libraries
import streamlit as st #Used to deploy as website
from scorer import similarity_check
import docx2txt
import pandas as pd
import altair as alt #Used to produce Visual

#Force streamlit to accept Docx format
st.set_option('deprecation.showfileUploaderEncoding', False)
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
job_spec = st.text_input("Job spec","paste job spec here") #Jobspec input box
st.sidebar.header("Upload up to 5 Resumes / CV") #Side bar heading

#Save uploaded files in respective variables
uploaded_file1 = st.sidebar.file_uploader("Choose resume 1", type="docx")
uploaded_file2 = st.sidebar.file_uploader("Choose resume 2", type="docx")
uploaded_file3 = st.sidebar.file_uploader("Choose resume 3", type="docx")
uploaded_file4 = st.sidebar.file_uploader("Choose resume 4", type="docx")
uploaded_file5 = st.sidebar.file_uploader("Choose resume 5", type="docx")

#Check if files are uploaded correctly and let user know
if uploaded_file1 is not None:
    st.write("Uploaded resume1.")
if uploaded_file2 is not None:
    st.write("Uploaded resume2")
if uploaded_file3 is not None:
    st.write("Uploaded resume3")
if uploaded_file4 is not None:
    st.write("Uploaded resume4")
if uploaded_file5 is not None:
    st.write("Uploaded resume5")

#Run similarity

if st.button('Run'):
    try:
        if uploaded_file1 is not None:
            resume_read1 = docx2txt.process(uploaded_file1)
        else:
            resume_read1 = ""
        if uploaded_file2 is not None:
            resume_read2 = docx2txt.process(uploaded_file2)
        else:
            resume_read2 = ""
        if uploaded_file3 is not None:
            resume_read3 = docx2txt.process(uploaded_file3)
        else:
            resume_read3 = ""
        if uploaded_file4 is not None:
            resume_read4 = docx2txt.process(uploaded_file4)
        else:
            resume_read4 = ""
        if uploaded_file5 is not None:
            resume_read5 = docx2txt.process(uploaded_file5)
        else:
            resume_read5 = ""

        job_description = job_spec
        text1 = [resume_read1, job_description]
        score1 = similarity_check(text1)
        st.write("Your resume1 matches about "+ str(score1)+ "% of the job description.")
        text2 = [resume_read2, job_description]
        score2 = similarity_check(text2)
        st.write("Your resume2 matches about "+ str(score2)+ "% of the job description.")
        text3 = [resume_read3, job_description]
        score3 = similarity_check(text3)
        st.write("Your resume3 matches about "+ str(score3)+ "% of the job description.")
        text4 = [resume_read4, job_description]
        score4 = similarity_check(text4)
        st.write("Your resume4 matches about "+ str(score4)+ "% of the job description.")
        text5 = [resume_read5, job_description]
        score5 = similarity_check(text5)
        st.write("Your resume5 matches about "+ str(score5)+ "% of the job description.")
#Convert the data to dataframe for easy plotting
        data = pd.DataFrame({
        'Resume': ['1','2','3','4','5'],
        'Similarity Score':[score1,score2,score3,score4,score5]
        })
#Using Altair and plotting results
        st.write(alt.Chart(data).mark_bar().encode(
        x='Resume',
        y='Similarity Score',
        color = 'Similarity Score'
        ).properties(width=800,height=300))

    except:
       st.write("Oops! Looks like some of the files are missing. Please check and rerun. ")






