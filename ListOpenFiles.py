import sublime
import sublime_plugin
import os

# created  18-04-2018
class ListOpenFilesCommand(sublime_plugin.WindowCommand):
    def run(self, forward=True):
        self.window = sublime.active_window()

        self.sheets = []
        self.filePaths = []
        self.fileNames = []
        self.viewIds = []

        self.untitled = self.get_settings().get("show_untitled_files")

        count = 0

        if self.get_settings().get("classic_mode") == True:
            self.get_direction(forward)
            return

        for sheet in self.window.sheets():
            if sheet and sheet.view():
                name = sheet.view().file_name()
                if name != None:
                    self.sheets.append(sheet.view())
                    name = os.path.abspath(sheet.view().file_name())

                    self.fileNames.append(name.rsplit(os.sep, -1)[-1])
                    self.filePaths.append(name)
                    self.viewIds.append(sheet.view().id())
                elif name == None and self.untitled == True:
                    temp = sheet.view().name()
                    self.sheets.append(sheet.view())
                    self.fileNames.append("Untitled-{}* {}".format(count, temp))
                    self.filePaths.append("Untitled-{}{}".format(count, temp))
                    self.viewIds.append(sheet.view().id())
                    count = count + 1

        self.get_direction(forward)

        self.current = self.viewIds.index(self.window.active_sheet().view().id())
        self.window.run_command("hide_overlay")

        self.show_panel()

    def show_panel(self):
        self.window.show_quick_panel(self.fileNames, self.on_done, selected_index=self.current, on_highlight=self.on_highlighted)

    def set_timeout(self):
        sublime.set_timeout_async(lambda: self.close_panel(), 1500)

    def close_panel(self):
        self.window.run_command("hide_overlay")

    def on_done(self, index):
        if index == -1:
            index = self.current
        self.window.focus_view(self.sheets[index])

    def on_highlighted(self, index):
        self.window.focus_view(self.sheets[index])

    def get_direction(self, forward):
        if forward == True:
            self.window.run_command("next_view")
        else:
            self.window.run_command("prev_view")

    def get_settings(self):
        return sublime.load_settings('ListOpenFiles.sublime-settings')

    def get_setting(self, setting):
        return self.get_settings().get(setting)
