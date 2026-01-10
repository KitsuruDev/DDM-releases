
init python:
    poem_words_a1_d10_ny = {
        1: (_("Начни"), "n", 0.65, 0.3),
        2: (_("Сложно"), "y", 0.3, 0.445),
        3: (_("Осторожно"), "y", 0.4, 0.514),
        4: (_("Начхать"), "n", 0.75, 0.3),
        5: (_("Понятно"), "n", 0.6, 0.162),
        6: (_("Красота"), "y", 0.35, 0.514),
        7: (_("Никакого смысла"), "n", 0.67, 0.445),
        8: (_("Хватит"), "n", 0.7, 0.162),
        9: (_("Часть меня"), "y", 0.3, 0.445),
        10: (_("Не слушаешь"), "n", 0.69, 0.3),
        11: (_("Завуалированно"), "n", 0.68, 0.234),
        12: (_("Плеваться"), "n", 0.6, 0.514),
        13: (_("Буйство"), "y", 0.3, 0.1),
        14: (_("Наивно"), "y", 0.35, 0.17),
        15: (_("Принять"), "y", 0.19, 0.306),
        16: (_("Не понимаешь"), "n", 0.68, 0.582),
        17: (_("Раздражаешь"), "y", 0.25, 0.309),
        18: (_("Часть твоя -- часть моя"), "n", 0.66, 0.445),
        19: (_("Ерунда"), "y", 0.37, 0.31),
        20: (_("Твори"), "n", 0.68, 0.3),
        21: (_("Бред"), "y", 0.37, 0.31),
        22: (_("Не вижу радости"), "n", 0.68, 0.3),
        23: (_("Так не пойдёт"), "y", 0.37, 0.305),
        24: (_("Манга"), "n", 0.68, 0.3),
        25: (_("Хватит издеваться"), "y", 0.35, 0.305),
        26: (_("Зараза"), "y_seizure", 0.3, 0.511),
        27: (_("Пусти"), "n", 0.37, 0.3),
        28: (_("Вместе"), "y_seizure", 0.42, 0.3),
        29: (_("Верни"), "n", 0.37, 0.3),
        30: (_("Пора взрослеть"), "y_seizure", 0.35, 0.511),
        31: (_("Перестань наглеть"), "n", 0.66, 0.514),
        32: (_("Хватит кобениться"), "y_seizure", 0.32, 0.37),
        33: (_("Хватит ерепениться"), "n", 0.7, 0.3),
        34: (_("ЗАТКНИСЬ"), "y_seizure", 0.3, 0.3),
        35: (_("Отпусти"), "n", 0.37, 0.3),
        36: (_("ЗАТКНИСЬ"), "y_seizure", 0.35, 0.3),
        37: (_("ДОСТАЛА"), "y_seizure", 0.35, 0.37),
        38: (_("ЗАТКНИСЬ"), "n", 0.68, 0.435)
    }


image n_chibi_vang:
    st_c22
    "n_chibi turned m2 e2 b2"

image n_chibi_vang hop:
    st_c22
    "n_chibi hop m2"
    chibi_hop(-180)
    "n_chibi turned m2 e2 b2"


image y_chibi_vang:
    xzoom -1
    st_c21
    "y_chibi turned m2 e2 b2"

image y_chibi_vang hop:
    xzoom -1
    st_c21
    "y_chibi hop m2 b2"
    chibi_hop(-180)
    "y_chibi turned m2 e2 b2"




label poem_act_1_day_10_ny:
    call skip_block_on
    scene bg notebook_full_y
    show y_chibi turned at st_c21:
        xzoom -1
    show n_chibi turned at st_c22
    with dissolve_scene_full
    "..."
    "......"
    show n_chibi e2
    "...ну и?"
    n "Мы начнём или как?"
    y "Я думаю..."
    n "...уже целую вечность!"
    show y_chibi e2
    show n_chibi e1
    n "Просто возьми и..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[1])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2
    call window_dialog("y")
    show y_chibi e1
    y "Нет, это слишком..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[2])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    y "Нельзя так легкомысленно к этому подходить."
    y "Со стихом нужно обращаться..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[3])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned e2
    call window_dialog("n")
    show n_chibi e1
    n "Ой, да мне..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[4])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2
    n "Обычные, простые слова, и всё!"
    show y_chibi e1
    n "Что тут запарного?"
    call screen poem_game_duo(*poem_words_a1_d10_ny[5])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2
    call window_dialog("y")
    y "Я не могу так, Нацуки."
    y "Стих -- это нечто сакральное, позыв души..."
    y "В нём должна быть..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[6])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned e2
    call window_dialog("n")
    show n_chibi b2
    play music dreams_of_hatred_and_literature
    n "Да какой в этом вообще смысл?!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[7])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    show y_chibi b2
    n "Юри, ты слишком над этим запарываешься."
    call screen poem_game_duo(*poem_words_a1_d10_ny[8])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    call window_dialog("y")
    y "Запарываюсь?!"
    y "Это мой честный труд!"
    show y_chibi e1
    y "Это..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[9])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    call window_dialog("n")
    show n_chibi e1
    n "ФИ!"
    show y_chibi e2
    n "Да ты вообще..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[10])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned b2
    n "Сколько можно писать так..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[11])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    n "Ну серьёзно?!"
    show y_chibi b2
    n "Мозг каждый раз ломается от понимания смысла, который ты заложила."
    n "Постоянно хочется с этого..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[12])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    call window_dialog("y")
    y "Вот именно, хочется плеваться!"
    y "Плеваться от твоей неграмотности и простодушия."
    y "Чего только стоит твоё..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[13])
    show y_chibi hop b2 at chibi_hop
    pause 0.72
    show y_chibi turned e2 b2
    show n_chibi m2
    y "Твой стиль ничем не лучше моего."
    y "В нём всё..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[14])
    show y_chibi hop b2 at chibi_hop
    pause 0.72
    show y_chibi turned e2 b2
    y "А раз ты не можешь понять мои стихотворения, то это твоя проблема."
    y "Тебе остаётся лишь это..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[15])
    show y_chibi hop b2 at chibi_hop
    pause 0.72
    show y_chibi turned e2 b2
    call window_dialog("n")
    y "Тебе надо развиваться, а не сидеть на месте!"
    "Опять она за своё!"
    n "Хватит меня учить!"
    n "Ты меня даже..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[16])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    show y_chibi m2
    "Какая же она упёртая!"
    y "Как же ты меня..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[17])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    k "{size=19}Ребят, потише, сбавьте обороты...{/size}"
    n "Ах, ну раз так..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[18])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m1 e2 b2
    call window_dialog("y")
    show y_chibi m1
    n "Давай, возрадуйся."
    y "Ч-что..."
    k "{size=19}Эй!{/size}"
    show y_chibi e1
    y "Это какая-то..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[19])
    show y_chibi hop b2 at chibi_hop
    pause 0.72
    show y_chibi turned e2 b2
    call window_dialog("n")
    n "Ну мой же стиль «наивный», а?"
    l "{size=19}Они тебя не слышат...{/size}"
    n "Давай, пиши свой «идеальный» стих на своей части!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[20])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    call window_dialog("y")
    y "Нацуки, это уже полнейший..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[21])
    show y_chibi hop b2 at chibi_hop
    pause 0.72
    show y_chibi turned e2 b2
    call window_dialog("n")
    n "Хм-м-м, странно, Юри..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[22])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    call window_dialog("y")
    show y_chibi m2
    y "Нацуки, хватит!"
    y "Мы должны написать стих совместно, а не по отдельности на своих сторонах!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[23])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    n "Даже и не мечтай, что я вернусь обратно."
    show n_chibi e1
    n "Разве только в том случае, если в литературе всё-таки окажется..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[24])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned e2 b2
    call window_dialog("y")
    y "Что ты несёшь?!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[25])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    n "Ой-ой, а где ж твой хвалёный «смысл»?"
    n "Давай, покажи мне, как надо!"
    y "Так, с меня хватит..."
    y "Иди сюда..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[26])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    show n_chibi m2
    n "Отпусти мою руку!"
    n "Что ты делаешь?!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[27])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    y "Пытаюсь вразумить тебя и вернуть на место!"
    y "Мы ДОЛЖНЫ написать этот стих..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[28])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    n "Нет уж, после всего, что ты наговорила, обратно меня..."
    call screen poem_game_duo(*poem_words_a1_d10_ny[29])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    y "Нацуки, перестань устраивать шоу!"
    y "Тебе уже 18!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[30])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    n "Ты сама меня провоцируешь!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[31])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    y "Я?!"
    y "Это ты тут всегда начинаешь!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[32])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    n "Потому что ты не в состоянии меня услышать!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[33])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    y "{sc=3}А-А-А-А-А!{/sc}"
    call screen poem_game_duo(*poem_words_a1_d10_ny[34])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    y "Меня сначала послушай!"
    n "А может, меня?!"
    y "{sc=3}ЗАТКНИСЬ!{/sc}"
    k "{size=19}Тихо!{/size}"
    l "{size=19}Это они так стихи сочиняют?{/size}"
    n "Да отцепись от моей руки!"
    call screen poem_game_duo(*poem_words_a1_d10_ny[35])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("y")
    y "{sc=3}ХВАТИТ!{/sc}"
    call screen poem_game_duo(*poem_words_a1_d10_ny[36])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call screen poem_game_duo(*poem_words_a1_d10_ny[37])
    show y_chibi hop m2 b2 at chibi_hop
    pause 0.72
    show y_chibi turned m2 e2 b2
    call window_dialog("n")
    n "{sc=3}САМА...{/sc}"
    call screen poem_game_duo(*poem_words_a1_d10_ny[38])
    show n_chibi hop m2 at chibi_hop
    pause 0.72
    show n_chibi turned m2 e2 b2
    call window_dialog("ny", multiple = True)
    ny "{sc=3}ЗАТКНИ-И-И-И-И-И-И-И-И-И-И-И-И-И-ИСЬ!!!{/sc}"
    k "{size=19}Успокойтесь!!!{/size}"
    call window_close

    hide y_chibi turned
    show y_chibi_vang
    hide n_chibi turned
    show n_chibi_vang

    python:
        progress = 1
        numWords = 10

        while True:
            ystart = 140

            for j in range(2):
                x = 375 if j == 0 else 695

                ui.vbox()

                for i in range(5):
                    seizure_word = list("ЗАТКНИСЬ")

                    if random.randint(0, 1):
                        for letter_pos in range(8):
                            if random.randint(0, 4) == 0:
                                seizure_word[letter_pos] = random.choice("ЗАТКНИСЬ")

                        ui.textbutton(
                            seizure_word,
                            hover_sound="mod_assets/sound/modding/buttons/word/hover_n.mp3",
                            clicked=ui.returns(s),
                            text_style="poem_button_n_text",
                            xpos=x,
                            ypos=i * 56 + ystart
                        )

                    else:
                        for letter_pos in range(8):
                            if random.randint(0, 4) == 0:
                                seizure_word[letter_pos] = random.choice(nonunicode)

                        ui.textbutton(
                            seizure_word,
                            hover_sound="mod_assets/sound/modding/buttons/word/hover_y_seizure.mp3",
                            clicked=ui.returns(s),
                            text_style="poem_button_y_seizure_text",
                            xpos=x,
                            ypos=i * 56 + ystart
                        )

                ui.close()

            ui.interact()

            renpy.play("mod_assets/sound/modding/buttons/word/select.mp3")
            renpy.show("y_chibi_vang hop")
            renpy.show("n_chibi_vang hop")
            progress += 1

            if progress > numWords:
                break

    call window_open
    stop music
    play music_none_loop music_stop
    call window_dialog("k")
    k "{sc=3}СТОП!!!{/sc}" with vpunch
    call skip_block_off

    return
