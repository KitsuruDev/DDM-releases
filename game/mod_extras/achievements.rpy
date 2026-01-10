## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## achievements.rpy

default persistent.achievements = {}

init -1 python in Achievements:
    from store import persistent, im
    dict, current = {}, None

    # This class declares the code to make a achievement (Non-Counting).
    # Syntax:
    #   name - This variable contains the human-readable name of the achievement.
    #   description - This variable contains the human-readable description of your
    #       achievement.
    #   image - This variable contains the path or image tag of the achievement.
    #   persistent - This variable contain the name of a in-game variable to check if the
    #       achievement has been completed or not.
    #   count - This variable checks if the achievement declared requires a number to match.
    #   locked_desc - This variable contains the human-readable description of your
    #       achievement when it is locked.
    class Achievement(object):
        def __init__(self, name, description, image, timeline=None, locked_desc="???"):
            self.name = name
            self.description = description
            self.image = f"mod_assets/mod_extra_images/achievements/{image}.png"
            self.timeline = timeline

            self.locked = "mod_assets/mod_extra_images/achievements/ach_locked.png"
            self.locked_desc = locked_desc

            if self.name not in persistent.achievements:
                persistent.achievements[self.name] = {"unlocked": False, "current_count": 0}

            self.unlocked = persistent.achievements[self.name]['unlocked']

            dict[self.name] = self

        def unlock(self):
            self.unlocked = True
            persistent.achievements[self.name]['unlocked'] = True
            renpy.show_screen("achievement_notify", self)

    # This class declares the code to make a achievement (Non-Counting).
    # This class has the same syntax as Achievement but 1 more argurment.
    # Refer to Achievement for the rest of the argurments here.
    # Syntax:
    #   max_count = The total counts needed to unlock the achievement
    class AchievementCount(Achievement):
        def __init__(self, name, description, image, timeline=None, max_count=100):
            Achievement.__init__(self, name, description, image, timeline)
            self.current_count = persistent.achievements[self.name]['current_count']
            self.max_count = max_count

        def increase_count(self):
            self.current_count += 1
            persistent.achievements[self.name]['current_count'] += 1
            if self.current_count == self.max_count: self.unlock()


init python:

    ach_timeline_prologue = _("Пролог. День")
    ach_timeline_act_1 = _("Акт 1 \"Новая жизнь\". День")

    #################### ОСНОВНОЙ СЮЖЕТ ####################

    ##### Пролог #####

    ach_pr_d1 = Achievement(
        _("Здравствуй, самостоятельность"),
        _("Начать новую жизнь."),
        "main_history/prologue/d1",
        f"{ach_timeline_prologue} 1"
    )

    ach_pr_d2 = Achievement(
        _("Конец спокойствия"),
        _("Заочно вступить в Литературный клуб."),
        "main_history/prologue/d2",
        f"{ach_timeline_prologue} 2"
    )


    ##### Акт 1 #####

    ach_a1_d1 = Achievement(
        _("Творческое начало"),
        _("Составить первый стих для\nЛитературного клуба."),
        "main_history/act_1/d1",
        f"{ach_timeline_act_1} 1"
    )

    ach_a1_d2 = Achievement(
        _("Счастливые мысли"),
        _("Написать стих в стиле Сайори."),
        "main_history/act_1/d2",
        f"{ach_timeline_act_1} 2"
    )

    ach_a1_d3 = Achievement(
        _("Писательское наслаждение"),
        _("Написать стих в стиле Юри."),
        "main_history/act_1/d3",
        f"{ach_timeline_act_1} 3"
    )

    ach_a1_d4 = Achievement(
        _("Поверхностное изречение"),
        _("Написать стих в стиле Нацуки."),
        "main_history/act_1/d4",
        f"{ach_timeline_act_1} 4"
    )

    ach_a1_d5 = Achievement(
        _("Теперь все могут быть счастливы"),
        _("Пережить кошмар с Сайори."),
        "main_history/act_1/d5",
        f"{ach_timeline_act_1} 5"
    )

    ach_a1_d6 = Achievement(
        _("Семь прощаний"),
        _("Восстановить связи Литературного клуба."),
        "main_history/act_1/d6",
        f"{ach_timeline_act_1} 6"
    )

    ach_a1_d7 = Achievement(
        _("Да кто такие эти ваши кексы?"),
        _("Принять участие в готовке кексов\nдля Литературного клуба"),
        "main_history/act_1/d7",
        f"{ach_timeline_act_1} 7"
    )

    ach_a1_d8 = Achievement(
        _("Синдром Аспергера"),
        _("Отпраздновать воссоединение\nкрайне нестандартным способом"),
        "main_history/act_1/d8",
        f"{ach_timeline_act_1} 8"
    )

    ach_a1_d9 = Achievement(
        _("Успешное пополнение"),
        _("Завлечь Котоноху в\nЛитературный клуб"),
        "main_history/act_1/d9",
        f"{ach_timeline_act_1} 9"
    )

    ach_a1_d10 = Achievement(
        _("Социальный голод"),
        _("Пережить кошмар с Нацуки."),
        "main_history/act_1/d10",
        f"{ach_timeline_act_1} 10"
    )

    ach_a1_d11 = Achievement(
        _("Гормональное безумие"),
        _("Пережить кошмар с Юри."),
        "main_history/act_1/d11",
        f"{ach_timeline_act_1} 11"
    )

    ach_a1_d12 = Achievement(
        _("Депривация любви"),
        _("Победить Нацуки и Юри в кошмаре."),
        "main_history/act_1/d12",
        f"{ach_timeline_act_1} 12"
    )

    ach_a1_d13 = Achievement(
        _("Имплицитное ядро"),
        _("Заглянуть себе в душу."),
        "main_history/act_1/d13",
        f"{ach_timeline_act_1} 13"
    )

    ach_a1_d14 = Achievement(
        _("Синкретическая основа"),
        _("Завершить 1 акт."),
        "main_history/act_1/d14",
        f"{ach_timeline_act_1} 14"
    )


    ##### Секретка #####

    ach_secret_gift = Achievement(
        _("Я у Мони программист"),
        _("Спасибо за помощь в\nпоиске багов, [persistent.playername]!"),
        "ach_secret_gift"
    )


## Achievements Screen #############################################################

screen achievements():
    tag menu

    style_prefix "achievements"

    use game_menu(_("Достижения")):

        frame:
            background "extra_background_element"

            vbox:
                xpos 0.185 ypos -0.197

                hbox:
                    if not Achievements.current:
                        null width 62
                        text _("Нажмите на иконку достижения,\nчтобы увидеть его описание"):
                            style "achievements_show_label_text"
                    else:
                        add ConditionSwitch(
                                Achievements.current.unlocked, Achievements.current.image, "True",
                                Achievements.current.locked) at achievement_scaler(200)

                    vbox:
                        xsize 400
                        ypos 0.1

                        if not Achievements.current:
                            null height 180

                        else:
                            if not Achievements.current.unlocked:
                                text Achievements.current.locked_desc:
                                    style "achievements_show_label_text"
                                    size 25

                                null height 10

                                text _("Достижение заблокировано"):
                                    style "achievements_label_text"
                                    size 22

                                null height 7

                                if isinstance(Achievements.current, AchievementCount):
                                    text "[Achievements.current.locked_desc] ([Achievements.current.current_count] / [Achievements.current.max_count])"
                                else:
                                    text Achievements.current.locked_desc

                            else:
                                text Achievements.current.timeline:
                                    style "achievements_show_label_text"
                                    size 25

                                null height 10

                                text Achievements.current.name:
                                    style "achievements_label_text"
                                    size 22

                                null height 7

                                if isinstance(Achievements.current, AchievementCount):
                                    text "[Achievements.current.description] ([Achievements.current.current_count] / [Achievements.current.max_count])"
                                else:
                                    text Achievements.current.description

            vpgrid:
                id "avp"
                rows math.ceil(len(Achievements.dict) / 4.0)
                cols 4

                mousewheel True
                arrowkeys True
                allow_underfull True

                xalign 0.5 yalign 1.05
                ysize 400
                spacing 40

                for name, ach in Achievements.dict.items():

                    imagebutton:
                        idle Transform(ConditionSwitch(
                                ach.unlocked, ach.image, "True",
                                ach.locked), size=(128,128))
                        action SetVariable("Achievements.current", ach)

            vbar value YScrollValue("avp") xalign 1.015 ypos 0.28 ysize 370

        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
                "extra_screen_help",
                _("Помощь\nОписание достижения отображается в верхнем окне.\nНекоторые заблокированные достижения имеют счётчик совершаемых действий, который указан в их описании.\nТакие достижения разблокируются после его заполнения."),
                ok_action = Hide("extra_screen_help"),
                chibi = "y_chibi turned magnifier",
                chibi_pos = 50
            )

        if config.developer:
            textbutton "AN":
                text_size 30
                pos (0.89, 0.98)
                action ShowMenu("achievement_notify", ach_a1_d6)

style achievements_show_label_text is achievements_text
style achievements_show_label_text:
    size 30
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    yalign 0.59

style achievements_image_button:
    activate_sound gui.activate_sound



## Achievements Notify Screen #############################################################
##
## This screen is used to notify a user of a unlocked achievement.
##
## Syntax:
##   reward.image - This variable contains the path or image tag of the achievement.
##   reward.name - This variable contains the locked image of the achievement.
##
## To call on this menu, do 'show screen achievement_notify(X)' where X is the achievement in question itself.
## Make sure to set the variable assign to it or else it will show up as locked.

screen achievement_notify(reward):

    timer 0.1 action [Play("sound", "mod_assets/sound/modding/achievement_unlock.mp3")]

    style_prefix "achievements"

    frame at achievement_notif_transition:
        background "achievement_notify_background"

        xsize 570 ysize 210
        xalign 0.5

        hbox:
            xalign 0.2 yalign 0.5

            add reward.image at achievement_scaler(180)

            null width 15

            vbox:
                null height 5

                xalign 0.5
                spacing 15

                text _("Достижение разблокировано!"):
                    style "achievements_notify_label_text"
                text reward.name:
                    style "achievements_label_text"
                text reward.description size 18

    timer 6.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]


image achievement_notify_background:
    "mod_assets/elements/mod_gui/menu/achievement_notify_background.png"
    align (0.5, 0.25) size (639, 255)

style achievements_text is gui_text
style achievements_label_text is achievements_text
style achievements_notify_label_text is achievements_text

style achievements_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    color "#000"
    outlines []
    size 20
    text_align 0.5
    xalign 0.5

style achievements_label_text:
    color "#fff"
    outlines [(2, "#505050", 0, 0)]

style achievements_notify_label_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    size 17

transform achievement_scaler(x):
    xysize(x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0
