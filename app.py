import click
from src.core import set_api_key
from src.core import get_api_key
from src.core import get_gpt_response
from src.core import set_model
from src.core import show_model_list
from src.core import get_selected_model_name

from src.util import success, error
from src.constant import (
    about_the_cli,
    about_authentication_command,
    about_model_command,
    about_prompt_command,
    about_show_supported_model_command,
    about_get_datetime_command,
    about_get_key_command,
)

main = click.Group(help=about_the_cli)


@main.command("authentication", help=about_authentication_command)
@click.option("--key", required=True, help="OpenAI authentication api key")
def command_set_api_key(key):
    try:
        set_api_key(key)
        response = "{}: API key added!".format(success("Status"))
        click.echo(response)
    except:
        click.echo(error() + ": Failed to set the api key.")


@main.command("model", help=about_model_command)
@click.option("--name", required=True, help="OpenAI supported model name")
def command_set_selected_model(name):
    try:
        set_model(name)
        message = ": The selected model name is valid. Added to the cache."
        click.echo(success("Status") + message)
    except:
        click.echo(error() + ": Failed to set the model.")


@main.command("prompt", help=about_prompt_command)
@click.option(
    "--message", required=True, help="Prompt based on what the response is generated"
)
def commaand_get_gpt_response(message):
    try:
        response = get_gpt_response(message)
        choices = response.get("choices")

        for choice in choices:
            if choice != None:
                text = choice.get("text")
                text = text.replace("\n\n", "\n")
            response = "{}\n{}".format(success("Response"), text)
            click.echo(response)
    except:
        message = ": Failed to generate a response based on the entered prompt. Please try again later."
        click.echo(error() + message)


@main.command("show-supported-models", help=about_show_supported_model_command)
def command_show_supported_models():
    try:
        models = show_model_list()
        response = "{}\n\n{}".format(success("Models"), models)
        click.echo(response)
    except:
        message = ": Failed to show the supported models from the system cache."
        click.echo(error() + message)


@main.command("get-selected-model", help=about_get_key_command)
def command_get_selected_model_name():
    try:
        key = get_selected_model_name()
        response = "{}: {}".format(success("Key"), key)
        click.echo(response)
    except:
        message = ": Failed to get the selected model from the system cache."
        click.echo(error() + message)


@main.command("get-api-key", help=about_get_key_command)
def command_show_api_key():
    try:
        key, datetime = get_api_key()
        response = "{}: {}".format(success("Key"), key)
        click.echo(response)
        response = "{}: {}".format(success("Datetime"), datetime)
        click.echo(response)
    except:
        message = ": Failed to get the api key from the system cache."
        click.echo(error() + message)


if __name__ == "__main__":
    main()
