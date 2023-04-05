import click


def success(text):
    return click.style(text, fg="green", bold=True)


def error_message(message):
    error_placeholder = click.style("Error", fg="red", bold=True)
    return "{}: {}".format(error_placeholder, message)


def is_null(text=""):
    return text == "" or text == None or type(text) != str
