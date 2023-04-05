import os

model_list = [
    "text-davinci-003",
    "text-davinci-002",
    "code-davinci-002",
    "code-davinci-001",
    "code-cushman-002",
    "code-cushman-001",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
    "ada",
    "babbage",
    "davinci",
    "curie",
]

about_the_cli = """
Language modeling (LM) is the use of various statistical and probabilistic techniques to determine 
the probability of a given sequence of words occurring in a sentence. Language models analyze bodies 
of text data to provide a basis for their word predictions.

Example of a Language Model,
ChatGPT is an artificial-intelligence chatbot developed by OpenAI and launched in November 2022. 
It is built on top of OpenAI's GPT-3.5 and GPT-4 families of large language models and has been 
fine-tuned using both supervised and reinforcement learning techniques.

The command line sends a request and generates a response based on the entered prompt by using Open AI's Language Models.
"""

AUTHENTICATION_COMMAND = {
    "ABOUT": "Authentication command module to perform actions based on your api key",
    "PARAMS": {"--key": "openai authentication api key"},
}

MODEL_COMMAND = {
    "ABOUT": "Model command module to check whether the selected model name is supported and select for default use",
    "PARAMS": {"--name": "Language model name"},
}

PROMPT_COMMAND = {
    "ABOUT": "Prompt command module to generate a response based on the selected language model",
    "PARAMS": {"--message": "Input prompt"},
}

CONFIG_COMMAND = {
    "ABOUT": "Configuration command module to show the data variables saved in the system cache",
    "SUB_MODULE": {
        "SELECTED_MODEL": {"ABOUT": "Returns the selected language model"},
        "AUTHENTICATION_KEY": {"ABOUT": "Returns the authenticaion api key"},
        "SUPPORTED_MODELS": {"ABOUT": "Returns a list of supported language models"},
    },
}


CACHE_PATH = os.path.expanduser("~") + "/.language-model"

LANGUAGE_MODEL_NAME = "LANGUAGE_MODEL_NAME"
LANGUAGE_MODEL_API_KEY = "LANGUAGE_MODEL_API_KEY"
LANGUAGE_MODEL_UPDATION_DATE = "LANGUAGE_MODEL_UPDATION_DATE"
