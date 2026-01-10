
label act_1_day_10:

    call window_open
    call autosave
    if persistent.censorship:
        mc "{sc=3}ЗАРАЗА!{/sc}" with vpunch
    else:
        mc "{sc=3}БЛЯТЬ!{/sc}" with vpunch
    mc "{sc=2}Больно-то как!{/sc}"
    mc "{sc=2}Проклятая тумбочка!{/sc}"
    mc "{sc=2}Мой лоб!{/sc}"
    if persistent.censorship:
        mc "{sc=2}С-с-сво-о-олочь!{/sc}"
    else:
        mc "{sc=2}С-с-су-у-ука!{/sc}"
    "{sc=1}......{/sc}"
    mc "{sc=0.5}Тумбочка?...{/sc}"

    scene bg bedroom at mc_bed
    with dissolve
    pause 0.25
    "..."
    mc "...чего?"
    call window_close

    play sound none_transition
    scene black
    show screen new_day(episode)
    pause 4.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d9.unlocked == False:
        $ ach_a1_d9.unlock()
        pause 7.0
    else:
        pause 3.0

    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg kitchen at mc_kitchen_table_alone
    with dissolve_scene_full
    "Как, блин, можно было дёрнуться во сне так, чтобы влететь лбом в тумбочку...{w}будучи лёжа?!"
    mc "Пф-ф-ф..."
    "Эти кошмары меня уже достали..."
    "То Сайори повешенная, то Моника орущая, то Юри чрезмерно возбуждённая..."
    "Но если абстрагироваться от выяснения причин этого маразма, возникает один жирный вопрос..."
    "КАК моему мозгу удаётся проецировать всё НАСТОЛЬКО реалистично?"
    "Причём я даже себя кое-как контролировать могу!"
    "Думать, оценивать ситуацию, принимать решения..."
    "Не просто прыгать в «облаках» или мыслить в полусне, когда вся голова в тумане, не-е-е..."
    "{b}Я полностью осознаю себя{/b}."
    "И при этом не могу управлять своим воображением."
    mc "Как это парадоксально!"
    "Мозг ведь один."
    "Получается, он сам себе в «колено» стреляет с полным пониманием происходящего?"
    mc "Да что за бред!"
    mc "У меня в жизни никогда такого не было."
    mc "Всё было в порядке..."
    mc "Что случилось?"
    mc "Может, это всё-таки прекратится и больше ничего подобного не будет?"

    scene bg kitchen with dissolve
    play sound trashcan
    pause 4.0
    mc "Мозг, засранец, пожалуйста, хватит..."
    mc "Мне уже по горло достаточно твоих представлений."
    mc "У меня и так проблемы с моральным отдыхом, плюс куча проблем, которые с ходу не решишь, а тут ещё твои сюрпризы!"
    mc "Почему?"
    mc "Из-за стресса?"
    mc "А как тогда от него избавиться?"
    mc "Я, чёрт побери, уже во взрослой жизни, хоть и школу официально не окончил."
    mc "Тут нет времени на такое."
    mc "Всем плевать на твои проблемы, всем нужен результат."
    mc "Ненавижу это дерьмо..."
    "..."
    mc "...я только что разговаривал вслух, а не в своих мыслях?"
    mc "Классно."
    mc "Я начинаю потихоньку терять контроль над своей психикой..."
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "Все предметы: пенал, ключи, мобильник, стих..."
    "Вроде всё."
    "Тогда выходим."
    call window_close

    scene black with dissolve
    pause 1.0
    play sound house_door_open
    play noise_2 street_suburban_noise fadein 3.0
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
    "Да что ж так солнечно..."
    "Вроде прохладно, а вроде на солнце припекает..."
    "Мы ж не прям в южной полосе Японии."
    "Тут зимой иногда и снег выпасть может."
    "Берём в расчёт то, что сейчас апрель."
    mc "Мда."
    "Я думал, что тут прохладнее."
    "..."
    "Так это...{w}где Сайори?"
    "Опаздывает на пару минут?"
    "Совсем на неё не похоже..."

    scene bg house with wipeleft_scene
    "Либо она просто заранее договорилась (условно) с Моникой о встрече по стиху и вышла намного раньше..."
    "Либо она дрыхнет..."
    "..."
    "Ну вот и сколько её ждать?"
    "Время не резиновое."
    "..."
    mc "Ой, ладно..."
    "Никто не помрёт, если я спрошу об этом напрямую."
    call window_close

    pause 0.6
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 3.5
    show sayori_mom happ cm oe at t11
    pause 0.25

    call window_open
    mc "Здравствуйте."
    show sayori_mom om ce rhip
    sm "Ах, Макс, доброе утро!"
    show sayori_mom neut cm oe
    mc "Сайори выйдет?"
    mc "А то уже пора в школу."
    show sayori_mom om lpoint
    sm "Она уже ушла."
    show sayori_mom cm ldown
    mc "Да?"
    show sayori_mom om
    sm "Как она сама сказала, побежала к Монике что-то со стихом делать."
    show sayori_mom happ cm oe
    mc "А-а-а, понятно..."
    "Значит, я попал в десятку."
    show sayori_mom om ce
    sm "Она творческая умничка!"
    show sayori_mom e1b
    sm "Так ответственно подходит к клубной деятельности..."
    show sayori_mom cm
    mc "Ага..."
    "Настолько, что ничего мне не написала."
    show sayori_mom oe
    mc "В общем, спасибо, я тогда пойду."
    show sayori_mom om
    sm "Конечно, Макс."
    show sayori_mom ce
    sm "Успехов в учёбе!"
    show sayori_mom cm
    mc "И Вам...{w}э-э-э, в целом."
    show sayori_mom rdown at thide
    hide sayori_mom

    scene bg residential_day with wipeleft_scene
    "Надо было по-другому последнюю фразу сформулировать..."
    "Ой, да пофиг."
    "Главное, что люди понимающие."
    "И добрые."
    "А то я в Интернете читал множество комментариев из других стран, и там пишут, что с этим делом всё обстоит намного плачевнее..."
    "Иногда мне кажется, что, родись я в другое время или в другой стране, я бы банально не выжил."
    "Не выдержал бы стресс, проблемы, прочую мишуру..."
    "Неужто я такой «хрупкий»?"
    "Как я вообще дожил до своих 18-ти лет?..."

    scene bg niigata street suburban 10 day with wipeleft_scene
    "..."
    "Нет, но Сайори могла хотя бы написать, что сегодня утром её не будет."
    "А может, она снова была в круговороте суеты, вот и забыла это сделать."
    "Вполне возможно."
    "Наверное, они там решили свои куски стихотворения своими почерками писать."
    "Ну или ещё что-то..."
    "Ха, надеюсь, Юри и Нацуки смогли найти общий стихотворный язык."
    "Не хватало ещё, чтобы они «поубивали» друг друга, когда недавно прекрасно помирились."
    "..."
    "......"
    mc "Как непривычно без Сайори..."
    "Сразу становится скучно."
    "Да, тишина, да, можно собраться с мыслями..."
    "Но это как-то совсем не то, что я хотел."

    scene bg school gate 1 with wipeleft_scene
    "Думать совершенно не хочется."
    "А если и начнёшь, то сразу всплывают все проблемы, задачи, обязательства..."
    "Я просто хочу отдохнуть от всего этого."
    "Не просто сделать глоток воздуха в этих бушующих волнах, а побыть на береге в ясную погоду, когда на воде штиль..."
    "Как я вообще могу наслаждаться жизнью и получать от неё удовольствие, когда на меня сваливается весь этот бардак?"
    "Решишь одно -- появится другое."
    "Не решишь -- будет больше проблем."
    "..."
    "Нет, это никогда не закончится..."
    "Надо жить на автопилоте, чтобы снизить свой уровень восприятия и, как следствие, уровень стресса."
    "И не уйти в таком состоянии куда-то не туда..."
    stop noise_2 fadeout 3.0
    call window_close

    call window_dialog_long_transition("n")

    call window_open
    play noise_1 school_corridor_light_noise fadein 3.0 volume 0.5
    scene bg school new_class_natsuki day with dissolve_scene_full
    "Да как же в последнее время всё...{w}мерзко!"
    "То Клуб выпечки, то пьянство Юри, то упрёки за то, что НеПрАвИлЬнО заставила Котоноху пригласить, то отец себя грубо ведёт..."
    n "Тьфу!" with vpunch
    "А тут ещё этот дурацкий совместный стих!"
    "\"Попробуйте составить что-то вместе, что-то там проработайте, бе-бе-бе\"..."
    "Вот серьёзно: такое ощущение, что Монике просто скучно!"
    "Мы что, своими делами заняться не можем?"
    "Почему мы обязаны что-то писать, когда это никем не проверяется от слова совсем?"
    "Почему бы просто не почитать мангу или сыграть в какую-нибудь настолку..."
    "И ладно, просто стих...{w}но совместный?!"
    "Я же стараюсь быстро их писать, чтобы отец ничего не увидел, а то мало ли, что подумает..."
    "Потому что я ему не очень доверяю."
    "Да, он знает, что я пишу стихи, но не знает, как это всё выглядит."
    "Если он только не нашёл мою стопку стихов в глубине шкафчика справа от стола..."
    "Короче, ничего мы ещё не написали."
    "Пока что Юри сказала сделать его сегодня на большой перемене в библиотеке."
    "И она уже началась."
    "Котоноха тоже должна прийти, за компанию."
    "Но что-то мне подсказывает, что у нас вообще ничего не получится..."
    "Ну не нравится мне стиль Юри, при всей моей симпатии!"
    "Её витиеватые словечки постоянно вводят в заблуждение, из-за чего теряется смысл прочитанного."
    "Они будут сильно выделяться на моём фоне!"
    "Или...{w}мой стиль будет сильно выделяться на её фоне..."
    play noise_2 school_corridor_hard_noise fadein 3.0
    stop noise_1 fadeout 3.0

    scene bg school f3 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    with wipeleft_scene
    "Да в любом случае это будет тяжело!"
    "Хоть бы вытерпеть этот момент, хоть бы что-то получилось..."
    stop noise_2 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school library
    show yuri turned neut cm e1b at t21
    show kotonoha neut cm e1b rhip at t22
    with wipeleft_scene
    "О, они все тут."
    show yuri e1d
    show kotonoha oe
    n "Хай."
    show yuri om
    show kotonoha happ cm oe
    y "Привет..."
    show yuri cm
    show kotonoha om ce lup rhid
    k "Наконец-то!"
    show kotonoha cm oe ldown rdown
    n "Значит так: мы быстро составляем короткий стих и--{nw}"
    show yuri e1b at t31
    show libitina forward neut cm oe at t32
    show kotonoha lsur cm oe at t33
    n "ЧТО?!" with vpunch
    show kotonoha neut cm oe
    n "Лина, ты что тут забыла?!"
    show libitina shy happ om oe
    l "Любопытство, Нацуки."
    show yuri e1d
    show libitina cm
    n "Коха, это ты её притащила?"
    show libitina forward happ cm ce
    show kotonoha om rhip
    k "Это её личное желание вообще-то."
    show kotonoha happ om ce
    k "Наблюдать же никто не запрещает, не правда ли?"
    show kotonoha cm
    "Это называется «нарушение личного пространства»!"
    show yuri anno cm e1a
    show libitina oe
    show kotonoha neut cm oe
    n "Вы у нас над душой стоять будете."
    show kotonoha om
    k "Совершенно нет."
    show libitina om
    show kotonoha happ cm oe
    l "Угу, мы вам не помешаем."
    show libitina cm
    show kotonoha ce
    n "Тц!"
    "Да что за издевательство?!"
    "Этот стих начинает превращаться в эпопею!"
    show yuri om
    show kotonoha oe
    y "Нацуки..."
    y "Тебя это не должно волновать."
    show yuri neut om e1d lup
    y "Наша задача -- стихотворение."
    show yuri cm ldown
    n "Правильно!"
    show yuri anno cm e1a
    n "И чем более комфортные условия будут, тем лучше мы его составим."
    show yuri om
    show libitina ce
    y "Они и так на достаточном уровне."
    show yuri cm
    n "......"
    "Я просто не хочу, чтобы на нас смотрели!"
    show yuri oe
    show kotonoha e1b
    "И так со скрипом согласилась на Котоноху..."
    show libitina oe
    "Но нет, ещё Либитина припёрлась."
    show yuri neut cm e1b at thide
    hide yuri
    show libitina neut cm oe
    "С чего вдруг ей стало интересно наблюдать за написанием стихов?"
    "Она всегда держалась в стороне от всего этого."
    show kotonoha oe
    y "Давай не будем терять время."
    show libitina happ cm oe
    y "Садись сюда, рядом со мной."
    y "А вы можете с другой стороны."
    show kotonoha om
    k "Да, как скажешь."
    show libitina ce at thide
    hide libitina
    show kotonoha cm rdown at thide
    hide kotonoha
    "Да почему...{w}я чувствую слабость..."
    "Я смущаюсь!"
    "Я не готова!"
    "Но нельзя подавать вид, нельзя..."
    "Иначе ничего не выйдет."

    call poem_act_1_day_10_ny

    scene bg school library
    show yuri shy angr cm oe at s31
    show natsuki cross fta at t32
    show libitina forward neut cm oe at t33
    with dissolve
    pause 0.25
    k "БРЭЙК!"
    show yuri e2
    k "Успокойтесь..."
    k "Иначе нас выгонят из библиотеки."
    show yuri ce
    show libitina om eb
    l "{size=19}Говорите за себя...{/size}"
    show libitina happ cm oe
    k "Даже не думай увильнуть, Либитина."
    show libitina shy happ om ce
    l "Ха-ха-ха!"
    show yuri neut cm ce
    show libitina cm
    "Ей совершенно фиолетово на конфликт?"
    show yuri oe
    show natsuki fs neut cm oe
    show libitina oe
    k "Кхм."
    show yuri angr cm oe
    show natsuki ce
    show libitina forward neut cm oe
    k "Неужели вы НАСТОЛЬКО сильно ненавидите стили друг друга?"
    show yuri e2
    ny "..."
    show libitina om
    l "Тут это и так очевидно."
    show libitina cm
    k "Но почему?"
    show libitina om
    l "Почему очевидно?"
    show libitina cm
    k "Нет, не это..."
    show libitina happ cm ce
    k "Агх, Либитина!"
    show libitina om
    l "Всё, молчу."
    show yuri neut cm e3
    show natsuki oe
    show libitina cm
    k "Юри, Нацуки, почему это происходит?"
    show yuri oe
    show natsuki ce
    show libitina neut cm oe
    k "Разве вы не можете прийти к какому-то...{w}консенсусу?"
    show yuri om ce
    show natsuki om
    show libitina happ cm oe
    ny "...с ней невозможно договориться."
    show yuri cm
    show natsuki cm
    k "{size=19}Вы друг друга точно стоите...{/size}"
    show yuri e3
    show natsuki oe
    k "Тогда давайте с холодной головой разберёмся в вашей проблеме."
    show yuri turned neut cm e1d at t31
    show natsuki turned ff anno cm oe lhip rhip
    show libitina shy happ om oe
    l "Оу, вот это уже поинтереснее, чем просто написание стиха."
    show libitina cm
    k "Почему ты такая весёлая?"
    show yuri anno cm oe
    show libitina forward happ om oe
    l "Настроение хорошее."
    show libitina cm
    k "Ну и ну..."
    "Истинный девиант..."
    show yuri neut cm e1d
    show natsuki neut cm oe ldown rdown
    k "Итак, приступим."
    show libitina neut cm oe
    k "Сначала выскажется Юри, а потом ты, Нацуки."
    k "Далее уже вместе будем думать."
    show natsuki dist om ce
    n "Угу-угу."
    show natsuki cm
    k "Юри, давай."
    show yuri e1c
    show natsuki neut cm oe
    k "Только не бойся."
    show yuri e1d
    k "Сейчас главное, чтобы вы всё полностью излили и решили раз и навсегда."
    show yuri anno cm oe
    y "...м-м..."
    show yuri dist om ce lup rup
    show natsuki curi cm oe
    y "Пу-у-уф..."
    show yuri flus om oe ldown rdown
    y "Как вы уже могли слышать...{w}я ненавижу в самой Нацуки и в её стиле несколько вещей..."
    show yuri dist om oe
    show natsuki angr cm oe
    show libitina shy neut cm oe
    y "Первая -- он слишком простой."
    show yuri angr cm oe
    show natsuki om lhip rhip
    n "Так это его особенность!"
    show natsuki cm
    show libitina forward neut cm oe
    k "Тихо-тихо!"
    show yuri neut cm e1d
    show natsuki anno cm oe
    k "Комментарии потом, после ваших высказываний, хорошо?"
    show natsuki ce
    n "Мпф..."
    show yuri om
    y "...вот, простота."
    show yuri dist om oe
    y "Прошло уже достаточное количество времени, за которое можно было бы значительно развить свой стихотворный талант, но..."
    show yuri anno om oe
    show natsuki oe
    y "...Нацуки ничего не сделала."
    show yuri neut om e1d
    show natsuki e1b b1d ldown rdown
    y "Я уже не раз об этом с ней говорила, но она меня не слушает."
    show yuri angr om oe
    show natsuki oe -b1d
    y "Из этого вытекает вторая вещь -- упрямость и упёртость."
    show yuri e1b
    show natsuki neut cm oe
    y "Конечно, я могу предположить, что такое поведение -- защитный механизм из-за личных проблем..."
    show yuri ce
    show natsuki anno cm e1b b1d
    show libitina shy neut cm oe
    y "...однако иногда это приобретает неуместный характер."
    show yuri neut om e1d
    y "Иными словами, перегибает палку."
    show yuri dist om oe
    y "Пока как-то так..."
    show yuri cm
    l "Хм-м-м..."
    show yuri neut cm e1d
    k "Хорошо, мы тебя услышали."
    show natsuki neut cm oe -b1d
    show libitina forward neut cm oe
    k "Теперь ты, Нацуки."
    show yuri anno cm e1a
    show natsuki angr om ce lhip rhip
    n "Во-первых, я ненавижу её прототип СПГС, который ложится абсолютно в каждом стихе такими «извилистыми» словами и строфами, что читать становится тяжело."
    show natsuki neut cm oe
    show libitina om
    l "Синдром поиска глубинного смысла?"
    show natsuki om
    show libitina cm
    n "Да."
    show natsuki curi om e1b
    n "Прототип в том смысле, что не поиск, а закладывание..."
    show natsuki cm
    k "Да, понятно."
    show yuri angr cm oe
    show natsuki anno om ce
    n "Во-вторых, навязывание."
    show yuri ce
    show natsuki curi om oe
    n "Почему нельзя оставить меня в покое?"
    show yuri om
    show natsuki angr cm oe
    y "Потому что ты сама начинаешь выкаблучиваться."
    show yuri cm
    show natsuki om
    show libitina angr cm oe
    n "Я выкаблучиваюсь?!"
    show natsuki cm
    show libitina om
    l "Тихо!"
    show libitina cm
    "Плохо дело, на нас уже библиотекарь засматривается..."
    show yuri oe
    show natsuki ce
    k "Так, поспокойнее."
    show libitina neut cm oe
    k "Нацуки, продолжай."
    show natsuki mh ce
    n "Навязывание..."
    show natsuki om oe
    n "У каждого свой стиль."
    n "Каждый пишет свои стихи."
    n "Но Юри лезет лишь ко мне."
    show yuri om
    show natsuki angr cm oe
    y "Я только что озвучивала, почему это происходит."
    show yuri cm
    show natsuki om
    show libitina angr cm oe
    n "Да помолчи!--{nw}"
    show natsuki cm
    show libitina om at h33
    l "Цыц!"
    show yuri neut cm e1d
    show libitina cm
    k "О нет..."
    show libitina neut cm oe
    "Пора отсюда ретироваться!"
    show yuri b1f
    show natsuki curi cm oe
    k "Что-то у меня аппетит разыгрался, ха..."
    show libitina shy neut cm oe
    k "А у меня, кстати, с собой шесть вкусных онигири с креветками."
    k "Не хотите попробовать?"
    show natsuki om
    n "...а?"
    show yuri -b1f
    show natsuki cm
    show libitina forward neut cm oe
    k "Пойдёмте на крышу, я вас угощу."
    k "Давайте-давайте-давайте~"
    show libitina om
    l "А, ага..."
    show yuri vsur cm oe lup rup at h31
    show natsuki lsur cm oe
    show libitina angr om oe
    l "{size=19}ВСЕМ ЖИВО НА КРЫШУ!!!{/size}" with vpunch
    show libitina cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 wind fadein 3.0
    scene bg school old_rooftop day
    show yuri turned neut cm e1b school_bag at t31
    show natsuki turned dist cm oe school_bag at t32
    show libitina forward neut cm oe at t33
    with wipeleft_scene
    k "Фу-у-ух..."
    show libitina om
    l "Вовремя."
    show libitina cm
    k "Ага..."
    show yuri e1d
    show natsuki neut cm oe
    show libitina shy neut om eb
    l "И не лень же было нас вести в старый корпус..."
    show libitina cm
    k "Здесь мало кто бывает."
    show libitina forward neut om oe
    l "Ладно..."
    show yuri e1c
    show natsuki curi cm oe rhip
    show libitina happ om oe
    l "Где мой онигири?"
    show libitina neut cm oe
    k "Ой, потерпи!"
    show libitina sad om ce
    l "Тю, так неинтересно..."
    show yuri e1d
    show natsuki pout cm oe
    show libitina cm
    k "Нацуки, ты же всё сказала?"
    show natsuki e1b
    show libitina neut cm oe
    n "У-у..."
    show natsuki om
    n "Вроде бы..."
    show natsuki cm
    n "..."
    show natsuki neut om oe rdown
    n "Да, больше нечего добавить."
    show natsuki cm
    k "...хорошо."
    k "Итак, стороны выслушаны."
    show libitina shy neut cm oe
    k "Дайте подумать..."
    "М-м-м-м-м..."
    show yuri e1b
    "Простой стиль и упрямство с одной стороны..."
    show natsuki e1c
    "Сложный стиль и навязывание с другой..."
    show libitina forward neut cm oe
    "Противоречивые характеры..."
    "Далеко не первый конфликт..."
    show yuri e1d
    show natsuki oe
    k "Угу."
    show yuri curi cm oe
    show natsuki curi cm oe
    k "Теперь более-менее понятно."
    show libitina shy neut cm oe
    ny "???"
    show yuri neut cm e1d
    show natsuki neut cm oe
    show libitina forward neut cm oe
    k "Вам нужно принять друг друга такими, какие вы есть."
    show yuri anno cm oe n2
    show natsuki pout cm e2a n2
    ny "..."
    "Звучит просто, но необходимо."
    k "Да, я понимаю, в вас сейчас много противоречий, которые вы дико недолюбливаете..."
    k "Но, во-первых, ваши противоречия являются вашими же особенностями, которых вы не хотите лишаться."
    show libitina happ cm oe
    k "Отсюда следует «во-вторых»: ваши конфликты решатся только тогда, когда вы примите себя."
    k "Если вы это не сделаете, то ссоры на этой почве будут происходить постоянно."
    show yuri ce
    show natsuki e2b
    show libitina om ce
    l "Я, например, приму онигири таким, какой он есть!"
    show libitina oe
    l "Котоноха, где он?"
    show natsuki e2a
    show libitina cm
    k "Прожора!"
    show libitina shy happ om oe
    l "Интересное замечание от человека, у которого с собой целых шесть таких онигири."
    show libitina cm
    k "Кхм..."
    show yuri om
    show libitina forward happ cm oe
    y "Принять..."
    show yuri cm
    n "..."
    show yuri neut cm e1d n1
    k "Юри, ты же говорила, что надо развиваться...{w}что-то в таком духе, верно?"
    show yuri om
    y "Да."
    show yuri cm
    k "Принятие как раз станет одной из ступенек вашего развития."
    show yuri doub cm oe
    show natsuki e2c
    k "И этот факт никак не изменить."
    y "..."
    k "Как только это произойдёт, вы обретёте, хоть и не гармонию, но некое спокойствие точно."
    show natsuki e2a
    k "А ещё это поможет укрепить дружескую связь."
    show yuri neut cm e1d
    show natsuki om n4
    n "...я..."
    show yuri angr cm oe
    show natsuki angr om oe lhip rhip n1
    show libitina neut cm oe
    n "...не могу принять Юри, пока она будет придерживаться своей позиции!"
    show yuri om
    show natsuki cm
    y "Кто сказал, что так будет?"
    show yuri e1b
    y "Если ты перестанешь сопротивляться, то я..."
    show yuri neut om e1d
    y "...ну да."
    show yuri cm
    show natsuki cross angr om oe school_bag
    n "\"Ну да!\""
    show yuri vang cm oe
    n "А если ты не ответишь за свои слова?!"
    show yuri cm ce
    show natsuki cm
    y "{sc=1}Кх-х-х, Нацуки, ты...{/sc}"
    show yuri om oe at h31
    show natsuki turned vang cm oe school_bag
    y "{sc=3}Клочок ярости!{/sc}" with vpunch
    show yuri cm
    "..."

    if persistent.add_random_menu == 11:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    play music t8 fadein 3.0
    show yuri yand cm ce
    show natsuki laug cm ce
    show libitina happ om ce
    kl "Ха-ха-ха-ха-ха!"
    show yuri om
    show natsuki om lhip rhip
    show libitina cm
    ny "Ха-ха-ха!"
    show yuri cm
    show natsuki cm
    show libitina om
    l "\"Клочок ярости\"."
    show yuri laug cm ce
    show natsuki mb
    show libitina shy happ om eb
    l "Звучит..."
    show yuri happ cm ce
    show natsuki happ cm ce
    show libitina cm
    k "Да..."
    show yuri om
    show libitina ce
    y "Ох..."
    show yuri cm
    show natsuki mb
    show libitina forward happ cm ce
    n "Фу..."
    show yuri oe
    show natsuki cm ldown rdown
    show libitina oe
    k "Ну так что?"
    show yuri neut cm e1d n2
    show natsuki neut cm oe n2
    k "Вы примите друг друга такими, какие вы есть?"
    show yuri flus md oe
    show natsuki sad cm e1c
    ny "..."
    "Ну же...{w}давайте..."
    show yuri ce
    y "Умпф..."
    show natsuki oe
    n "......"
    show yuri e2a
    show natsuki e1a
    y "..."
    show yuri pani cm ce n4
    show natsuki pout cm oe
    show libitina neut cm oe
    y "{sc=2}...........{/sc}"
    show yuri om e4c at h31
    show natsuki shoc cm oe
    y "{sc=2}Я принимаю тебя такой, какая ты есть, Нацуки,\nвне зависимости от твоих интересов!{/sc}"
    show natsuki n4
    show libitina happ cm oe
    y "{sc=2}Ты была, есть и будешь моей лучшей подругой!{/sc}"
    show yuri cm
    n "A..."
    show yuri mj
    show libitina om
    l "Ого..."
    show libitina cm
    "Ничего себе..."
    show natsuki om ce
    n "Я...{w}тоже...{w}да..."
    show yuri lsur om ce n3
    show natsuki cm
    show libitina ce
    k "Ура!"
    show yuri cm
    show natsuki pani cm ce
    show libitina om
    l "Как это миленько~"
    show natsuki om oe
    show libitina cm oe
    n "М-миленько?!"
    show natsuki cm
    show libitina shy happ cm oe
    l "Угу!"
    show natsuki fs neut om oe n5
    n "Апф!"
    show yuri oe
    show natsuki m2
    show libitina ce
    k "Что ж, поздравляю вас!"
    show libitina forward happ cm oe
    k "Теперь, если вы и впредь будете придерживаться этих слов, то сможете обходить подобные конфликты стороной."
    show yuri e2b
    show natsuki ff pout om e1b n1
    n "Надеюсь..."
    show natsuki cm
    show libitina om
    l "Я так понимаю, всё?"
    show natsuki neut cm oe
    show libitina cm
    k "Наверное."
    show yuri neut cm e1d n1
    show natsuki om lhip rhip
    show libitina neut cm oe
    n "Мы ещё стих не закончили."
    show natsuki cm
    k "Тогда дописывайте."
    show natsuki ldown rdown
    k "Только дайте я «обозначу разграничение», чтобы части «до» и «после» не слились."
    show yuri e1b
    show libitina angr cm oe
    n "Угу."
    show yuri e1d
    show natsuki curi cm oe
    show libitina om
    l "Так, эй!"
    show yuri happ cm oe
    show libitina happ om oe
    l "Мой онигири?"
    show natsuki neut cm oe
    show libitina cm
    k "А-а-а, точно."
    k "Где-то тут они у меня завалялись..."
    show yuri om lup
    y "И нам...{w}можно?"
    show yuri cm
    show natsuki happ cm oe
    k "Конечно!"
    show yuri ldown
    k "Хм-хм-хм..."
    k "А вот и она, «примирительная» еда!"
    call window_close

    stop music fadeout 0.5
    play music_none_loop oops
    show flattened_onigiri with dissolve
    pause 0.25
    show yuri neut cm e2a
    show natsuki curi cm oe
    show libitina neut cm oe
    pause 1.5

    call window_open
    k "У-у..."
    k "Утром они не были такими спрессованными..."
    call window_close

    play sound none_transition
    stop noise_1

    call window_dialog_long_transition("mc", transition = False)

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    mc "Их, ах..."
    "Затёк весь..."
    "Кстати, почему у меня вошло в привычку выходить последним из класса, не считая учителя?"
    "Вроде бы всегда вылетал при первой же возможности..."
    "Хотя есть ли смысл теперь спешить, когда ты привязан к Литературному клубу?"
    "Так, стоп, я стих взял?"
    "..."
    "......"
    "Вот он, на месте."
    mc "Фу-у-ух..."
    "Я уж думал, что он потерялся..."
    "Сегодня совершенно не мой день."
    "Тумбочка, отсутствие Сайори, ещё голова утомилась..."
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Снова в клуб, да?"
    show mrs_ida cm
    mc "А куда ж ещё?"
    show mrs_ida om
    mi "И то правда."
    show mrs_ida cm
    "Честно, абсолютно нет никакого желания поддерживать этот разговор."
    show mrs_ida neut cm oe
    "Надо как-то аккуратно извернуться..."
    mi "Хм..."
    mc "???"
    show mrs_ida om ce
    mi "Знаешь, Макс, может, твоя проблема с социумом кое-как решилась, что, конечно, не может не радовать..."
    "Ладно, фиг мне, а не изворот."
    show mrs_ida oe
    mi "...но боюсь, что у тебя стала проявляться новая."
    show mrs_ida cm
    mc "...что?"
    "Спасибо за порцию адреналина, без шуток."
    "Аж взбодрился."
    mc "Какая?"
    show mrs_ida om
    mi "Ты «прыгаешь» из крайности в крайность."
    show mrs_ida cm
    mc "Крайности?"
    show mrs_ida om
    mi "Я имею в виду, что один день ты словно на шарнирах, а другой...{w}как сейчас убитый."
    mi "Первое время, то есть до клуба, ты был более-менее стабильным, хоть и немного пессимистичным."
    mi "Но после вступления ты стал меняться каждый день, и я говорю не про появление друзей и отношений."
    show mrs_ida ce
    mi "Меня подобное совсем не радует."
    mi "Если такая тенденция сохранится, то, к сожалению, это будет иметь плохие последствия."
    show mrs_ida cm oe
    mc "Что-то из разряда расстройства личности?"
    show mrs_ida om
    mi "Именно."
    show mrs_ida happ om oe
    mi "Но, может быть, ты просто ещё не втянулся?"
    mi "Забот стало на порядок больше, взаимосвязей...{w}и Моника ещё, да?~"
    show mrs_ida neut cm oe
    mc "Не знаю..."
    mc "Но я тоже заметил за собой нечто подобное."
    show mrs_ida om
    mi "Что ж, будем надеяться, что это временное явление."
    mi "Пока ещё рано о чём-либо говорить."
    show mrs_ida happ om oe
    mi "Однако если что, то сразу обращайся, хорошо?"
    show mrs_ida cm
    mc "Конечно."
    show mrs_ida at thide
    hide mrs_ida
    pause 0.2
    "..."
    "Хм, интересно..."
    mc "У меня к Вам вопрос, Ида-сэнсэй."
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Да?"
    show mrs_ida cm
    mc "Почему Вы так беспокоитесь за меня?"
    mc "У нас тут целый класс в ~30 человек со своими причудами, а я...{w}даже близко не в центре всей этой «массы»."
    show mrs_ida om
    mi "Ты же ведь к нам недавно пришёл."
    mi "Сам класс довольно дружный и тихий."
    mi "К слову, один из приятных."
    mi "Все уже уверенно держатся друг за друга, потому что давно знакомы, несмотря на постоянную перетасовку каждый учебный год."
    mi "А ты новенький в этом месте."
    show mrs_ida neut om oe
    mi "И ещё почему-то класс тебя особо не принимает, что странно."
    show mrs_ida cm
    mc "Они хотя бы уважительно ко мне относятся."
    show mrs_ida sad om oe
    mi "В любом случае этого недостаточно."
    mi "Мы же люди -- существа социальные."
    mi "В одиночку очень тяжело жить."
    show mrs_ida happ om oe
    mi "Именно поэтому я и решила помочь тебе хоть каким-нибудь образом."
    show mrs_ida cm
    mc "Ясненько..."
    show mrs_ida ce
    mc "Спасибо за это, Ида-сэнсэй."
    show mrs_ida om
    mi "Что ты, это мой долг, как классного руководителя, -- следить за учениками под моим попечением."
    show mrs_ida cm
    "Как-то даже полегече стало...{w}но утомление никуда не делось."
    show mrs_ida oe
    mc "Пойду в клуб, не буду терять время."
    show mrs_ida om ce
    mi "Удачи!"
    show mrs_ida cm

    scene black with wipeleft_scene
    "Прямо как вчера, когда домой практически вернулся: ноги слегка подкашиваются, в глазах немного плывёт..."
    "Блин, обязательно, когда дойду до клуба, отсижусь рядом с открытым окном, пока в норму не приду."
    call window_close

    call plot_transition

    call window_open
    scene bg corridor
    show layer master at stress(0.5, 2)
    with wipeleft_scene
    mc "{bt=3}Я ща сдохну...{/bt}"
    "{bt=3}Что-то мне...{w}реально поплохело...{/bt}"
    "{bt=3}Вспотел так, будто стометровку пробежал за\nпару секунд...{/bt}"
    "{bt=3}...{/bt}"
    mc "{bt=3}Ф-ф-ф...{/bt}"

    scene black with wipeleft_scene
    "{bt=3}Дверь...{/bt}"
    "{bt=3}Открыть дверь...{/bt}"
    call window_close

    pause 1.0
    play sound closet_open
    pause 1.0

    call window_open
    m "Ах, привет, Макс!"
    mc "{bt=3}П-привет...{/bt}"
    "{bt=3}Моника первая в кои-то веки?...{/bt}"
    "{bt=3}Ай, голова кружиться начала...{/bt}"
    "{bt=3}Чё-ё-ёрт, сейчас же Мони начнёт волноваться...{/bt}"
    m "Что-то ты неважно себя чувствуешь..."
    mc "{bt=3}В порядке!{/bt}"
    mc "{bt=3}Я...{/bt}"
    m "Ладно, отдохни пока в классе, я как раз решила его проветрить."
    mc "{bt=3}Оке-е-ей...{/bt}"
    m "Мне надо Сайори встретить, чтобы окончательно со стихом разобраться."
    m "Поэтому мы с ней можем немножко задержаться."
    m "Ой, прямо рифма получилась, ха-ха-ха!"
    mc "{bt=3}П-понял...{/bt}"
    m "Всё, я побежала, восстанавливай силы!"
    mc "{bt=3}Ага...{/bt}"

    scene bg school literature_club board day
    show layer master at stress(0.5, 2)
    with wipeleft_scene
    "{bt=3}Очень...{w}хорошо...{/bt}"
    "{bt=3}Воздух...{/bt}"
    "{bt=3}Тишина...{/bt}"
    mc "{bt=4}Пф-ф-ф...{/bt}"
    show layer master at stress(1, 1)
    with dissolve
    "{bt=5}Тошнота...{/bt}"
    "{bt=5}......{/bt}"
    "{bt=4}Тихо-тихо...{/bt}"
    show layer master at stress(0.5, 2)
    with dissolve
    "{bt=3}Тихо...{/bt}"
    "{bt=3}Уши гудят...{/bt}"
    "{bt=4}......{/bt}"

    scene n_cg1_bg
    show layer master at stress(0.25, 2)
    with dissolve_cg
    mc "{bt=4}Уф-ф-ф...{/bt}"
    "{bt=3}Хорошо присел на пол...{/bt}"
    mc "{bt=3}Фу-у-у...{/bt}"
    "{bt=3}Отдых...{/bt}"
    "{bt=4}Блин...{/bt}"
    "{bt=4}Даже стена размазывается...{/bt}"
    "{bt=3}Успокойся...{/bt}"
    "{bt=2}Успокойся......{/bt}"
    stop noise_1 fadeout 3.0
    call window_close

    call nightmare_act_1_day_10_1
    $ _history_list.clear()

    call window_open
    play noise_1 school_corridor_empty_noise
    scene bg closet
    show natsuki turned pani cm ce at face zorder 2
    show natsuki mp at tfast
    with vpunch
    n "{sc=3}А-А-А, МОЙ ЛОБ!{/sc}"
    show natsuki om
    n "Дурак, ты что творишь?!"
    show yuri turned vsur om oe at l21
    show natsuki cm
    y "Н-Нацуки, ты в порядке?!"
    show sayori turned sad cm e2d at l41 zorder 2
    show monika forward lsur om oe at l42
    show natsuki oe at t43
    show yuri cm at t44
    m "Что случилось?!"
    show sayori om
    show monika cm
    s "Макс?..."
    show sayori cm
    show monika md
    show natsuki om
    show yuri lsur cm oe
    n "Вот что!..."
    show sayori oe
    show natsuki lhip rhip
    "..."
    show sayori neut cm oe
    show natsuki ce
    "......"
    show sayori curi cm oe
    show monika curi cm oe
    show yuri lup rup
    "Я только что врезал Нацуки со всей дури?"
    show natsuki oe
    "Из-за кошмара."
    show monika neut cm oe
    show natsuki cm
    show yuri ldown rdown
    "С её же образом."
    show natsuki pout cm oe
    "..."
    show natsuki ldown rdown
    "Почему...{w}я не могу понять причину моих кошмаров?"
    show natsuki om
    n "Эй!"
    show natsuki cm
    mc "А?!"
    show yuri om
    y "Ч-что на тебя нашло?..."
    show sayori om
    show monika dist cm oe
    show yuri cm
    s "Тебя что-то беспокоит?"
    show sayori cm
    show monika om
    m "{size=19}Макс...{w}такими темпами тебе самому понадобится психолог...{/size}"
    show sayori neut cm oe
    show monika neut cm oe
    mc "{sc=3}А-а-а, тихо, стойте!{/sc}" with vpunch
    mc "Стоп!"
    show natsuki curi cm oe
    mc "По порядку..."
    show natsuki pout cm e2d
    show yuri neut cm e1d
    mc "Что я сделал?"
    show natsuki pani om ce
    n "Влупил мне!"
    show monika om lpoint
    show natsuki mj
    m "Ты уснул, сидя на полу у стены, помнишь?"
    show monika cm ldown
    show natsuki pout cm oe
    mc "Да."
    show natsuki om
    n "...потом я пришла, никого ещё не было."
    show natsuki e1b
    n "Села рядом на своё любимое место и стала читать мангу от скуки, пока все собирались."
    show natsuki oe
    n "А дальше -- вот {b}это{/b}!"
    show natsuki cm
    mc "Манга..."
    "Получается, не было ни того блевотного томика, ни розыгрыша Нацуки...{w}да?"
    show sayori e2a
    show monika curi md oe
    show natsuki neut cm oe
    show yuri curi cm oe
    mc "Какая у тебя манга в той лимитированной коробке?"
    show natsuki curi om oe
    n "...чего?"
    show natsuki lhip rhip
    n "Это тут причём?"
    show sayori oe
    show monika neut cm oe
    show natsuki cm
    mc "Ты мне показывала её?"
    show natsuki om e1b
    n "Нет..."
    show natsuki pout cm oe
    mc "Так что в ней есть?"
    show yuri neut cm e1d
    mc "Ну там жанр: хоррор, ужастик, прочее..."
    show sayori curi cm oe
    show natsuki pani om oe
    n "Да что с тобой такое?!"
    n "Что за вопросы?!"
    show natsuki cm
    mc "Чёрт побери..."

    scene black with dissolve
    pause 0.25
    n "Эй, не надо там копошиться!"
    mc "Мне нужна эта коробка, чтобы убедиться в одной важной детали."
    "Коробка-коробка-коробка...{w}в виде полки..."
    "Вот она."
    n "Стой, я сама всё аккуратно в правильном порядке вытащу!"
    mc "Хорошо-хорошо, только покажи хотя бы один том!"
    n "Да успокойся!"
    n "Так..."
    n "Это всё из одной вселенной."
    n "Вот, любуйся."
    n "Только не повреди!"
    "..."
    "......"
    "Это...{w}совершенно не то, что я видел."
    "Здесь какая-то семья с большой белой собакой на обложке."
    "А сюжеты тут «адекватнее», за исключением моментов каких-то перестрелок с закосом под шпионов..."
    "Никакой хоррор-составляющей в манге не вижу..."
    "Да и по временной линии это похоже на 80-ые года, а не на современность, которая там была."
    mc "Ясно."
    n "Что?"
    mc "Можешь убирать."

    scene bg closet
    show sayori turned neut cm oe at t41 zorder 2
    show monika forward neut cm oe at t42
    show yuri turned neut cm e1d at t22 zorder 2
    with dissolve
    pause 0.25
    show sayori curi cm oe
    show monika worr cm e1a
    show yuri shoc md oe
    mc "Я официально заявляю, что я еду крышей."
    show yuri mk lup rup at h22
    y "Э?!"
    show yuri md
    n "{size=19}ПФ!{/size}"
    show sayori om
    s "В смысле..."
    show sayori cm
    show monika oe
    m "..."
    show sayori neut cm oe
    show yuri ldown rdown
    mc "В прямом, Сайори."
    show sayori om
    show yuri lsur cm oe
    s "Но почему?"
    s "Расскажи, если не секрет."
    show sayori cm
    mc "Эх..."
    "Как же...{w}не хочется этого делать..."
    "Не разболтают, а?"
    "Но если так подумать..."
    "Зачем мне об этом молчать?"
    "Хуже же станет."
    show monika e1a
    show yuri neut cm e1d
    mc "Хорошо."
    mc "Я расскажу..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg closet
    show sayori turned curi cm oe at i41 zorder 2
    show monika forward worr cm oe at i42
    show natsuki turned pout cm oe lhip rhip at i43 zorder 2
    show yuri turned anno cm oe at i44
    with wiperight
    "Естественно, что прошлые кошмары я немного переврал."
    "Кошмар с Моникой, потому что обнажёнка."
    "Кошмар с Юри, потому что...{w}попытка насильственного совокупления."
    "Это даже звучит бредово, кто это будет слушать?"
    "Не хватало, чтобы меня извращенцем заклеймили за воображение во сне, которое я контролировать не могу."
    m "..."
    show natsuki om
    n "Да у тебя реально крыша едет."
    show sayori e1a
    show natsuki cm
    mc "О чём и говорю."
    show sayori om
    show monika neut cm oe
    show natsuki ldown rdown
    show yuri curi md e1d
    s "Ты не знаешь, с чем это может быть связано?"
    show sayori cm
    mc "Без понятия."
    "Однако..."
    show sayori neut cm oe
    show yuri neut cm e1d
    mc "Ха..."
    show sayori b1d
    show natsuki curi cm oe
    mc "Всегда перед кошмарами я ощущал дикую усталость."
    "Серьёзно."
    "Я как-то это раньше не подмечал."
    show sayori om
    show monika dist cm oe
    show natsuki anno cm oe
    s "Вот, это точно закономерность!"
    show sayori cm -b1d
    show natsuki om
    n "И что?"
    show natsuki neut om oe lhip rhip
    show yuri anno cm oe
    n "Когда ты убитый, мозг перегружается и не может контролировать мысли."
    show natsuki pout om e1b
    n "В эти моменты в голову лезет всякое..."
    show natsuki md
    mc "М-мда..."
    show monika om ce
    show natsuki neut cm oe
    show yuri neut cm e1d
    m "Нам этот факт взаимосвязи ничего не даёт."
    show sayori e1b
    show monika worr om oe
    show natsuki ldown rdown
    m "Тут не обойтись без помощи квалифицированных специалистов."
    show monika cm
    "Да я тебя понял, Моника, понял!"
    show natsuki e1c
    "Сегодня ещё раз буду пытаться найти этого психолога."
    "И завтра."
    "И послезавтра..."
    show sayori sad md oe
    show monika e1a
    show natsuki oe
    show yuri lsur cm oe
    mc "В общем, я больной на всю голову и ничего не могу с этим сделать."
    show monika om
    show natsuki dist cm oe
    m "Макс, не говори так."
    show sayori om lup rup at h41
    show monika ma
    s "Ты обязательно сможешь, мы тебе поможем!"
    show sayori md ldown rdown
    show monika mb
    m "Да!"
    show monika ma
    show yuri e2b
    mc "...спасибо за поддержку, но как?"
    show sayori worr cm oe
    show monika cm oe
    ms "..."
    show natsuki neut cm oe
    y "Ум-м..."
    show sayori sad md oe
    show yuri om oe
    y "Не грузись, Макс..."
    show monika e1a
    y "Ты не один..."
    show sayori worr cm ce
    show yuri cm
    mc "Мне легче от этого факта не становится."
    show yuri om
    y "Я-я имела в виду..."
    show sayori neut cm oe
    show natsuki curi cm oe
    show yuri flus cm oe lup at s44
    y "Э-э-э..."
    show monika neut cm oe
    show yuri om e1a
    y "...что ты не одинок в изъянах..."
    show yuri cm
    call window_close

    pause 0.2
    show yuri at t44
    pause 0.2
    show natsuki nerv md oe
    show yuri rbandages with dissolve_cg
    pause 0.6

    call window_open
    "...охренеть..."
    show yuri oe
    "...она нашла в себе силы раскрыть это всем...{w}хоть все тут и так в курсе..."
    show monika e2a
    show yuri e2a
    mc "...стой, ты снова себе вред нанесла?"
    show monika oe
    show yuri om
    y "Нет!"
    show yuri cm oe
    y "Это...{w}это ещё прошлые бинты..."
    show natsuki pout cm oe
    show yuri lsur om oe
    y "Но почему Сайори такая...{w}спокойная?"
    show sayori anno cm oe
    show yuri e2b
    y "Она же ведь не в курсе..."
    show sayori om
    show natsuki shoc md oe
    show yuri cm oe
    s "Я всё знаю."
    show sayori angr om ce
    show monika dist cm oe
    s "И очень плохо, Юри, что ты решила умолчать о таком!"
    show sayori cm
    show yuri om
    y "Н-но откуда?!..."
    show sayori om oe
    show yuri cm
    s "Вот оттуда!"
    show monika neut cm oe
    show natsuki pani cm oe at h43
    s "И Нацуки ничего не сказала!"
    show sayori anno om oe
    s "Ты же ведь знала, да?"
    show sayori cm
    show natsuki om ce
    n "АГХ..."
    show natsuki pout om e4a
    show yuri e2b
    n "...а-а-ай."
    show sayori neut cm oe
    show monika curi md oe
    show natsuki oe lhip rhip
    n "Я не хотела выбивать Юри из колеи разбалтыванием её проблемы."
    show monika om
    show natsuki cm
    m "И поэтому ты всё время молчала?"
    show monika md
    show natsuki e1b
    n "..."
    show yuri nerv cm oe
    show natsuki om
    n "Ну я хотела об этом рассказать, Юри -- нет."
    show sayori anno cm oe
    show monika angr cm oe
    show natsuki e4a ldown rdown
    n "Да и теперь не думаю, что что-то от этого поменяется."
    show natsuki cm
    show yuri ce
    y "...простите..."
    show sayori angr om oe
    show monika neut cm oe
    show natsuki oe
    show yuri lsur cm oe
    s "Так, Юри, руки на стол!"
    show sayori ce
    s "Я должна их осмотреть!"
    show sayori cm
    show yuri om
    y "Ч-что?"
    y "Зачем?--{nw}"
    show sayori oe at t44 zorder 3
    show yuri flus cm e2a lup at h44
    y "Э-э-э, Сайори?!"
    show sayori om
    s "Пошли, давай-давай-давай!"
    show sayori cm at thide
    show yuri md at thide
    hide sayori
    hide yuri
    show monika at t21
    show natsuki at t22
    pause 0.2
    y "{size=19}Только не снимай бинты, пожалуйста...{/size}"
    show monika angr om oe
    show natsuki curi cm oe
    m "...нет, Нацуки, ещё как поменяется!"
    show monika ce
    show natsuki angr cm oe
    m "Ведь знание -- это половина победы."
    show monika cm
    show natsuki om lhip rhip
    n "Я ничего не смогла сделать с проблемой Юри на протяжении всего времени, что я её знаю!"
    show monika anno cm oe
    n "Будто вы что-то сможете!"
    show natsuki cm
    s "{size=19}Какой же это ужас!{/size}"
    mc "Да, сможем."
    show natsuki curi cm oe
    mc "И мы уже этим занимаемся."
    show monika neut cm oe
    show natsuki om
    n "И что же вы такое решили сделать?"
    show natsuki cm ldown rdown
    mc "Найти психолога, с которым я давно разорвал контакт."
    show natsuki pout om oe
    n "Разорвал контакт?"
    n "И почему?..."
    show natsuki cm
    mc "Нацуки, это дело прошлое."
    show monika happ cm oe
    show natsuki neut cm oe
    mc "Нам нужно думать о будущем."
    mc "И это будущее начинается уже сегодня."
    k "{size=19}Здраствуйте!{/size}"
    y "{size=19}А, привет...{/size}"
    show monika om ce
    m "Привет."
    show monika cm
    show natsuki cm e1b
    s "{size=19}Не крутись, Юри!{/size}"
    y "{size=19}Угх...{/size}"
    show kotonoha neut om oe at l41
    show monika oe at t42 zorder 2
    k "Что с вами случилось?"
    show kotonoha cm
    show monika om e1b
    m "Ну..."
    show monika oe b1b n2 lpoint
    m "Думаю, тебе тоже стоит всё рассказать..."
    show monika cm ldown
    "Чёрт, я сбился с мысли."
    show natsuki oe
    mc "Так, о чём это я?"
    show monika neut cm oe -b1b n1
    show natsuki pout om oe
    n "Мы в дерьме..."
    show kotonoha vsur cm oe
    show monika e2a
    show natsuki cm
    mc "Мы в дерьме!"
    call window_close

    play sound none_transition

    call window_dialog_long_transition(transition = False)

    call window_open
    scene bg school literature_club board day
    show yuri turned worr cm oe at t51
    show natsuki turned dist cm oe at t52 zorder 2
    show monika forward neut cm oe b1b at t53 zorder 3
    show sayori turned anno cm oe at t54
    show kotonoha sad cm oe at t55 zorder 2
    with dissolve_scene_full
    show yuri ce
    show monika e4b n2
    show kotonoha om ce
    k "Как же так..."
    show natsuki neut cm oe
    show monika happ om ce lpoint rhip
    show kotonoha cm
    m "Л-ладно, друзья, хватит."
    show yuri neut cm e1d
    show monika oe -b1b rdown n1
    show sayori neut cm oe
    show kotonoha neut cm oe
    m "Давайте пока на время забудем про проблему Юри и начнём первый обмен совместными стихами."
    show monika cm ldown
    "Ага, а про меня уже успели забыть?"
    show natsuki curi cm oe
    show monika om
    m "Демонстрируем стихотворения сразу перед всеми, поскольку это групповая работа."
    show monika lpoint
    m "Таким образом процесс обмена будет проходить быстрее и объективнее."
    show yuri e1b
    show natsuki e1b
    show monika ce ldown
    show sayori happ cm oe
    show kotonoha happ cm oe
    m "Начинаем!"
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show monika cm at thide
    hide monika
    show sayori ce at thide
    hide sayori
    show kotonoha at thide
    hide kotonoha
    pause 0.2
    "Эй..."
    mc "Моника, а мне тогда каким образом поступать?"
    show monika forward neut mh oe at t11
    m "Ах, точно, ты же пока один..."
    show monika cm
    mc "Мне придётся после вас показывать свой стих всем сразу?"
    show monika happ om oe
    m "Если тебе не будет дискомфортно."
    show monika cm
    mc "Ну, выбирать не из чего..."
    show monika om ce
    m "Хорошо, тогда твоя очередь после всех выступивших пар!"
    show monika cm
    mc "Угу."
    "Перед всеми придётся, значит..."
    "Ну это лучше, чем заставлять весь клуб ждать, подходя к каждой участнице для обсуждения."
    "...под пристальными взглядами остальных."
    show yuri turned neut cm e1d at t51
    show natsuki turned neut cm oe at t52 zorder 2
    show monika om oe lpoint at t53 zorder 3
    show sayori turned happ cm oe at t54
    show kotonoha happ cm oe at t55 zorder 2
    m "Итак, раз я стала инициатором совместных стихотворений, то тогда вместе с Сайори выступлю первой."
    show natsuki nerv cm oe
    show monika ce n2 b1b ldown
    m "Или кто-то из вас хочет?..."
    show yuri e1b
    show natsuki e2c
    show monika oe
    show sayori neut cm oe
    m "Нет?..."
    show monika neut om ce -b1b n1
    show kotonoha ce
    m "Ох..."
    show yuri e1d
    show natsuki ce
    show monika happ om ce
    m "Ясно."
    show natsuki neut cm oe
    show monika e1b
    show kotonoha oe
    m "Для удобства советую...{w}э-э-э..."
    show natsuki curi cm oe
    show monika oe lpoint
    show sayori e2a
    show kotonoha neut cm oe
    m "...зачитать кому-то одному перед остальными."
    show monika ldown
    m "Скажем так, сохраним тенденцию чтения «партнёрами», но при этом немного её расширим..."
    show yuri e2b
    show monika nerv mb oe n2 at s53
    show sayori oe
    m "Как-то у меня слова с трудом вяжутся..."
    show yuri e1d
    show monika cm
    show kotonoha om
    k "Не проще ли прочесть самим авторам?"
    show monika happ om oe n1 at t53
    show kotonoha cm
    m "Возможно кому-то так будет проще, соглашусь."
    show natsuki neut cm oe
    m "Такое тоже можно."
    show yuri happ cm oe
    show monika lean happ om oe n2 at h53
    show sayori nerv cm oe
    show kotonoha happ cm ce
    m "Но я стесняюсь."
    show monika cm
    show sayori mb at s54
    s "Я тоже..."
    show natsuki e1b
    show monika ce n1
    show sayori cm
    show kotonoha om
    k "Хе-хе-хе, понятно."
    show yuri neut cm e1d
    show natsuki oe
    show monika forward happ cm oe
    show sayori happ cm oe at t54
    show kotonoha cm
    mc "Тогда кто будет читать?"
    show natsuki sedu om oe lhip rhip
    show kotonoha oe
    n "Ты!"
    show natsuki cm
    mc "А почему я-то сразу?"
    show natsuki om ce
    n "А почему нет?"
    show natsuki cm
    mc "Уход от вопроса."
    show yuri happ om oe lup rup
    y "Давай, Макс, я уверена, у тебя хорошо получится."
    show yuri cm
    show natsuki oe
    show sayori ce
    s "Угу!"
    show yuri ldown rdown
    show natsuki happ cm oe
    mc "Пф, окей, хорошо..."
    show natsuki ldown rdown
    show sayori oe
    mc "Кучкуемся поближе."
    hide yuri
    hide natsuki
    hide kotonoha
    with dissolve
    show monika at t21
    show sayori at t22
    pause 0.2
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show monika om ce
    show sayori ce
    m "Прошу!"
    show monika cm n2
    pause 0.1
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    call show_poem(poem_ms)
    "Мон-ика?"
    "Моникальмар?"
    "Кальмароника?"
    show monika neut cm oe
    show sayori oe
    n "Мон-ика..."
    play music t5 fadein 3.0
    show monika anno cm oe n1
    show sayori laug cm oe
    n "Кхмпф-пф-пф!"
    show sayori ce
    n "Сайори, это гениально!"
    show monika angr cm oe
    n "Мон-{w=0.25}ика!"
    show monika om lpoint at h21
    m "МО-{w=0.5}НИ-{w=0.5}КА!" with vpunch
    show monika ce ldown
    m "Не Мон-{w=0.5}ика!"
    show monika cm
    show sayori om oe
    s "Но ведь это забавно!"
    show monika om
    show sayori cm
    m "Нет!"
    show monika oe
    show sayori neut cm oe
    m "Ни разу!"
    show monika cm
    "Теперь понятно, почему она не горела желанием выступить в первых рядах..."
    show monika anno cm oe
    y "Соглашусь..."
    show monika om ce
    show sayori sad cm oe
    m "Если честно, стих должен был окончиться на моменте, когда \"я дрейфовала в море\"."
    show monika cm
    show sayori om
    s "Тогда это было бы слишком чернушно по настроению..."
    show monika dist om oe
    show sayori cm
    m "Да, я знаю, но смысл..."
    show monika neut cm oe
    show sayori happ om ce lup rup at h22
    s "...получить настроение!"
    show monika angr cm oe
    show sayori ldown rdown
    s "Поэтому Мон-ика!"
    show monika om
    show sayori cm
    m "МО-{w=0.5}Н--{nw}"
    show monika vang cm oe at h21
    show sayori laug cm ce
    n "--ика!" with vpunch
    show monika cross angr_om_oe_n2
    m "ПФЬЮ!"
    show monika neut_cm_ce
    show sayori happ cm ce
    mc "Так, всё, хорош."
    show monika neut_cm_oe
    show sayori oe
    mc "Давайте делиться впечатлениями."
    n "Прикольно."
    n "Анализатор из меня всё равно никакущий."
    show monika angr_cm_oe_n2
    y "Это очень интересно..."
    show monika forward neut cm oe
    y "Необычно наблюдать сочетание стиля Сайори и Моники."
    show monika curi md oe
    show sayori neut cm oe
    y "Тем не менее стих не очень хорошо удался."
    y "Моника пыталась связать всё подтекстом взаимоотношений и поиска себя, а Сайори просто наслаждалась воображением."
    show monika neut cm oe
    y "В этом и заключается трудность таких стихотворений -- необходимо найти связь с партнёром, чтобы получить желаемый результат."
    show sayori dist cm oe
    y "Впрочем, это не только при составлении совместных стихов..."
    show monika e1d
    y "...хах..."
    "Она нарочно в мою руку выдохнула?"
    show monika oe
    show sayori om
    s "Значит, у нас не получилось..."
    show sayori neut cm oe
    y "Н-нет, я не это имела в виду!"
    y "Я говорила, что нужно просто добиться взаимопонимания, чтобы преследовать одну цель."
    y "У вас для первого раза вышло вполне нормально, но чем дольше вы писали, тем сильнее мешали друг другу из-за рассинхронизации..."
    show monika dist cm oe
    "Те же слова, только в профиль..."
    m "Хм..."
    mc "Заметно..."
    y "Это всё, что я могу сказать."
    show monika neut cm oe
    mc "Котоноха?"
    k "Ну, Юри...{w}уже всё сказала, да."
    mc "Мне тоже нечего добавить."
    show sayori worr om ce
    s "Эх..."
    show sayori cm
    show monika om ce
    m "Думаю, надо было мне стараться лучше..."
    show monika cm
    y "Не расстраивайтесь!"
    show monika oe
    show sayori neut cm oe
    y "Всё в порядке."
    show monika happ cm oe
    y "Просто попытайтесь в следующий раз договориться друг с другом."
    show monika om
    show sayori happ cm oe
    m "Конечно."
    show monika lean happ om oe at h21
    m "Спасибо, ребята."
    show monika cm
    show sayori om ce
    s "Угусь!"
    show monika forward happ cm oe
    show sayori cm
    pause 0.2
    play sound paper_torn_out
    pause 1.0
    "Как-то первый раз немного комом вышел..."
    show monika om lpoint rhip
    show sayori oe
    m "Теперь очередь Юри и Нацуки."
    show monika cm ldown rdown
    pause 0.1
    hide monika
    hide sayori
    with dissolve
    pause 0.2
    show natsuki cross worr cm oe at t21
    show yuri shy neut cm oe at s22
    with dissolve
    pause 0.2
    ny "..."
    m "У вас же получилось что-то написать, верно?"
    show yuri om
    y "Что-то...{w}да..."
    show yuri cm
    k "У них это с трудом вышло."
    show natsuki pout cm oe
    m "Но ведь получилось?"
    show natsuki om
    show yuri ce
    n "Не очень..."
    show natsuki cm
    show yuri turned neut cm e1d b1b rup at t22
    pause 0.5
    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0
    show yuri om
    y "В общем, Макс, вот, читай вслух."
    show yuri cm
    pause 0.1
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    show yuri anno om oe ldown rdown -b1b
    y "Или нет..."
    stop music fadeout 3.0
    show natsuki turned pout cm e1b
    show yuri neut om e1d
    y "Лучше про себя."
    y "При этом, чтобы все видели."
    show yuri cm
    mc "Ладно?..."
    show natsuki ce
    show yuri lsur cm ce
    y "Умф..."
    "Что ж там такое?"
    call show_poem(poem_ny)
    "..."
    "Они...{w}вообще забыли весь опыт прошлой недели?..."
    show yuri e2b
    "Нет, последние строчки этого «стиха» обнадёживают, но...{w}верится с трудом."
    show natsuki e1f
    "Такое ощущение, что это никогда не закончится, пока Юри и Нацуки в корне не поменяются."
    show natsuki neut cm e1f
    "А меняться из них никто не хочет...{w}или не может."
    show natsuki oe
    show yuri neut cm e1d
    k "Скажу сразу: они точно помирились."
    s "Точно-точно?"
    k "Точно-точно."
    m "Если это так, то..."
    show natsuki happ cm oe
    show yuri laug cm oe
    m "Я очень рада, что совместные стихи уже стали приносить пользу."
    show natsuki curi cm oe
    show yuri neut cm e1d
    mc "А будет ли закреплена эта польза?"
    show natsuki om lhip rhip
    show yuri om
    ny "Да."
    show natsuki neut cm oe
    show yuri dist om ce lup rup
    y "Мы решили забыть все прошлые распри и разобраться в себе окончательно."
    show yuri md
    n "Угу."
    show natsuki om e1b
    show yuri ldown rdown
    n "И у нас это стало получаться."
    show natsuki cm
    show yuri neut cm e1d
    mc "А..."
    "Такая уверенная речь..."
    show natsuki oe
    "Неужели реально всё?"
    "Но так быстро..."
    "Нет, до сих пор не верится."
    show natsuki nerv cm ce zorder 3
    show yuri happ cm oe zorder 2
    m "В таком случае предлагаю, во-первых, поблагодарить Юри и Нацуки за то, что они пришли к взаимопонимаю..."
    show natsuki oe
    s "Ва-а-а, ребят, вы настоящие молодцы!"
    play music t5 fadein 3.0
    show natsuki shoc om ce ldown rdown at t42
    show sayori turned happ cm ce lup rup at t11 zorder 1
    show yuri vsur mk e4c lup rup n3 at t43
    n "КХЕ!"
    y "В-в-в?!"
    k "Ха-ха-ха!"
    show natsuki cm oe at t52
    show sayori oe ldown rdown at t51
    show yuri flus cm oe ldown rdown n1 at t54
    pause 0.1
    show monika forward happ om oe lpoint at t53 zorder 4
    show kotonoha happ cm oe at t55 zorder 3
    with dissolve
    m "...а во-вторых, перейти к последнему на сегодня стихотворению!"
    show natsuki neut cm oe
    show monika lean happ om oe at h53
    show yuri neut cm e1d
    m "Макс, ты готов?"
    show monika cm
    "{s}НЕТ!{/s}"
    show monika forward happ cm oe
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    mc "...вот."
    show monika e1b
    "Чувствую себя идиотом."
    show sayori at t43
    pause 0.1
    show sayori e1b
    show natsuki e1c
    show yuri e1b
    show kotonoha at t42 zorder 2
    "Пусть поскорее это пройдёт, пожалуйста..."
    call window_close

    pause 3.0
    show sayori neut cm e2b
    pause 1.5
    show yuri happ cm e1b
    pause 3.0
    show monika neut cm e2b n2
    pause 3.0

    call window_open
    show monika mh
    show sayori oe
    m "Это...{w}очень интересно получилось..."
    show natsuki oe
    show monika om
    show sayori happ cm oe
    show yuri om oe
    y "Макс, с каждым разом у тебя выходит всё лучше и лучше."
    y "Ты подражал стилю Моники, верно?"
    show natsuki e1c
    show monika cm oe
    show yuri cm
    mc "Да."
    show monika e1c
    show sayori e1b
    show yuri neut om e1b
    y "У тебя это тонко вышло..."
    show yuri happ om e1b
    y "Да, действительно тонко."
    show natsuki curi cm e1c
    show kotonoha neut cm oe
    show sayori neut cm e1b
    show yuri worr om oe
    y "Жаль, что такие работы вне стен нашего клуба никому вовсе не интересны."
    show natsuki angr cm e2c b1e
    show yuri ce
    y "Особенно со вложенным смыслом..."
    show natsuki om lhip rhip
    show kotonoha angr cm oe rhip
    show monika e1b n1
    show sayori curi cm oe
    show yuri neut cm e2b
    n "Юри, да ты..."
    show natsuki mm ce
    show monika b1f
    n "...к-к..."
    show natsuki anno om ce -b1e ldown rdown
    show sayori neut cm e1b
    show yuri b1f
    n "...нет, не задолбала..."
    show natsuki curi om e1c
    show kotonoha neut cm oe rdown
    show monika -b1f
    show sayori oe
    show yuri dist cm ce -b1f
    n "...остальные стихи за борт выбросила?"
    show natsuki cm
    show monika e1c
    show yuri om
    y "Нацуки, ты не поняла, в чём дело..."
    show natsuki neut cm e1c
    show yuri oe lup
    y "Я про то, что людям, неинтересующимся поэзией, к сожалению, не суждено понять, какие плоды нашего творчества они пропускают мимо себя."
    show monika dist cm oe
    show yuri ce
    y "И в целом таких, как мы."
    show natsuki dist om oe
    show kotonoha e1c
    show yuri cm
    n "А-а..."
    show natsuki cm
    show kotonoha oe
    show monika neut cm oe
    show sayori om
    show yuri neut cm e1d ldown
    s "Но мы вот понимаем друг друга, правда?"
    show natsuki neut cm oe
    show kotonoha happ cm oe
    show monika happ om oe
    show sayori happ cm oe
    m "Правильно, и это главное."
    show kotonoha ce
    show monika ce
    show yuri flus cm oe
    m "Ладно, давайте вернёмся к стиху."
    show monika cm
    show yuri om lup rup at s54
    y "Ох, простите, я ушла в сторону..."
    show natsuki e1c
    show monika om oe
    show yuri cm
    m "Ничего-ничего."
    show kotonoha oe
    show monika cm e1c
    show sayori e1b
    show yuri neut om e1b rdown at t54
    y "...как я уже сказала, у Макса вышло ещё лучше, чем раньше."
    show yuri curi om e1b
    y "Учитывая органичность стиха..."
    show monika neut cm e1c
    show yuri ce
    y "...опустим пару моментов с рифмовкой фраз \"огней\"..."
    show yuri neut om e1b ldown
    y "...смею предположить, что твой стиль, Моника, для него наиболее благоприятен."
    show natsuki oe
    show monika e2a
    show sayori om ce lup rup at h43
    show yuri cm
    s "Согласна!"
    show sayori oe ldown rdown
    s "Это первый стих, в котором я проскользила взглядом без запинок."
    show natsuki om e1c
    show monika e1b
    show sayori cm
    n "Ну..."
    show natsuki mk e2c
    show sayori neut cm e1b
    n "...э-э-э..."
    show natsuki mb e1c
    show sayori happ cm e1b
    n "...эге."
    show natsuki ma
    show monika om
    show sayori oe
    m "Да, результат налицо..."
    show kotonoha ce
    show monika happ om oe
    m "Мне это очень нравится."
    show kotonoha neut cm oe
    show monika cm
    show sayori e1b
    show yuri om
    y "Котоноха, а ты как думаешь?"
    show kotonoha om
    show yuri cm
    k "Я?"
    show kotonoha m6 e1c
    k "У-у..."
    show kotonoha happ om ce
    show monika ce
    show yuri happ cm ce
    k "Всё отлично и прекрасно!"
    show natsuki oe
    show kotonoha cm
    show monika om
    show sayori oe
    m "Ты молодец, Макс."
    show monika cm
    mc "Спасибо."
    show kotonoha neut cm oe
    show monika om oe
    show yuri oe
    m "Выходит, цель эксперимента со стилями достигнута."
    show monika cm
    mc "Да..."
    show natsuki neut cm oe
    show kotonoha om rhip
    show yuri neut cm e1d
    k "Вы ещё эксперименты устраиваете?"
    show kotonoha cm
    show monika om ce
    show sayori ce
    show yuri e1b
    m "Не совсем, ха-ха-ха!"
    show kotonoha happ cm oe rdown
    show monika e1b
    m "Просто мы решили определить, как лучше Максу писать стихотворения, поскольку раньше он этим не занимался."
    show kotonoha om
    show monika cm
    show yuri e1d
    k "А, понятно."
    show kotonoha cm
    show monika om oe
    show sayori oe
    m "Что ж, возвращаю."
    show monika cm
    show yuri e1d
    mc "Угу."
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    show sayori at t51 zorder 1
    show natsuki happ cm oe at t52 zorder 2
    show monika om lpoint rhip zorder 3
    show yuri happ cm oe at t54 zorder 2
    show kotonoha at t55 zorder 1
    m "Итак, друзья!"
    show monika ce ldown rdown
    m "Первый обмен парными стихотворениями подошёл к концу."
    show sayori neut cm oe
    show natsuki curi cm oe
    show monika curi om oe
    show yuri neut cm e1d
    show kotonoha neut cm e1b rhip
    m "...есть ли смысл его оценивать?"
    show monika neut cm oe
    mc "Не думаю."
    show natsuki e1b
    show kotonoha oe
    mc "Было всего два стиха, один из которых уже «неактуален»."
    mc "Мой не в счёт."
    show sayori e1b
    show natsuki neut cm oe
    show yuri dist om ce
    y "Да, нам стоит попробовать ещё раз, только теперь с учётом ошибок и всем составом."
    show sayori oe
    show monika om
    show yuri cm
    m "Хорошо, другой вопрос."
    show monika mh lpoint b1f
    show yuri neut cm e1d
    m "Будем менять пары или оставим те, которые сформировались?"
    show sayori curi cm oe
    show natsuki cross neut cm e1b
    show monika cm ldown
    show yuri anno cm oe
    y "М-м-м..."
    show kotonoha rdown
    "Если они не поменяются, мне придётся возиться с Котонохой, а я её совершенно не знаю."
    "Было бы хорошо, если бы к ней примкнула Юри или Нацуки..."
    show sayori neut cm oe
    show natsuki om oe
    n "Не знаю даже."
    show natsuki cm
    show monika -b1f
    show yuri neut om e1d
    y "Не думаю, что подобный вид работы продержится у нас долго."
    show yuri e1b
    y "Поэтому хотелось бы по-максимуму испробовать различные вариации стилей..."
    show natsuki dist cm oe
    show monika e1b
    show yuri cm
    show kotonoha e1c
    m "Хм..."
    "Это ж сколько вариантов?"
    show yuri e1d
    show kotonoha happ om oe
    "Как там формула в теории вероятности...{w}а, факториалы:\nn!/(k!(n-k)!)...{w}правильно?"
    show sayori om
    show natsuki oe
    show monika oe
    show kotonoha cm
    "Где n -- общее количество групп, а k -- сами группы."
    show sayori cm
    show natsuki turned neut cm oe
    show monika happ cm oe
    show yuri happ om oe lup
    show kotonoha rhip
    "6 по 2..."
    show monika om lpoint
    show yuri cm ldown
    "6!/(2!*4!)."
    show sayori happ cm oe
    show natsuki om lhip rhip
    show monika cm ldown
    "Э-э-э..."
    "6!/(2!*4!)..."
    show natsuki cm
    show yuri om ce
    "Так, соберись."
    show sayori ce
    show natsuki happ cm oe
    show monika om ce
    show yuri cm
    "6! и 4! прекрасно ликвидируются."
    show monika cm
    show yuri oe
    show kotonoha om
    "Остаётся 5*6/(1*2)."
    show sayori oe
    show natsuki om
    show monika oe
    show kotonoha cm
    "Значит, 5*3=15 вариантов всего."
    show natsuki cm
    show kotonoha om rdown
    "И делим 15 на 3, потому что в день по 3 пары."
    show natsuki ldown rdown
    show kotonoha ce
    "5 дней выходит."
    show monika om
    show kotonoha cm
    "И минус 1, потому что вариант, который был сегодня, мы не учитываем."
    show monika cm
    show kotonoha oe
    "4..."
    show sayori neut cm oe
    show natsuki neut cm oe
    show kotonoha neut cm oe
    "Условно на неделю...{w}а уже среда."
    show monika neut cm oe
    show yuri neut cm e1d
    "В целом..."
    show monika om
    "Мы даже умещаемся."
    show monika cm e1d b1c
    "Разве что один день вылетает из-за субботы."
    show monika mq
    m "Макс!" with vpunch
    show monika cm oe -b1c
    mc "А?!"
    show monika happ om oe
    m "Ты согласен?"
    show natsuki angr cm oe
    show monika neut cm oe
    mc "С чем...{w}чего, кого?"
    show sayori curi cm oe
    show yuri om
    y "Ты снова провалился в себя?"
    show yuri cm
    mc "Так что?"
    show sayori neut cm oe
    show natsuki om lhip rhip
    n "Я в твоей паре, дурень!"
    show natsuki cm
    mc "О как."
    show natsuki neut cm oe ldown rdown
    mc "А остальные?"
    show sayori happ cm oe
    show monika om lpoint
    show yuri happ cm oe
    show kotonoha happ cm oe
    m "Юри со мной, а Сайори с Котонохой."
    show monika cm ldown
    mc "Ясно."
    show monika om
    m "Так ты не против?"
    show monika happ cm oe
    mc "Нет, конечно."
    show sayori ce
    show natsuki happ cm oe
    show monika om ce
    show yuri ce
    show kotonoha ce
    m "Отлично!"
    show sayori oe
    show monika oe lpoint rhip
    show yuri oe
    show kotonoha oe
    m "Итак, друзья!"
    show monika ce b1b ldown rdown
    m "Снова, ха-ха..."
    show monika oe -b1b
    m "Пары на следующее клубное собрание сформированы."
    m "Как и раньше, вы вольны писать и коммуницировать как угодно."
    m "Главное, чтобы работали оба партнёра."
    show yuri neut cm e1d
    m "Нет никаких вопросов?"
    show monika cm
    mc "Неа."
    show monika lean happ om oe at h53
    show yuri happ cm oe
    show kotonoha ce
    m "Тогда все свободны!"
    show sayori om ce lup rup at h51
    show natsuki ce
    show monika cm
    s "Всё, всем пока!"
    show sayori cm
    show kotonoha om lup rhid
    k "Пока!"
    show sayori cm ldown rdown
    show monika forward happ cm ce
    show yuri om
    show kotonoha cm rdown ldown
    y "До встречи!"
    stop music fadeout 3.0
    show sayori oe
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    show yuri cm at thide
    hide yuri
    show kotonoha at thide
    hide kotonoha
    pause 1.0
    show sayori neut om oe at t11
    s "Макс, на секунду."
    show sayori cm
    mc "Чегось?"
    show sayori tap dist om e1 at s11
    s "Ты извини, что сегодня утром тебя бросила."
    show sayori nerv om e2
    s "Я так увлеклась стихом, что забыла тебе отписаться, хе-хе..."
    show sayori cm oe
    mc "Да ладно, Сайори, не бери в голову."
    show sayori turned neut om oe at t11
    s "И сейчас придётся тебя покинуть: с Котонохой пойду домой, заодно обсужу с ней наше будущее стихотворение."
    show sayori happ cm oe
    mc "Ну, хорошо."
    show sayori om ce lup rup at h11
    s "Всё, я побежала!"
    show sayori cm ldown rdown
    mc "Удачи."
    show sayori at thide
    hide sayori
    pause 1.0
    show natsuki turned neut cm oe school_bag at t11
    pause 0.2
    show natsuki om lhip rhip
    n "Хей, Макс."
    show natsuki cm
    mc "Что?"
    show natsuki om e1b
    n "У меня домашки не так много сегодня, поэтому..."
    show natsuki cm oe
    mc "...придёшь в гости писать стих?"
    show natsuki om ldown rdown
    n "Возможно."
    show natsuki e1b
    n "Только у меня времени будет не очень много, ибо папа волнуется и возмущается, когда задерживаюсь."
    show natsuki dist om ce
    n "Либо я останусь дома и буду составлять с тобой стих по телефону."
    show natsuki neut om oe
    n "Но так и так, я буду подуставшей."
    show natsuki cm
    mc "Кх, понятно."
    show natsuki pout om oe
    n "Слушай, ты парень, а я хрупкая девушка."
    show natsuki neut cm oe b1d
    mc "Поэтому ты решила наглым образом воспользоваться своим статусом?"
    show natsuki cross neut om oe b1d school_bag
    n "Возьми и напиши всё от своей руки, злыдня!"
    show natsuki md -b1d
    mc "Хорошо-хорошо, я протяну свою руку хрупкой и беззащитной девушке."
    show natsuki turned laug om oe lhip rhip school_bag
    n "Да что Вы, что Вы?"
    show natsuki ce
    n "Вы мне льстите~"
    show natsuki ma
    mc "Ладно, хорош, беги уже."
    show natsuki happ cm oe
    mc "Раньше сделаешь, побольше отдохнёшь."
    show natsuki om
    n "Ага."
    show natsuki ce ldown rdown
    n "До вечера, напишу тебе!"
    show natsuki cm
    mc "До вечера."
    hide natsuki with easeoutright
    pause 0.2
    "Странно..."
    "Не похоже, что отец у неё прям серьёзный тиран."
    "Или просто сейчас всё очень...{w}нет, не хорошо...{w}стабильно."
    "Правда шестое чувство подсказывает, что продлится это недолго."
    "Или я это уже «говорил»?"
    "Чёрт, не помню..."
    show monika forward happ cm oe school_bag at t21
    show yuri turned happ om oe school_bag at t22
    y "...приду к тебе в гости к 5-6 часам после полудня."
    show monika om ce
    show yuri cm
    m "Договорились!"
    show monika oe
    show yuri ce
    m "Буду ждать."
    show monika cm
    show yuri anno om oe lup rup at s22
    y "Надеюсь, успею со всем управиться..."
    show monika om lpoint
    show yuri cm
    m "Если что, отпишись."
    show monika cm ldown
    show yuri happ om oe ldown rdown at t22
    y "Само собой."
    show monika ce
    show yuri ce
    y "До встречи!"
    show monika om
    show yuri cm
    m "До встречи!"
    show monika cm
    hide yuri with easeoutright
    pause 0.5
    show monika oe
    pause 0.5
    show monika neut om oe at t11
    m "О, Макс, ты ещё тут?"
    show monika cm
    mc "Да, что-то подзастрял."
    show monika lean happ om oe school_bag at h11
    m "Может, тогда пройдёмся вместе?"
    show monika ce
    m "Сви-ти?~"
    show monika cm
    mc "...я как раз это и хотел предложить."
    show monika forward happ om oe
    m "Хах, правда?"
    show monika cm
    mc "Да, так и есть."

    scene black with wipeleft_scene
    "Честно, одному уходить уже не хочется..."
    "Как в клуб вступил, так сразу и перестал."
    "Тем более когда есть возможность побыть с Моникой..."
    mc "Ключи у тебя?"
    m "Конечно."
    "Да-да, я потихоньку перестаю хотеть быть один."
    "Кажется...{w}мой организм снова подсел на «социальную» иглу..."
    call window_close

    $ r_name = "???"
    pause 1.0
    play sound closet_open
    pause 1.0

    call window_open
    n "Макс, Моника, сюда!"
    r "Отлично."
    "А это кто?"
    "По голосу кто-то знакомый..."

    scene bg corridor
    show monika forward neut cm oe school_bag at t31 zorder 2
    show natsuki turned neut cm oe school_bag at t32
    show reiko turned uniform_council happ cm oe lhip at t33 zorder 2
    with dissolve_scene_full
    $ r_name = _("Рэйко")
    play music reiko_music fadein 3.0
    show monika om ce
    show reiko neut cm oe
    m "Здравствуйте, Рэйко-сан..."
    show monika cm
    "Так вот ты какая -- глава школьного совета..."
    show monika oe
    show reiko om ce b1c
    r "Ой, давай без этих формальностей, Моника, аж тошно становится..."
    show monika om
    show reiko cm
    m "Хорошо, Рэйко."
    show monika curi om oe
    show reiko oe -b1c
    m "Что ты здесь делаешь вместе с Нацуки?"
    show monika md
    show natsuki e1b
    show reiko om
    r "Думаю, ты и сама догадаться можешь."
    show monika e1b
    show reiko cm
    m "..."
    show reiko om b1c rup
    r "Конфликт твоего клуба с Клубом выпечки, ну?"
    show monika dist om oe
    show natsuki oe
    show reiko cm rdown
    m "А, точно..."
    show monika cm
    show reiko -b1c
    "Рэйко явно успела поймать Нацуки за шкирку, иначе бы она ушла домой."
    show monika neut cm oe
    show reiko neut om e1b lhip rthink
    r "Я планировала ещё вчера заняться вашим бардаком, который как снег на голову, но было не до него."
    show reiko cm
    "Как грубо...{w}и с нашей стороны тоже..."
    show reiko om oe rdown
    r "А ты, я так понимаю, и есть тот самый новенький, кто «подарил» Литературному клубу официальный статус?"
    show monika happ cm oe
    show reiko cm
    mc "...да?"
    show monika om
    m "Он самый."
    show monika cm
    show natsuki curi cm oe
    show reiko om
    r "Как тебя там зовут?"
    show reiko e1b
    r "Из головы вылетело."
    show natsuki om
    show reiko cm oe
    n "Я только что говорила -- Макс."
    show natsuki cm
    show reiko om
    r "А, конечно."
    show monika neut cm oe
    show natsuki neut cm oe
    show reiko ldown
    r "Так вот, Моника."
    r "Я уже поймала президента Клуба выпечки, взяв Камуко и Сору, как тех, кто тоже был в конфликте, и отвела всех в выделенный учителями класс в этом корпусе."
    show natsuki e1b
    show reiko tough angr om oe
    r "А это значит, что ты с Нацуки нужна мне там {b}прямо сейчас{/b}."
    r "Никакие отговорки не принимаются."
    show natsuki oe
    show reiko turned neut om oe b1c lhip
    r "По-хорошему, Макса тоже надо взять, ведь он тоже там был по рассказу Соры."
    show monika om ce
    show reiko cm -b1c
    m "Хорошо."
    show monika cm oe
    show reiko om lpoint
    r "Класс, а теперь все дружно за мной."
    show reiko cm ldown
    "Етить твою мать..."
    "Я так и думал."
    "Хотя нет, Монику и Нацуки я бросать не намерен."
    show natsuki pout cm oe
    show reiko om oe b1c lhip
    r "Давайте, шевелитесь, не тяните время!"
    show reiko cm at thide
    hide reiko
    pause 0.5
    mc "Пф-ф-ф..."
    show monika mh lpoint
    m "Привыкай, она всегда такая."
    show monika om e1c ldown
    m "В школе точно..."
    show monika cm
    show natsuki om e1b
    n "Ага..."
    show natsuki cm

    scene black with wipeleft_scene
    "Я так и думал, что она мне не понравится..."
    r "Я жду!"
    call window_close

    call plot_transition

    call window_open
    scene bg class_day
    show monika forward neut cm oe at t51 zorder 2
    show natsuki turned neut cm oe at t52
    show reiko turned uniform_council neut cm ce b1c at t42 zorder 4
    show kohaku turned neut m3a oe at t43 zorder 3
    show kamuko turned lsur cm e1b headband_cat lhiphid rhid at t54:
        xoffset 140
    show sora turned neut cm ce at t55 zorder 2:
        xoffset 20
    with wipeleft_scene
    show reiko om lhip
    show kamuko neut cm oe
    show sora oe rpock
    r "Ура, наконец-то все в сборе."
    show reiko oe -b1c
    r "Итак, приступим."
    show monika curi om oe lpoint
    show natsuki curi cm oe
    show reiko neut cm oe b1c
    show kamuko curi cm oe
    m "Можно вопрос?"
    show monika md ldown
    show reiko om ce
    r "...что такое?"
    show monika om
    show reiko angr cm oe -b1c
    m "Почему ты решила провести всё в отдельном классе?"
    show monika neut cm oe
    show natsuki neut cm oe
    show reiko tough uniform_council angr om oe
    show kamuko neut cm oe
    r "Да потому что мне интересно ваше «чистое» мнение!"
    show reiko turned uniform_council neut om ce b1c
    show kamuko e1c
    r "Одно дело под взглядами учителей находиться, а другое -- здесь."
    show monika dist om oe
    show reiko cm
    m "Понятно..."
    show monika cm
    show natsuki pout cm oe
    show reiko om oe lhip
    show kamuko oe
    r "Так!"
    show monika neut cm oe
    show reiko -b1c
    show kohaku cross neut m3a oe
    r "Начнём разгребать ваш маразм."
    show reiko rup
    r "Просвещайте, в чём же дело конфликта."
    show reiko rdown
    show kohaku e1b n2
    r "С самого начала, без эмоциональной части."
    show monika dist cm oe
    show natsuki e1b
    show reiko cm
    "..."
    show sora ce
    show kamuko sad cm e2c
    "......"
    show reiko angr cm oe
    "Ну и?"
    "Мне придётся, что ли, всё рассказывать?"
    show monika worr cm oe
    show reiko sad om ce
    show sora sad cm ce n2
    r "О-о-о, убейте меня..."
    show natsuki oe
    show reiko tough uniform_council angr om oe
    show kamuko ce
    r "Ну хоть кто-то один, алло!"
    show reiko turned uniform_council neut om oe b1c lhip
    r "В ваших же интересах побыстрее уйти домой."
    show natsuki neut cm oe
    show monika neut cm oe
    show reiko cm
    show kohaku oe
    show kamuko neut cm oe
    show sora curi cm oe n1
    mc "Давайте я."
    show reiko om -b1c
    r "Ну давайте!"
    show reiko cm
    show sora neut cm oe
    mc "Э-э..."
    stop music fadeout 2.0
    call window_close

    call plot_transition(different_scene = False)

    if persistent.add_random_menu == 12:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    call window_open
    scene bg class_day
    show monika forward worr cm ce n2 at i51 zorder 2
    show natsuki cross worr cm oe at i52
    show reiko turned uniform_council neut cm e1b lhip rthink at i42 zorder 4
    show kohaku cross angr om ce at i43 zorder 3
    show kamuko turned vsur cm oe headband_cat lhiphid rhid at i54:
        xoffset 140
    show sora turned lsur cm oe at i55 zorder 2:
        xoffset 20
    with wiperight
    "Аудиозапись успешно прослушана..."
    koh "Т-т-т-т-т..."
    show sora om
    sor "Ничего себе, целая запись..."
    show monika oe
    show kamuko om rface
    show sora cm
    kam "Вот это интрижки!"
    show kamuko cm
    "Кстати, я же ничего не рассказал про позицию Соры в нашем бывшем плане, да?"
    "Хотя он мог своей сестре всё разболтать..."
    show natsuki neut cm oe
    show reiko oe
    show kamuko lsur cm oe rhid
    mc "На этом моменте всё и закончилось."
    r "Угу."
    show monika neut cm oe n1
    show natsuki turned neut cm oe
    show reiko om ce rdown
    show kohaku angr cm oe
    r "Значит, я правильно понимаю, что..."
    show reiko oe rup
    show kamuko curi cm oe
    show sora neut cm oe
    r "Первое (по твоему показанию и Соры): это была та самая беготня в понедельник, про которую мне рассказали в тот же день."
    show monika dist cm oe
    show natsuki worr cm oe
    show reiko e1b rthink
    r "А бег по коридорам у нас запрещён."
    show reiko cm
    "Ай..."
    show natsuki pout cm oe
    show reiko om ce rdown
    show kamuko neut cm oe
    r "Впрочем, я не удивлена, потому что всякая подобная ерунда, Нацуки, происходит далеко не в первый раз."
    show monika neut cm oe
    show reiko oe
    r "Второе (по записи)..."
    show natsuki curi cm oe
    show reiko ce rup
    show kamuko lsur cm e2c
    r "Я даже перечислять не стану, что наговорила Кохаку."
    show reiko oe rdown
    show kohaku ce
    r "И это я не затрагиваю то, что она же является инициатором всего этого конфликта."
    show reiko cm
    koh "......"
    show monika dist cm oe
    show natsuki pout cm e1b
    show reiko happ om ce lpoint
    show kamuko oe
    show sora ce
    r "Нет, ну финал реально был очень неожиданный, моё почтение, Моника!"
    show reiko cm lhip
    m "......"
    show natsuki oe
    show reiko neut om oe
    show kamuko neut cm oe
    show sora oe
    r "А теперь серьёзно."
    show monika neut cm oe
    show reiko b1c
    show kohaku oe
    show sora rpock
    r "Кохаку, почему ты до сих пор помешана на кексах Нацуки?"
    show reiko rup
    show kohaku e1b
    r "Это уже перебор, сколько можно?"
    show reiko rdown
    r "Столько времени прошло, а ты всё никак не успокоишься."
    show reiko cm -b1c
    show kohaku om
    koh "...я уже сказала всё на записи."
    show reiko om
    show kohaku cm
    r "Я уверена, что продвижение клуба таким способом -- не первостепенная причина."
    show reiko cm
    show sora anno cm oe
    koh "..."
    show reiko om ce b1c
    r "Опять эта молчанка..."
    show reiko oe rup
    r "Может, хватит?"
    show reiko rdown
    r "Сказать тяжело?"
    show reiko cm
    show kohaku angr om oe
    koh "Да, глава школьного совета, представляете?"
    show monika anno cm oe
    show natsuki curi cm oe
    show reiko angr cm oe -b1c
    koh "Есть личные мотивы, которые я не хочу афишировать."
    show reiko tough uniform_council angr om oe
    show kamuko lsur cm oe
    show sora angr cm oe
    r "А я как раз вас здесь и собрала, чтобы их, блин, выяснить!"
    show reiko turned uniform_council neut om oe b1c lhip
    show kohaku ce
    r "Кохаку, говори, как есть."
    r "Иначе мне придётся пустить в ход свои полномочия по наказанию тебя за нарушения школьного устава."
    r "За мелкие тебе уже прилетело, поскольку Моника уже показывала эту запись учителям."
    r "Но решение по таким случаям, как у тебя, лежат лично на мне."
    show natsuki neut cm oe
    show monika neut cm oe
    show reiko -b1c
    show kohaku neut m3a oe
    show kamuko curi cm oe
    show sora lsur cm oe
    r "И ты практически на целое отчисление от клубной деятельности наговорила."
    show reiko rthink
    r "Так-то я уже должна тебя в расход пустить, однако иду навстречу, потому что остался последний год обучения."
    show reiko e1b rdown
    r "И очернять своё «резюме» для поступления в вуз из-за такого бреда на финишной прямой, мягко говоря, не очень приятно."
    show reiko oe
    show kamuko lsur cm oe
    show sora neut cm oe
    r "Поэтому давай, я внимательно слушаю."
    show reiko cm
    show kohaku e1b
    koh "..."
    show monika b1f
    show natsuki curi cm oe
    show kamuko curi cm oe
    show sora curi cm oe
    koh "...можно мои уйдут?..."
    show reiko om
    r "Нет."
    show monika -b1f
    show reiko cm
    show kohaku angr om ce
    koh "Грх..."
    show kamuko neut cm oe
    show sora neut cm oe
    koh "Я хотела...{w}выяснить рецепт кексов..."
    show monika e2a
    show natsuki pout cm oe
    show kohaku oe
    show kamuko lsur cm oe lhid
    show sora lsur cm oe
    koh "Ой, да потому что я хотела стать {b}ЛУЧШЕ{/b} Нацуки!"
    koh "Потому что я хотела, чтобы меня {b}ПРИЗНАЛИ{/b} в клубе так же, как и Нацуки!"
    koh "Чтобы перестали принимать за идиотку!"
    koh "А ещё, чтобы порадовать своих родителей новым умением!"
    koh "А вы все, заразы, ополчились и выставили меня дурой!"
    "Она хочет признания?..."
    show sora anno cm oe lface
    show monika oe b1f
    show reiko om ce rup
    r "Ты сама выбрала такой радикальный способ, так что не надо тут капризничать."
    show reiko cm oe rdown
    show sora ldown
    koh "А у меня были другие варианты?!"
    show monika -b1f
    mc "Но почему бы просто не сказать всё Нацуки и не попросить рецепт?..."
    show sora neut cm oe
    koh "А ты серьёзно думаешь, что она даст?"
    show kohaku ce
    koh "Чёрта с два!"
    show natsuki angr cm oe
    koh "Она же у нас с «границами»: близко никого не подпускает!"
    show kohaku oe
    koh "А кексы для неё -- вообще нечто личное и сокральное!"
    koh "Сам же небось с этим сталкивался, а?"
    show natsuki om lhip rhip
    show kohaku cm
    n "Я не могу ТЕБЕ доверить ТАКОЕ!"
    show natsuki cm
    mc "Может, в самом начале, да, встречался, но потом всё изменилось."
    show natsuki anno cm oe ldown rdown
    show kamuko neut cm oe lhiphid
    mc "К членам Литературного клуба она относится прекрасно."
    show natsuki doub cm oe
    mc "Собственно говоря, вопрос: а не проблема ли в самой тебе?"
    show kohaku om ce
    show sora anno cm oe
    koh "Пф..."
    show natsuki om
    n "Вот именно."
    show natsuki cm
    show sora om lface
    sor "{size=17}Неужели сегодня до тебя это дойдёт?{/size}"
    show natsuki neut cm oe
    show kamuko happ om oe ldown rdown
    show sora neut cm oe ldown
    kam "А, так тебе поменяться надо?"
    show kamuko ce lup rup
    kam "Я помогу!"
    show kamuko oe
    kam "Тебе нужно быть более позитивной и приветливой, а ещё энергичной!"
    show kamuko ce rface
    kam "А для всего этого нужно всего лишь послушать--{nw}"
    show monika lsur cm oe
    show natsuki pani cm oe
    show reiko b1c
    show kohaku turned angr om oe lup rup at h43
    show kamuko pani cm oe rdown
    show sora lsur cm oe
    koh "{sc=3}НЕТ!{/sc}" with vpunch
    show kohaku ldown rhip
    show kamuko om
    kam "{sc=3}А-А-А!{/sc}"
    show natsuki pout cm oe
    show kohaku cross angr om oe
    show kamuko cm
    koh "Н-И-Ч-Е-Г-О НЕ ПОМЕНЯЕТСЯ!"
    show kamuko oe
    koh "Всё будет то же самое!"
    show monika om
    show kohaku cm
    show kamuko vsur cm oe lhid rhid
    m "Но ты даже не попробовала!"
    show monika cm
    show kohaku om
    koh "Да, потому что в этом нет {b}НИКАКОГО{/b} смысла!"
    show kamuko lsur cm oe
    koh "Будут тупо впустую потраченные силы с нервами ради мнимого результата в виде псевдодружбы, которую я в гробу видала!"
    show monika md
    show kohaku ce
    show sora sad cm oe
    koh "Нацуки меня пожизненно ненавидит из-за своих комплексов!"
    show monika neut cm oe b1b
    show kohaku oe
    koh "А раз ничего не поменяется, то и тактику свою менять я не собираюсь, потому что это {b}ЕДИНСТВЕННЫЙ{/b} способ добиться своих целей!"
    show monika worr cm oe -b1b
    koh "И никакого другого!"
    show monika om
    show kohaku cm
    m "А как же остальные участники и их труд..."
    show monika neut cm oe
    show kohaku om
    koh "А что остальные-то?"
    show monika e1a
    koh "Они-то тут причём?"
    show kamuko worr cm oe
    koh "Я ж для них тиран!"
    show monika om
    show kohaku cm
    show sora ce lface
    m "Но ты даже не хочешь это исправить..."
    show monika cm
    show kohaku om
    koh "Я уже говорила!"
    show kohaku ce
    koh "Я всё сказала!"
    show kohaku oe
    koh "И я не намерена идти на уступки, пока Нацуки сама не перестанет упираться и огрызаться!"
    show reiko om ce rup
    show kamuko neut cm oe
    show sora neut cm oe ldown
    r "Ну и зря."
    show monika neut cm oe
    show natsuki curi cm oe
    show reiko oe -b1c rdown
    show kohaku cm
    r "Тогда с этого момента будет действовать следующее негласное, но важное условие..."
    show reiko angr om oe
    r "Если я услышу хотя бы малейший «чих» с твоей стороны или узнаю об отвратительном отношении к участникам какого бы то ни было клуба..."
    show monika e2a
    show natsuki lsur cm oe
    show kamuko e2a
    show sora ec
    r "...то я тебя {b}исключу из состава школьного совета и вышвырну из Клуба выпечки{/b} без возможности вступления в любой другой."
    show reiko neut om oe
    r "А дальше тобой заниматься учителя будут, если что-то натворишь в дальнейшем."
    r "Вот они-то совершенно не будут церемониться."
    show reiko ce
    r "Вероятнее всего они тебя просто отчислят из школы или ещё что-нибудь сделают."
    show natsuki neut cm oe
    show reiko cm
    show kohaku om
    show sora sad cm oe
    koh "Замётано!"
    show monika oe
    show natsuki curi cm oe
    show reiko oe
    koh "Вот только не я одна во всём этом виновата!"
    show kohaku turned angr cm oe
    pause 0.1
    hide kohaku with easeoutright
    pause 0.5
    show reiko om ce b1c rup
    show sora ce lface
    r "Что за манеры..."
    show reiko rdown
    show kamuko e2b
    r "Я даже не договорила."
    show monika e1b
    show reiko cm
    show sora om
    sor "Она как всегда..."
    show monika oe
    show natsuki neut cm oe
    show reiko om oe -b1c
    show kamuko e2a
    show sora cm
    r "В общем, насчёт клуба при таком негативном раскладе..."
    show monika b1b
    show natsuki e1b
    show sora cm oe ldown
    r "Если же не найдётся новый участник, то клуб потеряет официальный статус, а также членство его президента в школьном совете."
    show reiko cm
    show kamuko om
    kam "Как это?!"
    show reiko om
    show kamuko cm
    r "Легко и просто."
    show natsuki oe
    r "Никто брать на попечение мелкие клубы не будет."
    show kamuko oe
    r "И уж тем более содержать кухонное оборудование, которым вы активно пользуетесь."
    show monika -b1b
    show reiko cm
    show kamuko worr cm oe
    show sora neut cm oe
    mc "Подожди, а как тогда..."
    show reiko om rup
    r "...Моника была частью школьного совета?"
    show reiko cm rdown
    mc "Да."
    show monika nerv cm oe
    show reiko om
    r "Она просто исключение."
    r "Захотела создать свой клуб вместо вступления в пост помощника."
    show reiko b1b
    r "Ну а я же не монстр, в конце концов, такой кадр топить."
    show reiko ce -b1b
    r "Ведь лидерство -- её призвание."
    show monika neut cm oe
    show reiko oe
    show kamuko neut cm oe
    r "Но такая практика у нас первая за всё время...{w}и последняя."
    show reiko e1b b1c rthink
    r "Преподавателям не нравятся, когда идут против правил."
    show reiko oe -b1c rdown
    r "Лишь репутация Моники и мои убеждения позволили сохранить её членство в совете."
    show reiko cm
    show kamuko worr cm oe
    "Ну и ну..."
    show reiko om ce
    show kamuko neut cm oe
    r "Ладно, хватит, не туда уехали."
    show natsuki dist cm ce
    show reiko oe
    r "В ситуации худо-бедно разобрались -- значит, вы все свободны, можете идти домой."
    show monika e1b
    show reiko cm
    show kamuko worr cm ce
    show sora om ce lface
    sor "Ох, надеюсь, всё устаканится..."
    show sora oe ldown
    sor "До свидания."
    show monika oe
    show natsuki neut cm oe
    show reiko om
    show kamuko neut cm oe
    show sora lsur cm oe
    r "И да, Сора..."
    show reiko cm
    show sora om
    sor "А?"
    show reiko om b1b
    show sora neut cm oe
    r "Ты уж постарайся отговорить её от этой идеи, раз это достигло такой точки."
    show reiko -b1b rup
    show sora anno cm oe
    r "И мозги заодно вправить, чтобы вела себя прилежно."
    show reiko cm rdown
    show sora om
    sor "Сестра, я уже тебе говорил, что это тяжело."
    show kamuko sad cm oe
    show sora lface
    sor "Пока что все мои попытки повлиять на неё не увенчались успехом."
    show reiko om
    show sora cm ldown
    r "Но сейчас на кону её судьба в Клубе выпечки, а не просто рядовой случай."
    r "И как-никак на данный момент она твой президент."
    show reiko cm
    show sora om
    sor "Прекрасно понимаю, но это не меняет её упрямство."
    show sora sad om oe
    sor "Так что...{w}извини."
    show sora cm rdown
    hide sora with easeoutright
    show monika at t31
    show natsuki at t42
    show reiko at t32
    pause 0.3
    show natsuki pout cm oe
    show reiko b1c
    show kamuko om ce
    kam "Меня это не устраивает!"
    show reiko om rup
    show kamuko cm
    r "А что я могу сделать, Камуко?"
    show reiko -b1c rdown
    show kamuko oe
    r "Как Кохаку будет действовать, так всё и пойдёт."
    show reiko cm
    show kamuko om
    kam "Но тогда клуб перестанет быть оффициальным!"
    show reiko om
    show kamuko cm
    r "Да."
    show kamuko e1c
    r "И?"
    show monika b1b
    show reiko cm
    show kamuko om
    kam "...я не хочу такой исход..."
    show reiko om ce
    show kamuko cm
    r "Ещё раз говорю: я ничего не могу сделать."
    show monika worr cm oe -b1b
    show natsuki e1b
    show reiko oe rup
    r "Единственное, что могу предложить в такой ситуации -- найти кого-нибудь нового."
    show reiko cm rdown
    show kamuko om ce
    kam "...эх..."
    show monika neut cm oe
    show natsuki oe
    show reiko om ce b1c
    show kamuko cm
    r "Всё, расходимся, у меня ещё дела есть."
    show monika om
    show reiko cm oe -b1c
    m "До свидания, Рэйко."
    show monika cm
    mc "До свидания."
    show natsuki om
    n "До свидания..."
    show natsuki cm
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show natsuki turned neut cm e1b school_bag at t31
    show kamuko turned sad cm oe lhid rhid headband_cat at t32
    show monika forward neut cm e1c school_bag at t33
    with wipeleft_scene
    show natsuki oe
    show kamuko om
    show monika oe
    kam "Э-эй..."
    show kamuko cm
    m "М-м?"
    show kamuko om
    kam "Моника-чан, можно..."
    show natsuki curi cm oe
    show kamuko mc
    show monika happ cm oe
    kam "...перейти к вам в случае чего?"
    show kamuko ma
    "Вот это гиперактивное существо будет среди нас тусоваться?!"
    show kamuko happ cm oe
    show monika om lpoint
    m "Конечно!"
    show monika ldown
    m "Если ты будешь участвовать в клубной деятельности."
    show kamuko om ce ldown rdown
    show monika cm ce
    kam "Да, писать поэмы, это я могу, ха-ха-ха!"
    show natsuki e1b
    show kamuko oe lhiphid rface
    show monika oe
    kam "Но я спросила так, на будущее."
    show kamuko cm
    show monika om
    m "Хорошо."
    show kamuko om ce lup rup at h32
    show monika cm
    kam "Пока-пока!"
    show kamuko cm ldown rdown
    show monika om ce
    m "Пока."
    call window_close

    show natsuki oe
    show kamuko lhiphid rhid at thide
    hide kamuko
    show monika cm
    pause 0.2

    call window_open
    scene black with wipeleft_scene
    "..."
    n "Камуко?"
    n "В нашем клубе?"
    m "Ну да, а что такое?"
    n "Моника, у неё «шило» в одном месте, и ты даже не представляешь, каких размеров."
    n "Наш уютный клуб превратится в белиберду."
    mc "Солидарен, она слишком специфична."
    m "Да ну вам обоим, Камуко не такая уж и непоседливая."
    m "И к тому же явно неглупая."
    m "А если она будет прилежно заниматься стихами, то вопросов никаких не будет."
    mc "Ну, здесь отчасти соглашусь..."
    n "Бэ-эх, ладно."
    n "Я побежала домой, мне надо успеть домашку закрыть."
    m "Хорошо, до завтра!"
    mc "Не забудь, жду сообщения."
    n "Помню-помню."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show monika forward neut cm oe school_bag at t11
    with wipeleft_scene
    show monika om
    m "Макс..."
    show monika cm
    mc "Чего?"
    show monika dist om oe
    m "Тебе не кажется, что..."
    show monika worr om oe
    m "...мы всё-таки слишком переборщили с Клубом выпечки?"
    show monika cm
    mc "Не думаю."
    show monika neut cm oe
    mc "Мы добиваем это дело до логического конца."
    show monika dist om oe
    m "Но тогда..."
    show monika ce
    m "...мы превратились в монстров..."
    show monika cm
    mc "Нет, Моника, монстрами мы бы были только в том случае, когда хотели бы целенаправленно развалить клуб."
    show monika worr cm e1a
    mc "А мы только защитились от нападка Кохаку."
    show monika om
    m "Да, но мы не заметили, как перешли в контратаку."
    show monika mh lpoint
    m "Смещение Кохаку в этой ситуации -- весомый удар по клубу!"
    show monika ldown
    m "И это то же самое, как если бы мы хотели сделать это умышленно!"
    show monika cm
    mc "Ага, а умышленное вмешательство в наш клуб -- это нормально?"
    show monika oe
    m "..."
    mc "К тому же сама подумай: если бы этот случай замяли, дальше было бы хуже как ей, так и нам."
    mc "И вот тогда бы последствия были более жёсткими -- никто бы никаких предупреждений и шансов не давал."
    mc "Хотя что-то я не верю, что Кохаку волшебным образом исправится, особенно после её последнего заявления..."
    show monika neut cm oe
    mc "А вообще у нас были другие пути решения этой ситуации?"
    show monika om e1b
    m "У-у..."
    mc "Правильно, не было."
    show monika cm
    mc "Поэтому никаких сожалений и розовых соплей нам здесь не надо."
    show monika mh oe
    m "Ты же сегодня будешь писать стих вместе с Нацуки, попробуй с ней поговорить насчёт корня проблемы."
    m "Может, тебе удастся докопаться до сути, которая поможет исправить всё в лучшую сторону?"
    m "А то её расплывчатые рассказы про конфликт будто не учитывают мелкие, но важные детали..."
    show monika cm
    mc "Хм..."
    mc "Могу, конечно, попробовать, но ничего не обещаю."
    show monika mh lpoint
    m "Всё равно потом расскажи про результат."
    show monika cm ldown
    mc "Само собой."
    show monika dist om oe
    m "Других вариантов я здесь не вижу..."
    show monika worr om ce
    m "Голова гудит..."
    show monika cm
    mc "У меня, честно, тоже..."

    scene bg niigata street suburban 15 day
    show monika forward dist cm oe school_bag at t11
    with wipeleft_scene
    show monika om
    m "Стихотворение ещё..."
    show monika cm
    mc "М-м?"
    show monika worr om oe
    m "Знаешь, я что-то вспомнила критику Юри..."
    m "...и она звучала так, словно я сделала всё неправильно."
    show monika cm
    mc "В каком плане?"
    show monika om ce
    m "Не смогла подстроиться под стиль Сайори, будто и не пыталась..."
    m "Не согласовала смысл стиха."
    show monika oe
    m "Ещё эта шутка про моё имя совершенно не к месту..."
    show monika cm
    mc "Ой, Моника, не закапывайся."
    show monika e1a
    mc "Ты молодец, потому что ты искренне старалась."
    mc "У нас такой опыт первый раз, а обычно он всегда идёт комом."
    mc "И главное, что ты поняла свои ошибки."
    mc "...да, это говорит тебе тот, кто ненавидит ошибаться."
    show monika om ce
    m "Всё равно, мой внутренний перфекционист не может с этим смириться..."
    show monika cm
    mc "Невозможно всё сделать идеально, как бы ты ни пыталась."
    mc "Зато возможно сделать всё качественно и с душой."
    mc "И это будет в разы лучше, чем просто «идеально»."
    show monika om oe
    m "...не знаю, Макс."
    show monika neut om oe lpoint
    m "Конечно, ты безусловно прав, но..."
    show monika dist om ce ldown
    m "Легче не становится."
    m "Перфекционизм никуда не девается..."
    show monika neut om oe
    m "Он преследует меня всю жизнь."
    show monika lpoint
    m "Помнишь, я тебе рассказывала про себя?"
    show monika cm ldown
    mc "Да."
    show monika om e1b
    m "Мне кажется, его корни идут как раз оттуда."
    show monika oe
    m "От родителей."
    m "От «успешности»."
    show monika dist om oe
    m "От всего этого..."
    show monika ce
    m "Теперь я просто не могу что-то сделать и оставить, как есть."
    show monika oe
    m "Всегда хочется довести это до идеала."
    m "И меня очень мотивировало, что у кого-то другого получается хуже, чем у меня, как бы это жестоко ни звучало."
    show monika ce
    m "Но при этом родители мне постоянно твердили, что не нужно себя с кем-то сравнивать."
    show monika oe
    m "Они вообще не понимали, что это даёт мне силы."
    m "Хотя и жестоким конкурентом для всех становиться не хочется..."
    show monika cm
    mc "Как бы тебе так себя не погубить..."
    show monika neut cm oe
    mc "Я тебе вот что скажу, Моника."
    m "М-м-м?"
    mc "Конечно, это может прозвучать глупо, даже настолько, что испанский стыд пробьёт, но тем не менее..."
    show monika nerv cm oe
    mc "Хотя чего нам стыдиться после понедельника, верно?"
    show monika mb ce
    m "Ха-ха-ха!"
    show monika happ om oe
    m "Ладно, не томи."
    show monika cm
    mc "В общем..."
    show monika neut cm e2a
    mc "Для меня ты являешься идеалом."
    show monika n4
    mc "Причём не только с эмоциональной точки зрения, но и с логической: настоящие чувства, внешность, искренность, так далее..."
    mc "И я не хочу, чтобы ты себя угробила из-за какого-то там дурацкого перфекционизма."
    mc "Ты -- настоящий идеал среди всех этих мнимых...{w}«идеалов»."
    mc "Поэтому, пожалуйста, не уходи в подобное с головой."
    mc "Ничто с тобой не сравнится."
    show monika mf
    m "О-о..."
    show monika mg
    m "...х-х-хорошо, Макс..."
    show monika happ om ce b1b
    m "Спасибо за такие слова...{w}большое..."
    show monika cm
    mc "Я просто не могу оставаться в стороне."
    show monika e1b -b1b
    mc "Всё-таки я парень твой или кто?"
    show monika om
    m "Хе-хе..."
    show monika cm

    scene bg niigata street suburban 16 day
    show monika forward worr cm ce school_bag at t11
    with wipeleft_scene
    show monika om
    m "Что-то я за сегодня замоталась..."
    show monika cm
    mc "Скоро придёшь домой и отдохнёшь."
    show monika om oe
    m "Но ещё домашнее задание и стих с Юри..."
    show monika neut cm oe
    mc "Много делать?"
    show monika mh
    m "Нет, к счастью."
    show monika cm
    mc "Тогда быстро управишься."
    show monika mh lpoint
    m "Кстати, насчёт Юри и тебя..."
    show monika cm ldown
    mc "Что такое?"
    show monika curi om oe
    m "Весь клуб...{w}как-то слишком быстро забыл про её проблему."
    m "И про твою тоже."
    show monika md
    mc "Хм..."
    "Кстати, да..."
    show monika happ cm oe
    mc "Возможно, ты так уверенно провела сегодняшнее клубное собрание, что тревоги у всех вылетели из головы."
    show monika om ce
    m "Ха-ха, может быть!"
    show monika oe
    m "Но если серьёзно, то очень хорошо, что Юри решилась на такой важный шаг и..."
    show monika neut mh e1b b1f
    m "...приоткрыла «завесу» тайны остальным..."
    show monika cm oe -b1f
    mc "Точнее рукава, да?"
    show monika om
    m "Ну...{w}да."
    show monika dist om oe
    m "Но за исключением причины возникновения самой тайны..."
    show monika cm
    mc "Думаю, выясним это в ближайшем будущем."
    show monika neut cm oe
    mc "Только теперь мы не вдвоём будем действовать, а всем клубом, не так ли?"
    mc "Без всяких шушуканий."
    show monika om e1b
    m "Это да..."
    show monika mh ce
    m "Я бы могла ещё раз попробовать поговорить с Юри..."
    show monika cm oe
    mc "Нет, давай не будем в лоб бить."
    mc "Лучше потихоньку и аккуратно раскрепостим её, как и говорил."
    show monika om
    m "Ладно, не буду донимать..."
    show monika cm
    mc "Пока что постарайся сделать так, чтобы она получила побольше позитивных эмоций."
    show monika happ cm oe
    mc "Уверен, это поможет задавить её переживания."
    show monika om
    m "Хорошо."
    show monika neut mh oe lpoint
    m "Но а что насчёт тебя?"
    show monika cm ldown
    mc "А что я?"
    show monika dist om oe
    m "Твой кошмар..."
    show monika worr om e1a
    m "Ты проснулся после дрёмы таким же нервным, как вчера утром."
    m "Мне это очень не нравится, Макс."
    m "Я начинаю за тебя беспокоиться."
    show monika cm
    mc "...я же озвучивал, мне нечего сказать по этому поводу."
    show monika curi om oe lpoint
    m "Может, если прислушиться к тому, что говорится в твоих снах, можно найти смысл происходящего?"
    show monika neut cm oe ldown
    mc "Ты серьёзно думаешь, что во всём этом есть какой-то смысл?"
    show monika om
    m "Но ведь не просто так всё началось, правда?"
    show monika cm
    mc "Хм-м..."
    show monika worr om e1a
    m "Я не хочу, чтобы ты страдал из-за этого."
    show monika happ om oe b1b
    m "Ты для меня тоже...{w}идеал."
    show monika cm
    mc "Я понимаю, Моника..."
    show monika worr om e1a
    m "С психологом пока ничего не выходит?"
    show monika cm
    mc "Нет, никаких результатов, начиная с воскресенья."
    mc "Что-то мне подсказывает, что не найду я его..."
    show monika om
    m "Всё равно, Макс, старайся до последнего."
    m "Ради себя, ради Юри, ради Литературного клуба..."
    m "Ради меня..."
    show monika cm
    mc "Да понятно, это не обсуждается."
    show monika neut mh oe
    m "Если что, могу попробовать помочь."
    show monika cm
    mc "М-м, нет, не стоит..."
    mc "У меня всё равно нет никаких зацепок, кроме пары отрывков в памяти."
    show monika om ce
    m "Ладненько..."
    show monika cm

    scene bg monika house outside day
    show monika forward neut cm e1b school_bag at t11
    with wipeleft_scene
    show monika oe
    mc "Что ж, прибыли."
    show monika happ om oe
    m "Да..."
    show monika cm
    mc "До завтра?"
    show monika ce
    m "Угу."
    show monika lean happ om oe school_bag at h11
    m "До завтра, свити."
    show monika cm
    mc "До завтра, Мони."
    call window_close
    show monika forward happ cm ce school_bag at thide
    hide monika
    pause 0.5
    stop noise_1 fadeout 2.0

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "Всё, вроде бы."
    mc "Ха-а-а..."
    "Голова никакая..."
    "Интересно, когда я последний раз чувствовал себя свежо и свободно?"
    "Без всяких там нагрузок, обязаловок, прочего..."
    "Я даже не помню."
    "А так хочется от всего этого избавиться и..."
    "А не из-за этого ли у меня кошмары?"
    "Я уже думал в таком ключе?"
    "Или нет?"
    "Да даже если и думал, то почему их раньше не было?"
    "В старшей школе всегда такие нагрузки, а появиться кошмары решили лишь под начало последнего года."
    mc "Блин, не понимаю!"
    "Это так отвратительно: когда ты знаешь, что в тебе что-то ломается и меняется в негативную сторону, а ты даже не знаешь, что именно."
    "Не говоря уже о причинах..."
    pause 0.2
    play phone_sound new_message_mc
    pause 1.0
    mc "А?"
    "Нацуки, что ли?"
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 65
        clock = (18, 2)

    phone register "mc_n_chat":
        time year 2018 day 25 month 4 hour 18 minute 2
        "n" "Макс, я вышла к тебе, скоро подойду"

    phone discussion "mc_n_chat"
    $ plot_pause()
    phone discussion "mc_n_chat":
        "mc" "Понял"
        "mc" "Отец-то твой не против?"
        "n" "А он ещё не дома"
    $ phone.system.clock = (18, 3)
    phone discussion "mc_n_chat":
        "mc" "И когда вернётся?"
        "n" "К 8 вечера"
        "mc" "Успеешь?"
        "n" "Если ты перестанешь писать когда я на ходу то да"
        "mc" "Ок"

    phone end discussion transition

    call skip_block_off
    "Не думаю, что за опоздание она получит по шее, но лишний раз лучше не рисковать..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom
    show natsuki turned casual fc neut cm oe at i11
    with wiperight
    show natsuki curi cm oe
    mc "Ну что, не будем терять время и сразу приступим?"
    show natsuki om lhip rhip
    n "Да я ради этого сюда и пришла."
    show natsuki cm
    mc "Тогда--{nw}"
    show natsuki neut om e1c
    n "Слушай, у тебя тут такая просторная кровать..."
    show natsuki nerv om e1a ldown rdown
    n "Можно полежать?"
    show natsuki angr cm oe
    mc "Ага, чтобы ты задрыхла, пока я стих писал?"
    show natsuki om ce
    n "Ничего я не задрыхну!"
    show natsuki neut om oe
    n "Буду тебе оттуда помогать."
    show natsuki cm
    mc "Хорошо устроилась, блин..."
    show natsuki happ cm oe
    mc "Ладно, ложись, только не свороти одеяло."
    show natsuki mb ce
    n "Окей."
    show natsuki cm at thide
    hide natsuki
    pause 1.0
    n "{size=19}О-о-о...{/size}"
    "Мда, с виду на неё так посмотришь -- пушинка какая-то."
    "И вот у такого человека своенравный характер..."
    n "{size=19}К-куда ты смотришь?!{/size}"
    mc "Сдались мне твои труселя..."
    n "{size=19}БАКА!{/size}"
    mc "Лучше давай думать, о чём писать."
    mc "У меня лично никаких идей нет."
    n "{size=19}У-у-у...{/size}"
    "Голова размякла."
    "Не могу преодолеть барьер тупизма..."
    mc "Ну?"
    n "{size=19}Подожди...{/size}"
    n "{size=19}...{/size}"
    n "{size=19}Кексы?{/size}"
    mc "Было, ты писала."
    n "{size=19}Готовка кексов.{/size}"
    mc "Халтура: кексы же были."
    n "{size=19}Чай.{/size}"
    mc "Что?"
    mc "Ты как себе это представляешь?"
    n "{size=19}Ясно, потолок.{/size}"
    mc "Блин, Нацуки, ты угораешь?"
    mc "Я тоже так могу мысли перебирать."
    mc "Ручка, бумага, кровать, телевизор, голос--{nw}"
    n "{size=19}ГУСЬ.{/size}"
    mc "...что?"
    mc "Какой, нафиг, гусь?"
    n "{size=19}Недавно в Интернете форс видела, в котором люди придумывают рифмы к слову «гусь».{/size}"
    n "{size=19}Вот и подумала, что это как вариант...{/size}"
    mc "Гусь..."
    mc "Ну да, легко рифмуется с глаголами, но далеко на этом не уедешь."
    n "{size=19}Ещё, помню, был тупой форс с «амогусом»...{/size}"
    mc "Ой, Нацуки, мало ли какую хрень в Интернете форсят!"
    mc "Лучше тему выбери!"
    n "{size=19}Вот же, блин!{/size}"
    n "{size=19}К-О-С-М-О-С.{/size}"
    mc "Космос..."
    "И что же про него написать?..."
    n "{size=19}Да, космос.{/size}"
    n "{size=19}Начни там как-нибудь, с чего-то...{w}ох, ну типо ты посмотрел наверх, стал мечтать, м-м?{/size}"
    mc "М-м..."
    mc "Лады, попробуем..."

    call poem_act_1_day_10_mcn_1

    scene bg bedroom
    show natsuki turned casual laug cm ce at t11
    with Dissolve(0.15)
    pause 0.15
    play sound sayori_hide_fast
    show natsuki at lhide
    hide natsuki
    mc "{sc=2}Стой, кому говорю!{/sc}"

    scene black with wipeleft_scene
    mc "{sc=2}Не надо бегать по моему дому!{/sc}"
    "{sc=1}...{/sc}"
    "Убежала на первый этаж, засранка..."
    "А вообще это на руку!"
    "Сейчас запрусь и доведу стих до логического конца."
    pause 0.2
    play sound closet_close
    pause 1.0
    stop music fadeout 3.0
    "Нам же ведь надо что-то показать, а?"

    scene bg bedroom with wipeleft_scene
    "Иначе это полный провал."
    "Хотя чего это я?"
    "Это УЖЕ провал."
    "Пф, так и назову «недостих»."

    call poem_act_1_day_10_mcn_2

    scene bg bedroom with dissolve_cg
    pause 0.5
    call show_poem(poem_mcn)
    "Моника явно будет не в восторге..."
    n "{size=19}Ну и?{/size}"
    mc "Иду-иду!"
    pause 0.2
    play sound closet_open
    pause 1.0
    show natsuki turned casual fc neut cm oe b1d at l11
    pause 0.5
    show natsuki om lhip rhip
    n "И что ты там такое дописывал?"
    show natsuki cm
    mc "Стих на столе, сама всё увидишь."
    show natsuki e1c ldown rdown at thide
    hide natsuki
    pause 0.5
    "Повеселиться ей, блин, приспичило..."
    "С чего вдруг?"
    "Нет, её слова я услышал, но..."
    "Ой, да такое ощущение, что она контролировать себя не может из-за «социальной» голодухи."
    "Иначе откуда такое «шило в её заднице»?"
    "А тут, стоит только найти того, кому можно доверять, так сразу начинаются свисты-пляски."
    "Но если так подумать...{w}я и сам был в таком состоянии до встречи с Сайори..."
    "У меня были своего рода припадки «радости» или что-то вроде того..."
    "Типо, когда с кем-то разговаривал, то больше становился весёлым: отшучивался, улыбался и так далее..."
    "И иногда такое состояние переростало адекватность и над ним терялся контроль."
    "И как хорошо, что оно уже давно сдохло, потому что практически не получало никакого отклика, кроме упрекания себя за неуместное поведение."
    show natsuki cross casual dist cm ce at t11
    pause 0.2
    show natsuki om
    n "М-м-мда, признаю -- это полная хрень."
    show natsuki cm
    mc "...угу."
    show natsuki turned casual curi om oe lhip rhip
    n "Будем показывать эту бумажку остальным?"
    show natsuki cm
    mc "Ты ещё спрашиваешь?"
    show natsuki e1b ldown rdown
    mc "Писать новый стих -- ноль желания."
    mc "Да и отрицательный результат -- тоже результат."
    mc "Хотя можно сделать вид, что у нас ничего не получилось и просто ничего не приносить, но, по факту, ничего не изменится."
    show natsuki pout om oe
    n "Но тогда клуб откажется от совместных стихов."
    show natsuki cm
    mc "Не думаю, что 2 провальных стиха станут приговором."
    mc "Но Моника точно рада не будет."
    show natsuki ce
    n "Ф-ф..."
    show natsuki oe
    mc "Что-то я раньше не видел твоего энтузиазма по этому поводу, а сейчас прям приуныла."
    show natsuki dist om oe
    n "Ладно, не будет никакого веселья."
    n "И стихов нормальных не будет."
    show natsuki ce
    n "Не знаю, что на меня нашло."
    n "Извини."
    n "Лучше отлежусь на кровати и пойду домой."
    show natsuki cm
    mc "Эй, не кисни ты так!"
    show natsuki at thide
    hide natsuki
    mc "Нацуки."

    scene black with dissolve
    pause 0.25
    "Не хватало ещё тут её внезапной грусти."
    mc "Я прекрасно понимаю твоё желание, оно вполне естественно."
    mc "У меня самого в прошлом такое же поведение было."
    mc "Тоже хотел получить дозу позитива, но в бесконтрольных порывах доводил ситуацию до абсурда."
    n "..."
    mc "Ну ладно, хочешь, давай всё-таки попробуем состряпать короткий стих, чтобы спасти положение."
    n "Нет времени."
    mc "Времени у нас ещё больше часа..."
    n "И сил."
    n "И желания, как ты говорил..."
    mc "Хм-м-м..."
    "Как развеять её состояние?"
    "Блин, не знаю...{w}или..."
    mc "О!"
    mc "Расскажешь мне про себя?"
    n "...что?"
    mc "Про Клуб выпечки, там, может, что-то интересное, что до меня было."
    mc "Ты же хотела \"поиграть\"..."
    mc "Пусть хотя бы в таком виде."
    n "...м-м-м..."
    mc "Да давай, не стесняйся."
    mc "Ты и так своими...{w}не очень белыми носками в меня упириваешься, чего тут стесняться?"
    n "Они сильно грязные?"
    mc "Нет."
    mc "Но скоро стирать придётся."
    n "Грх, когда успели запачкаться?!"
    n "Только пару недель назад их стирала, были белоснежными!"
    n "У тебя нахваталась, наверное!"
    mc "Чего?!"
    mc "Я тут столько не мусорю, чтобы грязь на твоих носках по всей ступне собиралась!"
    n "Ну не я же виновата, ха-ха-ха!"
    mc "И не я уж точно!"
    mc "Нацуки, мне кажется, или у тебя вся грусть улетучилась и вместо неё энергия в заднице заиграла?"
    n "Как ты угадал?"
    mc "Миндальная связь."
    n "Ха-ха-ха!"
    mc "Ха..."
    mc "Так это..."
    mc "Может, реально что-то расскажешь?"
    mc "У нас ещё осталось время, делать мы всё равно больше ничего не будем..."
    n "Ой, ладно."
    n "Так что именно ты хочешь услышать?"
    "{s}Подробности срача с Кохаку.{/s}"
    mc "Что-нибудь, неважно."
    n "Что-нибудь..."
    n "..."
    n "...я даже не знаю..."
    mc "Как ты вообще попала в клубы?"
    mc "И какой ты раньше была?"
    n "У-у..."
    mc "Если вдруг это личное или что-то негативное, то не надо, можем сменить тему разговора."
    n "Да не, ничего такого..."
    n "О, точно!"
    n "В курсе, что у меня в средней школе было интересное прозвище?"
    mc "Хм, надеюсь, оно нормальным было?"
    n "Ещё как!"
    mc "И какое же?"
    n "Догадайся."
    mc "Смеёшься?"
    mc "У меня нет вариантов."
    n "Карманная рысь."
    mc "Ты?!"
    mc "Рысь?!"
    n "Да, за резкость, проворность и неожиданность."
    n "Не веришь?"
    mc "Пха-ха-ха--{nw}"
    mc "{sc=3}А-АЙ!{/sc}" with vpunch
    mc "Ты зачем мне в бок ткнула со всего размаха?!"
    n "Чтоб ты поверил."
    mc "Тьфу ты..."
    mc "Реально рысь."
    mc "Я даже среагировать не успел."
    n "Ха-ха, а ты смеялся!"
    mc "Ты тоже только что посмеялась."
    n "Не считается!"
    n "Так, вообще, возвращаясь к разговору..."
    mc "Да, если серьёзно, откуда взялось это прозвище?"
    n "Меня же подстрекали постоянно -- я огрызалась."
    n "Иногда доходило до перепалок."
    n "А в те моменты я читала одну мангу, где была героиня с таким же ростом, как у меня, и прозвище было похожее, но другое."
    n "И волосы у неё были такие же длинные..."
    n "Короче, так и увязалось."
    mc "Да уж..."
    n "Правда, когда часть дурачков ушла после конца средней школы и когда нас перетасовали, то всё быстро забылось."
    n "Так, редко у кого-то проскальзывает в разговоре за спиной, да и то я не помню, когда последний раз слышала это прозвище..."
    mc "Подожди, волосы?"
    n "Что?"
    mc "У тебя были длинные волосы?"
    n "А, да."
    n "Я их растила с начальной школы, но потом подстригла незадолго до вступления в Литературный клуб."
    mc "А что так?"
    n "С ними одна сплошная морока!"
    n "В средней школе меня часто за них дёргали, они постоянно секлись, грязнились, колтуны образовывались -- не могла я за ними ухаживать, как надо."
    n "Думала, вот научусь, накоплю на всякие специальные шампуни, но так ничего и не вышло."
    n "В итоге, плюнула на это дело, потому что устала терпеть."
    mc "Жаль..."
    n "Неа."
    n "С короткими в разы проще и удобнее."
    n "Да и мне такие лучше подходят."
    mc "Хм..."
    "Вообще да, я настолько привык к короткой причёске Нацуки, что это стало неотъемлемой частью её образа."
    mc "Кстати, почему бы тебе не написать стихотворение про \"карманную рысь\"?"
    n "М-м-м..."
    mc "Уверен, вышло бы интересно, зная, как ты умеешь затрагивать темы."
    n "Я подумаю..."
    mc "О, ещё один интересный вопрос."
    n "Какой?"
    mc "Кексы."
    mc "Почему ты так любишь их делать?"
    n "Потому что они у меня получаются?"
    mc "Но ведь тебя мама как-то сподвигла их делать, верно?"
    n "Да..."
    n "Но здесь нет ничего особенного."
    n "Мне они просто очень нравились."
    n "Я хотела научиться печь так же, как она."
    mc "И в конце концов научилась?"
    n "Да."
    n "Но я на этом не остановилась: подчерпывала всякие рецепты из кулинарных манг, из Интернета, из телепередач..."
    n "Что попадалось, то и изучала."
    mc "И именно поэтому ты решила податься в Клуб выпечки?"
    n "Ну да."
    n "Во-первых, я хотя бы где-то числилась, во-вторых, там оборудование было лучше, чем у меня дома."
    n "А ещё время."
    n "И папе не мешала с работой..."
    mc "...а потом пришла Кохаку и решила скопировать твоё умение."
    n "Сначала она была ещё ничего."
    n "Но стоило узнать её получше, так сразу всё вылилось: упрямство, агрессия, бла-бла-бла..."
    mc "И ты не захотела с ней делиться навыками, понятно."
    mc "А почему Кохаку стала такой...{w}негативной?"
    mc "Не просто так-то, м-м?"
    n "А кто ж её знает?!"
    n "Она ничего не рассказывала."
    n "Стала себя так вести, и всё."
    n "А копаться в ней и её проблемах у меня нет никакого желания."
    mc "Но это могло бы решить ваш конфликт..."
    n "Ага, а изменилась бы она после этого?"
    mc "Хм..."
    n "Как там это закрученно называют?"
    n "Комплексы, да?"
    mc "Да."
    mc "Я это подметил за ней."
    n "Вот."
    n "У неё тараканы в голове основательно укоренились."
    n "И когда она пробыла президентом некоторое время, то все, по словам самих же участников, ощутили на себе, насколько сильно они ошиблись выбором."
    mc "А, ну да, ты же ушла, как только она у руля стала..."
    n "Правильно."
    n "Короче, Кохаку пустила корни, спихнуть её никто не мог: толком замены не было."
    n "А ещё, вероятно, не всё в ней было потеряно, раз она до сих пор глава клуба."
    mc "Судя по поведениям остальных, все просто свыклись, не более."
    n "Тоже верно."
    mc "Ладно, раз уж мы эту тему затронули, то спрошу напрямую: не замечала ли ты всякие детали касательно Кохаку или что-то вроде того..."
    n "Нет, говорила же."
    n "Мне это неинтересно."
    mc "Да я не в этом плане."
    mc "Может, краем уха слышала чей-то разговор про неё или что-то с ней связанное?"
    n "Думаешь, я помню?"
    n "Я редко пересекалась с Клубом выпечки после ухода, не говоря уже о разговорах..."
    mc "Ясно."
    "Так и думал, провал."
    "Блин, что ни попытка нарыть информацию по проблеме, то вечно что-то мешает это сделать."
    play sound natsuki_stomach_rumble
    pause 3.0
    n "Ой..."
    mc "Кхм, какой «художественный» у тебя звук вышел..."
    n "Грх..."
    mc "Не хочешь перекусить?"
    mc "У меня вроде остались кое-какие сласти с прошлых выходных."
    n "Н-нет, спасибо..."
    mc "Почему?"
    n "Не хочу портить аппетит перед ужином."
    mc "Папа будет возмущаться?"
    n "Наверное..."
    mc "Кстати, вы же довольно бедные по деньгам."
    mc "Хотя бы разнообразную еду едите?"
    n "Иногда..."
    mc "А то на одной химозе и полуфабрикатах желудок далеко не уедет."
    n "Я знаю."
    n "Но выбирать не из чего."
    mc "Хочешь, мы тебе всем клубом будем фрукты покупать или ещё что-то полезное..."
    n "Вот уж не надо всех на уши из-за этого поднимать!"
    mc "На уши мы поднимемся, когда тебе окончательно плохо станет от твоего вынужденного образа жизни."
    mc "А так, если захочешь условное яблоко, просто скажи: \"Яблоко\"."
    n "..."
    mc "Всего лишь простое слово: \"Яблоко\"."
    n "..."
    mc "Ты понимаешь, что я говорю?"
    mc "Понимаешь смысл?"
    mc "Ответь, просто скажи: \"Да-а\"{nw}"
    mc "{sc=3}А-А-А-А-А-А--{/sc}{nw}" with vpunch
    mc "--ты мне так дырку в боку сделаешь!"
    n "Потому что ты меня настолько заболтал, что осталось полчаса!"
    n "Мне срочно надо спешить домой!"

    scene bg bedroom
    show natsuki turned casual pani cm oe at t11
    with dissolve
    pause 0.25
    show natsuki pout cm oe
    mc "Блин, ну так беги!"
    play sound sayori_hide_fast
    show natsuki e4c at lhide
    hide natsuki
    mc "Только не навернись и никуда не воткнись!"
    "Скоро мне придётся в коридорах ставить отбойники и направляющие стрелки..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom with wiperight
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 65
        clock = (19, 55)

    phone register "mc_n_chat":
        "mc" "Жива? Успела добежать? Без происшествий?"

    phone discussion "mc_n_chat":
        "n" "Да, в порядке!"
        "mc" "Рад слышать"
        "n" "Папа только что вернулся"
    $ phone.system.clock = (19, 56)
    phone discussion "mc_n_chat":
        "n" "И он снова не в духе..."
        "mc" "Что случилось?"
        "n" "Опять что-то с работой"
        "n" "Не знаю короче"
        "mc" "Под горячую руку не попала?"
        "n" "Нет, её и нет"
        "n" "Сейчас папа не настолько злой + я ничего такого не сделала + он не знает, что я к тебе ходила"
    python in phone.system:
        battery_level = 64
        clock = (19, 57)
    phone discussion "mc_n_chat":
        "mc" "Ясно"
        "n" "Но с работой у него там серьёзные проблемы"
        "n" "Всё может дойти до того, что его уволить могут"
        "mc" "Мда, чем дальше в лес..."
        "n" "Тем скибиди доп доп ес ес"
        "n" "Хватит, ты меня уже заболтал сегодня!"
        "n" "Мне надо идти ужинать"
        "mc" "Приятного"
        "n" "Спс"
    $ phone.system.clock = (19, 58)

    phone end discussion transition

    call skip_block_off
    mc "Пф-ф-ф..."
    "Да, сегодня реально не мой день."
    "Всё не так, всё на перекосяк...{w}ещё эта разборка кондитерская...{w}и Нацуки со своими бестолковыми мемами, как вишенка на этом невкусном тортике."
    "Я уже догадался, что она их вставляет, куда ни попадя, чтобы внимание привлечь и «повеселить» собеседника."
    "Но это уже какой-то испанский стыд."
    "А это в свою очередь означает что?"
    "Правильно: с ней всё очень плохо."
    "Как я подмечал, раньше у меня такой же бзик был, поэтому понять могу."
    "Здесь важно утолить её «социальный» голод, пока это не вылилось во что-то очень хреновое."
    "Я-то ещё кое-как к этому адаптировался, правда полностью изменился..."
    "А вот Нацуки, боюсь, не выдержит всего этого и сломается."
    mc "Не в то время и не в том месте она родилась..."
    mc "Как и прошлый «я», ха-ха."
    "..."
    "Блин, а ведь я ничего не выяснил насчёт Кохаку."
    "Надо Монике написать..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 64
        clock = (20, 2)

    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        time year 2018 day 25 month 4 hour 20 minute 2
        "mc" "Мони, я поговорил с Нацуки"
        "mc" "И ничего не узнал"
        "mc" "Она сама не замечала ничего такого важного"
        "mc" "По её словам, Кохаку сначала была сдержанной, но потом её нутро вышло наружу"
        "mc" "...ну и всё"
    $ phone.system.clock = (20, 3)
    phone discussion "mc_m_chat":
        "mc" "Остальное мы уже знаем"
        "mc" "А у тебя как там дела с Юри?"
    "Вот я её завалил сообщениями..."
    "Хотя, может, она уже читает?"
    phone discussion "mc_m_chat":
        "m" "Ох, печально, что ничего нового не прояснилось"
        "m" "С Юри у меня то же самое"
        "mc" "Понятно"
        "m" "Вы смогли стих составить?)"
    $ phone.system.clock = (20, 4)
    phone discussion "mc_m_chat":
        "m" "У нас он вышел с большим трудом..."
        "mc" "Ха-ха-ха..."
        "mc" "Увидишь завтра"
        "m" "Хммм, хорошо"
        "mc" "Ладно, я за сегодня устал, так что завтра как раз увидимся"
        "m" "Согласна, я тоже знатно размякла)"
        "m" "Бай-бай!"
        "mc" "До завтра"

    phone end discussion transition

    call skip_block_off
    mc "Завтра -- до завтра, завтра -- до завтра..."
    "У меня уже настолько мозг расжижился, что предложения нормально не составишь."
    mc "У-у-угх..."
    "Не, всё, не могу больше думать."
    "Самое время, чтобы расслабиться."
    "...за избитой музыкой или внеочередным видосом..."
    call window_close

    $ nightmare_active = True

    call nightmare_act_1_day_10_2
    $ _history_list.clear()

    call window_open
    scene bg bedroom at mc_bed
    show dark:
        align (0.5, 0.5) anchor (0.5, 0.5) zoom 1.2
    mc "{sc=3}А-А-А-А-А-А-А!!!{/sc}{nw}" with shake(time=2.0)
    mc "{sc=3}............{/sc}"
    mc "{sc=2}.........{/sc}"
    mc "{sc=1}......{/sc}"
    mc "{sc=0.5}...{/sc}"
    mc "Дерьмо..."
    call window_close

    $ nightmare_active = False

    return
