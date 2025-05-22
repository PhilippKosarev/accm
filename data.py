# Imports
from libjam import Drawer

drawer = Drawer()

HOME = drawer.get_home()

# Stores variables
class Data:

  def __init__(self):
    # Paths
    ## Likely AC_DIR locations
    self.ac_path_suffix = "Steam/steamapps/common/assettocorsa"
    self.likely_ac_dirs = [f"{HOME}/.local/share/{self.ac_path_suffix}",
    f"{HOME}/.var/app/com.valvesoftware.Steam/data/{self.ac_path_suffix}",
    f"C:/Program Files (x86)/{self.ac_path_suffix}"]

    self.cfg_path_suffix = "Documents/Assetto Corsa"
    self.cfg_compatdata = "Steam/steamapps/compatdata/244210/pfx/drive_c/users/steamuser"
    self.likely_cfg_dirs = [f"{HOME}/.local/share/{self.cfg_compatdata}/{self.cfg_path_suffix}",
    f"{HOME}/.var/app/com.valvesoftware.Steam/data/{self.cfg_compatdata}/{self.cfg_path_suffix}",
    f"{HOME}{self.cfg_path_suffix}"]

  def get(self, item: str):
    return eval(f"self.{item}")
