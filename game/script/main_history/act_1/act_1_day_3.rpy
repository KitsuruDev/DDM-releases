transform movein_hugs_cookie:
    subpixel True
    yoffset 0 zoom 0.8 ypos 1.03
    parallel:
        linear 0.1 yoffset 20
        linear 0.1 yoffset 0
        repeat
    parallel:
        linear 0.4 zoom 1.4 ypos 1.65




label act_1_day_3:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d2.unlocked == False:
        $ ach_a1_d2.unlock()

    pause 7.0
    hide loading_sign_mc with dissolve
    pause 1.0

    play sound mc_alarm_clock
    show screen new_day(episode) with dissolve_scene_full
    pause 5.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    "{cps=20}...{/cps}"
    "{cps=20}Какой же я разбитый...{/cps}"
    "{cps=20}Вообще ничего не хочу...{/cps}"
    "{cps=20}Снова не выспался...{/cps}"
    "{cps=20}Хочу ещё спать...{/cps}"
    "Уберите от меня эту школу с её противным графиком и обществом."
    mc "Нет, не хочу смахивать одеяло."
    mc "Уберите, уберите эту всю хрень от меня!"
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "Всё на месте?"
    "..."
    "Всё на месте."
    "..."
    "А точно?"
    "..."
    "Да!"
    "Пошёл, давай, хватить тупить!"
    "Не хватало ещё в себя уйти..."
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
    mc "Ух, прохладно..."
    "В Ниигате по утрам в апреле это норма."
    "Но обычно в такое время должно быть теплее, что опять с погодой случилось?"
    "..."
    mc "Подождите-ка..."
    window hide

    $ phone.calendar.current_day = (18, _("СР"))

    python in phone.system:
        battery_level = 53
        clock = (5, 48)

    show screen phone() with Dissolve(0.5)
    $ plot_pause()

    window auto
    "Я вышел...{w}на час раньше?..."
    window hide

    hide screen phone with Dissolve(0.5)

    window auto
    "Каким образом?"
    "У меня так вчера глаза замылились, что я перепутал цифры при настройке будильника?"
    "..."
    mc "Класс."
    "Это фиаско, братан."
    "Ну раз так, то можно где-нибудь с Сайори прогуляться."
    "Вроде бы она как раз вчера этого и хотела."
    "Надо её найти."
    "А вот где?"
    "Дома?"
    "На пробежке?"
    "Аргх, как я не люблю такие моменты!"
    "Непонятно где, непонятно сколько ждать..."
    "Причём надо учитывать, что Сайори -- сама неожиданность."
    "Возможно, она волшебным образом сейчас выйдет из калитки своего дома."
    "Кто ж её знает?"

    scene bg house with wipeleft_scene
    "Выбора у меня нет, подожду здесь."
    "А если даже Сайори не появится, то сам пойду прогуляюсь."
    call window_close

    pause 6.0

    show sayori turned neut cm e1b school_bag at t11
    pause 0.25
    show sayori s_scream at h11
    call window_open
    s "А-А-А-А-А-А-А-А-А--{nw}" with vpunch
    show sayori curi om e2d -s_scream
    s "Макс?!"
    show sayori cm
    mc "Здрасьте."
    show sayori om oe
    s "Ты точно здоров?"
    show sayori cm oe
    mc "После твоего внезапного крика у меня на этот счёт появились сомнения..."
    show sayori neut om oe
    s "Чтобы ты в такую рань вышел, да ещё встретил меня..."
    show sayori laug om oe
    s "Ты меня пугаешь вдвойне!"
    show sayori cm oe ldown rdown
    mc "Сам в шоке."
    play music sayori_bliss fadein 3.0
    show sayori happ cm oe
    mc "Раз такое дело, то, может, прогуляемся?"
    show sayori happ mc e4c lup rup at h11
    s "Конечно да!"
    show sayori mn

    scene bg niigata street suburban 11 day
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om oe
    s "А почему ты так рано встал?"
    show sayori laug cm oe
    mc "Будешь смеяться, но я время на будильнике перепутал: поставил его на час раньше."
    show sayori om oe
    s "Серьёзно?"
    show sayori cm oe
    mc "Абсолютно."
    show sayori om ce
    s "Я думала, что только я такая невнимательная!"
    show sayori cm ce
    mc "Видишь, у тебя появилась конкуренция в этом деле."
    show sayori om ce
    s "Уж лучше бы её не было, ха-ха-ха!"
    show sayori cm ce
    mc "Мдэ..."
    show sayori cm oe

    scene bg niigata street suburban 12 day
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om ce lup rup at h11
    s "Площадка!"
    show sayori cm ce
    mc "Не поздновато ли ты захотела на ней поиграть?"
    show sayori tap pout cm oe school_bag at s11
    s "Ну, подумаешь, мне через пару месяцев 18..."
    show sayori turned happ cm ce school_bag at t11
    pause 0.1
    show sayori om lup rup at h11
    s "Мы все внутри дети!"
    show sayori cm ce ldown rdown
    "Да если бы..."

    scene bg niigata street suburban 13 day
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori cm oe
    mc "Один вопрос."
    show sayori neut cm oe
    mc "А куда мы вообще идём?"
    show sayori curi om e2b
    s "Э-э-э..."
    show sayori neut om oe
    s "Я за тобой шла."
    show sayori cm oe
    mc "А я за тобой."
    mc "И куда нас это привело?"
    mc "Снова на незнакомую улицу."
    show sayori happ om oe
    s "Почему же?"
    show sayori om ce
    s "Мы рядом с другим районом, там есть хороший парк!"
    show sayori cm oe
    mc "Это сколько мы уже прошли?"
    show sayori om ce lup rup at h11
    s "Пока недостаточное количество километров!"
    show sayori cm ce ldown rdown
    mc "Пф-ф-ф..."
    show sayori om oe
    s "Не помрёшь!"
    show sayori om ce
    s "Веселее шаг!"
    show sayori cm ce
    "Придётся сегодня все перемены отсиживаться..."

    scene bg niigata park small entrance 1
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori om ce
    s "А вот и он!"
    show sayori cm ce
    mc "Наконец-то..."
    show sayori neut om oe
    s "Ты уже замучился ходить?"
    show sayori cm oe
    mc "Немного, но я рассчитывал на меньшее расстояние."
    show sayori tap pout cm oe school_bag at s11
    s "Надо было с тобой каждый день с утра бегать, укрепил бы дыхание и ноги..."
    show sayori neut cm oe
    mc "А, нет-нет, прилив сил пришёл, всё в порядке!"
    show sayori turned laug om ce school_bag at t11
    s "А-ха-ха, вижу!"
    show sayori cm ce

    scene bg niigata park small path
    show sayori turned neut me ce school_bag at t11
    with wipeleft_scene
    mc "Фу-у-ух..."
    mc "Как хорошо в тени..."
    show sayori om ce
    s "Быстро припекло..."
    show sayori me ce
    mc "И не говори."
    show sayori dist om oe
    s "Что-то я сварилась в этой форме..."
    show sayori neut om oe
    s "Подержишь её у себя?"
    show sayori dist om oe
    s "У меня сумка маленькая..."
    show sayori neut cm oe
    mc "Да, давай."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg niigata park small path
    show sayori turned shirt nerv cm ce at i11
    with wiperight
    show sayori nerv om ce
    s "Фе-е-е, так-то лучше!"
    show sayori cm ce
    "Благо у меня место нашлось, а то тащить её пиджак в руках всю прогулку -- не комильфо."
    "Ещё взял её сумку и повесил на себя."
    "Эх, развалюсь я в школе на части..."
    show sayori happ cm oe
    "..."
    show sayori e1b
    "......"
    "Это, конечно, зашибись, что мы пришли, но...{w}стоять и неловко молчать на финише после такого пути довольно тупо."
    "Мы гулять пришли или что?"
    show sayori neut cm oe
    mc "Сайори, у меня тут к тебе важный вопрос появился..."
    show sayori curi cm oe
    s "М-м-м?"
    mc "Мы через год уже выпускаемся из школы."
    show sayori neut cm oe
    mc "Ты же ведь думала, куда дальше пойдёшь?"
    show sayori lsur om oe
    s "Э-э-э..."
    show sayori nerv om oe at s11
    s "...хе-хе..."
    show sayori cm oe
    "Я так и думал."
    show sayori neut cm oe at t11
    mc "Сайори, тебе придётся самой строить свою жизнь."
    show sayori dist om oe
    s "Я это понимаю..."
    s "Просто не знаю..."
    show sayori neut cm oe
    mc "Так давай обсудим."
    show sayori happ cm oe
    mc "Не зря же я твой лучший друг, а?"
    show sayori neut cm oe
    mc "Начнём с банальных вопросов."
    mc "Что ты любишь больше всего?"
    show sayori happ om ce lup rup at h11
    s "Печенье!"
    show sayori cm ce
    mc "...кроме печенья."
    show sayori neut cm oe ldown rdown
    mc "Хотя есть пекари..."
    show sayori om e2c
    s "Ну..."
    show sayori om oe
    s "Я часто утром варю себе и маме кофе."
    show sayori happ om ce
    s "Ей он очень нравится."
    show sayori cm ce
    mc "Кофе..."
    "Торговые центры, кафешки..."
    "...как же называлась эта профессия?..."
    "Думай, думай!"
    "О, ТОЧНО!"
    show sayori neut cm oe
    mc "Бариста?"
    show sayori curi om oe
    s "Бариста?"
    show sayori cm oe
    mc "А что?"
    show sayori neut cm oe
    mc "Это как бармен, только он вместо алкоголя подаёт кофе."
    mc "Зарплата вполне нормальная."
    mc "А если будет ещё хорошее заведение, то работа гарантированно превратится в любимое дело."
    show sayori om oe
    s "Разве это легко?"
    show sayori cm oe
    mc "Придётся постараться в любом случае, потому что надо знать множество сортов кофе..."
    show sayori e2c
    mc "...уметь их готовить, держа под контролем всё оборудование..."
    show sayori e2b
    mc "...при этом быть коммуникабельным, доброжелательным, гибким и уметь подстраиваться под ситуации."
    show sayori flus om oe at s11
    s "Ме-е-е..."
    show sayori neut cm oe at t11
    mc "Подумай, это неплохой вариант на самом деле."
    show sayori laug cm oe
    mc "Кто мне будет делать хороший кофе перед работой или после неё?"
    show sayori om oe
    s "Уже хочешь меня приватизировать?"
    show sayori cm oe
    mc "Ха, стану у вас постоянным клиентом."
    mc "Буду заказывать кофе с пенкой и какой-нибудь выпечкой."
    mc "С круассаном или пончиком."
    show sayori cm ce
    mc "Буду приходить и спрашивать: \"Где мой пончик, Сайори?\""
    show sayori om ce
    s "Ха-ха-ха!"
    show sayori happ om oe
    s "Хорошо, я подумаю и обсужу эту идею с мамой."
    show sayori neut cm oe
    mc "А я, наверное, дальше пойду учиться."
    show sayori om oe
    s "И куда конкретно?"
    show sayori cm oe
    mc "Парочку вариантов уже наметил."
    show sayori anno cm oe
    mc "Наверное, что-то в сфере {color=#fc7e23}IT{/color}."
    show sayori tap shirt pout cm oe at s11
    s "Опять твои компьютеры..."
    show sayori neut cm oe
    mc "Там не только компьтеры."
    show sayori turned shirt neut cm oe at t11
    mc "Там куча всего."
    show sayori angr om oe lup rup at h11
    s "Тебе придётся бегать по утрам всю жизнь!"
    show sayori cm oe ldown rdown
    mc "С чего это вдруг?"
    show sayori om ce
    s "У тебя тело размякнет с такого будущего, а его надо поддерживать."
    show sayori cm ce
    mc "Ох, Сайори..."
    show sayori anno cm oe
    mc "Да буду, буду я бегать, успокойся."
    show sayori om oe
    s "Ну-ну!"
    show sayori cm oe

    scene bg niigata park small entrance 2
    show sayori turned shirt nerv cm ce at t11
    with wipeleft_scene
    show sayori om ce
    s "Ладно, можно и обратно одеться."
    show sayori cm ce
    mc "Прохладно из-за ветра стало?"
    show sayori happ om ce
    s "Угусь!"
    show sayori cm ce
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg niigata park small entrance 2
    show sayori turned happ cm ce school_bag at i11
    with wiperight
    show sayori om ce
    s "Другое дело!"
    show sayori cm ce
    "Ох, точно, я ей стих не вернул..."
    show sayori cm oe
    mc "Кстати..."
    call window_close

    pause 1.0
    show sayori neut cm oe
    pause 1.0
    play sound paper_torn_out
    pause 1.0

    call window_open
    mc "А то ведь забуду."
    show sayori happ om oe
    s "А, сегодня же я увижу твой новый стих на основе моего."
    show sayori cm
    mc "Ага, только он так себе вышел..."
    show sayori om oe
    s "Уверена, ты преувеличиваешь."
    show sayori neut cm oe
    mc "С чего это вдруг?"
    show sayori vsur mi oe
    s "Ты же старался!"
    show sayori happ om oe
    s "А значит, он не мог выйти ужасным."
    show sayori cm oe
    mc "Хм..."
    "Он всё равно корявый."
    mc "Ладно, нам пора обратно идти, не хотелось бы опоздать."
    show sayori happ om ce lup rup at h11
    s "Ок-ке!"
    show sayori cm ce ldown rdown
    "И сдохнуть по пути..."
    call window_close
    stop noise_3 fadeout 3.0
    stop music fadeout 5.0

    call window_dialog_long_transition("n")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_natsuki day
    with dissolve_scene_full
    n "{bt=7}{cps=20}Ура-а-а-a-a...{/cps}{/bt}"
    "{bt=7}{cps=20}КоНеЦ уРоКоВ...{/cps}{/bt}"
    "{bt=7}{cps=20}КаК жЕ я ЗаМуЧиЛаСь...{/cps}{/bt}"
    n "Бр-р-р!" with vpunch
    "Фу, отпустило..."
    "Пора собирать свои вещи и идти за Юри."
    "..."
    "Мне показалось, или тот придурок опять хотел со мной заговорить?"
    "Мало ему было прошлого раза?"
    "Это хорошо, что глава школьного совета решила глаза закрыть на ту беготню, по словам Моники..."
    "Изрядно уже достала её своими выходками, самой неприятно."
    "Но что я могу сделать, если меня окружают такие вот дураки, которые творят дичь и провоцируют меня?!"
    n "Кх-х-х..."
    "..."
    "Надоело уже на всё это реагировать, честно..."
    call window_close

    call plot_transition

    call window_open
    scene bg school library
    show yuri turned neut cm e1b school_bag at t11
    with wipeleft_scene
    n "О, ты уже тут."
    show yuri e1d
    n "Привет."
    show yuri happ om oe
    y "Привет..."
    show yuri cm
    "Я так и думала, что Юри торчит именно в библиотеке."
    show yuri neut cm e1d
    n "И что ты тут ищешь?"
    show yuri om
    y "Что-то, что может меня заинтересовать."
    show yuri dist cm oe
    n "И как успехи?"
    show yuri om
    y "Никак..."
    show yuri cm
    "Потрясающий диалог!"
    "Не люблю Юри за её робость в общении."
    "Никого же нет, я тут одна, давно знакомы..."
    "В чём проблема?"
    "Или она просто не хочет сейчас со мной разговаривать?"
    "Вообще, в последнее время Юри словно не своя: всё реже общается со мной по мессенджеру..."
    if persistent.add_random_menu == 6:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()
    show yuri at t22
    show kotonoha sad cm oe at t21 with easeinleft
    pause 0.2
    show kotonoha om
    show yuri sad cm e1a
    k "Нет, здесь тоже нет ничего такого интересного..."
    show kotonoha happ om oe
    show yuri oe
    k "О, Нацуки!"
    show kotonoha ce lup rhid
    show yuri at thide
    hide yuri
    k "Привет!"
    show kotonoha cm ldown rdown
    n "Хай, Ко{image=accent_low_register}{space=-15}ха."
    show kotonoha om oe
    k "Снова сокращаешь моё имя?"
    show kotonoha cm
    n "Ага."
    "Ясно..."
    "Юри на пару с Котоно{image=accent_low_register}{space=-15}хой."
    show kotonoha e1b
    "Значит, с ней она тусуется, а на меня решила аккуратно забить?"
    "И что, что Котоноха более открытая, общительная и спокойная?"
    "И что, что она годится ей в старшие сёстры?"
    "Ну чем я хуже?"
    "Да-да, я ей завидую!"
    "Но Котоноха -- тоже моя подруга, хоть и реже с ней общаюсь..."
    show kotonoha neut cm oe
    y "И тут нет..."
    n "Блин, Юри, у нас как бы клуб по времени."
    n "Или ты тут до ночи планируешь застрять?"
    y "Ох, ладно..."
    show yuri turned worr om oe school_bag at t22
    y "Завтра сама поищу что-нибудь..."
    show kotonoha happ om ce
    show yuri neut cm e1d
    k "Точно, вы же обмениваетесь стихами, да?"
    show kotonoha cm
    n "Да."
    show kotonoha om
    k "Когда-то я пробовала себя в подобном, хе-хе-хе..."
    show kotonoha nerv omb oe
    k "Только потом перестала, когда увидела свои результаты."
    show kotonoha cm
    "Может, снова попробовать пригласить её в клуб?"
    n "Пф-ф-ф, давай к нам, поможем развить твой талант."
    show kotonoha neut om e1b
    k "М-м-м, не знаю, Нацуки, я ещё не задумывалась над вступлением в клубы..."
    show kotonoha cm oe
    n "А тебе и не надо!"
    show kotonoha happ cm oe
    n "Хороший вариант перед твоим носом."
    n "Всего 5 участников, двоих ты уже знаешь."
    show kotonoha ce
    n "Ламповая атмосфера, стихи, чаепития, э-э-э..."
    show yuri worr om ce
    y "Нацуки, не заставляй её..."
    show yuri cm
    n "Не вижу никаких минусов."
    "У меня гениальный план: если Коха вступит к нам, то мне будет проще общаться с Юри."
    "Или она окончательно на меня забьёт..."
    show kotonoha om oe
    show yuri neut cm e1d
    k "Ладно, я подумаю над твоим предложением."
    show kotonoha ce
    k "Но пока ничего не обещаю!"
    show kotonoha cm
    n "Ну-ну."
    show kotonoha oe
    n "Всё, пошли Юри, иначе мы так всех задержим!"
    show kotonoha neut cm oe
    show yuri shoc om oe lup rup at h22
    y "Ой, подожди!"
    show kotonoha happ cm oe
    show yuri at thide
    hide yuri
    y "Я хочу перепроверить свой стих!"
    n "Рофлишь?!"
    n "Почему просто не прийти в клуб и сделать всё там?"
    y "Там все увидят, а я не готова!"
    show kotonoha ce
    n "Пф-ф-ф-ф-ф-ф-ф-ф-ф..."
    n "Давай быстрее!"
    call window_close

    call window_dialog_fast_transition("mc")

    call window_open
    scene bg school new_class_mc day
    mc "Ух, ё-моё..."
    "Снова {s}противный{/s}, ой, простите, рутинный школьный день."
    "Как же меня это задолбало в некоторой степени."
    "Хотелось бы одному всё спокойно изучить, а не торчать в этом месте, сжигая всё свободное время..."
    "Но ничего не поделаешь, «официальное» посещение никто не отменял."
    "И клубы ещё..."
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Как успехи со стихом в этот раз?"
    show mrs_ida cm
    mc "Получше, думаю, хотя ещё недостаточно..."
    show mrs_ida om ce
    mi "Прекрасно, что у тебя получается!"
    show mrs_ida oe
    mi "А сам клуб тебе как?"
    show mrs_ida cm
    mc "...забавный и общительный."
    mc "Можно сказать, уже в нём освоился."
    show mrs_ida om
    mi "Хм, ты довольно быстро влился в общество, всего за пару дней, что очень хорошо."
    mi "Не каждому так удаётся."
    mi "Конечно, часть ответственности в этой сфере лежит на самом клубе, но основная остаётся за новеньким."
    mi "В общем, ты молодец."
    show mrs_ida ce
    mi "А всего лишь надо было сделать шаг, не правда ли?"
    show mrs_ida cm
    mc "Угу..."
    "Но перед этим стать «желаемым» объектом клуба, который засосёт тебя в пучину внеклассной деятельности."
    "А не будь этого, то было бы всем плевать по большей части..."
    show mrs_ida oe
    mc "Ой, мне пора идти, Ида-сэнсэй."
    show mrs_ida om
    mi "Ладно, удачи!"
    show mrs_ida ce lup
    mi "Она тебе понадобится с четырьмя девушками~"
    show mrs_ida cm

    scene black with wipeleft_scene
    "Да когда ж миссис Ида успокоится на этой теме?!"
    "Когда у меня будет жена, дети и собственное жильё с имуществом?"
    "Cудя по всему."
    call window_close

    call window_dialog_fast_transition("m")

    call window_open
    scene bg school old_class_music at class_music_piano
    m "......"
    m "......"
    m "{sc=1}......{/sc}"
    pause 0.1
    with vpunch
    play sound monika_piano_angr
    pause 2.0
    m "......"
    "У меня.{w} Совершенно.{w} Нет.{w} Настроя."
    "Я просто не могу сосредоточиться."

    scene bg school old_class_music with dissolve
    "Что-то у меня Макс один в голове..."
    "Просто он так быстро втянулся в наш клуб..."
    "Прошло всего два дня с момента его вступления, а я всё ещё не могу «смириться» с тем, что он никогда не проводил время с нами, ха-ха-ха..."
    "..."
    "А ведь наш состав мог быть больше, чем сейчас..."
    "Я запросто могла в прошлом году забрать к себе Фу{image=accent_low_register}{space=-15}кку, но не сделала этого."
    "Мне не хватило уверенности..."
    "А теперь и Литературный клуб потерял потенциального участника, и здесь тишина, только я одна..."
    m "Какой же я хороший лидер..."
    m "Уф-ф-ф..."
    "Ладненько, Моника, успокойся..."
    "Не надо себя корить, потому что в этом нет никакого смысла."
    "Лучше я потрачу силы на заботу о тех, кто есть сейчас, иначе я всех потеряю."
    "Не хочу снова остаться одной...{w}никогда больше в своей жизни."
    "Потому что это ужасно."
    play sound monika_stomach_rumble
    pause 2.5
    m "Ох..."
    m "Кажется, кто-то проголодался, животик, ха-ха!"
    "Хорошо с собой печенье взяла."
    "А оно ещё наполовину покрыто шоколадом, м-м-м..."
    "Вот только надо уже возвращаться в клуб, время поджимает..."
    "Ой, ладно, там съем."
    call window_close

    call plot_transition

    call window_open
    scene bg club_day
    show monika forward neut cm oe at e11 zorder 2
    with wipeleft_scene
    "Печенья мало, мне одной еле-еле хватит..."
    "Никого же здесь нет?"
    show monika e1b
    pause 1.0
    show monika e1c
    pause 1.0
    show monika happ cm ce
    "Да, отлично."
    "Пора подкрепиться!"
    play sound package_open
    pause 2.0
    show monika neut cm e4c
    with vpunch
    pause 1.814
    show monika cm ce
    "Это было громко..."
    "Зато теперь можно приступить к--{nw}"
    show sayori turned yand cm oe school_bag at t41
    pause 0.2
    show sayori om
    s "{sc=3}ПЕЧЕНЬКА?!{/sc}"
    show sayori cm oe
    show monika eyes_shock
    m "{sc=3}...{/sc}"
    show sayori om oe
    s "{sc=3}ДАЙ МНЕ ЕЁ!!!{/sc}"
    play music natsuki_run
    $ quick_menu = False
    show sayori lup rup mc e4c at movein_hugs_cookie
    show monika shoc mp e4c
    m "{cps=70}{sc=3}А-А-А-А!!!{/sc}{/cps}{nw}"
    window hide
    play sound ram_attack
    scene white
    pause 0.1
    scene black
    show particle_star
    with dissolve

    call window_open
    s "{sc=3}ДАЙ!!!{/sc}"
    m "{sc=3}САЙОРИ, УСПОКОЙСЯ!!!{/sc}"
    s "{sc=3}МОЁ ПЕЧЕНЬЕ!!!{/sc}"
    m "{sc=3}С КАКОГО ПЕРЕПУГУ?!{/sc}"
    s "{sc=3}ОНО ЕЩЁ С ШОКОЛАДОМ!!!{/sc}"
    "{sc=3}НАДО СКОРЕЕ ЗАПИХНУТЬ ЕГО В РОТ!{/sc}"
    "{sc=3}Я ОЧЕНЬ ХОЧУ ЕСТЬ!!!{/sc}"
    s "АМ-М-М!!!"
    m "САЙО--М-М-М-М-М!!!"
    "{sc=3}ЧТО ТЫ ТВОРИШЬ?!{/sc}"
    "{sc=3}ХВАТИТ ВЫРЫВАТЬ МОЁ ПЕЧЕНЬЕ ЗУБАМИ!!!{/sc}"
    "{sc=3}ОТЛИПНИ ОТ МОИХ ГУБ!!!{/sc}"
    call window_close

    call window_dialog_fast_transition("mc")

    call window_open
    scene bg corridor
    "..."
    "Вот теперь моя нерешительность подкреплена шестым чувством, которое прямо кричит, что мне не стоит туда идти."
    "Неужели в клубе происходит что-то такое, что..."
    "Да кто ж вас знает, я уже ничему не удивлюсь."
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show sayori tap pout cm ce n3 school_bag zorder 2 at tcommon(750)
    show monika forward flus om e4c n3 at t11
    with wipeleft_scene
    pause 0.15
    show sayori turned lup rup s_scream school_bag at hop(750)
    show monika s_scream at h11
    stop music
    play music_none_loop music_stop
    with vpunch
    pause 0.2
    show sayori at t22
    pause 0.05
    show monika -s_scream shoc cm oe n4
    show sayori -s_scream vsur cm oe n4
    "..."
    "Беру свои слова назад..."
    mc "Ребят..."
    mc "Какого чёрта?"
    show monika om oe
    m "Я..."
    show monika cm oe
    show sayori om oe
    s "Мы..."
    show sayori cm oe
    mc "Я понял."
    show sayori tap neut cm oe n5 school_bag at s22
    mc "Вам просто здесь парней не хватает, а гормоны прыгают."
    show monika om oe
    m "Н-нет!"
    show monika cm oe
    mc "Всё, проехали, сделаю вид, что ничего не видел."
    mc "Лучше приведите себя в порядок, чтобы другие ничего не заподозрили."
    show monika mk e2b at s11
    m "Угх..."

    scene black with wipeleft_scene
    "Хороший клуб, и участники интересные."
    "Так, надо выяснить, когда мы начнём обмен стихами..."

    scene bg club_day
    show monika forward happ cm oe at t11
    with wipeleft_scene
    play music t3 fadein 3.0
    mc "Моника?"
    show monika om oe
    m "Да?..."
    show monika cm oe
    mc "Когда мы начнём наше мероприятие?"
    show monika om ce
    m "Как только, так сразу!"
    show monika om oe lpoint rhip
    m "Нацуки и Юри должны подойти с минуты на минуту."
    show monika cm oe ldown rdown
    mc "Понятно."
    show monika dist om oe
    m "И всё-таки..."
    show monika sad om oe n4 at s11
    m "...извини за тот случай..."
    show monika cm oe
    mc "Да ладно тебе, я понимаю."
    show monika lsur om oe at t11
    m "Неправильно понимаешь!"
    show monika flus om oe
    m "Это всё из-за печенья..."
    show monika cm oe
    mc "Подожди, ты подкупила Сайори?"
    show monika lsur om oe
    m "Мы печенье не поделили!"
    show monika cm oe
    mc "А-а-а..."
    show monika cm ce
    "Ну тут тогда молчу."
    show monika neut cm oe n1
    mc "Я удивлён, что ты ещё жива."
    show monika curi om oe
    m "В каком плане?"
    show monika neut cm oe
    mc "Сайори съела бы тебя целиком."
    show monika laug cm oe
    mc "Это хорошо, что я успел прийти."
    show monika om ce
    m "Ха-ха-ха, да!"
    show monika cm
    mc "{size=19}О, точно, по поводу Сайори...{/size}"
    show monika neut om oe
    m "{size=19}Во внимании.{/size}"
    show monika cm
    mc "{size=19}Новости хорошие: она вроде бы меня послушала.{/size}"
    show monika om
    m "{size=19}Ты её попросил быть собой?{/size}"
    show monika happ cm oe
    mc "{size=19}Грубо говоря, да.{/size}"
    show monika om ce
    m "{size=19}Очень хорошая новость!{/size}"
    show monika happ cm zorder 2
    show natsuki turned neut om oe lhip rhip school_bag at t44
    n "Хаюшки."
    show monika oe
    show natsuki cm oe
    show yuri turned happ om e1b school_bag at t41
    y "Привет..."
    show yuri cm
    show natsuki curi om oe ldown rdown school_bag
    n "Ага, вы все уже здесь?"
    show monika neut cm oe
    show natsuki cross anno om oe school_bag
    show yuri sad cm oe
    n "Говорила же, надо быстрее собираться!"
    show natsuki cm oe
    show yuri shy sad cm oe n5 school_bag at s41
    y "Ух-х-х..."
    show monika happ om oe
    show natsuki neut cm oe
    m "Юри, всё нормально, мы просто пораньше пришли!"
    show monika cm oe
    show yuri turned laug mg oe lup rup school_bag at t41
    y "Хотя бы так..."
    show monika neut cm oe
    show natsuki dist cm oe
    y "Я не хочу всех задерживать своим отсутствием..."
    show monika happ om ce
    show yuri me
    m "Не нагружайся, мы никого не торопим."
    show monika cm ce
    show yuri mg
    y "Угу..."
    show monika neut om ce
    show natsuki neut cm oe
    show yuri neut cm e1d
    m "Раз все здесь собрались, то..."
    show monika happ om oe lpoint rhip at t43
    show sayori turned happ cm oe at t42
    show natsuki turned school_bag
    show yuri happ cm oe ldown rdown
    m "Итак, друзья!"
    show monika om ce ldown rdown
    show yuri cm ce
    m "Время делиться стихотворениями!"
    stop music fadeout 3.0
    show monika cm
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    pause 0.3
    show monika om oe at t11
    m "Макс, на этот раз я хочу, чтобы ты начал с меня."
    show monika cm oe
    mc "Да, экспериментальный стих..."
    show monika om ce
    m "Верно!"
    play music t5 fadein 3.0
    show monika om oe
    m "Можешь уже доставать."
    show monika cm oe
    mc "Сейчас, минуту..."
    pause 2.0
    mc "Вот, держи."
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    mc "Суди только честно."
    call window_close

    show monika e1b
    pause 2.0
    show monika neut cm
    pause 4.0
    show monika e2b
    pause 4.0
    show monika happ om ce

    call window_open
    m "Хорошо написано, Макс!"
    show monika om oe
    m "Очень в духе Сайори."
    show monika e1b
    m "Мне нравится, как у тебя вышли второе и третье четверостишия в форме нисходящей лесенки."
    show monika cm
    mc "Хм, этого я вообще не заметил..."
    show monika om oe
    m "Видишь?"
    show monika om ce
    m "У тебя есть некие способности, не принижай их."
    show monika e1b
    m "Так вот, читать такие четверостишия очень удобно, особенно если соблюдён ритм."
    show monika neut om
    m "Но..."
    show monika sad mh
    m "Жаль, что первая часть совершенно не такая."
    show monika md oe
    mc "Да, начало всегда тяжело выходит."
    show monika mh
    m "Я понимаю."
    show monika happ om ce
    m "Но если бы оно было в такой же форме, то стихотворение получилось бы идеальным!"
    show monika cm ce
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    mc "Ну это громко сказано..."
    show monika lean neut om oe b2 at h11
    m "Совсем нет, Макс!"
    show monika happ om oe b1
    m "Мне оно понравилось."
    show monika cm oe
    mc "Рад слышать."
    show monika forward happ om oe lpoint rhip
    m "Теперь посмотрим, как у тебя обстоят дела с другими стилями."
    show monika om oe ldown rdown
    m "Кого выберешь дальше?"
    show monika cm oe
    mc "Э-э-э..."
    "Есть два стула."
    "Первый -- Нацуки."
    "Я уже говорил, как у неё слишком поверхностно и просто выходят стихи."
    show monika curi md oe
    "У меня смысл непроизвольно выходит поглубже."
    "Второй -- Юри."
    "Вот тут уже лучше, хотя меня пугают её замудренные слова и приёмы..."
    show monika dist cm oe
    "Такое тоже с трудом вывезу, стих должен быть этим «затоплен», причём в меру."
    "Чёрт, кого же выбрать..."
    show monika happ om ce
    m "Тяжело решиться?"
    show monika cm oe
    mc "Да, есть такое..."
    show monika om ce
    m "Хах, согласна, выбор достаточно трудный."
    show monika om oe lpoint
    m "Но на твоём месте я бы взяла Юри."
    show monika ldown
    m "У тебя получается использовать базовые писательские приёмы: олицетворения, эпитеты, сравнения..."
    show monika e1c
    m "Да, местами они довольно «просты», однако умение грамотно их вставлять имеется."
    show monika cm oe
    mc "Хорошо, Юри -- так Юри."
    show monika om ce
    m "Отлично!"
    show monika om oe lpoint rhip
    m "Если с этой частью определились, то позволь мне показать свой стих."
    show monika cm oe ldown rdown
    mc "С удовольствием почитаю."
    show monika nerv cm oe
    call show_poem(poem_m2)
    "........."
    show monika lsur cm oe
    "Это.{w} Просто.{w} Охренеть!"
    show monika om oe
    m "Макс?..."
    m "У тебя немного странное выражение лица..."
    show monika cm oe
    mc "Да у меня челюсть на пол к чертям вылетела!"
    show monika nerv om oe
    m "Ха-ха, не льсти, это всего лишь--{nw}"
    show monika shoc cm oe n2
    mc "Опровергаю!" with vpunch
    mc "Это, как ты говорила, и есть идеальное стихотворение."
    mc "На полном серьёзе."
    mc "И смысл здесь виден очень хорошо..."
    show monika vsur om oe n3 at s11
    m "О-о..."
    show monika cm oe
    mc "Твой стих очень актуален в наши дни, но, думаю, ты сама это понимаешь."
    mc "Люди и вправду стали больше существовать, нежели жить и развиваться."
    mc "Нет, я не говорю, что нормальных не существует..."
    mc "Большинство в моральном плане стало жить гораздо хуже, при этом никто ничего не делает, чтобы это исправить."
    show monika om oe
    m "Ох..."
    show monika cm oe
    "Кажется, меня прорвало на слова..."
    "Что на меня вообще нашло?"
    show monika happ om ce n3 at t11
    m "Большое спасибо, Макс!"
    show monika nerv om oe at s11
    m "Д-даже и не знаю, что ещё сказать..."
    show monika vsur cm oe
    mc "Не стоит, Моника, ты реально заслужила эту похвалу."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    pause 1.0
    mc "Пойду, покажу стихотворение остальным, думаю..."

    scene black with wipeleft_scene
    "Минутка абсурда успешно пережита."
    "Блин, я что, Монику пронзить наповал пытался?"
    "Макс, ты ничерта не готов к отношениям в любом их проявлении, забыл?"
    "О, Сайори отлупилась от Нацуки и Юри."
    "Подойду-ка к ней."

    scene bg school literature_club board day
    show sayori turned happ cm oe at t11
    with wipeleft_scene
    show sayori om ce lup rup at h11
    s "Макс!"
    show sayori om e4c ldown rdown
    s "Скорее показывай, я вся в нетерпении!"
    show sayori cm
    mc "Читай на здоровье."
    "Лишь бы не сбить её настрой унылой аурой стиха..."
    show sayori oe
    call window_close

    play sound paper_torn_out
    show sayori lup poem_paper with dissolve
    pause 1.0
    show sayori e1b
    pause 3.0
    stop music fadeout 4.0
    show sayori neut cm e2a
    pause 5.0
    show sayori e2b
    pause 5.0
    show sayori neut cm oe
    pause 2.0
    show sayori om oe

    call window_open
    s "Оно..."
    s "У тебя так каждое утро?"
    show sayori cm oe
    mc "Практически часто."
    show sayori sad cm oe
    mc "А что?"
    show sayori om oe
    s "Если тебе плохо, то сразу скажи!"
    show sayori cm oe
    mc "Нет-нет, Сайори, со мной всё в порядке, не переживай на этот счёт."
    show sayori om e1b
    s "Всё равно..."
    show sayori cm e1a
    mc "Это всего лишь маленький стих, не принимай его близко к сердцу."
    show sayori e1b
    s "..."
    play sound paper_torn_out
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    show sayori e1a
    mc "Ладно, успокойся."
    show sayori neut cm oe
    mc "Давай я лучше твой стих почитаю, развею обстановку."
    show sayori worr om oe
    s "Вряд ли получится, потому что туда легли мои вчерашние чувства..."
    show sayori e1a
    s "...но держи."
    show sayori dist cm oe
    call show_poem(poem_s2)
    "Теперь я забеспокоился."
    "Если я правильно понял, Сайори написала про свой альтруизм, как я вчера выразился."
    "Она старается помочь всем и сразу, но при этом совершенно забывает о себе."
    show sayori neut cm oe
    mc "Хм, разве «друзья» в конце стиха кричали на тебя в негативном ключе?"
    show sayori om
    s "...у меня нет ответа на этот вопрос."
    show sayori dist om oe
    s "Писала, что в голову пришло..."
    show sayori neut cm oe
    mc "Просто мне кажется, они хотели, чтобы ты сохранила бутылочки себе."
    mc "Правда, поздно спохватились..."
    show sayori om
    s "Думаешь?..."
    show sayori cm
    mc "Уверен."
    show sayori curi cm oe
    mc "На самом деле, я мог бы даже продолжить твой стих прямо сейчас."
    mc "Отбить, скажем так, всю чернуху моего творения, ха."
    s "Хм..."
    "А ведь это реально идея..."
    "Мне же надо поддерживать её {b}искреннее{/b} настроение на должном уровне."
    show sayori neut cm oe
    mc "Так, сейчас..."
    mc "Ум-м-м..."
    show sayori me
    mc "...друзья столкнулись с отчаянием."
    mc "Они не могли смириться с таким окончанием."
    mc "Э-э-э..."
    show sayori flus cm oe
    mc "Они хотели отплатить и поддержать для них...{w}важного!..."
    show sayori happ cm oe b1b n3
    mc "Производителя счастливых бутылочек прекрасного."
    mc "Один из них взялся за уборку осколков..."
    mc "Другой...{w}э-э-э, за восстановлением колючих комков..."
    show sayori laug ma oe -b1b
    mc "Третий крепко обнял, отплатив за столько трудов..."
    mc "Четвёртый...{w}отдал своих пару...{w}комков."
    mc "Переживая, волнуясь, они поддержали того!..."
    show sayori cm
    mc "Кто был готов отдать для них всё!"
    mc "Кто заслужил себе отдых и объятья!"
    show sayori ce
    mc "Кому я протру макушку, полную счастья!"
    mc "Всё, ура!"
    show sayori om
    s "Ха-ха-ха!"
    s "Ты молодец, Макс!"
    show sayori cm
    mc "О, нет, Сайори, это ты молодец."
    play sound paper_torn_out
    pause 1.0
    call window_close

    hide sayori
    show sayori turned nerv cm ce n3 at e11
    with dissolve
    pause 2.0
    show sayori nl with dissolve
    pause 2.0
    hide sayori
    show sayori turned nerv cm ce nl at i11
    with dissolve
    pause 2.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    show monika lean happ cm oe at t_monika_watch with easeinright

    call window_open
    show monika om oe
    m "А меня ты ещё не гладил!"
    show monika cm ce
    show sayori flus om ce n1 lup rup at h11
    mc "ПФ-Ф-Ф!" with vpunch
    show monika om ce
    show sayori cm oe ldown rdown
    m "Ха-ха-ха!"
    hide monika cm ce with easeoutright
    pause 0.3
    mc "Ладно..."
    show sayori e1a
    mc "Я ещё не показывал свой стих Юри и Нацуки..."

    scene black with wipeleft_scene
    "Меня крайне настораживает, что мной интересуется Моника."
    "А может..."
    "Да не, бред какой-то."

    scene bg closet
    show natsuki turned fc neut cm oe at t11
    with wipeleft_scene
    show natsuki om rhip
    n "О, ты?"
    show natsuki cm
    mc "Да, я."
    show natsuki sedu cm oe
    mc "Снова будешь смеяться над моим стихом?"
    show natsuki om
    n "Зависит от того, что ты там написал."
    show natsuki cm
    call window_close

    play sound paper_torn_out
    show natsuki lup poem_paper with dissolve
    pause 1.0
    show natsuki ff e1b
    pause 3.0
    show natsuki neut cm e2b
    pause 5.0
    show natsuki om

    call window_open
    n "{size=19}Что-то не смешно нифига...{/size}"
    show natsuki oe
    n "Что ж, оно намного лучше предыдущего, и я не шучу."
    show natsuki cm oe
    mc "Вот как?"
    show natsuki om oe
    n "Ага."
    show natsuki curi om oe
    n "И вообще, стих довольно серьёзный, что тут может быть смешного?"
    show natsuki cm oe
    mc "Мало ли..."
    show natsuki anno om oe
    n "Я не настолько отбитая и подлая."
    show natsuki cm oe
    mc "И в мыслях не было."
    show natsuki om oe
    n "Но ведь сомнения были?"
    show natsuki cm oe
    mc "Нет."
    show natsuki curi om oe
    n "Тогда к чему было \"мало ли\"?"
    show natsuki neut cm oe
    mc "Банальное насторожение."
    show natsuki happ om ce
    n "Ха, расслабься, разорвать тебя на части всё равно не смогу."
    show natsuki cm oe
    mc "Допустим..."
    play sound paper_torn_out
    show natsuki ldown with dissolve
    pause 1.0
    show natsuki fc happ om oe
    n "Ок, оценивать по достоинству чьи-либо стихотворения я не умею, поэтому вместо того, чтобы стоять передо мной столбом, прочти моё."
    show natsuki om ce lhip
    n "К этому ты точно не прикопаешься."
    show natsuki cm
    call show_poem(poem_n2)
    "Этот стих намного лучше прошлого: затрагивает тему принятия чужих интересов..."
    show natsuki neut cm oe
    mc "Ха, не нравятся пауки, да?"
    show natsuki vang om ce
    n "Фу, мерзость!"
    show natsuki cm
    mc "Слушай, я тоже своего рода арахнофоб, но они всё-таки полезные."
    show natsuki doub cm oe
    mc "Не надо на них так гнать."
    show natsuki om lhip rhip
    n "С чего это вдруг?"
    show natsuki anno om oe
    n "Я видела, много раз, как они жрали всё, что попадёт в паутину."
    n "И мне очень мерзко наблюдать, как жертвы медленно пожираются этими чудовищами."
    show natsuki ce
    n "Передёргивает с такого..."
    show natsuki cm
    mc "Прекрасно понимаю, у самого возникают такие же чувства."
    show natsuki neut cm oe b1d
    mc "Но при этом паукам тоже не очень «радужно»."
    show natsuki om
    n "Это их не оправдывает."
    show natsuki cm
    mc "Ага, посмотрел бы я на тебя, когда ты несколько дней или даже недель ничего не ела, а тут вдруг попалось что-то съедобное."

    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0

    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        linear 240 rotate 8 zoom 1.30 # и ведь кто-то дождётся конца таймера и скажет, что тут недоработано

    mc "{size=24}О, например, помнится мне, когда меня ещё маленьким в деревню отвозили, я любил там всяких пауков подкармливать.{/size}"
    show natsuki brow
    mc "{size=23}Нет, я, конечно, арахнофоб, уже говорил, но почему-то мне было интересно пауков подкармливать...{/size}"
    show natsuki ldown rdown
    mc "{size=23}Так вот, был там один вид пауков, они плели густую паутину в укромных уголках дома, а себе делали небольшую норку.{/size}"
    mc "{size=22}И все эти паутины были покрыты жирнющим слоем пыли, как-будто они были заброшены.{/size}"
    mc "{size=22}Но не, пауки там сидели и сидели.{/size}"
    mc "{size=21}Всё ещё не могу понять: что они там жрали?{/size}"
    mc "{size=21}Они явно так по полгода без еды сидели, но всё ещё продолжали сидеть.{/size}"
    mc "{size=20}Я решил одного из них покормить, когда меня какая-то летающая зараза пыталась тяпнуть.{/size}"
    mc "{size=20}Я взял, кинул в паутину.{/size}"
    mc "{size=19}И стоило только оглушённому мною существу дёрнуть немного лапой, как в середину паутины выбежало это создание.{/size}"
    show natsuki lsur cm oe
    mc "{size=19}По соотношению размеров это всё равно, что если на тебя выпрыгнет микроавтобус с 8-ю лапами.{/size}"
    mc "{size=18}Существо дёрнулось второй раз, паук сразу на неё напал, схватил хлицерами и резко утащил в норку.{/size}"
    mc "{size=18}Буквально прошло 7 секунд.{/size}"
    mc "{size=17}У обычных пауков такая процедура проходит в течение 10 минут.{/size}"
    mc "{size=17}А теперь подумай, насколько тот паук был голодный и обездоленный, если он с таким остервенением существо сожрал?{/size}"
    mc "{size=16}Я реально понять не могу, зачем они сидят там, где всякие мухи будут пролетать в последнюю очередь?{/size}"
    mc "{size=16}И ещё не могу понять, как они выдерживают огромное количество времени без еды?{/size}"
    mc "{size=15}У меня бы давно уже желудок в узел связался.{/size}"
    mc "{size=15}Хотя если бы эти пауки пытались поселиться в открытых местах...{/size}"
    mc "{size=14}То обязательно бы припёрся другой, началась бы драка насметрь.{/size}"
    mc "{size=14}Или же прибежал бы «вор», который крадёт добычу.{/size}"
    show natsuki pani cm oe
    mc "{size=13}Или же человек какой-нибудь взял и раздавил нафиг...{/size}"
    show natsuki om ce

    show layer master

    stop music fadeout 1.0
    n "В-всё, хорош, хватит!" with vpunch
    show natsuki ff pout om ce
    n "Твоя охренительная история очень охренительная, но хватит, перестань!"
    n "Пожалуйста..."
    show natsuki cm
    mc "..."
    mc "Прости, ушёл в свои размышления..."
    "Чёрт, я перестарался."
    show natsuki sad cm oe
    "Не знаю, что именно Нацуки задело, но мне тоже мерзко от себя стало."
    mc "В общем, ты поняла, надеюсь..."
    play sound paper_torn_out
    pause 1.0
    n "..."
    mc "Пойду я..."

    scene black with wipeleft_scene
    "Как с вами всеми трудно..."
    "И непонятно, что там у вас в душе творится."
    "Благо Моника и Сайори уже спешат меня заменить, хоть развеят Нацуки."
    "Мда..."
    "Это ж сколько секретов мне про вас придётся узнать?..."

    scene bg club_day
    show yuri turned lsur cm e1d at t11
    with wipeleft_scene
    play music t5 fadein 3.0
    show yuri om lup rup
    y "Макс?"
    y "Ты довольно хмурый..."
    show yuri curi om oe ldown rdown
    y "Что-то случилось?"
    show yuri cm
    mc "Да как-то всё не так пошло, как ожидал..."
    show yuri om
    y "Снова Нацуки?"
    show yuri cm
    mc "Неа, здесь я перестарался."
    show yuri neut cm e1d
    mc "Решил рассказать ей про то, как трудно быть пауком, а в итоге увлёкся мыслью и умудрился её задеть."
    mc "Не знаешь, почему она так отреагировала?"
    show yuri anno om oe
    y "Узнать бы сначала, что ты конкретно ей говорил..."
    show yuri cm
    mc "Ничего особенного, честно."
    show yuri om e2c
    y "Но если о тяжести паучьей жизни...{w}даже не знаю..."
    show yuri neut cm e1d
    mc "Да блин, знал бы, промолчал."
    show yuri flus om oe lup rup
    y "Не надо винить себя в таком, все мы ошибаемся."
    show yuri lsur cm oe at s11
    mc "К чёрту такие ошибки."
    mc "Никакого толка или хоть какой-нибудь пользы."
    show yuri flus om oe
    y "Я бы поспорила..."
    show yuri neut cm e1d
    mc "Ладно, давай уже обмен стихами начнём, а то всё время потеряем."
    show yuri happ cm ce ldown rdown at t11
    y "Угу!"
    show yuri oe
    mc "Держи."
    call window_close

    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0
    show yuri e1b
    pause 3.0
    show yuri neut cm e2b
    pause 7.0
    show yuri happ om ce rup

    call window_open
    y "Стиль Сайори дал свои плоды, хе-хе..."
    show yuri e1d rdown
    y "Стих в этот раз достаточно компактный, при этом мысль завершена."
    show yuri flus om oe
    y "Если оценивать структуру, то, честно говоря, только третье четверостишие мне понравилось..."
    show yuri md oe
    mc "Ха, я даже не удивлён."
    show yuri cm e1d rup at s11
    y "П-прости за грубость!"
    show yuri mj
    mc "Нет-нет, продолжай."
    show yuri cm oe at t11
    y "У, хорошо..."
    show yuri dist om oe rdown
    y "Так вот, первое четверостишие сломано по ритму и продолжительности."
    show yuri anno om oe
    y "Второе уже лучше, но здесь слишком сильный разброс по длине строф."
    show yuri happ om e1b
    y "А вот в третьем у тебя получилось сохранить и ритм, и пропорции."
    show yuri oe
    y "Иными словами, это самая сбалансированная часть."
    show yuri ce rup
    y "Не знаю, заметил ты или нет, но это довольно любопытно, что у тебя получились лесенки."
    show yuri cm
    mc "Да, Моника уже подметила эту особенность."
    show yuri om e1b rdown
    y "Когда читаешь подобные четверостишия, то создаётся впечатление, что ты сам по инерции начинаешь спускаться вниз."
    show yuri oe
    y "Может, тебе стоит попробовать отточить стихотворения в таком виде?"
    show yuri cm
    mc "Не знаю, не ручаюсь."
    mc "Я больше пишу так, как выйдет."
    show yuri om oe
    y "Это просто предложение на будущее."
    show yuri cm oe
    mc "Да, я понимаю."
    show yuri flus om oe
    y "Больше мне нечего сказать."
    show yuri happ om ce rup
    y "У тебя начинает что-то получаться, так что продолжай в том же духе!"
    show yuri cm ce
    mc "Ох, спасибо."
    show yuri cm oe rdown
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    mc "Можно твой стих почитать?"
    show yuri happ om ce lup rup
    y "Конечно, бери!"
    show yuri cm ce
    call show_poem(poem_y2)
    show yuri ldown rdown
    mc "Это довольно миленько."
    show yuri cm oe
    mc "Любишь енотов, Юри?"
    show yuri om ce lup rup
    y "Отчасти, хех..."
    show yuri om oe ldown rdown
    y "Но стих совершенно не о нём."
    stop music_poem fadeout 5.0
    show yuri cm oe
    "Подождите..."
    "До меня только сейчас дошло, насколько тут всё...{w}странно."
    "Но больше всего меня напрягают моменты с описанием ножа."
    show yuri lsur cm oe
    "Юри, что...{w}лезвия любит?"
    "Хотя это поспешный вывод."
    "Даже если это бред моего воображения, то тогда причём тут енот с хлебом?"
    show yuri om oe
    y "Макс?"
    show yuri cm oe
    mc "Фу, я снова здесь."
    mc "Опять задумался и в себя провалился."
    show yuri flus om oe lup rup
    y "Всё хорошо!"
    show yuri cm oe
    mc "Что-то я в этом начинаю сомневаться..."
    show yuri shy sad cm oe n5 at s11
    y "Угх..."
    show yuri neut cm e1 n1
    mc "Если не секрет, то расскажи, о чём конкретно ты написала это стихотворение?"
    show yuri turned dist om oe lup rup at t11
    y "Ну..."
    show yuri happ om oe ldown rdown
    y "На самом деле мне хотелось бы, чтобы ты сам догадался."
    y "Стихотворения, помимо контекстного посыла, передают эмоции."
    y "Всё это в совокупности должно отозваться у читателя."
    show yuri dist om oe
    y "Если я расскажу смысл, то нарушу весь эффект восприятия."
    show yuri lsur cm oe
    mc "Иными словами, ты тактично увильнула от ответа?"
    show yuri shy sad cm oe n5 at s11
    y "Уф-ф-ф..."
    mc "Я пошутил!"
    play music t5 fadein 3.0
    show yuri neut cm e1 n1
    mc "В общем, я просто хотел уточнить, то ли это, о чём я подумал..."
    show yuri turned anno om oe lup rup at t11
    y "Ах, вот оно что..."
    show yuri neut cm e1d
    mc "Ладно, помозгую на досуге и позже озвучу свои мысли, если будет интересно."
    show yuri happ om oe ldown rdown
    y "Хорошо, можешь с этим не торопиться."
    show yuri ce
    y "К тому же услышать чью-то догадку по замыслу своего творчества всегда интересно."
    show yuri cm oe
    mc "Хе, спасибо за стих."
    play sound paper_torn_out
    pause 1.0
    show yuri cm ce
    show monika forward happ om oe lpoint at t43 zorder 2
    m "О, вы закончили?"
    show yuri neut cm e1d at t42
    show monika cm oe ldown
    mc "Да."
    show monika lean happ om oe at h43
    m "А то уже вас заждались."
    show monika cm oe
    mc "Разве мы так заболтались?..."
    show yuri lsur cm oe n3
    show monika forward happ om ce
    m "Да, вы так хорошо разговаривали, что не хотели вас прерывать."
    show monika cm ce
    mc "Да ладно вам, ничего такого."
    show yuri shy neut cm oe n5 at s42
    y "Угх..."
    show monika om oe
    m "Ну-ну, Макс..."
    show monika happ cm ce
    mc "Что ещё за \"ну-ну\"?"
    show monika om ce
    m "Ладно, проехали."
    show monika cm
    mc "Эй..."
    show sayori turned neut cm oe at t41
    show yuri e1 n1
    show monika om oe lpoint rhip
    show natsuki turned sad cm oe at t44
    m "Итак, друзья!"
    show monika cm ldown
    mc "{size=19}Ай...{/size}"
    show yuri turned neut cm e1d at t42
    show monika lean happ om oe at h43
    m "Как вам второй обмен стихотворениями?"
    show sayori dist cm oe
    show yuri anno mf oe
    show monika neut cm oe
    nsy "..."
    show yuri neut mf e1d
    show monika forward flus om e1a
    m "Ребят, чего вы такие кислые?"
    show monika cm
    show natsuki e1a
    mc "Честно сказать, этот обмен был так себе..."
    show sayori neut cm oe
    show yuri happ cm oe
    show monika happ om ce
    m "Ох, выше нос!"
    show yuri cm ce
    show monika om oe
    m "Нас ждёт ещё множество хороших и приятных событий!"
    show yuri cm oe
    show monika lpoint
    show natsuki neut cm oe
    m "А пока небольшое объявление на завтра."
    show yuri laug cm oe
    show monika om ce ldown
    m "Макс решил выбрать стиль Юри к следующей клубной сходке."
    show yuri happ om oe
    show monika cm oe
    y "Не будет ли ему трудно в составлении стиха?"
    show yuri cm oe
    show monika om oe
    show natsuki dist cm oe
    m "Ему придётся попробовать в любом случае."
    show yuri neut mf e1d
    show monika lpoint
    m "Всё зависит от личных способностей Макса, а также какое стихотворение будет выступать в качестве примера."
    show sayori e1b
    show yuri anno mf oe
    show monika cm oe ldown
    y "Хм..."
    show sayori oe
    show yuri neut mf e1d
    show monika om ce
    show natsuki neut cm oe
    m "Ладно, раз пока других вопросов нет, то Сайори и Нацуки могут быть свободны, а Юри я попрошу остаться!"
    show natsuki e1b at thide
    hide natsuki
    show yuri anno mf oe
    show monika om oe lpoint at t22
    m "Макс, тебя это тоже касается."
    show monika cm oe ldown
    mc "Конечно."
    show sayori sad om oe
    show monika neut cm oe
    s "Макс, я лучше провожу Нацуки до дома, так что меня потом не жди на выходе, хорошо?"
    show sayori cm oe
    mc "Договорились."
    show sayori at thide
    hide sayori
    show yuri at t21
    show monika dist cm oe
    "Надо будет позже извиниться перед Нацуки, не хочу это так оставлять."
    "Может, мне на руку сыграет стих в её стиле..."
    "Правда, через день..."
    show yuri neut cm e1d
    show monika happ om oe lpoint
    m "Итак, Юри, тебе нужно определиться с прототипом."
    show yuri happ cm oe
    show monika om ce ldown
    m "Желательно, чтобы он был как можно проще, ха-ха!"
    show yuri om oe lup
    show monika cm ce
    y "Могу отдать сегодняшнее стихотворение."
    show yuri flus om oe
    show monika cm oe
    y "Первое было хоть и короче, но сложнее в написании..."
    show yuri happ cm oe ldown
    show monika om oe
    m "Хорошая мысль."
    show yuri om ce lup rup
    show monika cm oe
    y "Макс, вот."
    show yuri cm ce
    play sound paper_torn_out
    pause 1.0
    mc "Да, спасибо."
    show yuri ldown rdown
    show monika om ce
    m "Отлично!"
    show yuri cm oe
    show monika lean happ om oe at h22
    m "Жду завтра твой второй экспериментальный стих."
    show monika forward happ om ce
    m "До встречи!"
    show yuri om ce
    show monika cm ce
    y "До встречи!"
    show yuri cm ce
    mc "Удачи."
    stop music fadeout 3.0
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show yuri turned neut cm e1d school_bag at t11
    with wipeleft_scene
    mc "В этот раз как-то реально вяло..."
    show yuri happ om oe
    y "Не бери в голову."
    y "Разве подобные случаи не показатель того, что у нас есть чувства?"
    show yuri neut cm e1d
    mc "Да я и без этого знал..."
    show yuri e1b
    "Голова снова никакая..."
    "А мне ещё стих клепать, а-а-а..."
    show yuri om e1d
    y "Кстати, м-может..."
    show yuri flus cm oe at s11
    y "Э-э-э..."
    mc "Что?"
    y "Ну..."
    show yuri om oe
    y "Раз все разошлись, то..."
    show yuri neut cm e1d
    mc "Хочешь, чтобы я составил тебе компанию по пути домой?"
    show yuri happ om ce lup rup at t11
    y "Д-да!"
    show yuri flus cm oe
    y "Если не против..."
    show yuri neut cm e1d ldown rdown
    mc "А далеко идти?"
    show yuri om
    y "Нет, тут рядом..."
    show yuri happ cm oe
    mc "Ладно, почему нет."
    mc "Вместе веселее."
    show yuri om ce lup rup
    y "Да!"
    show yuri cm ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show yuri turned happ cm e1b school_bag at t11
    with wipeleft_scene
    mc "Юри..."
    show yuri oe
    y "М-м?"
    show yuri neut cm e1d
    mc "А как у тебя прорезался писательский талант?"
    show yuri happ om e1b
    y "Родители привили любовь к книгам."
    y "В детстве я часто читала вместе с мамой."
    show yuri ce lup rup
    y "Мы с ней обсуждали различные истории."
    show yuri ldown rdown
    y "Сначала простые, потом посложнее..."
    show yuri oe
    y "Она покупала новые книжки, моё любопытство росло с каждым днём."
    show yuri e1b lup
    y "Когда я научилась читать самостоятельно, то стала проглатывать их одну за другой."
    show yuri oe ldown
    y "Чтение переросло в страсть."
    show yuri ce
    y "Она была настолько сильной, что даже отец решил привозить новые экземпляры из-за границы."
    show yuri oe
    y "Он часто уезжал в командировки и обязательно возвращался с сувенирами."
    show yuri om e1b
    y "Я всегда радовалась в такие моменты, потому что мне на руки попадали частички внешнего мира."
    show yuri neut om e1d
    y "Как-то так..."
    show yuri cm
    mc "У вас дома целая библиотека?"
    show yuri happ om ce lup rup
    y "Это громко сказано, хах..."
    show yuri om oe ldown rdown
    y "Но несколько стеллажей имеется."
    show yuri cm oe
    mc "Ох..."
    mc "У меня только в спальне небольшие полки заполнены, и то не мной, я это не читаю..."
    show yuri om oe
    y "Ну, ты же говорил, что любишь интересные визуальные новеллы..."
    show yuri om ce
    y "Так что можно считать, что ты тоже своего рода читатель, хе-хе."
    show yuri cm ce
    mc "Не такой ярый, на самом деле."
    show yuri oe
    mc "Как я говорил, с новеллами, как и с книгами, дела обстоят так же."
    mc "Просто главное, чтобы история захватывала."
    show yuri om
    y "Согласна."
    show yuri dist om ce lup rup
    y "Потому что история -- есть душа произведения."
    y "А без души любое существо перестаёт быть существом."
    show yuri cm ce
    mc "Верно..."
    show yuri om ce
    y "От неё же и зависит богатство внутреннего мира."
    y "Его разнообразие, красота..."
    show yuri cm
    "Что-то её понесло..."
    show yuri om e1a
    y "Макс, мне интересно..."
    show yuri ldown rdown
    y "У тебя богатый внутренний мир?"
    show yuri neut om e1d
    y "Н-ну, раз ты любишь читать произведения, которые тебя захватывают..."
    show yuri cm
    mc "Пф, ну и вопросы..."
    mc "Не хочу быть эгоистом, но скорее да, чем нет."
    mc "Воображение иногда кишит различными образами и мыслями."
    mc "Особенно я это замечал во время изучения книг и игр."
    mc "Некоторые даже хотелось бы дополнить своими идеями, которые помогли бы раскрыть тех или иных персонажей, или сделать некоторые ситуации лучше..."
    show yuri e1b
    mc "Но кто меня такого слушать будет, ха."
    show yuri om
    y "Да, авторские права..."
    show yuri curi cm oe
    mc "А ещё, кстати, на воображение сильно влияет музыка."
    show yuri om oe lup
    y "Вот как?"
    show yuri cm oe
    mc "Ага."
    show yuri neut cm e1d
    mc "Стоит только найти какую-нибудь насыщенную музыку, особенно без клишированного звучания, так сразу захлёстывает."
    mc "Потом переслушиваешь по 10 раз, затирая до дыр, правда воображение уже не так бурно работает..."
    show yuri anno cm oe
    y "М-м-м..."
    show yuri happ om oe ldown
    y "Да, я могу понять."
    show yuri e1b
    y "Иногда у меня тоже случается что-то подобное..."
    show yuri cm
    mc "Хах."

    scene bg yuri house outside day
    show yuri turned happ cm oe school_bag at t11
    with wipeleft_scene
    show yuri om ce
    y "Пришли."
    show yuri cm ce
    mc "Это твой дом?"
    show yuri om oe
    y "Да."
    show yuri cm oe
    mc "Довольно компактный..."
    show yuri om e1b lup
    y "Есть такое, но внутри я никогда не чувствовала себя тесно."
    show yuri om ce ldown
    y "Даже наоборот."
    show yuri cm ce
    "Оно и понятно, всё-таки дом -- безопасное место, где ты можешь быть собой."
    show yuri lsur cm oe
    mc "Ладненько, извини, Юри, но мне уже пора."
    show yuri om oe lup rup at s11
    y "Ох, прости за задержку!"
    show yuri cm oe
    mc "Нет, всё нормально."
    show yuri neut om e1d ldown rdown at t11
    y "Тебя же ведь кто-то ждёт дома?"
    show yuri curi cm e2a
    mc "Нет."
    show yuri e2b
    y "..."
    mc "Я один живу: родители в другом городе, далеко отсюда..."
    mc "Не подумай ничего такого."
    show yuri laug om oe lup rup
    y "Ах, вот оно что..."
    show yuri happ om oe ldown rdown
    y "Тогда до завтра?"
    show yuri cm oe
    mc "До завтра."
    show yuri om ce
    y "Спасибо за компанию!"
    show yuri cm ce
    mc "Да не за что."
    show yuri at thide
    hide yuri
    pause 2.0
    "Чтобы я раньше подумал, что вот так просто буду с кем-то разговаривать, кроме Сайори..."
    "Сам бы себе не поверил."
    "..."
    "Стойте..."
    "А обратно-то куда идти?"
    "Я ж здесь не был."
    mc "Да блин!"
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "О, мои ноги..."
    "Всё ещё гудят..."
    "Если бы не мобильный интернет, я бы тогда заплутал..."
    mc "Уф-ф-ф..."
    "Кровать так манит своим видом...{w}пытается меня соблазнить...{w}втянуть в свои объятия..."
    "Но стих вклинился в наши отношения, образовав любовный треугольник с одним вывернутым во внутрь углом."
    mc "Хорошо, берёмся за стих."
    "Сначала проанализируем пример от Юри..."
    call show_poem(poem_y2, music=False)
    "Блин, нет."
    "Меня всё ещё напрягают строфы про нож."
    "Здесь явно что-то более негативное, чем я думал раньше."
    "Что же с Юри не так?"
    "Возможно, у неё проблемы с родителями."
    "Или в жизни, или с чем-нибудь ещё..."
    "Короче, без понятия, но мне это начинает не нравиться."
    "Озвучивать ли самой Юри подобные домыслы?..."
    "Вообще стоит, вдруг тут нечто серьёзное в психологическом плане, что требует немедленной проработки и лечения."
    "Тут как раз бы помог тот психолог..."
    "Может, надо с ним связь восстановить?"
    "Да, он меня кинул без предупреждения в тот момент, когда я в нём максимально нуждался."
    "Однако...{w}в этот момент у него тоже был трудный период, даже хуже моего..."
    "А я тут со своими нуждами в общении..."
    mc "Аргх, блин, не знаю!" with vpunch
    "Достало уже в подвешенном состоянии находиться, не о том думаю."
    "Так, снова прочитаем стих и проанализируем его структуру."
    call show_poem(poem_y2, music=False)
    "Растянутость за счёт объединения двух строф в одну."
    "Деление на четверостишия отсутствует, вместо него -- сюжетные кластеры."
    "Есть аллегории."
    "Ну и в целом стих достаточно объёмный."
    "Ладненько, Юри, попробуем твой стиль..."

    call poem_act_1_day_3

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc3, music=False)
    "Да что ж так криво вышло..."
    "Начало точно в помойку, нарушил всё, что только мог нарушить."
    "Конец тоже слеплен коряво..."
    mc "Ф-у-ф-л-о."
    "С другой стороны, я впервые доволен своей работой, хоть и чуть-чуть."
    "Даже смог сделать некую аналогию с участницами клуба."
    mc "Эх, но могло быть и лучше..."
    "К чёрту, плевать."
    "У меня нет сил что-то делать."
    "Лучше откисну."
    call window_close

    return
