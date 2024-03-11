from talon import Context, actions, settings

ctx = Context()

ctx.matches = r"""
code.language: stata
"""

ctx.lists["user.code_parameter_name"] = {
    # regressions
    "v c e robust": "vce(robust)",
    "v c e cluster": "vce(cluster)",
}

@ctx.action_class("user")
class UserActions:
    def code_block():
        actions.auto_insert("\n")

    # 
    def code_state_if():
        actions.insert("if  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:2")

    def code_state_else_if():
        actions.insert("else if  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:7")

    def code_state_else():
        actions.insert("else  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:4")  

    def code_state_do():
        actions.insert("do {")
        actions.key("enter tab enter left")
        actions.insert("} while ()")
        actions.key("up tab")

    def code_state_for():    
        actions.insert("for () {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:4")

    def code_state_for_each():
        actions.insert("foreach  in {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:7")

    def code_break():
        actions.insert("break")

    def code_next():
        actions.insert("continue")        

    def code_comment_line_prefix():
       actions.auto_insert("* ") 
       # actions.auto_insert("// ") 

    # functions.py
    def code_private_function(text: str):
        result = "program {} \n\nend".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.up()
        actions.key("tab")

    def code_default_function(text: str):
        actions.user.code_private_function(text)

    def code_insert_named_argument(parameter_name: str):
        actions.insert(f"{parameter_name} ")




