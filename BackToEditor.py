import sublime_plugin

class BackToEditor(sublime_plugin.WindowCommand):
    def run(self):
        self.window.focus_group(self.window.active_group())
