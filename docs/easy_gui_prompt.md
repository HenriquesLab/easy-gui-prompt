<!-- markdownlint-disable -->

<a href="../easy_gui_prompt/easy_gui_prompt.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `easy_gui_prompt`





---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_config`

```python
get_config(title: Optional[str])
```

Get the configuration dictionary without needing to initialize the GUI. 



**Args:**
 
 - <b>`title`</b> (str):  Title of the GUI. If None, returns the entire configuration dictionary. 



**Returns:**
 
 - <b>`dict`</b>:  The configuration dictionary. 


---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `save_config`

```python
save_config(title: str, cfg: dict)
```

Save the configuration dictionary to a file. 



**Args:**
 
 - <b>`title`</b> (str):  Title of the GUI. 
 - <b>`cfg`</b> (dict):  Configuration dictionary. 


---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `EasyGUI`




<a href="../easy_gui_prompt/easy_gui_prompt.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(title: str)
```

Initialize the GUI. 



**Args:**
 
 - <b>`title`</b> (str):  Title of the GUI. 




---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

Add a dropdown prompt to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`choices`</b> (list):  List of choices for the dropdown. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`str`</b>:  The selected choice. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_header`

```python
add_header(message: str)
```

Add a header to the GUI. 



**Args:**
 
 - <b>`message`</b> (str):  The message to display. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_int`

```python
add_int(tag: str, message: str, *args, remember_value=False, **kwargs) → int
```

Add an integer prompt to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`int`</b>:  The integer entered. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

Add an integer range to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`vmin`</b> (int):  Minimum value of the range. 
 - <b>`vmax`</b> (int):  Maximum value of the range. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`int`</b>:  The integer entered. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_path_completer`

```python
add_path_completer(
    tag: str,
    message: str,
    *args,
    remember_value=False,
    **kwargs
) → Path
```

Add a path completer to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`Path`</b>:  The path entered. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_text`

```python
add_text(tag: str, message: str, *args, remember_value=False, **kwargs) → str
```

Add a text prompt to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`str`</b>:  The text entered. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_yes_no`

```python
add_yes_no(tag: str, message: str, *args, remember_value=False, **kwargs) → bool
```

Add a yes/no prompt to the GUI. 



**Args:**
 
 - <b>`tag`</b> (str):  Tag to identify the widget. 
 - <b>`message`</b> (str):  The message to display. 
 - <b>`remember_value`</b> (bool, optional):  Remember the last value. Defaults to False. 



**Returns:**
 
 - <b>`bool`</b>:  True if yes, False if no. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `restore_default_settings`

```python
restore_default_settings()
```

Restore the default settings. 

---

<a href="../easy_gui_prompt/easy_gui_prompt.py#L287"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `save_settings`

```python
save_settings()
```

Save the settings to the configuration file. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
