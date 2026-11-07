from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
import os

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    api_key = os.environ['GEMINI_API_KEY'],
    temperature=0
    )

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),      
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")                                     # {} ---> place holder to insert some messeges inside promt templete  we can use 
])

chain = prompt | llm | StrOutputParser()

store ={}
def get_session_history(session_id):                         # session history if the session already existt else create a new session and return empty history
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()     #   InMemoryChatMessageHistory()  --> to create history insde python memory 
    return store[session_id]

chain_with_memory = RunnableWithMessageHistory(              # RunnableWithMessageHistory --> it helps run the chain with memory 
    chain,
    get_session_history,
    input_messages_key="input",                              # it stores the input
    history_messages_key="history"                           # it stores the session history
)

'''
start

user input

session_id = session_1(default session id)
user input

do you want to continue the session 
yes
no 

create new session or exit 

'''
session_id = 1
print("----START----")

while True:
    user_input = input('''
                        Enter your querry
                        or 
                        For exit type => exit''').lower()
    if user_input=='exit':
        print('Thank You 😎')
        break
    try:
        response = chain_with_memory.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": session_id}}
        )
        print(f'''
                  User input => {user_input}
                  Response  => {response}
            ''')
    except Exception as e:
        print(f"Error => {e}")
        break
    new_session = input('''if you want to continue with the 
                           session type anything except 'no'
                           For new session => No''').lower()
    if new_session == 'no':
        session_id +=1