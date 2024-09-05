import streamlit as st
import requests
from pandas import DataFrame

api_url = "http://127.0.0.1:8000/api/predict/"

st.set_page_config(
    page_title="Contratación",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("Asistente de contratación")

age = st.sidebar.slider("Edad:", 20, 50)
gender_dict = {
    "Hombre": 0,
    "Mujer": 1
}
gender = st.sidebar.selectbox("Género:", gender_dict.keys())
education_dict = {
    "Bachiller": 1,
    "Pregrado": 2,
    "Maestría": 3,
    "Doctorado": 4
}
education = st.sidebar.selectbox("Educación:", education_dict.keys())
experience = st.sidebar.slider("Años de experiencia:", 0, 15)
companies = st.sidebar.slider("Compañías previas:", 1, 5)
distance = st.sidebar.number_input("Distancia de la compañía:", 0, 60)
interview_score = st.sidebar.slider("Puntuación en la entrevista:", 0, 100)
skill_score = st.sidebar.slider("Puntuación de habilidades:", 0, 100)
personality_score = st.sidebar.slider("Puntuación de personalidad:", 0, 100)
recruitment_strategy_dict = {
    "Agresivo": 1,
    "Moderado": 2,
    "Conservador": 3
}
recruitment_strategy = st.sidebar.selectbox("Estretegia de recrutamiento", recruitment_strategy_dict.keys())
st.header("Datos ingresados por el usuario...")

data = {
    "Age": age,
    "Gender": gender_dict[gender],
    "EducationLevel": education_dict[education],
    "ExperienceYears": experience,
    "PreviousCompanies": companies,
    "DistanceFromCompany": float(distance),
    "InterviewScore": interview_score,
    "SkillScore": skill_score,
    "PersonalityScore": personality_score,
    "RecruitmentStrategy": recruitment_strategy_dict[recruitment_strategy]
    }
st.write(DataFrame(data, index = ["Datos"])[:1])
if st.button("Predecir"):
    
    
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        try:
            json_data = response.json()  # Intentar decodificar JSON
            st.write(f"{'No' if json_data['HiringDecision'] == 0 else 'Si'} deberías contratar a este empleado")
        except requests.exceptions.JSONDecodeError:
            st.error("El servidor no devolvió un JSON válido.")
            print("Error: No se pudo decodificar la respuesta como JSON.")
    else:
        st.error(f"Error en la solicitud: {response.status_code}")
        print(f"Error: {response.status_code}")
        print(response.text)
        # print(response.json())
        
# streamlit run .\views\hiring_view.py