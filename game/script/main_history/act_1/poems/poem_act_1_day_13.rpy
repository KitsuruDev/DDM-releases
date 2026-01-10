
init python:
    poem_words_a1_d13 = {
        1: (_("Мир"), "k_chibi_poem hop", 0.25, 0.31),
        2: (_("Вместе"), "m_chibi_poem hop", 0.8, 0.514),
        3: (_("Радость"), "s_chibi_poem hop", 0.65, 0.31),
        4: (_("Мозг"), "y_chibi_poem hop", 0.7, 0.107),
        5: (_("Пронзай"), "y_chibi_poem hop", 0.7, 0.514),
        6: (_("Вырвать"), "n_chibi_poem hop", 0.3, 0.445),
        7: (_("Зрачки"), "y_chibi_poem hop", 0.35, 0.107),
        8: (_("Стыд"), "s_chibi_poem hop", 0.68, 0.31),
        9: (_("Слова"), "m_chibi_poem hop", 0.2, 0.445),
        10: (_("Оглушённый"), "s_chibi_poem hop", 0.2, 0.31),
        11: (_("Руки"), "y_chibi_poem hop", 0.4, 0.514),
        12: (_("Ласка"), "n_chibi_poem hop", 0.19, 0.31),
        13: (_("Любовь"), "m_chibi_poem hop", 0.8, 0.514),
        14: (_("Вырвало"), "n_chibi_poem hop", 0.24, 0.445),
        15: (_("Забота"), "n_chibi_poem hop", 0.68, 0.31),
        16: (_("Сломаться"), "s_chibi_poem hop", 0.8, 0.514),
        17: (_("Анализировать"), "m_chibi_poem hop", 0.37, 0.31),
        18: (_("Осчастливить"), "s_chibi_poem hop", 0.72, 0.107),
        19: (_("Стихи"), "k_chibi_poem hop", 0.65, 0.31),
        20: (_("Паралич"), "y_chibi_poem hop", 0.35, 0.107),
        21: (_("ПРОСНИСЬ"), "mix_chibi glitch hop", 0.5, 0.45),
        22: (_("И"), "mix_chibi glitch hop", 0.5, 0.45),
        23: (_("ПОЙ"), "mix_chibi glitch hop", 0.5, 0.45)
    }




label poem_act_1_day_13:
    window hide

    $ blocker = True
    $ blocker_key = "poem_before_mmm"

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

    call screen dialog("...", ok_action=Return())
    call screen dialog("...ну типа...", ok_action=Return())
    call screen dialog("...хм...", ok_action=Return())
    call screen dialog("Будь, что будет.", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d13[1])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[2])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[16])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[20])

    show noise zorder 5:
        alpha 0.3
    hide screen quick_menu
    stop music
    play music t4g
    hide m_chibi_poem
    hide s_chibi_poem
    hide n_chibi_poem
    hide y_chibi_poem
    show mmm_chibi_poem hop at c_d51
    show s_chibi_poem drawing hop at c_d52
    show k_chibi_poem hop
    show n_chibi_poem glitch at c_d54
    show y_chibi_poem hopg at c_d55
    pause 0.2
    hide noise

    scene white
    show y_chibi_poem glitch at c_d51
    show mix_chibi glitch at c_d52
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[21])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[22])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d13[23])
    play sound baa
    pause 0.5

    stop music
    scene black

    return
