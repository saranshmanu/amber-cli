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

Examples,
ChatGPT is an artificial-intelligence chatbot developed by OpenAI and launched in November 2022. 
It is built on top of OpenAI's GPT-3.5 and GPT-4 families of large language models and has been 
fine-tuned using both supervised and reinforcement learning techniques.

The command line sends a request and generates a response based on the entered prompt by using Open AI's Language Models.
"""

about_authentication_command = """
Response is only generated after the api key is added to the command line.
"""

about_model_command = """
Checks whether the passed model is supported and if valid then use it by default
"""

about_prompt_command = """
Returns a generated response from the GPT server
"""

about_show_supported_model_command = """
Returns the list of supported models using the command line
"""

about_get_key_command = """
Returns the selected AI model in use
"""

about_get_datetime_command = """
Returns the time when the key was set
"""
about_get_key_command = """
Returns the authentication api key in use
"""

CACHE_PATH = "cache"

CLI_GPT_MODEL = "CLI_GPT_MODEL"
CLI_GPT_API_KEY = "CLI_GPT_API_KEY"
CLI_GPT_API_LAST_UPDATED_DATE = "CLI_GPT_API_LAST_UPDATED_DATE"
