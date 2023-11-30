# AI-Driven-translator

Translation tool that utilizes LLMs such as OpenAI to perform accurate translations. Built using Streamlit, Langchain and OpenAI

## Features
- Speech-to-text translation enables users to upload audio files in various languages and convert the audio into translated text. (However, the current Whisper API supports translation from any language to English, but not the reverse.) 
- Normal text translation: User can input english text and select a language from the list provided to convert english text into the translated text

## Built with (Frameworks)
- Streamlit  
- Langchain 🦜️🔗

## Prerequisites
The following packages are required to run this app locally:
1. Streamlit:
```
pip install streamlit
```
2. OpenAI:
```
pip install openai
```
3. Langchain:
```
pip install langchain
```
## Installation 
Follow the steps below to ensure that the project runs as intended locally:

1. Clone the repo
```
git clone https://github.com/MM58-crypto/AI-Driven-translator.git
```
2. Inside the project directory, create a virtual environment by running the following command:
```
python -m venv your_virtual_environment_name (eg: env)
```
3. Activate your virtual environment:

```
source env/bin/activate
```
4. Install the required packages from the <a href="#prerequisites">Prerequisites</a> section

5. Within the same directory, create a new file "config.py"

6. Within the config.py file, paste your own OpenAI API key:

(can be obtained from openai.com, API keys > + Create new secret key)
```
OPENAI_API_KEY ="YOUR_API_KEY"
```
7. Run the app by using the following command in the terminal:
```
streamlit run main.py
```

## Usage

https://github.com/MM58-crypto/AI-Driven-translator/assets/62597737/fc93ae3b-5191-48b9-bbd9-f6fe37b075d2
