import streamlit as st


@st.cache_data(ttl=600)
def cache_ativos(func):
    return func()


def limpar_cache():
    st.cache_data.clear()