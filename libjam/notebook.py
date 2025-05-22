# Imports
import os, tomllib, configparser
from .drawer import Drawer

# Jam classes
drawer = Drawer()

# Deals with configs and reading/writing files
class Notebook:

  def __init__(self):
    # Pre-requisites
    script_folder = os.path.dirname(os.path.realpath(__file__))
    script_folder = drawer.get_parent(script_folder)
    self.config_template_file = f"{script_folder}/config.toml.in"

  # Checking if config exists, and creating one if it does not
  def check_config(self, config_file: str):
    config_template = open(self.config_template_file, 'r').read()
    config_folder = drawer.get_parent(config_file)
    if drawer.is_folder(config_folder) is False:
      drawer.make_folder(config_folder)
    if drawer.is_file(config_file) is False:
      drawer.make_file(config_file)
      with open(config_file, 'w') as config:
        config.write(config_template)
      print(f"Created configuration file in '{config_folder}'.")
    return config_file

  # parsing a toml config
  def read_toml(self, config_file: str):
    config_file = os.path.normpath(config_file)
    # Parsing config
    data = open(config_file, 'r').read()
    try:
      data = tomllib.loads(data)
      for category in data:
        for item in data.get(category):
          path = data.get(category).get(item)
          if type(path) == str:
            data[category][item] = path.replace(os.sep, '/')
      return data
    except:
      print(f"Encountered error reading '{config_file}'")
      print(f"Contents of '{config_file}':")
      print(data)
      return None

  # Reads ini file and returns its contents in the form of a dict
  def read_ini(self, ini_file: str, inline_comments=False):
    if drawer.is_file(ini_file) is False:
      return None
    ini_file = os.path.normpath(ini_file)
    if inline_comments is True:
      parser = configparser.ConfigParser(inline_comment_prefixes=('#', ';'))
    else:
      parser = configparser.ConfigParser()
    try:
      parser.read(ini_file)
    except configparser.ParsingError:
      return None
    sections = parser.sections()
    data = {}
    for section in sections:
      keys = {}
      for key in parser[section]:
        value = parser[section][key]
        keys[key] = value
      data[section] = keys
    return data

  def write_ini(self, ini_file: str, contents: dict):
    if drawer.is_file(ini_file) is False:
      return None
    ini_file = os.path.normpath(ini_file)
    parser = configparser.ConfigParser()
    for section in contents:
      for var_name in contents.get(section):
        value = contents.get(section).get(var_name)
        if (section in parser) == False:
          parser[section] = {}
        parser[section][var_name] = value
    with open(ini_file, 'w') as file:
      parser.write(file)
