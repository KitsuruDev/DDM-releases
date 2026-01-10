## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## about.rpy

screen about():

    tag menu

    use game_menu(_("О моде"), scroll="viewport"):

        style_prefix "about"

        window:
            xoffset 35
            has fixed:
                yfit True

            vbox:
                label _("Фанатская модификация «[config.name!t]»")
                null height 5
                label _("Разработчик «Multi Orange Team»")
                null height 25
                hbox:
                    null width 54
                    add "mod_assets/elements/logo/act/act_1.png" zoom 0.3
                    null width 65
                    add "mod_assets/elements/logo/developers.png" crop(205, 15, 880, 670) zoom 0.45

                null height 70

                label _("Оригинальная игра «Doki Doki Literature Club!»")
                null height 5
                label _("Разработчики «Team Salvato»")
                null height 25
                hbox:
                    null width 60
                    add "gui/logo.png" zoom 0.58
                    null width 150
                    add "bg/splash.png" crop(460, 115, 365, 460) zoom 0.65

                null height 70

                text _("Мод сделан на основе шаблона {a=https://github.com/GanstaKingofSA/DDLCModTemplate2.0}DDLC Mod Template 2.0{/a} -- Version 4.0.0.\nс добавлением кодов достижений и галереи из Version 4.0.2.\nАвтор шаблона -- Azariel Del Carmen (GanstaKingofSA)\n")
                text _("Авторские права по шаблону действительны и принадлежат вышеуказанному автору: Copyright © 2019 -- " + str(date.today().year) + ".\nВсе авторские права защищены.\n")
                text _("Авторские права по оригинальной игре \"Doki Doki Literature Club!\" принадлежат Team Salvato: Copyright © 2017.\nВсе авторские права защищены.\n")
                text _("Мод сделан с помощью {a=https://www.renpy.org/}Ren'Py{/a} версии [renpy.version_only].\n")
                text _("Лицензия по использованию Ren'Py:\n[renpy.license!t]")


style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label:
    xalign 0.5

style about_label_text:
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    size gui.label_text_size
    text_align 0.5

style about_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    xalign 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color "#000"
    hover_color "#e3b6f5ff"
    hover_underline True
