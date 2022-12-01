try:
    from browser import document, console, window
except:
    pass

jq = window.jQuery

config = {
    "button_setting": [
        {
            "type" : "tool_detail_button",
            "div_class_name" : "tool-detail-item-wrapper",
            "button_class_name" : "tool-detail-button",
            "onclick_bg_toggle" : False,
            "selected_class_name" : ""
        },
        {
            "type" : "tool_bar_button",
            "div_class_name" : "tool-bar-item-wrapper",
            "button_class_name" : "tool-bar-button",
            "onclick_bg_toggle" : True,
            "selected_class_name" : "tool-bar-button-selected"
        },
        {
            "type" : "nav_bar_button",
            "div_class_name" : "nav-bar-item-wrapper",
            "button_class_name" : "nav-bar-button",
            "onclick_bg_toggle" : True,
            "selected_class_name" : "nav-bar-button-selected"
        }
    ]
}

def renderBtn(type:str=None, label:str=None):
    try:
        button_setting_list = config['button_setting']
        for button_setting_obj in button_setting_list:
            if button_setting_obj['type'].strip().lower() == type.strip().lower():
                return f"<div class=\"{button_setting_obj['div_class_name']}\"><button class=\"{button_setting_obj['button_class_name']}\">{label}</button></div>"
    except Exception as e:
        console.log(f"Error in renderBtn function: {e}")

def binder_button_onclicks():
    def button_onclick(e):
        try:
            button_setting_list = config['button_setting']
            for button_setting_obj in button_setting_list:
                print("button_onclick:", button_setting_obj)
                print("e:", e.target.className)
                if button_setting_obj['button_class_name'].strip().lower() in e.target.className.strip().lower() and button_setting_obj['onclick_bg_toggle']:
                    jq(e.target).addClass(button_setting_obj['selected_class_name'])
        except Exception as e:
            print(f"Error in binder_button_onclicks: {e}")
        pass

    jq('.tool-detail-button').on('click', button_onclick)
    jq('.tool-bar-button').on('click', button_onclick)
    jq('.nav-bar-button').on('click', button_onclick)


possible_button_types = [
    {
        "type" : "tool_detail_button",
        "label" : "Instagram"
    },
    {
        "type" : "tool_bar_button",
        "label" : "App"
    },
    {
        "type" : "nav_bar_button",
        "label" : "App"
    }
]

for input_obj in possible_button_types:
    jq('.button').append(renderBtn(type=input_obj['type'], label=input_obj['label']))
binder_button_onclicks()