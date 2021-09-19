from sublime import load_settings
from sublime import save_settings
from sublime import status_message
import sublime_plugin

class ToggleVimCommand(sublime_plugin.WindowCommand):
  def run(self):
    settings = load_settings('Preferences.sublime-settings')
    use_ctrl_keys_setting = not settings.get('vintageous_use_ctrl_keys')
    settings.set('vintageous_use_ctrl_keys', use_ctrl_keys_setting)
    save_settings('Preferences.sublime-settings')
    if (use_ctrl_keys_setting):
      status_message('VIM MODE')
    else:
      status_message('SUBLIME MODE')
