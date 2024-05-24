Here is a suggested README.md for the easy_gui_prompt project:

```markdown
# easy_gui_prompt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python library to simplify the creation of GUI elements in the terminal using prompt-toolkit.

## Installation

Install easy_gui_prompt using pip:

```bash
pip install easy_gui_prompt
```

## Usage

Import the `EasyGUI` class:

```python
from easy_gui_prompt import EasyGUI
```

Create an instance of `EasyGUI` with a title:

```python
gui = EasyGUI("My GUI")
```

Add GUI elements using the available methods:

```python
# Yes/No prompt
result = gui.add_yes_no("confirm", "Do you want to proceed?", remember_value=True)

# Text input
name = gui.add_text("name", "Enter your name:", remember_value=True)

# Integer range
age = gui.add_int_range("age", "Enter your age:", 18, 100, remember_value=True)
```

Save the settings to a configuration file:

```python
gui.save_settings()
```

Restore default settings:

```python
gui.restore_default_settings()
```

## Configuration

The library automatically saves user preferences to a configuration file located at `~/.easy_gui/easy_gui.yml`. This allows the GUI to remember the last entered values when `remember_value=True` is used.

You can also access the configuration directly using the `get_config` and `save_config` functions:

```python
from easy_gui_prompt import get_config, save_config

config = get_config("My GUI")
save_config("My GUI", config)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
```

