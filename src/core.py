import openai
import dbm
from datetime import datetime
from src.error import APIKeyNotSetException, PromptNotSetException

model_name = "text-davinci-003"
path = "cache"

# The function fetches the api key from the system cache
def get_api_key():
    with dbm.open(path) as db:
        api_key = db.get("CLI_GPT_API_KEY").decode()
        return api_key


# The function fetches the date when the api key was updated and saved in the system cache
def get_api_key_date():
    with dbm.open(path) as db:
        datetime = db.get("CLI_GPT_API_LAST_UPDATED_DATE").decode()
        return datetime


# The function sets the authentication api key.
def set_api_key(api_key=""):
    # "sk-BAwzEWP224DgC1k2tDAxT3BlckFJU7OMYhzfmEvqrEDuvlVA"
    now = datetime.now()

    if api_key == "" or api_key == None:
        raise APIKeyNotSetException()

    with dbm.open(path, "c") as db:
        db["CLI_GPT_API_KEY"] = api_key
        db["CLI_GPT_API_LAST_UPDATED_DATE"] = now.strftime("%d/%m/%Y %H:%M:%S")

    return


# The function queries the Open AI server for the GPT response.
def get_gpt_response(prompt=""):
    with dbm.open(path) as db:
        api_key = db.get("CLI_GPT_API_KEY").decode()
        if api_key == "" or api_key == None or type(api_key) != str:
            raise APIKeyNotSetException()

    if prompt == "" or prompt == None or type(prompt) != str:
        raise PromptNotSetException()

    openai.api_key = api_key

    response = openai.Completion.create(
        model=model_name,
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response
