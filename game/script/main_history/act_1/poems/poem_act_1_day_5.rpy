
init python:
    poem_words_a1_d5 = {
        1: (_("Полуночная пора"), "s_chibi_poem drawing hop", 0.65, 0.31),
        2: (_("Печаль"), "s_chibi_poem drawing hop", 0.3, 0.445),
        3: (_("Пронзённое сердце"), "s_chibi_poem drawing hop", 0.8, 0.514),
        4: (_("Опустошение"), "s_chibi_poem drawing hop", 0.25, 0.31),
        5: (_("Светлый стержень"), "s_chibi_poem drawing hop", 0.35, 0.107),
        6: (_("Осколки"), "s_chibi_poem drawing hop", 0.7, 0.514),
        7: (_("Мир вверх дном"), "s_chibi_poem drawing hop", 0.2, 0.445),
        8: (_("Счастье"), "s_chibi_poem drawing hop", 0.7, 0.107),
        9: (_("Прекрасная душа"), "s_chibi_poem drawing hop", 0.7, 0.514),
        10: (_("Решение"), "s_chibi_poem drawing hop", 0.2, 0.31),
        11: (_("Тяготы"), "s_chibi_poem drawing hop", 0.68, 0.31),
        12: (_("Пытание"), "s_chibi_poem drawing hop", 0.4, 0.514),
        13: (_("Верёвка"), "s_chibi_poem drawing hop", 0.72, 0.107),
        14: (_("Шея"), "s_chibi_poem drawing hop", 0.35, 0.107),
        15: (_("Табурет"), "s_chibi_poem drawing hop", 0.19, 0.31),
        16: (_("Панические страхи"), "s_chibi_poem drawing hop", 0.8, 0.514),
        17: (_("Тошнота"), "s_chibi_poem drawing hop", 0.65, 0.31),
        18: (_("Рыдание"), "s_chibi_poem drawing hop", 0.24, 0.445),
        19: (_("Вешний голос"), "s_chibi_poem drawing hop", 0.37, 0.31),
        20: (_("Погасшие звёзды"), "s_chibi_poem drawing hop", 0.68, 0.31)
    }




label poem_act_1_day_5:
    window hide

    $ blocker = True
    $ blocker_key = "sayori_ghost"

    call skip_block_on

    show screen quick_menu
    scene bg notebook_full_mc
    show s_chibi_poem drawing at c_d42
    show mmm_chibi_poem:
        xcenter 1200 yalign 1.4
    with dissolve_scene_full

    show noise zorder 5:
        alpha 0
        linear 3 alpha 0.1

    play music "bgm/s_kill_early.ogg" fadein 3.0

    call screen dialog("Слова сами лезут в голову...", ok_action=Return())
    pause 0.5
    call screen poem_game_solo(*poem_words_a1_d5[1])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[2])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[3])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[4])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[5])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[6])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[7])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[8])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[9])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[10])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[11])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[12])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[13])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[14])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[15])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[16])
    show mmm_chibi_poem big hop
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[17])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[18])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[19])
    pause 1.5
    call screen poem_game_solo(*poem_words_a1_d5[20])
    pause 1.5
    call screen dialog("...", ok_action=Return())
    pause 0.5

    call skip_block_off

    stop music fadeout 3.0

    hide screen quick_menu
    show black zorder 6 as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0

    $ blocker = False

    return
