import openai
import dbm
from tabulate import tabulate
from datetime import datetime
from src.util import is_null
from src.error import (
    APIKeyNotSetException,
    APIKeyNotValidException,
    PromptNotValidException,
    ModelNotSetException,
    ModelNotValidException,
)
from src.constant import (
    model_list,
    CACHE_PATH,
    LANGUAGE_MODEL_NAME,
    LANGUAGE_MODEL_API_KEY,
    LANGUAGE_MODEL_UPDATION_DATE,
)

path = CACHE_PATH

# The function returns information about all the models supported in the cli
def get_language_models():
    models = [[model] for model in model_list]
    return tabulate(models, headers=["model_name"], tablefmt="outline")


# The function fetches the selected model from the system cache
def get_selected_language_model_name():
    with dbm.open(path, "r") as db:
        model = db.get(LANGUAGE_MODEL_NAME)
        if model == None:
            raise ModelNotSetException()
        return model.decode()


# The function fetches the api key and the date when it was set from the system cache
def get_api_key():
    with dbm.open(path, "r") as db:
        api_key = db.get(LANGUAGE_MODEL_API_KEY)
        datetime = db.get(LANGUAGE_MODEL_UPDATION_DATE)
        if api_key == None:
            raise APIKeyNotSetException()
        return api_key.decode(), datetime.decode()


# The function sets the authentication api key.
def set_api_key(api_key=""):
    # "sk-BAwzEWP224DgC1k2tDAxT3BlckFJU7OMYhzfmEvqrEDuvlVA"
    now = datetime.now()

    if is_null(api_key):
        raise APIKeyNotValidException()

    with dbm.open(path, "c") as db:
        db[LANGUAGE_MODEL_API_KEY] = api_key
        db[LANGUAGE_MODEL_UPDATION_DATE] = now.strftime("%d/%m/%Y %H:%M:%S")


# The function saves the language model to be used for the response
def set_language_model(model_name=""):
    if is_null(model_name):
        raise ModelNotSetException()

    # Checks if the model is supported or not
    if model_name not in model_list:
        raise ModelNotValidException()

    with dbm.open(path, "c") as db:
        db[LANGUAGE_MODEL_NAME] = model_name


# The function queries the Open AI server for the selected language model response.
def fetch_language_model_response(prompt=""):
    if prompt == "" or prompt == None or type(prompt) != str:
        raise PromptNotValidException()

    with dbm.open(path, "r") as db:
        api_key = db.get(LANGUAGE_MODEL_API_KEY).decode()
        model_name = db.get(LANGUAGE_MODEL_NAME).decode()

        if is_null(api_key):
            raise APIKeyNotSetException()

        if is_null(model_name):
            raise ModelNotSetException()

    openai.api_key = api_key

    # Requests a response based on the prompt from openai
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
