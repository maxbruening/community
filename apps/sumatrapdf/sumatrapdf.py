from talon import Context, Module, actions

# --- App definition ---
mod = Module()
mod.apps.sumatrapdf = """
os: windows
and app.name: SumatraPDF
os: windows
and app.exe: /^sumatrapdf\.exe$/i
"""

# Context matching
ctx = Context()
ctx.matches = """
app: sumatrapdf
"""


# --- Implement actions ---
@ctx.action_class("app")
class app_actions:
    # app.tabs
    def tab_open():
        actions.key("ctrl-o")


@ctx.action_class("edit")
class EditActions:
    def zoom_in():
        actions.key("+")

    def zoom_out():
        actions.key("-")


@ctx.action_class("user")
class UserActions:
    # find
    def find(text: str = None):
        if text:
            actions.edit.find(text)
        else:
            actions.edit.copy()
            actions.edit.find("")
            actions.edit.paste()

    def find_next():    
        actions.key("f3")   

    def find_previous():
        actions.key("shift-f3")

    # user.pages
    def page_current():
        actions.key("ctrl-g")
        page = actions.edit.selected_text()
        actions.key("escape")
        return int(page)

    def page_next():
        actions.key("n")

    def page_previous():
        actions.key("p")

    def page_jump(number: int):
        actions.key("ctrl-g")
        actions.insert(str(number))
        actions.key("enter")

    def page_final():
        actions.key("end")

    def page_rotate_right():
        actions.key("shift-ctrl-keypad_plus")

    def page_rotate_left():
        actions.key("shift-ctrl-keypad_minus")

    def page_go_back():
        actions.key("alt-left")

    def page_go_forward():
        actions.key("alt-right")

    # user.tabs
    def tab_jump(number: int):
        if number < 9:
            actions.key(f"alt-{number}")

    def tab_final():
        actions.key("alt-9")
