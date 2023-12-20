import os
from openai import OpenAI

import constants as c
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from pathlib import Path

c.Get_API()

client = OpenAI()


def CreateUpdate_Index(basepath, masterdocs, newdocs, indexpath):
    print('Create/Update function running')

    # Check if index path directory is empty
    chkindexpath = basepath + indexpath
    index_dir = Path(chkindexpath)
    is_empty = len(os.listdir(index_dir)) == 0

    if is_empty:
        print('Running creating index function')
        Create_Index(basepath, masterdocs, newdocs, indexpath)
    else:
        print('Running updating index function')
        Update_Index(basepath, masterdocs, newdocs, indexpath)


def Create_Index(basepath, masterdocs, newdocs, indexpath):
    print('Creating index')

    # Specify the input_dir path
    docpath = basepath + masterdocs
    documents = SimpleDirectoryReader(input_dir=docpath).load_data()

    # Create an index from the documents
    index = VectorStoreIndex.from_documents(documents)

    # Persist index to disk
    saveindexpath = basepath + indexpath
    index.storage_context.persist(saveindexpath)

    print('Index created and saved')


def Update_Index(basepath, masterdocs, newdocs, indexpath):
    print('Update index')

    # Load existing storage context
    updatedocpath = basepath + indexpath
    storage_context = StorageContext.from_defaults(persist_dir=updatedocpath)

    # Load existing index from storage
    index = load_index_from_storage(storage_context)
    print('Existing index loaded')

    # Index some new documents
    for doc in newdocs:
        index.add_documents(doc)
    print('New docs added')

    # Persist updated index to same storage
    storage_context.persist(index)
    print('New index saved')


def AskQuestion(basepath, indexpath, question):
    print('Running ask quesstion function')

    # Rebuild storage context
    trgtindexpath = basepath + indexpath
    storage_context = StorageContext.from_defaults(persist_dir=trgtindexpath)

    # Load index from the storage context
    new_index = load_index_from_storage(storage_context)
    print('Index loaded')

    # Create a query engine from the index
    query_engine = new_index.as_query_engine()

    question = ""
    while question.lower() != "exit":
        question = input("Enter question: ")
        if question.lower() != "exit":
            response = query_engine.query(question)
            print(response)


persistpath = 'AIToolsIndex\\Index'
newdocspath = 'AITools_Docs'
masterpath = 'AIToolsDocs_Master'

basepath = 'Z:\\MyCustomAI\\AIToolsApp\\'

question = 'List 5 AI tools'

CreateUpdate_Index(basepath, masterpath, newdocspath, persistpath)

# AskQuestion(basepath, persistpath, question)

print('Create or Update process finished')