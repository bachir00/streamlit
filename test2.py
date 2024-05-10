import hydralit as hy
import streamlit as st

app = hy.HydraApp(title='Secure Hydralit Data Explorer',
                  favicon="🚀", hide_streamlit_markers=True,
                  use_navbar=True, navbar_sticky=True)

selected_section = st.query_params().get("section", None)

with st.sidebar:
    expander = st.expander("Ml-Engineering")
    with st.expander("Machine Learning"):
        if st.button("Model 1"):
            st.experimental_set_query_params(section="model1")
        if st.button("Model 2"):
            st.experimental_set_query_params(section="model2")

@app.addapp(title="model 1")
def model1():
    hy.info('Hello from model1')

@app.addapp(title="model 2")
def model2():
    hy.info('Hello from model2')

if selected_section == "model1":
    model1()
elif selected_section == "model2":
    model2()
else:
    st.write("Select a model from the sidebar.")

app.run()
