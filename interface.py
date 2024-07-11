import streamlit as st
import pandas as pd
from engine_component import get_ai_response

st.title("SpreadsheetAI")

with st.sidebar:
    st.title("Instruction")
    st.write("""
 1. upload Your Excel Files \n
 2. SpreadsheetAI will index your spreadsheet data \n
 3. Ask Your Question \n
 4. Our AI algorithm will analyze and provide an answer \n
 5. Answers are displayed in a clear format \n
 6. Refine & Export Insights \n
 7. Rephrase your query if needed \n
 8. SpreadSheetAi learns from your feedback \n
""")



# ------------------------------------ main section --------------------------------
lock = 1
while(lock):
     file_upload = st.file_uploader('Upload the Csv File','csv')
     lock = 0
     button = st.button('Upload')
     
     
if(button or not(lock)):

    if(file_upload):
        if(file_upload.type == "text/csv"):
            
            
            st.write(file_upload.type)

            # operation on CSV file
            data_1 = pd.read_csv(file_upload, encoding='Latin-1')
            st.dataframe(data_1)
            # visulization

            # ask question

        else:
            st.warning('Please upload the file of valid type')
    else:
        st.warning('please upload the file')

print(lock)
if(lock == 0):
        input_text = st.text_input("please eneter query")
        button_search  = st.button("proceed")
        if(button_search):
                json_data = data_1.to_json()
                
                alfa = (get_ai_response(input_text +""+str(json_data)))
                #56
                try:
                     filter_data = alfa.index("Top 3 Authoritative Sources Used")
                     st.write(alfa[56: filter_data])
                except:
                     st.write(alfa[56:])