import streamlit as st
from langchain_groq import ChatGroq

# تحديث الاستيرادات لـ LangChain الحديثة
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import Tool, initialize_agent
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_classic.chains import LLMMathChain, LLMChain # ⬅️ الحفاظ على LLMMathChain
## Set upi the Stramlit app
st.set_page_config(page_title="Text To MAth Problem Solver And Data Serach Assistant",page_icon="🧮")
st.title("Text To Math Problem Solver Uing Google Gemma 2")

groq_api_key=st.sidebar.text_input(label="Groq API Key",type="password")


if not groq_api_key:
    st.info("Please add your Groq APPI key to continue")
    st.stop()

# استخدام نموذج Qwen (حسب آخر إدخال لديك)
llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)


## Initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find the vatious information on the topics mentioned"
)

## Initializa the MAth tool

# 1. تهيئة الآلة الحاسبة البسيطة (تستخدم وظيفة NumExpr الداخلية ولا تحتاج LLMMathChain)
math_chain=LLMMathChain.from_llm(llm=llm)
# 2. تعريف الأداة باستخدام وظيفة الآلة الحاسبة البسيطة
calculator_tool = Tool(
    name="Calculator",
    func=math_chain.run, # ⬅️ ربط الأداة بدالة التشغيل المضمونة
    description="A tools for answering math related questions. Only input mathematical expression need to be provided"
)

prompt="""
Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

## Combine all the tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## initialize the agents

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator_tool,reasoning_tool], # ⬅️ استخدام الاسم الصحيح calculator_tool
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a MAth chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## LEts start the interaction
# ⬅️ حقل إدخال فارغ
question=st.text_area("Enter your question:")

if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### Response:')
            st.success(response)

    else:
        st.warning("Please enter the question")