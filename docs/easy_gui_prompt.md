<!-- markdownlint-disable -->

<a href="../easy_gui_prompt/easy_gui_prompt.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `easy_gui_prompt`
A module to help simplify the create of GUIs in terminals using python prompt-toolkit. 


---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_config`

```python
get_config(title: str)
```

Get the configuration dictionary without needing to initialize the GUI. 

:param title: title of the GUI 


---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `save_config`

```python
save_config(title: str, cfg: dict)
```

Save the configuration dictionary to a file. 

:param title: title of the GUI :param cfg: configuration dictionary 


---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EasyGUI`




<a href="../easy_gui_prompt/easy_gui_prompt.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(title: str)
```

Initialize the GUI. :param title: title of the GUI 




---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_dropdown`

```python
add_dropdown(
    tag: str,
    message: str,
    choices: list,
    *args,
    remember_value=False,
    **kwargs
) → str
```

Add a dropdown prompt to the GUI. :param tag: tag to identify the widget :param message: the message to display :param choices: list of choices for the dropdown :param args: args for the prompt :param remember_value: remember the last value :param kwargs: kwargs for the prompt :return: the selected choice 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_header`

```python
add_header(message: str)
```

Add a header to the GUI. :param message: the message to display 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_int`

```python
add_int(tag: str, message: str, *args, remember_value=False, **kwargs) → int
```

Add an integer prompt to the GUI. :param tag: tag to identify the widget :param args: args for the prompt :param remember_value: remember the last value :param kwargs: kwargs for the prompt :return: the integer entered 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_int_range`

```python
add_int_range(
    tag: str,
    message: str,
    vmin: int,
    vmax: int,
    *args,
    remember_value=False,
    **kwargs
) → int
```

Add an integer range to the GUI. :param tag: tag to identify the widget :param args: args for the prompt 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_text`

```python
add_text(tag: str, message: str, *args, remember_value=False, **kwargs) → str
```

Add a text prompt to the GUI. :param tag: tag to identify the widget :param args: args for the prompt :param remember_value: remember the last value :param kwargs: kwargs for the prompt :return: the text entered 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L82"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_yes_no`

```python
add_yes_no(tag: str, message: str, *args, remember_value=False, **kwargs) → bool
```

Add a yes/no prompt to the GUI. :param tag: tag to identify the widget :param args: args for the prompt :param remember_value: remember the last value :param kwargs: kwargs for the prompt :return: True if yes, False if no 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `restore_default_settings`

```python
restore_default_settings()
```

Restore the default settings. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `save_settings`

```python
save_settings()
```

Save the settings to the configuration file. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
