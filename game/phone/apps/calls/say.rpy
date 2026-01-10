screen phone_say(who, what):
    style_prefix "phone_say"

    hbox:
        null width ((config.screen_width * gui.phone_call_xpos) + (gui.phone_xsize * gui.phone_zoom))

        frame:
            if who is not None:
                window style "phone_say_namebox":
                    text who id "who"

            window:
                text what id "what"


style phone_say_frame is empty:
    xfill True yfill True
    padding (12, 15)
    background recolorize("gui/nvl.png", "#fff", "#4d4a46", 1)

style phone_say_namebox is empty:
    yanchor 1.0 ypos 0.451
    xsize 200 xalign 0.5

style phone_say_window is empty:
    ypos 0.471 xalign 0.5
    xsize 600

style phone_say_dialogue is empty:
    font phone.config.basedir + "fonts/JetBrainsMono-Regular.ttf"
    color "#fff"
    outlines [(2, "#000000aa", 0, 0)]
    outline_scaling "step"
    text_align 0.5
    xalign 0.5 ypos 0.0

style phone_say_label is phone_say_dialogue:
    font phone.config.basedir + "fonts/JetBrainsMono-ExtraBold.ttf"
    size 27
