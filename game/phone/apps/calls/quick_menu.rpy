screen phone_quick_menu():
    grid 3 2 style_prefix "phone_quick_menu":
        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_history_idle.png"
                hover phone.config.basedir + "quick_menu_history_selected.png"
                selected_idle phone.config.basedir + "quick_menu_history_selected.png"
                activate_sound gui.activate_sound
                action ShowMenu("history")
            text _("История")

        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_afm_idle.png"
                hover phone.config.basedir + "quick_menu_afm_selected.png"
                selected_idle phone.config.basedir + "quick_menu_afm_selected.png"
                activate_sound gui.activate_sound
                action Preference("auto-forward", "toggle")
            text _("Авточтение")

        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_load_idle.png"
                hover phone.config.basedir + "quick_menu_load_selected.png"
                selected_idle phone.config.basedir + "quick_menu_load_selected.png"
                activate_sound gui.activate_sound
                action ShowMenu("load")
            text _("Загрузка")

        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_settings_idle.png"
                hover phone.config.basedir + "quick_menu_settings_selected.png"
                selected_idle phone.config.basedir + "quick_menu_settings_selected.png"
                activate_sound gui.activate_sound
                action ShowMenu("preferences")
            text _("Настройки")

        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_skip_idle.png"
                hover phone.config.basedir + "quick_menu_skip_selected.png"
                selected_idle phone.config.basedir + "quick_menu_skip_selected.png"
                activate_sound gui.activate_sound
                action Skip()
            text _("Пропуск")

        vbox:
            imagebutton:
                xalign 0.5
                idle phone.config.basedir + "quick_menu_save_idle.png"
                hover phone.config.basedir + "quick_menu_save_selected.png"
                selected_idle phone.config.basedir + "quick_menu_save_selected.png"
                activate_sound gui.activate_sound
                action ShowMenu("save")
            text _("Сохранение")


style phone_quick_menu_grid is empty:
    xspacing 21 yspacing 22

style phone_quick_menu_vbox is empty:
    xalign 0.5

style phone_quick_menu_text is phone_call_time:
    xalign 0.5
    size 14


screen phone_quick_menu_video():
    default qm = False

    add "#000":
        if qm:
            at transform:
                ease 0.35 alpha 0.35
        else:
            at transform:
                ease 0.35 alpha 0.0

    vbox style "empty" yalign 1.0 xsize 1.0 xfill True:
        button style "empty" padding (5, 7, 5, 4) xalign 0.5:
            at transform:
                ease 0.35 matrixtransform RotateMatrix(0, 0, 180 * qm) matrixcolor OpacityMatrix(0.8 if qm else 0.6)

            action ToggleLocalVariable("qm")

            add phone.config.basedir + "arrow_icon.png":
                at transform:
                    subpixel True xysize (70, 18)

        frame style "empty" top_padding 30 bottom_padding 15 xsize 1.0 modal True:
            if qm:
                at transform:
                    ease 0.35 crop (0, 0, 1.0, 1.0) alpha 1.0
            else:
                at transform:
                    ease 0.35 crop (0, 0, 1.0, 0.0) alpha 0.0

            background "#00000060"

            vbox style "empty" xalign 0.5:
                use phone_quick_menu()

                null height 15

                add phone.config.basedir + "hang_up.png":
                    subpixel True xysize (63, 63) xalign 0.5
