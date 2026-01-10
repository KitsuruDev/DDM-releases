
label act_1_day_6:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d5.unlocked == False:
        $ ach_a1_d5.unlock()

    pause 7.0
    hide loading_sign_mc with dissolve
    pause 1.0

    show screen new_day(episode) with dissolve_scene_full
    pause 5.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    "..."
    mc "...спать уже не хочется."
    "Тогда...{w}сразу отпишусь Монике..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = False
        battery_level = 48
        clock = (8, 58)

    phone discussion "mc_m_chat"
    $ plot_pause()
    "Практически 9..."
    "..."
    "Просто совпадение..."
    "..."
    "Может, всё-таки пойти к Сайори?..."
    "Да, это был чёртов кошмар, да, чисто физически она не успеет повеситься, потому что её мама дома..."
    "...но я не знаю, насколько мы задержимся..."
    "...либо я СЛИШКОМ переживаю."
    "..."
    "Так, нет."
    "Мы отпишемся Монике, я быстро с ней всё обсужу, а там уже подумаем."
    "Если Нацуки и Юри всё ещё не помирятся, то пойдём сразу к Сайори."
    "Так, включить вай-фай."
    window hide

    call phone_status_bar_button('wifi', disable = False)

    $ phone.system.clock = (8, 59)

    phone discussion "mc_m_chat":
        time year 2018 day 21 month 4 hour 8 minute 59
        "mc" "Моника, привет. В принципе, я буду готов выйти где-то через 15-20 минут"
    "Да, примерно столько..."
    "Сходить в туалет, умыться, пожрать, переодеться..."
    phone discussion "mc_m_chat":
        "m" "О, с добрым утром, Макс!"
        "mc" "...спасибо?"
        "m" "Да ладно, это я так)"
    $ phone.system.clock = (9, 0)
    phone discussion "mc_m_chat":
        "mc" "Тебя устроит мой приход в это время?"
        "m" "Да"
        "mc" "А ты же дома с родителями?"
        "m" "Нет, я одна"
    "Тоже родители отдельно..."
    "Япония -- большая семейная ирония."
    phone discussion "mc_m_chat":
        "mc" "А, хорошо"
        "mc" "Что ж, тогда встаю с кровати и начинаю готовиться"
    $ phone.system.clock = (9, 1)
    phone discussion "mc_m_chat":
        "m" "Ты даже с кровати не встал?"
        "mc" "Да"
        "m" "Ну ты и соня)"
        "mc" "Не, Моника, это вы все сплошные жаворонки, полные энергии"
        "m" "Хахаха)"
        "mc" "Кстати, с Юри и Нацуки тишина?"
        "m" "Ага, ничего нового не произошло"
    $ phone.system.clock = (9, 2)
    phone discussion "mc_m_chat":
        "mc" "Ясно"
        "m" "Ладненько, Макс, вставай"
        "m" "Жду тебя"
        "mc" "Ок"
        "m" "А, ещё!"
        "m" "Ты запомнил дорогу до моего дома?"
        "mc" "Примерно..."
        "m" "На всякий случай напомню"
    python in phone.system:
        clock = (9, 3)
        battery_level = 47
    phone discussion "mc_m_chat":
        "m" "От своего дома идёшь в сторону школы, на полпути сворачиваешь к единственному небольшому перекрёстку, от него идёшь на восток к главной улице"
        "m" "Как выйдешь на неё, пойдёшь вдоль этой улицы на север и свернёшь налево на первую зигзагообразную улицу"
    $ phone.system.clock = (9, 4)
    phone discussion "mc_m_chat":
        "m" "Дойдёшь по ней до ещё одного перекрёстка и там на углу будем мой двухэтажный дом"
        "m" "Его-то, надеюсь, помнишь?)"
    "Ё-моё..."
    phone discussion "mc_m_chat":
        "mc" "Такой дом трудно забыть"
    $ phone.system.clock = (9, 5)
    phone discussion "mc_m_chat":
        "m" "Хаха)"
        "m" "Если вдруг заблудешься, можешь мне написать"
        "m" "Я ближайшие районы хорошо знаю"
        "mc" "Понял-принял"
    "...нет, пока оставлю вай-фай, мало ли Моника ещё что-то напишет..."
    $ phone.system.clock = (9, 6)

    phone end discussion transition

    call skip_block_off
    mc "Капец какой-то..."
    "Узкие и запутанные улицы..."
    "Вот сколько не живу в этой стране, а привыкнуть к такому не могу."
    "Некомфортно."
    "Благо не везде так..."
    "..."
    "А вот, кстати...{w}этот...{w}отвратительный стих...{w}нужен вообще?"
    "Показывать его Монике или пошёл он к чёрту..."
    "Пугать же её не хочется..."
    "..."
    "Ладно, возьму, лишним не будет..."
    "Всё равно я планировал ей рассказать об этом кошмаре."
    "Моника мне уже вчера сказала, что скопление переживаний внутри пагубно влияет на психическое состояние."
    "Я и так прекрасно об этом знал, но...{w}что-то во мне торкнуло..."
    "Странное ощущение."
    play sound mc_sneeze
    pause 0.577
    with vpunch
    pause 1.0
    mc "Во, правда..."
    "Окей, сейчас быстро разбираемся с утренней рутиной и бодрым шагом идём к Монике."
    "Чем быстрее со всем разберёмся, тем быстрее окажемся у Сайори..."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg monika house outside day with wipeleft_scene
    "Спустя 40 минут с момента переписки я наконец-то вышел...{w}не, ну вы посмотрите, какой «жирный» дом!"
    "На самом деле я предполагал, что Моника -- богатая особа, с её-то внешностью и увлечением роялем."
    "Но даже так..."
    mc "Мне как-то не по себе..."
    "Чувствую себя каким-то плебеем, который пришёл на поклон к патрицианке."

    scene bg monika house outside day at monika_gate with dissolve
    pause 0.25
    "..."
    mc "Так..."
    "Где тут звонок?"
    play sound mc_sneeze
    pause 0.577
    with vpunch
    pause 1.0
    mc "Да что такое?!--{nw}"
    m "{size=19}О, ты пришёл!{/size}"
    m "{size=19}Сейчас открою!{/size}"
    "Чего я расчихался?!"
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg monika house hallway day
    show monika forward green_hoodie happ cm oe at t11
    with wipeleft_scene
    show monika om ce
    m "Я уже начала волноваться, думала, что ты заплутал в домах, ха-ха!"
    show monika cm ce
    mc "Пф, твою «крепость» ни с чем не спутать."
    show monika om oe lpoint
    m "Ну, ты прав."
    show monika dist mb oe ldown
    m "Большинство домов достаточно компактны и однотипны."
    show monika ma
    mc "Я вижу."
    "Мне показалось, или это было оскорбление по отношению к бедным?"
    show monika happ om oe
    m "Ладно, не об этом."
    play music mc_with_monika
    show monika lpoint
    m "Давай в гостиную, посмотрим твои стихи, всё обсудим."
    show monika cm oe ldown
    mc "Хорошо."
    hide monika with easeoutright
    pause 0.2
    "Она бегает босиком по дому?"
    show monika lean green_hoodie happ cm oe at t_monika_watch with easeinright
    show monika om ce
    m "Только ботинки сними!"
    show monika cm ce
    mc "Да-да..."
    hide monika cm ce with easeoutright
    "Хм..."
    "У неё очень...{w}грациозные ноги..."
    "..."
    "Хорош думать!" with vpunch
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day
    show monika forward green_hoodie happ cm oe at t11
    with wipeleft_scene
    show monika om ce lpoint rhip
    m "Чувствуй себя как дома!"
    show monika cm ce ldown rdown
    mc "Ого..."
    show monika cm oe
    mc "Тут прямо ни пылинки."
    mc "Очень усердно убираешься?"
    show monika om ce
    m "Это громко сказано."
    show monika om oe lpoint
    m "Провожу уборку раз в месяц, то есть перед приездами родителей."
    show monika ldown
    m "Я же здесь одна, поэтому в основном всё чисто."
    show monika cm oe
    mc "Понятненько."
    show monika neut cm oe
    mc "Но тебе не страшно одной жить?"
    show monika happ cm oe
    mc "Япония -- безопасная страна, да, но тем не менее..."
    show monika om ce
    m "Не переживай, Макс, у меня есть меры на этот счёт."
    show monika cm
    mc "А, ладно..."
    "Не знаю, что там за меры, но сказала она это уверенно."
    show monika om oe lpoint
    m "Давай лучше присядем, а то замучаемся стоять."
    show monika cm ce ldown
    call window_close

    hide monika with dissolve
    pause 0.2
    scene bg monika house livingroom day at monika_sofa
    show monika forward green_hoodie happ cm ce at e11
    with dissolve
    pause 0.25
    show monika cm oe

    call window_open
    show monika oe
    mc "Я чуть подальше сяду..."
    show monika om b1f
    m "Что, боишься меня?"
    show monika neut cm oe brow
    mc "Нет, я что-то сейчас расчихался, не знаю, почему."
    mc "Не хочу тебя заразить."
    show monika om
    m "Нанервничался вчера?"
    show monika cm
    mc "Есть такое."
    show monika e2a
    mc "Мне даже кошмар приснился один...{w}после которого я ночью проснулся и написал ещё один стих."
    mc "Потому что уснуть не мог..."
    show monika om
    m "Ох..."
    show monika cm
    mc "Его я тоже принёс."
    show monika oe
    play sound paper_torn_out
    pause 1.0
    mc "Но давай сначала быстро разберёмся с моим стилем."
    show monika oe
    mc "Ты уже проанализировала мои творения?"
    show monika happ om oe
    m "Конечно!"
    show monika oe lpoint
    m "Только сейчас их достану."
    show monika om ce ldown
    m "Так-так-так~"
    show monika cm
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg monika house livingroom day at monika_sofa
    show monika forward green_hoodie neut cm oe at e11
    with wiperight
    show monika mh oe lpoint
    m "Итак, смотри."
    show monika ldown
    m "Как я могу судить, у тебя уже есть задатки собственного стиля."
    m "Наиболее складное стихотворение вышло при подражании стилю Нацуки, что и так очевидно."
    show monika cm
    mc "Угу."
    show monika mh
    m "Ты способен закладывать контекстный смысл, как я ранее вроде говорила."
    m "При этом ты не забываешь о некой..."
    show monika curi om e1c
    m "...нет, не приземлённости..."
    show monika neut mh oe lpoint
    m "...в общем, ты придерживаешься «реализма» с примесью воображения."
    m "Иными словами, ты способен уходить в некую художественность, но неглубоко."
    show monika cm oe ldown
    mc "Вот как?"
    show monika mh
    m "Да."
    show monika lpoint
    m "Тебе стоит опираться исключительно на себя, подчерпывая некоторые детали у других."
    show monika cm ldown
    mc "Грубо говоря, особо ничего не поменялось относительно моего первого стиха."
    show monika om e1b
    m "Ну..."
    show monika happ om oe
    m "...у тебя уже есть представление обо всём этом, а также опыт написания стихотворений."
    show monika neut cm oe
    mc "Но подожди."
    mc "Ты ничего не сказала про свой стиль."
    show monika om oe
    m "Есть ли в этом смысл?"
    show monika dist om oe
    m "Моя абстракность--{nw}"
    show monika vsur md oe
    mc "Наиболее близка мне из всех стилей."
    m "..."
    mc "Я серьёзно."
    "Сказал, как есть, не более."
    show monika om oe n3
    m "Правда?..."
    show monika cm oe
    mc "Абсолютно."
    mc "У тебя как раз тоже примесь «реализма» и воображения."
    mc "Если бы я не был ограничен стилями других участниц, то писал бы в стиле, близком к твоему."
    mc "Возможно, из-за своего склада ума, потому что постоянно скатываюсь в какие-то размышления..."
    mc "Так что..."
    mc "Я могу подчерпывать у тебя чуть больше деталей, чем у других?"
    mc "Равняться на тебя, так сказать."
    "Вот реально, в её стихах больше всего подходящего для меня материала."
    "Надо потом попробовать составить стих на одном её каком-нибудь примере..."
    show monika om oe
    m "Э-э-э..."
    show monika nerv om oe
    m "Конечно!"
    show monika ce
    m "Ради этого и создавался Литературный клуб!"
    show monika neut mh ce
    m "Чтобы мы могли делиться, общаться, радоваться, учиться..."
    mc "Моника?"
    m "...понимать, созидать, уважать, любить..."
    mc "Моника, ау!"
    with vpunch
    show monika pani om e4c b1a n1
    m "А-а-а!"
    show monika shoc md oe -b1a
    mc "Что с тобой?"
    show monika pout om oe
    m "А-а-а..."
    show monika happ om ce
    m "Всё хорошо!"
    show monika dist om oe
    m "Просто...{w}это..."
    show monika ce
    m "...неожиданно..."
    show monika neut cm oe
    mc "Не сказал бы, потому что это было наиболее очевидно."
    mc "Странно, что ты этого не заметила."
    show monika happ om oe
    m "Но теперь мы оба об этом знаем, верно?"
    show monika cm oe
    mc "Да..."
    "..."
    stop music fadeout 6.0
    show monika neut cm oe
    mc "Что будем делать с клубом?"
    show monika curi om oe
    m "А как же твой пятый стих и кошмар?"
    show monika md
    mc "...я прикинул, что если мы воссоединим клуб, то ни в кошмаре, ни в стихе никакого смысла не будет."
    show monika neut mh oe
    m "Уверен?"
    show monika cm
    mc "Абсолютно."
    mc "Я просто вчера реально нанервничался."
    mc "Так что там по клубу?"
    show monika om
    m "Пока Юри и Нацуки молчат."
    show monika cm
    mc "Ну не будем же мы тупо сидеть и ждать, когда они помирятся?"
    show monika dist om oe
    m "Тоже верно..."
    show monika cm
    mc "Может, тогда вместе навестим Сайори?"
    show monika neut om oe lpoint
    m "Как раньше говорила, нам нужна Нацуки."
    show monika cm ldown
    mc "...но мы же не знаем, сколько времени пройдёт!"
    mc "Нам нужно УЖЕ что-то делать, пока не стало хуже."
    show monika sad cm oe
    mc "Аргх, всё могло пройти менее болезнено, если бы я додавил свою инициативу в этом конфликте..."
    mc "Но постоянно, когда дело доходит до меня, то всё идёт через задницу."
    show monika mh
    m "Макс, ты тоже человек..."
    m "Ты не можешь всё делать идеально."
    show monika neut mh oe
    m "Только методом проб и ошибок можно добиться результата."
    show monika sad cm oe
    mc "Пф-ф, Моника, я не хочу ошибаться, потому что устал от этого."
    mc "Ничего полезного от них не получаю, только одно дерьмо в свой адрес."
    mc "Вот, например..."
    mc "Написал по предмету тест ниже, чем думал, из-за глупых ошибок?"
    mc "Все задним числом, но говорят, что ты тупой, не оправдал ожидания, наплевав, что ты готовился, тратил силы и старался."
    mc "Ошибся в чём-то незначительном, помогая родителям?"
    mc "Принимай слова, какой ты криворукий полудурок, хотя ошибка настолько плёвая, что решается буквально за минуту."
    mc "Сделал хотя бы что-то не так по чьему-то поручению, причём из-за того, что поручитель всё отвратительно объяснил?"
    mc "Сразу начинаются возмущения, что ты глухой и тупой."
    mc "Пойми, в гробу я вертел все эти ошибки."
    show monika neut cm oe
    mc "Нет, то, что ты сказала, я, конечно, прекрасно понимаю..."
    mc "Но каким, блин, образом я должен мотивироваться что-то делать дальше, когда тебя искоса или напрямую топят и гнобят за каждый {b}не{/b}умышленный косяк?"
    mc "Вместо того, чтобы сразу проработать ошибку, тебе начинают проедать плешь и самоутверждаться на твоём фоне."
    mc "Уже который раз такое было..."
    show monika om
    m "Но ведь сейчас ты один...{w}да?"
    show monika cm
    mc "Да."
    mc "Когда я сюда переехал, то стал чувствовать себя в разы легче."
    mc "Да, мне тяжелее решать проблемы, да, я делаю не всё правильно и как надо..."
    mc "...но мне никто не гундит под ухом, никто не фарширует мозги хрен пойми чем, благодаря чему я могу в разы спокойнее, быстрее и эффективнее прорабатывать свои ошибки."
    mc "Да и привык я постоянно находиться один."
    mc "Я так и чувствую себя лучше, и работаю эффективнее."
    mc "Это всё я к чему..."
    mc "Я не хочу делать ещё одну ошибку, надеясь, что этот конфликт сам рассосётся."
    mc "Но при этом...{w}я чувствую себя таким пожёванным после вчерашних нервов..."

    scene black with dissolve
    mc "Мда, я думал, что здесь меня будет беспокоить только учёба, а в итоге..."
    mc "Негативный уровень, можно сказать, не спал."
    mc "А ещё разнылся тут на ровном месте..."
    mc "Какой же я слабый, а?"
    mc "Ха-ха..."
    "..."
    "Моника...{w}обняла меня?..."
    m "Нет, Макс, ты не слабый...{w}и это не нытьё."
    mc "...почему?"
    m "Это как реакция на физическую боль."
    m "Если человек будет сдерживаться, то ему будет в разы тяжелее и больнее, чем тому, кто будет кричать."
    mc "Вот только всем на это плевать."
    mc "Никто не хочет слушать."
    mc "Наоборот, даже могут облить дерьмом или самоутвердиться, как сказал ранее."
    m "Тогда это поганые и гнилые люди, не правда ли?"
    m "Они недостойны твоего внимания, даже капли, потому что они его никогда не оправдают."
    m "Главное, чтобы у тебя была опора, ведь в одиночку переживать такое тяжело, как я говорила тебе вчера."
    m "Надо сбрасывать с себя весь этот негатив тому, кому ты можешь доверять."
    m "Поэтому...{w}ты можешь мне доверять, Макс."
    m "Я понимаю тебя."
    m "И если быть честной, у меня примерно такая же проблема, хоть она и по-другому выражена..."
    m "Правда, тут больше акцент не на адекватную проработку ошибок, а на нахождение общего языка."
    mc "М-м..."
    mc "Можешь мне рассказать, если не против."
    m "Папа и мама постоянно обо мне заботились в детстве: проводили со мной время, делали подарки..."
    m "Это было беззаботное время."
    m "Но когда я стала ходить в школу, они захотели сделать из меня «успешную» дочь."
    m "Кружки, активности, репетиторство..."
    m "Куда меня только не гоняли, ха-ха..."
    m "Я научилась плавать, играть на клавишных инструментах, заниматься бегом, ораторством..."
    m "На меня возложили большие ожидания."
    m "Среди этого водоворота я поняла, что пропускаю мимо себя жизнь."
    m "Все мои одноклассники жили проще: они радовались, общались, занимались любимыми делами..."
    m "А у меня не было выбора."
    m "Я была совершенно на другом уровне."
    m "Осознав всё это ближе к концу средней школы, я полностью потеряла смысл и удовольствие от подобных занятий, кроме рояля."
    m "В общем, у меня ничего не было: не было друзей, не было приятных моментов..."
    m "Я очень долго разговаривала с родителями на эту тему, им совершенно не нравилось, что я пошла наперекор их ожиданиям."
    m "Один раз чуть не дошло до скандала..."
    m "В итоге мы сошлись на том...{w}что меня отправят в эту школу, но при этом я буду жить одна в новом доме."
    m "Я здесь всего чуть больше года."
    m "Начала учиться на втором году старшей школы."
    m "Сразу решила окунуться в социум с головой: участвовала в клубной деятельности..."
    m "...впрочем, с этого момента ты уже и сам знаешь."
    mc "Вот оно как..."
    m "Я думала, что вот это именно то, чего я хотела, однако..."
    m "С клубами оказалось всё сложно."
    m "Учёба ещё даёт нагрузку..."
    m "А родители..."
    m "...они всё ещё горят «этой» идеей."
    m "Только теперь она будет выражена в выборе университета."
    m "И будущей профессии."
    mc "Вообще-то это твоя жизнь, Моника."
    mc "И только тебе решать, куда идти дальше."
    mc "Не родители же за тебя жить будут, не так ли?"
    m "Я понимаю, уже говорила с ними на этот счёт."
    m "И пока ничего хорошего..."
    mc "Моника, не отчаивайся."
    mc "Слышишь?"
    mc "Тебе надо продолжать бороться, чтобы жить счастливой жизнью."

    scene bg monika house livingroom day at monika_sofa
    show monika forward green_hoodie sad cm oe at e11
    with dissolve
    show monika mh
    m "Макс..."
    show monika ce
    m "Я скоро тресну пополам..."
    show monika cm
    mc "Не надо!"
    show monika ma oe
    mc "Ты нам целой нужна!"
    play sound mc_sneeze
    pause 0.577
    with vpunch
    pause 1.0
    mc "Вот, да!"
    show monika happ om e1b b1b
    m "Хе-хе-хе..."
    show monika sad cm oe -b1b
    mc "Тебе просто нужно отдохнуть и восстановиться."
    show monika mh
    m "Но как?"
    show monika e1b
    m "Поговорить, кроме тебя, не с кем, у участниц клуба своих проблем полно, а ещё нужно срочно решать проблемы, которые наваливаются друг за другом..."
    show monika neut cm oe n3
    mc "Поэтому я сейчас возьму себя в руки, Моника, и помогу тебе хотя бы с клубом."
    mc "Можешь чуточку расслабиться."
    mc "И вообще давай так: сейчас мы спишемся с Юри, ты немного отдохнёшь, а потом либо встретим Юри и Нацуки, либо пойдём к Сайори."
    mc "Ты согласна?"
    m "..."
    show monika me
    "Моника...{w}обхватила меня руками?"
    mc "Стой-стой-стой, я же сегодня расчихался--{nw}"
    show monika ce
    call window_close

    show layer master:
        anchor (0.5, 0.5) pos (640, 360)
        linear 4 zoom 4.0

    pause 2.5

    scene black with dissolve
    pause 0.25
    call window_open
    mc "МФ!"
    "Вот ЭТОГО я вообще не ожидал!"
    "Второй неожиданный поцелуй за мою жизнь..."
    "..."
    "Стоп...{w}он всё ещё продолжается..."
    "Это...{w}приятно...{w}и абсурдно одновременно."
    "Бестолковое касание участками тела с тонкой кожей."
    "Но...{w}это реально приятно...{w}почему?"
    "Мысли уплывают...{w}голова куда-то уехала...{w}лишь бы Монику не заразить..."
    m "..."
    m "Спасибо тебе, Макс..."
    mc "...пожа...{w}луй...{w}ста..."
    m "Хах, первый раз всегда непривычен, да?"
    m "Я тоже неожидала такие ощущения."
    mc "..."
    "Умолчу про вчерашний инцидент..."
    m "Напишем Юри с моего телефона?"
    mc "Угу."
    mc "У меня нет её номера."
    m "Вот как..."
    "Выходит...{w}Моника тоже ко мне неравнодушна...{w}даже слишком!"
    "Теперь понятно, что она вчера ёрничала во время разговора..."
    "Блин, меньше недели прошло, а я уже в каком-то недолюбовном треугольнике..."
    "Как будто судьба решила надо мной знатно приколоться."
    "Хотя...{w}я и не против..."
    "Лучше уж такие приколы, чем неприятные сюрпризы в виде нескончаемых проблем."
    call window_close

    call window_dialog_long_transition("y")

    call window_open
    scene bg yuri house bedroom day at yuri_bed
    with dissolve_scene_full
    y "..."
    y "Как я могла забыть про Нацуки..."
    "Я уже несколько раз прокрутила у себя в голове события последней недели..."
    "И каждый раз я не нахожу моментов, где я её игнорировала."
    y "Не понимаю..."
    "Всё было, как и прежде."
    "..."
    "Или я...{w}{b}не замечала{/b} такие моменты?"
    "Да, соглашусь с Нацуки, в последнее время Макс занял у меня центральный фокус..."
    "Но...{w}настолько сильно?"
    y "Угх..."
    y "Неужели я и правда забыла про Нацуки..."
    "..."
    "Вне зависимости от правдивости этой фразы мне нужно с ней поговорить."
    "Она обиделась именно на меня."
    "Только я могу решить эту проблему..."
    "Сейчас клуб в моих руках."
    "Конечно, я не готова к такой ответственности, но ничего не попишешь..."
    "Надо делать шаг за шагом, как говорила Котоноха."
    y "Мне нужно действовать."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg yuri house outside day with wipeleft_scene
    "И куда дальше идти?"
    "Вдруг Нацуки не дома?"
    "Или её отец не в настроении?"
    "А вдруг она куда-то ушла?"
    y "У-у-у..."
    y "Куда делась моя уверенность, которая была 5 минут назад..."
    "..."
    y "Ой, точно!"
    "Совсем забыла про чат!"
    "Надо ей написать!"
    play music ringtone_yuri_1
    y "{sc=3}А-А-А!!!{/sc}" with vpunch
    "{sc=3}Кто это?!{/sc}"
    "{sc=3}...{/sc}"
    y "{sc=3}Н-Нацуки?!{/sc}"
    "{sc=3}Но почему?!{/sc}"
    call skip_block_on
    call window_close

    phone call_accept "n"
    phone call "n"

    stop music
    play phone_sound ringtone_yuri_2
    pause 0.75

    call window_open
    call skip_block_off
    phone_n "Алло!"
    phone_n "Ал-л-ло!"
    phone_y "Тут-тут-тут!"
    phone_n "Почему так долго не брала трубку?!"
    phone_y "Я...{w}умф..."
    phone_n "Ладно, забыли."
    phone_n "Слушай..."
    phone_n "..."
    phone_y "..."
    phone_n "Ты здесь?"
    phone_y "...угу."
    phone_n "Так вот, мне было больно."
    phone_n "Но я поняла, как глупо себя повела..."
    phone_n "Короче, когда я успокоилась, то осознала, насколько {b}сильно{/b} ты поменялась из-за Макса за последнюю неделю."
    phone_n "Ты стала сильнее срываться."
    phone_y "Но ты тоже...{w}стала чаще вспыливать..."
    phone_n "НЕ НАЧИНАЙ!" with vpunch
    phone_y "..."
    phone_n "..."
    phone_n "...ладно, ты права."
    phone_n "Я спровоцировала твоё демоническое состояние что в начале недели, что вчера."
    phone_n "Я в этом виновата, да."
    phone_n "Но знаешь почему?"
    phone_n "Хотя я тебе только что уже сказала."
    phone_y "...Макс?..."
    phone_n "Угадала!"
    phone_n "Ты стала постоянно о нём думать!"
    phone_n "Раньше мы с тобой часто общались, ты поддерживала любой разговор, даже если ты в нём не разбиралась..."
    phone_n "...но теперь я будто только мешаюсь у тебя под ногами."
    phone_n "Ты реже выходишь на связь."
    phone_n "Стала более закрытой, хоть и решительнее."
    phone_n "Чаще выходишь из себя."
    phone_n "Юри, ты, как подруга, охладела ко мне!"
    phone_n "Мне это {b}не нравится{/b}!"
    phone_n "Нет, я не говорю тебе бросить свою...{w}идею фикс..."
    phone_n "Просто про меня не забывай, а?"
    phone_n "У меня и так друзей нет."
    phone_n "Котоноха не такой близкий человек, как ты."
    phone_n "Бывшие участники Клуба выпечки практически перестали со мной общаться."
    phone_n "С Эми тоже как-то всё сошло на нет."
    phone_n "Моника вечно при делах, к тому же она по сравнению со мной даже рядом не стоит..."
    phone_n "С Сайори нормально поговорить не выходит, да и сама она тоже не норовит это сделать..."
    phone_n "Макс вроде бы может поддержать диалог, но он, как Моника, -- другой уровень."
    phone_n "Остаёшься только ты -- единственный человек, с которым я могу хорошо провести время."
    phone_n "А теперь я и тебя теряю."
    phone_y "..."
    phone_y "Прости..."
    phone_n "Да что толку от этих \"прости\"?!"
    phone_n "Ничего не поменяется!"
    phone_n "Я просто хочу, чтобы ты осталась той Юри, которую я знаю и которая меня помнит."
    phone_n "Или..."
    phone_n "..."
    phone_n "...хорошо, не так."
    phone_n "Занимайся чем угодно, развивайся, строй отношения..."
    phone_n "...но только меня не бросай."
    phone_n "Пожалуйста..."
    phone_y "..."
    phone_n "..."
    phone_y "Я не брошу тебя, Нацуки..."
    phone_n "..."
    phone_n "...честно?"
    phone_y "Да."
    phone_y "Я не хочу этого."
    phone_n "Хочется в это верить..."
    phone_y "..."
    phone_n "..."
    phone_y "..."
    phone_n "Может, повернёшься уже в мою сторону?"
    phone_n "А то мне надоело смотреть на твоё лицо и «буфера» сбоку."
    phone_y "...что?"
    phone_n "Я стою в конце твоей улицы."
    phone_n "Ты же ведь не думала, что я оставлю тебя даже после всего того, что произошло?"
    window hide

    phone end call "21/04/2018" transition

    window auto
    y "Хе..."
    y "Хе-хе-хе..."
    call window_close

    call plot_transition

    call window_open
    scene bg niigata street suburban 11 day
    show natsuki turned casual fc pout cm oe lhip rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Хоть бы ветровку сняла, сваришься же."
    show natsuki cm
    y "Моя футболка слишком тонкая."
    show natsuki curi cm oe
    y "Без накидки меня может продуть."
    show natsuki om
    n "Ты это говоришь подруге, которая как раз в одной футболке и которая тоньше тебя."
    show natsuki cm
    y "..."
    show natsuki neut om e4a ldown rdown
    n "Ай, проехали."
    show natsuki cm
    n "..."
    y "..."
    show natsuki anno om ce lhip rhip
    n "Ой, да нечего мне больше сказать."
    show natsuki curi om oe
    n "Вроде бы и так всё обсудили..."
    show natsuki e1b ldown
    n "Cвоё я высказала."
    show natsuki pout cm oe
    y "Если бы я знала раньше..."
    show natsuki om rdown
    n "Нет, Юри, не начинай, тема закрыта."
    show natsuki anno om ce
    n "Точка."
    show natsuki cm
    y "Н-но это же ведь так--{nw}"
    show natsuki angr om oe lhip rhip
    n "Блин, Юри!"
    n "Я о тебе забочусь!"
    show natsuki pout om oe rdown
    n "Если ты будешь закапываться, то твои выкрутасы будут набирать опасные обороты."
    show natsuki curi om oe ldown
    n "Оно тебе надо?"
    show natsuki cm
    y "Нет..."
    show natsuki neut om oe
    n "Правильно."
    show natsuki cm

    scene bg niigata street suburban 12 day
    show natsuki turned casual fc pout cm e1b at t11
    with wipeleft_scene
    show natsuki om lhip rhip
    n "Если ничего не предпринять, то ты так себя до ручки доведёшь."
    show natsuki cm
    y "Ум..."
    show natsuki neut cm oe ldown rdown
    y "Ты прямо как Макс."
    show natsuki doub cm oe
    y "Не надо за меня так переживать..."
    y "Я же раньше как-то жила..."
    show natsuki om lhip rhip
    n "И это говорит мне человек, который решил на днях попробовать резать себе руки?"
    show natsuki cm
    y "..."
    show natsuki pout om oe
    n "Юри, пойми же ты наконец: ты ни в чём не виновата!"
    show natsuki e1b
    n "Хоть я и не знаю, что ты там пережила..."
    show natsuki cm
    y "..."
    show natsuki om ce ldown rdown
    n "Перестань на себя накручивать!"
    show natsuki neut om e1b
    n "Виновато только непонятное событие, про которое ты до сих пор не хочешь мне рассказывать, но которое ты расплывчато упоминала, -- это раз."
    show natsuki oe
    n "Два -- я иногда провоцирую тебя на негатив, сама того не замечая."
    show natsuki pout om e1b lhip rhip
    n "{size=19}Чтоб я так всегда всё с холодной головой обдумывала...{/size}"
    show natsuki neut om oe
    n "Три..."
    show natsuki curi om e1c
    n "...а что три..."
    show natsuki pout om oe ldown rdown
    n "Короче, это не повод травмировать себя, лучше от этого никому не станет: ни мне, ни тебе, ни Литературному клубу."
    show natsuki ce
    n "Я понимаю, что держать свои переживания внутри -- очень плохо, но выводить их через порезы..."
    show natsuki sad om oe rhip
    n "...нет, тебе точно нужна помощь, хоть какая-нибудь: дружеская, психологическая, бла-бла-бла..."
    show natsuki neut om oe rdown
    n "Впрочем, поэтому я взяла себя в руки и пришла к тебе."
    show natsuki cm
    y "..."
    show natsuki pout cm oe
    y "...без тех порезов мне было бы хуже..."
    show natsuki om
    n "Тем более!"
    show natsuki cm

    scene bg niigata street suburban 13 day
    show natsuki turned casual fc pani me oe at t11
    with wipeleft_scene
    show natsuki cm
    y "Нет, ты не поняла: это был самый лучший вариант из всех существующих...{nw}"
    show natsuki om ce
    n "Нет же!" with vpunch
    show natsuki oe lhip rhip
    n "Тебе надо просто начать жить с чистого листа, выбросив из головы всю эту боль вперемешку с дурью!"
    show natsuki vang cm oe
    y "Если бы я могла, то я бы так сделала!"
    show natsuki om
    n "Не надо тут оправдываться!"
    show natsuki ce
    n "Твой бзик в голове начинает мутировать в страшное нечто!"
    show natsuki cm
    y "Бзик?!"
    show natsuki cross casual ff angr om oe
    n "И вот опять ты вспыхнула!"
    show natsuki cm
    y "Гх!..."
    show natsuki pani me oe
    y "...Нацуки, клянусь...{w}было бы так легко, я бы избавилась от всего..."
    show natsuki om ce
    n "И вот именно поэтому тебе нужна помощь!"
    show natsuki turned casual fc pout om oe lhip rhip
    n "Если продолжишь пытаться решать свою проблему в одиночку, это сведёт тебя в могилу."
    show natsuki cm
    y "..."
    show natsuki neut om oe
    n "И вообще, мне интересно..."
    show natsuki doub mh oe ldown
    n "Твой любимый Макс знает же про твои порезы?"
    show natsuki cm
    y "...да, я ему показывала их пару дней назад."
    show natsuki mh
    n "И как он отреагировал?"
    show natsuki cm
    y "Негативно."
    y "Сильно забеспокоился, попросил их обработать и обернуть бинтами, а ещё хотел выяснить, из-за чего всё это я делаю..."
    y "...на меня тогда столько эмоций нахлынуло, что я не смогла что-либо сказать..."
    show natsuki mh ce lhip
    n "Во-о-от."
    show natsuki om oe
    n "А как думаешь, будет ли он рад тому, что ты скрываешь в себе такую опасную травму, с которой справиться не можешь?"
    show natsuki cm
    y "..."
    show natsuki pout om oe
    n "Вот в этом и кроется вся твоя проблема, Юри!"
    n "В застенчивости и неуместной стыдливости."
    show natsuki e1b
    n "Это тянет тебя на дно."
    show natsuki neut om oe b1d
    n "Если хочешь жить счастливой жизнью вместе со своим любимым Максом, то тебе придётся через «не хочу» поведать о своей беде и уже вместе её решать."
    show natsuki cm
    y "..."

    scene bg niigata park small entrance 1
    show natsuki turned casual neut cm e1b at t11
    with wipeleft_scene
    show natsuki om
    n "И знаешь..."
    show natsuki worr om ce
    n "Раз ты так по уши влюбилась, то я в-о-з-м-о-ж-н-о помогу тебе подойти к Максу чуточку ближе."
    show natsuki curi om e1b
    n "Не как Котоноха, у который похабные мысли в любовных облаках витают..."
    show natsuki pani om ce
    n "Фу!"
    show natsuki curi om oe
    n "...а как та, которая непосредственно общается с «объектом твоего интереса»."
    show natsuki cross casual angr om ce
    n "Но не думай, что я прям буду нянчиться и уговаривать его встречаться с тобой, угу?!"
    show natsuki cm
    y "Хе..."
    show natsuki neut cm oe
    y "Спасибо большое...{w}Нацуки..."
    show natsuki om e1b
    n "Спасибо скажешь, когда результата добьёшься."
    show natsuki cm

    scene bg niigata park small path
    show natsuki turned casual fc neut cm oe at t11
    with wipeleft_scene
    show natsuki om
    n "А сейчас я бы хотела спросить..."
    show natsuki curi om oe lhip rhip
    n "Почему ты Монике не хочешь рассказать про свои руки?"
    show natsuki cm
    y "Ну..."
    show natsuki anno cm oe ldown rdown
    y "Я не хочу волновать её почём зря."
    y "Ничего же в итоге не поменяется..."
    show natsuki om
    n "Тогда смысл вообще эту проблему решать, если так думать?"
    show natsuki neut om oe rhip
    n "Моника -- та, кто может хоть что-то предпринять."
    show natsuki pout om oe
    n "Тем более у неё деньги есть!"
    show natsuki cm
    y "Это будет грубо, Нацуки!"
    y "Не она их зарабатывает: ей родители отсылают на поддержание самостоятельной жизни."
    show natsuki cross casual ff vang cm ce
    n "Кх-х!"
    show natsuki pout om e1b
    n "Что ж с тобой делать..."
    show natsuki cm
    n "..."
    show natsuki turned casual fc pout om oe lhip
    n "А твоя мама...{w}ничего не говорила по этому поводу?"
    show natsuki cm
    y "Что она скажет, если она ещё не знает?..."
    y "А если ты про деньги, то их только на содержание и хватает..."
    show natsuki vang om ce rhip
    n "А-а-а, как же, блин, всё сложно, сплошные палки в колёса!"
    show natsuki cm
    play phone_sound new_message_yuri
    pause 1.0
    show natsuki curi cm oe
    y "Ой..."
    show natsuki om ldown rdown
    n "А?"
    show natsuki cm
    y "Это у меня что-то в телефоне..."
    call skip_block_on

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 91
        clock = (11, 32)

    phone register "y_m_chat":
        time year 2018 day 21 month 4 hour 11 minute 32
        "m" "Юри, привет. Как там у тебя дела? Ты помирилась с Нацуки или ещё нет?"

    phone discussion "y_m_chat"
    $ plot_pause()
    $ phone.system.clock = (11, 33)
    y "Моника..."
    show natsuki cross casual ff neut om e1b at t44
    n "О, зашибись, самое время помириться с остальными."
    show natsuki curi om oe
    n "Что она хоть написала?"
    show natsuki cm
    y "Спрашивает, помирилась ли я с тобой..."
    show natsuki turned casual pout om oe lhip rhip
    n "Так пиши, что да!"
    show natsuki cm
    y "Сейчас..."
    phone discussion "y_m_chat":
        "y" "Привет, Моника. Всё хорошо. Я уже помирилась"
    $ phone.system.clock = (11, 34)
    show natsuki neut cm oe ldown rdown with None
    phone discussion "y_m_chat":
        "m" "Рада слышать)"
        "m" "Вы же сейчас вместе?"
        "y" "Да"
        "m" "Можете с нами встретиться?"
    show natsuki curi cm oe
    y "\"Можете с нами встретиться?\""
    show natsuki om
    n "Чего?"
    show natsuki e1b
    n "Моника собрала весь клуб?"
    show natsuki cm
    phone discussion "y_m_chat":
        "y" "Ты не одна?"
        "m" "Нет, я сейчас у себя дома с Максом"
    $ phone.system.clock = (11, 35)
    phone discussion "y_m_chat":
        "m" "Я анализировала его стиль"
        "y" "Ааа..."
    show natsuki e2a
    y "Она у себя дома с Максом..."
    show natsuki om
    n "...чё?"
    show natsuki cm
    y "Анализировала его стиль."
    show natsuki doub om oe lhip rhip
    n "Анализировала, ага."
    show natsuki ce
    n "А потом выяснится, что она увела его у тебя из-под носа."
    show natsuki cm
    y "Нацуки...{w}молчи..."
    $ phone.system.clock = (11, 36)
    show natsuki pout om oe
    n "Ты лучше не расслабляйся, а?"
    show natsuki cm
    phone discussion "y_m_chat":
        "m" "Так вы к нам придёте?"
    show natsuki neut cm e1c ldown rdown with None
    phone discussion "y_m_chat":
        "y" "Да, мы можем"
        "m" "Отлично"
        "m" "Но я предлагаю встретиться где-то на улице по пути к дому Сайори"
    show natsuki oe
    y "Моника хочет, чтобы мы встретились с ней на улице."
    show natsuki curi cm oe
    y "Где-то по пути к дому Сайори."
    $ phone.system.battery_level = 90
    show natsuki om
    n "Чтобы мы заплутали?"
    show natsuki cm
    y "Подожди..."
    phone discussion "y_m_chat":
        "y" "В каком именно месте?"
        "m" "Ну..."
    $ phone.system.clock = (11, 37)
    phone discussion "y_m_chat":
        "m" "Вы сейчас где?"
        "y" "В парке"
        "y" "Не который в японском стиле в нашем районе, а обычный в соседнем"
        "m" "А, поняла"
        "m" "Тогда лучше встретиться..."
    show natsuki om lhip rhip
    n "Ну что там?"
    show natsuki cm
    y "Нацуки, подожди!"
    phone discussion "y_m_chat":
        "m" "О, знаю!"
        "m" "Помнишь маленькую улицу с Т-образным перекрёстком?"
    $ phone.system.clock = (11, 38)
    phone discussion "y_m_chat":
        "m" "На нём двойное зеркало для автомобилистов стоит"
        "m" "И на углу частная территория с маленьким железным забором и со столбиками на входе"
        "m" "Ещё там кусты пышные и несколько деревьев"
    show natsuki pani me oe
    y "А-а-а?..."
    show natsuki om
    n "Да что там?!"
    show natsuki curi cm oe
    y "Т-образный перекрёсток, двойное зеркало, частная территория с забором, столбиками, кустами и деревьями..."
    show natsuki anno om ce
    n "Класс, потрясающие ориентиры."
    $ phone.system.clock = (11, 39)
    show natsuki doub om oe
    n "Моника серьёзно рассчитывает, что мы сможем найти эту улицу?"
    show natsuki angr om e2b b1d
    n "Да тут каждый второй перекрёсток такой!"
    show natsuki cm
    phone discussion "y_m_chat":
        "y" "Это весьма размытые ориентиры, Моника..."
        "y" "Мы так заблудимся"
        "m" "Знаю, но не могу по-другому это описать"
        "m" "Давайте так: мы с Максом сейчас пойдём к этой улице, вы тоже потихоньку выдвигайтесь"
        "m" "По пути будем вас координировать)"
    show natsuki vang cm oe -b1d
    y "Моника хочет координировать нас в процессе своего перемещения..."
    show natsuki om
    n "Она издевается?!"
    show natsuki cross casual vang om ce
    n "Что за маразм?!"
    show natsuki cm
    $ phone.system.clock = (11, 40)
    phone discussion "y_m_chat":
        "y" "Моника, почему именно так?"
        "m" "Нам нужно как можно скорее прийти к Сайори"
        "m" "Мы и так практически всё утро потеряли"
        "m" "Чем дольше мы тянем время, тем ей хуже"
    show natsuki pout cm oe
    y "Моника пишет, что времени в обрез."
    show natsuki doub cm oe
    y "Нужно как можно скорее прийти к Сайори..."
    show natsuki turned casual doub om oe lhip rhip
    n "Как будто Сайори помрёт, если мы придём чуть позже."
    show natsuki angr cm oe
    y "Но ей больно..."
    show natsuki om
    n "А мне тоже было, знаешь ли?!"
    show natsuki neut om oe b1d ldown
    n "И вообще, как же она потом без клуба жить будет?"
    show natsuki cm
    y "Угх..."
    phone discussion "y_m_chat":
        "y" "Хорошо, Моника, мы тоже выходим"
    $ phone.system.clock = (11, 41)
    show natsuki e1b rdown with None
    phone discussion "y_m_chat":
        "y" "Пока дойдём до нашего района"
        "m" "Окей! Как до него дойдёте, напишите"

    phone end discussion transition

    call skip_block_off
    show natsuki curi cm oe -b1d
    y "Пойдём, Нацуки."
    show natsuki om lhip rhip at t11
    n "Подожди, какой \"пойдём\"?"
    show natsuki pani om oe
    n "Мы даже не знаем куда!"
    show natsuki vang cm oe
    y "Я написала Монике, что мы возвращемся в старый район, после чего отписываемся ей."
    show natsuki om
    n "Какой \"отписываемся\"?!"
    show natsuki ldown rdown
    n "Вы чё, издеваетесь?!"
    show natsuki cross casual vang om ce
    n "Почему нельзя нормально выбрать место встречи?!"
    show natsuki cm
    y "Можешь возмущаться сколько угодно, но мы уже с ней об этом договорились."
    y "Поэтому, Нацуки, как хочешь, а я возвращаюсь в наш район."
    show natsuki pani cm oe

    scene black with wipeleft_scene
    n "Эй-эй-эй, подожди меня!"
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("mc")
    $ pov_key_mobile = "m"

    call window_open
    scene black with dissolve
    pause 1.0
    mc "А если они заблудятся?"
    m "Исключено: у них под рукой мобильник с картами."
    mc "Всё равно эта идея какая-то сумбурная..."
    m "Лучше так, чем они будут описывать целый крюк, из-за чего потратят полчаса минимум."
    mc "Твоя правда..."

    scene bg monika house livingroom day at monika_sofa
    show monika forward green_hoodie happ cm oe at e11
    with dissolve
    show monika cm oe
    mc "Всё, пора идти, Моника."
    show monika neut mh oe
    m "Подожди."
    show monika curi om oe
    m "Может, я всё-таки гляну твой последний стих..."
    show monika md
    mc "Да не надо, он же неактульным станет, уже говорил."
    show monika neut cm oe
    mc "К тому же там чернуха одна."
    show monika mh
    m "Всё равно."
    show monika e1b
    m "Сейчас быстренько пробегусь по нему, а обсудим всё уже по дороге."
    show monika cm ldown
    mc "...хорошо, как хочешь."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg monika house outside day
    show monika forward green_hoodie worr cm ce school_bag at t11
    with wipeleft_scene
    show monika om
    m "Это реально пугает, Макс..."
    show monika cm e1a
    mc "Знала бы ты, каким я был перепуганным в 3 часа ночи."
    mc "И ведь же приснился такой ужас..."
    mc "Настолько реалистичный..."
    show monika om
    m "Ты слишком сильно переживаешь."
    show monika oe
    m "Возможно, это и есть тот самый выплеск эмоций, про который я предупреждала..."
    show monika cm
    mc "Я не могу это контролировать, Моника."
    show monika e1a
    mc "Н-е м-о-г-у."
    show monika neut om oe rhip
    m "Но ведь ты только начал делиться эмоциями."
    m "В идеале тебе нужна вторая половина."
    m "То есть человек, которому ты не только будешь доверять, но и с которым ты будешь в близких отношениях."
    show monika cm
    mc "Я это уже понял..."
    show monika worr cm e1a rdown
    mc "Но от этого факта ничего не меняется."
    mc "Всё остаётся на своих местах."
    show monika om ce
    m "К сожалению, в этом направлении необходимо работать."
    show monika cm
    mc "...так и подорвать себя можно."
    play sound mc_sneeze
    pause 0.577
    with vpunch
    show monika oe
    pause 1.0
    mc "Да что ж такое..."
    show monika neut om oe lpoint
    m "Вот-вот, я бы сказала, что в твоём случае судьба тебе улыбнулась и дала заслуженный шанс."
    show monika cm ldown
    mc "Шанс?"
    show monika happ om oe
    m "Шанс."
    show monika lean green_hoodie happ om oe at h11
    m "Почему бы тебе не использовать его по полной?"
    show monika cm
    mc "Хм..."
    show monika forward green_hoodie happ cm ce
    "У меня только что дежавю проскочило."
    "И как-то необычно Моника произнесла последнюю фразу..."
    show monika e1c
    "Ну Макс, блин, хорош тупить!" with vpunch
    "Это ЖИРНЫЙ намёк на то, что Моника тоже наметила на тебя глаз!"
    "А ты всё пытаешься отвергнуть любой любовный факт в твою сторону..."
    show monika e1b
    "Пф, и что же теперь делать?"
    "Как себя вести?"
    "И куда это всё может привести?"

    scene bg niigata street suburban 16 day
    show monika forward green_hoodie happ cm ce at t11
    with wipeleft_scene
    pause 0.2
    play phone_sound new_message_monika
    show monika oe
    pause 1.0
    show monika om ce
    m "О, кажется, они пришли в наш район!"
    show monika cm
    mc "Неужели..."
    show monika om oe lpoint rhip
    m "Держи мой телефон."
    show monika cm ldown
    mc "Зачем?"
    show monika om
    m "Я буду вести тебя по улицам и говорить, что им писать."
    show monika dist om oe
    m "Иначе я буду постоянно отвлекаться на экран и сбиваться с пути."
    show monika happ cm oe b1b n2
    mc "Ты сегодня в ударе, Моника..."
    show monika om ce rdown
    m "Да, в странном состоянии сейчас, хах..."
    show monika cm
    call skip_block_on

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 80
        clock = (11, 55)

    phone register "m_y_chat":
        time year 2018 day 21 month 4 hour 11 minute 32
        "m" "Юри, привет. Как там у тебя дела? Ты помирилась с Нацуки или ещё нет?"
        "y" "Привет, Моника. Всё хорошо. Я уже помирилась"
        "m" "Рада слышать)"
        "m" "Вы же сейчас вместе?"
        "y" "Да"
        "m" "Можете с нами встретиться?"
        "y" "Ты не одна?"
        "m" "Нет, я сейчас у себя дома с Максом"
        "m" "Я анализировала его стиль"
        "y" "Ааа..."
        "m" "Так вы к нам придёте?"
        "y" "Да, мы можем"
        "m" "Отлично"
        "m" "Но я предлагаю встретиться где-то на улице по пути к дому Сайори"
        "y" "В каком именно месте?"
        "m" "Ну..."
        "m" "Вы сейчас где?"
        "y" "В парке"
        "y" "Не который в японском стиле в нашем районе, а обычный в соседнем"
        "m" "А, поняла"
        "m" "Тогда лучше встретиться..."
        "m" "О, знаю!"
        "m" "Помнишь одну маленькую улицу с Т-образным перекрёстком?"
        "m" "На нём двойное зеркало для автомобилистов стоит"
        "m" "И на углу частная территория с маленьким железным забором и со стобиками на входе"
        "m" "Ещё там кусты пышные и несколько деревьев"
        "y" "Это весьма размытые ориентиры, Моника..."
        "y" "Мы так заблудимся"
        "m" "Знаю, но не могу по-другому это описать"
        "m" "Давайте так: мы с Максом сейчас пойдём к этой улице, вы тоже потихоньку выдвигайтесь"
        "m" "По пути будем вас координировать)"
        "y" "Моника, почему именно так?"
        "m" "Нам нужно как можно скорее прийти к Сайори"
        "m" "Мы и так практически всё утро потеряли"
        "m" "Чем дольше мы тянем время, тем ей хуже"
        "y" "Хорошо, Моника, мы тоже выходим"
        "y" "Пока дойдём до нашего района"
        "m" "Окей! Как до него дойдёте, напишите"
        "y" "Моника, мы на стыке районов -- на четырёхполосной дороге, где парк начинается. Куда нам дальше?"

    phone discussion "m_y_chat"
    $ plot_pause()
    mc "Кхм, Юри Химэ..."
    show monika lean green_hoodie happ cm oe n1 -b1b at t21
    mc "Почему ты назвала её принцессой?"
    show monika forward green_hoodie happ om oe lpoint at t41
    m "Юри выглядит, как вылитая принцесса."
    show monika cm ldown
    mc "Хм..."
    show monika neut cm oe
    mc "Так, они добрались до четырёхполосной дороги, где начинается парк..."
    show monika rhip
    mc "Спрашивают, куда дальше идти."
    $ phone.system.clock = (11, 56)
    show monika om e1c
    m "Ага, сейчас прикину в голове..."
    show monika doub cm ce
    m "М-м-м..."
    show monika happ om oe lpoint
    m "Да, вот так!"
    show monika ldown
    m "Макс, пиши: идите на юг по широкой примыкающей улице."
    show monika cm
    phone discussion "m_y_chat":
        "m" "Идите на юг по широкой примыкающей улице"
    mc "Угу."
    show monika om e1b
    m "Дойдёте до развилки в форме игрека, поверните налево."
    show monika cm
    phone discussion "m_y_chat":
        "m" "Дойдите до Y-развилки, поверните налево"
    show monika oe
    mc "Есть..."
    $ phone.system.clock = (11, 57)
    show monika om
    m "И где-то на этой улице должен быть наш маленький Т-образный перекрёсток."
    show monika cm
    phone discussion "m_y_chat":
        "m" "Дальше должен быть наш Т-образный перекрёсток"
    mc "Всё, написал."
    show monika lean green_hoodie happ om ce at h41
    m "Молодец!"
    show monika forward green_hoodie happ cm oe at t44
    pause 0.6
    show monika om lpoint
    m "Идём сюда."
    show monika cm

    phone end discussion transition

    call skip_block_off
    show monika ldown
    mc "Понял."
    show monika ce

    scene bg niigata street suburban 15 day
    show monika forward green_hoodie happ cm e1b at t11
    with wipeleft_scene
    pause 0.2
    play phone_sound new_message_monika
    show monika oe
    pause 1.0
    mc "Так..."
    call skip_block_on

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 80
        clock = (12, 3)

    phone register "m_y_chat":
        "y" "МОНИКА КАКОГО ЧЁРТА???"
        "y" "Здесь НЕТ такого перекрёстка!!!"

    phone discussion "m_y_chat"
    $ plot_pause()
    show monika curi cm oe
    mc "А-а-а..."
    show monika om at t21
    m "Что там?"
    show monika cm
    mc "Кажется, это уже написала Нацуки."
    show monika neut cm e2a at t41
    mc "И она говорит, что нет никакого игрек-образного перекрёстка..."
    show monika om
    m "Как это?"
    $ phone.system.clock = (12, 4)
    show monika cm
    mc "Ты меня спрашиваешь?"
    show monika curi om ce
    m "Дай подумать..."
    show monika cm
    phone discussion "m_y_chat":
        "y" "АУ!!!"
        "m" "Нацуки, блин, успокойся"
        "m" "Дай Монике подумать"
        "y" "А, Макс?"
    show monika e1b with None
    phone discussion "m_y_chat":
        "y" "Скажи ей, чтобы она ПРЕКРАТИЛА ЭТОТ ЦИРК"
        "y" "МЫ РЕАЛЬНО ЗАБЛУДИЛИСЬ В ТРЁХ УЛИЦАХ!!!"
        "m" "Сказано же было: времени мало, Сайори плохо -- надо значительно сокращать путь"
    $ phone.system.clock = (12, 5)
    phone discussion "m_y_chat":
        "m" "И тут не так всё запутано, не надо раздувать из мухи слона"
        "y" "НО ЭТО ЖЕ МАРАААВЫФ"
    show monika e1c
    "...чего?"
    "Это что ещё за слово?"
    show monika om
    m "Ах, я поняла..."
    show monika neut mh oe lpoint
    m "Они могли попасть на соседнюю улицу."
    show monika cm ldown
    mc "Угу..."
    phone discussion "m_y_chat":
        "y" "Простите, Нацуки тут вспылила..."
        "m" "Ничего, нормально всё"
        "m" "Вы где сейчас?"
    python in phone.system:
        battery_level = 79
        clock = (12, 6)
    phone discussion "m_y_chat":
        "y" "На площадке в каком-то дворе"
        "y" "Её дорога по кругу огибает"
        "y" "Тут много разветвлений..."
    show monika happ cm oe
    mc "Площадка во внутреннем дворе, огибающая её дорога, куча разветвлений..."
    show monika om ce
    m "Да, я так и думала!"
    show monika oe lpoint rhip
    m "Пиши им, чтобы шли на восток."
    show monika ldown
    m "Им даже никуда сворачивать не надо."
    m "Они спокойно выйдут на эту улицу."
    show monika cm
    phone discussion "m_y_chat":
        "m" "В общем, идите на восток, никуда не сворачивая"
    $ phone.system.clock = (12, 7)
    phone discussion "m_y_chat":
        "m" "Вы на финишной прямой"
        "y" "Точно?..."
        "m" "Моника в этом уверена"
    mc "Всё."
    show monika worr om oe
    m "Надеюсь, тут-то они не собьются с пути..."
    show monika cm

    phone end discussion transition

    $ pov_key_mobile = "mc"

    call skip_block_off
    mc "Криво всё как-то вышло..."
    show monika neut cm oe at t11
    mc "Проще было встретить их в знакомом месте."
    show monika happ om oe
    m "Зато знатно сократим время."
    show monika lsur om oe rdown at h11
    m "Ой, нам сюда!"
    show monika cm
    mc "Угу."
    show monika md e2b

    scene black with wipeleft_scene
    mc "А нам самим далеко ещё топать?"
    m "Неа, почти пришли..."
    mc "Кстати, у меня другой вопрос."
    m "М-м?"
    mc "Как ты смогла так хорошо запомнить улицы?"
    mc "У меня хоть память и хорошая, но даже, поживя здесь год, не смог бы нормально разобраться в этой «паутине»."
    m "Хах, я просто тут часто гуляла, когда было время."
    m "Здесь очень безопасно и живописненько."
    mc "Но ты всё равно носи что-нибудь для самообороны."
    mc "Мало ли..."
    m "Ох, Макс, ты так за меня переживаешь?"
    mc "Меня просто нервирует тот факт, что такая девушка, как ты, живёт одна."
    mc "А в Интернете я насмотрелся всяких ужасных преступлений, которые произошли в нашей стране."
    mc "И некоторые из них были совершены нелюдьми школьного возраста."
    mc "Да, это происходит редко, но очень, блин, метко..."
    "У меня дома под кроватью спрятана телескопическая дубинка, то ли в прошлом купленная родителями для спорта, то ли ещё откуда-то..."
    "Как бы то ни было, никому она сейчас не сдалась, а вот в качестве экстренной защиты ещё может послужить."
    "Лишь бы только полиция её не откопала, а то начнётся: \"А чё она у вас делает?\", \"А нельзя по закону!\", бла-бла-бла..."
    "Я как себя защищать от агрессоров должен, если они будут угрожать моей жизни?"
    "Молитвами, обращёнными божествам?"
    "Ну он посмеётся с этого и пропишет мне в лицо со всего размаха, отправив к этим самым божествам."
    "Таким же плевать на сентиментальности: они видят, что человек отпор не даёт, -- значит, слабый -- а значит, его можно мочить без последствий."
    m "Ну, я уже говорила, что у меня есть меры на этот счёт."
    mc "Если бы я понимал, что это за меры..."
    m "...не могу сказать, Макс."
    m "Но я в безопасности, не переживай."
    mc "...хорошо."
    "Называйте меня параноиком, но я даже Сайори уговорил не забегать далеко на пробежках, желательно бегать по людным местам, а ещё всегда носить с собой мобильник на связи."
    "Лучше перебдеть, чем недобдеть."
    "И при этом никогда не расслабляться."
    "Даже сейчас--{nw}"

    scene bg niigata street suburban 14 day
    show natsuki turned casual fc laug mo e0b b1e at face zorder 2
    play sound screamer_meme
    show natsuki mr
    n "{sc=3}БА-А-АМ!!!{/sc}{nw}" with vpunch
    mc "{sc=3}А-А-А-А-А--{/sc}{nw}"
    show natsuki laug cm ce -b1e at tfast
    mc "--тьфу на тебя!"
    show monika forward green_hoodie vsur cm ce at l31
    show natsuki om
    show yuri turned windbreaker lsur cm oe at r33
    n "Пха-ха-ха-ха!"
    show natsuki oe lhip rhip
    show yuri angr cm oe
    n "А вот нечего было сюр этот устраивать!"
    show monika pout cm oe
    show natsuki cm ce
    show yuri om
    y "Никакой это не сюр!"
    show monika happ om oe
    show natsuki happ cm ce
    show yuri neut cm e1d
    m "Раз Нацуки так шутит, то вы точно помирились."
    show monika cm
    show natsuki oe
    show yuri om e1b
    y "Да..."
    show natsuki mb
    show yuri cm
    n "Ага."
    show natsuki pout om oe
    show yuri e1d
    n "И я очень надеюсь, что Юри меня услышала..."
    show monika om b1f
    show natsuki curi cm oe
    m "Это, конечно, похвально, но что насчёт нас, хах?"
    show monika cm
    show natsuki om e1b ldown rdown
    n "Вас..."
    show monika -b1f
    show natsuki cm
    n "..."
    show natsuki pout cm ce
    n "...мгх..."
    show monika b1b
    show natsuki om
    show yuri sedu ma oe
    n "...простите за моё поведение..."
    show natsuki e1b
    n "...во мне просто накипело..."
    show natsuki sad om ce
    n "...я осознала свою глупость..."
    show natsuki cm
    m "..."
    show yuri neut cm e1d
    mc "..."
    "...и?"
    show monika om -b1b lpoint
    show natsuki pout cm oe
    show yuri curi md oe
    m "Юри, подойди сюда."
    show monika cm
    show natsuki at t43
    show yuri lup at t52 zorder 3
    y "М?..."
    show monika om
    show yuri neut cm e1d
    show natsuki curi cm oe
    m "{size=19}Обнимаем с трёх сторон: Макс спереди, я слева, а ты справа.{/size}"
    show monika cm
    show yuri happ cm oe ldown
    mc "{size=19}А-а-а...{/size}"
    show yuri om
    y "{size=19}Поняла.{/size}"
    show monika om
    show yuri cm
    m "{size=19}Давайте на счёт «три»...{/size}"
    show monika ce
    show natsuki at t32
    show yuri ce at t33
    m "Раз-{w=0.25}два-{w=0.25}три!{w=0.25}{nw}"
    show monika cm
    call window_close

    hide monika
    hide yuri
    hide natsuki
    show monika forward green_hoodie happ cm ce at e21
    show natsuki turned casual pani cm oe n4 at e11 zorder 2
    show yuri turned windbreaker laug cm ce at e22
    with dissolve
    pause 0.5
    show natsuki om ce

    call window_open
    n "Кх-х-хя!"
    show natsuki oe
    n "Что вы делаете?!"
    show natsuki ce
    n "Отпустите!"
    show monika om
    show natsuki cm
    m "Это слишком мило, чтобы прерывать объятия!"
    show monika cm
    show natsuki om oe
    n "Мило?!"
    show natsuki cm ce
    n "Кх-х-х-х!"
    show natsuki om
    n "Вы меня раздавите!"
    show natsuki cm
    "Знала б сейчас Нацуки, что она буквально в центре любовного треугольника..."
    show monika nerv mb ce
    m "Ой, ладно, всё, хватит, ха-ха-ха..."
    show monika cm
    call window_close

    hide monika
    hide natsuki
    hide yuri
    show monika forward green_hoodie happ cm ce at i31
    show natsuki turned casual fc pout cm ce n4 at i32 zorder 2
    show yuri turned windbreaker happ cm ce at i33
    with dissolve
    pause 0.5

    call window_open
    mc "Фу-у..."
    show monika oe
    show natsuki sad om ce
    n "Ох..."
    show monika om oe b1b
    show natsuki pout cm oe
    show yuri oe
    m "Нацуки, пожалуйста, делись с нами подобными переживаниями, чтобы они не скапливались внутри и не создавали конфликтные ситуации, хорошо?"
    m "Или со мной лично."
    show monika cm -b1b
    n "...угусь..."
    show monika om lpoint
    show yuri neut cm e1d
    m "Это и остальных касается."
    show monika cm ldown
    show yuri e1c
    mc "Пф..."
    show monika lean green_hoodie happ om oe at h31
    show yuri oe
    m "И, кстати, об этом: мы тебя услышали."
    show monika ce
    show yuri happ cm oe
    m "И поэтому постараемся уделять тебе побольше времени."
    show monika cm
    show natsuki om e1b
    n "Ой, да не надо..."
    show monika forward green_hoodie happ cm oe
    show natsuki cm
    mc "Но ты же сама этого хочешь."
    show monika ce
    show natsuki pout om ce
    n "...ух..."
    show natsuki cm
    show yuri neut cm e1d
    "Впервые вижу её настолько смущённой."
    show monika oe
    show yuri om
    y "Давайте пойдём к Сайори..."
    show monika om
    show natsuki oe n1
    show yuri cm
    m "Да, согласна."
    show monika ce lpoint
    show yuri happ cm oe
    m "Все дружно идём за мной!"
    show monika cm ldown

    scene black with wipeleft_scene
    mc "К слову, мы как действовать будем?"
    n "Просто зайдём, и я извинюсь, чего тут думать?"
    mc "Ага, всей гурьбой попрёмся в комнату?"
    y "Не будем же мы ждать её снаружи..."
    mc "Я планировал, что сначала вы перед домом постоите, а я в это время проведаю Сайори."
    m "Тогда уж проще зайти всем сразу."
    m "Сайори не только почувствует поддержку, но и осознает, что мы ей дорожим."
    mc "Ладно, убедили..."
    "Просто хотелось бы аккуратно одному её успокоить, а тут целая группа поддержки..."
    "Хотя по идее как раз Нацуки должна идти первой, но, зная её характер..."
    "Да блин, стесняюсь я на «знакомых» людях проявлять чувства заботы...{w}или нет...{w}да как это выразить-то...{w}тьфу, я запутался уже!"
    y "...интересно..."
    m "Что там у тебя, Юри?"
    y "Н-ничего такого, я просто решила посчитать количество «прощаний»."
    n "Делать нечего..."
    y "Если Нацуки извинится перед Сайори, их станет 7."
    y "А 7 у нас считается счастливым числом."
    m "Ух ты..."
    mc "Это ты где остальные 6 насчитала?"
    y "Нацуки перед нами -- 3, а ещё мы перед Нацуки -- тоже 3."
    mc "А-а..."
    mc "Да уж, забавно..."
    "Эти ваши суеверия с эффектом самовнушения..."
    n "Мдэ."
    call window_close

    call plot_transition

    call window_open
    scene bg residential_day nearby
    show monika forward green_hoodie neut cm e1b at t31
    show natsuki turned casual neut cm e1c at t32
    show yuri turned windbreaker neut cm e1d at t33
    with wipeleft_scene
    "За поворотом уже моя с Сайори улица..."
    show monika oe
    show natsuki oe
    show yuri curi md oe
    mc "Точно ничего придумывать не будем?"
    show monika happ cm e1d b1b
    show natsuki anno cm oe
    mc "Хочу убедиться окончательно."
    show monika om
    show yuri neut cm e1d
    m "Ма-а-акс...."
    show monika ce -b1b
    m "Не накручивайся, пойдём."
    show monika cm oe
    show natsuki cross casual anno mh oe
    show yuri angr cm oe
    n "Вот именно, хорош время тянуть!"
    show monika anno cm oe
    show natsuki ce
    n "Сами же торопились и сами же тормозите."
    show natsuki cm
    show yuri mi
    y "Нацуки, хватит уже!"
    show monika happ cm oe
    show yuri dist om ce lup rup
    y "Мы все дружно идём к Сайори и рассасываем её душевный ушиб."
    show yuri cm

    scene black with wipeleft_scene
    mc "Да поймите: такие ситуации для неё -- редкость."
    mc "И я не хочу влетать к ней сломя голову, чтобы ненароком нанести ещё больший вред."
    m "Здесь и не нужно обдумывание."
    m "Здесь нужно контактировать на уровне чувств."
    m "А это не совсем поддаётся...{w}э-э-э, как там..."
    y "Рациональному мышлению?"
    m "О, именно!"
    m "Спасибо, Юри."
    "Волнение от этого никуда не делось..."

    scene bg house with wipeleft_scene
    n "Пришли..."
    m "Сайори же не одна, верно?"
    mc "Да, с ней мама."
    m "Тогда звоним в дверь."
    mc "Сейчас..."
    call window_close

    pause 1.0
    play sound doorbell_sayori
    pause 1.75
    play sound doorbell_sayori
    pause 1.75
    play sound doorbell_sayori
    pause 4.0
    show sayori_mom home_clothes neut cm oe at t11
    pause 0.5

    call window_open
    show sayori_mom happ om oe lpoint rhip
    sm "Здравствуй, Ма..."
    show sayori_mom e2a ldown
    sm "...ух ты, тут весь Литературный клуб собрался, да?"
    show sayori_mom cm
    mc "Есть такое."
    show sayori_mom ce
    mny "Здравствуйте!"
    show sayori_mom neut cm oe
    m "Мы хотим проведать Сайори, она сейчас дома?"
    show sayori_mom sad mh oe
    sm "Да, целый день сидит в своей комнате, не выходит."
    show sayori_mom worr om oe
    sm "Пришлось приносить ей еду в постель..."
    show sayori_mom sad mh oe lpoint
    sm "Я очень за неё переживаю, но она говорит, что всё в порядке."
    show sayori_mom neut cm oe ldown
    m "Мы как раз к ней и пришли разобраться в этой проблеме."
    show sayori_mom happ om ce
    sm "Тогда милости прошу, проходите!"
    show sayori_mom cm
    m "Спасибо!"
    show sayori_mom om oe
    sm "А я пока могу заварить чай, если хотите."
    show sayori_mom cm
    y "Можно..."
    m "Конечно, но хотелось бы ещё и Сайори вытянуть..."
    show sayori_mom om ce
    sm "Да, не смею задерживать."
    show sayori_mom cm rdown at thide
    hide sayori_mom
    pause 0.2
    m "Ребят, идём."
    stop noise_1 fadeout 3.0
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    "Сердце колотится как бешеное..."
    "Даже редко слегка покалывает..."
    "Руки трясутся."
    "Прямо как в том чёртовом кошмаре."
    "Отвратительная параллель..."
    n "Долго ты над дверью стоять будешь как вкопанный?"
    mc "{size=19}Бляха!{/size}" with vpunch
    y "{size=19}Нацуки, тише, сбавь голос!{/size}"
    n "{size=19}Бе-бе-бе!{/size}"
    mc "{size=17}Нет, я так с вами точно инфаркт заработаю...{/size}"
    m "{size=19}Всё, хватит!{/size}"
    m "{size=19}Макс, успокойся...{/size}"
    m "{size=19}У тебя сердце сейчас выпрыгнет...{/size}"
    "Моника, пожалуйста, можно не трогать меня ладонью в районе груди на виду у Юри и Нацуки?"
    mc "{size=19}Ф-ф-ф, хорошо...{/size}"
    mc "{size=19}Просто ещё от кошмара не отошёл...{/size}"
    m "{size=19}Я понимаю...{/size}"
    n "{size=19}Люди, хватит там тупить, открывайте!{/size}"
    m "{size=19}Макс, давай.{/size}"
    mc "{size=19}Окей, приготовьтесь.{/size}"
    "Постараюсь без скрипа..."
    mc "{size=19}Я осторожно открываю дверь...{/size}"
    call window_close

    scene white with dissolve
    pause 0.5

    call window_open
    if cg_a1_d6_s_1.unlocked == False:
        $ cg_a1_d6_s_1.unlock()
    play music sayori_my_confession_piano
    scene sayori_cg_act_1_day_6 with Dissolve(1.5)
    pause 1.5
    "Живая...{w}точно живая..."
    m "{size=19}Ох...{/size}"
    y "{size=19}Она...{w}похожа на брошенную куклу.{/size}"
    y "{size=19}Такая же неподвижная...{/size}"
    mc "{size=19}Грх...{/size}"
    "Почему же ты такая чувствительная, Сайори?..."
    "Каждый раз, когда она царапается об этот мир, на неё больно смотреть."
    "Вообще меня пугает тот факт, что рано или поздно наши с ней пути разойдутся и ей придётся жить одной."
    "Строить свою жизнь самостоятельно..."
    "Но в таком состоянии она ничего не выдержит."
    "Поэтому, пока есть возможность и время, надо научить её самостоятельной жизни."
    "...а я до этого момента практически ничего для этого не сделал."
    "Да, я не нянька, всего лишь друг, но...{w}я {b}знаю{/b}, кто такая Сайори, и что она заслуживает."
    "Хоть и в общих чертах."
    "И она не заслуживает ни одиночества, ни всего того дерьма, что творится снаружи."
    "Но если отгородить её от этого, то она не научится этому сопротивляться."
    "А значит, не станет самостоятельной."
    "Замкнутый круг..."
    n "{size=19}Вы как хотите, а мне надоело стоять в дверях и лицезреть, как Сайори мучится.{/size}"
    $ currentpos = get_pos(channel="music")
    stop music fadeout 6.0

    scene black with dissolve
    pause 0.25
    n "{size=19}Пропу...{w}сти...{w}те!{/size}"
    y "{size=19}Не толкайся!{/size}"
    m "{size=19}Аккуратнее!{/size}"
    n "{size=19}Кхм-кхм...{/size}"
    n "Сайо-о-о...{w=0.5}ри!{w=0.5}{nw}"
    s "{sc=3}ХИ-И?!{/sc}{nw}"
    play sound sayori_falldown_bed
    pause 1.520
    with vpunch
    pause 1.0
    mc "...кхпмф..."
    y "...пф..."
    m "...хах..."
    n "...ну как так-то?!"
    n "Ты себе зад не ушибла?"
    s "..."
    s "...хе-хе-хе!"

    scene bg sayori house bedroom day
    show sayori_house_bedroom_unmade_bed
    show monika forward green_hoodie laug cm ce zorder 2 at t41
    show sayori turned pajamas nerv cm oe zorder 3 at t42
    show natsuki turned casual angr cm oe lhip rhip zorder 4 at t43
    show yuri turned windbreaker laug cm ce zorder 2 at t44
    with dissolve
    pause 0.25
    show natsuki om
    n "Ничего смешного!"
    show monika happ cm oe
    show sayori laug om oe
    show natsuki curi cm oe
    show yuri happ cm oe
    s "Моя попа в порядке, всё хорошо!"
    show monika neut cm oe
    show sayori worr om oe
    show natsuki pout cm oe ldown rdown
    show yuri lsur cm oe
    s "Как и сама в целом..."
    show sayori cm e1a
    show natsuki om
    n "Ага, прекрасно это видела минуту назад."
    show sayori neut om oe
    show natsuki neut cm oe
    show yuri neut cm e1d
    s "...долго вы здесь были?"
    show monika om e1b
    show sayori cm
    m "Неа, где-то минут 5..."
    show monika cm oe
    show sayori curi mh e2a
    s "Странно, что я вас не заметила..."
    show monika happ cm oe
    show sayori neut cm oe
    mc "Ха, значит, у меня получилось осторожно открыть дверь."
    show monika om ce
    m "Это точно, ха-ха!"
    show monika cm
    show sayori om
    show natsuki curi cm oe
    s "...но зачем вы сюда пришли?"
    show monika oe b1b
    show sayori cm
    show yuri dist om oe lup rup
    y "Отпустить твою боль."
    show monika om
    show natsuki neut cm oe b1d
    show yuri cm
    m "Ты для нас важна, Сайори, именно поэтому."
    show monika cm
    show sayori worr cm oe
    show yuri neut cm e1d ldown rdown
    s "..."
    show sayori neut cm oe
    show natsuki om lhip rhip
    n "Так, да!"
    show monika -b1b
    show natsuki ce
    n "Дайте мне уже высказаться."
    show natsuki cm
    n "Кгхм..."
    show natsuki oe -b1d ldown rdown
    n "..."
    show natsuki vsur cm e1a
    n "......"
    $ audio.sayori_my_confession_piano_2 = "<from " + str(currentpos + 6) + " loop 0 to 125.278>mod_assets/music/characters/s/my_confession_piano.ogg"
    play music sayori_my_confession_piano_2 fadein 1.0
    show monika b1b
    show sayori flus om oe lup rup n4 at h42
    show natsuki fs cry cm ce at t11
    show yuri lsur cm oe
    n "{sc=1.5}............{/sc}"
    "Да ну на..."
    "Я рассчитывал, что она что-то скажет в своём смущённо-злом духе, но чтобы так..."
    s "Н-Нацуки?..."
    n "{sc=1.5}............{/sc}"
    show sayori cm
    "Может, она только сейчас всё полностью осознала и достигла своей точки эмпатии..."
    show monika om ce
    show yuri laug cm oe
    m "Ви-и-и, как это миленько!"
    show monika oe -b1b lpoint
    m "Макс, Юри, не стойте, присоединяйтесь!"
    show monika cm ce
    call window_close

    hide monika
    hide sayori
    hide natsuki
    hide yuri
    show monika forward green_hoodie happ cm ce b1b zorder 2 at eyes(200)
    show sayori turned pajamas cry ma ce lup rup n4 zorder 2 at eyes(500)
    show natsuki turned casual fs cry cm ce zorder 3 at eyes(800)
    show yuri turned windbreaker laug cm ce lup rup zorder 2 at eyes(1100)
    with dissolve
    pause 0.5

    call window_open
    "Нифига себе!"
    "Сайори в своей постели разогрелась как вулкан!"
    show natsuki om
    n "Я не хотела..."
    show sayori mb
    show natsuki cm
    s "Всё...{w}хорошо...{w}Нацуки..."
    show sayori ma
    show natsuki om
    n "Я реально не хотела..."
    show natsuki oe
    n "Прости меня!..."
    show sayori mb
    show natsuki cm
    s "Всё хорошо..."
    show sayori ma
    show natsuki ce
    "...блин, у меня самого сейчас ком в горле вскочет и в глаза «соринка» попадёт."
    "Сейчас подправим общий настрой..."
    show monika neut cm oe
    show sayori neut cm oe n2
    show yuri neut cm e1d
    mc "Ребят, что-то кисло вы друг за друга держитесь..."
    show monika curi md oe
    show sayori curi cm oe
    show natsuki cry cm oe
    mnsy "???"
    mc "Литературный клуб всё-таки."
    show monika neut cm oe
    mc "Давайте...{w=1.0}{nw}"
    show monika pani cm e4c
    show sayori flus om ce
    show natsuki ff pani cm ce
    show yuri laug me e4c
    mc "...покр-р-р-р-репче!" with vpunch
    mnsy "КХ-Х-Х!!!"
    show monika laug cm e4c
    show sayori laug cm e4c
    show natsuki om
    show yuri mn
    n "ФЫ МЕНЯ ФЕФФАЙ РАФДАФИТЕ!!!"
    show sayori om
    show natsuki cm
    s "Ха-ха-ха-ха-ха!"
    show sayori cm
    call window_close

    hide monika
    hide sayori
    hide natsuki
    hide yuri
    show monika forward green_hoodie happ cm ce b1b zorder 2 at i41
    show sayori turned pajamas laug cm ce zorder 3 at i42
    show natsuki turned casual shoc cm ce zorder 4 at i43
    show yuri turned windbreaker laug cm ce zorder 2 at i44
    with dissolve
    pause 0.5

    call window_open
    mc "...пф-ф-фа-а-а..."
    show monika oe
    show natsuki om
    n "ВОЗДУХ!!!"
    show monika e1b
    show sayori om
    show natsuki cm
    s "Фу-у-у..."
    show sayori cm oe
    show natsuki nerv om ce
    n "Чтобы я ещё раз..."
    show monika oe -b1b
    show sayori happ om ce lup rup at h42
    show natsuki cm oe
    show yuri happ cm oe
    s "...а мне понравилось!"
    show sayori oe b1b ldown rdown
    show natsuki ce
    s "Спасибо...{w}большое..."
    show monika om ce
    show sayori cm
    m "Нет, это тебе спасибо, что ты с нами."
    show monika cm
    show sayori e4a
    show natsuki e1a
    show yuri om lup rup
    y "Да, ведь именно ты собрала нас всех..."
    show natsuki om
    show yuri cm
    n "...снова вместе..."
    show natsuki cm
    play sound mc_sneeze
    pause 0.577
    stop music
    show monika neut cm e2a
    show sayori flus cm oe -b1b
    show natsuki curi cm oe
    show yuri neut cm e1d
    with vpunch
    pause 0.52
    "ДА ТВОЮ Ж МАТЬ!"
    show monika oe
    show sayori neut cm oe
    show yuri ldown rdown
    mc "Что-то я расклеился, простите..."

    scene black with wipeleft_scene
    s "{size=19}Будь здоров!{/size}"
    n "{size=17}ТАК, ПОДОЖИ!{/size}"
    n "{size=15}ТЫ НАС ДВА РАЗА ОБНЯЛ, ЗНАЯ, ЧТО ТЫ СОПЛИВИШЬ?!{/size}"
    "Да, позор какой-то..."
    "Такой редкий и эмоциональный момент, и вот так его засопливить..."
    "Где ванная, где ванная, где ванная..."
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    "Вот надо было мне так из-за нервов подболеть."
    "Ладно хоть нет мерзкой боли в горле или чего-то ещё..."
    mc "Пф-ф..."
    "Сначала разберёмся с Сайори, а потом уже со здоровьем."
    "Надо бы с ней поговорить наедине о её состоянии."
    "Не верю я, что клубного объятия хватило, не верю..."
    "..."
    "Так, что-то в её комнате тихо..."
    "Куда все делись?"
    play sound door_knock
    pause 1.8
    mc "Сайори?"
    "..."
    "Не могла ж она мгновенное переодеться или выйти в одной пижаме...{w}или могла?"
    mc "Ты там?"
    mc "Могу войти?"
    "..."
    "А в ответ мне -- тишина..."
    "Не, ну хорош издеваться, а?!"
    "Уже третий раз всё повторяется!"
    "Если первый закончился отвратительно, второй -- позитивно, то этот чем?"
    "..."
    "Да без понятия, там ноль шума."
    "Либо я его не слышу."
    "Всё, блин, вхожу."
    "Я стучался в дверь -- моя совесть чиста."
    call window_close

    play sound closet_open
    scene white with dissolve
    pause 0.25

    call window_open
    mc "Сайори, ты тут?{nw}"

    scene bg sayori house bedroom day
    show sayori turned body curi cm oe shorts at i22
    with Dissolve(0.1)
    show sayori neut cm oe s_scream lup rup at h22
    s "{sc=3}ХА-А-А!!!{/sc}{nw}" with vpunch

    scene black with Dissolve(0.1)
    pause 0.1
    mc "Всё-всё-всё, я закрыл глаза рукой и веками, а ещё повернулся в сторону двери, НЕ БЕЙ!"
    s "...там стена."
    mc "Да?"
    s "НЕ СМОТРИ!"
    s "И вообще, кто без стука входит в комнату к девушке?!"
    mc "В том-то и дело, что я стучался!"
    mc "И ничего в ответ не услышал."
    mc "Даже шороха."
    s "Значит, я осторожно переодевалась?"
    mc "Пх, ну да..."
    mc "Остальные куда делись?"
    s "Ушли на первый этаж, там мама чай, оказывается, для нас приготовила..."
    s "Я как раз одевалась, чтобы подойти."
    mc "Понятненько."
    s "{size=19}Где же мой лифчик...{/size}"
    mc "...извини, что стою тут у тебя над душой, но..."
    s "...да ладно тебе уже, Макс."
    s "Мы же друзья!"
    mc "Даже у друзей есть границы личного пространства..."
    mc "Так вот, я хотел бы с тобой поговорить о твоём состоянии за последний день..."
    s "А что о нём говорить?"
    mc "Ну..."
    "...а что, реально?"
    mc "Не было ли у тебя крайне негативных мыслей или что-нибудь такое..."
    s "{size=19}Может, тут...{/size}"
    s "А?"
    s "А, не, не было."
    mc "Точно?"
    mc "Ты была подавленной как вчера, так и сегодня целое утро."
    s "{size=19}А-а-а, его в шкафу вообще нет!{/size}"
    s "Нет, Макс, мне было грустно, да..."
    mc "Было."
    s "Но не так..."
    s "..."
    s "...мгх, давай потом об этом поговорим, когда все уйдут."
    s "Я не хочу...{w}портить себе настрой, копаясь в себе...{w}и беспокоить этим окружающих..."
    mc "Конечно."
    s "Хотя тут больше светло-горькое послевкусие, которое из меня не вышло..."
    s "Ой, не знаю, у меня всё перемешалось, но при этом если я начну разбираться в этой куче, то...{w}всё будет болеть..."
    mc "И именно поэтому я хочу с тобой поговорить, чтобы разобраться в этой куче наименее болезненно."
    s "...спасибо...{w}Макс..."
    s "Ты очень хороший друг!"
    mc "Да пожалуйста--{nw}"
    mc "АПФ!" with vpunch
    mc "Сайори, это перебор!"
    mc "Ты бы хоть свой лифчик нашла, прежде чем обниматься!"
    "Не акцентируй внимание, не акцентируй внимание, не акцентируй внимание..."
    s "Мы друзья, а ещё одни в этой комнате, не будь злюкой!"
    play sound door_knock
    pause 1.8
    s "Ха?!"
    m "{size=19}Сайори, ты там скоро?{/size}"
    m "{size=19}Уже всё готово.{/size}"
    s "Д-да, сейчас!"
    m "{size=19}Ещё Макс где-то потерялся...{/size}"
    m "{size=19}Он к тебе не заходил?{/size}"
    s "Он п-помогает мне кровать застилать!"
    s "Да..."
    m "{size=19}О, хорошо.{/size}"
    mc "Мы через пару минут выйдем."
    m "{size=19}Давайте, не задерживайтесь, ждём!{/size}"
    mc "..."
    s "..."
    mc "Блин, Сайори, живее ищи свой лифчик!"
    s "Не знаю я, куда он делся!"
    mc "Тут искать-то негде!"
    s "А, нашла!"
    s "Ты собой его загородил!"
    mc "...что?"
    s "Ты встал чуть левее двери перед тумбочкой."
    s "И под ней валяется мой лифчик..."
    mc "Ты его туда на эмоциях зашвырнула?"
    s "Не помню..."
    s "У-у, он у самой стены..."
    s "Макс, достанешь?"
    mc "Не дотягиваешься?"
    s "Неа."
    mc "Сколько ж проблем..."
    "..."
    "Ну, по ощущения тут нет пылищи и всякого сора, за что Сайори спасибо."
    "..."
    "А вот и злосчастное нижнее бельё..."
    mc "Фух."
    mc "На, закрытыми глазами достал, закрытыми глазами передаю."
    s "Так за бретельку держишь, будто сопля какая-то."
    mc "Сайори, просто надень уже своё добро."
    mc "Мы и так тут время растянули..."
    s "Ай, сейчас..."
    s "М-м-м..."
    s "Вот так..."
    s "Вот так вот..."
    s "Вот так во-о-от..."
    s "И...{w}вот так вот."
    s "Всё, можешь открывать глаза."

    scene bg sayori house bedroom day
    show sayori turned casual happ cm oe at i11
    with dissolve
    pause 0.25
    "Ух, мои глаза..."
    mc "Ха, снова твоя любимая розовая футболка?"
    show sayori ce
    s "Угусь~"
    show sayori neut cm oe
    mc "Я всё никак не пойму: эти рукава специально короткими сделали или ты просто из футболки выросла?"
    show sayori om
    s "Это лонгслив."
    show sayori happ om oe rup
    s "Такая же футболка, как у тебя, но да, с короткими рукавами."
    show sayori neut cm oe rdown
    mc "Опять это дурацкое слово..."
    show sayori om e1b
    s "Подумаешь, иностранное..."
    show sayori cm
    "Да оно звучит как..."
    "Я где-то видел русское слово «{color=#407fff}слив{/color}», которое обозначает стекание жидкости и прочего..."
    "Если «{color=#fc7e23}long{/color}» с английского -- длинный, а «{color=#407fff}слив{/color}» с русского -- сливание, то это звучит как спуск в унитаз или выливание ведра с помоями непонятного происхождения."
    show sayori oe
    "Фу!" with vpunch
    show sayori curi cm oe
    "Аж плохо стало..."
    show sayori om
    s "Макс, с тобой всё нормально?"
    show sayori neut cm oe
    mc "Да, просто глаза замылились..."
    show sayori laug ma oe
    mc "Ладно, пойдём уже, а то весь чай без нас высосут."
    show sayori om ce
    s "Пхе, пойдём."
    show sayori ma
    call window_close

    call plot_transition

    call window_open
    play music cup_of_tea fadein 3.0
    scene bg sayori house livingroom day with wipeleft_scene
    mc "Бу-у-ух..."
    n "{size=19}Сумасшедший!{/size}"
    s "{size=19}Как ты не ошпарился?{/size}"
    mc "Чай уже подостыл, вполне можно и большими глотками выпить."
    y "{size=19}Но ты им совсем не насладился...{/size}"
    mc "Я им удовлетворился и подлечился."
    "И вообще, можно мне посидеть на мягком диване?..."

    scene black with dissolve
    pause 0.25
    "Настоялся я за сегодня..."
    n "{size=19}Знаете что?{/size}"
    n "{size=19}Раз мы снова восстановились, то предлагаю торжественно это отметить!{/size}"
    m "{size=19}И что именно ты предлагаешь?{/size}"
    n "{size=19}Вот не знаю.{/size}"
    n "{size=19}Поэтому и сказала.{/size}"
    mc "Пф."
    "Массовик-затейник..."
    y "{size=19}Устроим собственное чаепитие?{/size}"
    s "{size=19}Точно, Юри!{/size}"
    s "{size=19}Кексы!{/size}"
    s "{size=19}Я хочу твои вкусные кексы с заварным чаем, Нацуки!{/size}"
    n "{size=19}Эй-эй-эй, не тереби меня!{/size}"
    m "{size=19}Хе-хе-хе...{/size}"
    sm "Решил немного отдохнуть от суеты?"
    mc "А?"

    scene bg sayori house livingroom day
    show sayori_mom happ cm oe rhip at t11
    with dissolve
    pause 0.25
    show sayori_mom om
    sm "Сидишь здесь один."
    show sayori_mom cm
    mc "У-у, угу."
    mc "Ноги за день подзабились..."
    show sayori_mom om e1b
    sm "А-а, понимаю..."
    show sayori_mom cm
    "...и голова тоже."
    "Тишины и спокойствия хочется."
    show sayori_mom oe
    m "{size=19}Но тогда нам придётся пожертвовать одним днём, чтобы организовать своё чаепитие...{/size}"
    n "{size=19}И?{/size}"
    show sayori_mom e1c
    y "{size=19}Думаю, ничего страшного не случится...{/size}"
    y "{size=19}Иногда нужно брать небольшой отдых, чтобы приступить к творчеству с новыми силами.{/size}"
    show sayori_mom neut cm e1c
    m "{size=19}Наша школа и так даёт 2 выходных дня.{/size}"
    s "{size=19}Моника, кексы же...{/size}"
    show sayori_mom happ cm e1c
    n "{size=19}Именно, у нас праздник!{/size}"
    n "{size=19}И его надо отметить!{/size}"
    s "{size=19}Да!{/size}"
    show sayori_mom om ce
    sm "Хах, вижу, Сайори стало намного лучше?"
    show sayori_mom cm
    mc "Да, есть такое."
    show sayori_mom om oe
    sm "Помогли ей выговориться?"
    show sayori_mom cm
    mc "Ну...{w}не совсем..."
    mc "Поддержали её."
    show sayori_mom neut cm oe
    mc "А так..."
    mc "Такое ощущение, будто не довели дело до конца."
    mc "Хочу потом наедине с ней поговорить."
    show sayori_mom om
    sm "Ясно."
    show sayori_mom worr om oe
    sm "Я тоже пыталась, но почему-то она от меня всё скрывает."
    show sayori_mom neut cm oe
    mc "Возможно, просто это для Сайори личное или она хочет поговорить с кем-то на одном уровне."
    mc "Ну я в том плане, что вы же всё-таки мама, взрослый человек."
    mc "А я...{w}просто друг примерно того же возраста."
    show sayori_mom om e1b
    sm "Да, ловила себя на этой мысли, и меня это очень не радует..."
    show sayori_mom happ cm oe
    mc "Не переживайте, бремя Сайори и на моих плечах, как бы пафосно это ни звучало."
    show sayori_mom om ce lpoint
    sm "Ха-ха, с таким другом ей точно ничего не страшно!"
    show sayori_mom cm ldown
    mc "Да..."
    n "{size=19}Мне нужно 2 дня на готовку кексов.{/size}"
    n "{size=19}И это в том случае, если у меня уже будут все нужные ингредиенты.{/size}"
    show sayori_mom e1c
    y "{size=19}Нельзя ли как-то ускорить процесс?...{/size}"
    n "{size=19}Можно.{/size}"
    n "{size=19}Если ты поможешь, и остальные тоже.{/size}"
    y "{size=19}Угх...{/size}"
    n "{size=19}Но тогда мне нужно готовить всё это где-то в другом месте, а не у себя дома.{/size}"
    show sayori_mom neut cm oe
    mc "Знаете, меня тут одна мысль посетила насчёт вашей дочери..."
    show sayori_mom om
    sm "Какая?"
    show sayori_mom cm
    mc "Рано или поздно наши с ней пути разойдутся, и я не смогу поддерживать её в критические моменты."
    mc "Ей бы научиться как-то преодолевать это самостоятельно."
    mc "Иначе каждый такой раз переживать будет очень больно."
    show sayori_mom om
    sm "Хм, я обсуждала этот вопрос со своим мужем."
    show sayori_mom cm
    mc "А..."
    show sayori_mom dist om oe
    sm "Мы тоже над этим «работаем», как можем..."
    show sayori_mom happ cm oe b1b
    mc "В общем, я просто хотел сказать, что постараюсь помочь Сайори встать на крыло как можно раньше."
    show sayori_mom om
    sm "Спасибо тебе, Макс."
    show sayori_mom ce -b1b
    sm "Сайори очень с тобой повезло."
    show sayori_mom cm
    mc "Скорее, ей с вами, чем со мной."
    show sayori_mom om oe
    sm "Ну что ты, не принижайся."
    sm "И кстати, я смотрю, в Литературном клубе много красивых девушек."
    show sayori_mom ce
    sm "Может быть, тебе стоит с кем-то из них сблизиться?"
    show sayori_mom cm
    mc "Сблизиться?"
    show sayori_mom om oe lpoint
    sm "Ты очень хорошо общаешься с Сайори."
    show sayori_mom ldown
    sm "И уверена, что с остальными, раз вы все дружно сюда пришли."
    show sayori_mom neut om oe b1b
    sm "Будет жаль, если вы возьмёте и разойдётесь в один момент, как ты сказал."
    show sayori_mom cm -b1b
    mc "Хотите, чтобы я «встречался» с кем-то из них?"
    show sayori_mom happ om oe
    sm "Почему нет?"
    show sayori_mom e1b
    sm "Думаю, ты бы мог образовать хорошую пару с одной из участниц."
    show sayori_mom cm
    mc "Хм..."
    "Что вы все так сговорились..."
    show sayori_mom ce
    "Жизнь, похоже, реально решила поиздеваться надо мной, вышвырнув такой разносторонний шанс."
    "Пф-ф-ф, надо будет обмозговать это вечером..."
    show sayori_mom oe
    mc "Я ещё не готов к нечто подобному..."
    mc "Да и вообще над таким не думал."
    show sayori_mom om
    sm "А ты подумай."
    sm "Время идёт: не заметишь, как пролетит."
    show sayori_mom ce
    sm "Так что такой вопрос откладывать не стоит, а не то упустишь своё счастье."
    show sayori_mom cm
    mc "...м-м-м..."
    show sayori turned casual happ cm oe at l33
    pause 0.5
    show sayori_mom oe
    show sayori om
    s "Макс!"
    show sayori cm
    mc "А?"
    show sayori curi om oe
    s "{size=19}У тебя же просторная кухня?{/size}"
    show sayori happ cm oe
    mc "Да."
    mc "А почему шёпотом?"
    show sayori om ce lup rup at h33
    s "Он согласен!"
    show sayori_mom laug cm oe
    show sayori cm ldown rdown
    n "{size=19}Отлично, значит, готовим кексы у Макса дома!{/size}"
    show sayori_mom ce
    show sayori laug cm ce
    mc "ЧТО?!" with vpunch
    show sayori om
    s "Ничего не знаю!"
    show sayori cm
    hide sayori with easeoutright
    mc "Это подло!"
    my "{size=19}Ха-ха-ха!{/size}"
    show sayori_mom ma
    s "{size=19}А заодно у него можно подержать твои кексы!{/size}"
    show sayori_mom oe
    n "{size=19}Классно, плюс ко всему он поможет с их готовкой.{/size}"
    mc "Я?!"
    s "{size=19}Ура!{/size}"
    mc "Эй, я вообще-то ещё ничего не сказал!"
    n "{size=19}И ты, Сайори, тоже поможешь.{/size}"
    s "{size=19}Я?!{/size}"
    show sayori_mom ce
    mc "Пха-ха-ха!"
    m "{size=19}Ребят, давайте пока выйдем на улицу, там всё обсудим.{/size}"
    show sayori_mom happ cm ce
    m "{size=19}Не будем шуметь и мешаться.{/size}"
    show sayori_mom oe
    y "{size=19}Хорошо...{/size}"
    mc "Ох, ладно..."
    show sayori_mom om rdown
    sm "Уже уходите?"
    show sayori_mom ce
    sm "Тогда спасибо тебе ещё раз, Макс."
    show sayori_mom cm ce
    mc "Да ладно уж, любой, кто способен сопереживать, так поступил бы."
    "Правда же?"
    stop music fadeout 2.0
    call window_close

    call plot_transition

    if persistent.add_random_menu == 8:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg house
    show monika forward green_hoodie neut cm oe at t41 zorder 2
    show yuri turned windbreaker neut cm e1d at t42
    show natsuki turned casual curi cm e1b at t43 zorder 3
    show sayori turned casual happ cm oe at t44
    with wipeleft_scene
    show natsuki om lhip rhip
    n "Так, нужно понять, сколько кексов делать..."
    show monika mh b1e lpoint
    show natsuki neut cm oe
    show sayori neut cm oe
    m "Вообще подождите: я ещё не озвучила своё решение."
    show monika cm ldown
    show yuri sad cm oe
    show natsuki cross casual pout om oe
    show sayori b1c
    n "Ой, да ну, серьёзно?!"
    show monika -b1e
    show natsuki cm
    show sayori om
    s "Мони..."
    show sayori cm
    "Это ж шанс пожрать на халяву тех самых кексов от Нацуки..."
    "А если честно, то это знатно обрадует Сайори."
    "И остальных."
    show monika doub cm oe
    show yuri neut cm e1d
    show natsuki neut cm oe
    show sayori happ cm oe -b1c
    mc "Моника, почему бы нам просто не провести на следующей неделе первый клубный день за чаепитием?"
    show monika neut cm oe
    show yuri happ cm oe
    show natsuki turned casual sedu cm ce lhip rhip
    show sayori om e4c lup rup at h44
    s "ДА!"
    show yuri om
    show natsuki e1a
    show sayori cm ldown rdown
    y "По поводу чая: сервиз можно одолжить у Клуба выпечки, как в прошлые разы, а я в свою очередь принесу ингредиенты для заварки."
    show yuri e1b lup
    show sayori oe
    y "Как раз недавно купила новые сорта, хотела попробовать на днях, но раз такой случай..."
    show yuri cm oe ldown
    show natsuki om e1b ldown rdown
    n "Ну, если вы мне поможете с кексами, то к понедельнику они точно будут готовы."
    show natsuki cm e1a
    mc "Ну так что, Моника?"
    show yuri ce
    show sayori om ce
    s "Пожалуйста!"
    show monika om
    show natsuki neut cm oe
    show sayori cm
    m "Н-но..."
    show monika flus om oe
    show yuri neut cm e1d
    show natsuki angr cm oe lhip rhip
    show sayori neut cm oe b1c
    m "Стихи..."
    show monika neut cm oe
    show natsuki om
    n "Да фиг с этими стихами!"
    show yuri happ cm oe
    show natsuki pout mh oe
    n "Один день себя побаловать нельзя, что ли?"
    show natsuki cm
    show sayori om
    s "Мони, ну пожалуйста..."
    show monika anno cm ce
    show natsuki ldown rdown
    show sayori cm
    m "..."
    show monika oe
    pause 1.0

    show layer master:
        pos (640, 360) anchor (0.5, 0.5)
        linear 120 pos (2400, 1000) zoom 4.0

    "Не надо.{w} Сверлить.{w} Меня.{w} Взглядом."
    "Да, я поддержал эту идею."
    "Да, я хочу попробовать кексы."
    "И да, мне совершенно не хочется выдавливать из себя новый стих."
    "Но ради счастья Сайори можно же отказаться от одного клубного дня!"
    "Ради светлого счастья!"
    "Ну же!"
    show monika ma
    "Соглашайся, Моника!"

    show layer master

    show monika happ om oe
    show natsuki happ cm oe
    show sayori happ cm oe -b1c
    m "М-м, хорошо."
    show monika ce lpoint rhip
    show yuri ce
    show natsuki ce
    m "Итак, друзья: я объявляю следующее клубное собрание посвящённым нашему воссоединению!"
    show monika laug ma ce ldown rdown
    show yuri laug cm ce
    show natsuki pani cm ce at h43
    show sayori yand om ce lup rup at h44
    s "{sc=2}УРА-А-А-А-А!!!{/sc}" with vpunch
    show natsuki om
    show sayori cm
    n "А-А-А, УШИ!"
    show yuri happ cm ce
    show natsuki pout cm ce
    show sayori ma ldown rdown
    "Вот, другое дело!"
    show monika happ cm oe
    show yuri om oe
    show natsuki neut cm oe
    show sayori happ cm oe
    y "Нацуки, ты что-то там говорила про количество кексов..."
    show yuri cm
    show natsuki om
    n "А, точно."
    show natsuki lhip rhip
    n "Раз нас теперь 5 человек, то кексов надо...{w}прилично."
    show natsuki e1b
    n "Штук..."
    show yuri neut cm e1d
    show natsuki curi om ce
    show sayori neut cm oe
    n "...э-э-э..."
    show monika vsur md oe
    show yuri lsur cm oe
    show natsuki neut om oe
    show sayori vsur cm oe
    n "...около 30-ти, думаю."
    show natsuki cm
    mc "30?!"
    "6 на одного человека?!"
    show monika neut cm oe
    show yuri om
    y "Ты раньше готовила не больше 12-ти."
    show natsuki doub cm oe
    y "Уверена, что не перебарщиваешь?"
    show monika happ cm ce
    show yuri neut cm e1d
    show natsuki om
    show sayori neut cm oe
    n "Эти 12 штук вы съедите в первые 5 минут."
    show natsuki neut om oe
    n "Поэтому надо намного больше."
    show monika oe
    show natsuki dist om ce
    n "Как я и говорила: мне нужны продукты, много места и помощь от вас."
    show natsuki oe
    n "Ещё надо будет аккуратно транспортировать кексы в клуб и закрыть в кладовке."
    show natsuki ce
    n "А значит, придётся оставить их у Макса до понедельника, что тоже было сказано..."
    n "Поэтому..."
    show yuri e1b
    show natsuki neut om oe
    n "Чтобы не терять время, нам надо уже сегодня затариться продуктами."
    show monika neut cm oe
    show yuri e1d
    show natsuki curi om oe ldown rdown
    show sayori e2c
    n "Вопрос: кто составит мне компанию и всё оплатит?"
    show monika e1b
    show yuri anno cm oe
    show natsuki cm
    mc "Среди нас только Моника при деньгах, мы-то бедные..."
    show monika e2a
    show natsuki dist om ce
    show sayori oe
    n "Значит, Моника точно идёт со мной."
    show monika lsur cm oe
    show natsuki cm
    m "Эх?!"
    show yuri neut cm e1d
    show natsuki curi om oe
    show sayori e2b
    n "Ещё кто-то будет?"
    show monika e2b
    show natsuki ce
    n "Мы вдвоём умрём пакеты тащить."
    show natsuki cm
    "Блин, мне надо с Сайори разбираться..."
    show monika neut cm oe
    show yuri om
    show natsuki neut cm oe
    show sayori oe
    y "Я пойду."
    show yuri cm
    show natsuki om
    n "Окей."
    show monika neut cm oe
    show sayori neut cm oe
    show natsuki curi om oe lhip rhip
    n "А ты, Макс?"
    show natsuki cm oe
    show natsuki doub om oe
    n "Ты единственный парень среди нас."
    show monika curi md oe
    show natsuki cm
    show sayori e1f
    mc "Я хотел бы кое-что важное с Сайори обсудить..."
    show natsuki om
    show sayori oe
    n "И что же это за \"кое-что\"?"
    show yuri e1b
    show natsuki cm
    show sayori happ cm oe
    mc "Это \"кое-что\" личного характера."
    show monika nerv cm oe
    show yuri e1d
    show natsuki sedu cm oe
    mc "Да и вообще, вы и так завтра будете эксплуатировать меня и мою кухню, не надо тут наглеть!"
    show natsuki om ce
    n "Пха-ха, засчитано..."
    show monika neut cm oe
    show natsuki happ om oe ldown rdown
    n "Всё, Юри, Моника, вперёд."
    show monika om lpoint
    show yuri neut cm e1d
    show natsuki neut cm oe
    m "Сначала ко мне зайдём: мне надо карту взять."
    show monika cm ldown
    show natsuki om b1d
    n "...хорошо, пошли к тебе."
    show monika om
    show natsuki cm
    m "Макс, мы напишем, когда обратно пойдём."
    show monika flus om e1a lpoint
    m "Будь на связи, ладно?"
    show monika ma ldown
    mc "Угу."
    show monika neut cm oe
    show yuri anno cm oe
    show natsuki anno om oe -b1d
    n "Ну давайте уже, а то ничего не успеем!"
    show monika e1b
    show natsuki cm e1b b1d
    pause 0.2
    hide natsuki
    hide monika
    hide yuri
    with easeoutleft
    pause 0.2
    show sayori at t11
    "..."
    mc "Тишина..."
    mc "Аж непривычно."
    show sayori om e1b
    s "Хе..."
    show sayori cm
    "..."
    mc "..."
    show sayori neut cm e1b
    s "..."
    "Да как вернуться к тому разговору?!"
    mc "..."
    "Ой, к чёрту..."
    show sayori oe
    mc "Я готов тебя...{w}дослушать, Сайори."
    mc "Если ты, конечно, не передумала..."
    show sayori worr cm oe lclose rclose
    s "У...{w}угу."
    mc "Я заметил, что ты снова была весёлой."
    mc "На людях."
    show sayori ce
    mc "Слишком."
    s "Угу..."
    mc "Боюсь, что у тебя это вошло в плохую привычку."
    show sayori e1a
    mc "И это даже странно: вроде бы позитив -- значит, хорошо, но в чрезмерном количестве он вреден."
    show sayori om
    s "Макс, мы уже разговаривали на эту тему."
    show sayori cm
    mc "Да."
    mc "И мне важно, чтобы ты приняла в себе идею из того разговора и следовала ей."
    show sayori om oe
    s "Эх..."
    show sayori cm
    "Нет, я совсем не понимаю, как до неё достучаться..."
    "Или она уже и так всё осознала, но отторгает..."
    show sayori neut cm oe
    mc "А насчёт твоей...{w}кучки в голове?"
    show sayori om
    s "Кучка?..."
    show sayori worr mb oe
    s "Хе...{w}хе-хе..."
    show sayori ma
    mc "...да, это странно звучит..."
    show sayori mb
    s "Кучка мыслей..."
    s "Тучка мыслей..."
    show sayori neut om e1b
    s "Тучки..."
    show sayori cm
    "Так, она сейчас в себя провалится."
    "А с другой стороны..."
    show sayori e4a
    "Мне же надо вытянуть весь тот эмоциональный шлак, который в ней скопился."
    "Это как с рвотой."
    "...буэх, да..."
    "Если долго терпеть бардак в желудке, то легче не станет, не говоря уж об интоксикации."
    "А вот если спровоцировать рвоту..."
    "Да, больно, да, противно, но по-другому шлаки не выведешь."
    "Здесь тоже самое."
    show sayori oe
    mc "Сайори, расскажи об этом."
    show sayori om
    s "О тучках?"
    show sayori cm
    mc "Да."
    mc "Твоё состояние до нашего прихода..."
    show sayori sad om ce
    s "Ух..."
    show sayori md
    s "..."
    show sayori worr om oe
    s "...сначала мне было больно от пощёчины Нацуки."
    s "Потом мне было больно от ухода Нацуки."
    show sayori ce
    s "Потом мне было больно у себя дома..."
    show sayori cm
    mc "А мысли?"
    show sayori neut cm oe
    mc "Тебя сжирали мысли, верно?..."
    show sayori om
    s "Да."
    show sayori worr om oe
    s "Я корила себя."
    s "Я всё сделала неправильно."
    s "Я хотела сохранить клуб, а в итоге чуть не развалила."
    show sayori e1a
    s "А потом, когда я была дома..."
    show sayori ce
    s "Я не могла ни на секунду успокоиться."
    s "Моё воображение стало играть со мной в жестокие игры..."
    show sayori oe
    s "Я не могла остановить мысли."
    s "Мне ничто не помогало."
    show sayori e1a
    s "Я полностью выбилась из сил."
    s "У меня была слабость во всём теле..."
    s "Я даже не могла пошевелиться."
    s "Каждое движение стоило мне больших усилий."
    show sayori oe
    s "Я была очень вялой и убитой..."
    s "А мысли в голове продолжали бурлить..."
    show sayori cm
    mc "Ужас..."
    show sayori om e1a
    s "Я с трудом уснула."
    s "Моё сердце не хотело успокаиваться, а ком в горле никуда не уходил..."
    show sayori oe
    s "Наверное, вертелась в кровати больше часа, прежде чем уснуть..."
    s "Я думала, что меня немного отпустит на следующий день..."
    show sayori ce
    s "...но ничего не изменилось."
    s "Я была разбитой."
    s "Я не смогла встать с кровати..."
    show sayori oe
    s "Провалялась в ней всё утро..."
    show sayori cm e1a
    mc "...грх, мне надо было сразу к тебе идти, а не остальных ждать, так и думал..."
    show sayori om
    s "Ты хотел навестить меня сам?"
    show sayori neut cm oe
    mc "Шутишь?"
    mc "Я настолько о тебе переживал, что мне даже кошмар приснился."
    mc "Твоя мама не рассказывала, что я сегодня ночью вам в дверь звонил?"
    show sayori om
    s "...н-нет, не помню..."
    show sayori cm
    mc "А вот я приходил!"
    mc "Но на утро мы с Моникой договорились, что навестим тебя всем составом."
    mc "...и, как всегда, всё затянулось..."
    show sayori sad mb oe
    s "...знаешь, я думала, что уже выполнила свою задачу в Литературном клубе."
    s "Я втянула тебя в клуб, где ты подружился с Моникой, Нацуки и Юри."
    s "Ты зажил новой жизнью, Макс."
    s "У тебя появились новые друзья."
    show sayori e1b
    s "А может, даже и отношения..."
    show sayori ma
    mc "Это громко сказано..."
    show sayori mb oe
    s "Но начальный шажочек в этом направлении сделан."
    show sayori ma
    mc "Не отрицаю..."
    show sayori mb
    s "Когда мне пришла эта мысль в голову, я хотела за тебя порадоваться."
    show sayori mh e1b
    s "Но..."
    show sayori md
    s "..."
    show sayori worr om ce
    s "Я понимала, что должна радоваться..."
    show sayori e1a
    s "...но я не могла радоваться."
    s "У меня не было радости."
    s "Я опустела."
    s "Почему, Макс?"
    show sayori sad mh e1g
    s "Я должна была за тебя порадоваться."
    s "Я должна была порадоваться за то, что клуб стал тобой дорожить."
    show sayori cry cm e4d lclosefist rclosefist
    s "{sc=1}Но почему...{/sc}"
    show sayori oe
    s "{sc=1}Почему вместо радости у меня началась\nтряска...{/sc}"
    s "{sc=1}Почему вместо радости у меня стали мутнеть\nглаза...{/sc}"
    show sayori om e1h
    s "{sc=2}Почему вместо радости у меня образовалось\nощущение, будто сердце разрывается пополам?!{/sc}"
    show sayori cm

    play sound hugs
    if cg_a1_d6_s_2.unlocked == False:
        $ cg_a1_d6_s_2.unlock()
    scene s_cg3
    with dissolve_cg
    play music sayori_happy_thoughts fadein 3.0
    pause 0.5
    "Вот она -- эмоциональная блевота..."
    mc "Достаточно, Сайори."
    s "{sc=2}Но мне так больно, Макс!{/sc}"
    s "{sc=2}Я больше не могу держать это в себе...{/sc}"
    s "{sc=2}Всё так болит...{/sc}"
    mc "Я не хочу, чтобы ты страдала и закапывалась из-за этих лживых мыслей ещё больше."
    s "{sc=2}Лживые?...{/sc}"
    mc "Именно."
    mc "И лживые они потому, что в них нет одной очень важной детали, которую ты опустила."
    s "{sc=1}Деталь?...{/sc}"
    mc "Эта деталь -- ты, Сайори."
    mc "Ты смотришь на всю ситуацию с неправильного угла."
    mc "Нет, Литературный клуб стал таким лишь благодаря тебе, это правда."
    mc "Но ты ничего не разрушила."
    mc "Наоборот, очень хорошо, что ты попыталась сохранить клуб, хоть и таким неожиданным способом..."
    mc "Нацуки всё равно бы ушла, что бы мы тогда ни сделали..."
    mc "А ещё ты не смогла порадоваться за нас из-за того, что во всей этой картине не было тебя, Сайори."
    mc "Без тебя Литературный клуб перестанет быть Литературным клубом."
    mc "Нам всем будет больно, если ты нас покинешь."
    mc "И твоя задача как раз заключается в том, чтобы быть вместе с нами."
    mc "Искренной собой."
    mc "Мы все тебя любим, Сайори."
    s "{sc=1}...{/sc}"
    "Чем больше она дрожит, тем сильнее хочется сжать её в объятиях."
    "Надо сейчас по-максимуму расставить все точки над «{color=#fc7e23}i{/color}» и зарядить её энергией."
    "..."
    "Аргх, как же не хочется отпускать!"
    "Никогда ещё не ощущал такие тёплые и крепкие объятия..."
    "..."
    "......"
    "Ладно-ладно, она первая ослабляет хватку."

    scene bg house
    show sayori turned casual sad ma e1g at t11
    with dissolve_cg
    pause 0.5
    mc "Ну как, лучше?"
    show sayori mb e4d
    s "Хе-хе..."
    show sayori e1g
    s "Да..."
    s "На душе стало легче..."
    show sayori ma
    mc "Я старался, ха."
    show sayori mb e4d
    s "Э-хе-хе..."
    show sayori ma
    "У меня самого прямо камень с души..."
    stop music fadeout 6.0
    show sayori e1g
    mc "Может, пройдёмся тогда где-нибудь?"
    mc "Время есть."
    show sayori mb
    s "Можно..."
    s "Только недалеко."
    show sayori ma
    mc "Да, конечно."

    scene bg niigata street suburban 11 day
    show sayori casual turned happ cm ce at t11
    with wipeleft_scene
    show sayori neut cm oe
    mc "Кстати, нам надо будет спросить Нацуки, во сколько завтра состоится готовка кексов."
    mc "А то этот пункт был торжественно проигнорирован."
    show sayori lsur om oe
    s "Ох, хорошо."
    show sayori curi mh e2b
    s "Я даже об этом не подумала..."
    show sayori cm

    scene black with wipeleft_scene
    s "Хэй..."
    mc "А?"
    s "Давай здесь остановимся."
    mc "На площадке?"
    s "Угусь."
    mc "Хорошо, как скажешь."

    scene bg niigata street suburban 12 day
    show sayori turned casual dist cm oe at t22
    with wipeleft_scene
    mc "Эх, тишина..."
    show sayori om oe
    s "Ага..."
    show sayori cm oe
    "Наконец-то окончательное спокойствие..."
    show sayori cm ce
    "После всего случившегося как нельзя кстати."
    show sayori neut om oe
    s "Макс..."
    show sayori cm oe
    mc "М-м?"
    show sayori happ om oe b1b
    s "Спасибо тебе за то, что прогнал мои...{w}тучки."
    show sayori cm oe
    mc "Ха, тебе так понравилось это слово?"
    show sayori om
    s "Просто оно лучше всего подходит моим мыслям."
    show sayori worr om oe -b1b
    s "Я заметила, что когда они на меня наваливаются, то вся голова становится, как в тумане."
    s "Как при дожде..."
    s "Тучки постоянно льют."
    s "Иногда мне нравится такое состояние: оно помогает подумать над собой, исправиться в лучшую сторону..."
    show sayori om ce
    s "Но часто дождь затягивается, становится невыносимо..."
    show sayori om oe
    s "Ты промокаешь насквозь, тебя одолевает дрожь."
    s "А тучки даже не планируют уходить."
    s "Они только начинают лить сильнее."
    show sayori om ce
    s "Спрятаться от них некуда..."
    show sayori neut cm oe
    mc "...но я принёс тебе зонт, не так ли?"
    show sayori happ om oe b1b
    s "Да, ты смог закрыть меня от этих тучек."
    show sayori ce
    s "Ты не бросил меня."
    show sayori oe
    s "Я очень этому рада."
    s "Спасибо тебе..."
    show sayori cm oe
    mc "Куда ж я тебя брошу, хах..."
    mc "Ради этого друзья и созданы."
    show sayori cm ce -b1b
    "В противном случае я был бы бесчувственным мудаком или сволочью, которая нашла бы 3000 причин не идти на контакт первым, чтобы морально помочь."
    "..."
    "Да не буду я своё прошлое вспоминать, хватит."
    "Отпустить давно пора уже, а..."
    show sayori laug cm oe
    mc "Вообще надо тебя официально в сёстры мне записывать."
    show sayori om ce
    s "Ха-ха-ха, я была бы рада такому «официальному» брату!"
    show sayori happ cm ce
    mc "Хотя мы и так с тобой вместе время проводим."
    show sayori om oe lup rup at h22
    s "А так ещё больше!"
    show sayori om ce ldown
    s "Ты бы тогда чистил мне зубы, помогал решать домашнюю работу, покупал бы мне печенье..."
    show sayori sedu cm oe rdown
    mc "Пф, я бы умер от такой натуги..."
    show sayori om oe
    s "Ой, ладно-ладно!"
    show sayori cm
    window hide

    pause 2.0
    show sayori e1b
    pause 4.0

    window auto
    show sayori happ cm oe
    mc "Хм, а твоё \"Мони\" звучит забавно..."
    show sayori om ce
    s "Хе-хе~"
    show sayori om oe rup
    s "Это очень милое сокращение, которое я давно придумала, мне оно нравится!"
    show sayori rdown
    s "У меня так Моника в телефоне записана."
    show sayori cm
    mc "Прикольно."
    show sayori neut om e1b
    s "Я ещё думала над \"Мон-Мон\", но оно..."
    show sayori om e2b curi at s22
    s "...э-э-э..."
    show sayori neut cm oe
    mc "Звучит вызывающе?"
    show sayori at t22
    mc "Будто рэп-исполнитель."
    show sayori happ om ce lup rup at h22
    s "Да!"
    show sayori yand om ce rdown
    s "\"Йо-йо, друзья!\""
    show sayori e1a ldown rup
    s "\"Время делиться рэпом с Мон-Мон!\""
    show sayori cm ce rdown
    mc "Пха-ха, Сайори, не надо, а то от стыда помрём!"
    show sayori happ om oe
    s "...и тут бы вышла На-цу, чтобы сразиться с Мон-Мон в невероятном поединке."
    show sayori cm oe
    mc "А Юри и Сайо?"
    show sayori neut om e2b
    s "Юри бы отвечала за музыку, а Сайо~..."
    show sayori happ cm oe
    mc "...достала бы светящиеся палочки и яро бы поддерживала выступающих."
    show sayori om ce
    s "Да!"
    show sayori cm ce
    play phone_sound new_message_mc
    pause 1.0
    show sayori neut om oe
    s "Это у тебя?"
    show sayori cm
    mc "Да, у меня, у кого ж ещё..."
    mc "Сейчас проверю."
    call skip_block_on

    python in phone.system:
        battery_level = 48
        clock = (14, 8)

    phone register "mc_m_chat":
        time year 2018 day 21 month 4 hour 14 minute 8
        "m" "Макс, мы закупились по полной, идём обратно, закинем всё к тебе в дом, встречайте у входа"

    phone discussion "mc_m_chat"
    $ plot_pause()
    show sayori e1b
    phone discussion "mc_m_chat":
        "mc" "Ок"
    phone end discussion transition

    call skip_block_off
    show sayori oe
    mc "Моника написала, что они закупились и идут обратно."
    mc "Поэтому нам пора потихоньку тоже возвращаться."
    show sayori lsur om oe
    s "Ох, уже?"
    show sayori dist om oe
    s "Ладно..."
    show sayori cm
    call window_close

    call plot_transition

    call window_open
    scene bg residential_day
    show sayori turned casual neut cm e1c at t11
    with wipeleft_scene
    mc "Что-то их всё ещё не видно..."
    show sayori om b1f
    s "Может, задерживаются?"
    show sayori oe
    s "Пакеты, там, еле тащат..."
    show sayori cm cm
    mc "Без понятия, но долго торчать здесь на ногах нет никакого желания."
    show sayori neut cm e1c -b1f
    s "М-м-м..."
    show sayori happ om e2c
    s "О, вот они!"
    show sayori cm
    mc "А, да, идут..."
    "Судя по лицам, Юри и Моника изрядно замотались."
    "Итак, у них...{w}всего два ёмких пакета...{w}и ни один из них Нацуки не прёт."
    "Хотя чего там, если, судя по виду, они её перевесят..."
    "Хм, в отличие от ковыляющих помощниц, она аж вся сверкает энтузиазмом."
    n "{size=17}О, а вот и вы!{/size}"
    show sayori om ce
    s "Ага!"
    show sayori cm
    n "{size=18}Макс, давай, веди на кухню, там всё разложим.{/size}"
    show sayori oe
    mc "Окей..."
    show sayori neut cm e1c
    m "{size=19}Можно мы...{w}посидим у тебя немного?...{/size}"
    y "{size=19}У-у, ноги гудят...{/size}"
    show sayori happ cm oe
    mc "Ой, хорош мучится, дайте сюда свои пакеты."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg kitchen
    show natsuki turned casual curi cm e1b lhip rhip at t21
    show sayori turned casual happ cm oe at t22
    with wipeleft_scene
    show natsuki om
    n "Вроде бы всё."
    show natsuki cm
    show sayori neut cm oe
    my "{size=19}Фью-у-у-у-у...{/size}"
    show natsuki oe
    mc "Кажется, ты их слишком загоняла."
    show natsuki cross casual anno om ce
    n "Ой, блин, я не виновата, что нигде не было «жирного» творога!"
    show sayori lsur cm oe
    n "Пришлось прыгать по всем продуктовым магазинам в округе."
    show natsuki cm
    show sayori om oe
    s "Ох..."
    show natsuki angr cm oe
    show sayori worr om oe
    s "Знала бы, вместо кексов предложила бы другую идею..."
    show natsuki turned casual angr om oe lhip rhip
    show sayori flus cm oe
    n "Ну уж нет, Сайори!"
    show natsuki anno om ce
    n "Я давно их не делала, мне нельзя терять хватку."
    show natsuki neut om oe
    show sayori neut cm oe
    n "А этот случай -- отличный вызов."
    show natsuki doub cm oe
    show sayori happ cm oe
    mc "Не тебе одной..."
    show natsuki om oe
    show sayori cm ce
    n "Ничё, не развалитесь."
    show natsuki neut om oe
    n "Мне просто нужна пара свободных рук для простой работы."
    show natsuki cm oe ldown rdown
    show sayori neut cm oe
    mc "О, точно, вспомнил..."
    mc "Время."
    mc "Когда именно мы будем этим заниматься?"
    show natsuki e1b
    n "Хм..."
    show natsuki om oe
    n "Можно и в 10 утра."
    show natsuki cm oe
    show sayori happ cm oe
    mc "Приемлемо."
    show natsuki doub cm oe
    show sayori om ce lup rup at h22
    s "Можно и в 9!"
    show natsuki om oe lhip rhip
    show sayori cm ce ldown rdown
    n "В 9 я только завтракаю!"
    show natsuki cm oe
    show sayori anno om e1b
    s "Нэ-э-э-э..."
    show natsuki neut cm oe ldown rdown
    show sayori cm
    m "{size=19}А мы, Нацуки?...{/size}"
    show natsuki om oe
    show sayori neut cm oe
    n "Можете прийти и посмотреть."
    show natsuki e1b
    n "И помочь, если понадобится."
    show natsuki oe
    n "Короче, Макс, отпишусь тебе."
    n "Только номер свой дай."
    show natsuki cm oe
    mc "А, да, сейчас..."
    show natsuki om oe
    n "Я его ещё Юри передам и тебе её скину."
    show natsuki cm oe
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day
    show yuri turned windbreaker happ cm oe at t31
    show natsuki turned casual neut cm oe at t32
    show sayori turned casual happ cm oe at t33
    with wipeleft_scene
    show natsuki om oe
    n "До завтра тогда."
    show yuri neut cm e1d
    show natsuki cm oe
    show sayori neut cm oe
    mc "Эй, а Моника?"
    show sayori happ om ce lup rup at h33
    s "Мо-ни, мы закончили!"
    show sayori neut cm oe ldown rdown
    m "{size=19}Да, знаю, но...{w}у меня что-то ноги ещё не прошли...{w}я тут ещё немного посижу...{/size}"
    show yuri lsur cm oe
    show sayori flus om oe
    s "Ох, у тебя ничего такого нет?!"
    show yuri neut e1d
    show sayori cm oe
    m "{size=19}Не-не, всё в порядке, просто устала.{/size}"
    show sayori neut cm oe
    m "{size=19}Уйду чуть позже.{/size}"
    show yuri happ cm ce
    show natsuki happ cm oe
    show sayori happ cm oe
    m "{size=19}До завтра, девчата!{/size}"
    show sayori om ce
    s "Пока~"
    show yuri om oe
    show sayori cm ce
    y "До встречи."
    show yuri cm oe
    mc "До встречи."
    call window_close

    scene black with dissolve
    pause 2.0
    play sound house_door_open
    play noise_3 street_suburban_noise fadein 1.0
    pause 4.0
    stop noise_3 fadeout 1.0
    play sound house_door_close
    pause 1.0
    call window_open
    "Как будто сегодня меня не хотят оставить одного..."
    call window_close
    play noise_1 mc_steps_house
    pause 3.005
    stop noise_1
    play sound hugs

    call window_open
    m "БАМ!"
    mc "Тьфу!"
    m "Испугался?"
    mc "Предупреждать надо!"
    m "Ха-ха-ха!"
    play music mc_with_monika
    m "Ну что, теперь я у тебя в гостях, Макс!"
    mc "Да уж..."
    mc "Понятно, почему у тебя ноги «не прошли»..."
    mc "Патологический Вы врун!"
    m "Ха-ха!"
    m "Ай!"
    mc "Осторожно!"
    m "Ноги по-настоящему болят..."
    m "Можно прилечь у тебя на кровати?~"
    mc "Ты помрёшь по пути."
    m "М-м?"
    mc "Она на втором этаже."
    m "Но ведь ты же поддержишь меня в трудную минуту?"
    mc "Ё-моё..."
    mc "Залезай на спину."
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom at mc_bed_deep
    show monika forward green_hoodie happ cm oe at e11
    with wipeleft_scene
    show monika om ce
    m "Фух, спасибо~"
    show monika cm ce
    mc "Не за что."
    show monika neut cm oe
    mc "Жаль у меня из лекарств нет какой-нибудь мази..."
    show monika happ om oe
    m "О, не переживай."
    show monika e1b
    m "Я полежу условно час, после чего смогу спокойно ходить."
    show monika cm
    mc "Надеюсь..."
    "Я прямо как Сайори: такой же беспокоящийся и заботливый, когда дело доходит до кого-то знакомого."
    show monika om ce lpoint
    m "У тебя тут довольно уютно."
    show monika neut cm oe ldown
    mc "Скорее небогато."
    show monika e1b
    mc "Шкаф с книгами, которые я не читаю, потому что не нравятся подобные, не я их собирал всё-таки..."
    mc "Телевизор, которым я периодически пользуюсь, чтобы глянуть всякие передачи и новости..."
    mc "Старая приставка, которая мне не нужна..."
    mc "Шкаф с вещами, их там не очень много..."
    mc "Тумбочка..."
    mc "Компьютер..."
    mc "...и кондиционер."
    mc "Всё."
    show monika om oe
    m "У меня примерно так же, Макс."
    show monika happ om ce b1b
    m "Не подумай, что я чрезмерно богатая особа."
    show monika oe b1f
    m "Стала бы такая общаться с кем-то, вроде тебя?"
    show monika cm
    mc "Хм..."
    show monika om ce -b1f lpoint
    m "Вот видишь."
    show monika oe ldown
    m "У тебя уютно и удобно, а это главное."
    show monika cm
    mc "Наверное..."
    show monika dist om e1c
    m "Даже и не верится, что ещё обед, хотя в сон так клонит..."
    show monika cm
    mc "Сегодня было много всего эмоционального, неудивительно."
    show monika om ce
    m "И не говори."
    show monika cm
    "Точно, заметку надо сделать..."
    stop music fadeout 2.0
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom at mc_bed_deep
    show monika forward green_hoodie happ cm oe at e11
    with wiperight
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 21,
            description = "Отличные новости: Нацуки помирилась с Юри, мы все дружно навестили Сайори + я вытянул из неё негатив. Не думал, что всё так успешно пройдёт. Хотя и не сказать, что случай какой-то невероятный... Конфликт есть конфликт."
        )

        current_day = (21, _("СБ"))

    python in phone.system:
        battery_level = 48
        clock = (15, 38)

    show screen phone_calendars() with Dissolve(0.5)
    $ plot_pause()
    hide screen phone_calendars with Dissolve(0.5)

    window auto
    show monika om b1f
    m "Что ты там смотрел?"
    show monika cm
    mc "Так интересно?"
    show monika om ce -b1f
    m "Ну, если это личное, то не говори, не настаиваю."
    show monika cm oe
    mc "Просто заметку в календаре написал о нашем воссоединении."
    mc "На память, так сказать."
    show monika om e1b
    m "Ясненько."
    show monika cm
    m "..."
    show monika flus cm oe
    m "М-м-м..."
    show monika e1a
    mc "М-м?"
    show monika om
    m "Знаешь, я боялась, что Литературный клуб дал трещину..."
    show monika oe
    m "Как будто это была точка невозврата."
    show monika om ce
    m "Мне давно не было так страшно."
    show monika cm
    mc "Моника, ты принимаешь это слишком близко к сердцу."
    show monika neut cm oe
    mc "Разве у вас вообще не было конфликтов?"
    show monika om
    m "Неа."
    show monika dist om oe
    m "Да и какие, если мы стали таким клубом, который ты знаешь, лишь ближе к концу прошлого учебного года..."
    show monika cm
    mc "Хм..."
    show monika neut om ce
    m "Ох, всё, засыпаю..."
    show monika happ om oe
    m "Не хочешь прилечь рядом?~"
    show monika cm
    mc "С каждым разом ты всё более странная..."
    show monika om ce
    m "Хах, я как была собой, так ей и остаюсь."
    show monika cm
    mc "Ладно, прилягу, тоже надо передохнуть."

    scene black with dissolve
    pause 0.25
    mc "Надеюсь, мы не сваримся..."
    m "Не так уж тут и жарко."
    mc "Если нужно будет включить кондиционер, то только скажи."
    m "Хорошо."
    "А, точно, я же хотел обдумать натягивание меня на отношения..."
    m "Спасибо тебе, Макс..."
    mc "Хм?"
    m "Спасибо, что стал частью нашего клуба."
    mc "Ну...{w}пожалуйста, Моника."
    "Прижалась ещё всем телом и уткнулась мне головой в верхнюю часть груди..."
    "..."
    "Хотел сказать уже про опасения от потенциального заражения, но...{w}меня будто отпустило."
    "К счастью, эта болезнь оказалась очень слабой."
    "..."
    "Вообще..."
    "Стоит ли тут кого-то выбирать?..."
    "Не-не-не, давайте всё объективно проанализируем!"
    "Первое -- внешность."
    "..."
    "...да все участницы клуба красивые."
    "Как-то я не акцентировал на этом своё внимание..."
    "Хотя именно такая «красота» не очень часто встречается, не говоря уже про 4-ёх девушек в одном клубе."
    "Окей, тогда второе -- характер."
    "..."
    "Ну они тоже все хороши!"
    "Со всеми спокойно находится общий язык, темы для разговора..."
    "Подробности характеров у себя прокручивать не буду, и так ясно, кто они, как себя ведут, какие у них проблемы..."
    "Грх, и тут не выберешь..."
    "Может, тогда третье?"
    "Уровень близости."
    "Сайори -- близкий друг, который всегда поддержит и которого самому надо поддерживать."
    "Как подмечал, она мне больше в сёстры идёт."
    "Нацуки -- соклубница, которая, может, и подколет по приколу или жёстко ответит, но способна к взаимопонимаю и эмпатии."
    "С ней больше сплошная развлекаловка, нежели что-то ещё."
    "Юри -- соклубница, с которой можно тихонько провести время."
    "Тут скорее как: я в её интересах плохо разбираюсь, но при этом она всё равно старается поддержать разговор."
    "Есть несколько общих вещей в поведении."
    "А ещё, если это прямо правда-правда, влюблена в меня..."
    "И вроде бы прекрасно, готовый фундамент для отношений, но...{w}если бы было всё так просто..."
    "Есть ещё Моника."
    "И с ней у меня проще получается общаться."
    "Тоже есть много общего."
    "И, учитывая её странно поведение, тоже неровно ко мне дышит..."
    "И как раз по степени близости она стоит на первом месте."
    "И если абстрагироваться от всех своих мыслей, неготовности нести ответственность за отношения и всего того, что я успел пережить со всеми..."
    "...я бы выбрал..."
    "..."
    "Кого бы...{w}я выбрал..."
    "......"
    "Ну решайся уже, Макс!"
    "Пора взрослеть и принимать важные выборы, которые повлияют на твою дальнейшую жизнь!"
    "Судьба дала тебе такой невероятно редкий шанс..."
    "И надо быть полнейшим дегенератом, чтобы им не воспользоваться."
    "Как мне там психолог писал?"
    "Я должен максимально серьёзно подойти к выбору спутника по жизни."
    "Без аффекта и эмоциональных порывов."
    "И этот момент только что настал."
    "Даже забавно: тогда, на момент сообщения, я думал, что этот выбор падёт где-то на 26 лет."
    "Ну, может, на 30."
    "Но не как на 18."
    "..."
    "Я выберу...{w}человека, который наиболее ближе ко мне по психотипу..."
    "...{w}того, кто точно готов нести всё это бремя..."
    "...да вашу ж мать, да, я время тяну!"
    "Вопросы?"
    "..."
    "{sc=1}...{/sc}"
    "{sc=2}......{/sc}"
    "{sc=2}МОНИКУ.{/sc}"
    "{sc=1}Я.{w} ВЫБИРАЮ.{w} МОНИКУ.{/sc}"
    "{sc=1}И ЭТО.{w} {b}МОЙ{/b}.{w} ВЫБОР.{/sc}"
    "ПЛЕВАЛ Я НА МНЕНИЕ ОКРУЖАЮЩИХ."
    "ОНА НЕ РАЗ ПОКАЗЫВАЛА МНЕ ЗНАКИ ВНИМАНИЯ."
    "ОНА НАИБОЛЕЕ БЛИЖЕ ВСЕХ ПО ВСЕМ ХАРАКТЕРИСТИКАМ."
    "ВСЁ."
    "Я СДЕЛАЛ СВОЙ ВЫБОР."
    "Я СПАТЬ."
    call window_close

    return
