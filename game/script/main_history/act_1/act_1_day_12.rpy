
label act_1_day_12:

    scene bg bedroom at mc_bed
    call window_open
    mc "{sc=3}А-А-А-А-А-А-А-А-А-А!!!{/sc}" with shake(dist=40)
    call autosave
    mc "{sc=3}МОЗГ, ДА ТЫ ДУРАК, ЧТО ЛИ, СОВСЕМ?!{/sc}"
    mc "{sc=2}ТЫ ЧЁ, ДУРАК, ЧТО ЛИ, ТАК ПУГАТЬ-ТО?!{/sc}"
    call window_close

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

    if ach_a1_d11.unlocked == False:
        $ ach_a1_d11.unlock()
        pause 7.0
    else:
        pause 3.0

    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    mc "Нет-нет-нет, это уже полнейший перебор..."
    "Кровавый стих с пятнами непонятного происхождения, Юри с глючной башкой и лопнувшими глазными сосудами, экран смерти...{w}и..."
    mc "...чёрная Моника?"
    "Это точно не та, что я видел в понедельник."
    "У этой вообще глаз нет."
    "И улыбка в пол-лица."
    "И всё полностью чёрное..."
    mc "{sc=2}Пф-ф-ф-ф-ф!{/sc}" with vpunch
    mc "Будто мой мозг сделал её максимально мерзкой и отвратительной."
    mc "Чего ты добиться хочешь?!"
    mc "{sc=2}НА-{w=0.5}ДО-{w=0.5}ЕЛ!!!{/sc}"
    mc "Если ты такой офигительно богатый по воображению, то почему бы просто не создать какую-нибудь хрень, которая пояснит за всё дерьмо, что ты успел наплодить?!"
    mc "Чё, так трудно, что ли?!"
    mc "Сволочь..."
    "Я смогу хоть...{w}да даже не выспаться..."
    "Я смогу хоть нормально пожить?"
    "Нормальной хорошей жизнью без всяких нервов и кошмаров?..."
    mc "Всё ж делаю, как надо: и дисциплину соблюдаю, и в учёбе преуспеваю, когда большинство на неё просто забивает, и стараюсь быть человеком, на которого можно положиться..."
    mc "...но нет, у придурков всё прекрасно, а у таких, как я, -- проблем, блин, дохрена."
    mc "..."
    mc "Ха, рифма, однако..."
    "«Профдеформация» от Литературного клуба?"
    "Ладно-ладно, тупая шутка."
    "Пора уже одеваться, пока у меня всё время не ушло."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 2.0
    scene bg residential_day with wipeleft_scene
    "..."
    mc "Что и требовалось доказать."
    "Нет уже никакой сырости после вчерашнего ливня."
    "Впрочем, это хорошо, потому что асфальт целиком высох."
    "Не будет никаких луж, «рек» и «озёр» по пути, которые пришлось бы обходить по криволинейной траектории."
    s "{size=19}Макс-Макс-Макс!{/size}"
    pause 0.5
    show sayori turned happ cm ce school_bag at l11
    pause 0.5
    show sayori oe
    mc "Что?"
    show sayori om ce lup rup at h11
    s "Пошли!"
    show sayori cm ldown rdown
    mc "...пошли."
    show sayori oe

    scene bg niigata street suburban 10 day
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori om
    s "Ну что, как спалось в этот раз?"
    show sayori neut om oe
    s "Без страшилок, надеюсь?..."
    show sayori cm
    mc "Пха-ха, ха-ха..."
    show sayori curi cm oe
    mc "Пока каждый кошмар поднимает планку «качества» всё выше и выше."
    show sayori om
    s "Да что же делать?!"
    show sayori cm
    mc "Я этот вопрос задавал себе уже много раз."
    show sayori neut om oe b1c
    s "И прямо плохо-плохо всё в этот раз было?"
    show sayori cm
    mc "Ну, я уже рассказывал вам, как просыпался после прошлых кошмаров..."
    show sayori shoc md oe -b1c
    mc "Сегодня тоже вскочил с коротким криком."
    show sayori vang om oe lup rup at h11
    s "УЖАС!" with vpunch
    show sayori angr om oe ldown rdown
    s "Всё, с этого дня я буду спать в твоей кровати!"
    show sayori cm
    mc "Чего?!" with vpunch
    mc "Это что ещё за вторжение?"
    show sayori om ce
    s "Если тебе ничего не может помочь, то будем прибегать к радикальным мерам!"
    show sayori cm
    mc "Не-не-не, я на такое не подписываюсь."
    show sayori happ om oe
    s "А мне и не нужна твоя подпись."
    show sayori cm
    mc "Сайори, я серьёзно."
    show sayori neut cm oe
    mc "Сама по себе ситуация абсурдная, так и ты ещё будешь каждый раз бегать в мой дом спать."
    mc "Неудобно же!"
    show sayori pout cm oe
    mc "И твои родители не поймут."
    show sayori mh
    s "Нэ-э-э..."
    show sayori sad om oe
    s "...но один раз можно?"
    show sayori cm
    mc "Один раз..."
    mc "Откуда такое желание?"
    show sayori om
    s "А вдруг по-настоящему поможет?"
    show sayori worr om oe
    s "Выспишься нормально...{w}хотя бы одну ночь."
    show sayori cm
    mc "М-м-м..."
    "Даже не знаю..."
    "Вроде бы бред, а вроде бы..."
    show sayori ce
    "Но я с Моникой спал и мне это не помогло."
    "Но и при этом я тогда нанервничался..."
    show sayori neut cm oe
    mc "Ладно, можно."
    show sayori happ om ce lup rup at h11
    s "Е-е-е!"
    show sayori cm ldown rdown
    mc "Думаю, сегодня как раз."
    show sayori oe
    mc "Потому что завтра выходной."
    show sayori om
    s "Да, согласна!"
    show sayori cm
    "Не отказывать же ей, в конце концов, когда есть такая хорошая возможность?"
    show sayori e1b

    scene bg school gate 1
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    mc "Всё, давай, беги на урок."
    show sayori om
    s "Да-да!"
    show sayori ce
    s "Жду тебя в клубе!"
    show sayori cm
    mc "И я..."
    show sayori at thide
    hide sayori
    pause 1.0
    "Почему-то на душе стало легче..."
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("s")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school f3 old_corridor
    show juice_apple
    with dissolve_scene_full
    s "...а-ах!"
    "Как хорошо освежать себя прохладным соком!"
    s "Хм-м-м..."
    "Яблочный всё-таки вкуснее апельсинового..."
    "Не такой кислый."
    "Жаль, что последний оказался..."

    scene black with wipeleft_scene
    s "Опять ступеньки..."
    "..."
    "Я всё ещё не могу понять, почему Нацуки не может помириться с главой Клуба выпечки."
    "Или глава Клуба выпечки с Нацуки..."
    "Они же не из тех, о ком говорил Макс вчера, верно?"

    $ kam_name = "???"

    scene bg school f2 old_stairwell center
    show juice_apple zorder 2
    with wipeleft_scene
    "А я ведь даже ни разу не видела этот клуб, хотя Нацуки рассказала мне про него, когда только-только к нам вступила."
    "Но уже так хочется помирить всех сразу..."
    s "{size=17}Почему вы все такие сложные?{/size}"
    kam "Доводы твои совсем уж ложные!"
    s "А-А-А!" with vpunch
    show kamuko turned happ om ce headband_cat at t11
    kam "Ня-ха-ха!"
    show kamuko oe lhiphid rhid
    kam "Как моя рифма, хорошо вышла?"
    show kamuko cm
    s "Ты меня напугала, э-хе-хе..."
    show kamuko om ce
    kam "Прости, не хотела терять музу вдохновения."
    show kamuko oe
    kam "Так как рифма?"
    show kamuko cm
    s "Э-э-э, отличная?"
    show kamuko om ldown rdown at h11
    kam "Вот!"
    show kamuko ce
    kam "У меня начинает что-то получаться!"
    show kamuko nerv om oe lhiphid rface
    kam "Надо будет точно вступить в Литературный клуб!"
    show kamuko neut cm oe
    s "...а ты кто?"
    show kamuko curi om oe rup
    kam "Я?"
    $ kam_name = _("Камуко")
    show kamuko happ om ce ldown rdown
    kam "Камуко, любительница игр, аниме и котиков!"
    show kamuko cm
    s "О-о..."
    show kamuko om oe
    kam "Вон, видишь рисунок на ободке?"
    show kamuko cm
    s "Котик..."
    show kamuko om ce
    kam "Правильно!"
    show kamuko cm
    s "М-м..."
    show kamuko om lhiphid rhid
    "Фу, Сайори, соберись, не будь тучкой!"
    show kamuko e2b
    "Я же вице-президент Литературного клуба, а Камуко хочет вступить к нам!"
    show kamuko oe
    "Это же целый новый участник!"
    show kamuko ce
    kam "...а у персидских мордочки такие забавные!"
    show kamuko cm
    s "Камуко, э-э..."
    show kamuko curi om oe
    kam "А?"
    show kamuko cm
    s "Ты хотела вступить к нам в клуб?"
    show kamuko om
    kam "\"К нам\"?"
    show kamuko pani om oe ldown rdown at h11
    kam "Подожди, ты тоже из Литературного?!"
    show kamuko cm
    s "Я Сайори, вице-президент!"
    show kamuko happ om oe lhiphid rhid
    kam "А-а-а-а-а, поняла-поняла, а то я только с Моникой знакома, а ещё с Юри, с Нацуки и...{w}ну с новеньким..."
    show kamuko cm
    "...почему я её не знаю?"
    show kamuko neut cm oe
    s "Мне про тебя ничего не рассказывали."
    show kamuko om
    kam "И мне про тебя."
    show kamuko doub om oe rface
    kam "Хотя подожди, я тебя вроде видела..."
    show kamuko laug om e4c
    kam "А-А-А-А-А, я видела тебя раньше, всё!!!--{nw}"
    show kamuko pout om e2e
    kam "Нет, я не видела тебя..."
    show kamuko cm
    s "...?"
    show kamuko happ om ce rhid
    kam "Ладно, я тебя видела/не видела, зато сейчас увидела!"
    show kamuko cm
    "Я сейчас запутаюсь!"
    show kamuko oe
    s "...так ты к нам хотела..."
    show kamuko om
    kam "Да-да-да, но я ещё в Клубе выпечки."
    show kamuko cm
    s "Том самом?!"
    show kamuko om ce b1c
    kam "Том самом, с которым у вас интрижки!"
    show kamuko neut om oe -b1c
    kam "А, тебя же не было в этой заварушке, да?"
    show kamuko cm
    s "Не было."
    show kamuko happ om oe b1c ldown rdown
    kam "У-у-ух, ну и правильно!"
    show kamuko ce
    kam "Туда эти конфликты со всякой дурью!"
    show kamuko cm
    s "Ха-ха-ха!"
    show kamuko om e1e -b1c lhiphid rface
    kam "Слушай, а мы с тобой в чём-то похожи..."
    show kamuko cm
    s "Да..."
    show kamuko pani om oe lup rup at h11
    kam "Ой, точно!"
    show kamuko happ om oe lhiphid rface
    kam "Если ты не знакома с Клубом выпечки, то хочешь сейчас познакомиться?"
    show kamuko cm
    s "...правда?"
    show kamuko om ce rhid
    kam "Честно-честно!"
    show kamuko nerv om oe rface
    kam "Только надо делать это быстро, пока перемена не закончилась, потому что нужно обследовать всю школу, так как все участники могли разбрестись куда угодно..."
    show kamuko cm
    "...а почему бы...{w}и нет?"
    show kamuko happ cm oe rhid
    "Мне всё равно нечем заняться: не сидеть же в классе и пялиться в окно или на окружающих?"
    s "...давай?"
    show kamuko om ce ldown rdown at h11
    kam "Отличный выбор!"
    show kamuko e4c
    kam "Поскакали!"
    show kamuko cm
    s "Стой!"
    show kamuko curi om oe
    kam "Э?"
    show kamuko neut cm oe
    s "Я сок не допила!"
    show kamuko happ cm oe
    s "Правда, я его уже не хочу..."
    show kamuko om ce lhiphid rface
    kam "А, сейчас исправим это дело!"
    show kamuko cm
    call window_close

    $ kam_name = "???"

    call window_dialog_fast_transition("k")

    stop noise_1
    play noise_1 school_corridor_hard_noise

    call window_open
    scene bg school f2 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    k "Ах, ну и чего она там закопалась?..."
    "Уже минуту возится со своей сумкой."
    "Будто кто-то намерен её украсть."
    show libitina forward happ cm ce at t11 zorder 2
    pause 0.2
    show libitina om
    l "У-ух, я здесь."
    show libitina cm
    k "Наконец-то!"
    show libitina oe
    k "Что же ты так усердно ковырялась?"
    show libitina om
    l "Не ковырялась, а искала колёсико от ножки циркуля."
    show libitina cm
    k "...даже не буду задаваться вопросом, как оно смогло выпасть из пенала в сумку..."
    show libitina om ce
    l "Правильно, не будем тратить время попусту."
    show libitina oe
    l "Потому что колёсико я уже прикрутила обратно."
    show libitina neut cm oe
    kam "{size=19}ДОРОГУ!{/size}"
    show libitina shy neut cm oe
    k "А?"
    show libitina ef be
    k "{sc=3}ЛИНА, ВПРАВО!{/sc}"
    show libitina at t33
    pause 0.1
    show kamuko turned happ cm e4c headband_cat at t53 zorder 4
    show sayori turned happ cm e4c at t52 zorder 3
    with easeinleft
    show kamuko at thide
    hide kamuko
    show sayori at thide
    hide sayori
    pause 1.0
    k "Что?!"
    k "Сайори?!"
    show libitina forward angr ma oe
    k "Почему они--{nw}"
    show libitina om
    l "Ты назвала меня \"Линой\"?"
    show libitina shy angr om oe
    l "{cps=15}К-о-х-а?{/cps}"
    show libitina ma
    k "Ли...{w}кх-х-х..."
    call window_close

    $ kam_name = _("Камуко")

    call window_dialog_fast_transition("mc")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene bg school new_class_mc day
    mc "{size=19}Прогуляться до крыши, что ли?{/size}"
    "В телефоне уже всё вдоль и поперёк проверил -- достало заглядывать в него каждую минуту."
    "Окружению...{w}вообще фиолетово на моё состояние."
    "Всё-таки среди него я так и не выявил людей, которым бы чуть-чуть, но симпатизировал."
    "А натягивать себя на общение с теми, кому на меня плевать, нет никакого желания."
    "Короче, надо пойти и освежиться, заодно собраться с мыслями и снова проанализировать эти чёртовы кошмары."
    "В них явно есть посыл, который мне нужно осознать...{w}или найти причину, по которой они появились."
    "Да, раньше я думал, что это просто набор тупого воображения, но чем дальше, тем...{w}они становятся более «сюжетноориентированными»?"
    show kamuko turned happ cm oe n2 headband_cat at l21 zorder 2
    show sayori turned happ cm oe n2 at l22
    pause 0.5
    show sayori om
    s "Макс, снова привет!"
    show kamuko om ce
    show sayori cm
    kam "Вот и новенький!"
    show kamuko cm
    show sayori ce
    mc "Пф-ф-ф!" with vpunch
    show kamuko oe
    mc "А вы чего сюда прискакали?"
    show kamuko om rface
    show sayori oe
    kam "На огонёк забежали!"
    show kamuko cm
    show sayori om
    s "Ага!"
    show kamuko om rdown
    show sayori cm
    kam "А так я хотела познакомить Сайори со всем Клубом выпечки!"
    show kamuko cm
    mc "Ха, весело..."
    show sayori ce
    "Сайори уже умудрилась найти себе приключение."
    show kamuko e1b
    "Подождите..."
    show kamuko neut cm oe
    show sayori neut cm oe
    mc "Вы бегали по коридорам?"
    show kamuko nerv cm oe lhid rhid
    show sayori nerv mb oe
    s "Немножко..."
    show kamuko om
    show sayori cm
    kam "Да не, всё классно, мы скорость не превышали!"
    show kamuko cm e2c
    mc "Оттого у вас капли пота по лицу стекают?"
    show sayori tap nerv om e2 n2  at s22
    s "Э-хе-хе..."
    show kamuko neut cm e2e
    show sayori neut cm oe
    e "{size=19}О!{/size}"
    show sayori turned neut cm oe n2  at t22
    pause 0.1
    show emi turned happ cm oe lhip rhip at l31
    show kamuko at t32
    show sayori at t33
    pause 0.5
    show emi om
    show kamuko happ cm oe lhiphid
    show sayori happ cm oe
    e "Неожидала вас здесь увидеть!"
    show emi cm
    show kamuko om ce
    kam "Ха-ха, Эми, привет!"
    show kamuko cm
    show sayori om
    s "Приветик!"
    show emi cross happ cm oe
    show kamuko om oe
    show sayori cm
    kam "Кстати, Сайори, вот, это Эми!"
    show emi happ mk ce bb n2
    show kamuko curi cm oe
    e "Да мы с ней и так знакомы."
    show sayori ce
    s "Угу!"
    show kamuko om
    kam "А-а-а..."
    show emi om oe brow -n2
    show kamuko cm e1b
    show sayori oe
    e "И Макс здесь?"
    show emi cm
    mc "Как видишь."
    show emi om
    show kamuko happ cm oe
    show sayori b1c
    e "С ними за компанию?"
    show emi neut cm oe
    mc "Здесь мой класс, здрасьте."
    show emi ec
    show kamuko ce b1c
    show sayori ce -b1c
    mc "Они сами сюда прискакали."
    show emi om
    e "Э-э-э, понятно."
    show emi cm
    show kamuko oe -b1c
    show sayori oe
    mc "К слову, об этом..."
    show emi oe
    show kamuko nerv cm oe lhid
    show sayori nerv cm oe
    mc "Сайори, Камуко, не надо носиться по коридорам!"
    mc "Собьёте же кого-нибудь по пути или сами куда-то вмажитесь."
    show emi curi cm oe
    show kamuko pani cm oe
    show sayori curi cm oe
    mc "Хотите себе проблем нажить, особенно от Рэйко?"
    show kamuko om ce lup rup at h32
    kam "Бр-р-р, не-не-не!"
    show emi happ cm ce bb n2
    show kamuko cm
    show sayori neut cm oe
    mc "Другое дело."
    show emi oe brow -n2
    show kamuko neut cm oe ldown rdown
    mc "Если и перемещаться, то только быстрым шагом."
    show kamuko happ cm oe
    show sayori happ cm oe
    mc "Хорошо?"
    show sayori om
    s "Да."
    show kamuko om ce
    show sayori cm
    kam "Без вопросов!"
    show kamuko cm
    mc "Отлично."
    show kamuko om oe at h32
    kam "Всё, у нас нет времени!"
    kam "Нам нужно найти остальных!"
    show emi neut cm oe
    show kamuko curi om oe
    kam "Эми, ты никого из наших не видела?"
    show emi om ec
    show kamuko cm
    show sayori neut cm oe
    e "У-у-у..."
    show emi angr om ec
    show kamuko neut cm oe
    show sayori curi cm oe
    e "Вроде бы с Юри кто-то был..."
    e "В классе этого коридора в дальнем углу..."
    show emi neut cm ec
    show kamuko happ om e4c at h32
    kam "Потрясающе!"
    show emi happ cm oe
    show kamuko oe
    kam "Сайори, пошли!"
    show kamuko cm ce
    hide kamuko with easeoutleft
    pause 0.1
    show emi neut cm oe
    show sayori flus om oe
    s "А-а, э-э..."
    show sayori happ om oe
    s "Макс, расскажу обо всём в клубе!"
    show emi happ cm oe
    show sayori cm
    mc "Конечно."
    show sayori om ce
    s "До скорого!"
    show sayori cm
    hide sayori with easeoutleft
    pause 0.2
    show emi turned happ cm oe lhip rhip
    mc "Ох..."
    show emi om
    e "Это что, получается, две ядерные батарейки?"
    show emi cm
    mc "Батарейки?"
    show emi laug cm ce
    mc "По-моему, тут целый мини-реактор."
    call window_close

    call window_dialog_fast_transition("sor")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    $ r_name = "???"

    call window_open
    scene black
    pause 0.5
    play sound door_knock
    pause 1.8
    sor "Прошу прощения, можно войти?"
    r "{size=19}Входите!{/size}"
    call window_close

    pause 1.0
    play sound closet_open
    pause 1.0

    $ r_name = _("Рэйко")

    call window_open
    scene bg school office_reiko
    show reiko turned uniform_council neut cm oe lhip at t11
    with wipeleft_scene
    show reiko b1c
    sor "А, Рэйко-сан, здравствуй..."
    show reiko om ce rup
    r "Рэйко-сан, Рэйко-сан..."
    show reiko tough uniform_council happ_om_oe
    r "А как дома, так сразу Рэйко-тян!"
    show reiko neut_cm_oe
    sor "Формальности никто не отменял."
    show reiko turned uniform_council neut cm oe lhip
    sor "К тому же в этот импровизированный микроофис могут зайти в любой момент."
    show reiko om
    r "Ладно, ты по какому делу?"
    show reiko cm b1c
    sor "Снова насчёт Клуба выпечки."
    show reiko om ce rup
    r "...ф-ф-ф, что на этот раз?"
    show reiko cm oe rdown
    sor "Я понимаю, прошло всего 2 дня, но Кохаку меня теперь люто ненавидит."
    show reiko om ce rthink -b1c
    r "Логично с её точки зрения, но маразматично с адекватной."
    show reiko oe rdown
    r "Пока всё ожидаемо."
    show reiko cm
    sor "В том то и дело, что нет."
    show reiko b1c
    sor "Рэйко-тян, я хочу уйти из этого клуба и взять перерыв."
    sor "Готов хоть прямо сегодня."
    show reiko om
    r "Э-э-э, ты что, забыл?"
    show reiko lpoint
    r "Пока не решим с ней проблему, никаких уходов!"
    show reiko cm lhip
    sor "А она нерешаема!"
    show reiko -b1c
    sor "Создаётся такое впечатление, что все прошедшие события у неё влетели в одно ухо и вылетели насквозь из другого."
    sor "Нет, я знал, что она будет упёртой и вряд-ли так сразу исправится, но я не думал, что она вообще никак не поменяется."
    sor "Всё, что в ней изменилось, -- она стала более вспыльчивой."
    show reiko om ce lpoint
    r "И при этом с заключённым со мной договором."
    show reiko cm oe ldown
    sor "Вот именно, что это совершенно не поменяло её поведение."
    show reiko om lhip
    r "Ну тогда ждём, когда она его нарушит."
    show reiko cm
    sor "Ой, сестра..."
    show reiko cm oe b1c
    sor "Я устал сидеть против своей воли там, где постоянно льётся нескончаемый негатив в мою сторону."
    show reiko om rup
    r "А ты думаешь, мне легче?"
    show reiko ce rdown
    r "Тут постоянно кто-то да нарушает школьные правила, постоянно надо проводить обсуждения по дурацким мероприятиям и заниматься бесконечной бюрократией!"
    show reiko cm
    sor "У тебя это необходимость!"
    show reiko oe
    sor "У меня -- наигранность."
    sor "Вместо клуба я бы мог тратить время на хозяйство по дому."
    sor "Или на учёбу."
    sor "Да даже уйти в другой клуб, который будет для меня более продуктивным."
    sor "Хоть в Литературный!"
    sor "Там пользы будет в разы больше, чем это вот всё."
    show reiko om ce
    r "Твоя душераздирающая речь меня эмоционально не впечатлила."
    show reiko cm
    sor "Тогда можешь распрощаться со своим любимым тамагояки по утрам--{nw}"
    show reiko happ om ce -b1c lpoint
    r "...однако, как любящая сестра, я тебя прекрасно понимаю."
    show reiko cm ldown
    sor "А..."
    show reiko tough uniform_council happ_om_oe
    r "Ха, ты думал, что я так просто возьму и откажусь от твоего омлета?"
    show reiko neut_cm_oe
    sor "То есть для тебя омлет важнее заботливого брата..."
    show reiko turned uniform_council happ om ce
    r "Сора, хорош, ха-ха-ха!"
    show reiko oe lhip rup
    r "Я подумаю над твоими словами ввиду исчерпания твоего «ресурса» в этом деле, но сегодня ты всё ещё часть Клуба выпечки, понял?"
    show reiko cm rdown
    sor "Понял-понял."
    sor "Тогда я пойду, не буду мешать."
    show reiko om
    r "Да, не держу тебя."
    show reiko cm
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    kam "{size=19}О, ещё один!{/size}"
    kam "{sc=3}СОРА!!!{/sc}"
    sor "А?!"
    play sound falldown
    pause 0.15
    with vpunch
    pause 0.75

    scene bg school office_reiko
    show sayori turned happ cm oe n2  at t51 zorder 2
    show kamuko turned happ cm oe n2 headband_cat at t52 zorder 3
    show reiko turned uniform_council vsur cm oe lhip at t21
    with dissolve
    show kamuko om rup
    kam "Сайори, Сора!"
    show sayori ce
    show kamuko ce lup rdown
    kam "Сора, Сайори!"
    show sayori neut cm oe
    show kamuko cm ldown
    show reiko at t53
    sor "Камуко, ты что творишь?!"
    show sayori happ cm oe
    show kamuko om oe
    kam "Знакомлю Сайори, вице-президента Литературного клуба, со всем Клубом выпечки!"
    show sayori pani cm oe at h51
    show kamuko pani om oe at h52
    show reiko happ cm oe b1c
    kam "{sc=3}А-А-А, Рэйко!!!{/sc}" with vpunch
    show kamuko ce lhid rhid
    kam "{sc=2}Рэйко, сумимасен!{/sc}"
    show kamuko oe ldown rdown
    kam "{sc=3}САЙОРИ, УХОДИМ!{/sc}"
    show kamuko cm
    show sayori ce
    s "{sc=1}П-п-прости--{/sc}{nw}"
    show kamuko ce at lhide
    hide kamuko
    show sayori om at lhide
    hide sayori
    play sound sayori_hide_fast
    s "{sc=3}--ТЕ!{/sc}"
    sor "..."
    show reiko om ce -b1c lpoint
    r "Видишь, какой у меня имидж?"
    show reiko oe lhip
    r "Я даже ничего сказать не успела, а они уже извинились и быстро ушли."
    show reiko cm
    sor "Зная твою «официальную» личность...{w}на их месте я бы себя до атомов аннигилировал."
    show reiko ce
    call window_close

    call window_dialog_fast_transition("y")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene bg school new_class_natsuki day
    "Конечно, я хотела почитать в одиночестве на лестнице, потому что в книге начались интересные события, но не хочу отказывать Нацуки от совместного времяпрепровождения..."
    show natsuki turned happ cm oe lhip rhip school_bag at t11
    pause 0.2
    show natsuki om ce b1d
    n "Всё, я готова!"
    show natsuki cm
    y "Ум-м, хорошо..."
    show natsuki oe -b1d
    "...а также я хотела ещё раз обдумать прошлый вечер..."
    show natsuki neut cm oe ldown rdown
    "До сих пор стыдно за всё сказанное Максу...{w}или не стыдно..."
    "Чувствую себя более уязвимой, чем когда-либо..."
    show natsuki doub om oe
    n "Ау, Юри!"
    show natsuki cm
    y "Э?!"
    show natsuki curi om oe
    n "Чего вид у тебя грустный?"
    show natsuki laug om oe lhip rhip
    n "Чай пила невкусный?"
    show natsuki cm
    y "Нацуки..."
    show natsuki om ce
    n "Да не кисни ты!"
    show natsuki cm
    call window_close

    hide natsuki
    show natsuki turned happ cm oe b1d lhip rhip school_bag at el11 zorder 2
    with dissolve
    pause 0.5

    call window_open
    show natsuki om
    n "У-лыб-нись!"
    show natsuki cm
    y "Фто ты делаеф?"
    y "Отпуфти мои фёки."
    show natsuki laug om ce -b1d
    n "Вот, такой вид уже получше!"
    show natsuki cm
    h "Кхмпф!"
    show natsuki pani om oe
    n "{sc=3}А-А-А!{/sc}" with vpunch
    call window_close

    hide natsuki
    show natsuki turned pani cm oe school_bag at i21 zorder 2
    show hiroshi fc laug cm ce rhip at i22
    with dissolve
    pause 0.5

    call window_open
    y "Фе-е-е!"
    show natsuki vang cm oe lhip rhip
    "Будто со всем «остервенением» моё лицо растянула!"
    show natsuki om
    n "Не смешно!"
    n "Пшёл отсюда!"
    show natsuki cm
    show hiroshi happ om ce
    h "Ну хватит, Нацуки!"
    show hiroshi oe
    h "Я даже ничего не сделал!"
    show natsuki cross angr om ce school_bag
    show hiroshi cm
    n "И на том спасибо!"
    show natsuki cm
    "Снова этот грубый тип..."
    show natsuki curi cm oe
    show hiroshi om
    h "И вообще, я поблагодарить тебя хотел!"
    show natsuki om
    show hiroshi cm
    n "За что?"
    show natsuki cm
    show hiroshi om
    h "Ты меня мотивировала на поиск этого...{w}как его...{w}«Ванильной симфонии»!"
    show natsuki turned anno om oe lhip rhip school_bag
    show hiroshi cm
    n "Поздравляю."
    show hiroshi neut cm oe
    n "Держи в курсе."
    show natsuki om ce
    n "Мы уходим."
    show natsuki neut om oe b1d ldown rdown
    n "Юри, пошли!"
    show natsuki cm
    y "А-а-а, да, пошли!"
    show natsuki e4a
    hide natsuki with easeoutright
    pause 0.2
    show hiroshi anno cm oe rdown
    h "..."
    call window_close

    call window_dialog_fast_transition("s")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene bg school new_class_yuri day
    show kamuko turned pani om oe n2 headband_cat at h11
    kam "Юри исчезла!"
    show kamuko curi om oe lhiphid rface
    kam "Ты не знаешь, где она может быть?"
    show kamuko cm
    s "Э-э-э, нет..."
    show kamuko happ om ce ldown rdown
    kam "Ладно, не за ней пришли!"
    show kamuko curi om e1c
    kam "Где тут кто-то из наших?..."
    show kamuko cm e1b
    kam "М-м-м..."
    show kamuko lsur om oe at h11
    kam "О!"
    $ f_name = _("Фукка")
    show kamuko happ om ce at thide
    hide kamuko
    kam "Фукка-чан!"
    "Ай, как громко!"
    "Нас так все окружающие взглядами прожгут!"
    kam "{size=19}Да не бойся ты, иди сюда!{/size}"
    f "{size=19}{cps=20}Б-б-б-б-б--{/cps}{/size}{nw}"
    show fukkacumi cross grab worr me oe at t21
    show kamuko turned happ cm ce headband_cat at t22 zorder 3
    pause 0.2
    show kamuko om
    kam "Вот она, красавица!"
    $ f_name = _("Фуккацуми")
    show fukkacumi neut cm oe
    show kamuko oe lup
    kam "Сайори, Фукка, а полностью -- Фуккацуми!"
    show fukkacumi nerv cm oe
    show kamuko ce ldown rup
    kam "Фукка, Сайори!"
    show fukkacumi e1a
    show kamuko cm rdown
    s "Приве-е-ет!"
    show fukkacumi happ om ce b1b
    show kamuko oe
    f "{cps=20}П-при-ивет...{/cps}"
    show fukkacumi cm
    show kamuko om lhiphid rface
    kam "Она у нас очень стеснительная, но хорошенькая!"
    show fukkacumi worr cm oe -b1b
    show kamuko ce
    kam "А ещё из России!"
    show kamuko cm
    s "Из России?"
    "По ней не скажешь, что она иностранка..."
    show kamuko om oe
    kam "Ага!"
    kam "Точнее, папа, но он сюда переехал."
    show fukkacumi vsur cm oe at h21
    show kamuko oe ldown rdown
    kam "Да, Фукка?"
    show fukkacumi e4c:
        linear 0.05 xoffset 5
        linear 0.05 xoffset 0
        linear 0.05 xoffset -5
        linear 0.05 xoffset 0
        repeat
    show kamuko cm
    f "{cps=15}Эве-ве-ве-ве-ве--{/cps}{nw}"
    show kamuko om ce
    kam "Думаю, она согласна."
    show kamuko cm
    s "Э-э-э..."
    "Не похоже, что она рада нашему визиту..."
    show kamuko oe
    s "Камуко, может--{nw}"
    show fukkacumi oe at h21
    show kamuko vsur cm oe at h22
    koh "{size=19}Э, отстаньте от Фукки!{/size}"
    show fukkacumi lsur cm oe
    show kohaku turned angr cm oe at l52 zorder 2
    pause 0.5
    show kohaku cross angr cm oe
    show kamuko lsur om oe
    kam "Ого, и сама Кохаку здесь!"
    show fukkacumi at tcommon(310)
    show kohaku angr om oe
    show kamuko cm
    koh "Чё?"
    show kohaku neut m3a oe
    show fukkacumi neut cm oe
    show kamuko happ om oe lup
    kam "Сайори, Кохаку, глава нашего клуба!"
    show kamuko cm ldown
    koh "Сайори?"
    show kamuko om ce rup
    kam "Кохаку, Сайори, вице-президент Литературного клуба!"
    show kohaku angr m3a oe
    show kamuko cm rdown
    koh "Серьёзно?"
    "Какая она злая..."
    show fukkacumi e1b
    "Мне уже за себя страшно."
    show kamuko curi om oe lhid rhid
    kam "А что несерьёзного?"
    show kohaku curi om oe
    show kamuko cm
    koh "Хотя..."
    show fukkacumi oe
    show kamuko neut cm oe
    koh "Тебя же не было тогда, да?"
    show fukkacumi at thide
    hide fukkacumi
    show kohaku angr cm oe
    show kamuko om
    kam "Не было её."
    show kohaku om
    show kamuko angr cm oe
    koh "Я Сайори спрашивала."
    show kohaku cm
    show kamuko om
    kam "А мне без разницы, ответ от этого не поменяется!"
    show kohaku om ce
    show kamuko cm
    koh "Камуко, помолчи, а?"
    show kamuko om ce
    kam "Фи!"
    show kohaku curi om oe
    show kamuko cm
    koh "Так тебя не было?"
    show kohaku happ cm oe
    s "Не было."
    show kohaku om ce
    show kamuko oe
    koh "Прекрасно, хоть кто-то ещё, кроме Юри, есть нормальный в вашем клубе..."
    show kohaku cm
    show kamuko ldown rdown
    "Как оскорбительно!"
    show kohaku angr cm oe
    show kamuko om rface
    kam "Вот это было грубо!"
    show kohaku om
    show kamuko cm rdown
    koh "А мне что, вас теперь превозносить и называть пуськами после всего случившегося?"
    show kohaku cm
    show kamuko om ce
    kam "Даже спорить не хочу, бла-бла-бла!"
    show kohaku om
    show kamuko cm
    koh "Иди ты...{w}отсюда!"
    show kohaku cm
    show kamuko om oe
    kam "С радостью, злыдня!"
    show kamuko happ om e4c lup rup at h22
    kam "Сайори, помчали!"
    show kamuko cm
    s "Угу!"
    show kamuko ldown rdown
    hide kamuko with easeoutleft

    scene black with wipeleft_scene
    s "Она всегда у вас такая...{w}недобрая?"
    kam "О-хо-хо, чем дальше, тем хуже!"
    kam "Но сейчас она пуще прежнего из-за словесной драки, которая была недавно...{w}практически неделю назад?!"
    s "...да, неделю."
    kam "Как быстро летит время!"
    call window_close

    call window_dialog_fast_transition("y")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene black
    n "Почему ты такая грустная?"
    n "Вчера вместе с Максом стих писала, должна сиять от счастья."
    y "Я...{w}рассказала ему про...{w}порезы..."
    y "Э-э, не про сами порезы, а про причину..."
    n "Вот оно что..."
    n "Окей, придём -- обсудим твоё состояние."
    n "Может, и мне наконец-то расскажешь причину..."
    n "Так, стоп."
    y "Что случилось?"
    n "Мне кажется, или я вижу Сайори...{w}с Камуко?!"
    y "Ох..."
    n "Когда они так подружиться успели?!"
    y "Я бы поставила здесь вопрос не во времени, а в скорости..."
    n "Один фиг."
    n "..."
    n "Они нас заметили..."
    y "И?"
    n "Что \"и\"?"
    n "Юри, если они к нам присосутся, то мы до лестницы не дойдём."
    n "А если и дойдём, то очень вероятно, что они захотят посидеть с нами!"
    n "А твою проблему обсудить надо без лишних глаз!"
    y "Ум-м..."
    n "Я же права?"
    n "Права."
    y "Тогда давай ускоримся и уйдём в толпу на втором этаже, потому что они сейчас идут быстрым шагом к нам..."
    n "Что?!" with vpunch
    play music natsuki_run
    n "Надо было сразу говорить, ПОБЕЖАЛИ!"
    y "{sc=3}Ай, не дёргай меня так!{/sc}"
    call window_close

    call window_dialog_fast_transition("s")

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene black
    kam "Сайори, они ретируются!"
    s "Что?!"
    s "Почему?!"
    kam "Догоним -- спросим!"
    kam "А сейчас поднажмём!"
    s "А как же Рэйко?!"
    s "И слова Макса?!"
    kam "Они все сзади!"
    kam "Бежим скорее!"
    call window_close

    call window_dialog_fast_transition("mc")

    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.1

    stop noise_1
    play noise_1 school_corridor_light_noise volume 0.5

    call window_open
    scene bg school f3 new_corridor
    show emi turned neut cm oe lhip rhip at i11
    mc "Странно, что Нацуки с тобой теперь не общается..."
    show emi angr om ee n2
    e "Да тут, как и сказала, мы перестали часто пересекаться после её ухода."
    show emi neut om oe -n2
    e "Она в одном клубе, я в другом."
    show emi cm
    mc "Мдэ..."
    "Я бы сказал, что рвать связь по такой причине довольно глупо, но...{w}с тем другом мы примерно так же общаться перестали..."
    "Девушка его увлекла, он ушёл в другой «социум»."
    "А я остался на том же месте."
    show emi lsur cm oe
    n "{sc=3}В СТОРОНУ!!!{/sc}"
    mc "Чего?"
    $ audio.natsuki_run_2 = "<from " + str(currentpos) + " loop 1.541>mod_assets/music/characters/n/run.ogg"
    play music natsuki_run_2 fadein 0.5
    show natsuki turned pani cm oe school_bag at t55 zorder 2
    pause 0.25
    show emi el ldown rdown at h11
    hide natsuki with easeoutleft
    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.4
    mc "Эй!"
    $ audio.natsuki_run_2 = "<from " + str(currentpos) + " loop 1.541>mod_assets/music/characters/n/run.ogg"
    play music natsuki_run_2 fadein 0.5
    show yuri turned pani cm e4c lup rup school_bag at t55 zorder 2
    pause 0.25
    hide yuri with easeoutleft
    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.4
    mc "Вы что творите?!"
    show emi oe n2
    mc "Нельзя бегать!"
    $ audio.natsuki_run_2 = "<from " + str(currentpos) + " loop 1.541>mod_assets/music/characters/n/run.ogg"
    play music natsuki_run_2 fadein 0.5
    show yuri turned pani cm ce lup rup school_bag at l51
    pause 0.5
    show yuri om
    y "{sc=2}П-прости, Макс!{/sc}"
    show yuri oe
    show emi curi cm oe
    y "{sc=2}Мы убегаем от Сайори и Камуко.{/sc}"
    show yuri cm
    n "{sc=3}ЮРИ, НЕ ТОРМОЗИ!!!{/sc}"
    show yuri om e4c at h51
    pause 0.15
    show yuri at lhide
    hide yuri
    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.4
    y "{sc=3}А-а-а, прости!!!{/sc}"
    show emi angr om ee -n2 lhip rhip
    e "Когда-нибудь терпение Рэйко лопнет и она открутит Нацуки голову за бег..."
    show emi neut cm oe
    mc "А она много раз попадалась?"
    show emi om ef
    e "...часто."
    show emi cm
    show kamuko turned pani cm oe n2 headband_cat at t54 zorder 2
    show sayori turned pani cm oe n2 at t55
    pause 0.2
    $ audio.natsuki_run_2 = "<from " + str(currentpos) + " loop 1.541>mod_assets/music/characters/n/run.ogg"
    play music natsuki_run_2 fadein 0.5
    show kamuko om lup rup at h54
    kam "{sc=3}Они практически удрали!{/sc}"
    show emi cross dwayne
    show kamuko cm ldown rdown
    show sayori om ce
    s "{sc=3}Буе-е-е!{/sc}"
    play music_none_loop music_stop
    stop music
    show emi laug cm ce -dwayne
    show kamuko mj ce at h54
    show sayori mj at h55
    mc "ТАК, ВСЁ, СТОП!" with vpunch
    show kamuko nerv cm ce
    show sayori vsur cm oe
    mc "Что я говорил несколько минут назад?!"
    show sayori at s55
    s "Ай-ай-ай!"
    show kamuko om lhid rhid
    show sayori laug cm ce
    kam "Не ругайся, сенсей!"
    show kamuko cm
    show sayori at t55
    mc "Когда я вам сенсеем стать успел?"
    show emi happ om oe
    e "Да она же прикалывается!"
    show emi cm
    show kamuko neut cm oe
    show sayori happ om ce
    s "Но мы так и не поняли, почему они убегали."
    show emi neut cm oe
    show kamuko curi om e1a ldown rdown
    show sayori cm oe
    kam "Они вам что-то говорили?"
    show kamuko cm
    show sayori neut cm oe
    mc "Кроме факта самого побега, нет."
    show emi om
    show kamuko neut cm oe
    e "А что тут думать?"
    show kamuko pout cm oe lhiphid rhid
    show sayori angr cm oe
    e "Они просто не захотели с вами общаться."
    show emi cm
    show kamuko om
    kam "Мы всего лишь хотели парочкой фраз перекинуться!"
    show emi angr md ee n2
    show kamuko cm
    e "...даже так."
    show kamuko ce
    show sayori om ce
    s "Не думала, что Юри и Нацуки такие злюки!"
    show emi neut cm oe -n2
    show sayori cm
    mc "Ой, ладно вам."
    show emi curi cm oe
    show kamuko neut cm oe
    show sayori neut cm oe
    mc "Наверное, ушли куда-нибудь уединиться, чтобы...{w}э-э-э..."
    show emi happ mk ce bb n2
    show kamuko lsur cm oe
    show sayori pout cm e1d
    e "Макс, это прозвучало слишком двусмысленно."
    show sayori om ce
    s "Фу!"
    show emi oe
    show kamuko om e1d rface
    show sayori cm
    kam "...посекретничать?!"
    show emi ce
    show kamuko cm
    e "Ещё лучше..."
    show emi laug cm ce brow -n2
    show kamuko curi cm oe rhid
    show sayori neut cm oe
    mc "Да чёрт вас побери, вы все мысли сбили!"
    show emi happ cm oe
    show kamuko neut cm oe
    mc "Книгу там почитать...{w}что-то такое, ну?"
    show kamuko om e1b
    kam "А-а-а..."
    show kamuko cm
    show sayori om
    s "Точно..."
    show emi neut cm oe
    show sayori e1b
    s "Они обычно в это время этим и занимаются."
    show sayori b1c
    s "Совсем про это забыла..."
    show kamuko happ om ce ldown rdown
    show sayori cm
    kam "Ясненько-понятненько."
    show kamuko oe
    show sayori oe -b1c
    kam "А вы сами куда шли?"
    show emi om ec
    show kamuko cm
    e "Туда...{w}не знаю куда."
    show emi cm
    show sayori happ cm oe
    mc "Шли, куда идётся."
    show emi oe
    show kamuko om
    kam "Может, тогда все вместе пройдёмся, например..."
    show kamuko ce
    show sayori neut cm oe
    kam "...на крышу?"
    show kamuko cm
    show sayori om
    s "И что мы будем там делать?"
    show kamuko curi om oe
    show sayori cm
    kam "Как что?"
    show emi happ cm oe
    show kamuko happ om ce lhiphid rhid
    kam "Общаться-разговаривать, дыша свежим воздухом!"
    show emi sedu cm oe
    show kamuko e2d rface at h54
    show sayori curi cm oe
    kam "Знаете, сколько у меня разных историй накопилось за всю жизнь?!"
    show emi happ om ce
    show kamuko cm rhid
    e "Ха-ха-ха, охотно верю!"
    show kamuko ce
    show sayori lsur md oe
    e "Ты нам в клубе каждый раз рассказываешь истории, офигительнее предыдущих."
    show emi cm
    show kamuko om
    kam "Вот-вот!"
    show kamuko cm
    show sayori om
    s "Ничего себе..."
    show sayori me
    "Хм, Камуко и не такая надоедливая, как я думал изначально..."
    show emi turned happ cm oe lhip rhip
    show kamuko om oe
    show sayori happ cm oe
    kam "Ладушки, всё, пошли!"
    show kamuko ce
    kam "Осталось 30 минут от перемены!"
    show kamuko cm
    pause 0.1
    play music ringtone_mc
    pause 1.3
    show emi neut cm ec ldown rdown
    show kamuko pani cm oe at h54
    show sayori neut cm e2a
    pause 1.0
    show emi oe
    show kamuko om
    kam "Телефон?!"
    show kamuko cm
    show sayori oe
    mc "Это мой."
    show kamuko neut cm oe
    "Ну и кому я, блин, понадобился в данный момент..."
    "..."
    "...Моника?"
    show emi cross curi cm oe
    show kamuko curi cm oe
    show sayori b1c
    mc "Ребят, простите, но я отойду на секунду."
    show sayori om
    s "Что-то очень важное?"
    show emi neut cm oe
    show sayori cm
    mc "Не знаю, сейчас выясню."
    show emi om
    show kamuko neut cm oe
    e "Мы здесь подождём."
    show emi cm
    mc "Угу."
    call skip_block_on
    call window_close

    scene black with wipeleft_scene

    phone call_accept "m"
    phone call "m"

    stop music
    pause 0.75

    call window_open
    call skip_block_off
    phone_mc "Алло."
    phone_m "Привет, Макс."
    phone_mc "В честь чего аж целый звонок вместо парочки сообщений в мессенджере?"
    phone_m "Тут...{w}в общем, у меня есть важная информация."
    phone_m "Прямо как ты мне вчера написал, хах."
    phone_m "Я хотела её с тобой обсудить сейчас вживую."
    phone_m "Так мне будет проще всё сказать."
    phone_mc "Хм..."
    phone_m "Именно поэтому я позвонила, чтобы ты точно вышел на связь."
    phone_mc "Ладно, понял, где встретимся?"
    phone_m "На крыше старого корпуса."
    phone_mc "Откуда у вас всех такая любовь к крышам..."
    phone_m "Ой, Макс, дойдёшь, не развалишься~"
    phone_mc "Я имел в виду, может, другие места?"
    phone_m "Окружающим на открытом воздухе будет хуже нас слышно."
    phone_m "А ещё сейчас дикие толпы шляются по первому и второму этажу."
    phone_mc "Хорошо, уговорила."
    phone_mc "Ты уже там?"
    phone_m "Да."
    phone_mc "Понял, жди."
    phone_m "Давай, а то я обижусь!"
    phone_m "Бай-бай~"
    window hide

    phone end call "27/04/2018" transition

    window auto
    "Обидется она..."

    scene bg school f3 new_corridor
    show emi cross happ cm oe at t31
    show kamuko turned happ om ce n2 headband_cat at t32 zorder 2
    show sayori turned neut cm oe n2 at t33
    with wipeleft_scene
    show emi neut cm oe
    show kamuko neut cm oe
    mc "Ребят, ещё раз простите, но мне придётся вас покинуть."
    show emi curi cm oe
    show kamuko curi om oe at h32
    kam "Э-э-э?!"
    show kamuko e1a lhiphid rhid
    kam "А как же прогуляться?!"
    show emi neut cm oe
    show kamuko cm
    mc "Как-нибудь позже, а пока без меня."
    show kamuko oe
    hide sayori
    show sayori turned neut cm oe n2 at e22 zorder 3
    with dissolve
    pause 0.25
    show sayori om
    s "{size=19}Тебя Моника вызвала?{/size}"
    show sayori cm
    mc "{size=19}...а как...{/size}"
    show sayori happ om oe
    s "{size=19}Юри и Нацуки сейчас заняты, я тут, с Котонохой ты бы вряд ли так общался, поэтому остаётся только Моника.{/size}"
    show sayori cm
    mc "{size=19}Ну ты и детектив.{/size}"
    show sayori om ce
    s "{size=19}Э-хе-хе...{/size}"
    show sayori cm
    "Порой Сайори меня пугает своими выпадами..."
    show emi turned neut cm oe lhip rhip
    show kamuko neut cm oe
    show sayori neut cm oe
    mc "Ладно, всё, я пошёл."
    show kamuko worr om ce
    show sayori flus cm oe
    kam "Обида..."
    show emi angr md ee
    show kamuko cm
    e "Эх, пока--{nw}"
    show emi neut md oe
    show kamuko neut cm e2a
    show sayori om
    s "А можно мне с тобой?!"
    show sayori cm
    mc "Что?"
    show emi md
    show sayori md e2b
    "Чёрт, Сайори тут ещё не хватало."
    "Явно же эта встреча не для «лишних глаз»."
    show emi cross curi cm oe
    show kamuko oe
    show sayori neut cm oe
    mc "{size=19}Сайори, там что-то важное, а может, и личное...{/size}"
    show sayori happ om oe
    s "{size=19}Но я же вице-президент: мне тоже нужно всё знать!{/size}"
    show sayori neut cm oe
    mc "{size=19}Сайори, подчёркиваю -- личное.{/size}"
    show sayori om
    s "{size=19}Макс, я и так знаю про ваши отношения.{/size}"
    show sayori cm
    mc "{size=19}А вдруг...{/size}"
    show emi neut cm oe
    show sayori happ cm oe
    mc "{size=19}Ох-х, хорошо.{/size}"
    mc "{size=19}Но если Моника тебе запретит, то тебе придётся подождать, когда мы закончим, ясно?{/size}"
    show sayori ce
    s "{size=19}М-м, м-м!{/size}"
    hide sayori
    show sayori turned happ cm ce at i33
    with dissolve
    pause 0.25
    show emi happ cm oe
    show kamuko pani cm oe
    show sayori om
    s "Я тоже пойду, ребята!"
    show kamuko om
    show sayori cm
    kam "Да куда вы?"
    show emi laug om ce
    show kamuko cm
    e "Явно ещё не все готовы к твоим рассказам, Камуко."
    show emi cm
    show kamuko om ce ldown rdown at h32
    show sayori oe
    kam "Но мы только собрались!"
    show emi happ cm oe
    show kamuko cm
    show sayori om
    s "Камуко."
    show kamuko curi cm e1a lhiphid rhid
    show sayori cm at t54
    kam "???"
    show emi neut cm oe
    show kamuko neut cm oe
    show sayori om
    s "Ты же хотела к нам в клуб?"
    show emi curi cm oe
    show kamuko om
    show sayori cm
    kam "Да."
    show emi om
    show kamuko cm
    e "Да?"
    show emi cm
    show sayori om ce
    s "Поэтому ещё успеешь рассказать нам много нового и интересного!"
    show emi neut cm oe
    show kamuko happ cm oe
    show sayori neut om oe b1d
    s "Но пообещай, что вступишь к нам."
    show emi happ cm oe
    show kamuko om ce ldown rdown
    show sayori cm
    kam "Ага, клянусь-клянусь!"
    show emi turned happ om ce lhip rhip
    show kamuko cm
    show sayori -b1d
    e "Какого-то там президента упрекали за переманивание людей, хм-хм-хм..."
    show emi cm
    show kamuko oe
    show sayori happ cm oe
    mc "Ничего, мы можем заслуженно себе позволить."
    show emi om
    show sayori at t33
    e "Ха-ха!"
    show emi cm
    show kamuko om
    kam "Да я всё равно в готовке никакая!"
    show emi oe
    show kamuko sad om e1c lhiphid rface
    show sayori neut cm oe
    kam "Вот только...{w}остальных жалко..."
    show emi cross happ om oe
    show kamuko neut cm oe
    e "Не, уж я как-нибудь выживу."
    show emi neut cm oe
    show kamuko om rhid
    show sayori b1f
    kam "А остальные \"остальные\"?"
    show kamuko cm
    show sayori -b1f
    mc "Всё, мы пошли."
    show emi angr md ee
    show kamuko happ cm oe
    show sayori happ om ce lup rup at h33
    s "Пока!"
    show kamuko om ce
    show sayori cm ldown rdown
    kam "Дзя нэ!"
    show kamuko cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 wind fadein 2.0
    scene bg school old_rooftop day
    show monika forward curi cm oe school_bag at t21
    show sayori turned happ cm oe at t22
    with wipeleft_scene
    show monika om
    m "А-а-а..."
    show monika happ om e1b b1b
    show sayori neut cm oe
    m "Я думала, ты будешь один."
    show monika cm
    mc "Это...{w}слишком долго объяснять."
    show monika neut cm oe -b1b
    show sayori om
    s "Если я мешаю, то могу уйти."
    show monika om lpoint
    show sayori cm
    m "Нет-нет, Сайори, можешь остаться."
    show monika happ om oe ldown
    show sayori happ cm oe
    m "Всё равно это не супер-секретная информация."
    show monika cm
    mc "Пока что именно так она и выглядит."
    show monika ce
    show sayori om ce lup rup at h22
    s "Мони, не томи!"
    show monika om
    show sayori cm ldown rdown
    m "А-ха-ха, хорошо."
    show monika oe lpoint rhip
    show sayori oe
    m "Слушайте внимательно."
    show monika ldown
    m "Мне буквально 10 минут назад позвонил папа и сказал, что он с мамой приедет ко мне завтра вечером на один день."
    show monika cm
    show sayori om ce
    s "Ух ты!"
    show monika neut cm oe
    show sayori curi mh oe
    s "Но...{w}твои родители и так каждый месяц навещают тебя..."
    show monika mh
    show sayori cm
    m "Да, Сайори, но дело не в этом."
    show monika happ om oe
    show sayori neut cm oe
    m "Макс, не хочешь с ними встретиться?"
    show monika cm
    mc "Э-э..."
    "Что-то как-то страшно за себя стало..."
    show monika neut cm oe
    mc "Не слишком ли быстро?"
    show monika rdown
    show sayori curi cm oe
    mc "Мы ещё не в таких отношениях, чтобы я с твоими родителями так сразу знакомился..."
    show sayori om
    s "Это как?!"
    show monika nerv cm oe n3
    show sayori e1a
    s "Вы же любите друг друга!"
    show sayori cm
    mc "Ну..."
    show monika mb ce
    show sayori neut cm oe
    m "...у нас пока пробуксовка в этой части из-за учёбы..."
    show monika cm
    "Блин."
    show sayori e2c
    "Уже практически целая неделя прошла, а всё, что я сделал с Моникой, -- помог ей опохмелиться после чаепития."
    "Мда-а-а, я всё ещё не готов к отношениям..."
    show monika oe
    show sayori vsur om oe lup rup at h22
    s "У вас ни разу не было свидания?!"
    show sayori cm ldown rdown
    mc "Сайори, какое свидание, я тебя умоляю..."
    show sayori neut om oe b1d
    s "Обыкновенное!"
    show monika mb
    show sayori cm -b1d
    m "У нас пока не так много времени..."
    show monika cm
    show sayori happ om ce
    s "О, знаю!"
    show monika neut cm oe n1
    show sayori oe
    s "Завтра утром я вытяну вас на пробежку!"
    show sayori ce
    s "А ещё можно будет захватить Юри, чтобы она из-за одиночества не начала ассоциировать себя с дынной булочкой!"
    show sayori cm
    "..."
    show monika happ cm oe
    mc "Сайори, тебя Камуко укусила?"
    show sayori om
    s "А ещё можно было бы сходить в какой-нибудь торговый центр!"
    show sayori neut om e2b
    s "Или в парк..."
    show sayori cm
    mc "Сайори, пожалуйста, успокойся, мы как-нибудь организуем эту часть сами."
    show monika om
    show sayori oe
    m "...но это интересные идеи..."
    show monika ce
    show sayori happ cm oe
    m "С утра пробежка, днём куда-нибудь сходим вместе, а ближе к вечеру вернусь домой."
    show monika oe rhip
    m "Только ты ещё не ответил на мой вопрос."
    show monika cm
    mc "...ох, ну это же даже не обсуждается."
    mc "Естественно, я встречусь с ними."
    show monika neut cm oe
    show sayori neut cm oe
    mc "Правда, немного боязно..."
    show monika om rdown
    m "Почему?"
    show monika cm
    mc "Твои родители очень богатые."
    mc "Ты тоже при деньгах."
    show monika happ cm oe b1b
    show sayori curi cm oe
    mc "И тут я, типичный дурачок, который из себя ничего не представляет."
    show monika om
    m "Ты слишком утрируешь, Макс."
    show monika cm
    show sayori happ om ce
    s "Я могу встретить их вместе с вами!"
    show monika -b1b
    show sayori oe
    s "Меня же они знают."
    show sayori cm
    mc "Вы уже знакомы?"
    show monika om ce
    show sayori e1b
    m "Да, было дело..."
    show monika oe
    show sayori oe
    m "Ладно, договорились!"
    show monika lpoint
    m "Завтра утром пробежка, днём поход всем клубом (по возможности) куда-нибудь отдохнуть, а вечером встретим моих родителей."
    show monika cm ldown
    mc "Да."
    show monika ce
    show sayori om ce lup rup at h22
    s "Ура!"
    show sayori cm ldown rdown
    "Минус суббота."
    "В хорошем смысле."
    show monika om oe
    show sayori oe
    m "Тогда пока на этом всё, вы свободны."
    show monika cm
    mc "Угу, но мы, наверное, тебе компанию составим."
    show sayori om
    s "Ага, нам всё равно делать нечего."
    show monika neut cm oe
    show sayori cm
    "Хотя было бы о чём поговорить..."
    show monika mh
    show sayori neut cm oe
    m "Уверены?"
    m "До урока осталось меньше 25 минут."
    show monika e1b b1f
    show sayori e2b
    m "Могли бы подготовиться, повторить записи..."
    show monika cm
    mc "Чёрт, Моника..."
    show monika happ cm oe -b1f
    mc "Ну зачем ты о плохом?"
    show sayori oe
    mc "Я вспомнил, что после перемены у меня должен быть английский, а там кучу новых слов навалили, которые я пару дней повторял."
    show monika om ce
    m "Хах, вот видишь, не зря сказала!"
    show monika cm
    show sayori om
    s "А у меня...{w}вроде всё прекрасно..."
    show monika om oe lpoint
    show sayori cm
    m "Лучше тоже сходи и проверь."
    show monika cm ldown
    show sayori worr om ce
    s "Эх..."
    show sayori cm
    mc "Ладно, я пойду."
    show sayori happ cm oe
    mc "До клубного собрания."
    show monika ce
    show sayori om
    s "До клубного собрания!"
    show monika om
    show sayori cm
    m "До встречи в клубе!"
    show monika cm
    show sayori ce
    stop noise_1 fadeout 5.0
    call window_close

    call window_dialog_long_transition

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    "..."
    mc "М-м-м..."
    "Учёба реально жрёт время."
    "А заодно и силы."
    mc "Свидания..."
    "Монике же ещё надо время уделять..."
    "Вот говорите что угодно, а я до сих пор...{w}не то, что бы боюсь...{w}стараюсь аккуратно их нивелировать."
    mc "Да что со мной такое..."
    "То сначала был охренеть как уверен в своём выборе, признался..."
    "...теперь вся уверенность улетучилась."
    "Эмоциональные, блин, качели..."
    call window_close

    call plot_transition

    call window_open
    scene bg corridor
    show sayori turned happ cm ce school_bag at t52
    with wipeleft_scene
    mc "Ха, первее всех первей?"
    show sayori om oe at t11
    s "А, ага!"
    show sayori cm
    mc "Ключи уже с собой?"
    show sayori om
    s "Да, сейчас открою."
    show sayori cm ce
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show sayori turned neut cm ce at t11
    with wipeleft_scene
    show sayori om
    s "Фу, душновато тут..."
    show sayori cm
    mc "Логично, что на таком солнце воздух спёрло."
    show sayori happ cm oe
    mc "Сейчас окна приоткрою."

    scene black with wipeleft_scene
    s "{size=19}Ой, точно, я же хотела тебе рассказать про мои похождения с Камуко!{/size}"
    mc "А-а-а, да..."
    "Так, открываем окно напротив двери..."
    s "{size=19}Это было невероятно весело!{/size}"
    mc "Угу..."
    mc "Фух..."
    "Отлично, пошёл лёгкий сквозняк."
    s "{size=19}Ты меня слушаешь?{/size}"
    mc "Да-да, Сайори, слушаю."
    s "{size=19}Так вот, мы...{/size}"
    s "{size=19}...мелки какие-то...{/size}"
    mc "А?"
    s "{size=19}Тут мелки лежат, сейчас положу их в кладовку.{/size}"
    s "{size=19}Так вот, мы сразу побежали--{/size}{nw}"
    mc "Сайори, давай ты сначала отнесёшь мелки, а потом договоришь."
    s "{size=19}Я не упаду, не переживай!{/size}"
    s "Так вот!"
    s "Мы побежали на третий этаж, там решили сначала забежать к тебе, потом мы увидели в дверях--{nw}"
    s "А-А-А-А-А!--{nw}" with vpunch
    play sound hit_wood
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 1.0
    s "У-у-у-у-у..."
    mc "Ну как знал же!"

    scene s_cg2_base1
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    with dissolve_cg
    s "Мой лобик..."
    mc "Как ты так умудрилась врезаться?"
    hide s_cg2_exp1
    hide s_cg2_exp3
    s "Споткнулась о шкафчики справа, ха-ха..."
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    s "Больно..."
    hide s_cg2_exp1
    show s_cg2_exp2 at cgfade
    mc "Подожди немного, сейчас сбегаю за чем-нибудь холодным."
    hide s_cg2_exp3
    hide s_cg2_exp2
    s "Х-хорошо!"
    mc "Только деньги надо захватить..."
    s "Тогда купи мне яблочный сок."
    s "Он очень холодный..."
    mc "Да?"
    mc "А по-моему, очень «яблочный»!"
    show s_cg2_exp3 at cgfade
    s "Ха-ха-ха!"
    show s_cg2_exp1 at cgfade
    s "Ай..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    if cg_a1_d12_s.unlocked == False:
        $ cg_a1_d12_s.unlock()
    scene s_cg2_base2
    show s_cg2_exp2 at cgfade
    show s_cg2_exp3 at cgfade
    with wiperight
    mc "Яблочный не нашёл, извини."
    mc "Был только апельсиновый."
    hide s_cg2_exp2
    show s_cg2_exp1 at cgfade
    s "Точно, он закончился..."
    hide s_cg2_exp1
    show s_cg2_exp2 at cgfade
    "Но, признаться честно, он реально холодный, а ещё габаритный и квадратный."
    "Самое то, чтобы прикладывать ко лбу."
    s "Ум-м..."
    hide s_cg2_exp2
    hide s_cg2_exp3
    s "100-процентное содержание апельсина..."
    mc "Было бы странно, если бы в апельсиновом соке не было бы 100 процентов апельсинов."
    s "Ха-ха!"
    show s_cg2_exp2 at cgfade
    show s_cg2_exp3 at cgfade
    s "Ох..."
    hide s_cg2_exp2
    hide s_cg2_exp3
    s "Опять я поторопилась и сбилась, э-хе-хе..."
    mc "Да, у тебя прямо энергия пёрла через край."
    s "Мне давно не было так весело с кем-то, кроме тебя и Литературного клуба..."
    mc "Я уже понял."
    mc "Но старайся контролировать своё состояние, ладно?"
    show s_cg2_exp1 at cgfade
    s "Но ты же сам говорил мне давать волю искренним эмоциям..."
    mc "Так-то да..."
    hide s_cg2_exp1
    show s_cg2_exp2 at cgfade
    mc "Но тут надо учитывать множество факторов."
    mc "Как например, твой случай."
    mc "Ты слишком увлеклась рассказом и поддалась эмоциям, в результате чего споткнулась и врезалась лбом о косяк."
    mc "А контроль поможет тебе избежать таких случаев."
    hide s_cg2_exp2
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    s "Как же всё сложно..."
    mc "Никто не говорил, что будет просто."
    hide s_cg2_exp3
    s "Я всего лишь хочу спокойно порадоваться..."
    mc "Понимаю, но...{w}весь мир от этого никуда не девается."
    s "Значит, мне никогда нельзя расслабляться?"
    mc "Не совсем."
    mc "Ты можешь расслабляться, но без фанатизма."
    s "Без фанатизма..."
    mc "Да."
    mc "Это и будет своего рода контролем эмоций."
    s "Я...{w}подумаю потом над этим..."
    mc "Конечно."
    "Ещё один кирпичик, вложенный в Сайори, отлично."
    hide s_cg2_exp1
    s "Но я тебе так и не рассказала про побегушки с Камуко, хе..."
    mc "Ты познакомилась со всем Клубом выпечки?"
    s "Да."
    s "Встретили Сору с Рэйко, потом Фукку."
    s "Ещё злого президента."
    s "И всё."
    show s_cg2_exp1 at cgfade
    mc "Она на тебя не наехала?"
    s "Нет."
    s "Всё хорошо."
    mc "Ну и отлично."
    mc "Если что, не заостряй на ней внимание, а то мало ли что там может ляпнуть..."
    s "Поняла."
    hide s_cg2_exp1
    show s_cg2_exp2 at cgfade
    mc "Ладно, хватит на полу сидеть."
    mc "Давай ты сядешь на стул, я проверю твой лоб."
    show s_cg2_exp3 at cgfade
    s "Уф..."
    mc "Хватайся за руку."
    call window_close

    call plot_transition

    call window_open
    scene bg school literature_club board day
    show sayori turned happ cm ce at t11
    with wipeleft_scene
    "К счастью, кроме маленького синяка, на лбу Сайори ничего больше не оказалось."
    "Обрадовавшись этому факту, она успела залпом высосать всю бутылку с соком, пока я убирал мелки в свободное место в кладовке."
    "Инвестировал деньги в Сайори, называется..."
    show sayori neut cm oe
    mc "Ты уж смотри, как бы тебя в туалет не приспичило."
    show sayori tap pout cm oe at s11
    s "Ну-у-у, слишком жарко!"
    show sayori turned happ om oe at t11
    s "Из меня быстрее всё выпариться, чем...{w}ну это..."
    show sayori cm
    mc "Давай не будем продолжать эту тему..."
    play sound closet_open
    pause 1.0
    y "{size=19}Привет всем...{/size}"
    show sayori om ce lup rup at h11
    s "Привет-привет!"
    show sayori cm ldown rdown
    hide sayori with easeoutright
    pause 0.5
    show natsuki turned fc pout cm oe at r11
    pause 0.5
    show natsuki om
    n "Макс."
    show natsuki cm
    mc "Э?"
    hide natsuki
    show natsuki turned fc neut cm e0b b1b at el11 zorder 2
    with dissolve
    pause 0.25
    show natsuki om
    n "НАЙДИ ПСИХОЛОГА.{w=1.0} НАЙДИ ПСИХОЛОГА.{w=1.0} НАЙДИ ПСИХОЛОГА."
    show natsuki cm
    mc "Что случилось?!"
    show natsuki om e0a
    n "Юри про папу рассказала..."
    show natsuki cm
    mc "О боги..."
    show yuri turned sad cm e1a at r55
    pause 0.5
    show yuri om
    y "Н-Нацуки, успокойся..."
    show yuri cm
    s "{size=19}Что-то с Нацуки?!{/size}"
    show yuri nerv om oe lup rup at h55
    y "НЕТ, с ней всё нормально!"
    show yuri cm
    hide yuri with easeoutright
    show natsuki shoc cm ce
    mc "Нацуки, соберись!" with vpunch
    show natsuki om:
        ease 0.5 xoffset 20
        ease 0.5 xoffset -20
        repeat
    n "{bt=5}А-а-А-а-А--{/bt}"
    mc "{size=19}Бессмыслено сейчас сопли распускать!{/size}"
    show natsuki pout cm oe at el11
    mc "{size=19}Слезами горю не поможешь!{/size}"
    show natsuki om
    n "{size=19}{cps=15}Н-но--{/cps}{/size}{nw}"
    show natsuki cm
    mc "{size=19}Но-но, но-но!...{/size}"
    mc "{size=19}Сейчас всё от меня зависит.{/size}"
    mc "{size=19}Общайся с Юри так же, как и раньше, только без всяких конфликтов и срачей, угу?{/size}"
    show natsuki neut cm oe
    mc "{size=19}И не говори никому про эту историю, чтобы слухи не поползли.{/size}"
    mc "{size=19}О ней знает только я и Моника, но Монике я сам сообщил.{/size}"
    n "{size=19}...{/size}"
    mc "{size=19}Вот, уже немного подуспокоилась, прекрасно.{/size}"
    mc "{size=19}А теперь соберись в единую кучку и готовься к обмену стихами.{/size}"
    show natsuki mg e1b
    n "{size=19}У-у...{/size}"
    hide natsuki
    show natsuki turned ff neut me e1b at i11
    with dissolve
    pause 0.25
    "Неужто она восприняла трагедию Юри так близко к сердцу?"
    show natsuki om
    n "...окей...{w}стих..."
    show natsuki curi om e1c
    n "Сайори, что там по стиху?..."
    show natsuki cm at t21
    show sayori turned neut cm oe at r22
    pause 0.5
    show sayori om
    s "Что-то ты бледная..."
    show natsuki pout cm oe
    show sayori happ om oe
    s "Может, подкольчик тебе в бок сделать?"
    show natsuki om ce
    show sayori cm
    n "В порядке!"
    show natsuki curi om oe lhip rhip
    show sayori neut cm oe
    n "Что там по стиху?"
    show natsuki cm
    show sayori om
    s "По стиху?"
    show natsuki at thide
    hide natsuki
    show sayori e2b at thide
    hide sayori
    s "{size=19}Ну, я могу его сейчас достать...{/size}"
    mc "Фух..."
    show yuri turned sad cm oe at e22 with easeinright
    show yuri mi
    y "Я ей тоже поведала про отца..."
    show yuri cm
    mc "Да, она только что мне про это сказала."
    show yuri neut cm e1d
    mc "Я так понимаю, ты её просветила на большой перемене?"
    show yuri om
    y "Да."
    show yuri cm
    mc "Нацуки прям обмякла..."
    show yuri sad mi oe
    y "Ей немного поплохело после моих слов."
    show yuri ce
    y "Мне было в этот раз легче говорить, но...{w}непонятно, что на душе творится...{w}а тут ещё и Нацуки неважно стало..."
    show yuri cm
    mc "Ага, у меня аналогичное паршивое ощущение..."
    show yuri e1a
    mc "Сейчас я кое-как привёл её в порядок, надеюсь, она прошла «пик» переживаний."
    show yuri neut om e1d
    y "Не волнуйся, это уже отголоски..."
    show yuri cm e1d
    mc "Меня, кстати, только один вопрос терзает."
    show yuri om
    y "Какой?"
    show yuri cm
    mc "Ты же с Нацуки со средней школы дружишь -- уже столько времени провела..."
    show yuri curi md oe
    mc "...а почему про твой «скелет в шкафу» она узнала только сейчас?"
    show yuri om e1c
    y "Э-э..."
    show yuri oe
    y "...н-наверное, я не видела в этом смысла..."
    show yuri neut cm e1d
    mc "А у меня он, типо, есть?"
    show yuri om
    y "Может, это прозвучит странно и резко, но к тебе у меня доверия больше..."
    y "Я ощущаю тебя не так, как её."
    y "Будто ты что-то можешь изменить, наверное, а не просто посочувствовать..."
    show yuri cm
    mc "Хм..."
    show yuri happ cm oe
    m "{size=19}Всем привет!{/size}"
    k "{size=19}Приветик.{/size}"
    s "{size=19}Ура, все в сборе!{/size}"
    m "{size=19}Не будем задерживаться, начнём сразу?{/size}"
    show yuri om
    y "Думаю, да."
    show yuri cm
    s "{size=19}Конечно, не терпится увидеть хорошие стихотворения!{/size}"
    hide yuri
    show yuri turned happ cm oe at i11
    with dissolve
    pause 0.25
    show sayori turned happ cm oe at t51
    show yuri at t52
    show monika forward happ cm oe at t53 zorder 2
    show natsuki turned neut cm oe at t54
    show kotonoha happ cm oe at t55 zorder 2
    pause 0.2
    play music t5 fadein 3.0
    show monika om lpoint rhip
    m "Итак, друзья!"
    show yuri ce
    show monika ce ldown
    show natsuki happ cm oe
    show kotonoha rhip
    m "Начинаем последнее собрание на этой неделе, а также по совместным стихотворениям."
    show yuri oe
    show monika oe
    m "Надеюсь, мы закроем их достойно, поэтому я на вас всех очень рассчитываю."
    show monika b1f
    m "У вас же всё получилось?"
    show monika cm
    mc "Поверь, более чем."
    show sayori om ce lup rup at h51
    show monika -b1f
    s "Да!"
    show sayori oe ldown rdown
    show yuri ce
    show kotonoha ce
    s "Давайте быстрее читать!"
    show sayori cm
    show monika om ce rdown
    m "Ух ты, давно у нас такого настроя не было!"
    show yuri oe
    show monika oe lpoint
    show kotonoha oe
    m "Тогда какая пара выступит первой?"
    show yuri om
    show monika cm ldown
    show natsuki neut cm oe
    y "М-может, наша?"
    show yuri cm
    "Юри захотела выступить первой на публику?"
    mc "...я не против."
    show yuri ce
    show monika om
    m "Давайте!"
    show yuri at thide
    hide yuri
    show monika cm
    pause 0.2
    mc "Вот, держите."
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show sayori at t22 zorder 2
    show monika om ce zorder 3
    show natsuki e1c at t21 zorder 2
    show kotonoha rdown at t43
    m "Приступим!"
    show sayori e1b
    show monika cm e1b
    call window_close

    pause 2.0
    show sayori neut cm e1b
    pause 2.0
    show natsuki b1f
    show kotonoha neut cm oe
    pause 2.0
    show sayori happ cm e1b
    pause 2.0
    show natsuki -b1f
    pause 1.0
    show kotonoha happ cm oe
    pause 3.0

    call window_open
    show monika om ce
    m "Отлично!"
    show monika cm
    show natsuki happ cm e1c
    show kotonoha om rhip
    k "Да, качественное стихотворение."
    show sayori om ce
    show monika e1b
    show kotonoha cm
    s "Согласна!"
    show sayori cm
    show natsuki mb
    n "Ага."
    show sayori oe
    show monika om oe
    show natsuki cm
    m "Юри, вы пробовали звукопись?"
    show monika cm
    show natsuki neut cm oe
    y "Верно."
    show sayori neut cm oe
    y "Мы решили привнести в стих что-то новое, то есть что-то, что больше погрузит читателя в атмосферу."
    show sayori om e1b
    show monika e1b
    show natsuki e1c
    s "А-а-а, да, вот тут вторая часть похожа на тарабанящие капли..."
    show sayori cm
    mc "Правильно."
    show monika om
    m "Интересно вышло..."
    show monika oe
    show kotonoha neut cm oe
    m "Надо будет в будущем попробовать нечто похожее."
    show sayori oe
    show monika neut cm oe
    show natsuki oe
    show kotonoha om
    k "Никто из вас ещё не пытался использовать данный приём?"
    show monika curi om e1c
    show kotonoha cm
    m "Нет, вроде бы..."
    show monika md
    show natsuki om lhip rhip
    n "Я точно нет: даже не думаю над этим."
    show natsuki e1b
    n "Тут только Юри...{w}со всей душой подходит к такому..."
    show sayori happ cm oe
    show monika happ om oe
    show natsuki cm oe
    show kotonoha happ cm oe
    m "В общем, стих очень хороший, ваше «парное» сочетание дало прекрасные плоды."
    show monika cm
    show natsuki happ cm oe ldown rdown
    show kotonoha ce
    y "Спасибо!"
    mc "Благодарю."
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    show sayori curi cm oe at t54
    show monika lean happ om oe at h53
    show natsuki neut cm oe at t52
    show kotonoha oe rdown at t55
    m "Что ж, не хочу показаться высокомерным человеком, но в своей с Котонохой работе я твёрдо уверена."
    show sayori neut cm oe
    show monika forward happ om oe lpoint rhip
    show natsuki curi cm oe
    m "Посему предлагаю выступить паре Сайори и Нацуки."
    show sayori happ om ce
    show monika cm ldown
    s "Да-да-да, давайте!"
    show sayori cm
    show natsuki om
    n "Так сразу?"
    show natsuki happ mb e4a lhip rhip
    n "...ладно."
    show kotonoha at thide
    hide kotonoha
    show monika ce rdown at thide
    hide monika
    show natsuki cm
    pause 0.2
    show natsuki oe at t21
    show sayori oe at t22
    pause 0.2
    show natsuki om
    n "В этот раз я тоже...{w}уверена в своей работе."
    show natsuki cm
    show sayori om
    s "Без лишних слов!"
    show natsuki ldown rdown
    show sayori cm
    pause 0.1
    play sound paper_torn_out
    show sayori lup poem_paper with dissolve
    pause 1.0
    show sayori om ce
    s "Макс, держи!"
    show sayori cm
    pause 0.1
    play sound paper_torn_out
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    mc "Так..."
    show sayori oe
    mc "Кхм-кхм."
    $ currentpos = get_pos(channel="music")
    stop music fadeout 3.0
    call show_poem(poem_ns)
    mc "Нифига себе..."
    y "Это...{w}это очень достойное стихотворение."
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    play music t5c fadein 3.0
    m "Потрясающе!"
    m "Именно такие парные стихи нам и нужны!"
    k "Ох..."
    show sayori om ce lup rup at h22
    s "Е-е-е, спасибо за похвалу!"
    show natsuki om ce lhip rhip
    show sayori cm ldown rdown
    n "Не зря старались."
    show natsuki cm oe
    show sayori oe
    m "Теперь мы точно знаем, что Нацуки лучше всего писать с Сайори."
    mc "Довольно очевидно."
    show natsuki ldown rdown
    mc "...но всё равно очень классно вышло."
    show natsuki nerv cm e1b
    show sayori nerv cm oe
    mc "Даже момент с «гитарой», кхмпф."
    show sayori tap nerv om ce at s22
    s "Я очень погрузилась в роль, хе-хе..."
    show natsuki happ cm oe
    show sayori turned happ cm oe at t22
    y "Мне понравилось, что сначала ваши точки зрения конфликтовали, а потом вы нашли общий язык."
    y "Это добавило в стих некую динамику..."
    y "Иными словами, вы смогли сохранить глубину своих стихотворений при объединении."
    show natsuki neut cm oe
    show sayori neut cm oe
    y "Единственное, к чему бы я немножко придралась, -- рифмовка в некоторых частях..."
    show natsuki happ cm oe
    show sayori happ cm oe
    y "...но это будет уже глупо с моей стороны, так как она стала в разы лучше."
    show sayori ce
    y "Нацуки, Сайори -- это одна из лучших ваших работ."
    show sayori oe
    y "Надеюсь, вы получили от неё опыт взаимодействия в команде и более улучшенной рифмовки, который поможет модернизировать ваши стили."
    show sayori om
    s "Несомненно!"
    show natsuki mb
    show sayori cm
    n "Агась."
    show natsuki cm
    "Вот это я понимаю -- нашли «своё» место."
    "А ещё Юри прилюдно похвалила Нацуки..."
    "Всё-таки она с ней поменялась в лучшую сторону."
    play sound paper_torn_out
    pause 1.0
    show natsuki ce
    show sayori ce
    m "Очень, очень и очень хорошо!"
    show natsuki oe
    show sayori oe
    m "Могу уже сказать, что это собрание -- тот самый эталон, который и должен был быть изначально."
    mc "Какие пафосные слова..."
    m "Не без этого, хах!"
    m "Но мы ещё не закончили: осталась моя пара с Котонохой."
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    pause 0.2
    show monika forward happ cm oe at t21
    show kotonoha happ cm oe at t22
    pause 0.2
    stop music fadeout 3.0
    show monika ce n2
    show kotonoha nerv om oe rhip
    k "Мы там...{w}многовато настрочили..."
    show monika om
    show kotonoha cm
    m "Да, у нас вышло непривычно много, поэтому не пугайтесь двух исписанных листов."
    show monika cm
    show kotonoha ce
    s "Два листа?!"
    show monika oe n1
    y "Что же там такое..."
    show monika lean happ om oe at h21
    show kotonoha happ cm oe
    m "А вот это вы сейчас и прочитаете!"
    show monika forward happ cm oe
    pause 0.1
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show monika om ce
    m "Макс, держи!"
    show monika cm
    pause 0.1
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    "...я уже был в курсе объёма стиха, но, блин...{w}даже у меня глаза на «лоб» полезли..."
    show monika oe
    mc "Кхм."
    call show_poem(poem_km)
    mc "..."
    show monika neut cm oe
    show kotonoha neut cm oe
    nsy "..."
    show monika om b1f
    show kotonoha rdown
    m "Ребята?..."
    show monika cm
    call window_close

    play sound applause_small
    pause 1.0
    show monika -b1f
    pause 1.0
    show monika happ cm oe b1b n3
    show kotonoha nerv cm oe n3
    pause 2.0
    show monika ce
    pause 2.0

    call window_open
    show monika oe
    show kotonoha ce
    n "Это.{w} Просто.{w} Бомба!"
    show monika n1 -b1b
    show kotonoha happ cm oe n1
    s "Это же сколько вы времени потратили?!"
    show kotonoha om
    k "Мы не засекали."
    show monika om lpoint
    show kotonoha cm
    m "Полтора часа точно...{w}возможно, даже больше двух."
    show monika cm ldown
    mc "Вот это точно та планка, которую никто из нас не перепрыгнет."
    show monika om
    m "...но это если не объединяться."
    show monika b1f
    m "Кто знает, что будет в будущем?"
    show monika cm -b1f
    y "...хотелось бы отметить нестандартную подачу «сюжета»."
    y "Повторяющиеся части довольно интересно контрастируют друг с другом, дополняя основную часть."
    show monika neut cm oe
    show kotonoha neut cm oe
    y "Но меня слегка обескуражили...{w}э-э-э...{w}«резкие» переходы между частями?"
    y "Что я хочу сказать: для данного стихотворения необходим определённый темп чтения."
    y "Даже некая напевность."
    show monika happ cm oe
    y "В этом кроется главный плюс и минус."
    show monika om rhip
    show kotonoha happ cm oe
    m "Соглашусь, у нас в голове есть своё «представление», как должен читаться этот стих."
    show monika cm
    y "Я бы отнесла это больше к специфической особенности, нежели к недоработке."
    show monika ce
    y "В любом случае работа проведена колоссальная -- отличное завершение парных стихотворений."
    show monika oe
    y "А ещё хотелось бы отметить работу Котонохи, потому что это только её второе стихотворение, а она уже смогла скооперироваться с Моникой."
    show kotonoha ce
    s "Точно, молодец!"
    show kotonoha om
    k "Спасибо!"
    play sound paper_torn_out
    show kotonoha cm
    pause 1.0
    show sayori turned happ cm oe at t51 zorder 2
    show natsuki turned happ cm oe at t52
    show monika rdown at t53 zorder 3
    show kotonoha rdown at t54 zorder 2
    show yuri turned happ cm oe at t55
    pause 0.2
    play music t8 fadein 3.0
    show monika om b1b
    m "Ну что ж, друзья..."
    show sayori b1b
    show monika ce
    show yuri e1a b2b
    m "Парные стихи подошли к концу."
    show monika lean happ om oe at h53
    m "Никто не остался недовольным?"
    show monika cm
    mc "На такой ноте?"
    show monika forward happ cm oe
    mc "Не думаю."
    show natsuki om e4a lhip rhip
    show kotonoha ce
    n "Наконец-то их победили..."
    show natsuki cm
    show yuri om e1b
    y "Жаль, что мы, вероятнее всего, не будем больше этим заниматься..."
    show natsuki oe ldown rdown
    show monika ce
    show kotonoha oe
    show yuri om ce -b2b
    y "...но я всё равно рада, что у нас всё получилось."
    show sayori om e4a
    show yuri cm
    s "Эх, да..."
    show sayori cm
    show natsuki neut cm oe
    show monika om oe
    show kotonoha neut cm oe
    show yuri oe
    m "Тогда знаете что?"
    show sayori oe -b1b
    show monika lpoint
    show kotonoha happ cm oe
    show yuri neut cm e1d
    m "Сегодня Сайори подкинула мне идейку сходить завтра всем клубом куда-нибудь отдохнуть."
    show natsuki curi cm oe
    show monika ldown
    show kotonoha rhip
    m "Что думаете?"
    show monika neut om oe
    m "Только если не можете, говорите сразу."
    show monika cm
    show kotonoha om
    k "А куда именно сходить?"
    show monika e1c
    show kotonoha cm
    m "М-м-м..."
    show sayori om
    show natsuki neut cm oe
    show monika oe
    show yuri happ cm oe
    s "Ближе к центру города есть большой торговый центр."
    show sayori e1b
    show monika happ cm oe
    s "Мы можем сходить туда..."
    show sayori neut cm oe
    show monika neut cm oe
    show kotonoha neut cm oe
    show yuri neut cm e1d
    mc "Влетит по кошельку."
    show natsuki anno cm oe
    mc "Да и это прям на целый день, под конец убитыми будем."
    show sayori happ cm oe
    show monika happ cm oe
    show kotonoha happ cm oe
    show yuri om
    y "Но я бы всё равно сходила."
    show natsuki om lhip rhip
    show yuri happ cm oe
    n "А я бы хотела поесть что-нибудь нормальное!"
    show natsuki ce
    n "Заодно папу не грузить."
    show natsuki cm
    show monika om ce rhip
    show kotonoha ce
    show yuri ce
    m "Хорошо, завтра пойдём в торговый центр и найдём там хороший ресторанчик!"
    show sayori neut cm oe
    show natsuki neut cm oe
    show monika neut cm oe
    show kotonoha neut cm oe
    show yuri neut cm oe
    mc "А платить как будем?"
    show natsuki laug om ce
    show yuri angr cm oe
    n "Моникой, хи-хи-хи!"
    show natsuki cm
    show yuri om
    y "Нацуки!"
    show natsuki ma
    show monika happ cm oe
    show kotonoha om
    show yuri cm
    k "Я могу за себя."
    show natsuki happ cm oe
    show kotonoha cm
    show yuri neut cm e1d
    mc "И я."
    show sayori happ cm oe
    mc "...ну и за Сайори."
    show sayori om ce
    s "Э-хе-хе!"
    show sayori cm
    show natsuki neut cm oe
    show yuri worr cm oe
    y "Умф..."
    show sayori oe
    show natsuki happ cm oe
    show monika om lpoint
    show kotonoha happ cm oe
    show yuri neut cm e1d
    m "Возьму на себя Нацуки и Юри."
    show monika b1f ldown
    show yuri happ cm oe
    m "Мы же всё равно много есть не будем, верно?"
    show monika cm
    show kotonoha e1c
    show yuri neut cm e1d
    mc "Надеюсь..."
    show sayori neut cm oe
    show natsuki curi cm oe ldown rdown
    show monika neut cm oe -b1f
    show kotonoha neut cm oe
    show yuri om
    y "Но мы ограничимся одним рестораном?"
    show natsuki e1b
    show monika e1b
    show yuri cm
    m "М-м-м..."
    show natsuki om
    show monika oe
    show kotonoha happ cm oe
    n "Торговые автоматы."
    show natsuki cm
    show kotonoha om
    k "Кинотеатр."
    show sayori om
    show kotonoha cm
    s "Парк."
    show sayori cm
    show natsuki oe
    mc "..."
    mc "...что?"
    show sayori happ cm oe
    show monika happ cm oe
    show kotonoha ce
    show yuri happ cm oe
    mc "Вы уже сами всё сказали."
    show sayori neut cm oe
    show natsuki neut cm oe
    show monika om lpoint rdown
    show kotonoha oe
    m "Давайте поступим следующим образом."
    show sayori happ cm oe
    show monika ldown
    m "Я сегодня создам общий чат для Литературного клуба, где мы вечером или завтра утром на холодную голову всё обсудим."
    show natsuki happ cm oe
    m "А заодно будем координироваться: когда вставать, где встречаться и так далее..."
    show monika cm
    mc "Дельная идея, а то мы так не договоримся."
    show monika om ce
    show yuri ce
    m "Вот и отлично!"
    show sayori ce
    show monika oe lpoint rhip
    show kotonoha rdown
    show yuri oe
    m "Итак, друзья!"
    show sayori oe
    show monika ldown
    show kotonoha ce
    m "Парные стихи официально завершены, как и это клубное собрание."
    show monika ce
    show kotonoha oe
    m "Всем быть на связи в чате."
    show natsuki neut cm oe
    show monika oe lpoint
    m "А ещё не забываем про следующий вторник, то есть про новые стихи."
    m "Понедельником вас грузить не буду, потому что после парных стихов надо немного передохнуть."
    show monika ldown
    m "И, Котоноха, теперь ты тоже в этом полноценно участвуешь."
    show monika cm
    show kotonoha om e1c
    k "Да, понимаю."
    show sayori ce
    show natsuki happ cm oe
    show monika om ce
    show kotonoha cm ce
    show yuri ce
    m "Все свободны!"
    stop music fadeout 3.0
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show monika cm at thide
    hide monika
    show kotonoha at thide
    hide kotonoha
    show yuri at thide
    hide yuri
    pause 1.5
    "Успеем ли мы вернуться после «похода» и встретить родителей Моники?"
    "И вообще, по идее это первое свидание с Моникой."
    "Короче, как-то всё странно выходит."
    "...но всё-таки весело."
    show sayori turned happ cm oe school_bag at t11
    pause 0.2
    show sayori om
    s "Пошли домой?"
    show sayori cm
    mc "Моника задержится?"
    show sayori nerv mb oe
    s "Не, просто я уже за сегодня набегалась..."
    show sayori e2c
    s "А ещё шишка на лбу: хочу немного её охладить..."
    show sayori cm
    mc "Ну ладненько, пойдём."
    show sayori ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 10 afternoon
    show sayori turned happ cm e1b school_bag at t11
    with wipeleft_scene
    show sayori oe
    mc "Как-то быстро прошёл наш «лучший» обмен..."
    show sayori om ce
    s "Значит, он по-настоящему был «лучшим»!"
    show sayori cm
    mc "И не поспоришь..."
    show sayori oe
    mc "Ах, да."
    show sayori sedu cm oe
    mc "Ещё не перегорела желанием отоспаться у меня?"
    show sayori laug om ce
    s "Нет конечно!"
    show sayori ma
    mc "Только сначала обсуди всё с мамой."
    show sayori neut om oe
    s "Ей придётся рассказать про твои кошмары...{w}ну, про факт их существования."
    show sayori cm
    mc "Знаю."
    mc "Но я уже поднимал её на уши ночью в прошлую пятницу, поэтому...{w}основания поверить тебе будет."
    show sayori e1b
    s "Хм-м-м..."
    show sayori oe
    mc "В общем, отпишись по результату."
    show sayori happ cm oe
    s "Угу!"
    show sayori ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "..."
    mc "Да что ж с тобой делать..."
    "Психолог, как тебя найти?"
    "Это уже какая по счёту «вылазка» в Интернет?"
    "..."
    "Явно пятая."
    mc "Может, есть всё-таки какая-то деталь, а..."
    "Неужели у меня в голове не отложился его ник?"
    "Столько с ним общался, блин...{w}и толку?"
    mc "Ну почему в самые ответственные моменты вы все испаряетесь вникуда..."
    call window_close
    call skip_block_on

    play phone_sound new_message_mc
    pause 2.0

    $ quick_menu = True

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 50
        clock = (19, 30)

    phone register "mc_s_chat":
        time year 2018 day 27 month 4 hour 19 minute 30
        "s" "Отличные новости! Мама разрешила мне сегодня поспать у тебя! (> ω <)"

    phone discussion "mc_s_chat"
    $ plot_pause()
    phone discussion "mc_s_chat":
        "mc" "Прекрасно"
        "mc" "Но что-то долго вы там разбирались..."
        "s" "Ну я сначала решила всю домашку закрыть"
        "mc" "А, ясно"
        "s" "Я возьму с собой только пижаму и всё"
        "mc" "А остальное? Зубную щётку, пасту, прочее?"
    $ phone.system.clock = (19, 31)
    phone discussion "mc_s_chat":
        "s" "Это я всё дома сделаю"
        "s" "Я к тебе только под самую ночь приду!"
        "mc" "Это сколько по времени?"
        "s" "22:00"
        "mc" "Понял, жду, позвонишь в дверь"

    phone end discussion transition

    call skip_block_off
    window auto
    "Интересно, поможет ли мне это избавиться от кошмаров?"
    mc "Что-то я сомневаюсь..."
    "Слишком они всё-таки осмысленные."
    "А я ведь так их и не проанализировал."
    "Да и забыл часть деталей."
    "А ещё голова устала."
    mc "Ужас..."
    "Но в любом случае...{w}в этот раз я церемониться не буду."
    "Надо действовать решительно."
    mc "Если у меня в голове появляются кошмары, то почему я не могу стать кошмаром для своих же кошмаров?"
    "Клин клином вышибают."
    mc "Посмотрим, как вы запоёте, когда вам будут давать смачной сдачи..."
    "Что только не сделаешь ради спокойной и тихой жизни..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom
    show sayori turned pajamas happ cm oe at t11
    with wiperight
    mc "Итак, краткий инструктаж!"
    show sayori om b1d
    s "Внимательно слушаю!"
    show sayori cm
    mc "Первое: если ты встаёшь ночью, то ложись на левую половину кровати."
    show sayori neut cm oe -b1d
    mc "Второе: есть вероятность, что я начную дрыгаться."
    mc "В эти моменты я могу по тебе «случайно» заехать, поэтому не бойся давать мне «отпор», но в меру."
    show sayori happ cm oe
    mc "Третье: встаём пораньше, чтобы заняться твоей пробежкой, про которую ты только что мне говорила."
    mc "Если удастся, то вытянем на неё Монику или кого-нибудь ещё."
    mc "Четвёртое: никому не рассказываем про вот это вот всё."
    show sayori ce b1c
    mc "Блин, опять произвольная рифма..."
    show sayori oe -b1c
    mc "Э-э-э, на этом инструктаж окончен."
    mc "Вроде все аспекты затронул..."
    show sayori om ce
    s "Разрешите спать!"
    show sayori cm
    mc "Не разрешу, а потребую!"
    show sayori oe
    mc "Но сначала выключу свет и у стенки лягу."

    scene black with dissolve
    pause 1.0
    play sound light_turning_on
    pause 1.0
    mc "Так..."
    mc "..."
    mc "......"
    mc "Фу, отлично."
    mc "Залезай."
    s "Е-ех..."
    s "Ух..."
    s "Есть."
    mc "...ну..."
    mc "Спокойной ночи."
    s "Спокойной ночи!"
    window hide

    pause 5.0

    window auto
    s "...а твои кошмары...{w}реально страшные?"
    mc "Скорее, неожиданные и реалистичные."
    mc "Будто на тебя {color=#fc7e23}vr{/color}-шлем надели и при этом к твоему телу подключили датчики для передачи ощущений."
    s "Ох..."
    window hide

    pause 5.0

    window auto
    s "Может, тебя обнять?"
    mc "Ага, чтобы мы оба сварились под одеялом?"
    s "Но я же тут, чтобы у тебя кошмаров не было."
    mc "..."
    mc "...как хочешь."
    "..."
    "......"
    mc "Ладно, пока не так жарко."
    s "Я ещё не нагрелась."
    mc "Тогда предлагаю сразу уснуть, пока нет дискомфорта."
    s "М-м, м-м!"
    "..."
    "Да уж..."
    "Она мне реально как сестра..."
    call window_close

    $ nightmare_active = True

    call nightmare_act_1_day_12
    $ _history_list.clear()

    $ nightmare_active = False

    return
