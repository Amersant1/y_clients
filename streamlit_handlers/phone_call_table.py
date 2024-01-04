import streamlit as st
import pandas as pd
from data_base import *
from utils import *
import time


ALREADY_CHECKED_DIDNT_ANSWER = dict()
ALREADY_CHECKED_ANSWERED=dict()

def __make_df():
    global ALREADY_CHECKED_ANSWERED
    global ALREADY_CHECKED_DIDNT_ANSWER
    calls = get_calls_today()
    data = {'user': [], "id": [], 'phone': [], 'service': [], "ответил": [], "сбросил": [],"нет необходимости звонить":[]}
    for call in calls:
        
        user_id = call.client.user_id_in_yclients
        call_id = call.id
        phone = call.client.phone
        service = call.service.name
        if call_id in ALREADY_CHECKED_DIDNT_ANSWER.keys():
            didnt_ans=True
        else:
            didnt_ans=False
        if call_id in ALREADY_CHECKED_ANSWERED.keys():
            answered=True
        else:
            answered=False
        data["user"].append(user_id)
        data["id"].append(call_id)
        data["phone"].append(phone)
        data["service"].append(service)
        data["ответил"].append(answered)
        data["сбросил"].append(didnt_ans)
        data["нет надобности звонить"].append(False)
    df = pd.DataFrame(data)
    return df



START_DF=__make_df()




def click_button(edited_df,):
    global START_DF
    global ALREADY_CHECKED_ANSWERED
    global ALREADY_CHECKED_DIDNT_ANSWER
    time.sleep(2)
    
    rows_didnt_answer=edited_df.loc[edited_df["сбросил"]==True].to_dict(orient='records')
    for row_didnt_answer in rows_didnt_answer:
        try:
            call_id = row_didnt_answer["id"]
            if call_id in ALREADY_CHECKED_DIDNT_ANSWER.keys():
                continue
            didnt_answer=row_didnt_answer["сбросил"]
        except:
            didnt_answer=False
        if didnt_answer:
            ALREADY_CHECKED_DIDNT_ANSWER[call_id]=1
            didnt_answer_change(id=call_id)
            # edited_df=edited_df.loc[edited_df["сбросил"]==False]  
    rows_doesnt_need_answer=edited_df.loc[edited_df["нет необходимости звонить"]==True].to_dict(orient='records')

    for row_didnt_answer in rows_doesnt_need_answer:
        try:
            call_id = row_didnt_answer["id"]
            # if call_id in ALREADY_CHECKED_DIDNT_ANSWER.keys():
            #     continue
            didnt_answer=row_didnt_answer["нет необходимости звонить"]
        except:
            didnt_answer=False
        if didnt_answer:
            # ALREADY_CHECKED_DIDNT_ANSWER[call_id]=1
            doesnt_need_to_answer(id=call_id)
            # edited_df=edited_df.loc[edited_df["сбросил"]==False]  

    rows_answered = edited_df.loc[edited_df["ответил"]==True].to_dict(orient='records')
    for row_answer in rows_answered:
        try:
            call_id = row_answer["id"]
            if call_id in ALREADY_CHECKED_ANSWERED.keys():
                continue
            answered=row_answer["ответил"]
        except:
            answered=False
        if answered:
            ALREADY_CHECKED_ANSWERED[call_id]=1
            answered_call(id=call_id)
            # edited_df=edited_df.loc[edited_df["ответил"]==False]  

    START_DF = edited_df.copy()
    # st.session_state["df_value"]=edited_df.copy()
    return edited_df


# Streamlit app
def phone_main():

    global START_DF

    st.title("Звонки на сегодня")
    df=START_DF
    # Call __make_df to create the initial DataFrame
    # st.session_state["df"]=df
    # Display the DataFrame
    edited_df = st.data_editor(
        df,
        key="editor",
        num_rows="dynamic",
    )

    if edited_df is not None and not edited_df.equals(START_DF):
        # This will only run if
        # 1. Some widget has been changed (including the dataframe editor), triggering a
        # script rerun, and
        # 2. The new dataframe value is different from the old value
        df=click_button(edited_df)
        edited_df=df
        # st.session_state["df_value"] = edited_df
        START_DF=df
        # new_df = st.data_editor(
        #     edited_df.loc[edited_df["сбросил"]==False],
        #     key=f"editor{COUNT}",
        #     num_rows="dynamic",
        # )
        # edited_df.empty()
    # # Add a custom column with buttons using HTML and JavaScript
    # for index, row in df.iterrows():
    #     button_id = f"button_{row['id']}_{index}"
    #     button_label = f"сбросил ({row['id']})"
    #     button_code = f'<button id="{button_id}" onclick="handleButtonClick({row["id"]})">{button_label}</button>'
    #     st.write(button_code, unsafe_allow_html=True)

    # Add a button column inside the table using custom HTML
    # for index, row in df.iterrows():
    #     button_id = f"button_{index}"
    #     button_label = f"сбросил ({row['id']})"
    #     button_code = f'<button id="{button_id}" onclick="handleButtonClick({row["id"]})">{button_label}</button>'
    #     st.write(button_code, unsafe_allow_html=True)