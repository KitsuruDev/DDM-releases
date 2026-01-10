
# Глючная голова
image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat




label nightmare_act_1_day_11:

    $ blocker = True
    $ blocker_key = "yuri_ghost"
    $ y_name = _("{glitch=15}{color=#000}Юри{/color}{/glitch}")

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    pause 1.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 3.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg club_day
    show darkred zorder 2:
        alpha 0.5
    with dissolve_scene_full
    call autosave
    "..."
    "......"
    mc "...прекрасно."
    "Я снова в чёртовом кошмаре."
    mc "Грх-х-х..."
    "Ну хорошо, мозг, давай думать, что ты хочешь мне сказать через это вот всё."
    "Блин, самое мерзкое, что осозновать себя я могу прекрасно, а выйти из сна -- нет."
    "Это происходит произвольно."
    "..."
    mc "И что же я должен найти..."
    mc "Или кого дождаться?"
    "..."
    mc "Пха, конечно..."
    mc "Бумажка на парте."
    "Это какое-то излюбленное клише моего мозга?"
    play music t5yg fadein 3.0
    call show_poem(poem_yg, music=False, paper="images/bg/poem_y2.jpg")
    mc "НУ НАЧИНАЕТСЯ!"
    "Весь лист в дерьме и крови!"
    "А ещё этот почерк ОЧЕНЬ похож на почерк Юри..."
    "Мне что, теперь опять ждать её неожиданного прихода, чтобы с ней бороться?!"
    "Фу-у-у, у меня аж голова плыть начала..."
    "И паника почему-то образовалась..."
    "{sc=1.5}Да что со мной происходит?!{/sc}" with vpunch
    mc "{sc=2}Соберись, твою мать!{/sc}"
    "{sc=2}Нужно что-то найти для самообороны!{/sc}"
    if persistent.censorship:
        "{sc=3}БЛИН, ДА ХОТЬ СТУЛ В РУКИ!!!--{/sc}{nw}" with vpunch
    else:
        "{sc=3}БЛЯТЬ, ДА ХОТЬ СТУЛ В РУКИ!!!--{/sc}{nw}" with vpunch
    play sound closet_open
    pause 1.0
    stop music fadeout 1.0
    show yuri turned neut cm e2d at t11
    pause 1.0
    y "..."
    mc "..."
    "Почему...{w}я застрял?..."
    show yuri e2a
    y "..."
    mc "..."
    "Я ВООБЩЕ пошевелиться не могу!"
    "Причём дышать и смотреть по сторонам -- запросто!"
    show yuri om
    y "Я..."
    show yuri me
    mc "..."
    show yuri anno om oe
    y "Ой, чего это я..."
    show yuri flus cm e2a
    y "Д-давай начну с самого начала!"
    show yuri neut om e1d
    y "Я помню, как ты дрался со мной в постели."
    y "И ты тогда врезался головой о тумбочку..."
    show yuri e1b
    y "А я упала на пол."
    show yuri e4a
    y "В общем..."
    show yuri lsur om oe
    y "Я хочу извиниться."
    show yuri ce
    y "Да, прости, Макс."
    show yuri e1b
    y "Я слишком увлеклась своими...{w}«позывами»."
    y "Мне их тяжело контролировать, но ты и сам знаешь..."
    show yuri cm
    mc "..."
    show yuri happ om e1b
    y "А, вот и моё стихотворение!"
    show yuri cm at thide
    hide yuri
    pause 0.5
    y "Я надеюсь, ты его ещё не читал?"
    y "А то я этот стих тебе посветила, но ещё не дописала..."
    show yuri turned happ cm oe at t11
    pause 0.2
    show yuri om
    y "Не довела до идеала, так скажем."
    show yuri cm
    mc "..."
    show yuri lsur om oe
    y "Ой, точно!"
    show yuri neut om e1d
    y "Ты сейчас парализован, но безопасно."
    y "То есть ты не можешь ни задохнуться, ни упасть, ни получить каких-либо травм."
    show yuri cm
    "Ну спасибо..."
    show yuri curi om oe
    y "Но, возможно, ты задаёшься вопросом: \"А как так получилось?\""
    show yuri happ om ce lup rup
    y "Это я так научилась!"
    show yuri oe
    y "Здорово, правда?"
    show yuri cm
    "Чё?..."
    show yuri om e1b ldown rdown
    y "Просто я решила обезопасить нас обоих от случаев, похожих на нашу первую встречу..."
    show yuri oe
    y "Так я хотя бы буду концентрировать своё внимание на удержание тебя, чем на свои «позывы»."
    y "Иными словами, мы оба в выигрыше."
    show yuri cm
    "Да чёрта с два!"
    "Если я торчу здесь, значит, моя психика в глубокой жопе!"
    show yuri om ce
    y "Знаешь, как я очень счастлива?"
    show yuri oe
    y "Мы стоим здесь...{w}наедине...{w}и никто нам не помешает..."
    show yuri cm
    "Понятно, она сейчас опять попытается меня изнасиловать: если не физически, то морально..."
    show yuri neut om e1d
    y "И даже та розововолосая дурочка."
    show yuri cm
    "А?..."

    play music t9g
    show black zorder 3
    show yuri zorder 4:
        xpos 923 ypos 1750 zoom 2.0
    show y_glitch_head zorder 5:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    y "Она только и умеет, что ныть."
    y "Ничего, кроме нытья, от неё не дождёшься."
    y "Она постоянно говорит, как ей нужно внимание..."
    y "...и при этом не понимает, что таким поведением его же и отпугивает."
    y "Впрочем, кто будет переживать по этой соплячке?"
    y "Я, в отличии от неё, умею заботиться о других."
    y "Только...{w}только ты один у меня, Макс..."
    y "И я очень хочу о тебе позаботиться...{w}очень..."
    y "ОЧЕНЬ...{w}ХОЧУ..."
    $ style.say_dialogue = style.normal
    stop music
    play sound "sfx/stab.ogg"
    show blood_eye zorder 6:
        pos (750, 320) zoom 2.5
    pause 0.5
    stop sound
    hide black
    hide y_glitch_head
    hide blood_eye

    show blood_eye_rare zorder 6:
        pos (750, 320) zoom 2.0
    show yuri pani om ce
    y "Ой!"
    show yuri lup rup
    y "Ай!"
    show yuri mi
    y "Мой глаз..."
    show yuri happ om e1e
    y "П-прости, я тебя, наверное, напугала..."
    show yuri pani mi ce
    y "И себе боль причинила, ай-й-й..."
    show yuri neut om e1e
    y "М-мне надо быстренько отойти в санузел и привести себя там в порядок."
    show yuri b1b
    y "Только...{w}никуда не уходи..."
    y "Хорошо?"
    show yuri cm
    "Да-да-да, замечательно!"
    show yuri happ om ce -b1b
    y "Всё, вернусь через минутку!"
    show yuri cm
    hide blood_eye_rare
    hide yuri with easeoutleft
    pause 1.0
    play sound closet_open
    pause 2.0
    "......"
    mc "Пх-х-ха-а-а...."
    mc "Свобода!"
    "Наконец-то я могу пошевелиться!"
    mc "Так..."
    "Если я здесь останусь, то всё кончится плачевно."
    "Но тогда куда валить?..."
    "Если на другой этаж или в новый корпус, то это надо идти к центральной лестнице."
    "А рядом с ней чёртов санузел."
    "Крайняя правая лестница тоже не вариант: перекрыта из-за ремонта, если мой мозг решил досконально скопировать школу..."
    mc "Чёрт..."
    "Времени думать вообще нет!"
    "Тогда надо взять стул, чтобы неожиданно оглушить эту «Юри»."
    "..."
    mc "Какого..."
    "Они приклеены к полу?!"
    "Я вообще ничего не могу сдвинуть!"
    if persistent.censorship:
        mc "Да что за бред?!" with vpunch
    else:
        mc "Да что за херня?!" with vpunch
    "Тогда нет смысла здесь пытаться что-то взять."
    "Надо уже убираться отсюда!"

    scene black with wipeleft_scene
    "Придётся испытать удачу с центральной лестницей, но другого выбора нет..."
    call window_close

    pause 1.0
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show monikamm_watch_a1_d11
    show darkred zorder 2:
        alpha 0.5
    with wipeleft_scene
    "А дверь, значит, открывается..."
    "Ну, мозг, сволочь ты этакая..."
    "Всё, несёмся быстрыми и тихими шага--{nw}"
    "{sc=3}ПАРАЛИЗОВАЛО!!!{/sc}" with vpunch
    $ style.say_dialogue = style.edited
    y "Я же сказала НИКУДА НЕ УХОДИТЬ!!!{nw}"
    $ style.say_dialogue = style.normal
    call skip_block_on
    window hide(None)
    $ quick_menu = False

    hide darkred
    play noise_1 g1
    play noise_2 white_noise
    show bg glitch
    show yuri eyes_base zorder 2 at face:
        yanchor 0.5 ypos 0

    pause 1.0

    hide yuri eyes_base
    stop noise_1
    stop noise_2

    play noise_1 g2
    show screen bsod("ANALYSIS_ERROR", "FrontalLobe.dll")
    if renpy.windows and osVer >= (10, 0, 10240):
        pause 22.0
    else:
        call screen bsod_enter
    hide screen bsod
    stop noise_1

    play noise_1 critical_error
    play noise_2 white_noise
    show monikammm_cg_act_1_day_11 zorder 2
    show layer master:
        align (0.5, 0.5) zoom 1.2
        linear 0.01 rotate 5
        linear 0.01 rotate 0
        linear 0.01 rotate -5
        linear 0.01 rotate 0
        repeat
    pause 1.0
    stop noise_1
    stop noise_2

    call skip_block_off
    $ blocker = False
    $ y_name = _("Юри")

    return
