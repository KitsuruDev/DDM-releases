# extras_screen.rpy

screen extras():
    tag menu
    style_prefix "extras"

    use game_menu(_("Экстра")):

        fixed:

            vpgrid id "ext":
                rows 2 cols 3
                allow_underfull True

                align (0.5, 0.4)
                spacing 70

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/characters.png", (15, 75), Text(_("Персонажи"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/characters.png", (13, 73), Text(_("Персонажи"), style="extras_hover_text"))
                            action (
                                If(
                                    persistent.full_playthrough,
                                    (
                                        SetVariable("extra_submenu_active", True),
                                        ShowMenu("characters")
                                    ),
                                    ShowMenu(
                                        "extra_screen_help",
                                        message = "Пройдите сюжет, чтобы\nоткрыть раздел «Персонажи».",
                                        ok_action = Hide("extra_screen_help"),
                                        chibi = "s_chibi turned mt ce",
                                        chibi_pos = 95
                                    )
                                )
                            )

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery_cg.png", (30, 75), Text(_("Галерея\n(CG)"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery_cg.png", (28, 73), Text(_("Галерея\n(CG)"), style="extras_hover_text"))
                            action (
                                SetVariable("extra_submenu_active", True),
                                ShowMenu("gallery_cg")
                            )

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery_bg.png", (30, 75), Text(_("Галерея\n(фоны)"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery_bg.png", (28, 73), Text(_("Галерея\n(фоны)"), style="extras_hover_text"))
                            action (
                                If(
                                    persistent.full_playthrough,
                                    (
                                        SetVariable("extra_submenu_active", True),
                                        ShowMenu("gallery_bg")
                                    ),
                                    ShowMenu(
                                        "extra_screen_help",
                                        message = "Пройдите сюжет, чтобы\nоткрыть раздел «Галерея (фоны)».",
                                        ok_action = Hide("extra_screen_help"),
                                        chibi = "s_chibi turned mt ce",
                                        chibi_pos = 95
                                    )
                                )
                            )

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (11, 75), Text(_("Достижения"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (9, 73), Text(_("Достижения"), style="extras_hover_text"))
                            action (SetVariable("extra_submenu_active", True), ShowMenu("achievements"))

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/ost_player.png", (32, 75), Text(_("Музыка"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/ost_player.png", (30, 73), Text(_("Музыка"), style="extras_hover_text"))
                            action (
                                If(
                                    persistent.full_playthrough,
                                    (
                                        SetVariable("extra_submenu_active", True),
                                        SetVariable("extra_submenu_music_player_active", True),
                                        Stop("music", fadeout=1.0),
                                        ShowMenu("music_player")
                                    ),
                                    ShowMenu(
                                        "extra_screen_help",
                                        message = "Пройдите сюжет, чтобы\nоткрыть раздел «Музыка».",
                                        ok_action = Hide("extra_screen_help"),
                                        chibi = "s_chibi turned mt ce",
                                        chibi_pos = 95
                                    )
                                )
                            )

                frame:
                    vbox:
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (36, 75), Text(_("О моде"), style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (34, 73), Text(_("О моде"), style="extras_hover_text"))
                            action (SetVariable("extra_submenu_active", True), ShowMenu("about"))

            vbar value YScrollValue("ext") xalign 0.99 ysize 560

        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
            "extra_screen_help",
            _("Помощь\nПри затруднениях вызывайте помощь через кнопку в форме знака вопроса.\nЭкстра-меню с персонажами, галереей (фоны) и музыкой будут открыты после прохождения всего имеющегося сюжета мода.\nЭкстра-меню с достижениями и галереей (CG) доступны сразу и заполняются элементами по мере прохождения."),
            ok_action = Hide("extra_screen_help"),
            chibi = "y_chibi turned magnifier",
            chibi_pos = 30)


style extras_frame:
    xsize 160
    ysize 140

style extras_vbox:
    xalign 0.5
    yalign 0.5

style extras_text:
    font "mod_assets/font/menu/NAMU-Pro.ttf"
    color "#000"
    outlines []
    size 20
    text_align 0.5
    line_leading -4

style extras_hover_text is extras_text:
    outlines [(2, "#cacaca", 0, 0), (1, "#cacaca", 0, 0)]

style extras_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound


default extra_submenu_active = False # для деактивации кнопок меню в подменю экстра
default extra_submenu_music_player_active = False # альтернатива renpy.music.is_playing("music"), т.к. команда не всегда отрабатывала


## Help Extra Screen #############################################################

screen extra_screen_help(message, ok_action, chibi, chibi_pos):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    add chibi:
        xalign 0.5 ypos chibi_pos

    frame:

        vbox:
            align (0.5, 0.5)
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action


## Extra Styles and Images #############################################################

image extra_background_element:
    "mod_assets/elements/mod_gui/menu/extra_background_element.png"
    size (665, 260)
    xalign 0.5 ypos -0.235
