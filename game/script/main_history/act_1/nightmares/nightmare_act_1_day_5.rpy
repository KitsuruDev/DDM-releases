image splash_glitch:
    subpixel True
    "bg niigata street suburban 10 day"
    alpha 0.0
    0.5
    linear 0.5 alpha 1.0
    1.3
    linear 0.2 alpha 0.0
    "bg niigata park small path"
    linear 0.2 alpha 1.0
    1.0
    linear 0.2 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        1.0
        easeout 1.0 ypos -500

image splash_glitch_chibi_s1:
    subpixel True
    "gui/poemgame/s_sticker_2.png"
    right
    block:
        xoffset 0 yoffset -20
        linear 0.05 xoffset -20 yoffset -20
        repeat

image splash_glitch_chibi_s2:
    subpixel True
    "gui/poemgame/s_sticker_1.png"
    left
    block:
        xoffset 15 yoffset -50
        linear 0.07 xoffset 25 yoffset -15
        repeat

image splash_glitch_s3:
    subpixel True
    "mod_assets/sprites/sayori/art_sayori_plus.png"
    zoom 0.45 pos (0.5, 0.5)
    0.1
    parallel:
        pos (0.3, 1.2)
        linear 0.08 ypos 0.1
        repeat
    parallel:
        0.5
        alpha 0.0

image splash_glitch_s2:
    subpixel True
    "gui/menu_art_s.png"
    zoom 0.5
    0.2
    pos (0.8, 0.8)
    0.05
    pos (0.2, 0.7)
    0.05
    pos (0.4, 0.2)
    0.05
    pos (0.7, 1.2)
    0.05
    pos (0.1, 1.0)
    0.05
    pos (0.2, 0.6)
    0.05
    pos (0.9, 0.4)
    0.05
    alpha 0.0

image splash_glitch_s1:
    subpixel True
    "gui/menu_art_s.png"
    zoom 0.5 ypos 1.3
    block:
        xpos 0.85
        0.02
        xpos 0.81
        0.02
        repeat

transform artificial_breath:
    anchor (0.5, 0.5) pos (640, 360) zoom 1.0
    block:
        linear 0.3 zoom 3.0
        linear 1.0 zoom 1.0
        repeat 3



label nightmare_act_1_day_5:

    $ save_name = _("Акт 1 «Новая жизнь». День 6")

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black
    pause 1.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 5.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    mc "Пф-ф-ф..."
    "Просыпаться без будильника в выходной -- такое удовольствие..."
    "Но его сейчас нет."
    "Стоило только очнуться от дрёмы, как воспоминание о вчерашнем событии окунуло мозг волной дерьма."
    "..."
    mc "Вставай, давай..."
    mc "С каждой секундой Сайори и остальным всё хуже и хуже..."
    "За что мне всё это..."

    scene bg bedroom with dissolve
    pause 0.25
    mc "А-а-А-а-А, вспомнил!"
    "Сначала же нужно Монике отписаться..."
    mc "М-м-м..."
    "..."
    "......"
    "Сколько сейчас времени?"
    "..."
    "Примерно без 15-ти 9 утра..."
    mc "Выходной, мать вашу..."
    "..."
    mc "Ой, да пошло всё!"
    "Я хочу наведаться к Сайори ПРЯМО СЕЙЧАС."
    "Я не могу ждать, пока там Нацуки и Юри разберутся в своих недопониманиях."
    "Это может длиться как всё утро, так и полдня, если не день..."
    "Вы хотите, чтобы мы на это время забили на Сайори?"
    "А-ля не развалится и подождёт нас?"
    mc "Что за свинство!"
    mc "Я её друг или кто?!"
    "Поэтому к чёрту, потом Монике отпишусь."
    "Не знаю, спит ли Сайори сейчас, но я всё равно зайду к ней и побуду рядом."
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "Так, там окно закрыто, тут всё выключено, всё в порядке..."
    "Мобильник с собой."
    "Выходим..."
    call window_close

    scene black with dissolve
    pause 1.0
    play sound house_door_open
    play noise_3 street_suburban_noise fadein 3.0
    pause 1.227
    play noise_1 mc_steps_outside
    pause 2.0
    stop noise_1
    play sound house_door_close
    pause 2.0
    play noise_1 mc_steps_outside
    pause 4.0
    stop noise_1

    call window_open
    scene bg residential_day with dissolve_scene_full
    mc "Теплее, чем обычно..."
    "Ветра нет, а ещё тихо: улица вся пустая."
    "Не, ну а что?"
    "Суббота в спальном районе."
    "Хотя даже без прохладного ветерка у меня все пальцы на руках и ногах превратились в льдышки."
    "Бедная моя нервная система и организм..."
    "Развалюсь так и сдохну к годам 50-ти."

    scene bg house
    show monikamm_watch_a1_d5
    with wipeleft_scene
    "Теперь сердце колотится, как сумасшедшее..."
    "Чувствую приток адреналина."
    "В итоге во мне перемешались слабость и прилив сил."
    "Противное состояние..."
    "Всё, хватит ёрзать, соберись!" with vpunch
    "Состояние Сайори в наших руках по большей части."
    "Так...{w}где звонок..."
    call window_close

    pause 1.5
    play sound doorbell_sayori
    pause 4.0

    call window_open
    "..."
    "Снова никого."
    "Что-то тот поход в магазин вспомнился."
    "Блин, он был две недели назад..."
    "Куда время так несётся?"
    call window_close

    pause 0.6
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 4.0

    call window_open
    mc "Ну и?"
    "Где все?"
    "Что там происходит?"
    call window_close

    pause 5.0

    call window_open
    "Подождите..."
    "Калитка-то открыта."
    "Как я этого сразу не заметил?"

    scene black with wipeleft_scene
    "А входная дверь?"
    call window_close

    pause 0.5
    play noise_1 mc_steps_outside
    pause 3.0
    stop noise_1
    play sound house_door_open
    pause 1.227

    call window_open
    "Почему всё открыто нараспашку?"
    mc "Здравствуйте!"
    "..."
    "Тишина..."
    "Ладно, зайду так."
    call window_close

    stop noise_3 fadeout 4.0
    play noise_1 mc_steps_outside
    pause 2.0
    stop noise_1
    play sound house_door_close

    call window_open
    scene bg sayori house hallway day with dissolve_scene_full
    "Кроссовки сняты, можно и по дому пройтись."
    mc "Сайори?"
    "..."
    mc "Кто-нибудь?"
    "..."
    "Вообще ни единого звука."
    "Меня это начинает нервировать."
    "Где Сайори?"
    "Где её мать?"
    "Может, просто они спят?"
    "А двери..."
    "Их же никто не ограбил?"
    "Или Сайори сбежала непонятно куда?"
    "Если последнее -- правда, то это очень плохо."
    "Аргх, одни проблемы!"
    "Ладно, проверим сначала первый этаж."
    call window_close

    scene black with dissolve
    pause 1.0
    play noise_1 mc_steps_house
    pause 3.0
    stop noise_1
    pause 1.0

    call window_open
    scene bg sayori house livingroom day with dissolve
    mc "Сайори-и-и..."
    mc "Ау!"
    "..."
    "Да, давно я у неё в гостях не был..."
    "Как будто прихожая ни капли не поменялась с момента моего последнего посещения."
    "Хотя что тут менять?"
    "Всё и так цивильно."
    mc "Опа..."
    "Что там за левым диваном на полу валяется?"
    "..."
    "Лист помятый какой-то..."
    "Небось упал со шкафа, или кто-то рассыпал несколько штук, а этот поднять забыл."
    "Вроде бы такой порядок везде..."
    "Ой, ладно, подниму его на диван."
    "Хотя...{w}что там?"
    "Интересно же!"
    "Но если что-то личное или связанное с документами, то, конечно, не буду вглядываться."
    call show_poem(poem_s_nightmare, music=False)
    mc "Какого..."
    "Что это такое?!"
    "Нет...{w}нет-нет-нет...{w}не могут же мои дурные мысли перед сном стать реальностью."
    "Они же утрированы донельзя!"
    "Тогда почему Сайори написала это?..."
    mc "...да что за тупой вопрос?"
    mc "Её сжирают негативные мысли, очевидно!"
    "А в совокупности с накруткой на себя...{w}тем более..."
    mc "Так, стоп."
    "Здесь на бумаге что-то просвечивается с обратной стороны..."
    call window_close

    play sound page_turn
    show drawing_sayori_nightmare with Dissolve(1.0)
    $ plot_pause()
    hide drawing_sayori_nightmare with Dissolve(0.5)
    pause 0.5

    call window_open
    if persistent.censorship:
        mc "Чёрт..."
    else:
        mc "Блять..."
    mc "Нет, это уже ненормально!"
    mc "{sc=3}САЙОРИ!!!{/sc}" with vpunch
    "..."
    "Опять эта долбаная тишина!"
    "Надо срочно проверить её спальню, на 100 процентов уверен, что она там убивается от раздутого горя."
    call window_close

    scene black with dissolve
    pause 1.0
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1

    call window_open
    mc "Угх..."
    "Сердце сейчас пробьёт мне грудь насквозь..."
    "Руки потрясываются..."
    "Никогда меня так ещё не штырило от волнения."
    play sound door_knock
    pause 1.8
    mc "Сайори!"
    mc "Это я, можно войти?"
    "..."
    mc "Я знаю, что вчера тебе было больно..."
    mc "И сейчас тоже."
    mc "А я стоял столбом и ничего не сделал, чтобы остановить конфликт."
    mc "Но это не значит, что я буду сидеть сложа руки."
    mc "Я хочу проведать тебя, Сайори."
    mc "Мне плохо от того, что плохо тебе, поэтому не могу это так оставить."
    mc "Я не хочу, чтобы ты страдала."
    "..."
    mc "Сайори?..."
    "Ай, да плевать, чем она там занимается!"
    "Хоть голой посреди комнаты стоит."
    "Мне важно знать, что с ней происходит после всего случившегося!"
    "Я открою эту чёртову дверь!"
    call window_close

    call skip_block_on
    play sound closet_open
    scene white with dissolve
    pause 0.5

    window auto
    mc "Сайори--{nw}"
    window hide

    if cg_a1_d5_night_s.unlocked == False:
        $ cg_a1_d5_night_s.unlock()

    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear_screen
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 4
    show s_kill2_zoom zorder 4
    show s_kill_zoom_trans zorder 4
    pause 3.0
    show noise zorder 4:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 4:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show splash_glitch zorder 2
    pause 0.5
    show sayori turned happ cm oe school_bag zorder 3 at t41
    pause 0.2
    show sayori om oe
    pause 0.2
    show sayori cm oe
    pause 0.2
    show sayori om ce
    pause 0.2
    show sayori cm ce
    pause 0.2
    show sayori om ce lup rup at h41
    pause 0.2
    show sayori cm ce ldown rdown at t41
    pause 0.1
    show sayori cm ce
    hide sayori
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear_screen
    pause 0.1
    show sayori turned shirt happ om oe zorder 3 at t44
    pause 0.1
    show sayori cm oe
    pause 0.1
    show sayori nerv om oe rup at s44
    pause 0.1
    show sayori cm oe rdown
    pause 0.1
    show sayori happ cm oe lup at t44
    pause 0.1
    show sayori om oe
    pause 0.1
    show sayori cm oe ldown
    pause 0.1
    show sayori om ce
    pause 0.1
    show sayori cm ce at thide
    hide sayori
    pause 1.0
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear_screen
    pause 1.0
    hide splash_glitch
    show splash_glitch_chibi_s1 zorder 2
    show splash_glitch_chibi_s2 zorder 2
    show splash_glitch_s3 zorder 2
    show splash_glitch_s2 zorder 2
    show splash_glitch_s1 zorder 2
    pause 0.75
    hide splash_glitch_chibi_s1
    hide splash_glitch_chibi_s2
    hide splash_glitch_s3
    hide splash_glitch_s2
    hide splash_glitch_s1
    pause 0.25
    show splash_glitch_chibi_s1 zorder 2
    show splash_glitch_chibi_s2 zorder 2
    show splash_glitch_s3 zorder 2
    show splash_glitch_s2 zorder 2
    show splash_glitch_s1 zorder 2
    pause 0.2
    hide splash_glitch_chibi_s1
    hide splash_glitch_chibi_s2
    hide splash_glitch_s3
    hide splash_glitch_s2
    hide splash_glitch_s1
    pause 6.0

    window auto
    $ style.say_dialogue = style.edited
    "{cps=40}ТВОЮ МААААААААААААААААТЬ!!!{/cps}{nw}"
    $ style.say_dialogue = style.normal
    window hide

    play sound narrative_fast_changing
    pause 0.25
    scene white zorder 4 with dissolve

    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        yoffset 0 zoom 1
        parallel:
            block:
                easein 0.15 yoffset 20
                easeout 0.15 yoffset 0
                easein 0.15 yoffset -20
                easeout 0.15 yoffset 0
                repeat
        parallel:
            linear 2.5 zoom 3 xoffset 400
            linear 2.5 zoom 5 xoffset 400

    play sound mc_steps_house_run
    show s_kill_bg zorder 5
    show s_kill zorder 6:
        truecenter
        align (0.315, 0.550) anchor (0.5, 0.5) zoom 0.75
    pause 2.0
    scene black with dissolve
    pause 1.0

    show layer master

    stop sound

    window auto
    "{sc=3}НАДО РАЗРЕЗАТЬ ВЕРЁВКУ!{/sc}"
    "{sc=3}ГДЕ НОЖ?!{/sc}"
    "{sc=3}ГДЕ ЧТО-ТО ОСТРОЕ?!{/sc}"
    "{sc=3}СТОЛ САЙОРИ!{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}В-ВОТ!{/sc}"
    mc "{sc=3}Я СХВАТИЛ ТЕБЯ!{/sc}"
    mc "{sc=3}ДЕРЖИСЬ!!!{/sc}"
    window hide

    play sound rope_cut
    pause 6.672

    window auto
    mc "{sc=3}АРГХ!{/sc}"
    "{sc=3}БАНТ ВЫЛЕТЕЛ!{/sc}"
    "{sc=3}ПЛЕВАТЬ!{/sc}"
    mc "{sc=3}КЛАДЁМ ТЕБЯ НА ПОЛ!{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}ЧЁРТ, ПЕТЛЯ НА ШЕЕ!{/sc}"
    window hide

    play sound rope_cut
    pause 6.672

    window auto
    mc "{sc=3}ГОТОВО!!!{/sc}"

    scene bg sayori house carpet
    show sayori turned pajamas neut mg e0a trail_rope at e11
    with dissolve
    "{sc=3}НАДО ПРОВЕРИТЬ ПУЛЬС!{/sc}"
    "{sc=3}...{/sc}"
    "{sc=3}......{/sc}"
    show vignette zorder 2:
        alpha 0
        linear 10 alpha 0.25
    mc "{sc=3}ГДЕ ОН?!{/sc}"
    "{sc=3}ПОЧЕМУ ЕГО НЕТ?!{/sc}"
    "{sc=3}НУЖНО ИСКУССТВЕННОЕ ДЫХАНИЕ!{/sc}"
    "{sc=3}РОТ ПУСТОЙ, ПИЖАМУ НАДО РАССТЕГНУТЬ!{/sc}"
    "{sc=3}...{/sc}"
    mc "{sc=3}ЕСТЬ!{/sc}"

    show layer master at artificial_breath
    "{sc=3}РАЗ!{w=1.25} ДВА!{w=1.25} ТРИ!{w=1.0}{/sc}{nw}"

    scene black with dissolve
    "{sc=3}ВЫДОХ!{/sc}"

    scene bg sayori house carpet
    show sayori turned pajamas neut mg e0a trail_rope at e11
    show vignette zorder 2:
        alpha 0.25
        linear 4.0 alpha 0.5
    with dissolve
    show layer master at artificial_breath
    "{sc=4}РАЗ!{w=1.25} ДВА!{w=1.25} ТРИ!{w=1.0}{/sc}{nw}"

    scene black with dissolve
    "{sc=4}ВЫДОХ!{/sc}"

    scene bg sayori house carpet
    show sayori turned pajamas neut mg e0a trail_rope at e11
    show vignette zorder 2:
        alpha 0.5
        linear 4.0 alpha 0.75
    with dissolve
    show layer master at artificial_breath
    "{sc=5}РАЗ!{w=1.25} ДВА!{w=1.25} ТРИ!{w=1.0}{/sc}{nw}"

    scene black with dissolve
    "{sc=5}ВЫДОХ!!!{/sc}"

    scene bg sayori house carpet
    show layer master at stress
    show sayori turned pajamas neut mg e0a trail_rope at e11
    show vignette zorder 2:
        alpha 0.75
        linear 4.0 alpha 1.0
    with dissolve
    mc "{sc=5}ПУЛЬСА НЕТ!!!{/sc}"
    mc "{sc=5}ЕГО НЕТ!!!{/sc}"
    mc "{sc=5}ПОЧЕМУ ЕГО НЕТ?!{/sc}"
    mc "{sc=5}ОН ДОЛЖЕН БЫТЬ!!!{/sc}"
    mc "{sc=5}ПОЧЕМУ?!{/sc}"
    mc "{sc=5}ПОЧЕМУ ТЫ МЕРТВА?!{/sc}"
    mc "{sc=5}НЕТ!!!{/sc}"
    mc "{sc=6}НЕТ!!!{/sc}"
    mc "{sc=7}НЕ-Е-ЕТ!!!{/sc}"
    mc "{sc=5}ЗА ЧТО?!{/sc}"
    mc "{sc=5}ЗАЧЕМ?!{/sc}"
    mc "{sc=5}САЙОРИ!!!{/sc}"
    mc "{sc=5}ПОЧЕМУ?!{/sc}"
    mc "{sc=5}ПОЧЕМУ-У-У?!{/sc}"
    mc "{sc=5}АААААААААААААААААА--{/sc}{nw}"
    window hide

    play sound mc_nausea
    pause 0.3

    window auto
    "{sc=6}ТОШНОТА!!!{/sc}" with vpunch
    window hide

    scene black with wipeleft_scene
    play noise_1 mc_steps_house_run
    pause 2.0
    stop noise_1
    play sound closet_open
    pause 2.0
    play sound mc_vomiting
    pause 12.233
    play sound toilet
    pause 5.4

    window auto
    "{cps=20}Надо...{w}вернуться...{w}к ней!...{/cps}"
    mc "{cps=20}С-Cайори...{/cps}"
    mc "{cps=20}Пожалуйста...{w}скажи что-нибудь...{/cps}"
    "{cps=20}...{/cps}"
    mc "{cps=30}Пожалуйста!...{/cps}"
    "{cps=20}...{/cps}"
    mc "{cps=30}Я ХОЧУ услышать, что ты ЖИВА-А-А!{/cps}"
    mc "{cps=30}ХОЧУ услышать снова твоё хихиканье!{/cps}"
    mc "{cps=30}СА-А-АЙО-О-ОРИ-И-И!{/cps}"
    "{cps=20}...{/cps}"
    mc "{cps=30}ПОЧЕМУ ТЫ МЕРТВА-А-А?!{/cps}" with vpunch
    mc "{cps=30}ПО-О-ОЧЕ-Е-ЕМУ-У-У?!{/cps}"

    scene bg sayori house carpet
    show layer master at stress
    show sayori turned pajamas neut mg e0a trail_rope at e11
    show vignette zorder 2
    show vignette as flicker zorder 3 at vignetteflicker
    with dissolve
    mc "{sc=3}ТЫ.{w} ДОЛЖНА.{w} ЖИ-И-ИТЬ!{/sc}"
    mc "{sc=3}РАДОВАТЬ ВСЕХ!{/sc}"
    mc "{sc=3}МЕНЯ!{/sc}"
    mc "{sc=3}ТЫ НУЖНА МНЕ!{/sc}"
    mc "{sc=4}САЙОРИ!!!{/sc}"
    mc "{sc=5}ТЫ...{/sc}"
    show layer master at stress(3)
    mc "{sc=2}...нужна...{w}мне...{/sc}"
    window hide
    stop music fadeout 1.0
    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        zoom 1.0
        linear 1.0 zoom 4.0

    scene black with dissolve
    play sound hugs
    pause 2.0

    $ save_name = episode.replace('\n', '. ')
    call skip_block_off

    return
