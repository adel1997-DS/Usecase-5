import streamlit as st


st.markdown(
    """
    <style>
    body {
        font-family: 'Arial'; 
        font-size: 20px; 
        color: white;
        direction: rtl;
        text-align: right; 
        background-color: #f0f2f6;
    }
    p, h2, h3 {
        font-size: 20px;
        color: white;
    }
    h1 {
        text-align: center;
        color: white;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("تبغى وظيفة؟")
st.markdown("<hr>", unsafe_allow_html=True)

# نص المحتوى
st.markdown("**أول شيء:** إذا بتدور وظيفة، ضبط السيفي. **ثاني شيء:** روح للأكثر منطقة فيها توظيف. هنا بنعرض لك أعلى عشر مناطق في التوظيف.")
st.image("images/نسبة التوظيف.png")

st.markdown("**اخترت المنطقة؟** خلني أطمنك، مهما كان جنسك ترى الطلب عالي على الجنسين. هنا نعرض لك نسبة الطلب.")
st.image("images/التوظيف حسب الجنس.png")

st.markdown("**هنا نطاق الرواتب للوظائف.**")
st.image("images/الراتب.png")

st.markdown("**السوق يطلب الخريجين الجدد أكثر من الخبرات.**")
st.image("images/الخبرة.png")

st.markdown("**بالتوفيق لك في رحلة البحث، وإن شاء الله عطيناك صورة واضحة عن سوق العمل.**")
