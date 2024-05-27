"""
A module to help simplify the create of GUIs in terminals using python prompt-toolkit.
"""

import yaml

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator

from pathlib import Path

CONFIG_PATH = Path.home() / ".easy_gui"


def get_config(title: str):
    """
    Get the configuration dictionary without needing to initialize the GUI.

    :param title: title of the GUI
    """

    config_file = CONFIG_PATH / f"{title}.yml"

    if not config_file.exists():
        return {}

    with open(config_file, "r") as f:
        cfg = yaml.load(f, Loader=yaml.SafeLoader)

    if title is None:
        return cfg
    elif title in cfg:
        return cfg[title]
    else:
        return {}


def save_config(title: str, cfg: dict):
    """
    Save the configuration dictionary to a file.

    :param title: title of the GUI
    :param cfg: configuration dictionary
    """
    config_file = CONFIG_PATH / f"{title}.yml"
    config_file.parent.mkdir(exist_ok=True)

    base_config = get_config(None)  # loads the config file
    base_config[title] = cfg

    with open(config_file, "w") as f:
        yaml.dump(base_config, f)


class EasyGUI:
    def __init__(self, title: str):
        """
        Initialize the GUI.
        :param title: title of the GUI
        """
        self.title = title
        self.cfg = get_config(title)

    def __getvalue__(self, tag: str):
        """
        Get the value of a widget.
        :param tag: tag to identify the widget
        :return: the value of the widget
        """
        return self.cfg[tag]

    def add_header(self, message: str):
        """
        Add a header to the GUI.
        :param message: the message to display
        """
        print("-" * len(message))
        print(message)
        print("-" * len(message))

    def add_yes_no(
        self, tag: str, message: str, *args, remember_value=False, **kwargs
    ) -> bool:
        """
        Add a yes/no prompt to the GUI.
        :param tag: tag to identify the widget
        :param args: args for the prompt
        :param remember_value: remember the last value
        :param kwargs: kwargs for the prompt
        :return: True if yes, False if no
        """
        if remember_value and tag in self.cfg:
            if self.cfg[tag]:
                kwargs["default"] = "yes"
            else:
                kwargs["default"] = "no"

        value = prompt(
            *args,
            message=message + " (yes/no): ",
            completer=WordCompleter(["yes", "no"]),
            validator=Validator.from_callable(
                lambda x: x in ["yes", "no"],
                error_message="Please enter 'yes' or 'no'.",
                move_cursor_to_end=True,
            ),
            **kwargs,
        )
        self.cfg[tag] = value.lower() == "yes"
        return self.cfg[tag]

    def add_text(
        self, tag: str, message: str, *args, remember_value=False, **kwargs
    ) -> str:
        """
        Add a text prompt to the GUI.
        :param tag: tag to identify the widget
        :param args: args for the prompt
        :param remember_value: remember the last value
        :param kwargs: kwargs for the prompt
        :return: the text entered
        """
        if remember_value and tag in self.cfg:
            kwargs["default"] = self.cfg[tag]
        value = prompt(message=message + ": ", *args, **kwargs)
        self.cfg[tag] = value
        return self.cfg[tag]

    def add_dropdown(
        self,
        tag: str,
        message: str,
        choices: list,
        *args,
        remember_value=False,
        **kwargs,
    ) -> str:
        """
        Add a dropdown prompt to the GUI.
        :param tag: tag to identify the widget
        :param message: the message to display
        :param choices: list of choices for the dropdown
        :param args: args for the prompt
        :param remember_value: remember the last value
        :param kwargs: kwargs for the prompt
        :return: the selected choice
        """
        if remember_value and tag in self.cfg:
            kwargs["default"] = self.cfg[tag]

        value = prompt(
            *args,
            message=message + ": ",
            completer=WordCompleter(choices),
            validator=Validator.from_callable(
                lambda x: x in choices,
                error_message="Please select a valid choice from the dropdown.",
                move_cursor_to_end=True,
            ),
            **kwargs,
        )
        self.cfg[tag] = value
        return self.cfg[tag]

    def add_int(
        self, tag: str, message: str, *args, remember_value=False, **kwargs
    ) -> int:
        """
        Add an integer prompt to the GUI.
        :param tag: tag to identify the widget
        :param args: args for the prompt
        :param remember_value: remember the last value
        :param kwargs: kwargs for the prompt
        :return: the integer entered
        """
        if remember_value and tag in self.cfg:
            kwargs["default"] = str(self.cfg[tag])
        value = prompt(
            *args,
            message=message + ": ",
            validator=Validator.from_callable(
                lambda x: x.isdigit(),
                error_message="Please enter a valid number.",
                move_cursor_to_end=True,
            ),
            **kwargs,
        )
        self.cfg[tag] = int(value)
        return self.cfg[tag]

    def add_int_range(
        self,
        tag: str,
        message: str,
        vmin: int,
        vmax: int,
        *args,
        remember_value=False,
        **kwargs,
    ) -> int:
        """
        Add an integer range to the GUI.
        :param tag: tag to identify the widget
        :param args: args for the prompt

        """
        if remember_value and tag in self.cfg:
            kwargs["default"] = str(self.cfg[tag])

        value = prompt(
            *args,
            message=message + f" ({vmin}-{vmax}): ",
            validator=Validator.from_callable(
                lambda x: vmin <= int(x) <= vmax,
                error_message=f"Please enter a valid number ({vmin}-{vmax}).",
                move_cursor_to_end=True,
            ),
            **kwargs,
        )
        self.cfg[tag] = int(value)
        return self.cfg[tag]

    def save_settings(self):
        """
        Save the settings to the configuration file.
        """
        save_config(self.title, self.cfg)

    def restore_default_settings(self):
        """
        Restore the default settings.
        """
        self.cfg = {}
        save_config(self.title, self.cfg)
