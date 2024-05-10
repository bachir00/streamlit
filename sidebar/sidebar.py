import streamlit as st 
# Définir les éléments du menu latéral
def get_selected_model():
  with st.sidebar:
    expander = st.expander("Ml-Engineering")
    with st.expander("Machine Learning"):
      selected_model = None
      if st.button("Model 1"):
        selected_model = "model1"
      elif st.button("Model 2"):
        selected_model = "model2"
      return selected_model