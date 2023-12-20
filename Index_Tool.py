import tkinter as tk
from tkinter import OptionMenu
import openai
import os
import constants as c
#import Build_Index as bi
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, Document

ai_tools = "ai"
digital_marketing = "digmktg"
learning_development = "ld"
personal_ai = "gn"
aipath = "Z:\\MyAI\\AI\\Index\\Index"
query_engine = None
root = tk.Tk()

def create_ui():
    chat_button = tk.Button(root, text="Submit")
    chat_button.pack(side="bottom")

    input_textbox = tk.Text(root, width=600, height=200)
    input_textbox.pack(side="top", fill="x")

    response_textbox = tk.Text(root, width=600, height=200)
    response_textbox.pack(side="bottom", fill="x", expand=True)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    response_textbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=response_textbox.yview)




# def show_button():
#     chat_button.pack()
#
# def hide_button():
#     chat_button.pack_forget()
#
# def clear_text():
#     input_textbox.delete("1.0", tk.END)
#     response_textbox.delete("1.0", tk.END)
#
# root.update()
#
# clear_button = tk.Button(root, text="Clear", command=clear_text)
# clear_button.pack(side="bottom")
#
#
#
# topics = ["Select", "Personal AI", "AI Tools", "Digital Marketing", "Learning Development"]
# topicdropdown = tk.StringVar(root)
# topicdropdown.set(topics[0])
# topicdropdown.trace('w', show_button())
#
# actions = ["Select", "build", "ask"]
# actiondropdown = tk.StringVar(root)
# actiondropdown.set(actions[0])
# actiondropdown.trace('w', show_button)
#
# topicdrop = OptionMenu(root, topicdropdown, *topics)
# topicdrop.pack(side="top")
#
# actiondrop = OptionMenu(root, actiondropdown, *actions)
# actiondrop.pack(side="top")
#
# root.update()
#
# def build_index(topic, action):
#     if topic == ai_tools:
#         bi.AskBuild(ai_tools, "build")
#     elif topic == digital_marketing:
#         bi.AskBuild(digital_marketing, "build")
#     elif topic == learning_development:
#         bi.AskBuild(learning_development, "build")
#     elif topic == personal_ai:
#         bi.AskBuild(personal_ai, "build")
#
#
# def build_topic(topic):
#     if topic == ai_tools:
#         bi.AskBuild(ai_tools, "ask")
#         aipath = "Z:\\MyAI\\AI\\Index\\Index\\"
#     elif topic == digital_marketing:
#         bi.AskBuild(digital_marketing, "ask")
#         aipath = "Z:\\MyAI\\digimtg\\Index\\Index\\"
#     elif topic == learning_development:
#         bi.AskBuild(learning_development, "ask")
#         aipath = "Z:\\MyAI\\ld\\Index\\Index\\"
#     elif topic == personal_ai:
#         bi.AskBuild(personal_ai, "ask")
#         aipath = "Z:\\MyAI\\gn\\Index\\Index\\"
#     return aipath
#
#
# def read_index():
#     trgt_aipath = build_topic(topic)
#     storage_context = StorageContext.from_defaults(persist_dir=aipath)
#     read_index = load_index_from_storage(storage_context)
#     query_engine = read_index.as_query_engine()
#
#
# def get_gpt_response(prompt):
#     response = query_engine.query(prompt)
#     response_text = response.response
#     return response_text
#
def main():
     create_ui()
     root.mainloop()

#     topics = ["Select", "Personal AI", "AI Tools", "Digital Marketing", "Learning Development"]
#     topicdropdown = tk.StringVar(root)
#     topicdropdown.set(topics[0])
#     topicdropdown.trace('w', show_button)
#
#     actions = ["Select", "build", "ask"]
#     actiondropdown = tk.StringVar(root)
#     actiondropdown.set(actions[0])
#     actiondropdown.trace('w', show_button)
#
#     if topicdropdown.get() == "Select" or actiondropdown.get() == "Select":
#         hide_button()
#
#     # if actiondropdown.get() == "ask":
#     #     chat_button.config(command=chatbot)
#     # elif actiondropdown.get() == "build":
#     #     chat_button.config(command=lambda: build_index(topicdropdown.get()))
#

# root.mainloop()
#
if __name__ == "__main__":
    main()