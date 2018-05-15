# 📃 ListOpenFiles

⚡ List open files in awesome Sublime Text

😊 The super-handy shortcut <kbd>control+p</kbd> or <kbd>command+p</kbd> shows the list of all the visible files (if not in `file_exclude_patterns` in .sublime-project) to choose from and go to is used by almost all Sublime Text users.

🙄 This handy shortcut is somewhat cumbersome in one case. Switching to an already editing file is somewhat overkill when using this command as it lists almost all the files in your project. This behavior annoys me and may certainly annoy you.

😌 Thus to get you relieved, here is a brand new plugin which with a simple keystroke <kbd>alt+p</kbd> or <kbd>option+p</kbd> lists only the files you are currently editing. It makes you keep your attention on what you are editing and not on what you should choose to edit.

### ⚙ Setting:
`"show_untitled_files"`:

This setting will toggle the inclusion of untitled files in the open files list.

Default value: false

Possible values:

- true: Include the untitled files.
- false: Do not include the untitled files.

### 🧠 Remember:

When `show_untitled_files` is set to `false`, and you are invoking the command from an `untitled` file, the list will appear highlighting the next file in the stack.
