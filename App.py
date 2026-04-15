import streamlit as st
from groq import Groq

st.set_page_config("EVO.AI Bot", layout="wide")
st.title("EVO.AI - Content Generator")
st.image("EVO_chatbot_logo.jpg",width = 300 )

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
#Get Product Name and Audience for that product
product = st.text_input("Product")
audience = st.text_input("Audience")
#Button to Generate Content
if st.button("Generate Content"):
  prompt = f"Write marketing content for {product} targeting {audience}."
  response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user","content": prompt}]
  )
  st.session_state.text = response.choices[0].message.content
  text =response.choices[0].message.content
  st.write(text)
  # After Content Create - Download The File
if "text" in st.session_state:
    content = st.text_area("Generated Content", st.session_state.text, height=300)
    st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
else:
    st.info("Generate content first")
  
