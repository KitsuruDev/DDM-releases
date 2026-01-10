
init python:
    poem_words_a1_d2 = {
        1: (_("Угрюмо"), "y_chibi_poem hop", 0.8, 0.514),
        2: (_("Смятая кровать"), "s_chibi_poem hop", 0.3, 0.445),
        3: (_("Понимание"), "m_chibi_poem hop", 0.65, 0.31),
        4: (_("Рутинный день"), "m_chibi_poem hop", 0.25, 0.31),
        5: (_("Залиться"), "y_chibi_poem hop", 0.7, 0.514),
        6: (_("Жёлтый оттенок"), "s_chibi_poem hop", 0.35, 0.107),
        7: (_("Свет"), "s_chibi_poem hop", 0.2, 0.445),
        8: (_("Достало"), "n_chibi_poem hop", 0.7, 0.107),
        9: (_("Пробуждение"), "s_chibi_poem hop", 0.68, 0.31),
        10: (_("Повторение"), "m_chibi_poem hop", 0.6, 0.514),
        11: (_("Исподлобья"), "y_chibi_poem hop", 0.2, 0.31),
        12: (_("Презрение"), "n_chibi_poem hop", 0.4, 0.514),
        13: (_("Смерть"), "y_chibi_poem hop", 0.8, 0.514),
        14: (_("Встать"), "s_chibi_poem hop", 0.19, 0.31),
        15: (_("День"), "m_chibi_poem hop", 0.35, 0.107),
        16: (_("Через себя"), "s_chibi_poem hop", 0.68, 0.31),
        17: (_("Барьер"), "y_chibi_poem hop", 0.24, 0.445),
        18: (_("Лень"), "n_chibi_poem hop", 0.37, 0.31),
        19: (_("Сонливость"), "y_chibi_poem hop", 0.65, 0.31),
        20: (_("Железная дверь"), "y_chibi_poem hop", 0.72, 0.107)
    }




label poem_act_1_day_2:
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

    call screen dialog("Что бы она сама написала?", ok_action=Return())
    call screen dialog("...", ok_action=Return())
    call screen dialog("Или мне тоже написать про своё утро?", ok_action=Return())
    call screen dialog("Ну...", ok_action=Return())
    call screen dialog("Хорошо, да будет так.", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d2[1])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[2])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[13])
    pause 1.5
    call screen dialog("Куда-то меня понесло...", ok_action=Return())
    call screen dialog("Это вообще не позитивный стих.", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d2[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d2[20])
    pause 1.5
    call screen dialog("Готово.", ok_action=Return())
    call screen dialog("Итак, кульминационный момент...", ok_action=Return())
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
