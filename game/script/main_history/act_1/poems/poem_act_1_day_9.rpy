
init python:
    poem_words_a1_d9 = {
        1: (_("Тишина"), "y_chibi_poem hop", 0.65, 0.31),
        2: (_("Цикл"), "m_chibi_poem hop", 0.3, 0.445),
        3: (_("Нервы"), "n_chibi_poem hop", 0.8, 0.514),
        4: (_("Жизнь"), "k_chibi_poem hop", 0.25, 0.31),
        5: (_("Спокоен"), "y_chibi_poem hop", 0.35, 0.107),
        6: (_("Дорога"), "m_chibi_poem hop", 0.7, 0.514),
        7: (_("Монотонность"), "s_chibi_poem hop", 0.2, 0.445),
        8: (_("Песни"), "y_chibi_poem hop", 0.7, 0.107),
        9: (_("Счастье"), "s_chibi_poem hop", 0.6, 0.514),
        10: (_("Взгляд"), "m_chibi_poem hop", 0.2, 0.31),
        11: (_("Огонь"), "y_chibi_poem hop", 0.68, 0.31),
        12: (_("Сердце"), "y_chibi_poem hop", 0.4, 0.514),
        13: (_("Разгар"), "y_chibi_poem hop", 0.72, 0.107),
        14: (_("Сбежать"), "n_chibi_poem hop", 0.35, 0.107),
        15: (_("Холодный"), "s_chibi_poem hop", 0.19, 0.31),
        16: (_("Пожар"), "y_chibi_poem hop", 0.8, 0.514),
        17: (_("Удар"), "n_chibi_poem hop", 0.65, 0.31),
        18: (_("Железный"), "m_chibi_poem hop", 0.24, 0.445),
        19: (_("Глаза"), "m_chibi_poem hop", 0.37, 0.31),
        20: (_("Магнит"), "y_chibi_poem hop", 0.68, 0.31)
    }




label poem_act_1_day_9:
    window hide

    $ blocker = True
    $ blocker_key = "poem"

    call skip_block_on

    show screen quick_menu
    scene bg notebook_full_mc
    show m_chibi_poem at c_d51
    show s_chibi_poem at c_d52
    show k_chibi_poem at c_d53
    show n_chibi_poem at c_d54
    show y_chibi_poem at c_d55
    with dissolve_scene_full

    play music t4 fadein 3.0

    call screen dialog("Наша задача осложняется тем, что\nни меня, ни Монику не смутило отсутствие\nпримера для написания.", ok_action=Return())
    call screen dialog("А хотя зачем он...", ok_action=Return())
    call screen dialog("«Абстракционизм» Моники у меня\nотносительно запомнился.", ok_action=Return())
    call screen dialog("Так что поехали.", ok_action=Return())
    pause 5.0
    call screen dialog("Ну и куда?", ok_action=Return())
    call screen dialog("О чём писать?", ok_action=Return())
    call screen dialog("Моника-Моника-Моника...", ok_action=Return())
    call screen dialog("Глаза, бант, волосы...", ok_action=Return())
    call screen dialog("Что ни мысль, то вечно её образ.", ok_action=Return())
    call screen dialog("Особенно глаза в голове всплывают.", ok_action=Return())
    call screen dialog("Может, тогда взять их за основу?", ok_action=Return())
    call screen dialog("М-м-м, ладно, попробуем...", ok_action=Return())
    pause 1.0
    call screen poem_game_solo(*poem_words_a1_d9[1])
    pause 3.0
    call screen poem_game_solo(*poem_words_a1_d9[2])
    pause 1.5
    call screen dialog("Отлично, есть начало!", ok_action=Return())
    call screen dialog("С трудом и не сразу, но всё-таки...", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d9[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d9[20])
    pause 1.5
    call screen dialog("Ага, смотрим...", ok_action=Return())
    pause 0.5

    call skip_block_off

    stop music fadeout 3.0

    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0

    $ blocker = False

    return
