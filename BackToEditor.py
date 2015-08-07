import sublime_plugin


class BackToEditor(sublime_plugin.WindowCommand):
    def run(self):
        group, idx = self.window.get_view_index(self.window.active_view())
        self.window.focus_group(group)
