from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_coversation():
    context = ""
    print("The AI chatbot is now running, enter 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        answer = chain.invoke({"context": context, "question": user_input})
        print("Chatbox response: ", answer)
        context  += f"\nUser: {user_input}\n AI: {answer}"

if __name__ == "__main__":
    handle_coversation()