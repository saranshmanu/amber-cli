import click
from src.core import set_api_key
from src.core import get_api_key
from src.core import get_api_key_date
from src.core import get_gpt_response

from src.util import success, error

about = """
ChatGPT is an artificial-intelligence chatbot developed by OpenAI and launched in November 2022. 
It is built on top of OpenAI's GPT-3.5 and GPT-4 families of large language models and has been 
fine-tuned using both supervised and reinforcement learning techniques.

The command line sends a request and generates a response based on the prompt entered.
"""
main = click.Group(help=about)


about_authentication_command = """
Response is only generated after the api key is added to the command line.
"""


@main.command("authentication", help=about_authentication_command)
@click.option("--key", required=True, help="OpenAI authentication api key")
def command_set_api_key(key):
    try:
        set_api_key(key)
        response = "{}: API key added!".format(success("Status"))
        click.echo(response)
    except:
        click.echo(error() + ": Failed to set the api key.")


about_prompt_command = """
Returns a generated response from the GPT server
"""


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
        click.echo(
            error()
            + ": Failed to generate a response based on the entered prompt. Please try again later."
        )


about_get_datetime_command = """
Returns the time when the key was set
"""


@main.command("get-datetime", help=about_get_datetime_command)
def command_show_api_key_date():
    try:
        datetime = get_api_key_date()
        response = "{}: {}".format(success("Datetime"), datetime)
        click.echo(response)
    except:
        click.echo(error() + ": Failed to get the datetime from the system cache.")


about_get_key_command = """
Returns the authentication api key in use
"""


@main.command("get-key", help=about_get_key_command)
def command_show_api_key():
    try:
        key = get_api_key()
        response = "{}: {}".format(success("Key"), key)
        click.echo(response)
    except:
        click.echo(error() + ": Failed to get the api key from the system cache.")


if __name__ == "__main__":
    main()
