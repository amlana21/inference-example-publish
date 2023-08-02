import streamlit as st
from dotenv import load_dotenv
import os
import openai

def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.api_key)
    st.set_page_config(page_title="Inference Example", page_icon="📝")
    st.header("Test Inference")
    st.divider()
    st.write("## 0 Shot Inference")
    st.write("### Using OpenAI text-davinci-002 model")
    user_question = st.text_input("Enter Prompt1")
    # Classify this review: I loved this movie \n Sentiment:
    if user_question:
        resp=openai.Completion.create(model="text-davinci-002",prompt=f"{user_question}",temperature=0,max_tokens=100)
        st.write(resp['choices'][0]['text'])
        print(resp)
    st.divider()
    st.write("## 1 Shot Inference")
    st.write("### Using OpenAI text-ada-001")
    user_question1 = st.text_input("Enter Prompt2")
    # Classify this review: I loved this movie \n Sentiment:
    # Classify this review: I loved this movie \n Sentiment: Positive Classify this review: I hatedthis movie \n Sentiment:
    if user_question1:
        resp2=openai.Completion.create(model="text-ada-001",prompt=f"{user_question1}",temperature=0,max_tokens=100)
        st.write(resp2['choices'][0]['text'])
        print(resp2)
    st.divider()
    st.write("## Few Shot Inference")
    st.write("### Using OpenAI davinci")
    user_question2 = st.text_area("Enter Prompt3")
    # Classify this review: I loved this movie\nSentiment:
    # Classify this review: I loved this movie\nSentiment: Positive\nClassify this review: I hated this movie\nSentiment:Negative\nClassify this review: This movie is good\nSentiment: Positive\nClassify this review: This movie is good\nSentiment:
    # Classify this review: I loved this movie \n Sentiment: Positive Classify this review: I hatedthis movie \n Sentiment: Negative Classify this review: I loved this movie \n Sentiment: Positive Classify this review: I hated this movie \n Sentiment: Negative Classify this review: I hated this movie \n Sentiment:
    # Classify this review: I loved this movie \n Sentiment: Positive \n Classify this review: I hatedthis movie \n Sentiment: Negative \n Classify this review: This movie is good \n Sentiment: Positive \n Classify this review: I liked this movie \n Sentiment: 
    if user_question2:
        resp3=openai.Completion.create(model="davinci",prompt=f"{user_question2}",temperature=0,max_tokens=100)
        st.write(resp3['choices'][0]['text'])
        print(resp3)

if __name__=="__main__":
    main()