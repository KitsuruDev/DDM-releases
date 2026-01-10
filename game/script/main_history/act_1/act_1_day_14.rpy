
label act_1_day_14:

    stop noise_1
    stop noise_2
    stop noise_3

    scene bg bedroom at mc_bed
    with Dissolve(0.15)
    pause 0.05
    with shake(dist=40)
    window show
    if persistent.censorship:
        mc "{sc=3}ЧЁРТ!!!{/sc}" with vpunch
    else:
        mc "{sc=3}БЛЯТЬ!!!{/sc}" with vpunch
    mc "{sc=1}А-а-а-а-а, голова...{/sc}"
    mc "{sc=0.5}...{/sc}"

    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        zoom 1.0 xoffset 0 yoffset 0
        ease 1.25 zoom 1.1
        parallel:
            ease 0.1 xoffset -4
            ease 0.1 xoffset 4
            ease 0.1 xoffset 0
        parallel:
            ease 0.1 yoffset -4
            ease 0.1 yoffset 4
            ease 0.1 yoffset 0
        0.9
        parallel:
            ease 0.1 xoffset -8
            ease 0.1 xoffset 8
            ease 0.1 xoffset 0
        parallel:
            ease 0.1 yoffset -8
            ease 0.1 yoffset 8
            ease 0.1 yoffset 0
        0.85
        parallel:
            ease 0.1 xoffset -24
            ease 0.1 xoffset 24
            ease 0.1 xoffset 0
        parallel:
            ease 0.1 yoffset -24
            ease 0.1 yoffset 24
            ease 0.1 yoffset 0
        0.85
        parallel:
            ease 0.1 xoffset -72
            ease 0.1 xoffset 72
            ease 0.1 xoffset 0
        parallel:
            ease 0.1 yoffset -72
            ease 0.1 yoffset 72
            ease 0.1 yoffset 0
        0.85
        parallel:
            ease 0.1 xoffset -72
            ease 0.1 xoffset 72
            ease 0.1 xoffset 0
        parallel:
            ease 0.1 yoffset -72
            ease 0.1 yoffset 72
            ease 0.1 yoffset 0
        0.6
        block:
            0.35
            parallel:
                ease 0.1 xoffset -72
                ease 0.1 xoffset 72
                ease 0.1 xoffset 0
            parallel:
                ease 0.1 yoffset -72
                ease 0.1 yoffset 72
                ease 0.1 yoffset 0
            repeat 6

    if persistent.censorship:
        mc "{sc=0.5}Тварь...{/sc}{w=1.0}{nw}"
        play sound hit_wood volume 0.2
        mc "{sc=1.0}Тварь...{/sc}{w=0.9}{nw}"
        play sound hit_wood volume 0.4
        mc "{sc=1.5}Тварь.{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 0.6
        mc "{sc=2.0}Тварь!{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 0.8
        mc "{sc=2.5}Тварь!!!{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 1.0
        mc "{sc=3.0}ТВАРЬ!!!{/sc}{w=0.8}{nw}"
    else:
        mc "{sc=0.5}Сука...{/sc}{w=1.0}{nw}"
        play sound hit_wood volume 0.2
        mc "{sc=1.0}Сука...{/sc}{w=0.9}{nw}"
        play sound hit_wood volume 0.4
        mc "{sc=1.5}Сука.{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 0.6
        mc "{sc=2.0}Сука!{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 0.8
        mc "{sc=2.5}Сука!!!{/sc}{w=0.8}{nw}"
        play sound hit_wood volume 1.0
        mc "{sc=4.0}СУКА!!!{/sc}{w=0.8}{nw}"
    window hide

    python hide:
        for i in range(5):
            renpy.play(audio.hit_wood, channel="sound")
            renpy.pause(0.65)
        renpy.play(audio.hit_wood, channel="sound")

    play phone_sound new_message_mc
    pause 0.5

    show layer master at stress
    window auto
    if persistent.censorship:
        mc "{sc=4.0}КОГО ТАМ, НАХРЕН, РАЗОБРАЛО?!{/sc}"
    else:
        mc "{sc=4.0}КОГО ТАМ, БЛЯТЬ, РАЗОБРАЛО?!{/sc}"

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 43
        clock = (8, 34)

    phone register "mc_s_chat":
        time year 2018 day 29 month 4 hour 8 minute 34
        "s" "С добрым утром!\n(> ω <)"

    phone discussion "mc_s_chat"
    pause 1.0
    mc "{sc=4.0}А-А-А-А-А, САЙОРИ!!!{/sc}"
    mc "{sc=4.0}САЙОРИ!!!{/sc}"
    mc "{sc=3.0}Да, это Сайори!!!{/sc}"
    mc "{sc=2.0}Это Сайори!{/sc}"
    mc "{sc=1.0}Сайори!...{/sc}"

    phone end discussion transition

    mc "{sc=0.5}Это Сайори...{/sc}"
    window hide

    $ nightmare_active = False

    play sound none_transition
    scene black
    show screen new_day(episode)
    pause 4.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d13.unlocked == False:
        $ ach_a1_d13.unlock()
        pause 7.0
    else:
        pause 3.0

    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    mc "Ещё лоб себе рассёк, твою ж ты..."
    play phone_sound new_message_mc
    pause 1.0
    call skip_block_on

    phone register "mc_s_chat":
        "s" "Я сегодня пойду гулять с родителями"

    phone discussion "mc_s_chat"
    $ plot_pause()
    phone discussion "mc_s_chat":
        "s" "Не хочешь с нами?"
    $ phone.system.clock = (8, 35)
    phone discussion "mc_s_chat":
        "mc" "Я только проснулся"
        "s" "Как раз успеешь приготовиться!"
        "mc" "Нет, Сайори, извини, но откажусь"
        "mc" "Я обещал сегодня сопроводить Нацуки до госпиталя"
        "s" "Ааааа точно!"
        "s" "Совсем про её походы забыла!"
        "s" "А вы уже успели договориться?!"
        "mc" "Да, пока вы вчера по магазинам бегали"
        "s" "Хехе... (* ^ ω ^)"
        "s" "А! Как спалось?"
        "mc" "Никак"
        "mc" "Не поменялось ничего"
    $ phone.system.clock = (8, 36)
    phone discussion "mc_s_chat":
        "s" "Опять кошмар?!"
        "mc" "Да"
        "mc" "Умудрился себе лоб поцарапать"
        "mc" "Надо будет сдвинуть эту дурацкую тумбочку подальше, пока я себя не прибил окончательно"
        "s" "Ужас!"
        "s" "Не сильно ушибся?!"
        "mc" "Нет, только небольшой синяк и царапина"
        "s" "Не нужно тебя забинтовать?!"
        "mc" "Сайори, не переживай"
        "mc" "Пластырь себе наклею и всё будет ок"
        "s" "Никакой не ок!"
        "s" "У тебя кошмары до сих пор прекратиться не могут!"
        "mc" "Зато теперь я осознал их корень"
    $ phone.system.clock = (8, 37)
    phone discussion "mc_s_chat":
        "mc" "Осталось только от него избавиться"
        "s" "И что же это?!"
        "mc" "Долго рассказывать, но если в двух словах, то кошмары для меня -- теперь не кошмары"
        "mc" "Они у меня больше не испуг вызывают, а мотивацию покончить с ними раз и навсегда"
        "s" "Прикольно но будто у тебя крыша едет...\n(_ _*)"
        "mc" "Да если бы, Сайори..."
        "mc" "Тут всё очень сложно и запутанно, и только я могу всё это решить"
        "s" "Ясненько..."
        "mc" "Ладно, не унывай, проблема потихоньку решается"
        "s" "Эх"
        "s" "Тогда хорошенько сегодня отдохни!"
        "mc" "И ты тоже!"
        "s" "Пока-пока! (> ω <)"

    phone end discussion transition

    call skip_block_off
    mc "Пф-ф-ф..."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg residential_day with wipeleft_scene
    mc "Фух, свежий воздух..."
    "Наконец-то стал потихоньку приходить в себя."
    "Мне надо...{w}переварить всю эту дурь...{w}хотя половина кошмара уже полностью выветрилась."
    mc "Так."
    "Пока время есть, лучше отсижусь где-то в спокойном месте, а потом уже Нацуки напишу."
    "Не хочу в выбитом состоянии что-либо делать, иначе всё пойдёт наперекосяк."

    scene bg niigata street suburban 10 day with wipeleft_scene
    "..."

    scene bg niigata street suburban 11 day with wipeleft_scene
    "......"

    scene bg niigata street suburban 12 day with wipeleft_scene
    mc "А вот и тихая площадка..."
    "..."
    "......"
    mc "Теперь у меня никакие мысли не лезут."
    mc "..."
    mc "Лишь адреналин и желание порвать эту мразь только при одном её образе..."
    if persistent.censorship:
        mc "С-с-сволочь..."
    else:
        mc "С-с-сука..."
    mc "..."
    mc "Но если откинуть всю эту ненависть..."
    mc "...неужели я реально такой?"
    mc "Да, я не любил людей, особенно видя их пороки и всякую дурь..."
    mc "Справедливости ради, и себя тоже, иногда так мерзко становится за своё поведение и эмоции, что плеваться хочется."
    mc "...но чтобы НАСТОЛЬКО всё ненавидеть?"
    mc "..."
    mc "И почему это я должен кидать Литературный клуб?"
    mc "Не, ну серьёзно!"
    mc "В кои-то веки у меня появился шанс на новую жизнь, на друзей, на общение и даже на девушку..."
    mc "Почему я должен всё терять?"
    mc "\"Моника улетит в Америку, а с остальными ты общаться перестанешь, бла-бла-бла...\""
    mc "Как будто ничего не поменяется, ага."
    mc "Как будто мы ничего не придумаем, ага."
    mc "\"Потому что мы тупые подростки, бэ-хэ\"..."
    mc "Если честно, то позиция...{w}как её, мрази...{w}Моникаммм, а...{w}крайне инфантильная."
    mc "Подростковая, короче."
    mc "Почему?"
    mc "Да потому что сплошные удары в крайности!"
    mc "Что за идиотизм?"
    mc "Почему какой-то образ в голове решил, что для меня лучше?"
    mc "Почему я должен выполнять хотелки хрен пойми какой дуры из разряда «потому что потому»?!"
    mc "Почему бы тебе просто не пойти в задницу?!"
    mc "Потому что Я ТАК ЗАХОТЕЛ!"
    mc "И МНЕ РЕШАТЬ, что делать в МОЕЙ жизни!"
    mc "Почему никто на других не наезжает и все живут прекрасно?"
    mc "Почему тех, на кого НУЖНО наехать, вы игнорируете, а на таких, как я, которые и так всё делают правильно, начинаете капать на мозги и вечно гадить?!"
    if persistent.censorship:
        mc "Что за хрень?!"
        mc "Пошли ещё раз в задницу!"
    else:
        mc "Что за херня?!"
        mc "Пошли ещё раз в жопу!"
    mc "Твари..."
    mc "..."
    mc "......"
    mc "Блин..."
    mc "Неужели я...{w}такой же агрессивный, как Моникаммм..."
    mc "..."
    mc "Может быть, я смогу от неё избавиться путём контроля над собой."
    mc "Хотя я и так пытаюсь контролировать себя каждый день, куда ещё больше-то?"
    mc "Или этого недостаточно..."
    mc "Чёрт, не понимаю."
    mc "..."
    mc "По крайней мере, теперь у меня есть «живой пример», как не надо себя вести."
    mc "Если я обнаружу в себе что-то общее с этим «примером», то меня начнёт с этого тошнить."
    mc "А это уже прогресс."
    mc "Но этого явно недостаточно, чтобы избавиться от этого дерьма..."
    mc "..."
    mc "И в кошмарах особо ничего не сделаешь, потому что она всё контролирует."
    mc "...если все её слова про кошмары -- правда."
    mc "А может, блеф?"
    mc "И ничего она контролировать не может, ни создавать, ни конструировать?"
    mc "Или не блеф, ведь она говорила всё так уверенно..."
    mc "Да ничерта я не знаю."
    mc "Тут всё запутанно-перепутанно, так ещё покрыто многослойной запутанностью вперемешку с дерьмом от всего и вся."
    mc "Но как бы то ни было..."
    mc "Всё, что я могу сейчас сделать, -- это не быть, как Моникаммм."
    mc "И пытаться ей сопротивляться абсолютно любыми способами."
    mc "Убить она меня точно не сможет, хотя почувствовать «физическую» боль я от неё могу..."
    mc "Лишь бы она не переросла в настоящую, как этот пластырь, блин..."
    mc "Интересно: если я могу чувствовать боль, то могу ли умереть от её большого количества?"
    mc "Хотя если быть реалистом, то всё это -- эффект самовнушения."
    mc "Самое опасная и уязвимая часть человека."
    mc "Одного эксперимента, который я видел в Интернете, про лимоны хватает, чтобы это осознать."
    mc "Не помню, как там конкретно было, но были люди, у кого имелась аллергия на лимоны."
    mc "Им давали мармеладные дольки в форме лимона, врали им, что они содержат что-то там из лимона."
    mc "Потом после то ли съедания, то ли нюха у них начиналась аллергия."
    mc "Далее им давали раствор с якобы лекарством от их аллергии (естественно, это была просто обычная вода)."
    mc "И как только они выпивали стакан с водой, то от их аллергии ничего не оставалось."
    mc "То есть, вдумайтесь, их мозг искренне думал, что в мармеладе были вещества из лимона."
    mc "И он послал сигнал организму этому сопротивляться."
    mc "А потом ещё «самовылечился» обычной водой из-за того же эффекта самовнушения."
    mc "Потрясающий орган, а?"
    mc "А теперь представьте, сколько можно «понавесить» на него лишнего или заставить что-то сделать..."
    if persistent.censorship:
        mc "Это же бардак полный."
    else:
        mc "Это же пиздец полный."
    mc "Не человеческое тело, а дурацкий набор органов..."
    mc "..."
    mc "...твою мать."
    mc "Не...{w}не-не-не..."
    mc "Надо избавляться от Моникаммм."
    mc "Иначе эта тварь мне всю жизнь искалечит своим тупым взглядом на жизнь."
    play phone_sound new_message_mc
    pause 1.0
    mc "Блин, Нацуки, что ли?"
    mc "Кажется, я слишком заболтался, но зато мне стало в разы легче."
    call skip_block_on

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 43
        clock = (9, 15)

    phone register "mc_n_chat":
        time year 2018 day 29 month 4 hour 9 minute 15
        "n" "Ну что, спишь ещё не?"

    phone discussion "mc_n_chat"
    $ plot_pause()
    phone discussion "mc_n_chat":
        "mc" "Уже на улице прохлаждаюсь"
        "mc" "С добрым утром, кстати"
        "n" "Да, утречка"
    $ phone.system.clock = (9, 16)
    phone discussion "mc_n_chat":
        "n" "Двигай на перекрёсток, оттуда пойдём пешком до станции Ниигата"
        "mc" "Опять пешком до туда?"
        "mc" "Не проще ли на автобусе?"
        "n" "У тебя так много лишних денег?"
        "mc" "Окей, значит ещё раз прогуляемся"
        "n" "Ты только карту на проезд не забудь"
        "n" "А то тебе придётся гулять через весь город"
        "mc" "Ага, ещё чего"
        "mc" "На загривке тебя туда-обратно нести?"
        "n" "Ну если ты так предлагаешь..."
    $ phone.system.clock = (9, 17)
    phone discussion "mc_n_chat":
        "mc" "Иди-ка ты... На перекрёсток уже"
        "n" "Хахаха"

    phone end discussion transition

    call skip_block_off
    mc "Почему только твой отец не может оклейматься и навестить твою маму?"
    mc "Вместе с тобой..."
    mc "..."
    mc "Все вы на голову двинутые."
    mc "И я тоже."
    call window_close

    call plot_transition

    call window_open
    scene bg niigata street suburban 11 day with wipeleft_scene
    "Уже пару минут тут стою, а её всё нет."
    "Её дом не так-то и далеко, а прошло уже примерно 7 минут с разговора, где её носит?"
    "А может быть, у неё там что-то с отцом..."
    mc "Отец-отец, блин."
    mc "А ведь серьёзно, я пока не видел ни одного случая насилия с его стороны."
    mc "Пусть и не увижу никогда, нам и так проблем хватает..."
    n "{size=19}Что ты там бормочешь?{/size}"
    mc "Ну наконец-то!"
    show natsuki turned black_shirt fc laug om oe lhip rhip at t11
    n "А, соскучился?--{nw}"
    show natsuki pani om oe ldown rdown at h11
    n "Эй-эй-эй, это что за пластырь в полбашки?!"
    show natsuki cm
    mc "Он размером с палец вообще-то."
    show natsuki om lhip rhip
    n "Да какая разница?!"
    show natsuki md
    call window_close

    hide natsuki
    show natsuki turned black_shirt fc pout cm oe lhip rhip at el11
    with dissolve
    pause 0.5

    call window_open
    show natsuki om
    n "Ты когда лоб поранить успел?!"
    show natsuki md
    mc "Не надо тыкать в мой пластырь, Нацуки!"
    mc "Успокойся!"
    call window_close

    hide natsuki
    show natsuki turned black_shirt fc pout md oe at i11
    with dissolve
    pause 0.5

    call window_open
    mc "Я в тумбочку врезался во время сна."
    show natsuki om
    n "Как ты так умудрился?..."
    show natsuki md
    mc "Ну..."
    mc "Кошмар."
    show natsuki curi md oe
    mc "Помнишь, пару дней назад рассказывал?"
    show natsuki om e1b
    n "А..."
    show natsuki cm
    mc "...вот."
    show natsuki pout om oe lhip rhip
    n "Что ж ты такой «больной»?"
    show natsuki md
    mc "Ну не здоровый, да."
    show natsuki curi om oe
    n "Может, тебя в тот же госпиталь положить?"
    n "Они как раз на мозге специализируются."
    show natsuki md
    mc "Ещё чего."
    show natsuki neut cm oe
    mc "Так, всё, пошли уже, хватит время тратить."
    show natsuki om e1b ldown rdown
    n "Пошли-пошли."
    show natsuki cm

    scene bg niigata street suburban 15 day
    show natsuki turned black_shirt fc neut cm e1c at t11
    with wipeleft_scene
    show natsuki oe
    mc "Ты, кстати, вчера зареклась про 17 скорых, когда у тебя отец в полиции работал."
    show natsuki curi om oe
    n "...и?"
    show natsuki md
    mc "Э-э..."
    "А что я тут скажу?"
    "Что бы я ни ответил, это буквально влезание не в своё дело."
    show natsuki neut cm oe
    mc "Просто не помню у нас в Японии такого случая..."
    show natsuki om e1b rhip
    n "Это было ещё в 2008 году."
    n "10 лет назад."
    show natsuki cm
    mc "А, ну тогда понятно."
    show natsuki oe
    mc "В то время у меня «выхода» в Интернет не было."
    show natsuki om e1b
    n "Ха, такая же ситуация..."
    show natsuki cm
    mc "И что же такое случилось, что столько скорых вызвали?"
    show natsuki curi om oe rdown
    n "...ты реально хочешь это узнать?"
    show natsuki md
    mc "Я уже столько начитался и насмотрелся, что теперь сильно не удивлюсь."
    show natsuki dist om ce lhip rhip
    n "Ну раз сам захотел, значит слушай."
    show natsuki cm

    scene bg niigata street urban 1 day
    show natsuki turned black_shirt fc neut cm e1b rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Мой папа работал в токийской полиции, отвечал за район\nЧиё{image=accent_high_register}{space=-15}да."
    n "И у него было всё прекрасно."
    show natsuki oe
    n "...по словам мамы."
    show natsuki curi om e1b rdown
    n "Я просто те времена смутно помню."
    show natsuki neut om e1b lhip
    n "И в злополучный день у папы был вызов."
    show natsuki b1d
    n "В квартале Акихаба{image=accent_low_register}{space=-15}ра какой-то человек с ножом стал кидаться на окружающих."
    show natsuki -b1d
    n "Папа приехал туда вместе со своими напарниками."
    show natsuki ldown rhip
    n "Местный патруль уже ловил сумасшедшего, а папа принялся помогать пострадавшим."
    n "Не знаю, насколько всё было плохо, но тогда вызывали эти 17 скорых."
    show natsuki flus cm oe
    n "А ещё...{w}несколько людей умерло, когда папа пытался им помочь..."
    show natsuki md
    mc "Твою мать..."

    scene bg niigata street urban day 2
    show natsuki turned black_shirt fc neut cm oe b1d lhip rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Ну и естественно это оставило на нём крайне сильное впечатление."
    show natsuki anno om ce -b1d
    n "Бзик у него случился: нас защитить захотел."
    show natsuki cross black_shirt ff vang om oe
    n "В более маленьком городе в разы безопаснее, чем в мегаполисе, тьфу!"
    show natsuki sad om oe
    n "У нас денег много было, у меня всё было хорошо..."
    show natsuki angr om oe
    n "...а сейчас проблема на проблеме, так ещё и самому папе плохо, а мама из-за него в аварию попала!"
    n "Хорошо ещё жива осталась, иначе бы я..."
    show natsuki cm
    n "..."
    show natsuki neut cm e2b b1d
    n "..."
    show natsuki anno cm ce -b1d

    scene bg niigata street urban day 3
    show natsuki turned black_shirt fc angr cm oe lhip rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Чем он вообще думал?!"
    show natsuki cm
    mc "Явно это был порыв эмоций..."
    show natsuki om e1b b1d ldown
    n "Порыв эмоций..."
    show natsuki oe brow lhip
    n "Контролировать себя надо уметь!"
    show natsuki cm
    mc "..."
    show natsuki e2b b1d
    "Чёрт побери, опять дежавю с Моникаммм..."
    show natsuki om
    n "Мне уже надоело каждый раз слышать возмущения и крики от родителей!"
    n "Пока мама была дома и папа был более буйным, они чуть ли не каждый день конфликтовали!"
    show natsuki oe
    n "Неужели так тяжело было нормально поговорить?!"
    show natsuki cross black_shirt ff vang om ce brow
    n "Будто им нравилось кричать друг на друга!"
    n "Нервов же никаких не хватит, сгорят все до основания!"
    show natsuki cm
    mc "Так, Нацуки, На-цу!"
    call window_close

    hide natsuki
    show natsuki cross black_shirt vang cm ce at el11
    with dissolve
    pause 0.5

    call window_open
    show natsuki ce
    mc "Я понимаю все твои возмущения и боль, но давай ты тоже не будешь скатываться в крики."
    "Надеюсь, поглаживания по голове на ней сработают..."
    show natsuki oe
    "На Сайори и Юри сработали же?"
    show natsuki om
    n "Да мне просто уже надое--{nw}"
    show natsuki cm
    show natsuki n3 with dissolve
    pause 0.5
    show natsuki anno mj ce
    n "--ф-ф-ф-ф-ф..."
    "Так-то лучше."
    "Теперь и с Нацуки корень проблемы окончательно прояснился..."
    "Только сейчас надо её успокоить."
    mc "Подожди-ка."
    call window_close

    hide natsuki
    show natsuki turned black_shirt curi cm oe at i11
    with dissolve
    pause 0.5

    call window_open
    mc "Выходит, ты была богаче меня?"
    show natsuki fc laug ma oe n1
    mc "Потому что То{image=accent_high_register}{space=-15}кио -- офигеть какой недешёвый город."
    show natsuki om lhip rhip
    n "Ха, зависть проснулась?"
    show natsuki ma
    mc "Просто любопытство."
    show natsuki neut om oe
    n "Даже если я и была богатой, то совершенно это не ощущала."
    show natsuki b1d ldown
    n "И вообще, я же говорила, что плохо помню то время!"
    n "Я тогда только начальную школу заканчивала."
    show natsuki cm
    mc "А-а..."
    show natsuki om
    n "Я же родилась в 1999 году!"
    show natsuki cm
    mc "Понял я, понял."
    show natsuki brow rdown
    mc "Стой..."
    show natsuki curi md oe
    mc "А в какой период?"
    show natsuki om
    n "В середине осени."
    show natsuki lhip rhip
    n "К чему твой вопрос?"
    show natsuki md
    mc "Ты старше меня на несколько месяцев?!"
    show natsuki lsur cm oe
    n "..."
    show natsuki laug om oe
    n "...подожди, ха-ха-ха, что?"
    show natsuki cm
    mc "Какой ужас..."
    show natsuki om ce
    n "Ха-ха-ха!"
    show natsuki cm
    mc "Мда, а по тебе вообще не скажешь..."
    show natsuki om oe
    n "Подумаешь, я тебе головой в грудь упираюсь!"
    show natsuki cm
    mc "Ага, зато как..."
    show natsuki om ce
    n "Теперь я тебе авторитет, ха-ха-ха!"
    show natsuki cm
    "Фух, соскочили с негативной темы."

    scene bg niigata street urban day 4
    show natsuki turned black_shirt fc happ cm oe at t11
    with wipeleft_scene
    show natsuki om
    n "А ты-то сам откуда?"
    show natsuki lhip rhip
    n "Уж если я поделилась, то и сам расскажи!"
    show natsuki neut cm oe
    mc "Из Морио{image=accent_low_register}{space=-15}ки."
    show natsuki curi om oe
    n "Из Мори...{w}что?"
    show natsuki md
    mc "Мориока."
    mc "Город в центре префектуры Ива{image=accent_low_register}{space=-15}тэ."
    show natsuki ldown
    n "?..."
    mc "Ну, под префектурой Аомо{image=accent_low_register}{space=-15}ри."
    show natsuki cm e1b b1f
    n "У-у-у..."
    mc "Ё-моё, Нацуки..."
    show natsuki md oe brow
    mc "Префектура Аомори на краю перед островом Хокка{image=accent_low_register}{space=-15}йдо."
    mc "Префектура Иватэ под Аомори."
    show natsuki neut cm oe
    mc "А город Мориока в центре Иватэ."
    show natsuki me rdown
    n "А-а-а..."
    show natsuki om
    n "Я за префектуры не особо шарю."
    show natsuki cm
    mc "Как будто у меня это прекрасно выходит, ага."
    show natsuki e1b b1a

    scene bg niigata street urban day 5
    show natsuki turned black_shirt fc curi md oe lhip at t11
    with wipeleft_scene
    show natsuki om
    n "И чего это тебя в Ниигату занесло?"
    show natsuki md
    mc "Да у родителей дом здесь был."
    mc "Точнее, и сейчас есть, я в нём живу."
    show natsuki om
    n "А откуда у них тут дом взялся?"
    show natsuki md
    mc "Родители хотели переселить меня в более...{w}лучшие условия."
    show natsuki neut cm oe ldown
    mc "Куда-то южнее, где больше доступной инфраструктуры и тому подобное."
    mc "Они перебрали множество вариантов, связанных с жильём, но везде было дорого."
    mc "Однако они наткнулись на этот вот дом."
    mc "Он был катастрофически дешёвым."
    show natsuki curi md oe rhip
    mc "Ай, как бы понятнее объяснить..."
    mc "Ты слышала про госпрограмму, связанную с заброшенным жильём?"
    mc "Что, типо, его раздают по дешёвке, чтобы люди из мегаполисов перебирались в районы для восполнения их населения."
    show natsuki om e1b b1f
    n "...да, что-то такое видела в новостных пабликах..."
    show natsuki oe brow
    n "А-а-а, а{image=accent_low_register}{space=-15}кийя, точно."
    show natsuki md
    mc "Ага."
    mc "Этот дом был заброшен, по документам там уже никто не числился."
    show natsuki neut cm oe
    mc "Мои родители положили на него глаз, поскольку здесь очень доступная инфраструктура."
    mc "Отец сразу нанял специалистов для проверки дома на повреждения и конструкцию."
    mc "Мало ли какой мог быть подвох: от развалившегося фундамента до отсутствия защиты от землетрясений."
    mc "Но специалисты сказали, что всё отлично, даже есть уровень сейсмоустойчивости «та{image=accent_low_register}{space=-15}йшин»."
    mc "Самый минимальный, но вполне обычный для маленьких домов."
    mc "В нём всего лишь требуется, чтобы толщина балок и прочих элементов конструкции была минимальной для выдерживания землестрясения."
    mc "Короче, моему отцу всё равно пришлось немного отремонтировать дом в некоторых местах, и всё -- можно было заселяться."
    show natsuki om
    n "И когда вы его приобрели?"
    show natsuki cm
    mc "Да год назад где-то."
    mc "Вот только жить не сразу начал: переехал только недавно."
    mc "Не помню: говорил я это тебе или нет..."
    show natsuki om e1b rhip
    n "Да я тоже что-то забыла..."
    show natsuki oe
    n "Ладно, а покупка с кем заключается?"
    show natsuki cm
    mc "С представителями-продавцами администрации Ниигаты."
    mc "Есть специальное приложение по продаже таких домов, там как раз и контакты продавцов имеются."
    show natsuki rdown
    n "Хм."
    mc "И вот, насчёт проживания: в договоре аренды было условие, что покупатели дома или представители их семьи должны в нём сразу жить после приобретения."
    mc "Однако родители договорились, что я перееду в него, когда буду учиться в местной школе."
    mc "Ну и всё в таком духе."
    show natsuki lhip
    mc "Со скрипом продавцы согласилась."
    mc "Потом ещё с бюрократией было много мороки."
    mc "А потом ещё подача документов в школу..."
    mc "Фу."
    mc "И вот пару недель назад я наконец-то переехал сюда окончательно."
    mc "А родители остались в квартире в Мориоке, где там же и работают."
    show natsuki om
    n "Прикольно..."
    show natsuki cm
    mc "А то."
    mc "Это реально чудо, что такой дом попался и его никто не выкупал."
    show natsuki om e1b b1a
    n "Если бы ещё электричество с водой были супер-дешёвыми..."
    show natsuki cm
    mc "Да вроде цены, которые я видел краем глаза, не сильно кусаются."
    show natsuki om oe b1d rhip
    n "Моему папе влетает по кошельку, знаешь ли?"
    show natsuki cm
    mc "Да знаю я ваше материальное положение, знаю..."
    show natsuki om brow
    n "Стой-ка!"
    show natsuki curi om oe
    n "У вас дом в аренде, а не куплен целиком?"
    n "Или ты оговорился?"
    show natsuki md
    mc "...да, этот дом именно в аренде."
    show natsuki om
    n "Обычной покупки вообще нет?"
    show natsuki md
    mc "Есть, конечно, но нас интересовал только этот дом."
    show natsuki om
    n "И когда он станет полностью твоим?"
    show natsuki md
    mc "Прямо так интересно?"
    show natsuki worr om oe
    n "А вдруг я тоже захочу приобрести какой-нибудь домик..."
    show natsuki cm
    mc "Я уже понял, что тебе просто любопытно."
    show natsuki sad om e1a
    n "Ну так скажи!"
    show natsuki md
    mc "Сейчас, подожди, сколько там было в договоре прописано..."
    show natsuki neut cm oe
    mc "..."
    show natsuki pani cm oe
    mc "...а, 10 лет аренды, после чего дом становится собственностью покупателя."
    show natsuki om ldown rdown at h11
    n "ЧЕГО?!"
    show natsuki md
    mc "Ха-ха-ха, а ты думала, что тебе даром отдадут дом в личную собственность?"
    show natsuki pout md oe
    mc "Ничего так просто в этой жизни не даётся."
    show natsuki om e1b b1b
    n "Ужас..."
    show natsuki cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 train_moving_3 fadein 3.0
    scene bg train zorder 1
    show train_window_niigata zorder 0
    show natsuki turned black_shirt fc neut cm e1b b1a zorder 2 at i22:
        ypos 800 zoom 0.9
    show layer master:
        align (0.5, 0.5) anchor (0.7, 0.55) zoom 1.7
    with wipeleft_scene
    "Значит, нам до Коба{image=accent_low_register}{space=-15}ри ехать: всего 4 станции..."
    "Не так далеко, как я думал."
    show natsuki oe brow
    mc "{size=19}Тут довольно пусто, на удивление...{/size}"
    show natsuki om
    n "{size=19}Потому что воскресенье.{/size}"
    show natsuki e1b b1a
    n "{size=19}Видел бы ты, какие тут толпы шарятся в рабочие дни...{/size}"
    show natsuki cm
    mc "{size=19}Верю.{/size}"
    "Да, в куче людей легко найти ненормального..."
    "Как там у нас прозвали, когда мужик лапает девушек в толпе...{w}а, тика{image=accent_low_register}{space=-15}н."
    "А если этим занимается женщина, то тидзё{image=accent_low_register}{space=-15}."
    "Что тот мразь, что эта мразь."
    show natsuki e4a
    "И эти мрази такие, что никак не изведутся."
    "Уже на разных станциях развесили плакаты про тюремное наказание за этот людской идиотизм, но даже это их не останавливает."
    "Это насколько должна быть хреновая психика из-за различных причин, что люди до такого опускаются?"
    "Про сталкеров и тем более маньяков я вообще молчу."
    "И если уж на то пошло, то это касается всех подобных преступлений и прочей грязи, которые люди совершают из-за своих эгоистичных желаний."
    "Сколько наказаний не вводи, даже смертных, они всё никак не успокоятся."
    "Интересно, а вот если бы всё, что связано с половыми органами, было бы...{w}болезненным или не приносило бы удовлетворения?"
    "То есть, не было бы никаких гормонов и прочего бардака..."
    show natsuki oe brow
    "Это сколько бы тогда извращённого дерьма исчезло?"
    "Не говоря уже о демографической катастрофе и деградации всего, что у нас называют любовью, а также--{nw}"
    show natsuki om
    n "{size=19}Я, кстати, видела, как ты в основном тусуешься с Моникой.{/size}"
    show natsuki cm
    mc "{size=19}...?{/size}"
    show natsuki om
    n "{size=19}У вас что-то есть?{/size}"
    show natsuki cm b1d
    mc "{size=19}К чему вообще твой вопрос?{/size}"
    show natsuki om
    n "{size=19}Скажу после твоего ответа.{/size}"
    show natsuki cm
    mc "{size=19}...{/size}"
    show natsuki om b1f
    n "{size=19}Значит, есть, да?{/size}"
    show natsuki cm brow
    mc "{size=19}Чёрт побери, да.{/size}"
    mc "{size=19}И дальше что?{/size}"
    show natsuki dist om oe
    n "{size=19}Я просто сейчас думала насчёт Юри.{/size}"
    show natsuki curi om oe
    n "{size=19}Ты же знаешь, что она в тебя втюрилась?{/size}"
    show natsuki md
    mc "{size=19}Уже как неделю.{/size}"
    show natsuki dist om oe
    n "{size=19}Я ей обещала помочь приблизиться к тебе.{/size}"
    show natsuki sad om oe
    n "{size=19}И теперь понимаю, что зря согласилась.{/size}"
    show natsuki ce
    n "{size=19}И я не знаю, что с этим делать.{/size}"
    show natsuki cm
    mc "{size=19}Кажется, мы все в Юри влипли...{/size}"
    show natsuki om oe
    n "{size=19}Мда уж...{/size}"
    show natsuki cm
    "..."
    show natsuki pout om oe
    n "{size=19}Ты же ещё ищешь психолога?{/size}"
    show natsuki md
    mc "{size=19}Да, ищу его каждый день, блин.{/size}"
    mc "{size=19}Уже заколебался.{/size}"
    mc "{size=19}Ника не помню, времени прошло хоть и не супер много, но достаточно, чтобы «потеряться».{/size}"
    mc "{size=19}Такое ощущение, что я трачу время впустую.{/size}"
    show natsuki om
    n "{size=19}Может, всё-таки наскребём денег на «живого» психолога?{/size}"
    show natsuki md
    mc "{size=19}Кто-то мне недавно писал, что у нас нет лишних денег на автобус.{/size}"
    show natsuki sad cm oe
    n "{size=19}...{/size}"
    show natsuki om
    n "{size=19}Хотя я предлагала Юри попросить Монику об оплате, но её родители не согласятся на такое...{/size}"
    show natsuki cm
    mc "{size=19}Да, её отец точно не согласится.{/size}"
    show natsuki curi om oe
    n "{size=19}Почему именно отец?{/size}"
    show natsuki md
    mc "{size=19}Я с ним вчера познакомился.{/size}"
    show natsuki neut om oe
    n "{size=19}А-а, всё, понятно.{/size}"
    show natsuki e1b b1a
    n "{size=19}Вот почему ты вчера после похода не ушёл домой сразу.{/size}"
    show natsuki cm
    mc "{size=19}Угу.{/size}"
    show natsuki oe brow
    mc "{size=19}И мне этой встречи хватило по горло.{/size}"
    show natsuki om
    n "{size=19}Я слышала, что он не мягкий.{/size}"
    show natsuki lsur cm oe
    mc "{size=19}Он меня нахрен послал.{/size}"
    mc "{size=19}Не открытым текстом, окольными словами, но послал.{/size}"
    show natsuki om
    n "{size=19}За что он тебя так невзлюбил?{/size}"
    show natsuki cm
    mc "{size=19}Хочет забрать Монику в Америку после окончания школы.{/size}"
    show natsuki neut cm oe
    mc "{size=19}Чтобы она там построила свою карьеру.{/size}"
    mc "{size=19}Я думаю, ты сама понимаешь, что наши новоиспечённые отношения он...{w}мягко говоря, не принял.{/size}"
    show natsuki om
    n "{size=19}...Моника про Америку нам ничего не рассказывала.{/size}"
    show natsuki e1b b1a
    n "{size=19}Хотя какая разница, всё равно отвратительная ситуация выходит.{/size}"
    show natsuki cm
    mc "{size=19}Ага.{/size}"
    mc "{size=19}Все мы в полной заднице.{/size}"
    show natsuki oe brow
    mc "{size=19}Одной лишь Сайори со всем повезло, и на том спасибо.{/size}"
    show natsuki om
    n "{size=19}У Котонохи тоже всё окей.{/size}"
    show natsuki cm
    mc "{size=19}Ну, уже хотя бы у двоих людей из пяти...{/size}"
    "..."
    show natsuki e1b b1a
    n "{size=19}...{/size}"
    mc "{size=19}...{/size}"
    show natsuki e2a b1a
    mc "{size=19}...а может, найти Юри парня?{/size}"
    show natsuki b1d
    mc "{size=19}Мне как-то Монику эту идею подкинула, я её сначала отверг, но сейчас это не очень-то и плохой вариант...{/size}"
    show natsuki om
    n "{size=19}С ума сошёл?{/size}"
    n "{size=19}Где мы его искать будем?{/size}"
    show natsuki cm
    mc "{size=19}Не знаю, в Интернете, например.{/size}"
    show natsuki om oe
    n "{size=19}Это надо, чтобы он жил в Ниигате, был адекватным, принял проблемы Юри и полюбил её вообще!{/size}"
    n "{size=19}Я не очень хороша в математике, но даже эти условия означают, что вероятность найти такого человека крайне мала.{/size}"
    show natsuki cm
    mc "{size=19}Ну не настолько же всё безнадёжно?{/size}"
    show natsuki anno cm oe brow
    mc "{size=19}Можно и просто ей друзей найти.{/size}"
    show natsuki om
    n "{size=19}Понимаешь, как это абсурдно будет выглядеть?{/size}"
    show natsuki neut cm oe
    mc "{size=19}Но делать-то что-то надо?{/size}"
    show natsuki dist om oe
    n "{size=19}Надо...{/size}"
    show natsuki neut om oe b1d
    n "{size=19}Но даже в такой ситуации я не хочу искать для Юри людей среди сброда малолетних дураков и взрослых идиотов.{/size}"
    n "{size=19}Ты вообще в курсе, что этот сброд в последнее время начал шутить про фимоз?{/size}"
    show natsuki cm
    if persistent.censorship:
        mc "{size=19}...фу, нахрен, реально?{/size}"
    else:
        mc "{size=19}...фу, блять, реально?{/size}"
    show natsuki om
    n "{size=19}Ага!{/size}"
    show natsuki anno om ce brow
    n "{size=19}Не знаю, какому придурку моча в голову ударила, но теперь я эту хрень в комментариях чуть ли не под каждой группой вижу.{/size}"
    n "{size=19}Тошнит уже от этой дури.{/size}"
    n "{size=19}Честное слово, как дегенераты, наслушаются всякой хрени и начнут её пихать во все щели.{/size}"
    n "{size=19}А потом оправдываться будут «рофлами», «приколами» и «иронией».{/size}"
    show natsuki oe
    n "{size=19}Я даже уверена, что эти малолетние дебилы не слышали про другую созвучную болезнь -- фиброз.{/size}"
    show natsuki angr om oe
    n "{size=19}И ведь первые побегут орать от боли, когда она у них обнаружится!{/size}"
    show natsuki e2c b1d
    n "{size=19}Гнилые полудурки...{/size}"
    show natsuki cm
    "...опять Моникаммм...{w}да что ж такое?!"
    show natsuki om oe brow
    n "{size=19}И ведь мы с ними на одной планете живём!{/size}"
    show natsuki cm
    mc "{size=19}Я тебе так скажу: мы с такими индивидами каждый день пересекаемся и даже учимся в одном классе.{/size}"
    mc "{size=19}Просто они это на публику не показывают.{/size}"
    show natsuki om
    n "{size=19}Вот в этом и заключается вся отвратительность!{/size}"
    n "{size=19}Представь, что этот идиот будет творить, когда останется с Юри наедине!{/size}"
    show natsuki ce
    n "{size=19}Доведёт её до демонического состояния, 100 процентов.{/size}"
    show natsuki sedu om ce
    n "{size=19}...хотя тогда в мире на одного идиота станет меньше...{/size}"
    show natsuki cm
    mc "{size=19}И всё-таки, может, попробовать найти хоть кого-то нормального?{/size}"
    show natsuki anno om oe
    n "{size=19}Я уже всё сказала.{/size}"
    n "{size=19}Это бессмысленно.{/size}"
    n "{size=19}И слишком долго, если вдруг возможно.{/size}"
    n "{size=19}Свои отношения построить практически нереально, а тут стороннему человеку помогать, хоть и подруге.{/size}"
    show natsuki cm
    mc "{size=19}...ладно, соглашусь.{/size}"
    show natsuki e1b b1d
    "Мы вообще хоть придём к какому-нибудь решению, нет?"
    show natsuki neut cm e1b brow
    "Честно, меня уже достали все эти разговоры."
    "Каждый раз накидываешь варианты, а они все летят в помойку."
    "Абсолютно каждый раз по абсолютно любой проблеме."
    "..."
    "И ведь самое мерзкое, что время идёт, а вместе с ним всё медленно усугубляется и становится хуже."
    "Неужели я так и не смогу ничего решить, как бы ни старался?..."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition
    pause 0.5

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    n "И...{w}нам сюда."
    mc "Что-то мы окольными путями попёрлись."
    n "Я не виновата, что тут такая застройка!"
    mc "..."
    n "..."
    n "А вот и госпиталь."

    scene bg niigata hospital outside day with dissolve
    pause 0.25
    mc "Фига себе он гигантсткий..."
    n "Конечно!"
    n "Ниши-Ниигата Тюо вообще на международном уровне!"
    mc "Ну...{w}я представлял его немного меньше..."
    n "Всё, давай, пошли во внутрь."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 hospital_empty_noise fadein 3.0
    scene bg niigata hospital inside day
    show natsuki turned black_shirt fc neut cm e1b b1a at t11
    with wipeleft_scene
    show natsuki oe
    mc "{size=19}Практически никого?...{/size}"
    show natsuki om b1d
    n "{size=19}Воскресенье!{/size}"
    show natsuki cm
    mc "{size=19}Госпиталь мирового уровня!{/size}"
    show natsuki doub om oe brow lhip rhip
    n "{size=19}Какая разница?{/size}"
    show natsuki cm
    mc "{size=19}...{/size}"
    "А реально, какая разница..."
    show natsuki neut om oe ldown rdown
    n "{size=19}Так, сиди тут, здесь как раз прохладненько, приятненько.{/size}"
    show natsuki e1b b1a
    n "{size=19}Я пойду к стойке, а потом в палату.{/size}"
    show natsuki oe brow
    n "{size=19}Вернусь через полчаса-час, как говорила вчера.{/size}"
    show natsuki cm
    mc "{size=19}Угу-угу.{/size}"
    mc "{size=19}Можешь не торопиться, я могу подождать.{/size}"
    show natsuki om
    n "{size=19}Ага.{/size}"
    show natsuki cm e1b b1a at thide
    hide natsuki
    pause 0.5
    mc "{size=19}...{/size}"
    mc "{size=19}...уф-ф-ф...{/size}"
    "А что мне делать-то?"
    "Вот об этом я не подумал..."
    mc "{size=19}М-м-м...{/size}"
    "В мобильнике порыться, что ли..."
    "...или кому-то написать?"
    "Кстати, да!"
    "Надо спросить у Моники, как там она и как у неё родители."
    "Всё-таки...{w}нужно же мне хоть какие-то шаги делать, а?"
    "Иначе у нас не отношения, а какая-то откровенная дрянь."
    call skip_block_on

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 43
        clock = (10, 53)

    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        time year 2018 day 29 month 4 hour 10 minute 53
        "mc" "Мони, привет!"
        "mc" "У тебя всё хорошо? Твой отец успокоился?"
    "Думаю, что да, но кто его знает..."
    "В любом случае я не хочу с ним пересекаться."
    $ phone.system.clock = (10, 54)
    "Вообще."
    phone discussion "mc_m_chat":
        "m" "Привет, Макс!"
        "m" "Со мной всё в порядке, спасибо, что беспокоишься"
        "m" "Мне пришлось поговорить с папой немного на высоком тоне после твоего ухода с Сайори"
        "m" "Но он быстро успокоился"
        "m" "Хотя ничего особо не поменялось..."
        "mc" "Кто бы сомневался"
        "mc" "Я тут, кстати, подумал..."
        "m" "?"
        "mc" "Может, нам сегодня сходить куда-нибудь наедине?"
    $ phone.system.clock = (10, 55)
    phone discussion "mc_m_chat":
        "mc" "Ну, вчера мы всей толпой шлялись, весело, да, но свиданием это трудно назвать, а хотелось организовать что-то наедине, но тут ещё твои родители..."
        "m" "Ахаха)))"
        "m" "Не волнуйся так, Макс!"
        "m" "Не уверена, что сегодня получится, но если что"
        "m" "Стой"
        "m" "Я вспомнила!"
        "m" "Мама хотела с тобой нормально познакомиться"
        "m" "Она ещё папу уговорила стать к тебе лояльнее"
        "mc" "Звучит не очень обнадёживающе..."
    $ phone.system.clock = (10, 56)
    phone discussion "mc_m_chat":
        "m" "Как есть"
        "m" "Лучше так, чем никак"
        "mc" "И то верно"
        "mc" "И когда же мне вас навестить?"
        "m" "Мои родители сегодня вечером уедут обратно, поэтому тебе стоит поторопиться до 17:00"
        "mc" "Хм, хорошо"
        "mc" "Я напишу, как приготовлюсь"
        "m" "Буду ждать, только сильно не оттягивай этот момент"
        "m" "Я знаю, что тебе тогда было неприятно, но в этот раз будет получше"
        "mc" "Угу"
        "m" "Ладно, не кисни)"
    $ phone.system.clock = (10, 57)
    phone discussion "mc_m_chat":
        "m" "Жду твоего сообщения!"
        "mc" "Да, конечно"

    phone end discussion transition

    call skip_block_off
    mc "{size=19}Первый раз всегда комом, блин...{/size}"
    "Всегда это ненавидел."
    "Особенно когда психолог затрагивал тему «с первыми шагами»."
    "Это всё равно, что шагать в яму, зная, что ты грохнешься мордой в землю."
    "Почему это никак нельзя невелировать?"
    "Есть же способ избежать это дерьмо, есть же!"
    "Но нет, приходиться каждый раз это испытывать..."
    mc "{size=19}Пф-ф-ф...{/size}"
    "Опять мерзко стало."
    "Словно я откатился до состояния, когда меня все кинули."
    "Отношения с Моникой ничего не изменили."
    "Мысли как сжирали меня, так и сжирают."
    "Что мне с этим делать?!"
    play phone_sound new_message_mc
    pause 1.0
    call skip_block_on

    $ phone.system.clock = (10, 59)

    phone register "mc_y_chat":
        time year 2018 day 29 month 4 hour 10 minute 59
        "y" "Привет"

    phone discussion "mc_y_chat"
    $ plot_pause()
    "Юри?"
    phone discussion "mc_y_chat":
        "mc" "Привет"
        "y" "Как у тебя дела?"
        "mc" "Более-менее"
    $ phone.system.clock = (11, 0)
    phone discussion "mc_y_chat":
        "mc" "Решил сопроводить Нацуки до госпиталя, сейчас сижу перед ресепшеном, делать особо нечего"
        "y" "Ах, понимаю"
        "y" "Я как раз написала Нацуки извинение, что не смогла составить ей компанию"
        "y" "Потому что сегодня возвращается моя мама..."
        "mc" "Ааа, понятно"
    "Да, Юри же говорила, что её мать уехала на работу на пару недель, если мне память не изменяет..."
    phone discussion "mc_y_chat":
        "y" "Ты не хотел бы с ней встретиться?"
        "mc" "Мы с Нацуки можем зайти к тебе на обратном пути"
        "mc" "Твоя мама когда приезжает?"
        "y" "Да конечно вы можете прийти вместе"
    $ phone.system.clock = (11, 1)
    phone discussion "mc_y_chat":
        "y" "Мама приедет примерно в полдень"
        "mc" "Прекрасно, мы как раз чуть позже подойдём"
        "y" "Поняла"
        "y" "Напишите мне, когда будете подходить"
        "mc" "Ок"

    phone end discussion transition

    call skip_block_off
    "Надеюсь, мы сильно у неё не засидимся."
    "Иначе фиг я с родителями Моники встречусь."
    "..."
    "Ладно, делать сейчас всё равно нехрен."
    "Надо снова искать этого чёртового психолога..."
    stop noise_1 fadeout 1.0
    call window_close

    call window_dialog_fast_transition("y")

    call window_open
    play noise_1 sink_open fadein 3.0
    scene bg yuri house bathroom day with dissolve_scene_full
    pause 2.0
    stop noise_1
    play sound sink_close
    pause 1.0
    y "Надеюсь, всё пройдёт хорошо..."
    "Я хотела, чтобы он был один, но...{w}пусть и Нацуки будет, я же обещала, что не буду её забывать."
    "И всё-таки не могу осознать..."
    y "...неужели...{w}я так сильно поменялась?"

    scene black with dissolve
    pause 0.25
    y "Куда только всё это идёт..."
    call window_close

    pause 1.0
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    scene bg yuri house hallway day with dissolve
    pause 0.25
    y "Хм..."
    y "Вроде бы я везде прибралась..."
    "Как хорошо, что наш дом такой компактный."
    "А если вести себя аккуратно и опрятно, то генеральную уборку можно проводить раз в год..."
    pause 0.25
    play phone_sound new_message_yuri
    pause 1.0
    y "М-м?..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 88
        clock = (12, 7)

    phone register "y_k_chat":
        time year 2018 day 29 month 4 hour 11 minute 7
        "k" "Юри, тут только что случился полный бардак!"

    phone discussion "y_k_chat"
    $ plot_pause()
    phone discussion "y_k_chat":
        "y" "?"
        "k" "Про меня внезапно вспомнила Камуко спустя n-ное количество времени"
        "k" "Ты, кстати, помнишь её?"
        "y" "Да, из Клуба выпечки, пересекалась с ней в понедельник"
        "k" "Вот, хорошо"
    $ phone.system.clock = (11, 8)
    phone discussion "y_k_chat":
        "k" "Она от Сайори узнала, что я состою в Вашем клубе и решила написать мне в ЛС для подготовки к вступлению к нам"
        "k" "Стихи научиться писать, всякое такое..."
        "y" "Камуко хочет вступить в Литературный клуб?..."
        "k" "Да"
        "y" "Но почему она написала именно тебе?"
        "k" "Сказала, что все, чьи номера она знает, заняты"
        "y" "Хм"
        "k" "Поскольку у меня сейчас нет на это времени..."
        "k" "Короче говоря, я перенаправила её на тебя)"
    $ phone.system.clock = (11, 9)
    y "...э?"
    phone discussion "y_k_chat":
        "y" "Что?"
        "k" "Извини, если ты вдруг занята!"
        "k" "Но ты сейчас единственная, кто может принять её по полной программе)"
        "y" "Она мне напишет?"
        "k" "Как только подойдёт к твоему дому"
        "y" "Она придёт лично?!"
        "k" "Агась)"
        "y" "Но ко мне вернётся мама через час..."
        "k" "Ох, прости!"
        "k" "Я могу пока притормозить Камуко, не срочно же всё это!"
        "y" "Не надо!"
    $ phone.system.clock = (11, 10)
    phone discussion "y_k_chat":
        "y" "Всё хорошо, я всё сделаю"
        "k" "Уверена?"
        "y" "Точно"
        "k" "Рада слышать)"
        "k" "Держу за тебя кулачки!"
        "y" "Спасибо!"

    phone end discussion transition

    y "У-у-у..."
    pause 0.25
    play phone_sound new_message_yuri
    pause 1.0

    phone register "y_kam_chat":
        time year 2018 day 29 month 4 hour 11 minute 10
        "kam" "ПРИВЕЕЕЕЕЕЕТ"

    phone discussion "y_kam_chat":
        "kam" "Я у твоего дома -- можно в гости???"
    y "Уже?!"
    $ phone.system.clock = (11, 11)
    phone discussion "y_kam_chat":
        "y" "Можно"
        "kam" "УРА"
        "kam" "Только открой мне дверь пожалуйста :D"
        "y" "Секунду"

    phone end discussion transition
    call skip_block_on
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    play music suspicion fadein 3.0
    scene bg yuri house hallway day
    show kamuko turned casual happ cm oe lhiphid rhid at t11
    with wiperight
    show kamuko om e1b rface
    kam "Ух, у тебя тут уютненько!"
    show kamuko cm
    y "Ум-м."
    show kamuko oe
    "Не думала, что она будет...{w}в настолько {b}лёгком{/b} прикиде..."
    show kamuko om ce ldown rdown
    kam "А, не обращай внимания, что я в таком виде."
    show kamuko oe
    kam "Ты, оказывается, всего лишь в паре кварталов от моего дома."
    show kamuko curi om e1c lhiphid rface
    kam "Вот я и подумала, чего мне вариться у тебя дома, когда я могу прийти в чём-то более лёгком."
    show kamuko happ om ce
    kam "Но не суть!"
    show kamuko oe rhid
    kam "Тебе Котоноха уже всё рассказала?"
    show kamuko cm
    y "А-а, да-да..."
    show kamuko om ce ldown rdown at h11
    kam "Отлично!"
    show kamuko cm
    y "Так ты...{w}хочешь вступить в наш клуб?"
    show kamuko om oe
    kam "Правильно!"
    show kamuko doub om oe lhiphid rface
    kam "Но не сразу: по немножечку, по легонечку..."
    show kamuko angr om oe
    kam "Потому что, «А»: я не хочу, чтобы из-за моего ухода страдали участники Клуба выпечки!"
    show kamuko e1i rdown
    kam "Президент не в счёт, тьфу на неё."
    show kamuko cm
    y "А как...{w}то есть, что значит \"страдать\"?"
    show kamuko neut om oe
    kam "Ну это, официальный статус клуба будет потерян, продукты перестанут приносить, там, всякую технику обновлять, наверное..."
    show kamuko curi om e2e rface
    kam "Это...{w}ну как его там..."
    show kamuko happ om ce
    kam "А, финансирование!"
    show kamuko cm oe rdown
    y "...поняла, точно...{w}вас же 5 человек..."
    show kamuko om rhid
    kam "Ага!"
    show kamuko curi om oe
    kam "Так, о чём я там говорила?"
    show kamuko cm
    y "Что-то про \"не сразу\"..."
    show kamuko happ om ce
    kam "Вступление, да-да-да!"
    show kamuko curi om e1b rface
    kam "Про «А» я сказала, а про «Б»...{w}а что я хотела сказать?..."
    show kamuko oe
    kam "Ты не знаешь?"
    show kamuko cm
    y "Откуда?"
    show kamuko om e2e
    kam "Действительно..."
    show kamuko happ om ce rdown
    kam "А-а-а, подготовиться!"
    show kamuko oe rhid
    kam "Точно, я хотела научиться у тебя мастерству написания стихов и прочей шняги!"
    show kamuko om ce b1c ldown rdown
    kam "Мне же надо быть во всеоружии, чтобы не пасть лицом и не опозорить своё имя!"
    show kamuko cm
    y "Как-то, ха-ха-ха...{w}пафосно немного..."
    show kamuko happ om oe brow
    kam "Такова цена за всю мою серьёзность и ответственность подхода к делу!"
    show kamuko lhiphid rhid
    kam "Итак, ближе к делу!"
    show kamuko curi om oe
    kam "Когда мы будем делать дело?"
    show kamuko cm
    y "Э-э-э..."
    show kamuko neut cm oe
    y "П-подожди, давай не так быстро..."
    show kamuko om
    kam "А что?"
    show kamuko cm
    y "Т-ты же всё-таки в гостях, а я тебя не приняла..."
    show kamuko happ om ce ldown rdown
    kam "А-а-а, конечно!"
    show kamuko oe rface
    kam "Я могу сейчас перезайти в твой дом, чтобы «обнулить» наш разговор для полноценного гостепреимства!"
    show kamuko cm rdown
    y "Что?"
    show kamuko om ce
    kam "Давай, я перезахожу!"
    call window_close

    show kamuko cm:
        align (0.5, 0.5) anchor (0.5, 0.5)
        ease 1.0 xoffset -1500 zoom 3.0
    pause 1.0
    hide kamuko

    call window_open
    y "П-подожди, не надо выходить!"
    kam "...хм-м-м..."
    kam "Да, ты права."
    kam "Достаточно подойти к двери, сделав вид, что закрыла её лично..."
    y "..."
    call window_close

    show kamuko turned casual happ cm ce at i11:
        align (0.5, 0.5) anchor (0.5, 0.5) xoffset -1500 zoom 3.0
        ease 1.0 xoffset 0 zoom 1.0
    pause 0.5

    call window_open
    show kamuko om
    kam "Приве-е-ет!"
    show kamuko cm
    y "..."
    show kamuko curi om oe
    kam "Юри?"
    show kamuko cm
    y "...я запуталась."
    show kamuko worr om ce lhiphid rhid
    kam "Эх, ладно, не будем повторно гостепреимничать!"
    show kamuko nerv om oe rface
    kam "А то выходит, что разговор между нами мы полностью друг другу проспойлерили."
    show kamuko happ om oe rhid
    kam "Хотя я не боюсь спойлеров, в отличие от некоторых умников в Интернете!"
    show kamuko anno om oe
    kam "Как только напишешь случайно хоть чуточку спойлера какого-то интересного сюжетного момента в каком-нибудь аниме, так всё!"
    show kamuko e1i rface
    kam "Бе-бе-бе, спойлеры, зачем ты это написала, бе-бе-бе!"
    show kamuko doub om oe
    kam "Когда видишь такие сообщения, кажется, что эти умники специально вчитывались в твои слова, прогоняли их несколько раз в голове и думали о них, пока сообщение писали..."
    show kamuko e1i
    kam "...и когда его выкладывали и перечитывали на ошибки, и потом ещё раз, когда их комментарии кто-то лайкнул или когда кто-то на него ответил."
    show kamuko anno om oe
    kam "А могли бы просто не акцентировать своё внимание и не вести себя, как дети!"
    show kamuko happ om oe ldown rdown
    kam "Вот я, например, если вижу что-то спойлерное, то выкручиваю свою силу волю на максимум, перестаю их читать и стараюсь переключить своё внимание на что-то другое!"
    show kamuko ce
    kam "А если даже и получаю спойлер, то он нисколько не портит мне впечатление об аниме!"
    show kamuko oe lhiphid rhid
    kam "Потому что мне оно нравится!"
    show kamuko anno om oe
    kam "А если умники теряют к аниме интерес, то это исключительно их проблемы, хмпф..."
    show kamuko curi om e2e
    kam "Так, э-э-э..."
    show kamuko neut om oe
    kam "Кажется, мы потеряли суть нашего разговора."
    show kamuko cm
    y "...давай я заварю тебе чай..."
    show kamuko happ om ce ldown rdown
    kam "О, прекрасно!"
    show kamuko oe
    kam "Как раз за ним вернёмся к разговору о важном!"
    show kamuko e1b lhiphid rhid
    kam "Мне, кстати, чёрный нравится."
    show kamuko neut om oe
    kam "Чай."
    show kamuko e1b
    kam "А цвет не очень...{w}как и серый, белый, жёлтый, зеленовато-морской, их блёклые оттенки..."
    show kamuko happ om oe
    kam "Хотя все цвета хороши и все цвета важны."
    show kamuko ce
    kam "Так что не суть!"
    show kamuko nerv om oe rface
    kam "Так вот, остальные чаи немного терпкие, а лимонный так вообще ужас!"
    show kamuko cm
    "Каждое её \"так\" словно стук по моей голове..."
    "Надо сделать ей жасминовый чай для успокоения..."
    show kamuko happ cm oe
    call window_close

    call window_dialog_fast_transition("mc")

    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.1

    call window_open
    play noise_1 hospital_empty_noise fadein 3.0
    scene bg niigata hospital inside day
    "После недолгих поисков весь мой внезапный прилив энтузиазма растратился на чтение комментариев по этому госпиталю в картах..."
    mc "{size=19}М-м-мда...{/size}"
    "Одни 5 звёзд ставят и говорят, что всё прекрасно."
    "Другие лупят 4 или 3 звезды либо по делу, либо по какой-то фигне в большинстве случаев."
    "И каждый раз всё варьируется."
    "Удивительно, что вроде бы это госпиталь мирового уровня, основывающийся на нейрохирургии, а в комментариях какая-то бестолковая каша и крайне субъективные оценки."
    "Нет, я не оправдываю какие-либо ошибки или ещё что-то негативное, из-за чего могли снизить оценку по делу."
    "Просто в большинстве комментариев написана причина сниженной оценки, которая иногда достаточно...{w}тупая?"
    "Ну как мне ещё этот бред назвать?"
    "С другой стороны, многие затрагивают серьёзные проблемы."
    "Например, здесь платный Wi-Fi, что-то с ценами палат, прочего..."
    "Плюс жалуются на отсутствие должных объяснений по тем или иным вопросам от персонала, на отношение с самим персоналом и его вялость реагирования на пациентов..."
    "...отдельно выделяют медсестёр в негативном ключе..."
    "...но при этом некоторые пишут, что этот же персонал достаточно добрый и отзывчивый."
    "И там, и там люди понапихали лайков: где-то больше, где-то меньше."
    "Кому после этого верить?"
    "И вот из-за такой вот мишуры итоговая оценка госпиталя Ниши-Ниигата Тюо -- 3.8 из 5."
    "Хрен знает, насколько всё соответствует правде, но надеюсь, что Нацуки и её мать с проблемами здесь не сталкиваются..."
    "Просто иногда такого поначитаешься, что хочется «оценённое» место за километр обходить."
    "А потом выясняется, что не всё так уж траурно и плохо."
    show natsuki turned black_shirt fc neut cm e1b at t11
    pause 0.2
    show natsuki oe
    mc "О, вернулась?"
    n "М-м."
    mc "Всё в порядке, нормально?"
    show natsuki om b1d lhip rhip
    n "Да ясен пень, что всё прекрасно."
    show natsuki e1b
    n "И я этому...{w}рада."
    show natsuki ff dist om ce ldown rdown
    n "Ладно, всё, пойдём, тут больше делать нечего."
    show natsuki cm
    mc "Окей."
    show natsuki e1b
    stop noise_1 fadeout 1.0
    call window_close

    call window_dialog_fast_transition("y")

    $ audio.suspicion_2 = "<from " + str(currentpos) + " loop 1.119 to 76.938>mod_assets/music/suspicion.ogg"
    play music suspicion_2 fadein 0.5

    call window_open
    scene bg yuri house livingroom day at yuri_sofa
    show kamuko turned casual happ cm e1b lhiphid rface at el11
    pause 0.2
    show kamuko om
    kam "Помнится, полгода назад я видела по телевизору выпуск развлекательного шоу, в котором репортёры находят иностранцев и выясняют их причины пребывания в Японии."
    kam "В каком-то аэропорту они поймали русскую косплеершу в образе Ха{image=accent_low_register}{space=-15}цунэ Ми{image=accent_low_register}{space=-15}ку."
    show kamuko cm oe
    y "Самый популярный вокалоид?"
    show kamuko om ce rhid
    kam "Он самый!"
    show kamuko cm
    y "Я просто...{w}не очень разбираюсь в этой теме..."
    show kamuko om oe
    kam "Да и не надо, их целый воз и маленькая тележка, всех в голове не удержишь."
    show kamuko cm
    y "Но песни от них довольно интересные..."
    show kamuko om
    kam "Ага, сама иногда слушаю."
    show kamuko nerv om oe rface
    kam "Так вот, видела бы ты, как косплеерша была растеряна!"
    show kamuko happ om oe
    kam "Но её понять можно: ни с того, ни с сего дядьки с камерами подошли и начали вопросами донимать!"
    show kamuko ce rhid
    kam "Хотя она так мило реагировала, прямо ужас!"
    kam "И сама она миленько и классно выглядела!"
    show kamuko oe
    kam "Ещё и поёт красиво!"
    show kamuko cm
    y "М-м..."
    show kamuko om e1d rface
    kam "О, а знаешь, что Фукка безумно боится самолётов?"
    show kamuko cm
    y "Правда?"
    show kamuko om ce rhid
    kam "Ага!"
    show kamuko oe
    kam "Она за несколько дней до перелёта из России сюда увидела по новостям какого-то дядьку-учёного, а было это...{w}э-э-э...{w}3000 лет тому назад, ну где-то в 2010-ых годах."
    show kamuko neut om e1b
    kam "Летел дядька из Японии в Россию и на полпути в самолёте случился пожар."
    show kamuko curi om oe
    kam "Непонятно почему, но, к счастью, никто не пострадал."
    show kamuko neut om oe
    kam "А вот его бумажки погорели."
    show kamuko e1b b1c
    kam "И вот он на камеру репортёров там так возмущался, что я, да вы, да мы, да оно, да не могло!"
    show kamuko oe brow
    kam "Досталось всем, короче: и пилотам, и бортпроводницам, и России, и Японии, и всему человечеству."
    show kamuko angr om oe
    kam "Ни капли благодарности персоналу за то, что всё обошлось без жертв!"
    show kamuko neut om oe
    kam "А Фукка, когда это увидела, была тогда маленькой и очень доверчивой."
    show kamuko curi om e1c
    kam "Хотя не сказать, что что-то в ней сильно поменялось..."
    show kamuko neut om oe
    kam "Короче, перепугалась сильно и очень переживала во время полёта."
    show kamuko nerv om oe rface
    kam "Наверное, навоображала себе тыщу сценариев взрыва самолёта и его падения с крутыми пике..."
    show kamuko happ om oe rhid
    kam "Однако перелёт прошёл нормально, ничего, к счастью, не случилось."
    show kamuko neut om e1b
    kam "Правда, с тех пор она боится самолётов..."
    show kamuko cm
    y "М-м..."
    show kamuko happ om oe
    kam "Так-то раньше можно было напрямую из Москвы в Токио попасть, поэтому Фукке повезло лететь лишь в одном самолёте."
    show kamuko pout om oe
    kam "А сейчас сплошные кривые пути с пересадками в других странах, как сама Фукка и сказала..."
    show kamuko cm
    y "Ох..."
    show kamuko neut cm oe
    y "Мне тоже самолёты...{w}не очень нравятся..."
    show kamuko happ om ce
    kam "Да я тоже не любительница летать, ха-ха!"
    show kamuko nerv om oe
    kam "Но, мне кажется, что Фукка принимает всё слишком близко к сердцу!"
    show kamuko neut om oe
    kam "Она такая волнительная, что скоро станет натуральным источником землетрясений."
    show kamuko happ om ce
    kam "Хотя, будь я на её месте, тряслась бы не хуже её!"
    show kamuko nerv om oe
    kam "Она же из России, а там жуть сплошная!"
    show kamuko rface
    kam "На севере морозы бывают такие, что горячая лапша замерзает в воздухе!"
    show kamuko e2c
    kam "В лесах большие медведи ходят и часто выходят к людям!"
    show kamuko pout om oe
    kam "А ещё люди любят пить много водки..."
    show kamuko cm
    y "П-подожди, это уже какие-то бестолковые стереотипы..."
    show kamuko neut om oe
    kam "Чего это они бестолковые?"
    show kamuko happ om ce rhid
    kam "Очень даже толковые!"
    show kamuko neut cm oe
    y "Совершенно нет."
    y "Я читала информацию, в России зимой в среднем -10-20 градусов, а сильные морозы только за северным полярным кругом."
    show kamuko om
    kam "Всё равно же холодно."
    show kamuko cm
    y "Но не так сильно..."
    y "У нас же на Хоккайдо тоже до -10 или -15 градусов температура опускается."
    show kamuko curi om oe
    kam "А..."
    kam "Что-то я не подумала..."
    show kamuko neut cm oe
    y "И там же медведи выходят к людям."
    show kamuko pani cm oe
    y "Недавно была новость, что в Хоккайдо участились случаи выхода голодных бурых медведей..."
    show kamuko om ldown rdown
    kam "Чего?!"
    kam "Реально?!"
    show kamuko cm
    y "Да, по телевизору в новостях показывали..."
    show kamuko curi om e1a lhiphid rhid
    kam "Ну хорошо, а водка?"
    kam "Люди же там пить любят!"
    show kamuko cm
    y "Тоже стереотип."
    show kamuko neut cm oe
    y "Самыми пьющими странами по данным ВОЗ за прошлый год признаны европейские."
    y "Россия даже в первую десятку не вошла."
    y "По крайней мере, то, что я видела в Интернете..."
    show kamuko om
    kam "Ну и ну!"
    show kamuko curi om oe
    kam "Так подожди, как мы от стихов до пьющих людей дошли..."
    show kamuko cm
    y "...э-э-э..."
    call window_close

    call window_dialog_fast_transition("mc")

    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.1

    call window_open
    play noise_1 train_moving_3 fadein 1.0
    scene bg train zorder 1
    show train_window_niigata zorder 0
    show natsuki turned black_shirt fc neut cm e1b b1a zorder 2 at i22:
        ypos 800 zoom 0.9
    show layer master:
        align (0.5, 0.5) anchor (0.7, 0.55) zoom 1.7
    mc "{size=19}...{/size}"
    show natsuki oe brow
    n "{size=19}...{/size}"
    mc "{size=19}...{/size}"
    show natsuki om
    n "{size=19}...о чём думаешь?{/size}"
    show natsuki cm
    mc "{size=19}М-м?"
    mc "{size=19}Да ни о чём, в голове как-то пусто.{/size}"
    mc "{size=19}Или бессвязная каша...{w}не знаю.{/size}"
    show natsuki om
    n "{size=19}Ясно.{/size}"
    show natsuki cm
    mc "{size=19}Скучно?{/size}"
    show natsuki e1b b1a
    n "{size=19}Угу.{/size}"
    show natsuki om
    n "{size=19}Не хочется к папе сразу возвращаться.{/size}"
    n "{size=19}Хочу немного прогуляться или побыть с друзьями.{/size}"
    show natsuki cm
    mc "{size=19}Ну...{w}тебе никто не мешает сделать вид, что ты задержалась на поезде или у мамы.{/size}"
    show natsuki om oe brow
    n "{size=19}Да я знаю, но всё равно долго торчать нельзя, а то начнётся гундёж и возмущения.{/size}"
    show natsuki anno om ce
    n "{size=19}Чувствую себя взаперти, вот реально.{/size}"
    show natsuki e1b b1d
    n "{size=19}Переехать бы в какой-нибудь маленький дом одной и начать там жить...{/size}"
    show natsuki neut om oe brow
    n "{size=19}Нет, я прекрасно понимаю, что это будет тяжело из-за кучи проблем, а ещё менее безопасно, но...{/size}"
    show natsuki e4a
    n "{size=19}...я точно буду знать, что там спокойно, тихо и свободно.{/size}"
    show natsuki cm
    mc "{size=19}...забавно, что у меня когда-то были абсолютно такие же мысли.{/size}"
    show natsuki curi om oe
    n "{size=19}Правда?{/size}"
    show natsuki cm
    mc "{size=19}Да.{/size}"
    show natsuki neut cm oe
    mc "{size=19}Впрочем, они и остались, хотя я уже живу отдельно.{/size}"
    show natsuki om b1d
    n "{size=19}Меня в этих мыслях раздражает тот факт, что их просто могло бы и не быть.{/size}"
    n "{size=19}Папа бы мог просто быть спокойнее и более понимающим.{/size}"
    show natsuki e1b
    n "{size=19}И я бы менее нервной стала.{/size}"
    show natsuki e4a
    n "{size=19}Но нет, ничего из этого не меняется.{/size}"
    n "{size=19}И если бы причина была только во мне...{/size}"
    show natsuki angr om oe brow
    n "{size=19}В общем, как-будто это всё неправильно!{/size}"
    show natsuki neut om oe b1d
    n "{size=19}Остальные со своими семьями прекрасно уживаются.{/size}"
    show natsuki e4a
    n "{size=19}И только у меня всё через задницу.{/size}"
    show natsuki cm
    mc "{size=19}Нет, Нацуки, твоё желание и мысли -- нормальное явление.{/size}"
    mc "{size=19}И называется это -- взросление.{/size}"
    show natsuki oe brow
    mc "{size=19}Просто мы доходим до той точки, когда нужно уже самому себя обеспечивать, чтобы стать самостоятельными людьми.{/size}"
    mc "{size=19}А если мы не отсепарируемся от всего этого, то приведёт это нас в плачевное состояние.{/size}"
    mc "{size=19}Проще говоря, сломаемся и нихрена не вырастим.{/size}"
    show natsuki om e1b b1a
    n "{size=19}...и я как раз застряла.{/size}"
    show natsuki cm
    mc "{size=19}Знаю."
    mc "{size=19}И ничем не могу помочь.{/size}"
    show natsuki oe brow
    mc "{size=19}Но я уверен, что вся эта ситуация продлится недолго.{/size}"
    show natsuki om
    n "{size=19}Помнится, на прошлой неделе ты уже говорил мне про этот прогноз...{/size}"
    show natsuki cm
    mc "{size=19}Ха, моя интуиция неизменна.{/size}"
    show natsuki curi om oe
    n "{size=19}Обычно интуиция -- это что-то женское.{/size}"
    show natsuki cm
    mc "{size=19}Ну, значит перед тобой психологический мутант.{/size}"
    show natsuki laug om ce
    n "{size=19}Тьфу ты, ха-ха-ха!{/size}"
    show natsuki oe
    n "{size=19}Ну хоть не абстрактный ангел из колец и глаз!{/size}"
    show natsuki cm
    mc "{size=19}А-а-а, это!{/size}"
    mc "{size=19}«Как тебя обнять, как тебя обнять?!»{/size}"
    mc "{size=19}«Не надо меня обнимать!»{/size}"
    show natsuki ce
    mc "{size=19}«ОТКУДА ты это СКАЗАЛ?!»{/size}"
    show natsuki om
    n "{size=19}Ха-ха-ха!{/size}"
    show natsuki cm
    mc "{size=19}Ха-ха!{/size}"
    mc "{size=19}Кстати, я же не сказал.{/size}"
    show natsuki happ cm oe
    mc "{size=19}Пока я один сидел, мне Юри написала, что к ней сегодня приедет мама.{/size}"
    show natsuki neut cm oe
    mc "{size=19}В общем, она в гости меня пригласила, чтобы с матерью встретиться, а ещё сказала, что ты тоже можешь прийти.{/size}"
    show natsuki om
    n "{size=19}О, вот как.{/size}"
    show natsuki e1b b1a
    n "{size=19}Она мне говорила о её приезде, но встречать её не приглашала.{/size}"
    show natsuki cm
    mc "{size=19}Хм...{/size}"
    show natsuki om oe brow
    n "{size=19}Не удивлюсь, если это её «подкат» в твою сторону.{/size}"
    show natsuki cm
    mc "{size=19}Мда, ситуация с ней развивается быстрее, чем я думал.{/size}"
    show natsuki pani cm oe
    mc "{size=19}Может, отказать ей в чувствах прямо в лоб?{/size}"
    show natsuki om
    n "{size=19}С ума сошёл?!"
    n "{size=19}Ты помнишь, что она себе с руками сделала?!{/size}"
    show natsuki sad om oe
    n "{size=19}Фиг мы её остановим в её же доме.{/size}"
    show natsuki e1a
    n "{size=19}А если и получится, то не уверена, что она будет рада видеть тебя в клубе.{/size}"
    n "{size=19}Ты буквально будешь источником её негативных мыслей.{/size}"
    show natsuki cm
    if persistent.censorship:
        mc "{size=19}Да блин, надо было мне сразу ей чётко всё сказать, а не тупить из-за мыслей...{/size}"
    else:
        mc "{size=19}Да блять, надо было мне сразу ей чётко всё сказать, а не тупить из-за мыслей...{/size}"
    show natsuki neut om oe
    n "{size=19}Как вышло, так вышло.{/size}"
    n "{size=19}Будем пробовать аккуратно скидывать её с тебя.{/size}"
    show natsuki cm
    stop noise_1 fadeout 1.0
    call window_close

    call window_dialog_fast_transition("y")

    $ audio.suspicion_2 = "<from " + str(currentpos) + " loop 1.119 to 76.938>mod_assets/music/suspicion.ogg"
    play music suspicion_2 fadein 0.5

    call window_open
    scene bg yuri house livingroom day at yuri_sofa
    show kamuko turned casual neut cm e1i lhiphid rhid at el11
    pause 0.2
    show kamuko om
    kam "Значит, надо начать с чего-то простого..."
    show kamuko cm
    y "Да, и желательно с того, о чём ты сама хочешь писать."
    show kamuko oe
    y "Важно, что никто не заставляет тебя писать стихи на определённые темы."
    show kamuko om
    kam "...но вы же каждый рабочий день стихами обмениваетесь?"
    show kamuko cm
    y "...да."
    show kamuko curi om oe
    kam "Значит, вас заставляют!"
    show kamuko cm
    y "У-у...{w}а ведь правда..."
    show kamuko pani om oe ldown rdown
    kam "Вас держат в поэтическом рабстве?!"
    kam "Юри, моргни 3 раза, если это правда!"
    show kamuko cm
    y "П-подожди, какое рабство?"
    show kamuko neut cm oe lhiphid rhid
    y "Мы просто привыкли к каждому обмену приносить свои стихи."
    y "Лично нам Моника не говорила про их обязательность."
    show kamuko doub cm oe
    y "Разве что...{w}её слова про «ожидания» наших стихов можно трактовать как «рекомендацию»..."
    show kamuko om
    kam "Добровольно-принудительно, поняла."
    show kamuko cm
    y "Н-не совсем!"
    show kamuko happ om e1b rface
    kam "Итак, с чего же начать стих..."
    show kamuko cm
    y "..."
    show kamuko doub cm ce
    kam "Хм-м-м..."
    show kamuko neut om oe rhid
    kam "Что-то не думается."
    show kamuko cm
    y "...это обычное явление, всё нормально."
    show kamuko anno om oe
    kam "Это «нормально» никакой погоды не делает."
    show kamuko cm
    y "Попробуй написать о том, что тебе нравится."
    show kamuko neut cm oe
    y "У тебя же есть любимые увлечения..."
    show kamuko happ om ce ldown rdown
    kam "Имеются!"
    show kamuko e1b rface
    kam "Аниме, котики, общение, прекрасное времяпрепровождение--{nw}"
    show kamuko neut cm oe
    y "В-вот выбери что-то одно и напиши об этом."
    show kamuko e1b
    kam "Хм-м-м..."
    show kamuko doub cm ce
    kam "Хм-м-м-м-м-м..."
    show kamuko om e1i ldown rdown
    kam "Ну-кась..."
    show kamuko cm
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg yuri house livingroom day at yuri_sofa
    show kamuko turned casual angr cm e1c lhiphid rhid at el11
    with wiperight
    show kamuko om
    kam "Да это какая-то фигня!"
    show kamuko cm
    y "Не расстраивайся!"
    y "Мы можем выбрать...{w}ещё одну другую тему."
    show kamuko om oe
    kam "Юри, это уже третья попытка что-то написать!"
    show kamuko e1i
    kam "Я в четвёртую верить не собираюсь!"
    show kamuko cm
    y "Но ведь надо пробовать, иначе не получится--{nw}"
    show kamuko om oe ldown rdown
    kam "Да я уже напробовалась!"
    kam "Что-то нифига не весело: я думала, что это будет просто и легко."
    show kamuko e1b
    kam "Ах-х-х, задница горит!"
    kam "Я так не потела, даже когда в одиночку боролась с командой «задротов-киберкотлет» в сетевой игре!"
    show kamuko neut cm oe
    y "...и ты тогда победила?"
    show kamuko happ om ce lhiphid rhid
    kam "Ещё бы!"
    show kamuko oe
    kam "У них полыхало так же, как у меня сейчас!"
    show kamuko nerv om oe
    kam "Обожаю таких засранцев ставить на место."
    stop music fadeout 3.0
    show kamuko cm
    y "Стой, подожди секунду..."
    show kamuko neut cm oe

    scene bg yuri house livingroom day with dissolve
    pause 0.25
    y "..."
    kam "Что там?"
    kam "Нас собираются штурмовать?!"
    y "Мама приехала!"
    show kamuko turned casual curi cm oe at t11
    pause 0.2
    show kamuko om
    kam "Мама?"
    show kamuko cm
    y "Надо её встретить!"

    scene black with wipeleft_scene
    kam "{size=19}Стой, я тоже хочу!{/size}"
    call window_close

    call window_dialog_fast_transition("mc")

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 day
    show natsuki turned black_shirt fc neut cm e1c lhip rhip at i11
    pause 0.2
    show natsuki oe
    mc "Ой, всё, надо снять уже этот пластырь."
    show natsuki om b1b lhip rhip
    n "Эй, куда?"
    n "У тебя там всё зажило?"
    show natsuki cm
    mc "Да ещё пока мы ехали в госпиталь."
    show natsuki brow
    mc "Пластырь и так уже отваливается, раздражает своими загнувшимися краями."
    show natsuki om e1b ldown rdown
    n "...хорошо, дело твоё."
    show natsuki cm

    scene bg yuri house outside day
    show natsuki turned black_shirt neut cm e1b at t33 zorder 1
    with wipeleft_scene
    mc "Фух, припёрлись."
    show natsuki om oe
    n "Ну что, звони."
    show natsuki sedu om ce lhip rhip
    n "Ты ж у нас главный гость нашей лавандовой принцессы."
    show natsuki cm
    mc "...что за надменный тон?"
    show natsuki happ om oe ldown rdown
    n "Да шучу я, жми давай."
    show natsuki cm
    call window_close

    show layer master at yuri_gate
    with dissolve
    pause 0.5
    play sound doorbell_yuri
    pause 2.0
    play sound doorbell_yuri
    pause 3.0

    call window_open
    show natsuki neut cm oe
    kam "{size=19}О!{/size}"
    call window_close

    show layer master
    show kamuko turned casual happ cm oe at t11 zorder 2
    show natsuki curi cm e2a
    with dissolve
    pause 0.5

    call window_open
    show kamuko om ce
    kam "Здрасьте!"
    show kamuko cm
    show natsuki om lhip rhip
    n "Чё?!"
    show kamuko angr cm oe
    n "Ты что тут делаешь?!"
    show kamuko om lup
    show natsuki cm
    kam "Во-первых, не что, а ради чего."
    show kamuko laug om oe ldown
    show natsuki angr cm oe
    kam "А во-вторых, я тоже рада видеть тебя, Нацуки!"
    show kamuko cm ce
    show natsuki om
    n "Это не даёт ответа на мой вопрос--{nw}"
    show kamuko at t22
    show natsuki pani om oe ldown rdown
    n "Куда ты ко мне полезла?!"
    show kamuko om
    show natsuki cm ce
    kam "Всегда тебя хотела сжать!"
    show kamuko cm
    show natsuki om
    n "Пусти-и-и!"
    show yuri turned sundress happ cm oe at t31 zorder 3
    show natsuki cm
    pause 0.2
    show yuri om
    y "Макс, ты пришёл?"
    show yuri cm
    mc "...да, как видишь..."
    show yuri neut cm e1d
    n "Пфпр-р-р!"
    show yuri angr om oe
    y "Камуко, хватит!"
    show yuri cm
    show kamuko happ om ce
    kam "Эх, ну ладно!"
    show kamuko cm at t32
    show natsuki om
    n "БУАХ!"
    show yuri neut cm e1d
    show natsuki cm
    mc "К тебе приехала мама, я так понимаю?"
    show yuri happ cm oe
    y "М-м."
    show yuri om
    show kamuko oe
    show natsuki dist om ce
    y "Она уже разгрузилась и приготовила чай."
    show yuri cm
    show kamuko om
    show natsuki cm
    kam "Ага!"
    show yuri flus cm oe
    show kamuko ce
    show natsuki neut cm oe
    kam "В итоге у нас двойная чайная доза!"
    show kamuko cm
    y "Камуко..."
    show kamuko neut cm oe
    show natsuki curi om oe
    n "Ты решила у Юри весь чай высосать?"
    show kamuko om e1b lhiphid rhid
    show natsuki cm
    kam "Это случайно вышло."
    show yuri neut cm e1d
    show kamuko happ om oe
    kam "Изначально я пришла сюда пройти боевое крещение!"
    show kamuko cm
    mc "Куда?"
    show yuri laug cm oe
    show kamuko om
    show natsuki lsur cm oe
    kam "В ваш клуб!"
    show kamuko cm
    n "..."
    mc "...уже?"
    show yuri mb
    y "...у неё есть...{w}потенциал..."
    show yuri cm
    show kamuko om e1c
    kam "Мы пытались 3 раза написать стих, но ничего не вышло."
    show kamuko cm
    mc "Мда уж...{w}весело у вас..."
    show kamuko om ce
    kam "А то!"
    $ ym_name = _("Мама Юри")
    show yuri neut cm e1d
    show kamuko cm
    ym "{size=17}Юри, кто там?{/size}"
    show yuri lsur om oe
    show kamuko oe
    y "О-ой, я сейчас!"
    show yuri cm at thide
    hide yuri
    show kamuko at t21
    show natsuki om e4a lhip rhip at t22
    n "Так."
    show kamuko neut cm oe
    show natsuki doub om oe
    n "С каких это пор ты захотела стать частью нашего клуба?"
    show kamuko doub om oe
    show natsuki cm
    kam "А почему это тебе вдруг стало интересно?"
    show kamuko cm
    show natsuki anno om oe
    n "Потому что клуб у нас и так на шарнирах."
    show kamuko sedu cm oe
    show natsuki angr om oe
    n "А я знаю, какое ты гиперактивное чудовище!"
    show kamuko om ce
    show natsuki vang cm oe
    kam "От клишированной милой аниме-девушки слышу."
    show kamuko cm
    show natsuki om ldown rdown
    n "М-МИЛ--{nw}"
    show kamuko neut cm oe
    show natsuki cm
    mc "ТАК, хватит!"
    show natsuki angr cm oe
    mc "Не хватало тут ещё собачанья между вами."
    show kamuko happ cm oe
    show natsuki anno cm oe
    mc "Камуко приняла решение вступить к нам в клуб -- значит, так оно и будет, ей никто не мешает это сделать."
    show kamuko ce
    show natsuki om ce
    n "Ай, фиг с вами."
    show natsuki cm
    y "{size=19}Ребят...{w}можете зайти в гости...{/size}"
    show kamuko om oe at h21
    show natsuki neut cm oe
    kam "О, прекрасно!"
    show kamuko ce at t22
    show natsuki pani cm oe
    kam "Давайте, пошли-пошли-пошли!"
    show kamuko cm
    show natsuki om ce
    n "Да я сама дойду!--{nw}"
    show kamuko at thide
    hide kamuko
    show natsuki cm at thide
    hide natsuki
    pause 0.2
    mc "Ох..."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play music chill_lofi fadein 3.0
    scene bg yuri house kitchen day
    show natsuki turned black_shirt neut cm e1b at t22 zorder 2
    with wipeleft_scene
    mc "А тут довольно уютно..."
    show natsuki oe
    "Не богато, но и не бедно уж точно."
    show natsuki curi om oe lhip rhip
    n "Ты в гостях у Юри не был?"
    show natsuki cm
    mc "Нет."
    show natsuki neut cm oe
    show yuri_mom happ om ce at t44 zorder 1
    ym "Присаживайтесь!"
    call window_close
    show natsuki ldown rdown
    show yuri_mom cm at thide
    hide yuri_mom
    pause 0.2

    hide natsuki with dissolve
    pause 0.2
    scene bg yuri house kitchen day at yuri_kitchen_table
    show yuri turned sundress happ cm e1b at e21
    show yuri_mom happ cm oe at e22
    with dissolve
    pause 0.25

    call window_open
    kam "Ух, какой аромат!"
    show yuri om oe
    y "Это лаванда?"
    show yuri cm
    show yuri_mom om
    ym "Да, для тебя купила."
    show yuri om e1b b1b n3
    show yuri_mom cm
    y "Ох, спасибо..."
    show yuri cm
    show yuri_mom om ce lup
    ym "Ну, ребят, рассказывайте, как у вас дела?"
    show yuri_mom oe ldown
    ym "И как поживает Литературный клуб?"
    show yuri oe brow n1
    ym "Вижу, уже новое лицо появилось."
    show yuri laug cm oe
    show yuri_mom cm
    kam "И второе на подходе!"
    show yuri_mom happ om eb
    ym "Ха-ха-ха, не без этого."
    show yuri happ cm oe
    show yuri_mom cm oe
    n "Да, мы...{w}расширились в последнее время."
    mc "Юри вам уже про меня рассказала?"
    ym "Угу."
    $ ym_name = _("Ари-сан")
    show yuri_mom om
    ym "Я, кстати, А{image=accent_high_register}{space=-15}ри-сан, переводчица туркомпании Ниигаты, будем знакомы."
    show yuri_mom cm
    mc "Я Макс, взаимно."
    show yuri_mom om
    ym "Ты недавно переехал?"
    show yuri_mom cm
    mc "Да, пару недель назад."
    show yuri_mom om
    ym "А откуда, если не секрет?"
    show yuri neut cm e1d
    show yuri_mom neut cm oe
    mc "Из Мориоки."
    show yuri_mom om
    ym "Ох, так далеко?"
    show yuri_mom cm
    mc "Да, до неё расстояние приличное..."

    scene bg yuri house kitchen day at yuri_kitchen_table_fifth_place
    show kamuko turned casual curi cm oe lhiphid rhid at el11
    with dissolve
    pause 0.25
    show kamuko om
    kam "Подождите, это где?"
    show kamuko cm
    ym "Север острова Хонсю{image=accent_low_register}{space=-15}."
    show kamuko lsur om oe
    kam "Ничего себе!"
    show kamuko curi om oe
    kam "А у вас там медведи не водятся?"
    show kamuko cm
    mc "Какие медведи?"
    show kamuko happ om ce ldown rdown
    kam "Обыкновенные!"
    show kamuko cm
    mc "Причём тут это?"
    show kamuko nerv om oe rface
    kam "По новостям говорили, что стало много голодных медведей, которые людей кушают."
    show kamuko cm
    mc "...?"
    show kamuko neut om oe
    kam "В большом количестве."
    show kamuko cm
    n "Да у нас бы тогда люди вымерли!"
    show kamuko lhiphid rhid
    y "Э-это я Камуко утром рассказала о новости, что на Хоккайдо участились случаи выхода медведей к людям из-за малого количества пищи..."
    mc "А-а, теперь понятно."
    show kamuko anno cm oe
    n "Камуко, как обычно, лютая фантазёрка."
    show kamuko om
    kam "У меня просто в голове всё перемешалось!"
    show kamuko cm
    n "Оно и видно."
    mc "Ладно, хватит."
    show kamuko neut cm oe
    n "Лучше историю про кактус расскажи."
    show kamuko happ om ce ldown rdown
    kam "А-а-а, кактус, да!"
    show kamuko oe
    kam "Короче, когда я была маленькой и безответственной, то есть только начала ходить в школу, мне папа подарил кактус."
    show kamuko neut om e1b lhiphid rface
    kam "Он сказал мне относится к нему бережно и постоянно о нём заботиться."
    show kamuko happ om oe
    kam "Поскольку кактусы неприхотливые, мне нужно было поливать его раз в 2 недели, либо раз в неделю, когда слишком жарко."
    show kamuko rhid
    kam "Я ухаживала за ним, поливала в течение нескольких лет."
    kam "Он как был зелёным, так и оставался, всё было хорошо."
    show kamuko neut om oe
    kam "Но одним летним жарким днём от него стал идти странный запах."
    show kamuko nerv om oe
    kam "А ещё он поменял цвет, который был даже не жёлтый, а бледно-зелёный."
    show kamuko cm
    mc "Это что за кактус такой?"
    show kamuko neut om oe
    kam "Пластиковый."
    show kamuko nerv om oe
    kam "Я все эти несколько лет поливала пластик в форме кактуса, который внутри оказался полый!"
    show kamuko cm
    n "Пха-ха-ха!"
    y "Пх..."
    mc "...как так-то?"
    show kamuko om ce
    kam "А я не знаю!"
    show kamuko oe rface
    kam "Я на него ещё надавила, где у него не было иголок, он вогнулся, как искусственный."
    show kamuko happ om oe rhid
    kam "Не кактус, а искуственная болванка!"
    show kamuko cm
    n "Зато ответственность воспитали, ха-ха-ха!"
    show kamuko om e1b
    kam "Да-а, это уж точно..."
    show kamuko oe
    kam "У меня он до сих пор стоит в комнате, пожухлый уже весь от старости."
    show kamuko cm
    ym "Главное, что ты извлекла из этого полезный урок."
    show kamuko neut om e1c
    kam "Ну...{w}да, соглашусь."
    show kamuko curi om oe
    kam "Но ведь коварно же: вместо кактуса пластиковая шняга!"
    show kamuko cm

    scene bg yuri house kitchen day at yuri_kitchen_table
    show yuri turned sundress neut cm e1d at e21
    show yuri_mom happ cm eb at e22
    with dissolve
    pause 0.25
    show yuri om
    show yuri_mom oe
    y "Кстати, как там...{w}в Мориоке..."
    y "Там же прохоладнее, чем у нас, верно?"
    show yuri cm
    mc "Угу."
    mc "Не сильно, конечно, но зимой бывает до -8 градусов со снегом."
    show yuri_mom om
    ym "У нас тоже зимой иногда снег выпадает, но не так часто."
    show yuri_mom neut om oe lup rup
    ym "Хотя в последнее время природа что-то разбушевалась: год назад в южных частях страны выпал снег, когда его там не было более 100 лет."
    show yuri anno om oe
    show yuri_mom cm ldown
    y "В этом году у нас в январе был зафиксирован рекорд по выпадению осадков..."
    show yuri cm
    show yuri_mom om eb
    ym "Да, жуть творится."
    show yuri neut cm e1d
    show yuri_mom cm
    n "Помнится, у нас тогда занятия в школе отменили."
    show yuri_mom oe
    kam "Ха, было дело!"
    show yuri_mom happ cm oe
    kam "Дополнительные зимние каникулы."
    mc "Ужас..."
    mc "Нас это не так сильно коснулось."
    show yuri om
    y "А у вас много достопримечательностей?"
    show yuri cm
    mc "Э-э-э..."
    show yuri laug cm oe
    show yuri_mom om ce rdown
    ym "Юри у нас любительница парков и различных памятных мест, особенно если в них немноголюдно."
    show yuri_mom cm
    mc "Ха."
    show yuri happ cm oe
    show yuri_mom oe
    mc "Ну, у нас не так много интересного."
    mc "Парков мало, да и сами по размеру они не очень большие."
    show yuri neut cm e1d
    mc "Хотя в одном из них есть руины замка Мориока."
    mc "А рядом с ними, чуть севернее, есть сакура, которая умудрилась прорасти сквозь большой камень, расколов его пополам."
    show yuri om
    y "Ох..."
    show yuri cm
    show yuri_mom om
    ym "Интересно."
    show yuri_mom cm
    mc "Ещё у нас есть парк Такама{image=accent_low_register}{space=-15}цу, в котором есть озеро, где можно поплавать на лодке."
    mc "А в целом так ничего особенного."
    mc "Разве что ещё через наш город протекает 3 реки: одна на западе, Шидзукуи{image=accent_low_register}{space=-15}ши, другая на севере, Китака{image=accent_low_register}{space=-15}ми, а третья на востоке, Нака{image=accent_low_register}{space=-15}цу."
    mc "Впадают все в Китаками и утекают на юг."
    mc "Они тоже не очень большие, набережных практически нет."
    mc "Зато лесопарков на окраинах города целое море."
    show yuri_mom om
    ym "У вас много, где властвует природа?"
    show yuri_mom cm
    mc "Да нет, не настолько."
    mc "Просто у нас реальный город только в центре."
    mc "Если из центра уйти, то больше ощущение некого пригорода."
    mc "Здесь, в Ниигате, урбанизация чувствуется сильнее."
    show yuri e1b
    show yuri_mom om
    ym "Вот как."
    show yuri om
    show yuri_mom cm
    y "Хотелось бы в будущем побывать в Мориоке..."
    show yuri cm
    show yuri_mom om ce
    ym "Ха-ха, всё будет, обязательно."
    show yuri laug cm ce
    show yuri_mom oe
    ym "Любопытная, а ещё такая большая, -- прямо вся в папу."
    play phone_sound new_message_mc
    show yuri_mom cm
    pause 1.0
    stop music fadeout 3.0
    show yuri neut cm e1d
    mc "Оп, простите, секунду."
    call skip_block_on

    phone register "mc_m_chat":
        "m" "Макс, снова привет"

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 42
        clock = (12, 21)

    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "m" "У родителей там что-то по работе, в общем они сейчас сказали, что сегодня уедут пораньше"
        "m" "Поэтому, нисколько тебя не заставляю и не гоню вперёд паровоза..."
    show yuri_mom eb with None
    phone discussion "mc_m_chat":
        "m" "Но если ты хочешь с ними познакомиться, то тебе лучше стоит сделать это сейчас"
    "Блин, мы только уселись и разговорились!"
    show yuri e1b
    "Некрасиво сейчас будет уйти...{w}но выбора нет."
    $ phone.system.clock = (12, 22)
    "Захотят снова увидеть меня в гостях -- зайду, если будет возможность."

    phone end discussion transition

    call skip_block_off
    show yuri lsur cm oe
    show yuri_mom neut cm oe
    mc "Прошу прощения, но у меня срочное дело образовалось, мне надо идти."
    show yuri om
    y "Уже?"
    show yuri cm
    kam "И часа не прошло, а ты уже уходишь?!"
    show yuri_mom happ om oe lup
    ym "Если дело срочное, то не задерживаем."
    show yuri_mom cm ldown
    n "Так, э-э-э...{w}мне бы тоже по-хорошему уйти, меня папа дома ждёт..."
    show yuri laug cm e1a
    kam "Опять, только собрались и уже расходимся!"
    show yuri mb oe
    y "Камуко, не переживай...{w}соберёмся ещё в ближайшее время."
    show yuri cm
    show yuri_mom om
    ym "Да, это можно будет организовать."
    show yuri e1a
    show yuri_mom cm
    mc "Ладно, извините, мы пойдём."
    show yuri_mom om
    ym "До встречи!"
    show yuri_mom cm
    kam "Эх, пока..."
    show yuri mb ce
    y "Д-до завтра!"
    show yuri cm
    n "Пока."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show natsuki turned black_shirt fc happ cm oe lhip rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Ну что, как я, а?"
    show natsuki cm
    mc "Ты про что?"
    show natsuki om
    n "Как я Камуко на разговор развела."
    show natsuki ce
    n "Я, между прочим, это специально сделала, чтобы Юри не успела тобой «проникнуться»."
    show natsuki cm
    mc "Нифига себе."
    show natsuki oe
    mc "Это ты уже действовать начала?"
    show natsuki om
    n "Ага, чего время терять?"
    show natsuki cm
    mc "Да, коварные вы, женщины."
    show natsuki laug cm ce
    mc "И глазом не моргнёшь, уже работаете во всю."
    show natsuki om
    n "Хорош прикалываться, тебя спасаю!"
    show natsuki cm
    mc "Ладно-ладно."
    show natsuki neut cm oe
    mc "Ну это...{w}до завтра?"
    show natsuki om ldown rdown
    n "Точно, тебе же сейчас к Монике..."
    show natsuki happ om ce
    n "Да, пока-пока."
    show natsuki cm
    mc "Пока."
    show natsuki oe at thide
    hide natsuki
    pause 1.0
    mc "К Монике..."
    mc "Пф-ф-ф..."
    "Опять к её родителям..."

    scene black with wipeleft_scene
    "Нет, её отца понять можно."
    "Я бы, наверное, так же поступил, если бы точно знал его планы на единственную дочь."
    "Родители (нормальные, конечно же) всегда хотят дать своему ребёнку всё самое лучшее, чтобы обеспечить ему хорошую стабильную жизнь."
    "Вот только: «а» -- это не всегда возможно ввиду причин, которые я сейчас не буду разбирать; и «б» -- иногда родители с этим перегибают палку."
    "Я бы даже сказал: «Ломают»."
    "И самое отвратительное здесь -- это найти хрупкий баланс."
    "Потому что пойти не так может что угодно."
    "И в случае с Моникой...{w}оно уже пошло."
    "Вопрос только в том, насколько сильно это повлияет на ситуацию."

    scene bg monika house outside day with wipeleft_scene
    mc "А может быть...{w}не надо было мне в Литературный клуб вступать..."
    "Тогда бы с Моникой диллемы не было."
    "Ведь я её инициатор, как ни крути."
    "Но с другой стороны, кто бы остальным хоть как-то помог?"
    "Кто бы положил начало «оживлению» клуба?"
    "Да и вообще, вдруг Моника позже нашла бы себе другого парня!"
    "Тогда от моего «невступления» ничего бы не поменялось."
    "Уж лучше я, с нормальными мозгами, попытаюсь взять ситуацию в свои руки и аккуратно выправить её на «спокойную дорожку», чем это будет делать кто-то другой."
    mc "Так, всё!"
    mc "Неизбежного не избежишь."
    "Единственное, что меня гложет -- это то, что вечером я буду лежать в своей постели, вспоминая об этом моменте в прошлом."
    "Поэтому давайте приблизим этот момент."
    call window_close

    scene bg monika house outside day at monika_gate
    with dissolve
    pause 0.5
    play sound doorbell_monika
    pause 2.0
    play sound doorbell_monika
    pause 5.0

    call window_open
    mc "{size=19}...ну же...{/size}"
    call window_close

    pause 5.0

    call window_open
    m "{size=19}Макс?{/size}"
    m "{size=19}Ты наконец-то пришёл!{/size}"
    mc "Угу."
    m "{size=19}Заходи быстрее, не стой снаружи.{/size}"
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day with wipeleft_scene
    "Так, пока Моника отошла оповещать родителей о моём присутствии, мне надо подумать, как я буду реагировать на её отца..."
    "Почему я об этом пару минут назад не подумал?!"
    "Он же меня с потрохами сожрёт и не покорчится!"
    mc "{size=19}Мх-х-х...{/size}"
    "Слабину точно давать нельзя: я должен показать себя с уверенной стороны."
    "Но и задирать нос тоже не стоит: будут считать типичным пубертатным максималистом-понторезом, а таким я даже близко не являюсь."
    mc "{size=19}Думай своей тупой башкой, думай...{/size}"
    "..."
    "Эмоции я точно показывать не должен, как минимум сильно."
    "Подождите..."
    "Меня же часто называли в школе роботом за усердие в учёбе."
    "В хорошем смысле, естественно."
    "Почему бы...{w}не оправдать это прозвище?"
    "Реально, я просто сконцентрирую внимание на отце Моники, сделаю нейтральное лицо, которое готово к любому виду разговора."
    "А чтобы не соскочить с этого состояния, я буду смотреть ему не в глаза, а в переносицу."
    "Так и мне проще станет, и визуальный контакт будет сохранён."
    "Осталось только приготовиться и дождаться--{nw}"
    show uncle_martin neut cm oe at t11
    pause 0.2
    show uncle_martin happ om oe
    um "Юноша, снова здравствуйте."
    show uncle_martin cm
    mc "О, здравствуйте!"
    show uncle_martin sad om oe
    um "Наслышан о вчерашней перепалке, сожалею, что так вышло."
    show uncle_martin cm
    mc "Да не, не переживайте, всё в порядке."
    show uncle_martin neut om oe
    um "Я знаю мистера Дэна ещё с давних времён: в личной жизни он консервативный человек, несмотря на свою бурную рабочую карьеру."
    show uncle_martin happ om oe
    um "Однако я уверен, что в конечном итоге он Вас примет."
    show uncle_martin cm
    mc "Хм."
    show uncle_martin om
    um "Просто учтите это в голове."
    show uncle_martin cm
    mc "Да, хорошо."
    show monika forward green_hoodie happ cm oe at t21
    show uncle_martin at t22
    pause 0.2
    show monika om ce lpoint rhip
    m "Макс, пойдём на кухню!"
    show monika cm oe ldown
    mc "Туда?"
    show monika om
    m "Поговорим за вкусняшками!"
    show monika ce
    m "Нечего тут диван просиживать."
    show monika cm
    mc "Хорошо-хорошо."
    show monika om oe
    show uncle_martin neut cm oe
    m "Дядя, ты не хочешь присоединиться?"
    show monika neut cm oe
    show uncle_martin sad md oe
    um "Нет, дорогая, мне завтрака за глаза хватило."
    um "К тому же надо готовиться к отъезду."
    show monika om e1b
    show uncle_martin mc
    m "Эх, ладно."
    show monika happ om oe
    show uncle_martin happ cm oe
    m "Всё, Макс, пойдём!"
    show monika cm ce rdown at thide
    hide monika
    pause 0.2

    scene black with wipeleft_scene
    "Мда, променял одну чайную посиделку на другую."
    "И подумать утром не мог, что такое сегодня случится."
    "Что не день, то неожиданное «приключение»."

    scene bg monika house kitchen day with wipeleft_scene
    mc "Здравствуйте."
    md "{size=19}Здравствуй.{/size}"
    mm "{size=19}Привет.{/size}"
    "Ну что, поехали, «попытка номер два»..."
    m "{size=19}Присаживайся!{/size}"
    call window_close

    scene bg monika house kitchen day at monika_kitchen_table
    show monika_mom cross casual happ cm oe at e21
    show monika_dad casual neut cm oe at e22
    with dissolve
    pause 0.25

    call window_open
    show monika_mom neut cm oe
    mc "Я хотел бы извиниться за своё вчерашнее поведение."
    mc "Я вчера был уставший и при этом на нервах."
    show monika_mom happ cm oe
    show monika_dad om
    md "М-м, я тоже хотел бы принести извинения за проявленную мною грубость."
    show monika_mom sedu cm oe
    md "Однако моя позиция остаётся неизменной."
    play music chill_lofi fadein 3.0
    show monika_dad cm
    m "Папа..."
    show monika_mom om
    mm "Дайсуке, не будь таким жестоким."
    show monika_mom happ om oe
    mm "Ты же ведь как-то женился на мне?"
    show monika_mom cm
    show monika_dad om
    md "Женился."
    md "Но было это, когда я уже сформировал под это материальную и психологическую основу."
    show monika_mom om ce
    show monika_dad cm
    mm "А по-моему у тебя просто не было выбора."
    show monika_mom cm
    show monika_dad om
    md "Не дурачься, Харуми."
    show monika_dad cm
    "Теперь понятно, в кого Моника такая «игривая»."
    show monika_mom oe
    m "Папа, нам никто же не мешает общаться на расстоянии!"
    m "На мою успеваемость в учёбе Макс никак не повлияет."
    m "Иначе бы она уже ухудшилась."
    show monika_dad om
    md "Я не могу быть уверен, что ты не поменяешься в будущем."
    show monika_mom om
    show monika_dad cm
    mm "А я не уверена, что Монике станет легче, когда у неё не будет отношений."
    show monika_mom sedu om oe
    mm "Дайсукэ, не будь таким категоричным."
    show monika_mom happ om oe
    mm "Ты должен радоваться, что твоя дочь самостоятельно нашла себе уверенного парня, который готов её поддержать без чрезмерной опеки."
    mm "Если всё, что рассказала Мони про Макса, правда."
    show monika_mom cm
    m "Гарантированно."
    show monika_dad om
    md "М-м-м, раз ты настаиваешь, то тогда попробуем узнать друг друга получше."
    md "Времени до полного отъезда из Японии у нас пока хватает, но его уже осталось меньше года."
    md "Что же можешь рассказать про себя, Макс?"
    md "Характер, увлечения, таланты, способности..."
    show monika_mom om ce
    show monika_dad cm
    mm "Не стесняйся, и не нужно формальностей: у нас не собеседование на работу, как может показаться."
    show monika_mom cm
    mc "Хорошо."
    show monika_mom oe
    mc "Э-э, мне 18 лет, пару недель назад я переехал из Мориоки в Ниигату, чтобы жить здесь на постоянной основе."
    mc "По характеру я спокойный и стараюсь быть уравновешенным, хотя не всегда это получается..."
    mc "Стараюсь анализировать ситуацию и принимать взвешенное решение без эмоций."
    mc "В школе я учусь успешно и проблем с ней никогда не было ни в учебном, ни в социальном плане."
    show monika_mom neut cm oe
    mc "Однако у меня за всю жизнь было мало друзей и вообще людей, с которыми я мог бы провести время."
    mc "В последнее время единственным другом была только Сайори."
    mc "Которая затянула меня в Литературный клуб после первой недели учёбы в новой школе."
    show monika_mom happ cm oe
    mc "Там я подружился со всем маленьким коллективом и как раз познакомился с Моникой."
    mc "Ну и в свободное от учёбы время я иногда изучаю программные языки."
    show monika_dad om
    md "Какие?"
    show monika_dad cm
    mc "{color=#fc7e23}Python{/color}."
    mc "Ещё немного {color=#fc7e23}C-Sharp{/color}."
    mc "В будущем хочу наверстать {color=#fc7e23}C++{/color}."
    mc "О, а также потихоньку изучаю систему контроля версий {color=#fc7e23}Git{/color}."
    show monika_mom sedu cm oe
    show monika_dad om
    md "Хороший набор для начинающего разработчика приложений..."
    show monika_mom om
    show monika_dad cm
    mm "Уже рассматриваешь его, как будущего стажёра?"
    show monika_mom cm
    show monika_dad om
    md "Не исключаю такой сценарий развития событий."
    show monika_mom neut om oe
    show monika_dad cm
    mm "Вообще странно: с виду проблем с внешностью у тебя нет, ты парень достаточно примечательный, а друзей мало."
    mm "Как так получилось?"
    show monika_mom cm
    mc "Если бы я сам знал."
    show monika_mom om
    mm "Отсутствует подача?"
    show monika_mom cm
    mc "Я и не горю желанием светиться на публику."
    mc "Из сверстников меня никто не привлекал и мне никто не симпатизировал."
    show monika_mom om
    md "Они вовсе не рассматривают тебя?"
    show monika_mom cm
    mc "Нет."
    mc "Я мимикрирую с окружением."
    show monika_mom om
    mm "Очень странно."
    show monika_mom cm
    show monika_dad om
    md "Да, не очень хороший показатель человека, если быть откровенным."
    md "Однако нельзя отрицать, что и сверстники «хороши»."
    md "Ведь в клубе ты нашёл своё место?"
    show monika_dad cm
    mc "Более чем."
    show monika_mom happ cm oe
    m "Его приняли, как миленького!"
    m "Благодаря нему у нас оживился клуб и мы наконец-то стали пополняться людьми!"
    m "Медленно...{w}но верно."
    show monika_dad om
    md "Что ж, это радует."
    show monika_dad cm
    mc "В целом, мне больше нечего рассказать."
    show monika_mom om
    mm "А почему переехал именно в Ниигату, если не секрет?"
    show monika_mom cm
    mc "Получить более лучшее обучение и работу."
    mc "Ну и тут жильё хорошее попалось, которое, как уже сказал, должно быть моим постоянным на ближайшее время."
    show monika_dad om
    md "Значит, с финансами у вас проблем нет?"
    show monika_dad cm
    mc "Нет, даже близко нет."
    show monika_dad om
    md "Это тоже радует."
    show monika_mom sedu om oe
    show monika_dad cm
    mm "Думаешь, у Макса будут проблемы с финансами?"
    show monika_mom cm
    show monika_dad om
    md "Всякое может быть."
    md "В Японии до сих пор экономическая стагнация, которая постоянно рискует впасть в рецессию."
    md "А это приведёт к ухудшению экономики и всей жизни в целом, хоть и не сразу."
    show monika_mom om
    show monika_dad cm
    mm "Ой, Дайсуке, поверь, тут не будет сумасшедших скачков и падений."
    show monika_mom happ om ce
    mm "Ещё когда я работала ландшафтным дизайнером, мне хватало на обеспечение семьи, на необходимые расходы и на откладывание на отпуск."
    show monika_mom oe
    mm "А было это в конце 90-ых годов."
    show monika_mom cm
    show monika_dad om
    md "Уже столько времени с того момента прошло?"
    show monika_mom om ce
    show monika_dad cm
    mm "Ой, и не говори."
    mm "Будто ещё вчера ездила по стране и занималась эскизами..."
    show monika_mom cm
    show monika_dad om
    md "О, Мартин."
    show monika_dad cm
    um "{size=19}Да?{/size}"
    show monika_mom sedu cm oe
    show monika_dad om
    md "Помнишь, как ты в молодости рассекал по гоночным трассам?"
    show monika_dad cm
    um "{size=19}О-о-о, было дело.{/size}"
    um "{size=19}Я даже одно соревнование выиграл.{/size}"
    mc "Ничего себе..."
    show monika_mom happ cm oe
    m "Да, дядя Мартин может дать жару на машине!"
    show monika_mom om ce
    mm "Ух, в одной поездке он даже слишом перестарался."
    show monika_mom cm
    um "{size=19}Всё было под контролем.{/size}"
    show monika_mom om
    mm "Охотно верим."
    show monika_mom cm
    um "{size=19}Да и не по мне эта высокая динамика.{/size}"
    um "{size=19}Всё-таки тише едешь -- дальше будешь.{/size}"
    show monika_mom oe
    show monika_dad om
    md "Я так понимаю, что уже всё готово, Мартин?"
    show monika_dad cm
    um "{size=19}Да, только хотел сообщить.{/size}"
    um "{size=19}Можете уже собираться.{/size}"
    show monika_mom sedu cm oe
    m "Уже уезжаете?"
    show monika_dad om
    md "Да, нельзя сильно оттягивать, как бы мы ни хотели."
    show monika_mom happ om ce
    show monika_dad cm
    mm "Главное, что мы успели познакомиться с твоим парнем."
    show monika_mom cm
    mc "Это точно."
    show monika_mom om oe
    mm "Только Дайсуке про себя не рассказал."
    show monika_mom cm
    show monika_dad om
    md "Я вчера уже говорил ему про компанию."
    show monika_mom om
    show monika_dad cm
    mm "А про штат Нью{image=accent_low_register}{space=-15}-Дже{image=accent_low_register}{space=-15}рси, где ты родился?"
    mm "Или Чика{image=accent_low_register}{space=-15}го, где ты отучился в сфере бизнес-администрирования?"
    show monika_mom cm
    show monika_dad om
    md "А что про них рассказывать?"
    md "Особо ничего интересного там нет."
    md "Ладно, был рад нашему успешному знакомству."
    show monika_dad cm
    mc "Да, я рад, что нам удалось поладить."
    show monika_mom ce
    show monika_dad om
    md "Пойдём, дорогая."
    call window_close

    show monika_dad cm:
        ease 0.75 yoffset 100
    pause 0.5
    show monika_mom:
        ease 0.75 yoffset 100
    hide monika_dad with easeoutright
    pause 0.1
    hide monika_mom with easeoutright
    pause 0.5
    show monika forward green_hoodie happ cm oe at e21 with easeinleft
    pause 0.5
    show monika om lpoint

    call window_open
    m "Жаль, что сейчас у родителей времени в обрез, но как твои впечатления от первого нормального общения?"
    show monika cm ldown
    mc "Ты ещё спрашиваешь?"
    mc "Я ожидал, что всё будет тяжелее и труднее, а тут с ходу удалось нормально поговорить."
    show monika om ce
    m "Вот видишь, не всё так плохо!"
    show monika oe
    m "Просто в первый раз не задалось."
    show monika cm
    mc "Осадок всё равно какой-то остался."
    show monika neut cm oe
    mc "Тебя же ведь в любом случае заберут."
    show monika om
    m "Боишься потерять меня?"
    show monika cm
    mc "..."
    mc "Давай честно, поддерживать в таком состоянии отношения будет реально сложно."
    show monika happ cm oe b1b
    mc "И мне это ничерта не нравится."
    show monika om
    m "Мне тоже, Макс, но мы же обещали друг другу, что преодолеем все трудности, верно?"
    show monika cm brow
    mc "...да."
    show monika om ce
    m "Поэтому это лишь очередная трудность на нашем пути."
    show monika oe
    m "И вообще, у нас ещё полдня впереди!"
    show monika curi mb oe
    m "Ты же хотел полноценное свидание, а?"
    show monika happ om oe lpoint
    m "Давай не будем терять время зря."
    show monika cm ldown
    mc "Предлагаешь куда-то сходить?"
    show monika om ce
    m "Конечно!"
    show monika curi mb oe
    m "Или как ты себе это представляешь?"
    show monika ma
    mc "Ты прям вся завелась."
    show monika happ cm oe
    mc "Снова на веселе?"
    show monika om ce
    m "А то, ха-ха!"
    show monika oe
    m "Так что, какие есть идеи?"
    show monika cm
    mc "М-м-м..."
    mc "Как-будто бы хочется просто где-то прогуляться."
    show monika om
    m "Соглашусь."
    show monika nerv mb oe
    m "Сходить в какое-то заведение сейчас мы пока не можем, потому что...{w}ну, мне немножко прилетело за вчерашние траты..."
    show monika cm
    mc "Блин, точно."
    show monika happ cm oe
    mc "Я же обещал тебе отдать деньги за себя."
    show monika om
    m "Ой, не торопись."
    m "Можешь сделать это позже."
    show monika cm
    mc "Завтра отдам, иначе потом забуду."
    show monika om
    m "Дело твоё."
    show monika cm
    mc "Ладно, насчёт прогулки..."
    show monika neut cm oe
    mc "Я вот не знаю, есть ли здесь какие-нибудь близлежайшие парки или интересные места?"
    mc "Потому что до набережной на севере мы помрём идти."
    show monika e1b
    mc "К тому же там места открытые, сгорим на солнце, хоть сейчас и не лето."
    m "М-м-м..."
    mc "..."
    m "..."
    mc "У меня реально нет идей."
    show monika om oe lpoint
    m "Может, тогда посетим то место, где впервые встретились?"
    show monika cm ldown
    mc "Тот парк?"
    mc "Мы там уже вчера были."
    mc "И там смотреть особо нечего."
    show monika happ om oe
    m "Зато там много деревьев, а значит -- тень хорошая."
    m "И посетим ту роковую то{image=accent_low_register}{space=-15}рии."
    m "Всё равно других вариантов нет."
    show monika e1b
    m "Но на набережную надо будет сходить."
    show monika e1c
    m "А может быть, и на озеро Тоя{image=accent_low_register}{space=-15}но Га{image=accent_low_register}{space=-15}та в центре города."
    show monika cm
    mc "Точно, про него я забыл..."
    show monika om oe lpoint
    m "Туда лучше приходить в период цветения сакуры, я была там как раз в начале апреля."
    show monika ce ldown
    m "Было очень красиво!"
    show monika e1b b1b
    m "Жаль, что уже всё отцвело..."
    show monika cm
    mc "Думаю, как-нибудь в будущем там будем."
    show monika oe brow
    mc "Или съездим в более лучший парк."
    show monika om ce
    m "Не сомневаюсь!"
    show monika cm
    mc "Значит, решено?"
    show monika om oe
    m "Да."
    show monika cm
    mc "Только я в таком виде...{w}у меня уже, наверное, весь запах спрея-дезодоранта выветрился."
    show monika sedu om b1f
    m "Ой, не переживай."
    m "Меня всё устраивает."
    show monika happ om ce brow
    m "Мы же не в помещении будем."
    show monika cm
    mc "...хорошо."
    show monika om oe lpoint
    m "Давай тогда сейчас попращаемся с родителями, а потом я переоденусь, а ты меня подождёшь в гостиной."
    show monika cm ldown
    mc "Да, конечно."
    stop music fadeout 3.0

    scene black with wipeleft_scene
    "Прямо легче на душе стало, что всё так хорошо обошлось."
    mc "Фух..."
    mm "{size=19}Дорогая, мы уходим!{/size}"
    m "Ой, Макс, скорее, попрощаемся с родителями и дядей!"
    mc "Да-да-да, иду."

    scene bg monika house livingroom day
    show monika forward green_hoodie happ cm oe at t41 zorder 2
    show monika_mom happ cm oe at t42
    show monika_dad neut cm oe at t43 zorder 2
    show uncle_martin happ cm oe at t44
    with wipeleft_scene
    show uncle_martin om
    um "Точно всё забрали?"
    show monika_mom om
    show uncle_martin cm
    mm "Да, все вещи с собой."
    show monika_mom cm
    show monika_dad om
    md "Я уже проверил, мы готовы."
    show monika om
    show monika_dad cm
    m "До следующего месяца?"
    show monika cm
    show monika_dad om
    md "Разумеется."
    show monika ce
    show monika_mom sedu om oe
    show monika_dad cm
    mm "Береги себя."
    show monika_mom happ om oe
    mm "А ты защищай её, если что-то случится."
    show monika oe
    show monika_mom cm
    mc "Э-э, да."
    show monika e1b b1b
    show monika_mom om ce
    mm "Ха-ха-ха!"
    show monika oe brow
    show monika_mom cm
    show uncle_martin om
    um "Всего вам наилучшего."
    show monika om ce
    show monika_mom oe
    show uncle_martin cm
    m "До встречи!"
    show monika cm
    mc "До свидания."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg monika house livingroom day with wiperight
    "Как тихо тут стало..."
    "..."
    mc "{size=19}Ну и где Монику носит?{/size}"
    "Уже минут 5 прошло, наверное, если не больше, а её всё нет."
    "Я понимаю, что у нас свидание (если это так можно назвать) и Моника хочет выглядеть подобающе, но...{w}я не из тех, кто требует всё по высшему разряду."
    "Потому что я и сам его обеспечить не в состоянии."
    "..."
    mc "Эх..."
    "С другой стороны, мы никуда не торопимся."
    "А диван тут такой мягкий..."
    m "{size=19}Ну что, Макс?{/size}"
    "Чёрт, я только пригрелся!"
    show monika forward white_dress happ cm oe at t11
    pause 0.2
    show monika om lpoint rhip
    m "Готов к нашему первому свиданию?"
    show monika cm ldown
    mc "Ого, то самое платье?"
    show monika lean white_dress happ om ce at h11
    m "Ага!"
    show monika forward white_dress happ om oe rhip
    m "Так что?"
    show monika cm
    mc "Всегда готов!"
    show monika om ce
    m "Тогда вперёд!"
    show monika cm
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    show bg monika house outside day
    show monika forward white_dress happ cm e1b at t11
    with wipeleft_scene
    show monika oe
    mc "Твои родители реально такие кардинально разные?"
    mc "Твой папа хладнокровен и твёрд, а мама мягкая и весёлая, прямо как ты."
    show monika om
    m "В большинстве случаев."
    show monika e1b
    m "Не обольщайся первым контактом."
    show monika nerv mb oe n2
    m "Иногда моя мама пугала своим гневом и меня, и папу..."
    show monika cm
    mc "Это что такого должно произойти, чтобы твоя мама дошла до такого состояния?"
    show monika mb ce
    m "Ну...{w}хе-хе...{w}иногда я, будучи маленькой, ерунду совершала, иногда случалось что-то другое..."
    show monika cm
    mc "Ясненько."

    scene bg niigata street suburban 16 day
    show monika forward white_dress happ cm e1c at t11
    with wipeleft_scene
    show monika oe
    mc "Возможно, я повторю мысль твоих родителей относительно времени, но..."
    show monika lsur cm oe
    mc "...даже не верится, что прошёл практически месяц с момента нашей встречи."
    show monika om
    m "Месяц?"
    show monika cm
    mc "Ну, я приехал 2 апреля, а встретился с тобой на следующий день."
    mc "А сейчас уже 29 апреля."
    show monika om e2b
    m "Ого..."
    show monika cm
    mc "Сам в шоке."
    "..."
    show monika happ om oe lpoint rhip
    m "Могу его, кстати, усилить."
    show monika cm ldown
    mc "Кого \"его\"?"
    show monika om
    m "Твой шок."
    show monika cm
    mc "И как же?"
    show monika om
    m "Наша встреча не была случайной."
    show monika cm
    mc "Пф, намёк на судьбу?"
    show monika om ce
    m "Нет, я её запланировала."
    show monika cm
    mc "В смысле?"
    show monika om oe
    m "Мне Сайори немного про тебя рассказала, а потом сообщила о твоём переезде."
    m "Вот я и подумала, что в целом ты человек хороший, мог бы вступить к нам."
    show monika ce
    m "И чтобы повысить шансы, я решила лично с тобой подружиться."
    show monika cm
    mc "..."
    show monika oe
    mc "...зачем так сложно?"
    show monika lean white_dress happ om ce at h11
    m "Зато весело!"
    show monika forward white_dress curi mb oe rhip
    m "Да и откуда я могла быть уверена, что всё пройдёт хорошо?"
    show monika ma
    mc "Хм-м-м..."
    show monika happ cm oe
    mc "Значит, если бы я не был хорошим кандидатом на вступление в клуб, то ты бы меня продинамила?"
    show monika nerv mb oe n2
    m "Э-э-э...{w}хе-хе..."
    show monika ce lpoint rdown
    m "Не думаю, я бы в тот день всё равно была в парке."
    show monika happ om oe ldown n1
    m "И даже если бы мы там не встретились, то обязательно увиделись бы в школе."
    m "А там бы и подружились."
    show monika cm
    mc "Ну ладно, хитрюжка, убедила."
    show monika om ce
    m "А-ха-ха!"
    show monika cm

    scene bg niigata street suburban 15 day
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    show monika lean white_dress happ om oe at h11
    m "А когда ты меня познакомишь со своими родителями?"
    show monika cm
    mc "Куда ж так сразу?"
    show monika forward white_dress happ om oe lpoint
    m "Не вижу смысла ждать."
    show monika neut cm oe ldown
    mc "Это будет тяжело организовать."
    mc "Хотя можно попробовать и дистанционно, но я не знаю, как всё пройдёт."
    mc "Лучше уж вживую, но, как сказал, сделать это сейчас практически нереально."
    m "Хм..."
    mc "А зная, какая волнительная у меня мама..."
    show monika curi om oe
    m "Она за тебя сильно переживает?"
    show monika md oe
    mc "Не прям так, но иногда да."
    show monika neut cm oe
    mc "Поэтому я и хочу, чтобы всё прошло вживую."
    mc "Так нервов будет меньше."
    show monika om e1b
    m "Ясно, значит, в ближайшее время этого не будет."
    show monika cm
    mc "Угу."
    show monika happ cm oe
    mc "Но мы что-нибудь потом придумаем."
    show monika om rhip
    m "Очередная трудность, с которой нам надо справиться."
    show monika cm
    mc "Да, очередная..."
    show monika ce
    "Эти практические непреодолимые трудности по количеству растут, как дрожжах."

    scene bg niigata street suburban 11 afternoon
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    show monika neut cm oe
    mc "О, кстати, насчёт Нацуки..."
    show monika om
    m "Что такое?"
    show monika cm
    mc "Она решила помочь мне, поубавив пыл Юри."
    show monika curi om oe rhip
    m "Да ладно, она тоже вошла в нашу «игру»?"
    show monika md
    mc "Угу."
    show monika neut cm oe
    mc "И это при том, что раньше она обещала ей помочь со мной сблизиться."
    mc "Но вряд-ли для этого что-то сделала."
    mc "По крайней мере за всё время я ничего такого не заметил."
    show monika om e1b
    m "Да, страсти накаляются."
    show monika oe
    m "Ты ещё не нашёл психолога?"
    show monika cm
    mc "Нифига."
    show monika curi md oe
    mc "Но у меня такое чувство, что мне не хватает какой-то маленькой детали для его нахождения."
    show monika om rdown
    m "...имени аккаунта?"
    show monika cm
    mc "Нет, не в этом плане."
    show monika neut cm oe
    mc "Буквально вспомнить сочетание нескольких символов и всё."
    show monika b1d
    mc "Но у меня никак не получается, хоть убей."
    show monika om
    m "Но-но-но!"
    show monika brow lpoint
    m "Не надо так говорить, иначе поверишь в это."
    show monika happ om oe ldown rhip
    m "У тебя всё получится, просто надо ещё постараться."
    show monika cm
    mc "Да куда я денусь?"
    mc "Понятное дело, что надо ещё делать."
    show monika neut cm oe
    mc "Но эта безрезультатная рутина уже очень раздражает."
    show monika om b1b
    m "Знаю, но по-иному сейчас никак."
    m "Ты единственный, кто может его найти."
    show monika cm
    mc "Прекрасно понимаю."
    show monika e1b

    scene bg residential_day
    show monika forward white_dress neut cm e1b at t11
    with wipeleft_scene
    mc "Так, вроде мы вчера туда шли...{w}точнее, бежали."
    show monika happ om oe lpoint
    m "Верно, нам туда."
    show monika cm ldown
    mc "Ой, нам отсюда ещё километр с чем-то топать, ужас..."
    show monika om ce
    m "Не развалимся."
    m "Давай, веселее шаг!"
    show monika cm
    "...кажется, у меня снова дежавю."
    "Эту фразу же мне Сайори когда-то на прошлой неделе говорила?"
    show monika e1b
    call window_close

    call plot_transition

    call window_open
    scene bg niigata park japanese entrance stairs
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    mc "А вот и роковой парк..."
    show monika om ce
    m "Хах, да, это самое подходящее название."
    show monika cm
    mc "Только как мы по нему пойдём?"
    show monika neut om oe
    m "Тут не так много маршрутов."
    show monika cm
    mc "Ну, например, мы можем пройтись по моему пути."
    mc "Только там камней много."
    show monika happ om oe
    m "Ничего, у меня толстая подошва."
    show monika lpoint
    m "Через неё камни ощущаются, как массажёр."
    show monika cm ldown

    scene bg niigata park japanese path 1
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    mc "Значит, не у одного меня возникали такие ассоциации..."
    show monika om b1f
    m "Ха-ха, но ведь приятно же ощущается, а?"
    show monika cm
    mc "Да, есть такое."
    show monika neut cm oe brow
    mc "Кстати, нам сейчас налево."
    show monika om
    m "А, ты шёл не по этой дороге?"
    show monika cm
    mc "Неа."
    mc "Мы здесь с Сайори поспорили, кто быстрее добежит до выхода разными путями."
    show monika happ cm oe
    mc "Я и глазом моргнуть не успел, как она убежала по этой дороге за поворот."
    show monika om ce
    m "Хах, Сайори себе не изменяет."
    show monika cm

    scene bg niigata park japanese path 4
    show monika forward white_dress neut cm e2a at t22
    with wipeleft_scene
    show monika om
    m "Ох, как тут тихо и красиво..."
    show monika cm e2b
    mc "Ага, здесь по-своему уютно."
    show monika om
    m "За пару моих посещений я всегда шла по асфальтированной дороге и обходила эту тропу стороной..."
    show monika worr om ce
    m "Зря я это делала."
    show monika pani om e4c at h22
    m "А-А-А!!!--{nw}" with vpunch
    call window_close

    play sound hugs
    hide monika
    show monika forward white_dress pani cm e4c at e11
    with dissolve
    pause 0.25

    call window_open
    mc "СТОЯТЬ, НЕ ПАДАТЬ!"
    mc "Всё в порядке?!"
    show monika om
    m "В-в полном, да!"
    show monika mj
    mc "Не хватало тут ещё наших кульбитов с тройным сальто."
    show monika md e2a
    mc "Давай слезем отсюда и выйдем на дорогу."
    show monika mh
    m "Хорошо..."
    show monika md

    scene bg niigata park japanese path 3
    show monika forward white_dress neut cm e1c b1f at t11
    with wipeleft_scene
    mc "Отлично, теперь нам направо."
    show monika mh
    m "Подожди-ка..."
    show monika cm
    mc "Что такое?"
    show monika mh oe brow lpoint
    m "Это же...{w}продолжение той асфальтированой дороги."
    show monika cm ldown
    mc "Что?"
    show monika mh
    m "Мы сейчас крюк выписали."
    show monika cm
    mc "Да?"
    show monika laug cm oe
    mc "Реально?"
    show monika mb
    m "Ха-ха-ха, кажется, Сайори классно с тобой разминулась."
    show monika e2c
    m "Потом куплю ей шоколадку с печеньем в качестве бонуса за такую блестящую работу."
    show monika cm
    mc "Мда-а-а..."
    show monika ce
    mc "Обвели меня вокруг...{w}дороги..."
    show monika mb
    m "Ха-ха-ха!"
    show monika cm

    scene black with wipeleft_scene
    mc "Скоро должна быть тории..."
    m "До сих пор помню, как ты в меня влетел."
    mc "А я не помню, как смог так провернуться, что ты на ногах осталась, а я грохнулся."
    m "Виртуоз, хах!"
    mc "Да уж..."

    scene bg niigata park japanese torii
    show monika forward white_dress happ cm oe at t33
    with wipeleft_scene
    show monika b1b
    mc "А вот и место, где всё началось..."
    show monika om
    m "Будто это было ещё вчера."
    show monika cm
    mc "...неужели ворота реально такие низкие?"
    show monika om b1f rhip
    m "А что, они должны быть такими же огромными, как тории на воде в святилище Ицукуси{image=accent_low_register}{space=-15}ма?"
    show monika cm
    mc "Просто в голове они у меня запомнились БОЛЕЕ массивными."
    show monika brow
    m "Хм..."
    "..."
    show monika e1b
    mc "..."
    m "..."
    mc "Как я сильно изменился с того момента..."
    show monika om oe
    m "...и я этому рада."
    show monika rdown
    m "Конечно, не видела всех твоих изменений, но то малое, что я точно заметила, уже говорит о многом."
    show monika cm
    mc "..."
    show monika neut cm oe
    mc "Как-будто этих изменений всё равно недостаточно."
    mc "И будто они могут с лёгкостью развалиться на части..."
    show monika om rhip at t11
    m "Почему ты так думаешь?"
    show monika cm
    mc "Ну, если, в теории, ты меня кинешь сейчас, то я уж точно в себе закроюсь, ибо хватит с меня доверий к людям."
    mc "Или если тебя вырвут отсюда, из-за чего мы потеряем связь..."
    mc "В общем, вот это меня и пугает."
    mc "С таким трудом, с такими силами и огромным количеством времени выстраивался карточный домик, держащийся на честном слове..."
    mc "...и тут слегка его что-то микроскопически задевает, после чего он рушится до основания, автоматически выкидывая всё в него вложенное на помойку."
    mc "И потом задаёшься вопросом: \"А зачем ты вообше тратил на него рерсурсы, которые никогда не восстановишь?\""
    show monika om ce rdown
    m "...поверь мне, Макс, я тоже этого боюсь и мне нисколько не лучше от всей этой ситуации."
    show monika mh oe
    m "Как я и говорила, здесь главное держаться друг за друга, иначе мы со всем не справимся и нас разорвёт на части."
    show monika cm
    mc "Хватит ли наших сил для этого?"
    show monika happ om oe
    m "Да."
    show monika b1f rhip
    m "И вообще, мы уже третий раз к этой идее приходим."
    show monika ce brow lpoint
    m "Думаю, на этой ноте здесь можно поставить жирную точку."
    show monika cm ldown
    mc "...да, ты права."
    show monika om oe
    m "Пойдём дальше?"
    m "Стоять здесь вечность нет никакого смысла."
    show monika anno om oe
    m "Всё равно, что застреваешь в прошлом: каждый раз испытываешь одни и те же эмоции, которые рушат твою жизнь, так ещё и ничего полезного не приносят."
    show monika cm
    mc "Да."
    show monika happ cm oe
    mc "Пойдём отсюда...{w}навстречу будущему."
    show monika om ce rdown
    m "Вот, такой твой настрой мне больше нравится!"
    show monika cm

    scene black with wipeleft_scene
    mc "О-о-о, точно!"
    m "М-м?"
    mc "Я вспомнил, что хотел у тебя ещё при встрече спросить про твоё имя."
    mc "Мне оно показалось немного иностранным..."
    m "В древности оно и правда было завезено из Европы в Японию."
    m "Но здесь оно...{w}адаптировалось, назовём это так."
    mc "И что же всё-таки оно означает?"
    m "Я бы сказала, здесь несколько значений, так как моё имя из 3-ёх иероглифов."
    mc "О, вот как..."
    m "Вариаций много, но в целом они имеют схожий смысл."
    m "Сейчас вспомню, как моя мама мне рассказывала..."
    m "А, точно."
    m "Первый -- «Мо» -- это желание и надежда."
    m "Я думаю, ты и сам понимаешь."
    mc "Да, ты рассказывала, как тебя в детстве «мучали»."
    m "Хах."
    m "Второй -- «Ни» -- это человечность и доброта."
    mc "Тут и так понятно."
    m "И третий -- «Ка» -- это что-то связанное с цветком: аромат, сам «цветок» и так далее."
    mc "Хм, именно поэтому тебя привлекают орхидеи?"
    m "Может, и так!"

    scene bg niigata park japanese off entrance arc 1
    show monika forward white_dress neut cm e1b at t22
    with wipeleft_scene
    show monika om
    m "Эх, я думала, что тут стало получше..."
    show monika cm
    mc "Да, как было кисло, так и осталось."
    show monika oe
    mc "На глицинии всё ещё нет бутонов."
    show monika om
    m "Вроде бы её период цветения где-то ближе к концу мая, нет?"
    show monika cm
    mc "Не помню."
    show monika happ om oe b1b
    m "Ладно, пойдём."
    show monika cm

    scene bg niigata park japanese off entrance
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    mc "Зато хоть пруд наполнили."
    show monika om ce
    m "Ха-ха, прогресс."
    show monika cm
    mc "Правда, я никого там так и не увидел."
    show monika om oe
    m "Явно они туда ещё не вернули карпов."
    show monika neut cm oe
    mc "Может, ещё куда-нибудь сходим?"
    show monika om
    m "Даже не знаю..."
    show monika e1b
    m "По-хорошему мне нужно вернуться домой и разобраться с бытовыми делами, пока есть время."
    show monika oe
    m "Заодно проверить домашнюю работу на завтра."
    show monika happ om oe lpoint
    m "Воскресенье, как ни крути."
    show monika cm ldown
    mc "Да, ты права."
    mc "Надо будет тоже всё проверить."
    mc "Тогда идём обратно?"
    m "Угу."
    show monika ce

    scene black with wipeleft_scene
    mc "Я тебе не говорил, что сегодня катался с Нацуки в госпиталь?"
    m "Нет."
    m "Вы ездили к её матери?"
    mc "Ага."
    m "Как она там?"
    m "Выздоравливает?"
    mc "В порядке, по словам самой Нацуки."
    mc "Я-то в холле остался -- к палате не ходил."
    m "А-а, ясненько."
    mc "И ещё сегодня я увидел мать Юри."
    m "О-о-о, она вернулась обратно?"
    mc "Да, теперь Юри хоть под её присмотром будет."
    mc "Вряд-ли при ней сможет схатиться за нож."
    m "Это точно."
    mc "И теперь я понимаю, откуда у Юри такое лёгкое понимание английского..."
    m "Ха, уже знаком с её особенностью?"
    mc "Да, когда совместный стих писали, она об этом рассказала."
    mc "Вообще не думал, что у неё мать -- профессиональный переводчик."
    m "На самом деле это очень хорошо."
    m "Если Юри попытается развить свои способности писательства, а также подтянет английский и русские языки, то она в будущем познакомится со множеством людей."
    m "Например, соберёт вокруг себя любителей её произведений, а там, может быть, отправится в какой-то тур или поездку..."
    m "Это очень поможет её социализировать и дать дозу общения, которой ей не хватает в нашем обществе..."
    mc "Хм, а мысль дельная..."
    mc "К слову, помнится, я на её любимом месте, на первом этаже старого корпуса у правой летницы, увидел одну старую листовку."
    mc "Это вроде была агитка от Клуба английского языка."
    mc "Почему бы Юри не вступить туда?"
    m "Ну...{w}ха-ха..."

    scene bg niigata street suburban 9 day
    show monika forward white_dress nerv cm oe at t11
    with wipeleft_scene
    show monika mb
    m "Его сейчас не существует."
    show monika cm
    mc "...опять мёртвый клуб?"
    show monika neut cm oe
    mc "Неужели у вас такая высокая текучка в клубной деятельности?"
    show monika om lpoint
    m "Скорее, некий кризис."
    show monika anno om oe ldown
    m "Ученики и ученицы не особо рвутся стать частью какого-то клуба..."
    show monika cm
    mc "Фигня какая-то."
    mc "Ладно я ещё, свои беды с общением, но остальные-то почему?"
    show monika neut om oe
    m "Кто их знает, Макс?"
    m "К нам же тоже мало кто идти хочет, так и тут то же самое."
    show monika cm
    mc "С другой стороны, это объясняет, почему ты с таким трудом собрала в клуб всего несколько человек."
    show monika e1b
    m "М-м."
    mc "Подожди-ка."
    show monika oe
    mc "А на самом деле...{w}нам это ситуация может играть на руку."
    show monika curi om oe
    m "Что ты имеешь ввиду?"
    show monika md
    mc "Почему бы Юри самой не стать президентом Клуба английского языка?"
    show monika neut cm oe
    mc "Да, знаю, на неё будет возложена дополнительная ответственность, но ведь она сможет раскрыться людям, а не быть замкнутой."
    show monika om
    m "Иными словами, ты взял мою идею, но решил реализовать уже сейчас?"
    show monika cm
    mc "Ну а почему нет?"
    mc "Ты же знаешь, какой в Юри просыпается азарт со страстью, когда она рассказывает о чём-то любимом: будь то книга или стихи."
    mc "Она даже на себя становится не похожа."
    mc "А тут такой шикарный шанс и язык подтянуть, и единомышленников найти, и себя раскрыть среди них."
    show monika mh
    m "Идея, может, и хорошая..."
    show monika e1b
    m "Вот только Юри очень любит прикипать к людям."
    m "Если такой человек уйдёт из клуба по какой-либо причине, она будет переживать это болезненно."
    show monika cm oe
    mc "Но это же неизбежно."
    show monika mh
    m "Тогда почему ты сразу ей не откажешь в чувствах?"
    show monika cm
    mc "..."
    show monika mh ce
    m "Правильно: из-за её эмоционального вихря и, как следствие, пагубных для неё последствий."
    show monika oe
    m "А здесь это будет происходить чаще."
    show monika lpoint
    m "Изучать английский -- это не писать простенькие стихотворения на какие душе угодно темы."
    show monika ldown
    m "И к тому же изучать его нужно по чему-то конкретному."
    m "Должны быть учебные материалы, должна быть какая-то интерактивная деятельность, которую надо придумать и реализовать."
    m "Так и ещё не факт, что участники в этом будут заинтересованы."
    show monika e1b
    m "Для Юри такая нагрузка будет высокой."
    show monika oe lpoint
    m "Тем более скоро выпускные экзамены, поэтому по-хорошему всю прочую нагрузку надо снизить."
    show monika cm ldown
    mc "Никто и не требует от неё чрезмерных высот в изучении английского."
    show monika mh
    m "Но тогда получится каша."
    show monika cm
    mc "Но здесь же всё зависит от людей, которые придут в клуб."
    mc "Никому же из них не будет интересно, насколько всё в клубе «официально» происходит."
    show monika mh rhip
    m "Не отрицаю, но потом Юри после официального статуса неизбежно станет членом Школьного совета, где мы проводим собрания по клубной деятельности."
    m "Эти собрания включают обсуждения президентов клубов между собой по различным вопросам и импровизированные отчёты перед главой Совета."
    show monika e1c
    m "Иными словами, сколько человек пришло, ушло, поломали ли мы какое-то официальное оборудование, нужно ли что-то докупить, и так далее."
    show monika oe
    m "Также можно предложить какие-нибудь идеи развития или сотрудничество между клубами."
    m "И вот эти собрания являются обязательными."
    show monika cm
    mc "А Кохаку, которая плевала на этот официоз?"
    show monika mh
    m "...на самом деле...{w}ну ты же слышал, что Рэйко давала Кохаку шанс?"
    show monika cm
    mc "Да, было дело."
    show monika mh
    m "Вот."
    m "Если президент по неуважительной причине не является на собрание...{w}не помню, сколько раз...{w}то с него снимаются полномочия по управлению клубом."
    m "И также ему запрещается принимать участие в клубной деятельности."
    show monika rdown
    m "Проще говоря, вышвыривают из клубов."
    show monika cm
    mc "Ничего себе..."
    mc "Прямо безвозвратно?"
    show monika curi om e1b
    m "Ну, «искупление вины» происходит в индивидуальном порядке."
    show monika neut mh oe
    m "У нас просто очень редки такие случаи."
    show monika lpoint
    m "За моё время пребывания в Совете только Кохаку до такого дошла."
    show monika cm ldown
    mc "Значит, Рэйко её очень пощадила."
    show monika mh
    m "Да, но безрезультатно, так что скоро это будет исправлено."
    show monika cm
    mc "В общем, возвращаясь к Юри..."
    mc "Ты думаешь, ей будет тяжело участвовать в ваших собраниях?"
    show monika mh ce
    m "Да."
    show monika oe
    m "Я знаю, какой она была полгода назад, даже чуть меньше."
    m "То есть, когда она только вступила в Литературный клуб."
    show monika e1b
    m "Она ещё не готова к такой нагрузке."
    show monika cm
    mc "Но в последнее время она стала более открытой."
    show monika mh oe
    m "Понимаю, но этого недостаточно."
    show monika cm
    mc "Тогда...{w}может, найти того, кто станет президентом вместо неё?"
    show monika curi md oe
    mc "А она просто вступит в клуб и будет этакой неофициальной важной фигурой."
    show monika om rhip
    m "И кто станет этим президентом?"
    m "У меня нет каких-либо вариантов, совершенно."
    show monika md
    mc "М-м-м..."
    show monika neut cm oe
    mc "Чёрт, вечные нерешаемые проблемы..."
    show monika happ om oe lpoint rdown
    m "Тем не менее не будем выбрасывать эту идею из головы: она реально хорошая."
    show monika ldown
    m "Просто необходимо подготовиться к её реализации."
    stop noise_1 fadeout 2.0
    show monika cm
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day
    show monika forward white_dress happ cm oe at t11
    with wipeleft_scene
    show monika neut cm oe
    mc "Ладно, Моника, извини."
    mc "Свидание вышло полной хренью."
    show monika sedu om oe
    m "Ой, Ма-а-акс..."
    show monika b1f
    m "Почему тебя так волнует разнообразие нашей прогулки?"
    show monika ma
    mc "Потому что я, как парень, должен обеспечить тебя хорошим времяпрепровождением?"
    show monika happ om oe brow
    m "И ты им сегодня обеспечил."
    show monika cm
    mc "...не так хорошо, как хотелось бы."
    show monika om
    m "А я не из требовательных людей."
    show monika ce
    m "И я буду ценить даже такие наши моменты."
    show monika lpoint
    m "Потому что мы провели время вместе, а это самое главное."
    show monika cm ldown
    mc "Ты права, но маленький осадок от своей дурости всё равно остался."
    show monika sedu om oe b1f
    m "Ну если тебе настолько это важно..."
    show monika ma

    if cg_a1_d14_m.unlocked == False:
        $ cg_a1_d14_m.unlock()

    scene monika_cg_act_1_day_14_base
    show monika_cg_act_1_day_14_exp3 at cgfade
    with dissolve_cg
    m "...то почему бы нам не закончить свидание поцелуем?"
    mc "Пф, вот так сразу?"
    show monika_cg_act_1_day_14_exp1 at cgfade
    hide monika_cg_act_1_day_14_exp3
    m "А чего ждать?"
    m "Здесь, кроме нас, никого нет."
    show monika_cg_act_1_day_14_exp3 at cgfade
    hide monika_cg_act_1_day_14_exp1
    m "К тому же кто-то здесь в первый раз у меня уже забрал поцелуй~"
    mc "Ничего себе!"
    mc "А по-моему, кто-то здесь меня обхватил руками и не дал вырваться наружу!"
    show monika_cg_act_1_day_14_exp1 at cgfade
    hide monika_cg_act_1_day_14_exp3
    m "Хе-хе-хе!"
    m "Так какой твой положительный ответ?"
    show monika_cg_act_1_day_14_exp3 at cgfade
    hide monika_cg_act_1_day_14_exp1
    mc "Подожди, это моя фраза перед вступлением в клуб..."
    mc "Блин, атакуешь меня по всем фронтам!"
    show monika_cg_act_1_day_14_exp1 at cgfade
    hide monika_cg_act_1_day_14_exp3
    m "А-ха-ха!"
    show monika_cg_act_1_day_14_exp3 at cgfade
    hide monika_cg_act_1_day_14_exp1
    mc "Ох, ладно, шутки в сторону, иди сюда."

    scene black with dissolve_cg
    pause 0.5
    "Хотя бы в такие моменты я могу почувствовать себя по-настоящему расслабленным..."
    "...но они длятся буквально считаные секунды."
    "Блин, мысли путаются, не могу думать..."
    "..."

    scene monika_cg_act_1_day_14_base
    show monika_cg_act_1_day_14_exp2 at cgfade
    with dissolve_scene_full
    pause 0.5
    hide monika_cg_act_1_day_14_exp2
    mc "Пф..."
    show monika_cg_act_1_day_14_exp1 at cgfade
    m "Как тебе?"
    show monika_cg_act_1_day_14_exp3 at cgfade
    hide monika_cg_act_1_day_14_exp1
    mc "...успокаивающе..."
    m "Вот теперь и я спокойна."

    scene bg monika house livingroom day
    show monika forward white_dress happ cm oe at i11
    with dissolve_cg
    show monika om ce rhip
    m "Ладно, Макс, не кисни."
    show monika oe
    m "Ты молодец, что стал делать шаги в развитии наших отношений."
    m "Это уже говорит о тебе о многом."
    show monika cm
    mc "М-м."
    show monika lean white_dress happ om oe at h11
    m "Всё, мне пора приниматься за дела."
    show monika forward white_dress happ om ce
    m "Завтра увидимся в клубе!"
    show monika cm
    mc "Конечно."
    show monika oe
    mc "До завтра!"
    show monika om ce
    m "Пока-пока!"
    show monika cm
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg residential_day with wipeleft_scene
    mc "Да, ну и день выдался..."
    "..."
    mc "Блин, уже конец апреля..."
    mc "Даже не верится."
    mc "Хотя вполне ощущается: воздух стал теплее."
    s "{size=19}А, Макс, вернулся?{/size}"

    scene bg house
    show sayori turned casual happ cm oe at t11
    with wipeleft_scene
    mc "Ага."
    "Как-будто бы лучше пока не буду говорить про посиделки с Юри..."
    show sayori neut om oe
    s "Там с мамой Нацуки всё прекрасно?"
    show sayori cm
    mc "Наверное."
    mc "Я сидел в холле, Нацуки одна в палату пошла."
    show sayori curi om oe
    s "А..."
    show sayori cm
    mc "Кстати, мне удалось...{w}скажем, помириться с родителями Моники и поговорить с ними."
    show sayori neut om oe
    s "Ого, когда успел?"
    show sayori cm
    mc "Так мы вернулись где-то в полдень, времени до их отъезда было полно."
    show sayori om
    s "Ясненько."
    show sayori cm
    mc "Вот только планы отца Моники не поменялись..."
    show sayori curi om oe
    s "Кажется, он их вряд-ли поменяет, потому что он очень серьёзный дядька с очень серьёзными намерениями!"
    show sayori cm
    mc "Это я уже понял."
    show sayori neut cm oe
    mc "Но посмотрим, как там будет дальше."
    show sayori sad om oe
    s "Только...{w}ну...{w}не расстраивайся, если вы с Моникой друг друга потеряете, хорошо?"
    show sayori cm
    mc "..."
    s "..."
    show sayori neut cm oe
    mc "...ой, Сайори, ты реально повелась на моё угрюмое выражение лица?"
    show sayori curi om oe
    s "Что?"
    show sayori laug cm ce at h11
    mc "Бам!"
    show sayori om
    s "Ай, щекотно!"
    show sayori oe
    s "Меня аж целиком дёрнуло!"
    show sayori cm
    mc "Ха-ха-ха!"
    show sayori happ cm oe
    mc "В общем, куда я денусь, всё в порядке."
    mc "Если такое случится...{w}значит, так тому и быть, жизнь на этом не закончится."
    mc "И кстати, насчёт Моники."
    show sayori neut cm oe
    mc "Мы с ней немного прогулялись по окрестностям, зайдя в наш избитый парк..."
    show sayori curi cm oe
    mc "...короче, она захотела дать тебе бонус в виде шоколада с печеньем."
    show sayori om
    s "Что?!"
    show sayori e1a
    s "За какие заслуги?"
    show sayori cm
    mc "А это ты сама у неё узнай."
    show sayori happ cm oe
    mc "Заодно напомнишь ей про этот «долг»."
    show sayori om ce
    s "Ух, уже не терпится!"
    show sayori cm
    mc "Ладненько, я пойду, ноги уже никакущие."
    show sayori om oe
    s "Агась!"
    show sayori pani om oe at h11
    s "Стой!"
    show sayori md
    mc "Что такое?"
    show sayori neut om oe
    s "Может...{w}мне снова у тебя поспать..."
    show sayori cm
    mc "...нет, Сайори, я так прикинул, кошмары не изменились."
    mc "Они будто живут своей жизнью, но последовательно, как сюжет в книге или где-нибудь ещё..."
    show sayori doub cm e1b
    mc "А ещё завтра в школу!"
    mc "В общем, Сайори, не парься."
    show sayori om
    s "Буэ-э-э..."
    show sayori cm
    mc "Всё, ноги отваливаются, увидимся завтра утром."
    show sayori happ om oe
    s "Эх, увидимся!"
    show sayori cm

    scene black with wipeleft_scene
    "Да, ноги уже ноят во всю."
    "Надо поскорее вернуться в кровать, пока не помер."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "Уф-ф-ф..."
    mc "Как же классно лечь на кровать и расслабиться после долгого стояния на ногах..."
    mc "Уф-ф..."
    mc "..."
    mc "Надо передохнуть немного, а потом опять искать этого психолога..."
    mc "..."
    mc "Почему-то у меня реально такое ощущение, что меня скоро что-то осенит и я найду его по нику."
    mc "Вот только что..."
    mc "Брожу вокруг, да около, а результата ноль."
    mc "Одна пустота."
    mc "..."
    mc "......"
    mc "Пустота."
    mc "..."
    mc "Пусто...{w}та..."
    mc "Неужели что-то связанное с пустотой?"
    mc "Да, я в первый раз тоже говорил это слово, но сейчас..."
    mc "Сейчас оно почему-то вызывает у меня смешанные эмоции."
    mc "И не обычные, а словно...{w}прошедшие."
    mc "Что-то из прошлого, как раз с психологом."
    mc "М-м-м, мерзко немного на душе, но мне надо спасать Юри."
    mc "Поэтому надо ещё поразмыслить..."
    mc "..."
    mc "......"
    mc "Подождите...{w}я же писал стихотворение вчера."
    mc "И так его не посмотрел."
    mc "Надо исправить это дело."
    call show_poem(poem_mc7)
    mc "......"
    mc "...что...{w}я, блин, понаписал?"
    mc "Что это за..."
    mc "Пф-ф-ф..."
    mc "Нет, всё, хватит с меня этого тупого розовосопливизма."
    mc "Заколебало уже, честное слово."
    mc "Что ни стих, то какие-то смазливые самокопающие размышления, размазанные тонким слоем по стенке."
    mc "А оно ещё стекает вниз и воняет на километр."
    mc "Надо уже начать писать нормальные стихи на нормальные, чёрт побери, темы, а не вот эту идиотскую сопливую дурь для мамкиных любителей недопсихологии."
    mc "Всё, с этого момента я буду стараться это делать."
    mc "А это пусть отправляется в помойку нахрен."
    mc "Задрало."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom with wiperight
    mc "Аргх, нет!"
    mc "Опять мысль потерял!"
    mc "Чёртова пустота в голове, чёртова пустота!"
    mc "Пустота-пустота-пустота!"
    mc "Что, твою мать, такого в этом слове?!"
    mc "Пф-ф-ф..."
    mc "Ф-ф-ф..."
    mc "..."
    mc "Так, надо немного расслабиться и восстановиться..."
    mc "У меня снова мозги горят."
    mc "Замучаешься восстанавливать утраченную память..."
    mc "..."
    mc "Хм..."
    mc "У меня только сейчас проскачила мысль, что на моей кровати лежал весь Литературный клуб."
    mc "Выходит, все попользовались кухней, все потоптались в моей комнате и все повалялись на моей кровати."
    mc "Когда мой дом успел стать проходным двором?"
    mc "..."
    mc "...опять Юри вспомнилась..."
    mc "Нет, надо всё-таки что-то придумать с Клубом английского языка."
    mc "Даже при всей моей нелюбви к школе, я не верю, что из всего многообразия учеников не найдётся хоть одного, кто будет в этом заинтересован."
    mc "Вот только как найти такого человека..."
    mc "..."
    mc "Всё вечно упирается в бестолковый поиск."
    mc "Поиск того, не знаю что."
    mc "И там, не знаю где."
    mc "..."
    mc "Вообще, если так подумать, я бы, может, даже сам вступил в такой клуб."
    mc "Он-то реально полезным будет, потому что этот чёртов английский везде."
    mc "А такой клуб помог бы поддерживать его хоть на каком-то разговорном уровне."
    mc "А то мне иногда попадались иностранные видео, в них так быстро говорят на английском, что слова разобрать не можешь."
    mc "Всё превращается в какую-то «кашу» с «проглатыванием» звуков, кучей сокращений и прочих прелестей упрощения слов."
    mc "Как они сами друг друга понимают, ума не приложу..."
    mc "Даже если бы я родился в англоговорящей стране, я всё равно бы не смог привыкнуть к такому."
    mc "Хотя не знаю..."
    mc "По крайней мере мне надо, чтобы у меня были прямые ассоциации слов с предметами."
    mc "Ну да, это немного бы помогло в понимании."
    mc "Например, ну-ка..."
    mc "{color=#fc7e23}Bed{/color} -- кровать."
    mc "{color=#fc7e23}Table{/color} -- стол."
    mc "{color=#fc7e23}Computer{/color} -- компьютер."
    mc "{color=#fc7e23}Book{/color} -- книга."
    mc "{color=#fc7e23}Shelf{/color} -- полка."
    mc "{color=#fc7e23}TV{/color} -- телевизор."
    mc "Да, эта аббревиатура слишком очевидна..."
    mc "Так, э-э-э...{w}шкаф для одежды...{w}{color=#fc7e23}wardrobe{/color} что-ли...{w}вроде да."
    mc "Ладно, предметы более-менее, а если что-то абстрактное?"
    mc "Э-э-э...{w}пустота эта...{w}а, {color=#fc7e23}void{/color}."
    mc "О, восстанавливать -- {color=#fc7e23}restore{/color}."
    mc "Ждать -- {color=#fc7e23}wait{/color}."
    mc "Э-э-э, свидание...{w}а-а-а...{w}а вот не помню."
    mc "Ладно, проехали."
    mc "Неделя -- {color=#fc7e23}week{/color}."
    mc "Что ещё можно вспомнить..."
    mc "Собака -- {color=#fc7e23}dog{/color}."
    mc "Еноты -- хринь."
    mc "А-а, лангуаге -- бинь."
    mc "Чёртовый энгрийский, блин!"
    mc "..."
    mc "Ладно, уже кривляния пошли, дурь какая-то."
    mc "Но что-то «родить» можем, уже радует..."
    mc "..."
    mc "Сто-о-оп."
    mc "Пустота -- {color=#fc7e23}void{/color}."
    mc "{color=#fc7e23}Void{/color}...{w}{color=#fc7e23}voi{/color}..."
    mc "Что я там после него говорил?"
    mc "Восстановление, вроде...{w}{color=#fc7e23}restore{/color}."
    mc "{color=#fc7e23}Re{/color}...{color=#fc7e23}re-re-re{/color}..."
    mc "{color=#fc7e23}Reid{/color}...{w}{color=#fc7e23}revoi{/color}...{w}{color=#fc7e23}voistore{/color}...{w}{color=#fc7e23}vo{/color}..."
    mc "..."
    mc "...{color=#fc7e23}voires{/color}..."
    mc "..."
    mc "Не...{w}не-не-не..."
    mc "{color=#fc7e23}Voires{/color}..."
    mc "Разве это {b}оно{/b}?"
    mc "{color=#fc7e23}Voires{/color}..."
    mc "{color=#fc7e23}Voires{/color}."
    mc "Чёрт..."
    mc "{color=#fc7e23}VOIRES{/color}!" with vpunch
    mc "{sc=3.0}ЧЁРТ ПОБЕРИ!{/sc}"
    mc "{sc=3.0}ТОТ САМЫЙ ГРЁБАНЫЙ НИК!{/sc}"
    mc "{sc=3.0}ТВОЮ МАТЬ!{/sc}"
    mc "{sc=3.0}Я ЖЕ ЗНАЛ, ЧТО ЭТО СЛОВО У МЕНЯ НА ЯЗЫКЕ\nВЕРТИТСЯ!{/sc}"
    mc "{sc=3.0}НАДО СРОЧНО ПРОВЕРИТЬ СУЩЕСТВОВАНИЕ ЕГО\nАККАУНТА!{/sc}"
    mc "{sc=2.5}Лишь бы он имя не поменял!{/sc}"
    mc "{sc=2.0}......{/sc}"
    mc "{sc=2.0}Поиск-поиск-поиск-поиск...{/sc}"
    mc "{sc=2.0}......{/sc}"
    mc "{sc=2.0}Тихо, соберись, не надо пальцами трястись!{/sc}"
    mc "{color=#fc7e23}Vo{/color}...{w}{color=#fc7e23}i{/color}...{w}{color=#fc7e23}res{/color}..."
    mc "......"
    mc "{sc=1.0}Это он...{w}это он...{w}единственный с этим ником...{/sc}"
    call skip_block_on

    $ contact_list["mc"].append("mc_v_chat")

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 41
        clock = (17, 12)

    phone discussion "mc_v_chat"
    $ plot_pause()
    mc "{sc=2.0}Блин, руки опять трясутся...{/sc}"
    mc "{sc=2.0}И сердце готово выпрыгнуть...{/sc}"
    mc "{sc=2.0}Все прошлые сообщения, к счастью, стёрты.{/sc}"
    mc "{sc=2.0}Не хочу вспоминать всё, что было.{/sc}"
    mc "{sc=2.0}...{/sc}"
    mc "{sc=2.0}Что же написать...{/sc}"
    mc "{sc=2.0}......{/sc}"
    mc "{sc=3.0}АРГХ, НЕ ЗНАЮ!{/sc}" with vpunch
    mc "{sc=2.0}Но мою заявку в друзья он точно заметит...{/sc}"
    mc "{sc=2.0}Но всё равно надо что-то написать!{/sc}"
    mc "{sc=2.0}Мне надо подумать.{/sc}"

    phone end discussion transition

    call skip_block_off
    mc "{sc=1.5}Мне надо подумать...{/sc}"
    call window_close

    $ nightmare_active = True

    call nightmare_act_1_day_14

    scene black
    pause 5.0
    play phone_sound new_message_mc
    pause 1.5
    call window_open
    "{cps=20}{sc=2}.........{/sc}{/cps}"
    "{cps=20}{sc=2}...я же разбил...{w}тебя...{/sc}{/cps}"

    scene bg bedroom at mc_bed
    show dark
    with dissolve
    mc "{cps=20}{sc=2.0}ОБ КА...{w}а-а-а...{/sc}{/cps}"
    mc "{cps=20}{sc=1.0}...чёртов кошмар...{/sc}{/cps}"
    mc "{cps=20}{sc=0.5}...{/sc}{/cps}"
    mc "{cps=20}{sc=0.5}...стоп...{w}уведомление о сообщении?...{/sc}{/cps}"
    mc "{cps=20}{sc=1.0}...кого...{w}разобрало...{w}так поздно...{/sc}{/cps}"
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 100
        clock = (2, 34)

    phone register "mc_v_chat":
        time year 2018 day 30 month 4 hour 2 minute 32
        "v" "Макс?"

    phone discussion "mc_v_chat"
    $ plot_pause()
    phone discussion "mc_v_chat":
        "v" "Это ты?"
    pause 0.5
    play sound mc_inhale
    pause 2.0
    phone discussion "mc_v_chat":
        "mc" "Да"

    phone end discussion

    call skip_block_off
    $ quick_menu = False

    $ nightmare_active = False

    scene black
    pause 3.0

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d14.unlocked == False:
        $ ach_a1_d14.unlock()
        pause 7.0
    else:
        pause 3.0

    hide loading_sign_mc with dissolve
    pause 1.0

    return
