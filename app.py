import os
from dotenv import load_dotenv
import streamlit as st
import openai

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration d'OpenAI avec votre clé d'API depuis le fichier .env
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configuration de la page Streamlit
st.set_page_config(page_title='Générateur d histoires structuré avec GPT-3.5 Turbo', page_icon='📖', layout='wide', initial_sidebar_state='expanded')

# Titre et introduction
st.title('Générateur d histoires structuré crée par LeBlanc 📖')

# Entrée utilisateur
prompt = st.text_area('Entrez votre prompt pour l histoire:')

# Génération du plan
if st.button('Générer le plan 📝'):
    plan_prompt = f'Vous êtes un expert en création de plans d histoires. Créez un plan détaillé pour une histoire basée sur : {prompt}. Le plan doit contenir 10 chapitres.'
    try:
        plan_response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role':'system', 'content':'Vous êtes un expert en création de plans d histoires.'}, {'role':'user', 'content':plan_prompt}])
        plan = plan_response.choices[0].message['content'].strip()
        st.subheader('Plan de l histoire 📝')
        st.text_area('', plan, height=300)
    except Exception as e:
        st.error(f'Une erreur est survenue: {e}. Essayez de reformuler votre prompt.')

# Génération des chapitres
chapter_number = st.slider('Sélectionnez le chapitre à générer', 1, 10, 1)
if st.button(f'Générer le chapitre {chapter_number} 📖'):
    chapter_prompt = f'Vous êtes un conteur talentueux. Écrivez le chapitre {chapter_number} de l histoire basée sur le plan précédent et le prompt : {prompt}.'
    try:
        chapter_response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role':'system', 'content':'Vous êtes un conteur talentueux.'}, {'role':'user', 'content':chapter_prompt}])
        chapter = chapter_response.choices[0].message['content'].strip()
        st.subheader(f'Chapitre {chapter_number} 📖')
        st.text_area('', chapter, height=300)
    except Exception as e:
        st.error(f'Une erreur est survenue: {e}. Essayez de reformuler votre prompt.')