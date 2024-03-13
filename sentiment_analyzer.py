import openai
import streamlit as st

openai.api_key = st.secrets("OPENAI_API_KEY")

header_style = """
    text-align: center;
    color: white;
    background-color: #0080FF;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 30px;
"""

def sentiment_analyzer(input_prompt):
    response = openai.chat.completions.create(model='gpt-3.5-turbo-0125', messages=[{'role': 'user', 'content': f'{input_prompt}'},
                                                                                  {'role': 'system', 'content': 'You are a sentiment analyzer. You will analyze the text given to you and answer in just a single word: Positive, Negative or Neutral'}], temperature=0.1, max_tokens=1, n=1,  stop=["/n"])
    return response


def main():
    st.set_page_config("Zain's Sentiment Analyzer", page_icon="💭")
    st.markdown(f"<h1 style='{header_style}'>Zain's Sentiment Analyzer</h1>", unsafe_allow_html=True)
    input_prompt = st.text_area("Enter the text: ")
    if st.button("Submit"):
        response = sentiment_analyzer(input_prompt)
        final = response.choices[0].message.content

        st.write(response.choices[0].message.content)
        if final == "Negative":
            st.markdown("<h1 style='text-align: center;'>😔 😞 👎 😢 💔</h1>", unsafe_allow_html=True)
        elif final == "Positive":
            st.markdown("<h1 style='text-align: center;'>😊 😄 👍 🌟 💖</h1>", unsafe_allow_html=True)
        else:
            st.markdown("<h1 style='text-align: center;'>😐 😶 😑 🤔</h1>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
