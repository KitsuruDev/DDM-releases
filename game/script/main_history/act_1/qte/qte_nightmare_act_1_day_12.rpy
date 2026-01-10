
screen touch_yuri_ghost_a1_nd12:
    button:
        area(479, 268, 70, 36)
        mouse "touch"
        action [Play("sound", "mod_assets/sound/body/hit_eyes.mp3"), Return()]

    timer 1.0/30.0 repeat True action Function(RigMouse, 430, 620)


screen punch_natsuki_ghost_a1_nd12:
    button:
        area(365, 115, 600, 600)
        mouse "punch"
        action [Hide("punch_natsuki_ghost_a1_nd12"), Play("sound", "mod_assets/sound/body/hit.mp3"), SetVariable("qte_stage", 1), Jump("nightmare_act_1_day_12_qte_nice_punch_man")]




label nightmare_act_1_day_12_qte_yuri_ghost:
    call screen touch_yuri_ghost_a1_nd12

    stop music
    hide yuri_realistic_eyes
    hide yuripupils
    hide yuristeam

    show yuri turned pani om e4c lup rup at face
    show yuri at tfast
    pause 0.25
    show yuri:
        ease 0.1 xoffset 3
        ease 0.1 xoffset -3
        repeat
    $ style.say_dialogue = style.edited
    y "АААААААААААААААААААААААААА--{nw}"
    $ style.say_dialogue = style.normal
    show yuri:
        ease 0.1 xoffset 0
    play sound fall
    play music confrontation_part_1
    hide yuri with easeoutbottom

    window auto
    "{sc=3}ЕСТЬ, ВАШУ Ж МАТЬ!!!{/sc}"
    if persistent.censorship:
        "{sc=3}БЕЖИМ ОТСЮДА К ЧЁРТУ!!!{/sc}"
    else:
        "{sc=3}БЕЖИМ ОТСЮДА НАХЕР!!!{/sc}"
    "{sc=2}...{/sc}"
    "{sc=2}Ключи на учительском столе?!{/sc}"
    "{sc=3}ОТ КЛАССА!{/sc}"
    "{sc=3}ДА, НАДО ЕГО ЗАПЕРЕТЬ!!!{/sc}"
    window hide

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    $ qte_stage = 0

    jump nightmare_act_1_day_12_qte_0



label nightmare_act_1_day_12_qte_0:
    window auto
    queue music confrontation_part_2
    scene bg corridor
    show darkred zorder 3:
        alpha 0.5

    if qte_loss_transition:
        with dissolve_qte
        $ qte_loss_transition = False
    else:
        with wipeleft_scene

    play sound club_door_lock_close
    pause 2.0
    mc "{sc=3}ХА-ХА-ХА!!!{/sc}"
    "{sc=3}НА ЛЕСТНИЦУ, СРОЧНО!!!{/sc}"
    mc "{sc=3}А-А-А!!!...{/sc}" with vpunch
    if persistent.censorship:
        "{sc=3}ЗАРАЗА!!!{/sc}"
    else:
        "{sc=3}СУКА!!!{/sc}"
    "{sc=3}ОПЯТЬ ПАРАЛИЗОВАЛО!!!{/sc}"
    "{sc=3}ЧЁРТОВО СТЕКЛО НА ДВЕРИ И РОЖА ПСЕВДО-ЮРИ!!!{/sc}"
    "{sc=3}КАКОЙ ПРИДУРОК ВСТАВИЛ СТЁКЛА В ЭТИ ДВЕРИ?!{/sc}"
    play sound club_door_knock
    with vpunch
    pause 1.0
    "{sc=3}ДА НЕ МОЖЕТ ВСЁ ТАК ЗАКОНЧИТЬСЯ!!!{/sc}"
    queue music confrontation_part_3
    show natsuki ghost_base at t11
    pause 1.0
    $ style.say_dialogue = style.edited
    n "Какого...{w=1.0}здесь происходит?"
    $ style.say_dialogue = style.normal
    "{sc=3}ТЫ-ТО ЧТО ТУТ ЗАБЫЛА?!{/sc}"
    show natsuki ghost_base at h11
    play sound club_door_knock
    with vpunch
    pause 1.5
    $ style.say_dialogue = style.edited
    n "А-а-а, я поняла..."
    show natsuki ghost2
    n "Ты её очень достал."
    n "Она хочет тебя убить."
    show natsuki ghost2 at h11
    play sound club_door_knock
    with vpunch
    pause 1.5
    n "Я её о-о-очень ненавижу, но сейчас с ней...{w}солидарна."
    n "Потому что ты мне тоже нагадил."
    n "Я тебя даже по имени называть не буду."
    show natsuki ghost2 at h11
    play sound club_door_knock
    with vpunch
    pause 1.5
    n "Слушай, а чего мне тут стоять и бездействовать?"
    show n_rects_left zorder 2:
        yoffset -20 alpha 0
        easeout 12 alpha 1.0
    show n_rects_right zorder 2:
        yoffset -20 alpha 0
        easeout 12 alpha 1.0
    n "Я тоже хочу тебя убить."
    n "Ты урод."
    n "Но ты обязательно поиграешь со мной в игру \"Сдохни или умри\"."
    play sound club_door_knock
    with vpunch
    pause 1.0
    n "И начнём мы..."
    play sound club_door_knock
    with vpunch
    pause 1.0
    n "...прямо..."
    stop music fadeout 1.0
    play sound club_door_knock_out
    with vpunch
    pause 0.5
    play sound fall2
    pause 1.0
    play music confrontation_part_4 fadein 1.0
    n "СЕЙЧА-А-АС!!!--{w=0.25}{nw}"
    $ style.say_dialogue = style.normal
    "{b}{color=f00}НАДО ВРЕЗАТЬ{/color} ЕЙ СО ВСЕЙ СИЛЫ!!!--{/b}{nw}"
    window hide

    show screen punch_natsuki_ghost_a1_nd12

    hide n_rects_left
    hide n_rects_right
    show natsuki ghost3
    show n_rects_neck_right zorder 4:
        pause 0.2
        easeout 0.25 zoom 4.5 xoffset 250 yoffset -250
    show n_rects_neck_left zorder 4:
        pause 0.2
        easeout 0.25 zoom 4.5 xoffset 250 yoffset -250
    pause 0.2
    hide natsuki

    play sound natsuki_ghost_run
    show natsuki ghost4 at i11
    pause 0.25

    hide screen punch_natsuki_ghost_a1_nd12

    jump nightmare_act_1_day_12_qte_loss



label nightmare_act_1_day_12_qte_nice_punch_man:
    scene black
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 0.25

    play sound falldown
    with vpunch
    pause 0.25

    window auto
    "{sc=3}ХА-ХА-ХА, В ЯБЛОЧКО!!!{/sc}"
    "{sc=3}НА ЛЕСТНИЦУ, БЕГОМ!!!{/sc}"
    window hide

    jump nightmare_act_1_day_12_qte_1



label nightmare_act_1_day_12_qte_1:
    scene bg school f2 old_stairwell center
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking

    if qte_loss_transition:
        with dissolve_qte
        play music confrontation_part_4 fadein 1.0
        $ qte_loss_transition = False
    else:
        with wipeleft_scene

    play noise_1 mc_steps_school_run

    window auto
    y "{sc=3}СТОЙ, МАКС, СТО-О-ОЙ!!!{/sc}"
    "{sc=3}СВОЛОЧЬ, ПЫТАЕТСЯ ЗАТОРМОЗИТЬ!{/sc}"
    "{sc=3}ОТКУДА У НЕЁ НОЖ?!{/sc}"
    "{sc=3}ПЛЕВАТЬ, НУЖНО СОПРОТИВЛЯТЬСЯ И БЕЖАТЬ ВНИЗ!!!{/sc}"
    window hide

    call screen qte_key_interactive("ПРОБЕЛ")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    window auto
    "{sc=3}ТВОЮ МАТЬ!{/sc}"
    "{sc=3}Я ЖЕ СПУСКАЛСЯ ВНИЗ!{/sc}"
    "{sc=3}ПОЧЕМУ ЭТО ТРЕТИЙ ЭТАЖ?!{/sc}"
    if persistent.censorship:
        "{sc=3}А-А-А, ПОШЛИ ВЫ НАХРЕН!{/sc}"
    else:
        "{sc=3}А-А-А, ПОШЛИ ВЫ НАХЕР!{/sc}"
    "{sc=3}БЕЖИМ В НОВЫЙ КОРПУС!{/sc}"

    scene bg school f3 old_corridor
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking
    with wipeleft_scene
    y "{sc=3}СТОЙ, ЛЮБИМЫЙ!{/sc}"
    y "{sc=3}ПРИМИ СВОЮ СУДЬБУ!!!{/sc}"
    window hide

    call screen qte_key_interactive("W")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    window auto
    "{sc=3}БЕГИ-БЕГИ-БЕГИ!!!{/sc}"

    scene bg school f3 new_corridor
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking
    with wipeleft_scene
    y "{sc=3}ЛЮБОВЬ -- САМОЕ ЛУЧШЕЕ ЧУВСТВО ИЗ ВСЕХ!!!{/sc}"
    y "{sc=3}ПЕРЕСТАНЬ УБЕГАТЬ!!!{/sc}"
    window hide

    call screen qte_key_interactive("W")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    window auto
    "{sc=3}ПОКА ДЫХАЛКА В НОРМЕ, ОТЛИЧНО!{/sc}"
    "{sc=3}КУДА БЕЖАТЬ, КУДА БЕЖАТЬ?!{/sc}"
    "{sc=3}НА ЗАПАСНУЮ ЛЕСТНИЦУ НЕ УДЕРЁШЬ!{/sc}"
    "{sc=3}НУЖНО СНОВА ВАЛИТЬ ВНИЗ!{/sc}"
    window hide

    call screen qte_key_interactive("ПРОБЕЛ")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    window auto
    "{sc=3}КАКОГО ЧЁРТА?!{/sc}"
    "{sc=3}ОТКУДА ЗДЕСЬ ЗАВАЛ?!{/sc}"
    "{sc=3}КАК МНЕ НА ПЕРВЫЙ ЭТАЖ ПОПАСТЬ?!{/sc}"
    "{sc=3}ТВОЮ МАТЬ, ЭТА СВОЛОЧЬ УЖЕ ДОГОНЯЕТ!{/sc}"
    "{sc=3}ОПЯТЬ БЕЖАТЬ В СТАРЫЙ КОРПУС?!{/sc}"
    "{sc=3}ВЫБОРА НЕТ!{/sc}"

    scene bg school f2 new_corridor
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking
    with wipeleft_scene
    y "{sc=3}ЛЮБИ МЕНЯ, МАКС!{/sc}"
    y "{sc=3}ЛЮБИ-И-И!!!{/sc}"
    window hide

    call screen qte_key_interactive("W")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    window auto
    "{sc=3}ОТЛИЧНО, СНОВА ТУТ!{/sc}"
    "{sc=3}БЕЖИМ НА ЛЕСТНИЦУ--{/sc}{nw}"
    stop noise_1
    "{sc=3}ЧТО?!{/sc}"
    "{sc=3}ОНА ВСЯ ЗАВАЛЕНА МУСОРОМ!!!{/sc}"
    "{sc=3}И ЛЕВЫЙ КОРИДОР ТОЖЕ!!!{/sc}"
    "{sc=3}ТОГДА БЕЖИМ НАПРАВО!{/sc}"
    play noise_1 mc_steps_school_run

    scene bg corridor
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking
    with wipeleft_scene
    "{sc=3}ХОРОШО, ЧТО ВТОРАЯ МРАЗЬ В ОТКЛЮЧКЕ!{/sc}"
    "{sc=3}ЗНАТНО ЕЙ ПРОПИСАЛ!{/sc}"

    scene black with wipeleft_scene
    "{sc=3}РАЗ-ДВА, РАЗ-ДВА, РАЗ-ДВА!{/sc}"
    stop noise_1
    "{sc=3}...ПРАВАЯ ЛЕСТНИЦА ТОЖЕ ПЕРЕКРЫТА!{/sc}"
    if persistent.censorship:
        "{sc=3}М-М-МАТЬ!!!!{/sc}"
    else:
        "{sc=3}СУ-У-УКА-А-А!!!!{/sc}"
    "{sc=3}ТОГДА ЗАПИРАЕМСЯ В КРАЙНЕМ КАБИНЕТЕ!{/sc}"
    "{sc=3}ПОТОМУ ЧТО В ЛИТЕРАТУРНОМ КЛУБЕ ОДНУ ДВЕРЬ\nВЫЛОМАЛИ!{/sc}"
    window hide

    play sound club_door_lock_close
    pause 2.0

    window auto
    "{sc=3}НУ А ДАЛЬШЕ ЧТО?!{/sc}"
    "{sc=3}ЗДЕСЬ ТОЖЕ СТУЛЬЯ К ПОЛУ ПРИКЛЕЕНЫ!{/sc}"
    "{sc=3}...{/sc}"

    $ qte_stage = 2

    jump nightmare_act_1_day_12_qte_2



label nightmare_act_1_day_12_qte_2:

    if qte_loss_transition:
        scene black with dissolve_qte
        play music confrontation_part_4 fadein 1.0
        $ qte_loss_transition = False
        window auto

    "{sc=3}ЗНАЮ!{/sc}"
    "{sc=3}СПРЯЧУСЬ СБОКУ, ВЫБЬЮ НОЖ, А ДАЛЬШЕ ПО\nОБСТАНОВКЕ!{/sc}"
    "{sc=3}ГЛАВНОЕ -- ОБЕЗВРЕДИТЬ ЕЁ И НЕ ДАТЬ МЕНЯ\nПАРАЛИЗОВАТЬ!{/sc}"
    play sound club_door_knock
    with vpunch
    pause 1.0
    "{sc=3}ЛОМИТСЯ, МРАЗЬ!{/sc}"
    play sound club_door_knock
    with vpunch
    pause 1.0
    "{sc=3}БЫЛА БЫ ТЫ УМНЕЕ, ПОПРОБОВАЛА БЫ ДРУГУЮ\nДВЕРЬ!{/sc}"
    "{sc=3}ХОТЯ Я ОБЕ ЗАКРЫЛ!{/sc}"
    play sound club_door_knock
    with vpunch
    pause 1.0
    "{sc=3}ТАК!{/sc}"
    "{sc=3}ПРИГОТОВИТЬСЯ!{/sc}"
    play sound club_door_knock
    with vpunch
    pause 1.0
    play sound club_door_knock
    with vpunch
    pause 1.0
    play sound club_door_knock
    with vpunch
    pause 1.0
    play sound club_door_knock_out
    with vpunch
    pause 0.5
    play sound fall2
    pause 1.0
    "{sc=3}СЕЙЧА-А-АС!!!--{/sc}{w=0.5}{nw}"
    window hide

    call screen qte_key_interactive("ЛКМ")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    jump nightmare_act_1_day_12_after_qte_yuri_ghost



label nightmare_act_1_day_12_qte_natsuki_ghost:
    scene black with wipeleft_scene
    stop noise_2
    play noise_1 mc_steps_school_run
    window auto
    "{sc=3}УВОРАЧИВАЕТСЯ, ГАДИНА!{/sc}"
    "{sc=3}И НОСИТСЯ ПО-СУМАСШЕДШЕМУ!{/sc}"
    "{sc=3}ТЕПЕРЬ ЕЙ ТАК НЕ ВЛУПИШЬ!{/sc}"
    "{sc=3}НУЖНО ОТКРЫТОЕ ПРОСТРАНСТВО!{/sc}"
    "{sc=3}И БЕЖАТЬ ЕЩЁ БЫСТРЕЕ!{/sc}"

    $ qte_stage = 3

    jump nightmare_act_1_day_12_qte_3



label nightmare_act_1_day_12_qte_3:
    scene bg corridor
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking

    if qte_loss_transition:
        with dissolve_qte
        play music confrontation_part_4 fadein 1.0
        play noise_1 mc_steps_school_run
        window auto
        $ qte_loss_transition = False
    else:
        with wipeleft_scene

    n "{sc=3}УМРИ!!!{/sc}"
    window hide

    call screen qte_key_interactive("W", 1.5, 5)

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    window auto
    "{sc=3}НИХРЕНА СЕБЕ!{/sc}"
    "{sc=3}ВЕРХНИЙ ЗАВАЛ НА ЛЕСТНИЦЕ ПРОПАЛ!{/sc}"
    "{sc=3}НО ВНИЗУ ОН ОСТАЛСЯ!{/sc}"
    "{sc=3}И ПОЯВИЛСЯ В КОРИДОРЕ НОВОГО КОРПУСА!{/sc}"
    "{sc=3}У МЕНЯ ДАЖЕ НЕТ ВРЕМЕНИ ЭТО ОСОЗНАТЬ!{/sc}"
    "{sc=3}ОСТАЁТСЯ БЕЖАТЬ НА КРЫШУ!{/sc}"

    scene bg school f2 old_stairwell center
    show darkred zorder 2:
        alpha 0.5
    show layer master at run_shaking
    with wipeleft_scene
    n "{sc=3}Я ТЕБЯ УБЬЮ, СЛЫШИШЬ?!{/sc}"
    n "{sc=3}УБЬЮ-Ю-Ю!{/sc}"
    window hide

    call screen qte_key_interactive("W", 1.5, 5)

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    scene black with wipeleft_scene
    queue music confrontation_part_6
    window auto
    "{sc=3}ПО СТУПЕНЬКАМ ОНА ДОЛЖНА БЕЖАТЬ МЕДЛЕННЕЕ!{/sc}"
    "{sc=3}НО ЭТО НЕ ПОВОД РАССЛАБЛЯТЬСЯ!{/sc}"
    "{sc=3}ШЕВЕЛИСЬ НАВЕРХ!!!{/sc}"
    window hide

    call screen qte_key_interactive("ПРОБЕЛ")

    if _return == 0:
        jump nightmare_act_1_day_12_qte_loss

    window auto
    "{sc=3}ТРЕТИЙ ЭТАЖ ЗАВАЛЕН, КТО БЫ СОМНЕВАЛСЯ!{/sc}"
    "{sc=3}НО МНЕ НУЖНА КРЫША!{/sc}"
    stop noise_1
    "{sc=3}А ВОТ И ДВЕРЬ!{/sc}"
    "{sc=3}ОТКРЫВАЙСЯ, ЗАРАЗА!{/sc}"
    "{sc=3}...{/sc}"
    mc "{sc=3}Я ТЕБЯ ВЫБЬЮ{w=0.5} НАХЕР!!!--{/sc}{w=0.5}{nw}"
    window hide

    play sound rooftop_door_knock_out
    pause 0.117
    with vpunch
    pause 1.0

    scene bg school new_rooftop 1 day
    show darkred zorder 2:
        alpha 0.5
    show school_new_rooftop_1_a1_d12_gun
    show layer master at stress(2.0, 0.5)
    with dissolve
    pause 1.0
    window auto
    "{sc=3}ГДЕ СТАРЫЙ КОРПУС?!{/sc}"
    "{sc=3}ПОЧЕМУ Я...{/sc}"
    "{sc=3}НИХРЕНА СЕБЕ, ПИСТОЛЕТ!{/sc}"
    window hide

    hide school_new_rooftop_1_a1_d12_gun with dissolve
    pause 0.25
    show pistol_view with dissolve
    pause 0.25

    window auto
    "{sc=3}ЧТО ЭТО ВООБЩЕ ЗА МОДЕЛЬ?!{/sc}"
    "{sc=3}ГДЕ ТУТ ПРЕДОХРАНИТЕЛЬ И СБРОС МАГАЗИНА?!{/sc}"
    "{sc=3}Я ТОЛЬКО КРАСНЫЙ ИНДИКАТОР СБОКУ ВИЖУ!{/sc}"
    "{sc=3}ЧЁРТ, ХОТЯ БЫ ЗАТВОР НАДО ВЫДВИНУТЬ!{/sc}"
    window hide

    hide pistol_view with dissolve
    pause 0.25
    play sound pistol_slide_open
    show pistol_open_slide:
        xoffset -40 yoffset -5
        ease 0.15 xoffset 10 yoffset 5
        ease 0.1 xoffset 0 yoffset 0
    with dissolve
    pause 0.25

    window auto
    "{sc=3}СРАБОТАЛО!{/sc}"
    "{sc=3}ИНДИКАТОР СТАЛ ЖЁЛТЫМ!{/sc}"
    "{sc=3}ПРЕДОХРАНИТЕЛЬ ТОЧНО СНЯТ!{/sc}"

    scene black with dissolve
    pause 0.25
    play sound pistol_slide_close
    pause 1.0
    "{sc=3}СТАЛ ЗЕЛЁНЫМ!{/sc}"
    "{sc=3}ЗНАЧИТ, ЗАРЯЖЕН?!{/sc}"
    play noise_1 natsuki_ghost_run fadein 1.5 volume 0.75
    "{sc=3}ТВОЮ МАТЬ, НЕТ ВРЕМЕНИ!{/sc}{w=1.0}{nw}"

    jump nightmare_act_1_day_12_after_qte_natsuki_ghost



label nightmare_act_1_day_12_qte_loss:
    $ qte_loss_transition = True

    if qte_stage == 1:
        show yuri turned yand om oe lup_item knife at movein_hugs
        pause 0.3
    elif qte_stage == 3:
        show natsuki ghost2 run at natsuki_ghost_run_animation:
            pos (640, 360) anchor (0.5, 0.5) alpha 0
            parallel:
                ease 0.1 alpha 1.0
            parallel:
                ease 0.25 yoffset -500
        play sound natsuki_ghost_run
        pause 0.25

    stop music

    if qte_stage == 2:
        play sound stab

        scene red
        scene black with dissolve
        pause 0.2
        stop sound
        pause 0.5
    else:
        stop noise_1
        play sound ram_attack

        scene white
        scene black with dissolve
        pause 0.25

    python:
        phrases_n_a1_d12_qte_loss = (
        "ОЧНИ-И-ИСЬ!!!",
        "ПРИДИ В СЕБЯ!",
        "ХВАТИТ ПРОВАЛИВАТЬСЯ В СЕБЯ!",
        "ПЕРЕСТАНЬ ТУПИТЬ!",
        "ДЕЙСТВУЙ, ДАВАЙ!",
        "ВОЗЬМИ СЕБЯ В РУКИ!",
        "ЗАДАВИ СВОЁ ВООБРАЖЕНИЕ!"
        )

        phrase = random.choice(phrases_n_a1_d12_qte_loss)

    centered "{sc=4}[phrase]{/sc}"

    play sound flashback_end
    pause 0.382

    show white:
        alpha 0
        ease 0.25 alpha 1.0
    pause 0.25

    jump expression "nightmare_act_1_day_12_qte_" + str(qte_stage)
