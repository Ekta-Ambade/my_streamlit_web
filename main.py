import streamlit as st
st.title("Streamlit Introduction")
st.subheader("Exploring Streamlit")

st.text("Start by selecting a AI model you are familier with.")
st.write("We will suggest some tools!!")

prompt=st.sidebar.text_input("Enter your prompt:","Write Something....")
if prompt:
    st.sidebar.write(f"hello,{prompt}")

llm= st.sidebar.selectbox(
    "Pick  an  LLM  you  have  used  or  want  to  explore",
    ["GPT-3.5","GPT-4o","GPT-5","Claude 3","DeepSeek"]
    
)
st.sidebar.write(f"You Selected:{llm}")

if st.button("Send"):
    st.write("Button clicked!!")

msg=st.text_area("Message:")
if msg:
    st.write(f"You wrote:{msg}")

agree = st.checkbox("Enables autonomous agent mode")

if agree:
    st.write("Great! Your AI is now active.You can use it independenly.")    

temp = st.radio(
    "Select Temperature Setting:",
    ["Stable(0.2)", "Balanced(0.7)", "Creative(1.0)"],
    
)

st.write(f"Model set to:{temp}")   

token = st.slider("Max token limit:", 100, 2000,300)
st.write(f"LLM will respond upto {token} tokens.")

date=st.date_input("When do you want to launch your AI?")
st.write(f"Launching date:{date}")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

with st.expander("See explanation:"):
    st.write('''
        -The chart above shows some numbers I picked for you.

        -I rolled actual dice for these, so they're *guaranteed* to
        be random.

        -Basic info is clearly mentioned.
    ''')
st.markdown("## Webdevlopment")  
st.markdown(">You have completed you course!!")  
   
