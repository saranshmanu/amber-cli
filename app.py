import click
from src.core import (
    set_api_key,
    get_api_key,
    fetch_language_model_response,
    set_language_model,
    get_language_models,
    get_selected_language_model_name,
)
from src.constant import about_the_cli, AUTHENTICATION_COMMAND, MODEL_COMMAND, PROMPT_COMMAND, CONFIG_COMMAND
from src.error import APIKeyNotSetException, ModelNotSetException
from src.util import success, error_message
from rich.progress import track
from time import sleep

main = click.Group(help=about_the_cli)


# Authentication command module to perform actions based on your api key
@main.command("authentication", help=AUTHENTICATION_COMMAND["ABOUT"])
@click.option("--key", type=str, required=True, help=AUTHENTICATION_COMMAND["PARAMS"]["--key"])
def set_authentication_api_key(key):
    try:
        set_api_key(key)
        message = "{}: {}".format(success("Status"), "API key added!")
    except:
        message = error_message("Failed to set the api key.")
    click.echo(message)


# Checks whether the passed model is supported and if valid then use it by default
@main.command("model", help=MODEL_COMMAND["ABOUT"])
@click.option("--name", type=str, required=True, help=MODEL_COMMAND["PARAMS"]["--name"])
def set_language_model_name(name):
    try:
        set_language_model(name)
        message = "{}: {}".format(success("Status"), "The entered language model is valid. Saved your preference for future use.")
    except:
        message = error_message("Failed to set the model.")
    click.echo(message)


# Returns a generated response from the language model server
@main.command("prompt", help=PROMPT_COMMAND["ABOUT"])
@click.option("--message", type=str, required=True, help=PROMPT_COMMAND["PARAMS"]["--message"])
def get_language_model_response(message):
    try:
        for _ in track(range(10), description="[green]Generating a response"):
            sleep(0.1)

        response = fetch_language_model_response(message)
        choices = response.get("choices")

        for choice in choices:
            if choice != None:
                text = choice.get("text")
                text = text.replace("\n\n", "\n")
            response = "{}\n{}".format(success(message), text)
            click.echo(response)
    except:
        message = error_message("Failed to generate a response based on the entered prompt. Please try again later.")
        click.echo(message)


@click.group(name="show", help=CONFIG_COMMAND["ABOUT"])
def config_module():
    pass


# Returns a list of supported models
@config_module.command("supported-models", help=CONFIG_COMMAND["SUB_MODULE"]["SUPPORTED_MODELS"]["ABOUT"])
def show_supported_models():
    try:
        models = get_language_models()
        message = "{}\n\n{}".format(success("Models"), models)
    except:
        message = error_message("Failed to show the supported models from the system cache.")
    click.echo(message)


# Returns the selected Language model
@config_module.command("selected-model", help=CONFIG_COMMAND["SUB_MODULE"]["SELECTED_MODEL"]["ABOUT"])
def show_selected_language_model():
    try:
        key = get_selected_language_model_name()
        message = "{}: {}".format(success("Selected Model"), key)
    except ModelNotSetException:
        message = error_message("Langauge model not selected.")
    except:
        message = error_message("Failed to fetch the selected language model from the system cache.")
    click.echo(message)


# Returns the authenticaion api key
@config_module.command("api-key", help=CONFIG_COMMAND["SUB_MODULE"]["AUTHENTICATION_KEY"]["ABOUT"])
def show_api_key():
    try:
        key, datetime = get_api_key()
        message = "{}: {}\n".format(success("Key"), key)
        message += "{}: {}".format(success("Datetime"), datetime)
    except APIKeyNotSetException:
        message = error_message("API Key not set!")
    except:
        message = error_message("Failed to fetch the authentication api key from the system cache.")
    click.echo(message)


if __name__ == "__main__":
    main.add_command(config_module)
    main()
