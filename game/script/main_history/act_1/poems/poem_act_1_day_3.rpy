
init python:
    poem_words_a1_d3 = {
        1: (_("Байка"), "y_chibi_poem hop", 0.65, 0.31),
        2: (_("Волшебник"), "y_chibi_poem hop", 0.25, 0.31),
        3: (_("Густая чаща"), "y_chibi_poem hop", 0.8, 0.514),
        4: (_("Гора самоцветов"), "y_chibi_poem hop", 0.3, 0.445),
        5: (_("Экипироваться"), "n_chibi_poem hop", 0.7, 0.514),
        6: (_("Большой путь"), "m_chibi_poem hop", 0.7, 0.107),
        7: (_("Лесная пустота"), "y_chibi_poem hop", 0.68, 0.31),
        8: (_("Ангел"), "y_chibi_poem hop", 0.35, 0.107),
        9: (_("Огонь"), "y_chibi_poem hop", 0.2, 0.445),
        10: (_("Обработанные камни"), "y_chibi_poem hop", 0.8, 0.514),
        11: (_("Сапфир"), "s_chibi_poem hop", 0.4, 0.514),
        12: (_("Бездна"), "y_chibi_poem hop", 0.2, 0.31),
        13: (_("Аметист"), "y_chibi_poem hop", 0.19, 0.31),
        14: (_("Кристалл"), "y_chibi_poem hop", 0.8, 0.514),
        15: (_("Рубин"), "n_chibi_poem hop", 0.24, 0.445),
        16: (_("Безопасность"), "n_chibi_poem hop", 0.68, 0.31),
        17: (_("Изумруд"), "m_chibi_poem hop", 0.35, 0.107),
        18: (_("Неимоверный труд"), "m_chibi_poem hop", 0.72, 0.107),
        19: (_("Ярмарка"), "s_chibi_poem hop", 0.65, 0.31),
        20: (_("Талисман"), "s_chibi_poem hop", 0.37, 0.31)
    }




label poem_act_1_day_3:
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

    call screen dialog("Но мне нужен стержень, вокруг которого будет составляться стих.", ok_action=Return())
    call screen dialog("Что же это может быть?", ok_action=Return())
    call screen dialog("Книги, истории...", ok_action=Return())
    call screen dialog("Написать что-то в мире европейского средневековья?", ok_action=Return())
    call screen dialog("Не люблю я эту тему...", ok_action=Return())
    call screen dialog("...", ok_action=Return())
    call screen dialog("Хотя...", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d3[1])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[2])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[4])
    pause 1.5
    call screen dialog("Да!", ok_action=Return())
    call screen dialog("Я напишу стих про драгоценные камни.", ok_action=Return())
    call screen dialog("А назову его -- «Рудник».", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d3[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d3[20])
    pause 1.5
    call screen dialog("Вот так-то!", ok_action=Return())
    call screen dialog("Я даже собой доволен в некоторой степени.", ok_action=Return())
    call screen dialog("Посмотрим на нашу первую объёмную работу.", ok_action=Return())
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
