
label qte_act_1_day_8:

    play noise_2 natsuki_steps_run
    scene bg corridor
    show layer master at run_shaking
    show sora turned neut cm oe s_scream at j22
    with wipeleft_scene
    show sora at thide
    hide sora
    pause 0.2
    window show(Dissolve(0.25))
    n "{sc=3}СТО-О-ОЙ!!!{/sc}"
    window hide(Dissolve(0.25))

    call screen qte_key_interactive("W", 5)

    if _return == 0:
        show layer master:
            align (0.5, 0.5)
            parallel:
                easeout 0.15 yoffset 0 zoom 1.1
                ease 0.5 rotate -45 zoom 3.0 xoffset -200
            parallel:
                ease 0.05 yoffset -3
                ease 0.05 yoffset 3
                ease 0.05 yoffset -3
                ease 0.05 yoffset 3
        stop noise_2
        pause 0.25

        scene black with dissolve
        play sound falldown
        with vpunch
        pause 0.25

        window show(Dissolve(0.25))
        n "{sc=3}А-А-А-А-А!!!{/sc}"
        "{sc=3}БОЛЬНО!!!{/sc}"
        "{sc=3}НЕТ, СЕЙЧАС НЕ ДО БОЛИ!!!{/sc}"
        play noise_2 natsuki_steps_run
        "{sc=3}НАДО ДОГНАТЬ ЭТОГО ВОРА!!!{/sc}"
        window hide(Dissolve(0.25))

    play noise_1 school_corridor_hard_noise fadein 2.0
    scene bg school f2 new_corridor
    show crowd_foreground zorder 2
    show sora turned neut cm oe s_scream zorder 1:
        xcenter 900 yanchor 1.0 ypos 0.76 zoom 0.5
        parallel:
            easein 0.15 yoffset 15
            easeout 0.25 yoffset 0
            repeat
    show crowd_background zorder 0
    show layer master at run_shaking
    with wipeleft_scene
    window show(Dissolve(0.25))
    n "{sc=3}ВЕРНИ МОЙ ЧЁРТОВ КЕКС!!!{/sc}"
    window hide(Dissolve(0.25))
    show sora:
        ease 0.2 alpha 0 zoom 0.48
    pause 0.2
    hide sora

    call screen qte_key_interactive("W", 5)

    scene black with wipeleft_scene
    window show(Dissolve(0.25))
    if _return == 1:
        n "{sc=3}Я ТЕБЯ ДОГОНЮ, СЛЫШИШЬ?!{/sc}"
        "{sc=3}НА ТРЕТИЙ ЭТАЖ ПОБЕЖАЛ, ЗАСРАНЕЦ!{/sc}"
        "{sc=3}ОН ТЕБЯ НЕ СПАСЁТ!{/sc}"
        "{sc=3}АРГХ, СТУПЕНЬКИ!{/sc}"
    else:
        stop noise_2
        "{sc=3}БЛИН, НЕТ!{/sc}"
        "{sc=3}Я ЕГО ПОТЕРЯЛА!{/sc}"
        "{sc=3}КУДА ОН МОГ УЙТИ?!{/sc}"
        "{sc=3}КУДА?!{/sc}"
        "{sc=3}...{/sc}"
        "{sc=3}А, ЕГО СИЛУЭТ МЕЛЬКНУЛ НА ЛЕСТНИЦЕ!{/sc}"
        play noise_2 natsuki_steps_run
        "{sc=3}НА ТРЕТИЙ ЭТАЖ ПОБЕЖАЛ, ЗАСРАНЕЦ!{/sc}"
        "{sc=3}ПРИДЁТСЯ БЕЖАТЬ ПО ЧЁРТОВЫМ СТУПЕНЬКАМ!{/sc}"
    window hide(Dissolve(0.25))

    call screen qte_key_interactive("ПРОБЕЛ", 5)

    if _return == 0:
        play sound hit
        stop noise_2
        scene white
        pause 0.1
        scene black
        show particle_star
        with dissolve
        window show(Dissolve(0.25))
        n "{sc=3}А-А-АЙ!!!{/sc}"
        "{sc=3}ДА ЧТО Ж ТАКОЕ?!{/sc}"
        "{sc=3}КАК МОЖНО БЫЛО ТАК ГЛУПО ЗАПНУТЬСЯ?!{/sc}"
        "{sc=3}ПОЧЕМУ ИЗ-ЗА ЭТОГО ПРИДУРКА Я ДОЛЖНА СЕБЯ КАЛЕЧИТЬ?!{/sc}"
        "{sc=3}НЕТ, Я ЕГО НЕ ОТПУЩУ!{/sc}"
        play noise_2 natsuki_steps_run
        "{sc=3}Я ЕГО ДОГОНЮ!{/sc}"
        window hide(Dissolve(0.25))

    play noise_1 school_corridor_hard_noise fadein 2.0
    scene bg school f3 new_corridor
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    show layer master at run_shaking
    with wipeleft_scene
    window show(Dissolve(0.25))
    "{sc=3}ДА-ДА-ДА, ЕЩЁ ОДНА ТОЛПА!{/sc}"
    "{sc=3}ГДЕ ЕГО ТУТ ИСКАТЬ?!{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}ВОТ!{/sc}"
    "{sc=3}Я ВИДЕЛА ЕГО В КОНЦЕ КОРИДОРА!{/sc}"
    "{sc=3}БЕЖИТ В СТАРЫЙ КОРПУС!{/sc}"
    "{sc=3}НАДО ЕГО ДОГНАТЬ, ПОКА ОН НЕ СКРЫЛСЯ!{/sc}"
    window hide(Dissolve(0.25))

    call screen qte_key_interactive("W", 5)

    scene black with wipeleft_scene
    stop noise_1 fadeout 2.0

    window show(Dissolve(0.25))
    if _return == 1:
        "{sc=3}Я ЕГО ДОГОНЮ-ДОГОНЮ-ДОГОНЮ!!!{/sc}"
        "{sc=3}ЕЩЁ НЕМНОГО!!!{/sc}"
    else:
        "{sc=3}ТЕМП СБИЛСЯ!{/sc}"
        "{sc=3}Я СЕЙЧАС ВЫДОХНУСЬ!{/sc}"
        "{sc=3}ПХА!{/sc}"
        "{sc=3}НЕЛЬЗЯ СЕЙЧАС БЫТЬ СЛАБОЙ!{/sc}"
        "{sc=3}ПОДНАЖМИ!!!{/sc}"
    window hide(Dissolve(0.25))

    pause 4.0
    stop noise_2

    return
