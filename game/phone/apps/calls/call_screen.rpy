init -100 python in phone.calls:
    from store import Text

    def _call_time(st, at):
        global _call_time_st
        _call_time_st = st # st might not be the same when loading
        return Text(time.strftime("%M:%S", time.gmtime(st)), style="phone_call_time"), 0.0

default phone.calls._call_time_st = 0.0

screen phone_call_bg(): # отдельно из-за видеозвонков
    use _phone(xpos=gui.phone_call_xpos, xanchor=0.0):
        add Solid("#302D29")

screen phone_call(video = False):
    frame style "empty" modal True:
        at transform:
            zoom gui.phone_zoom anchor (-0.27, -0.01)

        padding gui.phone_margin
        xysize (gui.phone_xsize, gui.phone_ysize)

        if phone.calls._current_caller is not None:
            if video:
                use _phone_video_call()
            else:
                use _phone_call()


screen _phone_call():
    style_prefix "phone_call"

    vbox:
        text phone.calls._current_caller.name
        add DynamicDisplayable(phone.calls._call_time)

    frame:
        add phone.calls._current_caller.icon at _fits(None)

    frame style "empty" xalign 0.5 ypos 0.45:
        use phone_quick_menu()

    add phone.config.basedir + "hang_up.png":
        subpixel True xysize (63, 63)
        xalign 0.5 ypos 0.8


screen phone_call_accept():
    style_prefix "phone_call"

    use _phone(xpos=gui.phone_call_xpos, xanchor=0.0):
        add Solid("#302D29")

        vbox:
            text phone.calls._current_caller.name

        frame:
            add phone.calls._current_caller.icon at _fits(None)

        imagebutton:
            idle "pick_up_call"
            xalign 0.5 ypos 0.8
            action Return()


style phone_call_vbox is empty:
    spacing 3
    ypos 0.05
    xfill True

style phone_call_text is empty:
    xalign 0.5
    text_align 0.5
    outlines [ ]
    line_spacing 0
    size 24
    font phone.config.basedir + "fonts/tahoma.ttf"
    hyperlink_functions hyperlink_functions_style("phone_call_text_hyperlink")

style phone_call_text_hyperlink is phone_call_text:
    hover_underline True

style phone_call_time is phone_call_text:
    size 16

style phone_call_frame is empty:
    background CircleDisplayable(2)
    xysize (120, 120)
    padding (int(22 * (120 / 404)), int(22 * (120 / 404)))
    ypos 0.18
    xalign 0.5

image pick_up_call:
    phone.config.basedir + "pick_up.png"
    subpixel True xysize (63, 63)
    easein 0.6 yoffset -35
    easeout 0.3 yoffset -20
    easeout 0.3 yoffset -35
    easeout 0.6 yoffset 0
    1.0
    repeat


screen _phone_video_call():
    style_prefix "phone_video_call"

    vbox:
        text "[phone.calls._current_caller.name!t]"
        add DynamicDisplayable(phone.calls._call_time)

    use phone_quick_menu_video()


style phone_video_call_vbox is phone_call_vbox:
    ypos 0.03

style phone_video_call_text is phone_call_text:
    size 27
