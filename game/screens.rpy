## screens.rpy

init offset = -1

define -2 text_outline_color = "#b59"

## Styles
################################################################################

style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(absolute(2), "#000000aa", absolute(0), absolute(0))]
    outline_scaling "step"
    line_overlap_split -7.0
    line_spacing 8

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "mod_assets/font/ChareInk-Bold.ttf"
    kerning 8
    outlines [(7, "#000", 0, 0)]
    pos (gui.text_xpos, gui.text_ypos)
    xanchor gui.text_xalign
    xsize gui.text_width
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    pos (gui.text_xpos, gui.text_ypos)
    xanchor gui.text_xalign
    xsize gui.text_width
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size


style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    bar_vertical False
    base_bar Frame("mod_assets/elements/mod_gui/sliders/vertical_bar.png", tile=False)
    thumb Frame("mod_assets/elements/mod_gui/sliders/vertical_thumb.png", left=6, tile=False)
    left_gutter 23 right_gutter 23
    thumb_offset 22.5
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("mod_assets/elements/mod_gui/sliders/vertical_bar.png", tile=False)
    thumb Frame("mod_assets/elements/mod_gui/sliders/vertical_thumb.png", left=6, tile=False)
    left_gutter 22 right_gutter 22
    thumb_offset 22.5
    unscrollable "hide"
    bar_invert True

style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"


image bar_sayori:
    "mod_assets/elements/mod_gui/sliders/bar_sayori.png"
    size (110, 45)

image thumb_sayori_idle:
    "mod_assets/elements/mod_gui/sliders/thumb_sayori_idle.png"
    size (45, 42)

image thumb_sayori_hover:
    "mod_assets/elements/mod_gui/sliders/thumb_sayori_hover.png"
    size (45, 42)

style slider_sayori:
    maximum (349, 40)
    left_gutter 22 right_gutter 22
    base_bar Frame("bar_sayori", 25)
    idle_thumb "thumb_sayori_idle"
    hover_thumb "thumb_sayori_hover"
    thumb_offset 22.5


image bar_natsuki:
    "mod_assets/elements/mod_gui/sliders/bar_natsuki.png"
    size (110, 45)

image thumb_natsuki_idle:
    "mod_assets/elements/mod_gui/sliders/thumb_natsuki_idle.png"
    size (50, 42)

image thumb_natsuki_hover:
    "mod_assets/elements/mod_gui/sliders/thumb_natsuki_hover.png"
    size (50, 42)

style slider_natsuki:
    maximum (349, 40)
    left_gutter 40 right_gutter 35
    base_bar Frame("bar_natsuki", 25)
    idle_thumb "thumb_natsuki_idle"
    hover_thumb "thumb_natsuki_hover"
    thumb_offset 40


image bar_yuri:
    "mod_assets/elements/mod_gui/sliders/bar_yuri.png"
    size (110, 45)

image thumb_yuri_idle:
    "mod_assets/elements/mod_gui/sliders/thumb_yuri_idle.png"
    size (45, 55)

image thumb_yuri_hover:
    "mod_assets/elements/mod_gui/sliders/thumb_yuri_hover.png"
    size (45, 55)

style slider_yuri:
    maximum (349, 45)
    left_gutter 22 right_gutter 22
    base_bar Frame("bar_yuri", 25)
    idle_thumb "thumb_yuri_idle"
    hover_thumb "thumb_yuri_hover"
    thumb_offset 22.5


image bar_monika:
    "mod_assets/elements/mod_gui/sliders/bar_monika.png"
    size (110, 45)

image thumb_monika_idle:
    "mod_assets/elements/mod_gui/sliders/thumb_monika_idle.png"
    size (58, 53)

image thumb_monika_hover:
    "mod_assets/elements/mod_gui/sliders/thumb_monika_hover.png"
    size (58, 53)

style slider_monika:
    maximum (349, 45)
    left_gutter 40 right_gutter 27
    base_bar Frame("bar_monika", 25)
    idle_thumb "thumb_monika_idle"
    hover_thumb "thumb_monika_hover"
    thumb_offset 40


image bar_monikammm:
    "mod_assets/elements/mod_gui/sliders/bar_monikammm.png"
    size (110, 45)

image thumb_monikammm:
    "mod_assets/elements/mod_gui/sliders/thumb_monikammm.png"
    size (58, 53)

style slider_monikammm:
    maximum (349, 45)
    left_gutter 40 right_gutter 27
    base_bar Frame("bar_monikammm", 25)
    thumb "thumb_monikammm"
    thumb_offset 40


style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################

screen say(who, what):
    style_prefix "say"

    window:

        id "window"

        text what id "what"

        if who is not None:

            window:

                style "namebox"

                text who id "who"

    add SideImage() align (0.0, 1.0)

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    align (0.5, gui.textbox_yalign)
    xfill True
    ysize gui.textbox_height
    background Transform("mod_assets/elements/dialog/textboxes/[pov_key].png", xalign=0.5, yalign=1.0)

style namebox:
    pos (gui.name_xpos, gui.name_ypos)
    xanchor gui.name_xalign
    xysize (gui.namebox_width, gui.namebox_height)
    padding gui.namebox_borders.padding
    background Frame("mod_assets/elements/dialog/nameboxes/[pov_key].png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    align (gui.name_xalign, 0.5)

style say_dialogue:
    pos (gui.text_xpos, gui.text_ypos)
    xanchor gui.text_xalign
    xsize gui.text_width
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    subpixel True align (0.81, 0.98) xoffset -5 alpha 0.0
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat


## Input screen ################################################################

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xpos gui.text_xpos
            ypos gui.text_ypos
            xanchor 0.5

            text prompt style "input_prompt"
            input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5


## Choice screen ###############################################################
##
##      Examples: "Option 1 (kwargs=#00fbff)" | "Option 2 (kwargs=#00fbff, #6cffff)"
##      Обводка + внутренняя область
##
##      ГГ: (kwargs=#707070, #cfcfcf)
##      Сайори: (kwargs=#00e2e5, #a8ffff)

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            if "kwargs=" in i.caption:
                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    $ kwarg = kwarg.replace(", ", ",").split(",")

                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')

                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]

                    textbutton caption:
                        idle_background Frame(
                            im.MatrixColor(
                                im.MatrixColor(
                                    "gui/button/choice_idle_background.png", 
                                    im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)
                                ),
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)
                            ), 
                            gui.choice_button_borders
                        )
                        hover_background Frame(
                            im.MatrixColor(
                                im.MatrixColor("gui/button/choice_hover_background.png",
                                im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)
                                ),
                                im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)
                            ), 
                            gui.choice_button_borders
                        )
                        action i.action

                else:
                    textbutton caption:
                        style kwarg
                        action i.action

            else:
                textbutton i.caption action i.action


# true - menu captions will be spoken by the narrator; false - menu captions will be displayed as empty buttons
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "gui/sfx/hover.ogg"
    activate_sound "gui/sfx/select.ogg"
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse(x=640, y=345):
        currentpos, targetpos = renpy.get_mouse_pos(), [x, y]
        if currentpos[1] != targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
        return None

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Quick Menu screen ###########################################################

screen quick_menu():
    style_prefix "quick"

    zorder 100

    hbox:
        align (0.5, 1.0)
        spacing 20

        imagebutton:
            if quick_menu:
                idle "history_idle"
                hover "history_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "history_close"
            action If(quick_menu, ShowMenu('history'), NullAction())

        imagebutton:
            if quick_menu:
                idle "skip_idle"
                hover "skip_hover"
                selected_idle "skip_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "skip_close"
            action If(quick_menu, Skip(), NullAction()) alternate If(quick_menu, Skip(fast=True, confirm=True), NullAction())

        imagebutton:
            if quick_menu:
                idle "afm_idle"
                hover "afm_hover"
                selected_idle "afm_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "afm_close"
            action If(quick_menu, Preference("auto-forward", "toggle"), NullAction())

        imagebutton:
            if quick_menu:
                idle "save_idle"
                hover "save_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "save_close"
            action If(quick_menu, ShowMenu('save'), NullAction())

        imagebutton:
            if quick_menu:
                idle "load_idle"
                hover "load_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "load_close"
            action If(quick_menu, ShowMenu('load'), NullAction())

        imagebutton:
            if quick_menu:
                idle "preferences_idle"
                hover "preferences_hover"
                hover_sound gui.hover_sound
                activate_sound gui.activate_sound
            else:
                idle "preferences_close"
            action If(quick_menu, ShowMenu('preferences'), NullAction())

image history_idle:
    "mod_assets/elements/dialog/signs/quick/history_idle.png"
    size (47, 47)
image history_hover:
    "mod_assets/elements/dialog/signs/quick/history_hover.png"
    size (47, 47)
image history_close:
    "mod_assets/elements/dialog/signs/quick/history_close.png"
    size (47, 47)

image skip_idle:
    "mod_assets/elements/dialog/signs/quick/skip_idle.png"
    size (47, 47)
image skip_hover:
    "mod_assets/elements/dialog/signs/quick/skip_hover.png"
    size (47, 47)
image skip_close:
    "mod_assets/elements/dialog/signs/quick/skip_close.png"
    size (47, 47)

image afm_idle:
    "mod_assets/elements/dialog/signs/quick/afm_idle.png"
    size (47, 47)
image afm_hover:
    "mod_assets/elements/dialog/signs/quick/afm_hover.png"
    size (47, 47)
image afm_close:
    "mod_assets/elements/dialog/signs/quick/afm_close.png"
    size (47, 47)

image save_idle:
    "mod_assets/elements/dialog/signs/quick/save_idle.png"
    size (47, 47)
image save_hover:
    "mod_assets/elements/dialog/signs/quick/save_hover.png"
    size (47, 47)
image save_close:
    "mod_assets/elements/dialog/signs/quick/save_close.png"
    size (47, 47)

image load_idle:
    "mod_assets/elements/dialog/signs/quick/load_idle.png"
    size (47, 47)
image load_hover:
    "mod_assets/elements/dialog/signs/quick/load_hover.png"
    size (47, 47)
image load_close:
    "mod_assets/elements/dialog/signs/quick/load_close.png"
    size (47, 47)

image preferences_idle:
    "mod_assets/elements/dialog/signs/quick/preferences_idle.png"
    size (47, 47)
image preferences_hover:
    "mod_assets/elements/dialog/signs/quick/preferences_hover.png"
    size (47, 47)
image preferences_close:
    "mod_assets/elements/dialog/signs/quick/preferences_close.png"
    size (47, 47)

default quick_menu = True


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos yalign 0.8
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Новая игра"):
                action [
                    Start(),
                    SensitiveIf(renpy.get_screen("main_menu"))
                ]
        else:
            textbutton _("История"):
                action [
                    ShowMenu("history"),
                    SensitiveIf(not renpy.get_screen("history"))
                ]

            textbutton _("Сохранения"):
                action [
                    ShowMenu("save"),
                    SensitiveIf(not renpy.get_screen("save"))
                ]

        textbutton _("Загрузки"):
            action [
                ShowMenu("load"),
                SensitiveIf(not (renpy.get_screen("load") or extra_submenu_active))
            ]

        if main_menu:
            textbutton _("Экстра"):
                action [
                    If(extra_submenu_active,
                        [
                            SetVariable("extra_submenu_active", False),
                            If(extra_submenu_music_player_active,
                                [
                                    SetVariable("extra_submenu_music_player_active", False),
                                    Stop("music_player_channel"),
                                    Play("music", audio.mod_main_menu_after_disclaimer, fadein=1.0)
                                ]
                            )
                        ]
                    ),
                    ShowMenu("extras"),
                    SensitiveIf(not renpy.get_screen("extras"))
                ]

        textbutton _("Настройки"):
            action [
                ShowMenu("preferences"),
                SensitiveIf(not (renpy.get_screen("preferences") or extra_submenu_active))
            ]

        if renpy.variant("pc"):

            textbutton _("Помощь"):
                action [
                    ShowMenu("help"),
                    SensitiveIf(not (renpy.get_screen("help") or extra_submenu_active))
                ]

            if not main_menu:
                textbutton _("Главное меню"):
                    action If(blocker,
                                Show(screen="dialog"),
                                [
                                    If(not sprite_main_menu_set,
                                        SetVariable("sprite_main_menu_set", True)
                                    ),
                                    MainMenu()
                                ]
                    )

            textbutton _("Выход"):
                action If(blocker, Show(screen="dialog"), Quit(confirm = not main_menu))


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/font/menu/Vivl-rail.ttf"
    size 22
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]


## Main Menu screen ############################################################

screen main_menu():
    tag menu

    style_prefix "main_menu"

    if persistent.secret_monikammm_active:
        add "#ffffff"

        if 5 < secret_monikammm_count < 20:
            add "monikammm forward":
                align (0.5, 0.5) zoom 0.05 * (secret_monikammm_count - 4) alpha 0.05 * (secret_monikammm_count - 4)
        elif secret_monikammm_count >= 20:
            add "art_secret_monikammm_full_switch"

    else:
        add "menu_bg"

        if random_menu == 3:
            add "images/cg/monika/monika_bg.png" # Just Monika
        else:
            frame

        if not sprite_main_menu_set:
            add "menu_logo_animated"
        else:
            add "menu_logo"


        if random_menu == 3:
            button:
                area(623, 240, 17, 21)
                action [Play("sound", gui.activate_sound), Jump("secret_monika_script")]

        else:
            for i in sprite_main_menu[random_menu]:
                if not sprite_main_menu_set:
                    add i[0]:
                        xcenter i[1] ycenter i[2] zoom i[3]
                        at menu_sprite_move_first_show(i[3], i[4])
                else:
                    add i[0]:
                        xcenter i[1] ycenter i[2] zoom i[3]
                        at menu_sprite_move

        vbox:
            text "ver. [config.version]":
                style "main_menu_text"

    use navigation

    add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text

style main_menu_frame:
    xsize 310
    yfill True
    background "menu_nav"

style main_menu_vbox:
    align (1.0, 0.05)
    xoffset -20 yoffset -20
    xmaximum 800

style main_menu_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    size gui.title_text_size
    color gui.accent_color
    outlines [(4, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    text_align 1.0 xalign 1.0
    layout "subtitle"


## Game Menu screen ############################################################

screen game_menu(title, scroll=None):
    style_prefix "game_menu"

    if main_menu:
        if persistent.secret_monikammm_active:
            add "#ffffff"
            if secret_monikammm_count >= persistent.secret_monikammm_count_all_menus_limit:
                add "art_secret_monikammm_full_switch"
        else:
            add gui.main_menu_background
    else:
        if nightmare_active:
            add "#ff616188"
        else:
            add "#ffe8f8d7"

        key "game_menu" action Return()

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame: # reserve space for the navigation section
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"

                        if title == "История":
                            yinitial 1.0
                        else:
                            yinitial 0

                        mousewheel True
                        arrowkeys True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        scrollbars "vertical"

                        cols 1

                        if title == "История":
                            yinitial 1.0
                        else:
                            yinitial 0

                        mousewheel True
                        arrowkeys True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Назад"):
        style "return_button"
        action [
            If(main_menu,
                If(persistent.secret_monikammm_active,
                    [
                        SetVariable("secret_monikammm_count", secret_monikammm_count + 1),

                        If(secret_monikammm_count == persistent.secret_monikammm_count_screamer_limit,
                            Jump("secret_monikammm_script")
                        )
                    ],
                        If(sprite_main_menu_set == False,
                            SetVariable("sprite_main_menu_set", True)
                        )
                )
            ),
            Return(),
            SensitiveIf(not extra_submenu_active)
        ]

    label title


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "game_menu_image"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    pos (30, 30)

style game_menu_label_text:
    size 27
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

image game_menu_image:
    "mod_assets/elements/mod_gui/menu/game_menu.png" # "gui/overlay/game_menu.png"
    size (1280, 720)


## Load and Save screens #######################################################

screen save():
    tag menu
    use file_slots(_("Сохранения"))

screen load():
    tag menu
    use file_slots(_("Загрузки"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Страница {}"), auto=_("Автосохранения"))

    use game_menu(title):

        fixed:
            order_reverse True # ensures the input will get the enter event before any of the buttons do

            button:
                style "page_label"

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                align (0.5, 0.5)
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1

                    button:
                        action If(blocker, Show(screen="dialog"), FileAction(slot))

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        null height 5

                        text FileSaveName(slot, empty=_("Пустой слот")):
                            style "slot_button_text"

                        null height -3

                        # %B - месяц буквами, %a - только 3 буквы дня недели, %A - день недели целиком
                        text FileTime(slot, format="{#file_time}%H:%M %d/%m/%Y"):
                            style "slot_button_text"

                        key "save_delete" action [Play("sound", gui.activate_sound), FileDelete(slot)]

            hbox:
                style_prefix "page"

                align (0.5, 1.0)
                spacing gui.page_spacing

                textbutton "{#auto_save}A" action FilePage("auto")

                for page in range(1, 4):
                    textbutton "[page]":
                        action FilePage(page)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text
style slot_button is gui_button
style slot_button_text is gui_button_text

style page_label:
    xalign 0.5
    padding (50, 3)

style page_label_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    outlines [(4, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    text_align 0.5
    layout "subtitle"

style page_button:
    properties gui.button_properties("page_button")
    activate_sound gui.activate_sound

style page_button_text:
    properties gui.button_text_properties("page_button")
    font "mod_assets/font/menu/TickingTimebombBb.ttf"
    size 50
    color "#fff"
    hover_color "#f9d"
    selected_color "#f9d"
    outlines [(2, text_outline_color, 0, 0)]

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)
    activate_sound gui.activate_sound

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    font "mod_assets/font/menu/Vivl-rail.ttf"
    size 13
    color "#7f7f7f"
    outlines []


## Preferences screen ##########################################################

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            style_prefix "pref"
            xoffset 50

            label _("Основные настройки") xalign 0.4

            null height (4 * gui.pref_spacing) + 5

            hbox:
                style_prefix "main_check"
                box_wrap True
                xalign 0.3
                spacing 110

                vbox:
                    label _("Отображение экрана")

                    null height gui.pref_spacing + 5

                    textbutton _("Оконный режим"):
                        action Preference("display", "window")

                    null height gui.pref_spacing

                    textbutton _("Полный экран"):
                        action Preference("display", "fullscreen")

                vbox:
                    label _("Разрешения пропуска текста")

                    null height gui.pref_spacing + 5

                    textbutton _("Непрочитанный"):
                        action Preference("skip", "toggle")

                    null height gui.pref_spacing

                    textbutton _("После выборов"):
                        action Preference("after choices", "toggle")

            null height (5 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Скорость вывода текста"):
                        text_outlines [(3, "#12a4e3", 0, 0), (2, "#12a4e3", 0, 0)]
                    bar value Preference("text speed") style "slider_sayori"

                    null height (2 * gui.pref_spacing)

                    label _("Время задержки авточтения"):
                        text_outlines [(3, "#a937de", 0, 0), (2, "#a937de", 0, 0)]
                    bar value Preference("auto-forward time") style "slider_yuri"

                    if secret_monikammm_chance:
                        null height (2 * gui.pref_spacing)

                        label _("Громкость голосов"):
                            text_outlines [(3, "#000", 0, 0), (2, "#000", 0, 0)]
                        bar value Preference("voice volume") style "slider_monikammm"

                vbox:
                    label _("Громкость звуков"):
                        text_outlines [(3, "#ed2d94", 0, 0), (2, "#ed2d94", 0, 0)]
                    bar value Preference("sound volume") style "slider_natsuki"

                    null height (2 * gui.pref_spacing)

                    label _("Громкость музыки"):
                        text_outlines [(3, "#22a800", 0, 0), (2, "#22a800", 0, 0)]
                    bar value Preference("music volume") style "slider_monika"

                    null height (4 * gui.pref_spacing)

                    textbutton _("Заглушить всё аудио"):
                        xalign 0.15
                        action Preference("all mute", "toggle")

            null height (10 * gui.pref_spacing)

            label _("Дополнительные настройки") xalign 0.4

            null height (3 * gui.pref_spacing) + 5

            hbox:
                style_prefix "check"
                box_wrap True

                vbox:
                    hbox:
                        label _("Цензура (для стримеров)")
                        textbutton "?":
                            style "pref_description_button"
                            action ShowMenu(
                                "extra_screen_help",
                                _("РЕЖИМ ЦЕНЗУРЫ\nРежим цензуры заменяет ТОЛЬКО мат на более нейтральные слова\n(остальные элементы: кровь, скримеры и прочее -- остаются без изменений).\nЭто может сказаться на градусе атмосферы некоторых сюжетных моментов,\nпоэтому использование данного режима рекомендуется исключительно стримерам.\nДля активации режима нажмите на кнопку \"Режим цензуры\".\nЕсли она горит зелёным цветом -- режим цензуры активирован."),
                                ok_action = Hide("extra_screen_help"),
                                chibi = "y_chibi turned magnifier",
                                chibi_pos = 12
                            )

                    null height gui.pref_spacing - 5

                    textbutton _("Режим цензуры"):
                        action ToggleVariable("persistent.censorship", True, False)

                null width 125

                vbox:
                    hbox:
                        label _("Текущее имя игрока")
                        textbutton "?":
                            style "pref_description_button"
                            action ShowMenu(
                                "extra_screen_help",
                                _("РЕДАКТИРОВАНИЕ ИМЕНИ ИГРОКА\nИмя игрока ни на что не влияет, а также оно не используется в сюжете мода,\nоднако может быть использовано за его пределами.\nЕсли вы хотите изменить своё имя, нажмите на кнопку с вашим текущем именем,\nчтобы перейти в режим редактирования.\nВсе ограничения по вводу имени отображены в окне редактирования."),
                                ok_action = Hide("extra_screen_help"),
                                chibi = "y_chibi turned magnifier",
                                chibi_pos = 30
                            )

                    null height gui.pref_spacing - 5

                    textbutton "[persistent.playername]":
                        action ShowMenu(
                            "name_input",
                            message_label = _("ОГРАНИЧЕНИЯ ВВОДА ИМЕНИ:"),
                            message_text = _("1) вне зависимости от введённого регистра первый символ имени будет заглавным,\nостальные символы -- строчные;\n2) имя должно быть в диапазоне от 2 до 12 символов русского или английского\nалфавитов (пробелы, цифры и спец. символы запрещены);\n3) в имени должны быть буквы только из одной раскладки;\n4) в имени нельзя использовать маты и слова c откровенно сексуальным и «грязным» характером (обходом данного ограничения Вы подтверждаете, что\nВам плевать на свою мораль и адекватность и что клоуничество для Вас важнее);\n5) запрещено добуквенно использовать имена персонажей мода (даже на\nанглийской раскладке) (и даже если это ваше настоящее имя);\n6) запрещено добуквенно использовать никнейм разработчика модификации\n(даже на русской раскладке)."),
                            ok_action = Hide("name_input"),
                            first_name = False
                        )


style pref_label is gui_label
style pref_label_text is gui_label_text

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text

style main_check_label is check_label
style main_check_label_text is check_label_text
style main_check_button is check_button
style main_check_button_text is check_button_text

style slider_label is pref_label
style slider_label_text is gui_button_text
style slider_button is check_button
style slider_button_text is check_button_text
style slider_slider is gui_slider

style pref_description_button is gui_button
style pref_description_button_text is gui_button_text


style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    color "#fff"
    size 35


style check_label:
    xalign 0.5

style check_label_text:
    outlines [(3, "#ff833b", 0, 0), (1, "#ff833b", 0, 0)]
    size 21

style check_button:
    properties gui.button_properties("check_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    selected_hover_sound None
    xalign 0.3

style check_button_text:
    properties gui.button_text_properties("check_button")
    idle_color "#bdbdbd"
    hover_color "#ff8b47"
    selected_color "#4aff71"
    size 18

style check_vbox:
    xalign 0.5


style main_check_label_text:
    outlines [(3, "#488ef7", 0, 0), (1, "#488ef7", 0, 0)]


style slider_slider:
    xsize 350

style slider_label_text:
    size 18
    color "fff"

style slider_vbox:
    xsize 450


style pref_description_button:
    properties gui.button_properties("check_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    xoffset -25

style pref_description_button_text:
    properties gui.button_text_properties("check_button")
    color "#fff"
    outlines [(4, "#3eb9ed", 0, 0), (2, "#3eb9ed", 2, 2)]
    hover_outlines [(4, "#91deff", 0, 0), (2, "#91deff", 2, 2)]
    insensitive_outlines [(4, "#ade7ff", 0, 0), (2, "#ade7ff", 2, 2)]
    size 18


## History screen ##############################################################

screen history():
    tag menu

    predict False # avoid predicting this screen - it can be very large

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed: # if history_height is None
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История пуста")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    pos (gui.history_name_xpos, gui.history_name_ypos)
    xanchor gui.history_name_xalign
    xsize gui.history_name_width

style history_name_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    font "mod_assets/font/menu/UZSans-Regular.ttf"
    pos (gui.history_text_xpos, gui.history_text_ypos)
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################

screen help():

    tag menu

    default device = "info"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        hbox:
            xpos 150

            textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")

            null width 15

            textbutton _("Мышь") action SetScreenVariable("device", "mouse")

            null width 15

            textbutton _("Особенности мода") action SetScreenVariable("device", "feature")


        null height 30


        vbox:
            if device == "info":
                use info_help
            elif device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "feature":
                use feature_help


screen info_help():

    hbox:
        text _("Здесь расписаны все рабочие функции горячих клавиш,\nа также технические и визуальные особенности мода.\n\nЧтобы с ними ознакомиться,\nвыберите соответствующий раздел сверху."):
            style "help_info_text"


screen keyboard_help():

    vbox:
        spacing 40

        hbox:
            label "Enter"
            text _("Альтернатива левой кнопки мыши: прожимает кнопки, если на них наведён курсор, и продвигает диалоги в игре.")

        hbox:
            label _("Пробел")
            text _("Только продвигает диалоги в игре.")

        hbox:
            label _("Клавиши со стрелками")
            text _("Выбор кнопок в меню, если на них наведён курсор, выбор кнопок интерфейса во время игры и прокрутка ползунков.")

        hbox:
            label "Esc"
            text _("Закрывает игру при нажатии в главном меню и вызывает игровое меню.")

        hbox:
            label "Ctrl"
            text _("Активирует пропуск текста при удерживании.")

        hbox:
            label "Del"
            text _("Вызывает экран подтверждения удаления сохранения, если на него наведён курсор.")

        hbox:
            label "S"
            text _("Делает скриншот при нажатии (путь к скриншоту выводится в левом верхнем углу экрана на несколько секунд).")

        hbox:
            label "F"
            text _("Меняет оконный режим отображения экрана на полноэкранный и наоборот.")

        if persistent.streamer_detected:
            hbox:
                label "H"
                text _("ДЛЯ СТРИМЕРОВ: скрывает игровой интерфейс и интерфейс телефона для создания превью и прочего.\nВАЖНО! Технически скрывается не только интерфейсы, но и все активные «экраны» (на них отображаются элементы «интерактивных» моментов сюжета с прожатием кнопок клавиатуры или областей на самом экране), поэтому пользуйтесь этой кнопкой только в моменты, когда «интерактива» нет, чтобы не испортить впечатление от прохождения (если даже использовали эту кнопку в момент «интерактива», то она его не «поломает» -- просто нажмите её повторно, чтобы вернуть отображение «экранов»). Подробнее об «интерактиве» можно узнать в разделе «Особенности мода».")

        hbox:
            label "F1"
            text _("Вызов помощи, в которой вы сейчас находитесь.")

        hbox:
            label "F11"
            text _("Альтернатива клавиши F: меняет оконный режим отображения экрана на полноэкранный и наоборот.")


        if config.developer:

            null height 20

            text "{b}Если включен режим разработчика:{/b}":
                xalign 0.5
                text_align 0.5
                size 23

            hbox:
                label "Page Up"
                text "Откат на прошлый текст сюжета (при единичном нажатии сдвигается на одну строку, при удерживании ускоряется до «пропуска»)."

            hbox:
                label "Page Down"
                text "Альтернатива обычному пропуску (при единичном нажатии сдвигается на одну строку, при удерживании ускоряется до «пропуска»)."

            hbox:
                label "Shift + R"
                text "Производит перезапуск скрипта."

            hbox:
                label "Shift + D"
                text "Открывает меню разработчика."

            hbox:
                label "Shift + O"
                text "Открывает консоль разработчика."

            hbox:
                label "Shift + i"
                text "Открывает инспектор разработчика."


screen mouse_help():

    vbox:
        spacing 40

        hbox:
            label _("Левая кнопка мыши")
            text _("Не нуждается в представлении, без неё бы вас тут не было.")

        hbox:
            label _("Правая кнопка мыши")
            text _("Открывает игровое меню и скрывает его, когда оно активно.")

        hbox:
            label _("Прокрутка колеса мыши")
            text _("Прокрутка вертикальных ползунков.")

        if config.developer:

            null height 20

            text "{b}Если включен режим разработчика:{/b}":
                xalign 0.5
                text_align 0.5
                size 23

            hbox:
                label "Прокрутка колеса мыши вверх"
                text "Альтернатива Page Up (откат на прошлый текст сюжета на столько, на сколько прокучено само колесо)."

            hbox:
                label "Прокрутка колеса мыши вниз"
                text "Альтернатива Page Down и обычному пропуску (пропускает текст сюжета на столько, на сколько прокучено само колесо)."


screen feature_help():

    vbox:
        spacing 40

        text _("{b}Технические нюансы мода:{/b}"):
            xalign 0.5
            text_align 0.5
            size 23

        hbox:
            label _("Повествование от лица не главного героя")
            text _("Во время игры за другого персонажа меняется цвет диалогового окна и курсора, однако это никак не влияет на загрузки сохранений, когда цвет был другой.")

        hbox:
            label _("Сюжетные переходы и некоторые анимации спрайтов")
            text _("Во время таких сцен игровое меню деактивировано. Это сделано для того, чтобы нельзя было сломать тайминги и, как итог, впечатление от игры.")

        hbox:
            label _("Автосохранения")
            text _("В начале каждого дня (и не только) перед первой фразов, выведенной в этом дне будет создаётся автоматическое сохранение. Загрузить их можно из специального раздела, помеченного буквой «A», в меню слотов сохранений.")

        hbox:
            label _("Пропуск текста")
            text _("Деактивируется, если по сюжету идёт переписка в мессенджере, составление и чтение стихотворения или интерактив.")

        hbox:
            label _("Интерактив")
            text _("В моде есть сюжетные моменты, где задействуется QTE либо мышь. Во время QTE обязательно будут отображены необходимые кнопки для прожатия по центру экрана и иногда шкала прогресса сверху. Если используется интерактив с мышью, то обращайте внимание на визуал её курсора, чтобы понять, с какими областями можно взаимодействовать.")

        hbox:
            label _("Использование телефона")
            text _("Использование телефона происходит исключительно по сюжету в двух вариациях:\n1) переписка в мессенджере (текст выводится и прощёлкивается так же, как и в диалоговом окне) без доступа к приложениям;\n2) просмотр телефона с доступом к приложениям.\nИнтерфейс телефона простой и интуитивно понятный, однако в первые моменты всё равно будут даны всплывающие подсказки по его использованию. Некоторые интерактивные элементы (шкалы, кнопки и т.д.) активны лишь в определённые моменты, которые будут озвучены персонажем, от лица которого ведётся повествование. Даже при «невнимательном» чтении можно быстро выявить, какой элемент стал активным, и активировать/деактивировать его для продолжения прохождения.")

        null height 20

        text _("{b}Визуальные особенности мода:{/b}"):
            xalign 0.5
            text_align 0.5
            size 23

        hbox:
            label _("Анимированный текст")
            text _("В игре используются различные анимации шрифта: изменение размера, цвета, дрожание и т.д. Они также сохраняются в истории диалогов.")

        hbox:
            label _("Цвета имён персонажей")
            text _("Все имена персонажей имеют собственные цвета. Это сделано для облегчения чтения диалогов.")

        hbox:
            label _("Цвета текста в диалоговом окне")
            text _("Основным цветом шрифта в диалоговом окне является белый, т.е. «японский», но в некоторых моментах цвет отдельных слов или фраз заменён на другой:\n1) синий -- «русский»;\n2) оранжевый -- «английский».")


style help_button is confirm_button
style help_button_text is confirm_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_info_text is help_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")
    font "mod_assets/font/menu/Vivl-rail.ttf"

style help_label:
    xsize 260
    right_padding 20

style help_label_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    color "#fff"
    outlines [(2, "#505050", 0, 0)]
    size gui.text_size
    xalign 0.5
    text_align 0.5

style help_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    color "#000"
    outlines []
    size 22
    text_align 0.0
    ypos 4

style help_info_text:
    color "#fff"
    outlines [(2, "#505050", 0, 0)]
    size 28
    text_align 0.5
    pos (95, 135)


################################################################################
## Additional screens
################################################################################

init -1 python:
    class PlayernameFilters:
        _name_character = {
            'Макс', 'Моника', 'Сайори', 'Нацуки', 'Юри', 'Котоноха', 'Коха', 'Либитина', 'Лина', 'Рэйко', 'Кохаку', 'Сора', 'Эми',
            'Фуккацуми', 'Фукка', 'Камуко', 'Хироши', 'Моникаммм', 'Гг', 'Мс', 'Харуми', 'Дэн', 'Дайсуке', 'Юко', 'Мамору', 'Тамоцу',
            'Ари', 'Мартин', 'Ида',
            'Мама', 'Папа', 'Классрук', 'Директор', 'Официант', 'Коровка', 'Птиц',
            'Max', 'Maks', 'Monika', 'Sayori', 'Natsuki', 'Yuri', 'Kotonoha', 'Koha', 'Libitina', 'Lina', 'Reiko', 'Kohaku', 'Sora', 'Emi',
            'Fukkacumi', 'Fukka', 'Kamuko', 'Hiroshi', 'Mc', 'Dan', 'Daisuke', 'Harumi', 'Yuko', 'Mamoru', 'Tamotsu', 'Ari', 'Martin', 'Ida',
            'Mother', 'Mama', 'Mom', 'Father', 'Papa', 'Dad', 'Director', 'Waiter', 'Teacher', 'Cow', 'Bird'
        }
        _name_dev = {'Китсуру', 'Кицуру', 'Кицурудев', 'Кицурудэв', 'Китсурудев', 'Китсурудэв', 'Kitsuru', 'Kitsurudev'}
        _suffixes = re.compile(r'(сан|san|кун|kun|чан|тян|chan|сама|sama|сэнсэй|сенсей|сенсэй|сэнсей|sensei)$')

        def __normalization(name):
            return name[0].upper() + name[1:].lower() if len(name) > 1 else ""

        def __mix(name):
            return True if bool(re.search('[\u0400-\u04FF]', name)) and bool(re.search('[a-zA-Z]', name)) else False

        # Если бы кто-то мне в детстве сказал, что я на серьёзных щах буду писать на Питоне функцию проверки имени игрока на всякое дерьмище,
        # я бы этому не поверил...
        def __swearing(name):
            name = name.lower()
            filepath = "name_censorship/words_swearing_"
            if bool(re.search('[a-zA-Z]', name)):
                filepath += "eng.txt"
            else:
                filepath += "rus.txt"
                name = name.replace("ё", "е")
            with renpy.file(filepath) as f:
                lines = [line.decode("utf-8").strip("\n") for line in f.readlines()] # вместо одного readlines() из-за rpa-архивов
                for i in lines:
                    if i.strip("\n") in name:
                        return True
            return False

        # По большей части я это делал, когда у меня были творческие затупы, оттого тут такое разнообразие
        def __forbidden(name):
            name = PlayernameFilters._suffixes.sub('', name)
            if name in PlayernameFilters._name_character or len(name) > 6 and name[:7] in ('Моникам', 'Monikam'):
                return 1
            if name in PlayernameFilters._name_dev:
                return 2
            return 0

        @classmethod
        def checking_first_run(cls, name):
            name = cls.__normalization(name)
            if name == "":               return 0
            if cls.__mix(name):          return 1
            if cls.__swearing(name):     return 2
            f = cls.__forbidden(name)
            if f > 0:                    return 3 if f == 1 else 4
            if name in ("Мита", "Mita"): return 5
            return name

        @classmethod
        def checking(cls, name):
            name = cls.__normalization(name)
            if name == "" or cls.__mix(name) or cls.__swearing(name) or cls.__forbidden(name):
                return False
            persistent.playername = name
            return True


screen name_input(message_label, message_text, ok_action, first_name = True):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    key "K_ESCAPE" action None

    frame:
        vbox:
            align (0.5, 0.5)

            label _(message_label):
                style "confirm_prompt"
                xalign 0.5

            null height 10

            text _(message_text):
                style "name_input_message_text"

            null height 20

            input default "[persistent.playername]" value VariableInputValue("playername_raw") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

            null height 30

            if first_name:
                textbutton _("OK"):
                    xalign 0.5
                    action If(playername_raw, ok_action, None)
            else:
                textbutton _("OK"):
                    xalign 0.5
                    action If(
                        PlayernameFilters.checking(playername_raw),
                        (ok_action, renpy.save_persistent()),
                        None
                    )


style name_input_message_text is confirm_prompt_text:
    xalign 0.5
    text_align 0.0


init python:
    # [картинка, zoom, xalign, yalign]
    blocker_image = {
        "poem": ("m_chibi turned", 1.0, 0.5, 0.185),
        "poem_before_mmm": ("mc_chibi turned", 1.0, 0.5, 0.19),
        "sayori_ghost": ("gui/menu_art_s_ghost.png", 0.455, 0.52, 0.1),
        "natsuki_ghost": ("gui/menu_art_n_ghost.png", 0.455, 0.51, 0.1),
        "yuri_ghost": ("gui/menu_art_y_ghost.png", 0.455, 0.51, 0.1)
    }

    blocker_text = {
        "poem": _("Не-не-не, у меня в голове уже пронзительное лицо Моники с улыбкой,\nполной «добра» и «позитива», я не могу сейчас вот так взять и прерваться."),
        "poem_before_mmm": _("У меня ещё есть силы, к тому же меня что-то осенило,\nя не хочу сейчас прерываться."),
        "sayori_ghost": _("Счастливые мысли! Счастливые мысли!\nСчастливые мысли!\nВ бутылочках в ряд!"),
        "natsuki_ghost": _("Ты куда делся?!\nВернись! Вернись обратно!\nНе, серьёзно. Ну вернись.\nВернись, пожалуйста..."),
        "yuri_ghost": _("Согрей меня.\nСогрей меня.\nСогрей меня.")
    }


screen dialog(message = None, ok_action = Hide("dialog")):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    if blocker and not message:
        python:
            sprite_set = blocker_image[blocker_key]
            message_text = blocker_text[blocker_key]

        image sprite_set[0]:
            zoom sprite_set[1] align (sprite_set[2], sprite_set[3])
    else:
        $ message_text = message

    frame:
        vbox:
            align (0.5, 0.5)
            spacing 30

            label _(message_text):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action


image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat


## Confirm screen ##############################################################

init python:
    # [картинка, yalign]
    default_image = {
        layout.LOADING: ("m_chibi turned m2", 0.185),
        layout.OVERWRITE_SAVE: ("m_chibi turned m2", 0.22),
        layout.DELETE_SAVE: ("m_chibi turned m2", 0.22),
        layout.MAIN_MENU: ("n_chibi turned b3", 0.20),
        layout.QUIT: ("n_chibi turned b3", 0.20)
    }

    default_text = {
        layout.LOADING: _("Вы точно хотите загрузить сохранение?\nВсе несохранённые данные будут потеряны."),
        layout.OVERWRITE_SAVE: _("Вы точно хотите переписать сохранение?"),
        layout.DELETE_SAVE: _("Вы точно хотите удалить сохранение?"),
        layout.MAIN_MENU: _("Вы точно хотите вернуться в главное меню?\nВсе несохранённые данные будут потеряны."),
        layout.QUIT: _("Вы точно хотите выйти из игры?\nВсе несохранённые данные будут потеряны.")
    }


screen confirm(message, yes_action, no_action):
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    python:
        sprite_set = default_image[message]

    image sprite_set[0]:
        align (0.5, sprite_set[1])

    frame:
        vbox:
            align (0.5, 0.5)
            spacing 30

            label _(default_text[message]):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Нет") action no_action
                textbutton _("Да") action yes_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    align (0.5, 0.5)

style confirm_prompt_text:
    font "mod_assets/font/menu/NAMU-Pro.ttf"
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            if yuri_ghost_death != 0:
                text _("Защитная реакция мозга")
            else:
                text _("Пропуск")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform delayed_blink(delay, cycle):
    alpha 0.5

    pause delay

    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    size 24
    align (0.5, 0.5)

style skip_triangle:
    font "DejaVuSans.ttf"
    size 32


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    font "mod_assets/font/menu/UZSans-Regular.ttf"
    size gui.notify_text_size


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:
            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:
            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if config.narrator_menu is set to True, as it is above
        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

# This controls the maximum number of NVL-mode entries that can be displayed at once
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    pos (gui.nvl_name_xpos, gui.nvl_name_ypos)
    anchor (gui.nvl_name_xalign, 0.0)
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    pos (gui.nvl_text_xpos, gui.nvl_text_ypos)
    xanchor gui.nvl_text_xalign
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    pos (gui.nvl_thought_xpos, gui.nvl_thought_ypos)
    xanchor gui.nvl_thought_xalign
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


# # Thanks RenpyTom! Borrowed from the Ren'Py Launcher
# init python:
#     def scan_translations():
#
#         languages = renpy.known_languages()
#
#         if not languages:
#             return None
#
#         rv = [(i, renpy.translate_string("{#language name and font}", i)) for i in languages ]
#         rv.sort(key=lambda a : renpy.filter_text_tags(a[1], allow=[]).lower())
#
#         rv.insert(0, (None, "English"))
#
#         bound = math.ceil(len(rv)/2.)
#
#         return (rv[:bound], rv[bound:2*bound])
#
# default translations = scan_translations()
#
# screen choose_language():
#     default local_lang = _preferences.language
#     default chosen_lang = _preferences.language
#
#     modal True
#     style_prefix "radio"
#
#     add "gui/overlay/confirm.png"
#
#     frame:
#         style "confirm_frame"
#
#         vbox:
#             xalign .5
#             yalign .5
#             xsize 760
#             spacing 30
#
#             label renpy.translate_string(_("{#in language font}Please select a language"), local_lang):
#                 style "confirm_prompt"
#                 xalign 0.5
#
#             hbox:
#                 xalign .5
#                 for tran in translations:
#                     vbox:
#                         for tlid, tlname in tran:
#                             textbutton tlname:
#                                 xalign .5
#                                 action SetScreenVariable("chosen_lang", tlid)
#                                 hovered SetScreenVariable("local_lang", tlid)
#                                 unhovered SetScreenVariable("local_lang", chosen_lang)
#
#             $ lang_name = renpy.translate_string("{#language name and font}", local_lang)
#
#             hbox:
#                 xalign 0.5
#                 spacing 100
#
#                 textbutton renpy.translate_string(_("{#in language font}Select"), local_lang):
#                     style "confirm_button"
#                     action [Language(chosen_lang), Return()]
#
# translate None strings:
#     old "{#language name and font}"
#     new "English"
#
# label choose_language:
#     call screen choose_language
#     return
