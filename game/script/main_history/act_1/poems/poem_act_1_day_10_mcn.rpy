
init python:
    poem_words_a1_d10_mcn = {
        1: (_("Время"), "mc", 0.4, 0.514),
        2: (_("Бремя"), "mc", 0.75, 0.31),
        3: (_("Космос"), "mc", 0.65, 0.31),
        4: (_("Звездолёт"), "mc", 0.6, 0.107),
        5: (_("Межгалактический полёт"), "mc", 0.32, 0.445),
        6: (_("АСТРОГУСЬ"), "n", 0.67, 0.435),
        7: (_("Человечество"), "mc", 0.7, 0.107),
        8: (_("Постижимо"), "mc", 0.69, 0.31),
        9: (_("Разнос"), "mc", 0.35, 0.514),
        10: (_("Куча переходов"), "mc", 0.62, 0.514),
        11: (_("АСТРОГУСЬ"), "n", 0.68, 0.22),
        12: (_("Строфы"), "mc", 0.35, 0.174),
        13: (_("Катастрофа"), "mc", 0.3, 0.107),
        14: (_("Больной мозг"), "mc", 0.69, 0.31),
        15: (_("Повеселиться невозможно"), "n", 0.19, 0.3),
        16: (_("Хватит портить"), "mc", 0.25, 0.31),
        17: (_("Воротить"), "n", 0.68, 0.582),
        18: (_("Хрень пихать"), "mc", 0.66, 0.445),
        19: (_("Душный"), "n", 0.37, 0.3),
        20: (_("Чистый лист"), "mc", 0.68, 0.31),
        21: (_("Ветвистое"), "mc", 0.19, 0.309),
        22: (_("Убрать обороты"), "mc", 0.35, 0.514),
        23: (_("Тишина"), "mc", 0.37, 0.31),
        24: (_("АСТРОГУСЬ"), "n", 0.78, 0.155)
    }


transform st_c22_in_out(x1, x2):
    subpixel True
    yalign 0.5 xcenter x1
    parallel:
        easein 1.08 xcenter x2
    parallel:
        easein_quad .18 yoffset -80
        easeout_quad .18 yoffset 0
        easein_quad .18 yoffset -80
        easeout_quad .18 yoffset 0
        easein_quad .18 yoffset -80
        easeout_quad .18 yoffset 0


image n_chibi_in:
    "n_chibi hop"
    st_c22_in_out(1380, 1030)
    "n_chibi turned"

image n_chibi_out:
    "n_chibi hop"
    st_c22_in_out(1030, 1380)




label poem_act_1_day_10_mcn_1:
    call skip_block_on
    scene bg notebook_full_mc
    show mc_chibi turned at st_c21:
        xzoom -1
    with dissolve_scene_full
    play music t4 fadein 3.0
    mc "Космос...{w}космос...{w}космос..."
    mc "Хм..."
    "Думается с трудом, но кое-что в голове появилось..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[1])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[2])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "Та-а-ак..."
    "Кривое и натянутое начало есть."
    "Может, дальше получится лучше?"
    call screen poem_game_duo(*poem_words_a1_d10_mcn[3])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[4])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[5])
    show mc_chibi at chibi_hop
    pause 0.72
    n "{size=19}Ха, вошёл в раж?{/size}"
    mc "Угу."
    n "{size=19}Ну-ка, мне даже самой интересно стало...{/size}"
    show n_chibi_in
    pause 1.0
    show mc_chibi e2
    mc "Да ладно, ты решила встать с кровати и помочь мне непосредственно?"
    hide n_chibi_in
    show n_chibi turned e2 at st_c22
    n "Всего лишь любопытство!"
    n "Не более."
    mc "Тогда на, любуйся."
    show n_chibi e1
    n "Тэк..."
    show mc_chibi e1
    mc "Правда, я последнюю строфу не дописал: рифму не придумал."
    show mc_chibi e2
    mc "Есть идеи?"
    mc "Её конец должен перекликаться вот здесь, с этим словом."
    n "Хм-м-м..."
    n "Кхмф..."
    mc "Что?"
    n "Есть одна..."
    mc "Тогда напиши, а то я так не сдвинусь дальше."
    call window_dialog("n")
    call screen poem_game_duo(*poem_words_a1_d10_mcn[6])
    stop music fadeout 3.0
    show n_chibi hop at chibi_hop
    pause 0.72
    show mc_chibi e1
    show n_chibi turned
    call window_dialog("mc")
    mc "......"
    mc "Что это?!"
    n "Астрогусь."
    mc "Понятнее не стало!"
    n "Ну типо, гусь-астронавт -- астрогусь."
    mc "......"
    show mc_chibi ce
    mc "Да ты издеваешься..."
    n "Ха-ха-ха!"
    show mc_chibi e2
    mc "Нацуки, тебе скучно, что-ли?"
    mc "Ты понимаешь, что вот ЭТО будет показано всему клубу?"
    show n_chibi e2
    n "Да."
    n "И?"
    show mc_chibi ce
    show n_chibi b2
    mc "Нет, ты не понимаешь..."
    n "Макс!"
    n "Стих должен приносить нам удовольствие!"
    show n_chibi e1
    n "А не превращаться в бумажную нудятину с высосанным из пальца подтекстно-метафорическим смыслом."
    show mc_chibi e2
    mc "Но ведь первые стихи ты как-то написала?"
    show n_chibi e2
    mc "Вон, про пауков же нормально вышло."
    mc "В чём сейчас проблема?"
    n "Я хочу у-д-о-в-о-ль-с-т-в-и-е, ещё раз говорю."
    n "П-о-и-г-р-а-ть."
    n "Аргх, порадоваться!"
    show mc_chibi ce
    mc "Нашла, где этим заниматься..."
    n "Самое время!"
    show n_chibi e1
    n "Мне надоело постоянно торчать в своей комнате."
    n "А тут с тобой нужно составить совместный стих."
    show mc_chibi e2
    show n_chibi b1
    mc "У тебя настолько всё с этим плохо?"
    n "..."
    show mc_chibi e1
    mc "Ладно, хватит время прожигать."
    mc "Дай я пока дальше попробую написать."
    n "Ага."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[7])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[8])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[9])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[10])
    show mc_chibi at chibi_hop
    pause 1.44
    call window_dialog("n")
    call screen poem_game_duo(*poem_words_a1_d10_mcn[11])
    play music dreams_of_hatred_and_literature
    show n_chibi hop at chibi_hop
    pause 0.72
    show mc_chibi e2
    show n_chibi turned
    call window_dialog("mc")
    mc "Да ёптить, Нацуки!"
    n "Ха-ха-ха-ха!"
    show mc_chibi e1
    mc "Чёрт, это ж всё под откос, все..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[12])
    show mc_chibi at chibi_hop
    pause 0.72
    show mc_chibi ce
    mc "Полная..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[13])
    show mc_chibi at chibi_hop
    pause 0.72
    show n_chibi e2
    n "Ой, не надо тут драматизировать."
    show n_chibi e1
    n "Прекрасно всё со стихом."
    show mc_chibi e2
    mc "Какой прекрасно, если стих два раза буквально оборвался?"
    show mc_chibi e1
    mc "У меня уже от этого..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[14])
    show mc_chibi at chibi_hop
    pause 0.72
    call window_dialog("n")
    show n_chibi e2 b2
    n "Да что ты вечно такой «правильный»?"
    call screen poem_game_duo(*poem_words_a1_d10_mcn[15])
    show n_chibi hop at chibi_hop
    pause 0.72
    show mc_chibi e2
    show n_chibi turned b2
    call window_dialog("mc")
    mc "Причём тут «правильность»?!"
    show mc_chibi e1
    mc "Стих..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[16])
    show mc_chibi at chibi_hop
    pause 0.72
    call window_dialog("n")
    show n_chibi m2 e2
    n "Порчу?!"
    show mc_chibi e2
    n "Ты тут опять со своей абстракцией!"
    mc "Чего?!"
    show n_chibi m1
    mc "Ты сама сказала написать что-то в духе «мечтаний»!"
    show n_chibi e1
    n "Да, но ты любишь всё..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[17])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned b2
    call window_dialog("mc")
    mc "В каком месте?!"
    show n_chibi e2
    mc "Давай, покажи!"
    n "Да во всём стихе!"
    mc "Знаешь, это самая наглая попытка уйти от ответственности!"
    n "Да неужели?"
    mc "Ага."
    show mc_chibi e1
    mc "Ты меня не послушаешь и продолжишь..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[18])
    show mc_chibi at chibi_hop
    pause 0.72
    call window_dialog("n")
    show n_chibi e1
    n "Какой же ты..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[19])
    show n_chibi hop at chibi_hop
    pause 0.72
    show n_chibi turned b2
    call window_dialog("mc")
    stop music
    play music_none_loop music_stop
    mc "ТАК, ВСЁ, СТОП!" with vpunch
    show n_chibi e2
    n "..."
    show mc_chibi ce
    mc "Не будем собачиться."
    mc "Иначе такими темпами ничего не добьёмся."
    show mc_chibi e1
    mc "Нам нужно начать заново."
    mc "Но продолжим писать здесь же: у меня листов не так много осталось, чтобы ими разбрасываться."
    show n_chibi e1
    n "Хмф-ф-ф..."
    show n_chibi b1
    mc "Поэтому...{w}так...{w}вот, ограничение готово."
    mc "Начнём мы..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[20])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "...а дальше..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[21])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "Вот, снова что-то получается."
    show n_chibi e2
    mc "Видишь?"
    mc "И ничего не перекручено."
    mc "Просто надо..."
    call screen poem_game_duo(*poem_words_a1_d10_mcn[22])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d10_mcn[23])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "Тц, снова ступор на последнем слове..."
    show n_chibi e1
    n "Ясно, мой выход."
    window hide
    call window_dialog("n")
    call screen poem_game_duo(*poem_words_a1_d10_mcn[24])
    show n_chibi hop at chibi_hop
    pause 0.72
    show mc_chibi ce
    show n_chibi turned
    window auto
    call window_dialog("mc")
    mc "Чёрт тебя дери, Нацуки, с твоим тупым мемом..."
    hide n_chibi
    show n_chibi_out
    n "Хи-хи-хи!"
    play music natsuki_run
    show mc_chibi e2
    hide n_chibi_out
    mc "Куда вскочила?!"
    mc "{sc=2}А ну стой!{/sc}"
    call skip_block_off

    return


label poem_act_1_day_10_mcn_2:
    call skip_block_on
    scene bg notebook_full_mc
    show mc_chibi turned ce at st_c21:
        xzoom -1
    with dissolve_cg
    pause 0.5
    mc "Нет, это реально какое-то позорище..."
    "Зачем я только предложил эту инициативу?"
    "Точнее спровоцировал на выбор этой инициативы..."
    n "{size=19}Эй, ты там что, заперся?{/size}"
    show mc_chibi e1
    "Всё, давайте уже покончим с этой хренью."
    play sound door_knock volume 0.5
    pause 1.5
    n "{size=19}МАКС!{/size}"
    mc "Допишу и открою, успокойся!"
    "Нет, даже по словам ориентироваться не буду."
    n "{size=19}Впусти меня!{/size}"
    "Мысли прямо так ложатся."
    show mc_chibi ce
    n "{size=19}Хватит издеваться!{/size}"
    mc "Кто бы говорил!"
    n "{size=19}Я просто хочу повеселиться!{/size}"
    mc "Вот когда стих допишу, тогда и будет тебе веселье!"
    n "{size=19}Времени мало!{/size}"
    mc "Если продолжишь стучать, его станет ешё меньше!"
    n "{size=19}ТЦ!{/size}"
    "Ух, тишина..."
    show mc_chibi e1
    mc "Так..."
    "...мысли размазаны..."
    "...зияет пустота..."
    mc "Хм-хм-хм..."
    "...вот и живи вот так всегда, пока не развалишься на части."
    mc "Всё!"
    mc "Позорище готово."
    n "{size=19}Что ты там бубнишь?{/size}"
    mc "Закончил, говорю!"
    mc "Сейчас прочитаю и открою..."
    call skip_block_off

    return
