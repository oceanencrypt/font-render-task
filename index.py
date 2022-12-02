try:
    from browser import document, ajax, console, window
    from index_data import DATA
    import default_font_family as constants
except:
    pass
jq = window.jQuery

# url = "https://check.free.beeceptor.com/" #pass url here

# def on_complete(req):
#     import json
#     data = json.loads(req.responseText)
#     console.log(data)

config = {
    "button_setting": [
        {
            "type" : "tool_detail_button",
            "div_class_name" : "tool-detail-item-wrapper",
            "button_class_name" : "tool-detail-button",
            "onclick_bg_toggle" : True,
            "selected_class_name" : "tool-detail-button-selected"
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
        },
        {
            "type" : "tool_detail_disabled_button",
            "div_class_name" : "tool-detail-disabled-item-wrapper",
            "button_class_name" : "tool-detail-disabled-button",
            "onclick_bg_toggle" : False,
            "selected_class_name" : ""
        },
    ],
    "global_font_setting":{
        "type" : "tool-detail-button",
        "label" : "Choose an appropriate Font Pair",
        "global_font_setting_state" : [
            {
                "label" : "Font Family",
                "div_class_name" : "font-family-item-wrapper",
                "button_class_name" : "font-family-button ",
                "type" : "font_family_detail_button",
                "select" : {
                    "type" : "select_option",
                    "select_class" : "selected-font-family",
                    "option_class" : "selected-font-family-name",
                    "id" : "selected-font-family-id",
                    "options" : constants.DEFAULT_FONT_FAMILY,
                },
                "help_text" : "for all text except headings"
            },
            {
                "label" : "Font Family",
                "div_class_name" : "font-family-item-wrapper",
                "button_class_name" : "font-family-button",
                "type" : "font_family_detail_button",
                "select" : {
                    "type" : "select_option",
                    "select_class" : "selected-font-family",
                    "option_class" : "selected-font-family-name",
                    "id" : "selected-font-family-id",
                    "options" : constants.DEFAULT_FONT_FAMILY
                },
                "help_text" : "for all headings"
            }
        ]
    }
}

def renderSelect(data:dict=None):
    try:
        options = ''
        for font in data["options"]["font_family"]:
            options += f'<option class=\"{data["option_class"]}\" value="{font}">{font}</option>\n'
        return f"""
                <select class=\"{data["select_class"]}\" id=\"{data["id"]}\">
                        {options}
                </select>
            """
    except Exception as e:
        console.log(f"Error in renderSelect function: {e}")

def renderBtn(type:str=None, label:str=None, data:dict=config['button_setting']):
    try:
        button_setting_list = data
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

    
def renderer():
    data = DATA
    for i in data["functions"]:
        jq("#main-functionalities").append(renderBtn('tool_bar_button', i))
    for i in data["AI-reply"]:
        jq("#code-structure-type").append(renderBtn('tool_detail_button', i))
    for i in data["screens"]:
        jq("#screens").append(renderBtn('nav_bar_button', i))
    for i in data["image-src"]:
        if i == "setting":
            continue
        jq("#top-icons").append(f'<img class="icon-style"src={data["image-src"][i]}>')
    jq("#select-font").prepend(renderBtn('tool_detail_disabled_button', config["global_font_setting"]['label']))
    for font in config["global_font_setting"]["global_font_setting_state"]:
        jq("#select-font").append(
            f"""
                <div class="font-family-box">
                        {renderBtn(font["type"], font["label"], config["global_font_setting"]["global_font_setting_state"])}{renderSelect(font["select"])}
                    <h6 class="font-info">{font["help_text"]}</h6>
                </div>
            """
        )
    jq("#select-pallete-heading-text").append(data["pallete-heading"])
    for idx, i in enumerate(data["pallete"]):
            html = f"<button class='font-family-btn'><h5 class='font-family-btn-text'>{i}</h5></button>"
            jq(f'#pallete-{idx}').prepend(html)
    jq("#main-bottom-div").append(f' <iframe class="link-player" src={data["iframe"]} alt="W3Schools.com"></iframe>')
    jq("#first-intro").append(data["cerebro"])
    jq("#main-icons").append(f'<img class="setting-icon"src={data["image-src"]["setting"]}>')
renderer()
binder_button_onclicks()