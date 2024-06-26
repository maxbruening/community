from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: stata
code.language: stata
win.title: /^Do-file Editor/
"""


@ctx.action_class("user")
class UserActions:
    def code_run_selection():
        actions.key("ctrl-d")

    def code_run_line_start():
        print(
            "This action cannot be implemented in stata's do-file editor because it automatically selects the whole line."
        )

    def code_run_line_end():
        print(
            "This action cannot be implemented in stata's do-file editor because it automatically selects the whole line."
        )

    def code_run_line():
        actions.edit.select_line()
        actions.key("ctrl-d")

    def code_run_file():
        actions.edit.select_all()
        actions.edit.copy()
        actions.key("ctrl-d")

    def code_run_file_start():
        actions.edit.extend_file_start()
        actions.edit.copy()
        actions.key("ctrl-d")

    def code_run_file_end():
        actions.edit.extend_file_end()
        actions.edit.copy()
        actions.key("ctrl-d")
