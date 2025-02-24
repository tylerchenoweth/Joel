import streamlit as st
import requests
import json
from PIL import Image

def query_model(model, prompt):
    url = "http://localhost:11434/api/generate"  # Ollama has to be running
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False 
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "No response key found")
    else:
        return f"Error: {response.status_code}, {response.text}"

st.set_page_config(page_title="...🥃💃🦊", page_icon="", layout="wide")

# sidebar 
with st.sidebar:
    logo = Image.open("logo.webp")  # Ensure logo.webp is in the same directory as the app or provide correct path
    st.image(logo, width=logo.width, )
    # st.markdown("## AI Model Comparator")
    st.markdown("### \n\nSelect Model Services:")
    models = {"LLaMA2": "llama2", "DeepSeek": "deepseek-r1", "Mistral": "mistral"}
    selected_models = st.multiselect("Models:", options=list(models.keys()), default=list(models.keys()))

# Main content
st.title("Hi, I'm Joel")

# User input
prompt = st.text_area("Ask me a question!")

# Model selection in sidebar
# with st.sidebar:
#     st.markdown("### \n\nSelect Model Services:")
#     models = {"LLaMA2": "llama2", "DeepSeek": "deepseek-r1", "Mistral": "mistral"}
#     selected_models = st.multiselect("Models:", options=list(models.keys()), default=list(models.keys()))

# Generate response
if st.button("Generate Response") and prompt:
    results = {}
    for model_name in selected_models:
        try:
            model_key = models[model_name]
            results[model_name] = query_model(model_key, prompt)
        except KeyError:
            results[model_name] = "Model selection error."

    # Dynamically adjust the number of columns based on selected models
    cols = st.columns(len(selected_models))
    
    for idx, model_name in enumerate(selected_models):
        with cols[idx]:
            st.subheader(f"{model_name} Response")
            st.write(results.get(model_name, "No response generated."))
