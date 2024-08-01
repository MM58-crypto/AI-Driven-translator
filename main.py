import streamlit as st
import whisper
#import os
#import config
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv, find_dotenv


st.title('Multilingual Text + Audio Translation (tool)')
load_dotenv(find_dotenv())
openai_api_key == st.secrets["OPENAI_API_KEY"] 
#os.getenv("OPENAI_API_KEY")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.success(llm(input_text))

#prompt template is needed for translation
#prompt = PromptTemplate.from_template("Translate {text} to {selected_lang}")
st.header('Text Translation')
with st.form('my_form'):
  selected_language = st.selectbox(
      'Select a language from the options below',
      ('German', 'French', 'Italian', 'Arabic', 'Japanese')
      )
  text = st.text_area('Enter text to translate:', 'What is your name?')
  prompt = PromptTemplate(input_variables=["input_text", "selected_lang"],
                       template="Translate {input_text} to {selected_lang}",)
  submitted = st.form_submit_button('Submit')
 # if not openai_api_key.startswith('sk-'):
 #   st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted:
    generate_response(prompt.format(input_text=text, selected_lang=selected_language))

# translate from audio file
st.header('Translation from an audio file (to English)') # to english
with st.form('audio_translation_form'):
 # speech/audio -> text
  upload_audio_file = st.file_uploader("Upload an audio file to translate") 
  def translate_from_file(file): 
    #model = whisper.load_model("base")
    if file is not None:
      #result = model.translate(file)
      transcript = openai.Audio.translate("whisper-1", file)
      st.success(transcript["text"])
  translate_btn = st.form_submit_button('Translate')
  if translate_btn:
    translate_from_file(upload_audio_file) 

# Translate from file  
# detect lang from doc then translate into desired language
# download translated document
#st.header('Translation from text file')
#with st.form('translate_from_txt_file'):
#   selected_language = st.selectbox(
#      'Select a language from the options below',
#      ('German', 'French', 'Italian', 'Arabic', 'Japanese', 'spanish')
#      )
#   uploaded_doc = st.file_uploader("Upload a doc to translate")
#   submit = st.form_submit_button('Translate file')

#   st.success(translated_document[0].page_content)
 
   



