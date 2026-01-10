
init python:
    poem_words_a1_d1 = {
        1: (_("Куча мыслей"), "s_chibi_poem hop", 0.65, 0.31),
        2: (_("Думать"), "y_chibi_poem hop", 0.3, 0.445),
        3: (_("Круто"), "n_chibi_poem hop", 0.8, 0.514),
        4: (_("Белый лист"), "m_chibi_poem hop", 0.25, 0.31),
        5: (_("Белоснежный"), "y_chibi_poem hop", 0.35, 0.107),
        6: (_("Криворучка"), "n_chibi_poem hop", 0.7, 0.514),
        7: (_("Время"), "m_chibi_poem hop", 0.2, 0.445),
        8: (_("Грамотно изрекать"), "y_chibi_poem hop", 0.7, 0.107),
        9: (_("Муторно"), "m_chibi_poem hop", 0.6, 0.514),
        10: (_("Стараться"), "s_chibi_poem hop", 0.2, 0.31),
        11: (_("Бумага"), "m_chibi_poem hop", 0.68, 0.31),
        12: (_("Пустота"), "y_chibi_poem hop", 0.4, 0.514),
        13: (_("Напряг"), "n_chibi_poem hop", 0.72, 0.107),
        14: (_("Рифма"), "m_chibi_poem hop", 0.35, 0.107),
        15: (_("Плевать"), "n_chibi_poem hop", 0.19, 0.31),
        16: (_("Прилагать силу"), "s_chibi_poem hop", 0.8, 0.514),
        17: (_("Поэма"), "y_chibi_poem hop", 0.65, 0.31),
        18: (_("Творить"), "m_chibi_poem hop", 0.24, 0.445),
        19: (_("Так сойдёт"), "n_chibi_poem hop", 0.37, 0.31),
        20: (_("Чих"), "s_chibi_poem hop", 0.68, 0.31)
    }




label poem_act_1_day_1:
    window hide

    $ blocker = True
    $ blocker_key = "poem"

    call skip_block_on
    show screen quick_menu
    scene bg notebook_full_mc
    show m_chibi_poem at c_d41
    show s_chibi_poem at c_d42
    show n_chibi_poem at c_d43
    show y_chibi_poem at c_d44
    with dissolve_scene_full

    play music t4 fadein 3.0

    call screen dialog("Итак, слова...", ok_action=Return())
    pause 3.0
    call screen dialog("Что, если...", ok_action=Return())
    call screen poem_game_solo(*poem_words_a1_d1[1])
    pause 1.5
    call screen dialog("Ну и начало. Надо думать дальше...", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d1[2])
    pause 1.5
    call screen dialog("Круто, что-то получается.", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d1[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[6])
    pause 1.5
    call screen dialog("Самокритично.", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d1[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[14])
    pause 1.5
    call screen dialog("Какая-то фигня выходит...", ok_action=Return())
    call screen dialog("..........", ok_action=Return())
    call screen dialog("Ну и плевать, первый раз же.", ok_action=Return())
    call screen poem_game_solo(*poem_words_a1_d1[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d1[18])
    pause 1.5
    call screen dialog("Или всё-таки...", ok_action=Return())
    call screen dialog("..........", ok_action=Return())
    call screen dialog("Ай, ладно.", ok_action=Return())
    call screen poem_game_solo(*poem_words_a1_d1[19])
    pause 1.5
    call screen dialog("А конец?", ok_action=Return())
    call screen dialog("Концовка никакущая.", ok_action=Return())
    call screen dialog("Нет подходящего слова.", ok_action=Return())
    call screen dialog("За исключением одного, но тогда точно бред выходит.", ok_action=Return())
    call screen dialog("Эх, блин, выбора нет.", ok_action=Return())
    call screen poem_game_solo(*poem_words_a1_d1[20])
    pause 1.5
    call screen dialog("Что ж, всё.", ok_action=Return())
    call screen dialog("А ну-ка глянем, что получилось...", ok_action=Return())
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
