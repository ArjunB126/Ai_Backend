import os
import vertexai
from vertexai.language_models import TextGenerationModel
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "... Add Path ..."
PROJECT_ID = "total-entity-409908"  
LOCATION = "us-central1" 

vertexai.init(project=PROJECT_ID, location=LOCATION)

def create_session():
    chat_model = vertexai.language_models.ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat
