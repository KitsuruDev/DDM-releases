
init python:
    poem_words_a1_d4 = {
        1: (_("Кухня"), "n_chibi_poem hop", 0.25, 0.31),
        2: (_("Апельсин"), "s_chibi_poem hop", 0.8, 0.514),
        3: (_("Улыбка"), "s_chibi_poem hop", 0.65, 0.31),
        4: (_("На свете"), "y_chibi_poem_cut hop", 0.7, 0.107),
        5: (_("Солнце"), "s_chibi_poem hop", 0.7, 0.514),
        6: (_("Яркий"), "n_chibi_poem hop", 0.3, 0.445),
        7: (_("Мания"), "y_chibi_poem_cut hop", 0.35, 0.107),
        8: (_("Шкурка"), "s_chibi_poem hop", 0.68, 0.31),
        9: (_("Монолит"), "m_chibi_poem hop", 0.2, 0.445),
        10: (_("Развалить"), "s_chibi_poem hop", 0.2, 0.31),
        11: (_("Зашибись"), "n_chibi_poem hop", 0.4, 0.514),
        12: (_("Чёрт с тобой"), "n_chibi_poem hop", 0.19, 0.31),
        13: (_("Желудок"), "s_chibi_poem hop", 0.8, 0.514),
        14: (_("Наслаждение"), "y_chibi_poem_cut hop", 0.24, 0.445),
        15: (_("Класс"), "n_chibi_poem hop", 0.68, 0.31),
        16: (_("Мерзкие косточки"), "n_chibi_poem hop", 0.8, 0.514),
        17: (_("Ничего противного"), "n_chibi_poem hop", 0.37, 0.31),
        18: (_("Позитив"), "s_chibi_poem hop", 0.72, 0.107),
        19: (_("Обрадовать"), "s_chibi_poem hop", 0.65, 0.31),
        20: (_("Время"), "m_chibi_poem hop", 0.35, 0.107)
    }




label poem_act_1_day_4:
    window hide

    $ blocker = True
    $ blocker_key = "poem"

    call skip_block_on

    show screen quick_menu
    scene bg notebook_full_mc
    show m_chibi_poem at c_d41
    show s_chibi_poem at c_d42
    show n_chibi_poem at c_d43
    show y_chibi_poem_cut at c_d44
    with dissolve_scene_full

    play music t4 fadein 3.0

    call screen dialog("Нацуки-Нацуки-Нацуки...", ok_action=Return())
    call screen dialog("Что-то простое, да?", ok_action=Return())
    call screen dialog("Хм...", ok_action=Return())
    call screen dialog("Запах апельсина до сих пор идёт в нос.", ok_action=Return())
    call screen dialog("Стих про апельсин?", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d4[1])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[2])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d4[20])
    pause 1.5
    call screen dialog("Ух, в этот раз сразу на одном дыхании.", ok_action=Return())
    call screen dialog("Чтоб так каждый раз было...", ok_action=Return())
    call screen dialog("Итак, что же получилось?", ok_action=Return())
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
