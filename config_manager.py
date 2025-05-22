# Jam imports
from libjam import Drawer, Clipboard, Notebook
# Jamming
drawer = Drawer()
clipboard = Clipboard()
notebook = Notebook()

# Manages configs for Assetto Corsa
class ConfigManager:
  def __init__(self, config):
    cfg_dir = config.get('paths').get('CFG_DIR')
    self.cfg_dir = f"{cfg_dir}/cfg"
    defaults_cfg_dir = config.get('paths').get('AC_DIR')
    self.defaults_cfg_dir = f"{defaults_cfg_dir}/cfg"

  def to_relative_path(self, path: str):
    path = path.removeprefix(self.defaults_cfg_dir)
    path = path.removeprefix(self.cfg_dir)
    path = path.removesuffix('.ini')
    return path

  def to_absolute_path(self, path: str):
    path = self.cfg_dir + path
    path = path + '.ini'
    return path

  def config_to_list(self, config: dict):
    contents = {}
    for section in config:
      for item in config.get(section):
        value = config.get(section).get(item)
        contents[f"/{section}/{item}"] = value
    return contents

  def list_to_config(self, config: dict):
    contents = {}
    for item in config:
      var_name = drawer.basename(item)
      section = item.removesuffix(f'/{var_name}').removeprefix('/')
      value = config.get(item)
      if (section in contents) == False:
        contents[section] = {}
      contents[section][var_name] = value
    return contents

  def get_configs(self, defaults = False):
    if defaults is True:
      files = drawer.get_files_recursive(self.defaults_cfg_dir)
    else:
      files = drawer.get_files_recursive(self.cfg_dir)
    ini_files = clipboard.match_suffix(files, '.ini')
    configs = {}
    for ini_file in ini_files:
      config = notebook.read_ini(ini_file, inline_comments=True)
      if config is None:
        continue
      contents = self.config_to_list(config)
      configs[self.to_relative_path(ini_file)] = contents
    return configs

  def write_config(self, path_to_config, contents):
    path_to_config = self.to_absolute_path(path_to_config)
    contents = self.list_to_config(contents)
    notebook.write_ini(path_to_config, contents)
