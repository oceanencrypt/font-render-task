try:
    from browser import document, console, window
    import default_font_family as constants
except:
    pass

jq = window.jQuery

config = {
    "button_setting": [
        {
            "type" : "tool-detail-button non-italic",
            "div_class_name" : "tool-detail-item-wrapper",
            "button_class_name" : "tool-detail-button non-italic",
            "onclick_bg_toggle" : False,
            "selected_class_name" : ""
        },
        {
            "type" : "tool-detail-button",
            "div_class_name" : "tool-detail-item-wrapper",
            "button_class_name" : "tool-detail-button",
            "onclick_bg_toggle" : True,
            "selected_class_name" : "tool-bar-button-selected"
        },
    ],
    "global_font_setting":{
        "type" : "tool-detail-button",
        "label" : "Choose an appropriate Font Pair",
        "global_font_setting_state" : [
            {
                "label" : "Font Family",
                "class" : "tool-detail-button non-italic",
                "type" : "tool-detail-button",
                "select" : {
                    "type" : "select_option",
                    "class" : "global-font-family-except-headings",
                    "id" : "global-font-family-except-headings-id",
                    "options" : constants.DEFAULT_FONT_FAMILY,
                },
                "help_text" : "for all text except headings"
            },
            {
                "label" : "Font Family",
                "class" : "tool-detail-button non-italic",
                "type" : "tool-detail-button",
                "select" : {
                    "type" : "select_option",
                    "class" : "global-font-family-only-headings",
                    "id" : "global-font-family-only-headings-id",
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
            options += f'<options value="{font}">{font}</options>\n'
        return f"""
                <select class=\"{data["class"]}\" id=\"{data["id"]}\">
                        {options}
                </select>
            """
    except Exception as e:
        console.log(f"Error in renderSelect function: {e}")

def renderBtn(type:str=None, label:str=None):
    try:
        button_setting_list = config["button_setting"]
        for button_setting_obj in button_setting_list:
            if button_setting_obj['type'].strip().lower() == type.strip().lower():
                return f"<div class=\"{button_setting_obj['div_class_name']}\"><button class=\"{button_setting_obj['button_class_name']}\">{label}</button></div>"
    except Exception as e:
        console.log(f"Error in renderBtn function: {e}")

def renderExceptHeading(data:dict=None):
    try:
        btn = renderBtn(data['type'], data['label'],)
        return f"""
                <div class="global-font-family-except-headings-wrapper">' 
                    {btn}
                    <div class="global-font-family-except-headings-selection-wrapper">
                        {renderSelect(data["select"])}
                    </div>
                    <p class="help-text">{data['help_text']}</p>
                '</div>'
               """
    except Exception as e:
        console.log(f"Error in renderExceptHeading function: {e}")


def renderOnlyHeading(data:dict=None):
    try:
        btn = renderBtn(data['type'], data['label'],)
        return f"""
                <div class="global-font-family-except-headings-wrapper">' 
                    {btn}
                    <div class="global-font-family-except-headings-selection-wrapper">
                        {renderSelect(data["select"])}
                    </div>
                    <p class="help-text">{data['help_text']}</p>
                '</div>'
               """
    except Exception as e:
        console.log(f"Error in renderOnlyHeading function: {e}")

def renderGlobalFontPair():
    try:
        global_font_setting = config['global_font_setting']
        btn = renderBtn(global_font_setting['type'], global_font_setting['label']) 
        return '<div class="global-font-pair">' + btn + renderExceptHeading(global_font_setting['global_font_setting_state'][0]) + renderOnlyHeading(global_font_setting['global_font_setting_state'][1]) + '</div>'
    except Exception as e:
        console.log(f"Error in renderGlobalFontPair function: {e}")

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
            console.log(f"Error in binder_button_onclicks: {e}")
        pass

    jq('.tool-detail-button').on('click', button_onclick)
jq('.button').append(renderGlobalFontPair())
binder_button_onclicks()