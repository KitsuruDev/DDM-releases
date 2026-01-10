define audio.t6s1 = "<from 84.271 loop 43.572>bgm/6s.ogg"

default yuri_ghost_death = 0


# Глаза дракона
image yuri dragon:
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    repeat

# Левый глаз уходит налево
image yuri_oneeye = Composite((960, 960), (-1, -1), "yuri/oneeye.png", (-1, -1), "yuri_oneeye2")
image yuri_oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 4.0
    ease 100 xoffset -1000 yoffset 400

# Глючный спрайт с помехами
image yuri glitch:
    "yuri/glitch1.png"
    pause 0.05
    "yuri/glitch2.png"
    pause 0.05
    "yuri/glitch3.png"
    pause 0.05
    "yuri/glitch4.png"
    pause 0.05
    "yuri/glitch5.png"
    pause 0.05
    repeat

# Глючное лицо
image yuri glitch2:
    "yuri/0a.png"
    pause 0.05
    "yuri/0b.png"
    pause 0.05
    "yuri/0a.png"
    pause 0.05
    "yuri/0b.png"
    pause 0.05
    repeat


# Живые глаза и анимации дыхания и смеха под My Confession - Yuri ver.
layeredimage yuri_realistic_eyes:

    always "yuri/eyes1.png"

    group mouth:
        attribute mouth default:
            "yuri_realistic_mouth"

    group eyes:
        attribute eyes default:
            "yuri_realistic_pupils"

image yurimouth_close = "mod_assets/sprites/characters/yuri/yuri_eyes/mouth_close.png"
image yurimouth = "mod_assets/sprites/characters/yuri/yuri_eyes/mouth_open.png"

image yuri_realistic_mouth:
    alpha 0.0
    block:
        "yurimouth_close"
        pause 1.688
        alpha 1.0
        pause 3.076
        "yurimouth"
        pause 2.07
        alpha 0.0
        pause 1.604
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.2
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.06
        alpha 1.0
        pause 1.631
        alpha 0
        pause 0.718
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.2
        alpha 1.0
        pause 2.07
        alpha 0
        pause 0.974
        alpha 1.0
        pause 2.07
        alpha 0
        pause 0.437
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.28
        alpha 1.0
        pause 5.722
        "yurimouth_close"
        pause 1.355
        "yurimouth"
        pause 2.07
        alpha 0
        pause 0.974
        alpha 1.0
        pause 2.07
        alpha 0
        pause 0.557
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.192
        alpha 1.0
        pause 0.742
        "yurimouth_close"
        pause 2.4
        "yurimouth"
        pause 4.416
        alpha 0
        pause 1.2
        alpha 1.0
        pause 1.84
        alpha 0
        pause 1.2
        alpha 1.0
        pause 2.07
        alpha 0
        pause 0.392
        alpha 1.0
        pause 2.07
        alpha 0
        pause 0.929
        alpha 1.0
        pause 2.07
        alpha 0
        pause 1.586
        alpha 1.0
        pause 1.347
        "yurimouth_close"
        pause 1.585
        "yurimouth"
        pause 2.07
        alpha 0
        pause 1.162
        alpha 1.0
        pause 2.07
        alpha 0
        pause 3.232
        repeat

transform yuristeam_move:
    ease 0.1 alpha 0.5
    ease 0.797 xoffset -100 yoffset 30 alpha 0
    xoffset 0 yoffset 0

image yuristeam:
    "mod_assets/sprites/characters/yuri/yuri_eyes/steam.png"
    alpha 0
    block:
        pause 5.937
        yuristeam_move
        pause 2.777
        yuristeam_move
        pause 2.373
        yuristeam_move
        pause 1.794
        yuristeam_move
        pause 1.891
        yuristeam_move
        pause 2.373
        yuristeam_move
        pause 2.147
        yuristeam_move
        pause 1.61
        yuristeam_move
        pause 9.53
        yuristeam_move
        pause 2.147
        yuristeam_move
        pause 1.73
        yuristeam_move
        pause 5.062
        yuristeam_move
        pause 2.528
        yuristeam_move
        pause 1.142
        yuristeam_move
        pause 2.402
        yuristeam_move
        pause 1.784
        yuristeam_move
        pause 2.023
        yuristeam_move
        pause 5.925
        yuristeam_move
        pause 2.096
        yuristeam_move
        pause 3.435
        repeat

init python:
    def yuripupils_function(trans, st, at):           # объект, временная ось и временная ось анимации
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 1.3            # обязательная задержка в секундах перед повторным вызовом

    # https://stackoverflow.com/q/8949661
    def dying_words(phrase, loop):

        if not phrase or "." in phrase:
            if len(phrase) < 67:
                phrase += "."
            return phrase

        def get_chance():
            if loop < 460:           return 0.99
            elif 460 <= loop < 1060: return 0.85
            else:                    return 0.75

        def modify_word(word):
            if not word:
                return word

            if random.random() > chance:
                index_random = random.randint(0, len(word) - 1)
                word = word[:index_random] + word[index_random + 1:]
                r_char = random.choice(normal_char_rus) # Менять, если будет перевод в будущем
                word = word[:index_random] + r_char + word[index_random:]

                if loss_strength:
                    index_random_delete = random.randint(0, len(word) - 1)
                    word = word[:index_random_delete] + word[index_random_delete + 1:]

            return word

        words = phrase.split()
        loss_strength = (loop >= 1400)

        chance = get_chance()

        modified_words = [modify_word(i) for i in words]
        if loss_strength:
            modified_words = [w for w in modified_words if w]

        return " ".join(modified_words)


transform yuripupils_move:
    function yuripupils_function # постоянно вызывает функцию

image yuripupils_close = "mod_assets/sprites/characters/yuri/yuri_eyes/eyes_close.png"
image yuripupils: # наложены отдельно, чтобы спрайт не "корёжило"
    "yuri/eyes2.png"
    yuripupils_move

image yuri_realistic_pupils:
    "yuripupils_close"
    alpha 0
    block:
        pause 35.0
        alpha 1.0
        pause 1.421
        alpha 0
        pause 14.398
        alpha 1.0
        pause 1.0
        alpha 0
        pause 15.685
        alpha 1.0
        pause 1.346
        alpha 0
        pause 8.899
        repeat


transform yuri_realistic_eyes_move:
    pause 1.688
    block:
        ease 0.2 yoffset 3
        ease 0.2 yoffset -3
        repeat 3
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 6
    ease 0.1 yoffset 0
    pause 25.0
    block:
        ease 0.2 yoffset 3
        ease 0.2 yoffset -3
        repeat 9
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 6
    ease 0.1 yoffset 0
    pause 0.75
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 4
    ease 0.1 yoffset 3
    ease 0.1 yoffset 0
    pause 10.218
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 3
    ease 0.1 yoffset 0
    pause 4.231
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 3
    ease 0.1 yoffset 0
    pause 15.769
    block:
        ease 0.1 yoffset 3
        ease 0.1 yoffset -3
        repeat 5
    ease 0.1 yoffset 0
    pause 9.193
    repeat


# Юри, пронзённая ножом в сердце
layeredimage yuri_stab:

    always "yuri stab_6"

    group mouth:
        attribute mouth default:
            xoffset (1)
            "mod_assets/sprites/characters/yuri/yuri_stab/yuri_stab_6_mouth.png"

image yuri stab_6 = Composite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")
image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.1
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.1
        repeat
    parallel:
        2.0
        easeout 1.0 yoffset 7
        linear 3.0 yoffset 7
        easeout 1.0 yoffset 0
        0.5
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image natsuki ghost2 run = Composite((960, 960), (0, 0), "natsuki/ghost2.png", (390, 340), "n_rect", (480, 334), "n_rect")

transform natsuki_ghost_attack_dodge:
    parallel:
        easeout 1.0 zoom 3.0 yoffset 1500
    parallel:
        easeout 0.2 xpos 1000
        easeout 0.2 xpos 280
        repeat
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat


screen shot_natsuki_ghost_a1_nd12:
    button:
        area(590, 235, 40, 40)
        action [Play("sound", "mod_assets/sound/weapon/pistol/shot_single.mp3"), Return()]

    timer 1.0/40.0 repeat True action Function(RigMouse, 610, 255)




label nightmare_act_1_day_12:

    $ blocker = True
    $ blocker_key = "yuri_ghost"
    $ n_name = _("{glitch=15}{color=#000}Нацуки{/color}{/glitch}")
    $ y_name = _("{glitch=15}{color=#000}Юри{/color}{/glitch}")

    pause 1.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 5.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg club_day
    show darkred zorder 2:
        alpha 0.5
    with dissolve_scene_full
    call autosave
    mc "..."
    "Не помогла Сайори, значит..."
    "Тогда действуем."
    "Где эти сволочи?"
    mc "..."
    "Стойте, я снова пошевелиться не могу..."
    "Значит, это «фальшивая» Юри!"
    "Она научилась вводить моё тело в состояние паралича."
    "Тогда вопрос: где она?"
    "Сзади?"
    "Спереди-то её нет."
    y "Перестань волноваться..."
    y "Я чувствую, что ты пытаешься пошевелиться."
    show yuri turned anno cm e1a at l11
    pause 0.5
    show yuri om
    y "Хватит от меня убегать."
    show yuri worr om e1a
    y "Почему ты меня боишься?"
    show yuri oe rup
    y "Да, тогда я «сорвалась» из-за того, что ты пытался сбежать..."
    show yuri ce
    y "Сильно надавила на твой мозг, в результате чего ты потерял сознание."
    show yuri neut om e1d rdown
    y "Но я отнесла тебя обратно в класс и дала восстановиться."
    y "Сейчас ты уже в порядке."
    show yuri anno om e1a
    y "...но при этом всё ещё пытаешься сбежать."
    show yuri oe
    y "Как напуганный дикий зверь, которого усыпили, чтобы оказать помощь, а он, после дрёмы, просыпается и пытается удрать прочь."
    show yuri neut om e1d
    y "Но ты же человек."
    y "Ты выше этого."
    y "Неужели ты не хотел бы меня отблагодарить хотя бы тем, что оставался бы на месте?"
    show yuri cm
    "...какая потеря сознания?"
    "Какое восстановление?"
    "Что за дурдом?"
    show yuri om e1c
    y "Или отблагодарить...{w}другим способом..."
    show yuri flus om oe
    y "Здесь нет хотя бы того, о ком можно было бы позаботиться."
    show yuri lsur om oe
    y "Нет, Макс..."
    show yuri ce
    y "Я говорила, что ты один такой..."
    show yuri happ om oe
    y "Один...{w}мой..."
    show yuri ce
    y "И я очень хочу...{w}хочу..."
    show yuri yand om oe
    $ style.say_dialogue = style.edited
    y "ТЕБЯ!!!--{nw}"
    $ style.say_dialogue = style.normal
    window hide(None)
    $ quick_menu = False

    hide yuri
    show yuri dragon at i11
    pause 0.1
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound s_kill_glitch1
    pause 0.25
    hide yuri dragon
    hide screen tear_screen
    stop sound
    show yuri turned pani cm ce at i11

    $ quick_menu = True
    window show(None)
    show yuri om
    y "НЕТ, нельзя давать волю эмоциям!!!"
    show yuri vsur om ce lup rup
    y "Ух...{w}фу-у-ух..."
    show yuri nerv om oe
    y "Это...{w}я напугана не меньше тебя, ха-ха-ха..."
    show yuri cm ce
    y "Я должна сейчас успокоиться и сосредоточиться на сдержании тебя, чтобы мои припадки ушли прочь."
    show yuri neut om oe ldown rdown
    y "Поэтому...{w}побудем немного в тишине..."
    show yuri happ om e1a
    y "Смотря друг другу в глаза..."
    show yuri_oneeye at i11
    call window_close

    pause 10.0

    call window_open
    y "..."
    mc "..."
    y "..."
    y "...умф..."
    window hide(None)
    $ quick_menu = False

    play noise_1 interference
    hide yuri
    hide yuri_oneeye
    show yuri glitch at i11
    pause 0.75
    hide yuri glitch
    show yuri glitch2 at i11
    pause 1.5
    stop noise_1
    hide yuri glitch2
    show yuri turned happ cm oe at i11

    $ quick_menu = True
    window show(None)
    y "..."
    show yuri om
    y "Отлично, всё в порядке."
    show yuri ce
    y "Мои глаза меня же предают, хе-хе..."
    show yuri oe
    y "Всё-таки тяжело сдерживать бушующие внутри чувства."
    show yuri anno om oe lup
    y "Правда, не пойму, почему именно правый глаз так перенапрягается..."
    show yuri neut om e1d
    y "...для тебя он левый."
    show yuri anno om oe
    y "Возможно, всё из-за левого полушария моего мозга: то, что происходит внутри меня, не может поддаться логике, вот оно и «сбоит»..."
    show yuri happ om oe ldown
    y "...но это лишь мои догадки."
    show yuri ce
    y "И маленькая слабость, хе-хе-хе..."
    show yuri oe
    y "Ты же никому про неё не расскажешь?"
    show yuri cm
    "Кому интересен левый глаз образа Юри в кошма...{w}а-а-а...{w}ага..."
    "Только попробуй подойти ко мне поближе и потерять надо мной контроль..."
    mc "..."
    show yuri om ce
    y "Вот и прекрасно!"
    show yuri cm
    y "..."
    show yuri oe
    mc "..."
    y "..."
    show yuri neut cm e1d
    y "......"
    show yuri om
    y "Н-нет...{w}не могу удержаться..."
    show yuri happ om oe
    y "Я хочу быть ближе к тебе."
    show yuri e2a
    y "Смотреть на тебя."
    y "Ощущать твоё дыхание...{w}запахи..."
    y "Пусть хотя бы это утолит мой внутренний «ураган»."
    show yuri neut om e1d
    y "Т-только...{w}я должна кое-что сделать..."
    show yuri happ om oe
    y "Закрой глазки..."
    show yuri cm
    "Чёрт, я веки не могу контролировать."
    show yuri ce
    "Будто под какой-то тяжестью опускаются..."
    window hide

    scene black with dissolve_cg
    pause 0.5
    window auto
    mc "..."
    "...я чувствую...{w}как она стала ближе..."
    "Что ты, зараза, творишь..."
    "..."
    y "Д-да...{w}вот так..."
    mc "..."
    y "Всё...{w}я здесь...{w}перед тобой..."
    "Кажется, веки отпустило."
    call window_close
    call skip_block_on

    play music t10y fadein 3.0
    scene bg club_day
    show darkred zorder 3:
        alpha 0.5
    show yuri_realistic_eyes at yuri_realistic_eyes_move
    show yuripupils at yuri_realistic_eyes_move zorder 2:
        pause 35.0
        alpha 0
        pause 1.421
        alpha 1.0
        pause 14.398
        alpha 0
        pause 1.0
        alpha 1.0
        pause 15.685
        alpha 0
        pause 1.346
        alpha 1.0
        pause 8.899
        repeat
    show yuristeam zorder 2
    with dissolve_scene_full
    pause 4.0

    window auto
    "............"
    "Какого...{w}{b}ХРЕНА{/b}?!"
    $ style.say_dialogue = style.edited
    y "Наконец-то..."
    y "Это всё, что я хотела."
    y "Быть с тобой наедине вблизи..."
    y "Это так здорово, не правда ли?"
    y "А-ха-ха-ха!"
    y "Я теряю над собой контроль."
    y "Хотя знаешь что?"
    y "ПЛЕВАТЬ!"
    y "Я всё своё существование не чувствовала себя настолько хорошо!"
    y "Быть вплотную к тебе -- куда большее удовольствие, чем я могла себе представить."
    y "Потому что я связана с тобой."
    y "Настолько связана, что теперь не могу сделать и шаг в сторону."
    y "Будто я сразу умру, если ты только выйдешь из комнаты."
    y "Разве не замечательно, когда есть кто-то, кто так сильно заботится о тебе?"
    y "Тот, кто захочет посвятить тебе всю свою жизнь..."
    y "Это невообразимо приятное чувство."
    y "Почему я ему сопротивлялась?"
    y "Ведь это было бессмысленно."
    y "Оно нарастает с каждой секундой."
    y "И теперь оно СЛИШКОМ сильное."
    y "А сильное оно потому..."
    y "...что я люблю тебя, Макс!"
    y "Я очень безумно тебя люблю."
    y "Каждая клетка моего тела выкрикивает твой образ."
    y "Мне даже иногда хочется разорвать твою плоть, чтобы заползти во внутрь."
    y "Оставить там свои жидкости."
    y "Всю себя."
    y "Я хочу, чтобы ты принадлежал только мне."
    y "А я -- только тебе."
    y "Разве это не изумительно?"
    y "Скажи мне, Макс."
    y "Скажи, что хочешь стать моим возлюбленным."
    y "Скажи, что хочешь быть объектом моей любви."
    y "Прими моё признание."
    $ style.say_dialogue = style.normal
    "Вот и вскрылось всё дерьмо!"
    "Более чем уверен, что она меня не отпустит, а даже попробует изнасиловать или убить в попытке изнасилования..."
    "Чёрт, надо шевелиться!"
    $ style.say_dialogue = style.edited
    y "Ты принимаешь моё признание?"
    $ style.say_dialogue = style.normal
    "Какое, нахрен, признание?!"
    "Какая любовь?!"
    "Я даже говорить не могу!"
    "Хотя...{w}да, сейчас самое время!"
    "Я покажу тебе своё «признание»!"
    "Только...{w}чёртов паралич...{w}благо она обезумела, из-за чего ослабила контроль надо мной..."

    jump nightmare_act_1_day_12_qte_yuri_ghost



label nightmare_act_1_day_12_after_qte_yuri_ghost:
    stop music
    play sound stab
    show red:
        alpha 1.0
        ease 0.25 alpha 0
        1.85
        alpha 1.0
        ease 0.25 alpha 0
        1.85
        alpha 1.0
        ease 0.25 alpha 0
    pause 5.0

    scene bg class_day
    show darkred zorder 3:
        alpha 0.5
    show veins onlayer front:
        additive 0.5
    show yuri_stab at eyes:
        7.8
        easeout_cubic 0.5 yoffset 600
    show blood:
        pos (530, 585)
    with dissolve_cg
    pause 7.55
    hide veins onlayer front
    hide blood

    scene black
    play sound fall
    pause 4.0
    window auto
    $ style.say_dialogue = style.edited
    y "{cps=15}...зачем...{w}зачем ты это сделал?...{/cps}"
    window hide

    play music t6s1 fadein 3.0
    scene y_kill with dissolve_scene_full
    pause 1.0
    window auto

    $ yuri_ghost_phrase = "Зачем ты это сделал?"
    $ yuri_ghost_death = 0

    $ config.skipping = True
    $ config.allow_skipping = True
    $ preferences.skip_unseen = True

    label yuri_ghost_death_loop:
        $ yuri_ghost_death += 1

        if yuri_ghost_death < 200:
            y "[yuri_ghost_phrase]"
            jump yuri_ghost_death_loop

        elif yuri_ghost_death < 2450:
            $ yuri_ghost_phrase = dying_words(yuri_ghost_phrase, yuri_ghost_death)
            y "[yuri_ghost_phrase]"
            jump yuri_ghost_death_loop

        else:
            $ config.skipping = False
            $ config.allow_skipping = False
            $ preferences.skip_unseen = False
            jump nightmare_act_1_day_12_after_yuri_ghost_death


label nightmare_act_1_day_12_after_yuri_ghost_death:
    if cg_a1_d12_night_y.unlocked == False:
        $ cg_a1_d12_night_y.unlock()

    $ style.say_dialogue = style.normal
    "..."
    mc "..."
    "..."
    play sound closet_open
    pause 1.0
    "..."
    $ style.say_dialogue = style.edited
    n "..."
    n "...что..."
    n "...что ты...{w}сделал..."
    $ style.say_dialogue = style.normal
    mc "...то, что сделал."
    $ style.say_dialogue = style.edited
    n "...зачем?!"
    $ style.say_dialogue = style.normal
    mc "Самооборона."
    $ style.say_dialogue = style.edited
    n "УРОД!" with vpunch

    scene bg school old_class
    show darkred zorder 3:
        alpha 0.5
    show natsuki ghost_base at i11
    show n_rects_left zorder 2
    show n_rects_right zorder 2
    show n_rects_mouth zorder 2
    with dissolve

    $ yuri_ghost_death = 0

    n "ТЫ УБИЛ ЮРИ!!!"
    $ style.say_dialogue = style.normal
    mc "Это не Юри."
    mc "Это фальшивка моего мозга."
    $ style.say_dialogue = style.edited
    n "ТЫ.{w=1.0} УБИЛ.{w=1.0} ЮРИ!!!"
    $ style.say_dialogue = style.normal
    mc "Ты как вообще очнулась?"
    $ style.say_dialogue = style.edited
    n "Я её ненавидела, но она часть НАС!"
    n "ЧАСТЬ ТЕБЯ!"
    n "И ТЫ ЕЁ УБИЛ!!!"
    stop music fadeout 3.0
    $ style.say_dialogue = style.normal
    mc "Ты меня слушаешь?!"
    $ style.say_dialogue = style.edited
    hide n_rects_mouth
    n ghost2 "НО ТЫ МЕНЯ НЕ ПЕРЕИГРАЕШЬ!"
    n "Я УБЬЮ ТЕБЯ ЛОВКО И БЫСТРО!"
    play music confrontation_part_4 fadein 1.0
    $ style.say_dialogue = style.normal
    mc "Ах ты ж мразь!--{nw}"
    window hide(None)

    hide n_rects_left
    hide n_rects_right

    show natsuki ghost2 run at natsuki_ghost_attack_dodge
    play noise_2 natsuki_ghost_run
    pause 0.25

    jump nightmare_act_1_day_12_qte_natsuki_ghost



label nightmare_act_1_day_12_after_qte_natsuki_ghost:
    $ blocker_key = "natsuki_ghost"

    window auto
    stop noise_1
    scene bg school new_rooftop 2 day
    show monikamm_watch_a1_d12
    show darkred zorder 3:
        alpha 0.5
    show natsuki ghost2 at i11
    show n_rects_left
    show n_rects_right
    show layer master at stress(2.0, 0.5)
    with dissolve
    show pistol_idle zorder 2 with dissolve
    $ _history_list.clear()
    queue music confrontation_part_7
    mc "{sc=3}СТОЯТЬ!{/sc}"
    $ style.say_dialogue = style.edited
    n "Что, застрелишь меня?"
    $ style.say_dialogue = style.normal
    mc "{sc=3}Сомневаешься?!{/sc}"
    $ style.say_dialogue = style.edited
    n "ТАК ДАВАЙ, ЖМИ НА КУРОК!"
    n "УБЕЙ МЕНЯ!"
    $ style.say_dialogue = style.normal
    mc "{sc=3}......{/sc}"
    $ style.say_dialogue = style.edited
    n "Чего ты ждёшь?!"
    n "ТЫ ЖЕ УБИЛ ЮРИ!"
    n "ТАК УБЕЙ И МЕНЯ!"
    n "Или кишка тонка?!"
    $ style.say_dialogue = style.normal
    mc "{sc=4}Информация!{/sc}"
    mc "{sc=3}Мне нужна информация!{/sc}"
    mc "{sc=3}Нажать на курок ещё успею!{/sc}"
    mc "{sc=3}А вот вытащить из тебя информацию - нет!{/sc}"
    mc "{sc=2}Потому что ты тут единственная «при мозгах»!{/sc}"
    mc "{sc=2}Как раз сыграем в твою бестолковую игру,\nтолько поменявшись ролями!{/sc}"
    $ style.say_dialogue = style.edited
    n "Всё-таки переиграл..."
    n "...а теперь и уничтожишь..."
    $ quick_menu = True
    stop music fadeout 6.0
    show layer master
    with dissolve
    show n_rects_mouth
    n ghost_base "Ну и что же такому уроду, как ты, после всего случившегося вдруг захотелось узнать?"
    $ style.say_dialogue = style.normal
    mc "Много чего!"
    play music contact fadein 1.0
    mc "Во-первых, что творится с пространством?"
    mc "Пока я бегал по коридорам, я видел завалы из всякого мусора, которые закрывали мне проходы."
    mc "А потом эти завалы резко меняли своё местоположение."
    mc "И это я молчу про то, что когда я бежал вниз, то очутился на третьем этаже!"
    mc "А сейчас нас обоих вышвырнуло на крышу НОВОГО корпуса, когда мы были в СТАРОМ!"
    $ style.say_dialogue = style.edited
    n "Ты думаешь, я знаю?"
    n "Я здесь не главная."
    n "Я не могу никого и ничто контролировать."
    $ style.say_dialogue = style.normal
    mc "Тогда кто это делает?!"
    $ style.say_dialogue = style.edited
    n "Тот, кого мы все ненавидим."
    $ style.say_dialogue = style.normal
    mc "Я?!"
    $ style.say_dialogue = style.edited
    n "Пошёл ты со своим \"я\"!"
    n "Это..."
    n "..."
    $ style.say_dialogue = style.normal
    mc "Ну?!"
    $ style.say_dialogue = style.edited
    n "...я забыла."
    $ style.say_dialogue = style.normal
    mc "Что?!"
    $ style.say_dialogue = style.edited
    n "У меня только что были мысли, но их будто стёрли."
    n "Я только помню размытое чёрное пятно с белыми вкраплениями."
    n "А кто или что это -- выясняй сам, мне всё равно."
    n "Тебе же плевать, как тут оказался этот навороченный пистолет, который я вижу впервые?"
    n "Хотя я здесь всё вдоль и поперёк излазила."
    $ style.say_dialogue = style.normal
    mc "Ну охрененно..."
    "Неужели это та «чёрная Моника»?"
    mc "Второй вопрос: самый первый мой кошмар был не в школе, а в доме Сайори."
    mc "И там она висела в петле очень долгое время."
    mc "Я её даже пытался реанимировать искуственным дыханием."
    mc "Она тоже связана с вами или это отдельный кусок моего воображения?"
    $ style.say_dialogue = style.edited
    n "Она тоже была здесь."
    n "Но с нами давно не ладила."
    n "Постоянно жила в своём дурацком мирке, была «не от мира сего»."
    n "Однажды она отсюда ушла и не вернулась, но я не поняла, почему это произошло."
    $ style.say_dialogue = style.normal
    mc "Пятно?"
    $ style.say_dialogue = style.edited
    n "Может, и пятно."
    n "Но нам было плевать на Сайори, поскольку она перестала быть частью нас."
    $ style.say_dialogue = style.normal
    mc "Почему?"
    $ style.say_dialogue = style.edited
    n "Тупой или как?"
    n "Она полностью ушла в свою башку и стала постоянно ныть, как ей плохо!"
    n "Ныла-ныла, ныла-ныла!"
    n "Донылась, дура."
    n "Повешенье закономерно в её случае."
    $ style.say_dialogue = style.normal
    mc "Ну вы и гниль..."
    $ style.say_dialogue = style.edited
    n "...сказал урод, зарезавший Юри и держащий меня на мушке пистолета."
    $ style.say_dialogue = style.normal
    mc "В твоих глазах -- да, урод!"
    mc "Но теперь я точно уверен, что делаю всё правильно."
    $ style.say_dialogue = style.edited
    n "Ты разрушаешь свой мир...{w}и ты этому рад?"
    $ style.say_dialogue = style.normal
    mc "Лучше я разрушу его целиком, чтобы отстроить новый, чем пытаться что-то делать на этих гнилых обрубках."
    $ style.say_dialogue = style.edited
    n "Но ведь изначально тут всё было прекрасно."
    $ style.say_dialogue = style.normal
    mc "О, как раз третий вопрос: что тут было до всех этих кошмаров, раз вы «существовали» раньше?"
    $ style.say_dialogue = style.edited
    n "Обычный добрый мир с хорошими людьми и радугой на небе, блин."
    n "Если серьёзно, то мы все ладили, радовались, было всё прекрасно."
    n "А потом появился ТЫ и всё испортил!"
    n "Правда, ты валялся без сознания у себя дома очень долгое время."
    n "Ты был как кукла: просто лежал в кровати и не двигался."
    n "Я думала, что ты ни на что не сможешь повлиять в таком положении."
    n "Но всё получилось наоборот: именно с момента твоего появления всё пошло через жопу!"
    n "Грёбаная ирония..."
    $ style.say_dialogue = style.normal
    mc "...и каким образом я смог на вас повлиять, если я был «без сознания»?"
    $ style.say_dialogue = style.edited
    n "Поведение Юри забыл?"
    n "Она была без ума от тебя."
    n "Забила тобой всю голову, стала огрызаться на остальных."
    n "Она перестала уделять мне внимание, за что я её возненавидела."
    n "Сайори переживала, что мы тебя повредим."
    n "Она всячески останавливала любого, кто пытался к тебе подойти."
    n "И всё, чего она добилась, лишь оплеухи от Юри в свою сторону."
    $ style.say_dialogue = style.normal
    mc "А пятно?"
    $ style.say_dialogue = style.edited
    n "Да что ты со своим \"пятно\"?!"
    n "Пятно, уверена, всё знает!"
    n "А мы -- нет."
    if persistent.censorship == True:
        n "Мы, блин, обычные смертные."
    else:
        n "Мы, блять, обычные смертные."
    n "Потом кто-то тебя притащил в клуб."
    n "Я уверена, что это сделала Юри."
    n "И тогда я решила, что, может, ты не так уж и плох."
    $ style.say_dialogue = style.normal
    mc "Подожди, но я помню, что ты вела себя, как Нацуки из реальности."
    $ style.say_dialogue = style.edited
    n "Ты же сам вечно талдычешь: \"проекция мозга\" и \"кусок воображения\"."
    n "У меня в голове есть отрывки последних минут твоей жизни перед твоим сном."
    n "Самая «свежая» память."
    $ style.say_dialogue = style.normal
    mc "Выходит, вы знаете, когда я засыпаю?"
    $ style.say_dialogue = style.edited
    n "Верно."
    n "Иначе бы ты мог проснуться в помещении один и ничего бы с тобой не было."
    $ style.say_dialogue = style.normal
    mc "И мои пробуждения -- «потеря сознания» здесь?"
    $ style.say_dialogue = style.edited
    n "Да."
    $ style.say_dialogue = style.normal
    mc "А почему тогда вы не получаете память в реальном времени, когда я «без сознания»?"
    $ style.say_dialogue = style.edited
    n "Получаем."
    n "Только в разы слабее и хуже."
    n "Какофония шумов с картинкой в виде разноцветной мазни."
    n "Когда ты пробуждаешься, тогда мы будто ободряемся."
    n "И тогда твоя память становится невероятно чёткой."
    $ style.say_dialogue = style.normal
    mc "Как всё запутано, твою мать..."
    mc "Точно, ещё один вопрос!"
    mc "У меня был кошмар, где я находился в доме Моники."
    mc "И там на меня выпрыгнула она, но с белыми глазами."
    mc "Тоже «ваша»?"
    $ style.say_dialogue = style.edited
    n "Моника, точно...{w}мы так её прозвали."
    n "Но это не её имя."
    n "Но у неё никогда не было белых глаз."
    n "Они всегда были чёрные."
    n "Белой была только кожа."
    n "Настолько, что это режет глаза..."
    $ style.say_dialogue = style.normal
    mc "Тогда что это вообще было за существо?"
    $ style.say_dialogue = style.edited
    n "Наверное, здесь можно вставить твоё избитое слово \"проекция\"."
    n "Моника много что умеет."
    n "Постоянно нас усмиряла, когда были конфликты."
    n "И делала это больно, без единого прикосновения."
    n "А мы пытались её физически достать, каждый раз тщетно."
    n "Даже близко подойти не получалось."
    n "Только видно её силуэт издалека."
    if persistent.censorship == True:
        n "Сверлит мёртвым взглядом, сволочь."
    else:
        n "Сверлит мёртвым взглядом, сука."
    n "Каждый раз видеть её страшно."
    n "Сидишь в классе -- она в окнах двери, выходишь в коридор -- она в его конце."
    n "Остаётся только надеяться, что ты никак ей не помешал."
    n "Иначе начнёт снова ломать тебя, как печенье."
    n "Раньше была Юри, которая с ней могла бороться."
    n "Но из-за тебя я теперь одна."
    n "Одна с этой тварью."
    n "Она точно меня до смерти изведёт, либо придумает что-то хуже этого."
    n "Настоящий хоррор, из которого мне никогда не выбраться!"
    $ style.say_dialogue = style.normal
    mc "А почему вообще Моника чёрно-белая?"
    $ style.say_dialogue = style.edited
    n "Откуда мне знать?!"
    n "Она изначально такой была и никогда ничего про это не говорила."
    n "Она нам вообще ничего не говорила."
    n "Мы пытались с ней контактировать, но она быстро раздражалась."
    n "А потом сказала, как мы ей мешаем."
    $ style.say_dialogue = style.normal
    mc "Ясно..."
    mc "Что ж ты раньше такой «полезной» не была..."
    mc "Нормально же сейчас разговариваешь: без бестолковой абстракции."
    $ style.say_dialogue = style.edited
    n "Потому что я с тобой играла."
    $ style.say_dialogue = style.normal
    if persistent.censorship == True:
        mc "Играла она, блин..."
    else:
        mc "Играла она, блять..."
    mc "В здании, в котором есть опасное непонятное существо."
    $ style.say_dialogue = style.edited
    n "А что тут ещё остаётся?!"
    n "Я здесь всегда была одна...{w}в переносном смысле..."
    n "А ты глоток свежего воздуха."
    n "Хотя ты же всё и испортил..."
    $ style.say_dialogue = style.normal
    mc "Сама себе жизнь усложнила."
    mc "Всего лишь-то надо было сдерживать себя."
    $ style.say_dialogue = style.edited
    n "Посмотрела бы я на тебя, такого дохрена умного."
    n "Сам бы развалился и взвыл через неделю нахождения здесь."
    n "А мы тут торчим уже минимум 10 лет!"
    $ style.say_dialogue = style.normal
    mc "А как вы тогда выглядели, если в реальности я перевёлся в эту школу только пару недель назад?"
    $ style.say_dialogue = style.edited
    n "Я не помню."
    n "Очертания часто меняются и размываются."
    n "Иногда они чётче, иногда не очень."
    n "В голове они не задерживаются."
    $ style.say_dialogue = style.normal
    mc "А воспоминания?"
    $ style.say_dialogue = style.edited
    n "Антураж меняется вместе с ними, но действия остаются те же."
    n "Я это заметила, когда чётко запомнила прошлые мелкие предметы и строения помещений."
    $ style.say_dialogue = style.normal
    mc "Пф-ф-ф..."
    mc "Дурдом какой-то..."
    mc "Целый мир в башке..."
    $ style.say_dialogue = style.edited
    n "И ты его разрушаешь."
    $ style.say_dialogue = style.normal
    mc "Последний вопрос."
    mc "Если это МОЙ мир, то что будет, если ты меня...{w}«убьёшь»?"
    $ style.say_dialogue = style.edited
    n "Не знаю."
    n "Учитывая, что меня тут уже ничто не держит и я питаю к тебе за это ненависть..."
    n "...то получу удовлетворение как минимум."
    n "А остальное меня не волнует."
    $ style.say_dialogue = style.normal
    mc "И тем не менее ты упорно пытаешься поставить меня перед фактом разрушения мира мной же."
    mc "И убийства Юри, которую ты так ненавидишь."
    mc "У тебя что, есть мизерная надежда, что всё поменяется в светлую сторону?..."
    hide n_rects_mouth
    $ style.say_dialogue = style.edited
    n ghost2 "Нет, просто хочу, чтобы тебя совесть сожрала."
    n "Так я получу ещё больше удовольствия."
    $ style.say_dialogue = style.normal
    mc "Ну ты и мразь..."
    mc "Я думал, ты будешь лучше, но ты сгнила до основания."
    show n_rects_mouth
    $ style.say_dialogue = style.edited
    n ghost_base "..."
    $ style.say_dialogue = style.normal
    mc "Какое счастье, что я здесь не живу."
    mc "И какое счастье, что я вас больше никогда не увижу."
    mc "Не я виноват во всём этом."
    mc "Вы сами всё без меня разрушили."
    mc "Потому что надо уметь себя контролировать."
    if persistent.censorship:
        mc "А вы нихрена не умеете это делать, чёртовы инфантилы."
    else:
        mc "А вы нихера не умеете это делать, ёбаные инфантилы."
    mc "Поэтому пожрите сполна плоды своей тупости."
    stop music fadeout 2.0
    show natsuki_ghost_blood_animation zorder 2:
        pos (574, 252) zoom 0.80
    mc "Сайонара, ничтожество."
    call window_close

    show veins onlayer front:
        additive 0.5

    play noise_1 mc_exciting_heartbeat fadein 1.5
    $ default_mouse = "aim"
    pause 0.1

    call screen shot_natsuki_ghost_a1_nd12

    hide pistol_idle
    show pistol_shot:
        ease 0.09 xoffset 30 yoffset 20
    with Dissolve(0.09)

    stop noise_1
    $ default_mouse = "default"

    hide veins onlayer front

    scene black
    show white:
        alpha 1.0
        ease 0.25 alpha 0
    pause 0.25

    play music_none_loop confrontation_part_8 fadein 3.0

    call skip_block_off
    window auto

    $ blocker = False
    $ n_name = _("Нацуки")
    $ y_name = _("Юри")

    return
