import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Caffeineview · 서울 카페 뷰 파인더",
    page_icon="☕",
    layout="wide",
)

# Streamlit 기본 여백/헤더를 최소화해서 원본 디자인이 그대로 보이게 함
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        iframe { border: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PATH = pathlib.Path(__file__).parent / "caffeineview.html"
html_content = HTML_PATH.read_text(encoding="utf-8")

components.html(html_content, height=1550, scrolling=True)
