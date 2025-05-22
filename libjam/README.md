# libjam
A library jam for Python.

## Modules
libjam consists of of 6 modules:

### Captain
responsible for handling command-line arguments

### Drawer
responsible for file operations

### Typewriter
responsible for transforming and printing text

### Clipboard
responsible for working with lists

### Notebook
responsible for configuration

### Flashcard
responsible for getting user input from the command line

## Example project
```python
#! /usr/bin/python

# Imports
import sys
from libjam import Captain

captain = Captain()

class CLI:
  def hello(self, text):
    print(text)
    if options.get('world').get('enabled'):
      print('world!')

cli = CLI()

# Inputs/Commands/Options configuration
app = "example"
description = "An example app for the libjam library"
# help = "" # If you wish to set your own help page text
commands = {
  'print':     {'function': cli.hello,
  'description': 'Prints given string'},
}
options = {
 'world': {'long': ['world'], 'short': ['w'],
 'description': 'Appends \'world\' after printing given input'},
}

# Getting program arguments
arguments = sys.argv
# Removing script name from arguments
arguments.remove(arguments[0])
# Generating help
help = captain.generate_help(app, description, commands, options)
# Interpreting user input
interpretation = captain.interpret(app, help, commands, arguments, options)
# Getting parsed output
function = interpretation.get('function')
options = interpretation.get('options')
# Executing function
exec(f"cli.{function}")
```
