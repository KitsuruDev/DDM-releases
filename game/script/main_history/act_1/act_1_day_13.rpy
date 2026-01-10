
label act_1_day_13:

    pause 3.0

    show loading_sign_mc at loading_sign_position with dissolve
    pause 4.0

    if ach_a1_d12.unlocked == False:
        $ ach_a1_d12.unlock()

    pause 8.5
    hide loading_sign_mc with dissolve
    pause 2.0

    show screen new_day(episode) with dissolve_scene_full
    pause 6.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    mc "{cps=20}...{/cps}"
    "{cps=20}...{/cps}"
    "{cps=20}...я победил...{/cps}"
    mc "{cps=20}{size=19}...я победил.{/size}{/cps}"
    mc "{size=19}Ха-ха-ха-ха-ха!{/size}"
    "НАКОНЕЦ-ТО!"
    "Я смог дать им отпор!"
    "...только всё в голове перемешалось -- ничего не могу нормально вспомнить..."
    "Особенно подробности разговора с псевдо-Нацуки: они вообще полностью выветрились."
    "А там же была полезная информация, а-а-а..."
    s "{cps=20}...амф-ф-ф, что ты...{w}хихикаешь...{/cps}"
    mc "Сайори, кажется, твой план сработал."
    s "{cps=20}...правда?...{/cps}"
    mc "Чего ты такая сонная?"
    s "{cps=20}...так это...{w}сплю...{/cps}"
    mc "Логично..."
    "Время-то сколько..."
    window hide

    $ phone.calendar.current_day = (28, _("СБ"))

    python in phone.system:
        battery_level = 49
        clock = (6, 0)

    show screen phone() with Dissolve(0.5)
    $ plot_pause()

    window auto
    "Ровно 6 утра..."
    window hide

    hide screen phone with Dissolve(0.5)

    window auto
    mc "{size=19}...пробежка...{/size}"

    scene black with dissolve
    pause 0.25
    mc "Сайори, вставай."
    s "{cps=20}...ещё пять...{w}пять...{w}пя...{/cps}"
    mc "Кто-то там на пробежку собирался!"
    mc "Уже 6 утра!"
    s "{cps=20}...у-у...{/cps}"
    mc "Ты ж раньше меня встаёшь -- ни свет ни заря."
    mc "А тут вся размякла..."
    s "{cps=20}...ты там...{w}иди...{w}я чуть позже вста...{w}у-у-у...{/cps}"
    mc "Хорошо, пойду пока завтрак сделаю."
    mc "Только не усни, а?"
    s "{cps=20}...угу...{/cps}"
    call window_close

    call plot_transition

    call window_open
    scene bg kitchen with wipeleft_scene
    "Хорошо у меня были куриные яйца в холодильнике: отметим мою «победу» вкусной яичницей, но в маленькой порции, чтобы она во время бега обратно не вылезла..."
    "Я бы уже приступил есть, но всё-таки надо дождаться плетущуюся Сайори."
    "Не думал, что в выходные она такая спящая..."
    "Хотя теперь понятно, почему она раньше выходила позднее меня на пару минут."
    "Как это парадоксально при её активном образе жизни..."
    "Короче, надо было ставить будильник: уверен, Сайори в такое время только так и просыпается."
    show sayori turned pajamas neut cm e0g at r11
    pause 0.5
    show sayori neut cm ce lup rup
    s "У-у-у-ум-м-м-м..."
    show sayori ldown rdown
    mc "С бодрым утром."
    show sayori e0f
    mc "Еда готова, садись."
    show sayori om
    s "Ви-и-и..."
    show sayori cm e0g
    call window_close

    show sayori at thide
    hide sayori
    pause 0.5
    scene bg kitchen at mc_kitchen_table
    show sayori turned pajamas neut cm e0g at e11
    with dissolve
    pause 0.25

    call window_open
    mc "Как поедим, расскажу, что у меня в кошмаре было."
    show sayori e0h
    s "..."
    "Она будто не с нами."
    "Надеюсь, завтрак вернёт её с небес на землю."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg kitchen at mc_kitchen_table
    show sayori turned pajamas lsur me oe at e11
    with wiperight
    show sayori om
    s "Ничего себе..."
    show sayori me
    "Сказал в общих чертах, как мог."
    "...единственное, что я точно переврал -- убийства ножом и пистолетом."
    "Да, битва на кулаках, где противник отлетает за один удар, звучит не лучше, но...{w}менее кроваво..."
    show sayori happ cm oe
    mc "Не знаю, будут ли ещё кошмары, но это явно переломная точка."
    show sayori om ce
    s "Тогда я должна спать у тебя до того момента, пока ты полностью не выздоровеешь!"
    show sayori cm
    mc "Ты так скоро в моём доме жить будешь!"
    show sayori om oe
    s "А я и не против!"
    show sayori cm
    mc "Сайори..."
    show sayori sedu cm oe
    mc "...давай не будем доводить ситуацию до абсурда."
    show sayori mb
    s "Ой, ладно-ладно."
    show sayori happ om oe
    s "Но ещё один разочек, чтобы закрепить твой...{w}э-э-э, результат...{w}можно?"
    show sayori cm
    mc "..."
    "По-моему, она просто развлекается..."
    mc "...разочек, потому что завтра выходной."
    mc "И всё."
    show sayori om ce
    s "Ура!"
    show sayori cm
    mc "Только не надо снова на меня свои ноги закидывать, ладно?"
    show sayori curi om oe
    s "Э?"
    show sayori cm
    mc "Я ночью немного проснулся и почувствовал, что мне что-то давит на грудь."
    show sayori neut cm e2a
    mc "Я не знаю, как ты так извернулась, но там оказалась твоя нога."
    show sayori nerv cm oe
    mc "Ещё немного и ты бы мне ступнёй лицо придавила."
    show sayori mb
    s "Э-хе-хе..."
    show sayori cm
    mc "Ты уж поаккуратнее."
    show sayori happ om ce
    s "Постараюсь!"
    show sayori nerv mb oe
    s "Но оно само..."
    show sayori cm
    mc "Да я уж понял."
    show sayori happ cm oe
    mc "Ладно, всё, давай готовиться к пробежке."
    mc "Через сколько выйдем?"
    show sayori om
    s "Ну, завтрак был лёгкий, поэтому достаточно и часа."
    show sayori cm
    mc "Отлично, как раз приведу себя в порядок."
    show sayori om
    s "А я попробую вытянуть кого-нибудь ещё."
    show sayori cm
    mc "Договорились."
    show sayori ce
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg residential_day with wipeleft_scene
    mc "М-м-мда..."
    "Либо это я уже сам не замечаю, как тороплюсь, либо Сайори снова закопалась."
    "Пока можно прикинуть, куда лучше сегодня пойти во время похода всем клубом."
    "Но как я могу это сделать, если я был в центре города буквально пару раз, и то давно?"
    "Я тут только окресности худо-бедно знаю."
    mc "Позорище..."
    "Да не люблю я шляться повсюду!"
    "Нет, прогуляться в какие-нибудь интересные места -- да, но в целом..."
    s "{size=19}Макс!{/size}"
    mc "А."
    show sayori turned cat_shirt happ cm oe at l11
    pause 0.5
    show sayori om
    s "Я смогла достучаться до Юри и Моники."
    show sayori neut om e2b
    s "Обе спали..."
    show sayori happ om oe lup
    s "...но согласились на пробежку."
    show sayori cm ldown
    mc "Ясненько."
    mc "Только им уже поздно завтракать."
    show sayori om
    s "Я написала им выпить стакан тёплой воды и съесть что-то очень лёгкое, но с углеводами."
    show sayori curi om e2c
    s "Банан там...{w}энергетический батончик..."
    show sayori neut cm oe
    mc "Что-то я не уверен, что у них найдётся банан с батончиком, и что они успеют перевариться."
    show sayori happ om ce
    s "Значит, позавтракают после пробежки!"
    s "А если уж что-то и найдётся, то у нас ещё где-то 40 минут времени!"
    s "За это время всё маленькое и лёгкое успеет перевариться."
    show sayori cm
    mc "Ладно, по месту разберёмся."
    show sayori oe
    mc "Мы к ним пойдём или встретимся в одном месте?"
    show sayori om
    s "Написала прийти на перекрёсток."
    show sayori cm
    mc "Ну тогда в путь."
    show sayori ce
    s "Угу!"

    scene bg niigata street suburban 10 day
    show sayori turned cat_shirt happ cm e1b at t11
    with wipeleft_scene
    show sayori oe
    mc "Кстати, а Нацуки с Котонохой?"
    show sayori om
    s "Котоноху я решила не мучить."
    show sayori laug cm oe
    mc "Какое снисходительство."
    show sayori ce
    mc "Я ей даже завидую..."
    show sayori om
    s "Ха-ха-ха!"
    show sayori cm
    mc "А Нацуки?"
    show sayori happ om oe
    s "У неё папа."
    show sayori cm
    mc "Всё, ясно."
    "Даже если бы она вышла, вряд ли бы выдержала пробежку."
    show sayori e1c
    "Не говоря уже об удовольствии от такого занятия..."
    show sayori neut cm oe
    mc "Эй, ты опять в той же футболке?"
    show sayori om
    s "Да, а что?"
    show sayori cm
    mc "Не сваришься?"
    show sayori happ om oe
    s "Неа!"
    show sayori ce
    s "Она вентили...{w}вентилятор!"
    show sayori oe rup
    s "Проще говоря, продувается насквозь."
    show sayori neut cm oe rdown
    mc "Она вообще предназначена для бега?"
    show sayori b1d
    mc "А то, по-моему, она такая же, как и розовая..."
    show sayori om
    s "Нет!"
    show sayori lup
    s "Та из хлопка, а это синтетика!"
    show sayori cm
    mc "Хм..."
    show sayori -b1d ldown
    mc "А складки снизу?"
    show sayori om e2b
    s "Складки...{w}да они маленькие."
    show sayori happ om oe
    s "Эта футболка всегда такая."
    show sayori neut cm oe b1d
    mc "...как и розовая."
    show sayori om
    s "Не похожи они!"
    show sayori cm
    mc "Ну-ну."
    show sayori doub cm oe
    mc "Главное, смотри, чтобы ничего не натёрло."
    show sayori om
    s "Я в ней всегда бегаю."
    show sayori cm

    scene bg niigata street suburban 11 day
    show sayori turned cat_shirt happ cm e1c at t11
    with wipeleft_scene
    show sayori e1b
    mc "Надеюсь, они быстро придут."
    show sayori om
    s "Ага..."
    show sayori cm
    mc "О, точно!"
    show sayori neut cm oe
    mc "Моника ещё не сделала общий чат?"
    show sayori om
    s "Неа."
    show sayori cm
    mc "Странно, что у вас его раньше не было."
    show sayori curi mh oe
    s "Да как-то и не нужен был..."
    show sayori neut cm oe
    mc "Хе, обычно люди любят делать кучу всяких групп по различным поводам, куда и тебя приглашают."
    show sayori happ cm oe
    mc "А потом листаешь все эти чаты и не понимаешь, от каких можно избавиться, а от каких -- нет."
    show sayori om e1b
    s "Хе-хе..."
    show sayori cm at t21
    show yuri turned sport_casual happ cm oe at r22
    pause 0.5
    show sayori oe
    show yuri om
    y "Привет всем."
    show sayori om
    show yuri cm
    s "Ух ты, Юри, основательно подготовилась?"
    show sayori cm
    show yuri om lup
    y "Да, хочется сделать всё грамотно и без негативных последствий."
    show yuri cm
    mc "Правильно."
    show yuri neut om e1d ldown
    y "С нами кто-то ещё будет?"
    show yuri cm
    mc "Моника."
    show sayori om
    show yuri happ cm oe
    s "Да, тоже должна скоро подойти."
    show sayori cm
    show yuri om e1b
    y "Понятно..."
    show yuri cm
    "Её спортивная форма смотрится...{w}слишком открыто?"
    "Надеюсь, она не простудится, несмотря на то, что сейчас уже довольно тепло."
    "Хотя именно такую форму я поначалу и ожидал от Сайори."
    show sayori e1b
    "Надеюсь, она хотя бы одевает топик или какой-нибудь...{w}спортивный лифчик."
    show yuri e1c
    "Не знаю, существуют ли такие..."
    show sayori neut cm e1b
    "Я это к тому, что во время бега всё трясётся, причём очень больно, не говоря уже о вытекающих последствиях."
    "Если нам, парням, нужно надеть всего лишь трусы, чтобы всё зафиксировать, то вот девушкам нужен каркас в районе груди."
    "А я ведь даже где-то видел новость, что в некоторых школах хотят запретить ношения лифчиков во время физ-ры..."
    show yuri neut cm e1c
    "Это ж каким надо быть идиотом, чтобы вводить такой запрет в силу?"
    show yuri e1d
    "Давайте ещё всю одежду с ботинками отменим, хрен ли, -- будем бегать как на Олимпийских играх в Древней Греции."
    "Сотрём все ноги, оторвём все органы и сдохнем от солнечного удара."
    show sayori oe
    show yuri om
    y "Сайори, разве ты в этой одежде бегаешь?"
    show sayori om b1d
    show yuri cm
    s "Да."
    show sayori lup
    show yuri lsur cm oe
    s "Эта футболка спортивная, хоть и кривоватая!"
    show sayori ldown rup
    s "И шортовые джинсы просторные, свободные и дышащие!"
    show sayori cm -b1d rdown
    show yuri om lup rup
    y "П-прости, не хотела тебя задеть..."
    show sayori happ om oe
    show yuri neut cm e1d
    s "А, ничего, всё хорошо!"
    show sayori sedu mb oe
    s "Просто мы с Максом недавно затрагивали эту тему..."
    show sayori happ cm oe
    show yuri ldown rdown
    mc "...почему бы тебе не купить такую же спортивную форму, как у Юри?"
    s "Хм-м-м..."
    show sayori om
    s "Как-нибудь позже, если понадобится."
    show sayori cm
    mc "...ладно."
    show sayori at t31
    show monika forward sport_casual happ cm ce at t32
    show yuri at t33
    pause 0.2
    show monika om
    m "Ух, ох..."
    show monika oe lpoint rhip
    show yuri happ cm oe
    m "Я с вами!"
    show sayori om ce lup rup at h31
    show monika cm ldown
    s "Ура, явилась -- не запылилась!"
    show sayori cm ldown rdown
    show yuri om
    y "Привет."
    show sayori oe
    show yuri cm
    mc "Отлично, все в сборе."
    show sayori om
    s "Прикольно выглядишь!"
    show sayori cm
    show monika rdown
    show yuri om lup
    y "Соглашусь, довольно мило."
    show monika om ce
    show yuri cm
    m "Спасибки~"
    show sayori laug ma oe
    show monika cm
    show yuri ldown
    mc "Ну что, теперь все дружно будем догонять Сайори?"
    show sayori om ce
    show monika oe
    s "Ха-ха, а вот и нет!"
    show sayori happ om oe rup
    s "После пары пробежек я «настроила» свою скорость под тебя."
    show sayori cm rdown
    "Если откинуть самую первую...{w}то да, я там меньше выматывался."
    mc "Даже так, нам всё равно надо бежать чуть медленне, потому что нас 4 человека."
    show monika om lpoint
    m "Думаю, в процессе адаптируемся."
    show monika cm ldown
    show yuri om
    y "Да, попробуем найти общий темп."
    show sayori om
    show yuri cm
    s "Ладненько, маршрут следующий!"
    show sayori lup
    s "Начинаем отсюда, заканчиваем в парке на холме!"
    show sayori ce ldown
    show yuri neut cm e1d
    s "Больше объяснять ничего не буду, просто бегите за мной!"
    show sayori cm
    show monika neut cm oe
    show yuri om
    y "А если потеряемся..."
    show sayori oe
    show yuri cm
    mc "Ну, телефон в помощь."
    show monika e1c
    "Какие тут ещё варианты?"
    show sayori om
    show monika happ cm oe
    show yuri happ cm oe
    s "Итак..."
    play music impalpable_force fadein 3.0
    show sayori mc e4c lup rup at h31
    show monika laug cm oe
    show yuri laug cm e2b
    s "ПОБЕЖАЛИ!{w=1.0}{nw}"
    play sound sayori_hide_fast
    show sayori mn ldown rdown at lhide
    hide sayori
    show monika ce
    show yuri ce
    mc "ДА КУДА ТЫ ТАК РВАНУЛА?!"
    play noise_2 mc_steps_outside_run
    play noise_3 sayori_steps_run
    play noise_4 monika_steps_run
    play noise_5 yuri_steps_run

    scene bg niigata street suburban 10 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j31
    with wipeleft_scene
    mc "{sc=3}И ЭТО ТЫ НАЗЫВАЕШЬ \"НАСТРОИЛА\"?!{/sc}"
    show sayori at thide
    hide sayori
    show monika forward sport_casual mi e4c b2b at j32
    pause 0.2
    show monika ml
    m "{sc=3}САЙОРИ, ЧУТЬ МЕДЛЕННЕЕ!{/sc}"
    show monika mi
    show yuri turned sport_casual e4c b2c lup rup at j33
    pause 0.2
    show yuri ml
    y "{sc=3}ДА, ОЧЕНЬ РЕЗКО!{/sc}"
    show yuri mi
    s "{sc=3}ЧТО ВЫ ТАМ ГОВОРИТЕ?!{/sc}"
    s "{sc=3}НЕ СЛЫШУ!{/sc}"
    mc "{sc=3}ТВОЮ Ж ТЫ МАТЬ!{/sc}"

    scene bg residential_day at jugging
    show monika forward sport_casual mi e4c b2b at j21
    show yuri turned sport_casual mi e4c b2c lup rup at j22
    with wipeleft_scene
    "{sc=3}Как её остановить?!{/sc}"
    "{sc=3}Если дёрну за плечо, она точно грохнется!{/sc}"
    "{sc=3}А если...{/sc}"
    mc "{sc=3}МОНИ, ЮРИ, В СТОРОНУ!{/sc}"
    show monika ml e2d
    show yuri e2d
    m "{sc=3}ЧТО ТЫ ДЕЛАЕШЬ?!{/sc}"
    show monika mi
    mc "{sc=3}НАШИ ЛЁГКИЕ СПАСАЮ!{/sc}"
    show yuri e4c

    scene bg niigata street suburban 1 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j21
    with wipeleft_scene
    show sayori at j11
    "{sc=3}Блин, несётся как угорелая!{/sc}"
    "{sc=3}Фиг догонишь!{/sc}"
    mc "{sc=3}САЙОРИ!{/sc}"
    s "{sc=3}...{/sc}"
    "{sc=3}НИХРЕНА НЕ СЛЫШИТ!{/sc}"
    "{sc=3}Нужно подойти ещё ближе!{/sc}"

    scene bg niigata street suburban 2 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j22
    with wipeleft_scene
    y "{sc=3}У меня...{w}ха, ха...{w}дыхание сбивается...{/sc}"
    show sayori at thide
    hide sayori
    m "{sc=3}Юри, держись, ты сможешь!{/sc}"
    "{sc=3}ДА КАК К НЕЙ ПОДБЕЖАТЬ?!{/sc}"
    "{sc=3}Только ближе подхожу, а она уже отрывается!{/sc}"

    scene bg niigata street suburban 3 day at jugging
    with wipeleft_scene
    "{sc=3}А-а-а, проклятая горка!{/sc}"
    "{sc=3}Нет, тут всё мешает мне сократить дистанцию\nдо Сайори!{/sc}"
    my "{sc=3}Фух, ах, ха...{/sc}"

    scene bg niigata street suburban 4 day at jugging
    with wipeleft_scene
    "{sc=3}Ещё выше...{/sc}"
    "{sc=3}Ну давай, дорога, добей меня!{/sc}"
    show sayori turned cat_shirt mn e4c b2a at j11
    pause 0.2
    show sayori mc
    s "{sc=3}Тут машины, если что!{/sc}"
    s "{sc=3}Смотрите по сторонам!{/sc}"
    show sayori mn
    "{sc=3}Не буду я сейчас тратить силы на крик, она всё\nравно не услышит!{/sc}"
    show sayori at thide
    hide sayori
    "{sc=3}Надо подойти ещё ближе, ближе, БЛИЖЕ!{/sc}"

    scene bg niigata street suburban 5 day at jugging
    with wipeleft_scene
    "{sc=3}УРА, поднялись!{/sc}"
    "{sc=3}Теперь можно ускориться, пока ноги окончательно\nне развалились!{/sc}"
    "{sc=3}А они уже забиваются!{/sc}"
    show yuri turned sport_casual e4c b2c lup rup at j22
    pause 0.2
    show yuri ml
    y "{sc=3}Ух, а-а-ах...{w}я сейчас...{w}помру!{/sc}"
    show monika forward sport_casual mi e4c b2b at j21
    show yuri mi
    pause 0.2
    show monika ml
    m "{sc=3}Юри, вперёд, давай-давай!{/sc}"
    show monika mi
    show yuri ml
    y "{sc=3}П-пытаюсь!{/sc}"
    show yuri mi

    scene bg niigata street suburban 6 day at jugging
    with wipeleft_scene
    "{sc=3}Нет, не могу, ноги отнимаются!{/sc}"
    "{sc=3}Пока это САМАЯ хреновая пробежка!{/sc}"
    show monika forward sport_casual mi e4c b2b n2 at j31
    "{sc=3}Сайори даже в первый раз так не носилась!{/sc}"
    show monika ml e2d
    m "{sc=3}С-сколько нам ещё?!{/sc}"
    show monika mi
    mc "{sc=3}Чуть меньше половины!{/sc}"
    show monika ml e4c
    m "{sc=3}УЖАС!{/sc}"
    show monika mi

    scene bg niigata street suburban 7 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j22
    with wipeleft_scene
    show sayori mc
    s "{sc=3}Скоро свернём...{w}на узкие улочки!{/sc}"
    s "{sc=3}Будьте...{w}аккуратней!{/sc}"
    show sayori mn
    "{sc=3}Ха-ха, как обычно, она здесь начинает выдыхаться!{/sc}"
    show sayori at thide
    hide sayori
    "{sc=3}Надо воспользоваться этим шансом!{/sc}"
    show yuri turned sport_casual e4c b2c lup rup at j33
    pause 0.2
    show yuri ml
    y "{sc=3}М-мы можем...{w}медленнее?!...{/sc}"
    show yuri mi
    mc "{sc=3}Сейчас...{w}достучусть до неё!{/sc}"
    show monika forward sport_casual mi e4c b2b n2 at j33
    show yuri at j32
    pause 0.2
    show monika ml
    m "{sc=3}Б-быстрее!{/sc}"
    show monika mi

    scene bg niigata street suburban 8 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j11
    with wipeleft_scene
    mc "{sc=4}САЙОРИ!{/sc}"
    show sayori mc
    s "{sc=4}АСЬ?!{/sc}"
    show sayori mn
    "{sc=3}Услышала!{/sc}"
    mc "{sc=3}Медленнее!{/sc}"
    show sayori mc
    s "{sc=4}ДЛИННЕЕ?!{/sc}"
    s "{sc=3}Куда уж длиннее?!{/sc}"
    show sayori mn
    mc "{sc=4}МЕДЛЕННЕЕ!{/sc}"
    show sayori mc
    s "{sc=4}А?!{/sc}"
    show sayori mn
    mc "{sc=4}А-А-А!{/sc}"
    show sayori mc
    s "{sc=4}ХА-ХА-ХА!!!{/sc}"
    s "{sc=4}Прибежим -- скажешь!{/sc}"
    show sayori mn
    "{sc=4}.........{/sc}"

    scene bg niigata street suburban 9 day at jugging
    with wipeleft_scene
    "{sc=3}Я реально начинаю выдыхаться!{/sc}"
    "{sc=3}Не могу уже держать темп!{/sc}"
    "{sc=3}А всё из-за фанатичного бега!{/sc}"
    y "{sc=3}Ох...{w}кажется...{w}второе дыхание!{/sc}"
    show yuri turned sport_casual mi e4c b2c lup rup at j31
    pause 0.2
    m "{sc=3}Юри?!{/sc}"
    show yuri at j11
    pause 0.2
    show yuri at thide
    hide yuri
    pause 0.2
    mc "{sc=3}Ты-то куда рванула?!{/sc}"
    "{sc=3}Они обе сумасшедшие!{/sc}"
    "{sc=3}Я с Моникой в хвосте!{/sc}"
    mc "{sc=3}Мони!{/sc}"
    show monika forward sport_casual mi e4c b2b n2 at j11
    pause 0.2
    show monika e2d
    mc "{sc=3}Мы их не догоним!{/sc}"
    show monika ml
    m "{sc=3}Правда?!{/sc}"
    show monika mc e4c
    m "{sc=3}Ну и не надо!{/sc}"
    show monika mn
    mc "{sc=3}Что?--{/sc}{nw}"
    hide monika
    show monika forward sport_casual mn e4c b2b n2 at e11:
        easein 0.15 yoffset 15
        easeout 0.25 yoffset 0
        repeat
    with dissolve
    pause 0.25
    mc "{sc=4}НЕ ДЁРГАЙ МЕНЯ ТАК!!!--{/sc}{nw}" with vpunch
    stop noise_3 fadeout 3.0
    stop noise_5 fadeout 3.0

    scene black with wipeleft_scene
    mc "{sc=3}Куда мы бежим?!{/sc}"
    m "{sc=3}К другому входу в парк!{/sc}"
    mc "{sc=3}А Сайори и Юри?!{/sc}"
    m "{sc=3}Прибегут к нам через сам парк!{/sc}"
    stop music fadeout 3.0
    stop noise_2 fadeout 3.0
    stop noise_4 fadeout 3.0
    call window_close

    call plot_transition

    call window_open
    scene bg niigata park japanese off entrance
    show monika forward sport_casual me e4b b1b n4 at t11
    with wipeleft_scene
    mc "Ха-а-а..."
    show monika mi
    m "Ах-х-х..."
    show monika me
    mc "...ух-х-х..."
    show monika mi
    m "...ах-х-х..."
    show monika me oe n2
    mc "У меня чуть в глазах двоиться не начало..."
    show monika mi e4b b1b
    m "А у меня чуть в груди не закололо..."
    show monika me
    mc "Блин, фанатизм Сайори порой пугает."
    show monika neut om oe
    mc "Она со мной так никогда не бегала, а тут..."
    show monika happ om oe
    m "Исправится, ха...{w}она умная девочка..."
    show monika cm
    mc "Девочка..."
    "Торпедочка..."
    mc "Так это...{w}захотела побыть наедине?"
    show monika lean sport_casual happ om ce n2 at h11
    m "Хи-хи-хи!"
    show monika cm
    mc "Нам бы по-нормальному это организовать."
    show monika forward sport_casual happ om e1b b1b n2
    m "В ближайшее время это...{w}затруднительно..."
    show monika cm
    mc "Я понимаю..."
    show monika oe -b1b
    mc "...но тем не менее надо что-то придумать."
    show monika neut cm oe
    mc "Кстати, да, насчёт сегодняшнего!"
    show monika nerv cm oe
    mc "Ты ещё не делала общий чат?"
    show monika mb
    m "...неа."
    show monika cm
    mc "Кхм, так и думал..."
    show monika happ cm oe
    mc "Просто я о чём: раз даже Сайори хотела организовать свидание, то мы могли бы придумать что-то такое, где нам бы пришлось разбиться на пары на некоторое время."
    mc "А она будет на подстраховке, чтобы никто ничего не понял."
    show monika curi ma oe
    mc "Ну или попробовать отпустить всех пораньше, а самим где-то притормозить..."
    show monika mb
    m "Ух ты, Макс, решил сразу покорить моё сердечко?~"
    show monika ma
    mc "Да тут бы сначала свою лень со скованностью покорить, а уж потом..."
    show monika happ om oe lpoint
    m "Никогда за тобой такого не замечала, но уверена, что ты справишься."
    show monika cm ldown
    mc "Иного и не надо."
    play phone_sound new_message_monika
    pause 1.0
    show monika om ce
    m "Ха, кажется, нашу «пропажу» обнаружили."
    show monika cm
    mc "Хе..."
    show monika om oe
    m "Тогда сейчас отпишусь, заодно групповой чат сделаю."
    show monika cm
    mc "Хорошо."
    show monika ce at thide
    hide monika
    pause 0.2
    "Так..."
    "...у меня ничего не лезет в голову."
    "Вот серьёзно."
    "Примерный план похода?"
    "Имеется."
    "Идея со свиданием?"
    "Высказана."
    "А детали обсудить невозможно, потому что надо договариваться со всеми."
    mc "Хм-м-м..."
    "Ладно, если не цепляться за этот день, то когда можно будет нормально организовать свидание?"
    "..."
    "...только в следующие выходные."
    "А это ещё целая неделя."
    "Какое издевательство..."
    "В моей жизни всё всегда будет таким кривым и странным, когда у других с этим всё намного проще?"
    $ contact_list["mc"].append("ddlc_chat")
    show monika forward sport_casual happ cm ce at t11
    pause 0.2
    show monika om
    m "Ух, я закончила!"
    show monika cm
    mc "Молодец!"
    show monika oe
    mc "Что будем делать?"
    show monika om e1b
    m "Ну..."
    show monika oe lpoint rhip
    m "Я написала, что мы потерялись и пришли к этому входу."
    show monika ldown
    m "Можно прийти к арке и встретить наших бегунов там."
    show monika cm
    mc "Ладненько, пошли потихоньку."
    show monika rdown

    scene black with wipeleft_scene
    mc "Есть какие-нибудь мысли по моей идее?"
    mc "Только у меня денег мало на «прочие» расходы: придётся вычеркнуть всякие кафешки-рестораны..."
    m "Макс..."
    m "Успокойся, сначала обсудим всё со всеми, а потом уже подумаем над твоим предложением."
    m "Даже если не получится, то ничего страшного."
    m "Главное, что мы проведём время все вместе и получим от этого удовольствие."
    mc "Да это понятно."

    scene bg niigata park japanese off entrance arc 1
    show monika forward sport_casual neut cm oe at t11
    with wipeleft_scene
    mc "Но тут уже целая неделя прошла, а я ничего не сделал."
    show monika anno cm oe
    mc "Дела и нервы всё время сожрали."
    show monika om
    m "Ма-а-акс..."
    show monika cm
    mc "Реально!"
    mc "Что я за парень такой?"
    show monika angr om oe
    m "Макс!"
    show monika cm
    pause 0.1
    hide monika
    show monika forward sport_casual angr me e4c n3 at eyes(y=1425, z=1.5)
    with dissolve
    pause 0.25
    mc "УМ-М!" with vpunch
    show monika neut om ce with dissolve
    pause 0.25
    m "..."
    mc "..."
    hide monika
    show monika forward sport_casual neut cm ce n3 at i11
    with dissolve
    pause 0.5
    mc "Так, а вот это было нечестно!"
    show monika happ cm oe
    mc "Я не был готов!"
    show monika om ce rhip
    m "На это и был расчёт, ха-ха-ха!"
    show monika cm
    mc "Уф..."
    show monika om oe n1
    m "Если бы ты был никудышным, то не стал бы переживать насчёт наших отношений."
    show monika cm
    mc "Это тоже да, но..."
    show monika lean sport_casual happ om oe at h11
    m "Ещё успеешь, сви-ти~"
    m "Всё впереди."
    show monika cm
    "Но ситуация-то от этого не меняется..."
    show monika forward sport_casual neut cm oe
    "Бардак какой-то."
    show monika om
    m "О..."
    show monika cm
    mc "Что?"
    show monika om
    m "Мне кажется или..."
    show monika happ om oe
    m "...да, это Рэйко!"
    show monika cm
    mc "Чего?"
    show monika om ce at thide
    hide monika
    m "Рэйко-сан, привет!"
    r "{size=19}Да ладно, Моника?!{/size}"
    sor "{size=19}Ничего себе...{/size}"
    m "{size=19}Макс, давай сюда!{/size}"
    mc "Пф-ф-ф..."
    "Их-то что сюда занесло?"

    if persistent.add_random_menu == 13:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    scene bg niigata park japanese off entrance arc wall
    show monika forward sport_casual happ cm oe at i31
    show reiko turned vest happ cm oe lhip at i32 zorder 2
    show sora turned casual happ cm oe at i33
    with dissolve
    pause 0.25
    mc "Всем привет."
    show sora om
    sor "Здаров."
    show monika om
    show sora cm
    m "А что вы тут делаете?"
    show monika cm
    show sora curi om oe
    sor "Не видно, что ли?"
    show sora cross casual happ om ce
    sor "Сестру выгуливаю."
    show monika laug cm oe
    show reiko om ce
    show sora cm
    r "Сора, хорош уже, ха-ха!"
    show monika ce
    show reiko cm
    "Рэйко аж на себя не похожа..."
    show monika happ cm oe
    show sora turned rpock happ om oe
    sor "А вы тут чем вдвоём занимаетесь?"
    show monika b1b
    show reiko om oe lpoint
    show sora neut cm oe
    r "Уже во всю «обрабатываешь» своего новенького?"
    show monika om
    show reiko cm lhip
    m "Рэйко..."
    show monika ce -b1b rhip
    show reiko vsur cm oe
    show sora lsur cm oe
    m "Мы уже в отношениях."
    show monika cm
    show reiko om
    show sora rdown
    r "Да ну?!..."
    show reiko cm
    show sora om
    sor "...на."
    show monika oe
    show sora cm
    mc "Чистая правда."
    show reiko happ om oe b1c lpoint
    r "Сора, видишь?!"
    show reiko tough vest happ_om_oe -b1c
    show sora angr cm oe rpock
    r "Тебе тоже уже пора!"
    show reiko turned vest neut om ce lhip rup
    r "А то скоро начнётся вуз с работой, там будет совершенно не до этого."
    show reiko oe rdown
    show sora om ce lface
    sor "Ой, не надо мне тут этого."
    show reiko happ cm oe
    show sora happ om oe be ldown
    sor "Сама-то без парня!"
    show monika b1b
    show reiko om ce lpoint
    show sora cm
    r "Это потому что вокруг одни бездари."
    show reiko cm lhip
    show sora om ce -be
    sor "Пф, тоже мне, принцесса «голубых» кровей."
    show reiko oe
    show sora oe be
    sor "Вообще, кто о тебе позаботится, если у меня будет девушка?"
    show reiko om ce rup
    show sora cm
    r "Я!"
    show reiko cm rdown
    show sora om -be
    sor "Ага, охотно верю."
    show reiko oe b1b
    show sora ce
    sor "Если бы я тебя сегодня не разбудил, ты бы так и провалялась до 10 утра."
    show sora cm
    "Да, Рэйко не в рабочее время -- совершенно другой человек..."
    show monika -b1b
    show reiko om ce
    r "Так, ладно, всё!"
    show reiko oe -b1b lpoint
    show sora oe
    r "Мы ушли от темы разговора."
    show reiko cm lhip
    mc "Короче, мы на пробежку группой вышли."
    show sora neut cm oe
    mc "А по пути пришлось разделиться, поскольку Сайори удрала вперёд."
    mc "И вот мы тут остальных ждём."
    show monika neut cm oe
    show sora om
    sor "А, это та девушка, которая вчера к нам в кабинет с Камуко завалилась?"
    show monika rdown
    show sora cm
    mc "Да."
    show monika om
    m "А что вчера было?"
    show monika cm
    show sora om
    sor "Камуко её знакомила со всем Клубом выпечки и со мной в частности."
    show monika om e1b
    show sora cm
    m "О-о..."
    show monika cm
    show reiko neut cm oe
    show sora curi om oe lup at t54
    sor "{size=19}Кстати, может сказать им?...{/size}"
    show reiko om e1b ldown
    show sora cm
    r "{size=19}Ну скажи, чего уж.{/size}"
    show monika oe
    show reiko oe
    show sora ldown
    r "{size=19}Монике можно доверять...{w}и новенькому, наверное, тоже.{/size}"
    show monika om
    show reiko cm
    m "Чего вы там шепчетесь?"
    show monika cm
    show reiko lhip
    show sora neut om oe at t33
    sor "А, насчёт Выпечки..."
    show monika curi md oe
    show sora ce
    sor "Я думаю, вы и так поняли, что я не просто так туда вступил."
    show sora cm
    m "???"
    show sora oe
    mc "...ясно, тебя туда Рэйко засунула?"
    show monika neut cm e2a
    show reiko happ om ce lpoint
    r "Не засунула, а отправила под прикрытием."
    show reiko cm lhip
    show sora om
    sor "Угу, я должен был повлиять на Кохаку, чтобы она перестала творить всякую дичь."
    show reiko oe
    show sora anno om oe
    sor "Но вы сами видели, какая она...{w}упорная...{w}в плохом смысле этого слова."
    show sora neut om oe
    sor "В общем, делать мне в Выпечке больше нечего, на днях покину его к чертям."
    show reiko neut cm oe
    show sora anno cm oe
    mc "Тогда он развалится..."
    show monika oe
    show sora om lface
    sor "Мы уже обсуждали этот вопрос."
    show sora ldown
    sor "А если выбирать между им и собой, то прости за эгоизм, но я выберу себя."
    show sora ce
    sor "Лучше потрачу время на учёбу и сестру, чем буду каждый день болванчиком прохлаждаться в одном месте с мерзким человеком."
    show sora angr cm oe
    mc "Значит, вы решили гарантированно изгнать Кохаку, но ждёте повод?"
    show sora om
    sor "Да пошла она в пень!"
    show reiko om rup
    show sora cm
    r "Ультиматум уже был озвучен, поэтому да."
    show monika curi md oe
    show reiko rdown
    show sora anno cm oe
    r "Было слишком много подачек с нашей стороны за всё время вплоть до игнорирования её отсутствия на собраниях."
    show monika e2a
    show reiko e1b rthink
    r "И не использовать их во благо...{w}ну это уже край идиотизма."
    show monika doub cm ce
    show reiko oe rup
    r "Наше терпение небесконечное."
    show reiko rdown
    r "Вообще такую наглость за свою жизнь ещё не видела."
    show monika om
    show reiko cm
    show sora neut cm oe
    m "Подождите, стоп-стоп-стоп!"
    show monika lsur om oe
    show sora anno cm oe
    m "То есть...{w}вы знали, что рано или поздно Кохаку начнёт с нами конфликтовать...{w}и ничего с этим не сделали?"
    show monika cm
    show sora om lface
    sor "Ещё раз говорю: делали, но повлиять не удалось от слова «никак»."
    show monika neut cm oe
    show reiko happ cm oe
    show sora neut om oe ldown
    sor "Сейчас вы все можете выдохнуть, потому что Рэйко буквально приставила к её затылку заряженный пистолет."
    sor "Даже если Кохаку совершит ещё один выпад в сторону вашего клуба, то она отлетит сразу."
    show monika curi om oe
    show sora cm
    m "Но откуда гарантия, что она не перестанет преследовать свою цель?"
    show monika md
    show reiko om ce rup
    r "Учителя, директор, отчисление."
    show monika neut cm oe
    show reiko oe rdown
    r "Она уже себе яму выкопала, сама того не ведая."
    show reiko lpoint
    r "Так что, Моника, успокойся, тебе нервы ещё для будущих дел пригодятся."
    show monika flus om ce
    show reiko cm lhip
    m "Как всё запутано-перепутано..."
    show monika cm
    mc "В общем, веселье с Клубом выпечки начнётся в ближайшее время..."
    show sora om
    sor "Ага."
    show monika neut cm oe
    show reiko om ce
    show sora cm
    r "Ой, всё, пойдём мы уже, а то заболтались."
    show reiko cm
    show sora happ om oe
    sor "Да, у нас ещё дела, поэтому времени на прогулку не так много."
    show reiko oe
    show sora ce
    sor "Ещё свидимся!"
    show reiko e1b zorder 3
    show sora cm zorder 2
    pause 0.1
    hide reiko
    hide sora
    with easeoutleft
    pause 0.2
    show monika at t11
    mc "..."
    m "..."
    mc "Мда уж..."
    "Клубная, блин, деятельность..."
    call window_close

    pause 0.5
    play noise_2 sayori_steps_run fadein 5.0
    play noise_3 yuri_steps_run fadein 5.0
    pause 5.0
    stop noise_2
    stop noise_3
    show yuri turned sport_casual flus om ce n2 lup rup at l31
    show sayori turned cat_shirt flus om ce n2 at l32 zorder 2
    show monika happ cm oe at t33
    pause 0.5
    show sayori mi

    call window_open
    s "Фуэ-э-э!!!"
    show yuri dist om ce
    show sayori cm
    y "Фью-ю-ю..."
    show yuri cm
    show monika om ce rhip
    m "Наконец-то мы снова вместе!"
    show yuri neut cm e1d ldown rdown
    show sayori oe
    show monika cm
    mc "Сайори, что ты так носишься?!"
    show sayori vsur cm oe
    show monika oe
    mc "Ладно ещё я, но с тобой Юри и Моника бежали."
    show sayori tap cat_shirt dist om ce n2 at s11
    s "Простите!"
    show sayori oe
    s "Я слишком увлеклась..."
    show yuri anno cm oe
    show sayori cm
    show monika om ce b1b
    m "Кажется, Сайори проще бегать одной, ха-ха..."
    show yuri om
    show sayori neut cm oe
    show monika cm
    y "Надеюсь, мы не развалимся во время похода..."
    show yuri cm
    show sayori turned cat_shirt neut cm oe n2 at t11
    show monika oe -b1b
    mc "До вечера нас должно хватить."
    show yuri neut cm e1d
    mc "По крайней мере у меня тело всегда расклеивалось под конец дня после таких нагрузок."
    show yuri lsur cm oe
    show sayori curi cm oe
    show monika om lpoint
    m "Тогда советую нам поскорее возвращаться обратно, чтобы не терять силы и время."
    show sayori om
    show monika cm ldown
    s "Уже?!"
    show sayori e1a
    s "Мы даже не отдохнули!"
    show yuri e2b
    show sayori cm
    show monika rdown
    mc "Мы будем возвращаться медленно и печально."
    show yuri om
    show sayori oe
    y "У нас вышла достаточно странная пробежка..."
    show yuri cm
    show monika nerv mb e2c
    m "...ну, как вышла..."
    show monika cm
    mc "Ладненько, пошли."

    scene black with wipeleft_scene
    s "Мы, кстати, чуть кого-то не сбили!"
    mc "Кого и где?"
    s "Да нас солнце слепило, когда мы по мосту через пруд бежали."
    s "Только с него сошли, а тут два силуэта!"
    y "Да, было неожиданно..."
    s "Кое-как разминулись."
    mc "...ох, Сайори, знала бы ты, кого вы чуть не сбили..."
    s "А кто это был?!"
    m "Тот, кого мы тоже не ожидали здесь увидеть."
    s "Да кто?!"
    mc "...Рэйко..."
    s "{sc=3}ЧЕГО-О-О?!{/sc}" with vpunch
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "Ура..."
    "Разойдясь по домам и отмывшись от пота и грязи, мы в кои-то веки можем начать обсуждение нашей будущей эпопеи."
    "Уже без 15-ти 8, а мы всё ещё ничего не придумали!"
    "Нам бы по-хорошему уже в 9 (ну или в 9:30) выйти."
    "К слову, что там по чату..."
    "Я в него ещё не заглядывал."
    window hide
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 49
        clock = (8, 46)

    phone register "ddlc_chat":
        time year 2018 day 28 month 4 hour 6 minute 54
        label "Моника создал(а) группу"
        label "Моника переименовал(а) группу"
        label "Моника добавил(а) Юри"
        label "Моника добавил(а) Сайори"
        label "Моника добавил(а) Вас"
        label "Моника добавил(а) Нацуки"
        label "Моника добавил(а) Котоноха"
        "m" "Итак, друзья!"
        "m" "Я наконец-то сделала общую группу нашего клуба!"
        "m" "Можете начинать обсуждение нашего будущего мероприятия"
        "m" "Я, Макс, Сайори и Юри присоединятся позже, потому что мы все на пробежке"
        "n" "Ок"
        "k" "У меня вчера вечером появилось несколько идей"
        "n" "И какие же?"
        "k" "1) можно было бы сходить в океанариум Маринепия Нихонкай: посмотреть на пигвинов, львов, дельфинов, всяких рыбок"
        "k" "Я там была пару раз, особенно красивым местом там является подводный туннель"
        "n" "Фи"
        "n" "Будет скучно"
        "n" "И вообще это надо через реку Шинано переходить на самое северное побережье!"
        "n" "Мы умрём"
        "k" "Хорошо, другой вариант"
        "k" "2) парк Хакусан: он небольшой, но там можно полюбоваться природой"
        "n" "> небольшой\nCкучно X2\nПереходить Шинано => мы умрём X2"
        "k" "Ладно, третий вариант!"
        "k" "3) Ниигата Дайдзингу: я там тоже была, там интересная атмосфера"
        "n" "> небольшой храм\nCкучно X3\nПереходить Шинано => мы умрём X3"
        "n" "И что там атмосферного?"
        "k" "Природа!"
        "k" "Там единение с природой"
        "n" "Единение с природой -- это когда тебя прихватило, а из туалетов у тебя только туалетный пакет"
        "k" "ФУ!"
        "k" "Тебе вообще что-то может понравиться?"
        "n" "Да"
        "k" "Ну и что?"
        "n" "ТЦ KoKoRo"
        "n" "Его нам за глаза хватит"
        "n" "Там и ресторанчики, и куча всякой еды, и тп, и тд"
        "n" "А ещё он в разы ближе, чем все твои перечисленные варианты"
        "k" "Потратить целый день на какой-то торговый центр?"
        "n" "Нет блин давайте шляться на другом конце Ниигаты!"
        "n" "Уж лучше в его сердце... буквально"
        "k" "Клянусь, у меня найдутся деньги на паром, который отвезёт тебя на остров Садо и который там тебя и оставит!"
        "n" "Хочешь бросить хрупкую и беззащитную подругу на произвол судьбы?"
        "k" "Ничего, там около 50000 жителей -- позаботятся о тебе"

    phone discussion "ddlc_chat"
    $ plot_pause()
    $ phone.system.clock = (8, 49)
    window auto
    "Кто бы сомневался..."
    "Полноценный бардак."
    phone discussion "ddlc_chat":
        "mc" "Блин, мы ещё не освободились, а вы уже пособачиться успели"
        "n" "Ну хоть кто-то ожил"
        "n" "Вы там на пробежке не сдохли?"
        "mc" "Живые, куда мы денемся"
        "k" "Нацуки слишком ленивая"
        "k" "А ещё думает лишь о еде..."
        "n" "Мы полдня угробим на хождение по твоим местам!"
        "n" "И вообще я за остальных думала, они же носились непонятно где"
        "n" "Значит устанут и захотят поесть"
        "k" "Всё, прекрасно, не буду ничего предлагать, сами решайте"
        "n" "Победа"
    $ phone.system.clock = (8, 50)
    phone discussion "ddlc_chat":
        "s" "Аааа не надо ссориться!!!"
        "mc" "Так, давайте сначала мы ВСЕ соберёмся, а уже потом будем думать"
        "mc" "Уже ж понятно, что поодиночке мы ничего не добьёмся"
        "n" "В итоге будет 6 человек со своими идеями"
        "mc" "...которые мы будем анализировать вместе"
        "n" "(каждый по-своему)"
        "mc" "Нацуки..."
        "mc" "У тебя свербёж в заднице?"
        "mc" "Скучно что ли?"
        "n" "НЕВЕРОЯТНО"
        "n" "Сколько уже можно тянуть?"
        "mc" "Терпи"
        "n" "Нет сил терпеть"
        "mc" "Твои проблемы"
        "n" "> твои проблемы\nА тормозите вы"
        "mc" "Котоноха, во сколько там сегодня паром в Садо отправляется?"
        "k" "Хм, сейчас гляну расписание"
        "n" "Эй!"
        "s" "О мне тоже билетик купите!"
    $ phone.system.clock = (8, 51)
    phone discussion "ddlc_chat":
        "s" "Там места красивые!"
        "mc" "Сайори, это шутка"
        "s" "А да?..."
        "m" "Ух, я снова здесь"
    $ phone.system.battery_level = 48
    phone discussion "ddlc_chat":
        "mc" "Осталась только Юри"
        "y" "Я тоже здесь"
        "mc" "...ладно, не осталась"
        "k" "Ближайшее время отправления парома -- 9:20"
        "m" "Какой паром?"
        "s" "Шуточный..."
        "mc" "Да, это шутка, не обращай внимания"
        "m" "Я просто не читала, что вы тут настрочили"
        "m" "Но вы уже предложили какие-нибудь варианты?"
    $ phone.system.clock = (8, 52)
    phone discussion "ddlc_chat":
        "k" "Я предалагала океанариум, парк, небольшой храм, как достопримечательность, но Нацуки всё отвергла"
        "n" "ТЦ KoKoRo и точка"
        "m" "Негусто..."
        "m" "Есть ещё что-нибудь на примете?"
        "mc" "У меня в голове пусто"
        "n" "А у меня в животе"
        "mc" "Да мы уже поняли"
        "s" "Мне без разницы!"
        "k" "Я уже предалагала выше"
        "k" "А так -- пас"
        "y" "...в еде одна голова"
        "m" "..."
        "n" "АХАХАХА ЧТО?)))"
    $ phone.system.clock = (8, 53)
    phone discussion "ddlc_chat":
        "y" "ОЙ"
        "y" "Голова в еде"
        "y" "......"
        "n" "АХАХВАХВАХАХАВХВ"
        "k" "Ох..."
        "s" "ПРЕДАЛАГАААААЮ"
        "s" "Всем нам пойти сразу покушать"
        "s" "Чтобы думалось легче..."
        "n" "УРА, правильная мысль за сегодня"
        "m" "Да, Сайори говорит дело"
        "m" "Мы так точно ничего не придумаем"
        "mc" "Ну раз вы такие прожоры, то нужно ещё и кафешку выбрать"
        "mc" "Хотя мы даже не определились с набросками основного маршрута..."
        "m" "Это надо по картам посмотреть + отзывы"
        "k" "Подождите"
    $ phone.system.clock = (8, 54)
    phone discussion "ddlc_chat":
        "k" "У меня есть один хороший вариант злополучного кафе"
        "n" "Да ладно, какая ирония"
        "k" "Не язви"
        "n" "Вививи ближе к делу!"
        "k" "Оно находится на краю нашего районе"
        "k" "Мне проще вживую провести, чем тут расписывать"
        "mc" "А цены?"
        "k" "Приемлемые"
        "k" "Не помню, чтобы там было дорого, поскольку это и так не очень популярное кафе, оно же не в центре города или в ТЦ"
        "s" "И там вкусно???"
        "k" "Не прямо супер, но вкусно"
    $ phone.system.clock = (8, 55)
    phone discussion "ddlc_chat":
        "s" "Отлично, одеваемся и выходим!!!"
        "mc" "САЙОРИ, СТОЙ"
        "mc" "Где мы встречаемся?"
        "s" "Эээээээ"
        "m" "Так, друзья, минутку внимания!"
        "m" "Общий сбор на том же перекрёстке, где мы недавно уже были"
        "m" "Нацуки, сама понимаешь, где он находится"
        "n" "Угу"
        "m" "Котоноха, напишу тебе в личку, придём вместе"
        "k" "Поняла"
        "m" "Всем одеваться и выходить!"
        "m" "И если есть деньги, возьмите с собой на всякий случай"
        "m" "А то мне потом от родителей прилетит)"
        "s" "Оки-доки!"
    $ phone.system.clock = (8, 56)
    phone discussion "ddlc_chat":
        "y" "Хорошо"

    phone end discussion transition

    call skip_block_off
    mc "НА-КО-НЕЦ-ТО!"
    "Криво, косо, но хоть как-то договорились."
    "Однако...{w}меня слегка корёжит шестое чувство."
    "Будто что-то не так пойдёт."
    "Но, возможно, это обычное состояние, вызванное отсутствием нормального плана."
    "А я очень не люблю, когда его нет."
    "Потому что надо на что-то опираться, а не наобум всё делать."
    mc "Ладно, всё, хватит думать."
    mc "Нужно надеть что-то выходное и чистое..."
    "А ещё прихватить кошелёк для себя...{w}и для Сайори."
    "А может, и Моники..."
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 2.0
    scene bg niigata street suburban 11 day
    show sayori turned casual neut cm e1b at t11
    with wipeleft_scene
    show sayori oe
    mc "Опять никого..."
    show sayori om e1b
    s "Ага..."
    show sayori cm
    "Вечно все у себя копошатся."
    "Либо я с Сайори чуть ли не пулей вылетел на место встречи."
    s "..."
    mc "..."
    "Чем дольше идёт ожидание, тем больше начинаю нервничать."
    "Неизвестные места, в которых надо правильно себя вести..."
    show sayori e1c
    "Вот как бы смешно это ни звучало, но я никогда не ходил в кафе и рестораны самостоятельно."
    "Вот что там?"
    "Как я официанта должен попросить дать меню?"
    show sayori e1b
    "Крикнуть через всё помещение?"
    "А потом?"
    "Оплата как?"
    show sayori dist cm ce
    "Официант же должен там что-то принести."
    "А потом надо будет деньги куда-то положить...{w}или карту приложить..."
    "У меня мозги уже взбухли."
    "Это ещё хорошо, что у нас, в Японии, чаевые не приняты."
    "А пришлось бы и их ещё куда-то впихивать."
    "А манеры поведения?"
    "Или как класть вилки, ложки, ножи, прочее?"
    "Там же свои маразматичные тонкости."
    show sayori neut cm oe
    mc "Уф-ф-ф..."
    show sayori om
    s "О чём-то подумал?"
    show sayori cm
    mc "Да, но так, мимолётная фигня."
    show sayori om e1b
    s "Ясненько."
    show sayori cm
    n "{size=17}Чем тебе тофу не нравится?{/size}"
    n "{size=17}Сыр как сыр.{/size}"
    n "{size=18}Повкуснее моцареллы, от которой рот вяжет в большом количестве.{/size}"
    show sayori oe
    mc "О, идут..."
    y "{size=18}Тофу пресный.{/size}"
    n "{size=19}Зато благодаря этому его можно добавлять куда угодно!{/size}"
    n "{size=19}Я видела рецепты, где его даже в торты пихали.{/size}"
    show natsuki turned black_shirt curi cm e1b at t31 zorder 2
    show yuri turned windbreaker neut cm e1d at t32
    show sayori happ cm oe at t33 zorder 3
    pause 0.2
    show natsuki om
    n "Правда, я не знаю, какие они после этого по вкусу..."
    show natsuki cm oe
    mc "Новая одежда?"
    show natsuki om
    n "Не очень-то и новая."
    show natsuki cm
    show yuri happ cm oe
    show sayori om ce
    s "Всё равно прикольно выглядит!"
    show natsuki neut cm oe
    show sayori oe
    s "Кстати, вы уже во всю еду обсуждаете?"
    show yuri om
    show sayori cm
    y "Нет, просто так вышло."
    show natsuki pani mj oe
    show yuri cm
    show sayori om ce lup rup at h33
    s "А вот я бы хотела снова попробовать мидии!"
    show natsuki om lhip rhip
    show yuri neut cm e1d
    show sayori cm
    n "Мидии?!"
    show natsuki ce
    show yuri b1f
    show sayori curi cm oe ldown rdown
    n "Бе-е-е!"
    show natsuki cm
    show sayori mh e1a
    s "А что такого?"
    show yuri anno om oe -b1f
    show sayori cm
    y "Да, я тоже не понимаю."
    show sayori happ cm oe
    y "Маринованые в масле мидии достаточно вкусные..."
    show natsuki oe
    show yuri happ cm oe
    show sayori om
    s "Или свежие!"
    show natsuki cross black_shirt pani om oe
    show yuri neut cm e1d
    show sayori cm
    n "Да они склизкие!"
    show natsuki pout om ce
    show sayori neut cm oe b1d
    n "И солёные..."
    show natsuki cm
    show sayori om
    s "Наоборот, прикольно!"
    show natsuki oe
    show yuri happ cm oe
    show sayori rup
    s "Они в любом виде вкусные!"
    show natsuki shoc om oe
    show sayori happ om e1b -b1d rdown
    s "Я и жареные, и варёные ела, и в составе супов...{w}каких-то..."
    show natsuki om ce
    show yuri ce
    show sayori cm
    n "Сумасшедшие!..."
    show natsuki cm
    show yuri oe
    show sayori om oe
    s "Макс, ты же их ел?"
    show sayori ce lup rup at h33
    s "Скажи, что они вкусные!"
    show natsuki pout cm oe
    show sayori neut cm oe
    mc "\"Что они вкусные\"."
    show yuri laug cm oe
    show sayori om b1d ldown rdown
    s "Да не это!"
    show sayori cm
    mc "...ну, вполне."
    show yuri happ cm oe
    show sayori -b1d
    mc "С чем-нибудь пойдут."
    show sayori happ cm oe
    mc "Но если их так есть, то вряд ли удовольствие получишь."
    show sayori om ce
    s "Вот-вот!"
    show natsuki neut cm oe b1d
    show sayori oe
    s "Нацуки, ты когда в последний раз их ела?"
    show natsuki turned black_shirt neut om oe b1d lhip rhip
    show sayori cm
    n "В одна тыща девятьсот каком-то там году!"
    n "И мне этого за глаза хватило."
    show natsuki pout om e1b -b1d
    show yuri neut cm e1d
    show sayori curi cm oe
    n "Меня тогда чуть не стошнило."
    show natsuki cm
    show sayori om
    s "Выходит, это была не мидия, а натуральная кака!"
    show natsuki angr om oe
    show sayori cm e1a
    n "Я гадость в рот не пихаю!"
    show natsuki cm
    show sayori om
    s "Но ведь отравилась?!"
    show natsuki cross black_shirt angr om oe
    show sayori cm
    n "Не говорила я этого!"
    show natsuki sad om oe
    show sayori neut cm oe
    n "Просто в желудке бурда была..."
    show natsuki ce
    n "Он был готов связаться в узел."
    show natsuki cm
    show yuri anno cm oe
    show sayori happ om ce
    s "Значит, отравилась!"
    show natsuki angr cm oe
    show yuri om
    show sayori cm
    y "Очень «аппетитно» такое слышать перед походом в кафе..."
    show yuri cm
    "У меня самого сейчас желудок в узел свяжется и в нём же и повесится."
    show monika forward green_hoodie_long happ cm oe at t51 zorder 2
    show kotonoha casual happ cm oe at t52
    show natsuki neut cm oe at t53
    show yuri neut cm e1d at t54
    show sayori oe at t55
    pause 0.5
    show monika om ce
    show yuri happ cm oe
    m "О, уже все в сборе!"
    show monika cm
    show kotonoha om ce lup rhid
    k "Здрасьте-здрасьте!"
    show monika neut cm oe
    show kotonoha cm oe ldown rhip
    show natsuki turned black_shirt neut cm oe
    show yuri neut cm e1d
    mc "Ура, а то мы уже от обсуждения тофу перешли к отравлениям."
    show monika om
    m "Оу..."
    show monika cm
    show kotonoha e1b
    show yuri happ cm oe
    show sayori om ce lup rup at h55
    s "Ух ты, красивый сарафан, Котоноха!"
    show monika happ cm oe
    show sayori ldown rdown
    s "И прикольная кофта, Моника!"
    show sayori cm
    "Да, им очень идёт..."
    show kotonoha ce
    show yuri om
    show sayori oe
    y "Все воздушные..."
    show monika ce
    show kotonoha om
    show natsuki sedu cm oe lhip rhip
    show yuri cm
    k "Спасибо-спасибо!"
    show monika oe
    show kotonoha cm
    show natsuki om ce
    show yuri angr cm oe
    show sayori neut cm oe
    n "...как тофу."
    show monika neut cm oe
    show kotonoha neut cm oe
    show natsuki anno cm oe
    show yuri om
    y "Тофу пресный и плотный, он не может ассоциироваться ни с этим худи, ни с этим сарафаном."
    show monika e2a
    show kotonoha nerv cm oe
    show yuri cm
    show sayori e2c
    mc "Мы сейчас опять до отравлений дойдём!"
    show monika oe
    show kotonoha om
    show natsuki neut cm oe
    show yuri neut cm e1d
    show sayori happ cm oe
    k "Тогда скорее идите за мной, пока всем не поплохело!"
    show kotonoha cm

    scene bg niigata street suburban 15 day with wipeleft_scene
    "..."
    "Не прошло и минуты, как все резко стали обсуждать друг с другом...{w}да, еду."
    "Будто других тем для разговора нет."
    "С другой стороны, пусть общаются о чём угодно."
    "Главное, что им весело и что они заняты."
    "И что меня не теребят."
    "..."
    "Хм..."
    "Я только сейчас осознал, что Литературный клуб на данный момент -- женское общество."
    "Правда, его классические черты стали проявляться только сейчас, в свободное время и всем составом..."
    "Ну серьёзно!"
    "Они бурно обсуждают какие-то съедобные безделушки, периодически хихикая и тому подобное..."
    show sayori turned casual happ cm oe at t11
    "А если нас занесёт в торговый центр (а нас занесёт), то вся эта компания разбредётся по куче магазинчиков."
    show sayori om
    "Преимущественно со жрачкой."
    show sayori cm
    "Думаю, была бы воля, они бы всю еду в витринах съели."
    show sayori neut cm oe b1d
    "Вместе с витринами..."
    show sayori om
    s "Макс, ку-ку!"
    show sayori cm
    mc "А."
    show sayori om -b1d
    s "Опять в себя провалился?"
    show sayori cm
    mc "Да, задумался..."
    show sayori om
    s "А тебе точно легче стало?"
    show sayori cm
    mc "Ну, я сейчас не о кошмарах думал."
    show sayori om
    s "А в целом?"
    show sayori cm
    mc "Пока рано что-либо говорить."
    mc "Скажу через пару дней."
    show sayori e1b
    s "М-м."
    mc "Ты чего-то хотела?"
    show sayori om oe
    s "А, да так, один вопрос спросить..."
    show sayori happ cm oe
    mc "И какой же?"
    show sayori om b1f
    s "Какиго{image=accent_low_register}{space=-15}ри или Му{image=accent_low_register}{space=-15}ри-Му{image=accent_low_register}{space=-15}ри-сан?!"
    show sayori cm
    mc "Опять еда..."
    show sayori -b1f
    "Толчёный лёд в форме кучки на тарелке или кусок льда в форме кирпича на палочке, который ещё разгрызть надо..."
    "Неудивительно, что его назвали «невозможным»."
    show sayori om
    s "Так что выберешь?"
    show sayori lsur md oe
    mc "Мо{image=accent_low_register}{space=-15}ти."
    show sayori om
    s "Моти?!"
    show sayori laug om oe
    s "Ну ты гурман!"
    show sayori cm
    mc "Ага, щас."
    show sayori ce
    mc "Мне до вашего уровня ещё далеко."
    show sayori om
    s "Хе-хе-хе!"
    show sayori cm ce
    "Не, ну мороженное в тонкой рисовой оболочке удобно есть: и руки не пачкаются, и ничего не отваливается."
    show sayori at thide
    hide sayori
    "Да и в зубы не отдаёт при укусе."
    "А то как пытаешься откусить кусочек мороженого, так сразу все нервы начинают биться в агонии."
    "Будто ты со всего размаха влетел зубами в стену или в стол."
    "Или тебе кулаком в них смачно заехали."
    "Хрень какая-то."
    "Лучше уж лизать мороженое до посинения и прижимать его кусочки к нёбу, чем пытаться работать зубами."
    "..."
    "Блин, я тоже о еде стал думать!"

    scene bg niigata street urban 1 day
    show kotonoha casual happ cm oe at t11
    with wipeleft_scene
    show kotonoha om ce rhip
    k "Практически пришли!"
    show kotonoha cm
    mc "Уже?"
    show kotonoha om oe
    k "Я же писала, что на краю района."
    show kotonoha cm at t22
    show sayori turned casual happ om e2a at t21
    s "Но это прямо супер-близко!"
    show sayori oe rup
    s "Мы с Максом, например, здесь постоянно еду покупаем!"
    show sayori cm rdown at thide
    hide sayori
    show natsuki turned black_shirt dist om ce lhip rhip at t21
    n "Вот и прекрасно."
    show natsuki oe
    show kotonoha ce
    n "А то меня уже слегка крючит от голода."
    show natsuki cm
    mc "{size=19}Прожора...{/size}"
    "Она сегодня вообще завтракала?"

    scene black with wipeleft_scene
    k "Итак...{w}входим."
    call window_close

    play sound building_door_open
    pause 0.377
    play sound_2 building_door_bell
    pause 1.5
    stop noise_1 fadeout 0.5
    play sound building_door_close
    pause 1.0

    call window_open
    scene bg niigata cafe local inside
    show monika forward green_hoodie_long happ cm e1b rhip at t21
    show kotonoha casual happ cm e1c at t22
    with dissolve_scene_full
    play music martini_sunset fadein 3.0
    show monika oe
    mc "Довольно уютно."
    show monika om ce
    m "Согласна."
    show monika cm
    show kotonoha om oe
    k "Давайте за свободный столик."
    show kotonoha cm

    scene bg niigata cafe local inside with dissolve_cg:
        blur 15.0
    s "Интересно, есть ли тут какигори..."
    wai "Доброе утро, меня зовут Кайо{image=accent_low_register}{space=-15}ши, я буду вашим официантом."
    wai "Хотите начать с меню, или я могу предложить вам закуску, основное блюдо, десерты?"
    k "Давайте меню, мы выберем блюда и позовём вас для заказа."
    wai "Конечно, держите."
    k "Благодарю!"
    "Довольно оперативно..."
    "В моей голове всё представлялось совсем не так."
    n "Так-с, так-с, так-с..."
    "Хм, тут в основном японский ассортимент, несмотря на весь антураж..."
    n "Да ладно!"
    n "Тонка{image=accent_low_register}{space=-15}цу?!"
    show tonkatsu as t1 with dissolve:
        align (0.5, 0.2)
    pause 0.5
    n "Возьму сразу две порции."
    play sound object_appearance
    show tonkatsu as t2 zorder 2:
        align (0.7, 0.3)
    pause 0.5
    "Ого, сразу на свинину потянуло?"
    hide t1
    hide t2
    with dissolve
    m "...ограничусь окономия{image=accent_low_register}{space=-15}ки."
    show okonomiyaki with dissolve:
        align (0.5, 0.2)
    pause 0.5
    "«Солянка» из продуктов в форме блина...{w}может, тоже взять?"
    hide okonomiyaki with dissolve
    s "О, тайя{image=accent_low_register}{space=-15}ки!"
    show taiyaki with dissolve:
        align (0.5, 0.2)
    pause 0.5
    s "Вкуснотища!"
    hide taiyaki with dissolve
    s "Возьму 5 штук!"
    play sound object_appearance
    show taiyaki as t1 zorder 0:
        align (0.1, 0.5) rotate -45
    pause 0.15
    play sound object_appearance
    show taiyaki as t2 zorder 1:
        align (0.3, 0.25) rotate -22.5
    pause 0.15
    play sound object_appearance
    show taiyaki as t3 zorder 2:
        align (0.5, 0.01) rotate 0
    pause 0.15
    play sound object_appearance
    show taiyaki as t4 zorder 3:
        align (0.7, 0.25) rotate 22.5
    pause 0.15
    play sound object_appearance
    show taiyaki as t5 zorder 4:
        align (0.9, 0.5) rotate 45
    pause 1.0
    "Печенье в форме рыбки со сладкой начинкой, кто бы в Сайори сомневался..."
    hide t1
    hide t2
    hide t3
    hide t4
    hide t5
    with dissolve
    k "Здесь очень вкусный караа{image=accent_low_register}{space=-15}ге."
    show karaage with dissolve:
        align (0.5, 0.2)
    pause 0.5
    k "Не устану его каждый раз заказывать."
    "Мясо курицы..."
    hide karaage with dissolve
    y "Хорошо, попробуем снова этот тофу..."
    show miso_soup with dissolve:
        align (0.5, 0.2)
    pause 0.5
    y "Закажу ми{image=accent_low_register}{space=-15}со-суп."
    hide miso_soup with dissolve
    mc "Хм-м-м..."
    m "Макс, а ты что выберешь?"
    mc "..."
    n "Не тормози, есть хочется!"
    n "Пока они там это всё приготовят, я уже весь стол сожру!"
    mc "Ой, чёрт с вами, возьму ра{image=accent_low_register}{space=-15}мэн."
    show ramen with dissolve:
        align (0.5, 0.2)
    pause 0.5
    s "Может, что-то другое?"
    mc "Нет, этого достаточно."
    hide ramen with dissolve
    "Да ну нафиг сейчас возиться, выбирать..."
    "Был бы один, мог бы спокойно выбрать."
    "А тут осознать не успеваешь, как все всё взяли."
    "Торопыги."
    k "Так, напомните ваши блюда."
    play sound object_appearance
    show tonkatsu as t1 zorder 0:
        align (0.1, 0.1) zoom 0.5
    pause 0.15
    play sound object_appearance
    show tonkatsu as t2 zorder 1:
        align (0.2, 0.1) zoom 0.5
    pause 0.15
    n "Тонкацу, 2 порции."
    play sound object_appearance
    show taiyaki as t3 zorder 2:
        align (0.5, 0.1) zoom 0.7
    pause 0.15
    play sound object_appearance
    show taiyaki as t4 zorder 3:
        align (0.6, 0.1) zoom 0.7
    pause 0.15
    play sound object_appearance
    show taiyaki as t5 zorder 4:
        align (0.7, 0.1) zoom 0.7
    pause 0.15
    play sound object_appearance
    show taiyaki as t6 zorder 5:
        align (0.8, 0.1) zoom 0.7
    pause 0.15
    play sound object_appearance
    show taiyaki as t7 zorder 6:
        align (0.9, 0.1) zoom 0.7
    pause 0.15
    s "Тайяки, 5 штук."
    play sound object_appearance
    show okonomiyaki as t8 zorder 7:
        align (0.1, 0.55) zoom 0.5
    pause 0.15
    m "Окономияки, 1 порция."
    play sound object_appearance
    show ramen as t9 zorder 8:
        align (0.5, 0.55) zoom 0.5
    pause 0.15
    mc "Рамэн, 1 порция."
    play sound object_appearance
    show miso_soup as t10 zorder 9:
        align (0.9, 0.55) zoom 0.5
    pause 0.15
    y "Суп мисо, 1 порция."
    k "Угу."
    play sound object_appearance
    show karaage as t11 zorder 10:
        align (0.5, 0.3) zoom 0.7
    pause 0.15
    k "И ещё моё карааге..."
    k "Так, сейчас закажем."
    mc "Стой, а напитки?"
    mc "Не в сухомятку же всё есть."
    y "Давайте возьмём чай со льдом."
    n "Да что угодно, блин, быстрее!"
    k "Хорошо, чай со льдом."
    play sound object_appearance
    show tea_with_ice as t12 zorder 11:
        align (0.1, 0.1) zoom 0.7
    pause 0.15
    play sound object_appearance
    show tea_with_ice as t13 zorder 12:
        align (0.26, 0.2) zoom 0.7
    pause 0.15
    play sound object_appearance
    show tea_with_ice as t14 zorder 13:
        align (0.42, 0.3) zoom 0.7
    pause 0.15
    play sound object_appearance
    show tea_with_ice as t15 zorder 14:
        align (0.58, 0.4) zoom 0.7
    pause 0.15
    play sound object_appearance
    show tea_with_ice as t16 zorder 15:
        align (0.74, 0.5) zoom 0.7
    pause 0.15
    play sound object_appearance
    show tea_with_ice as t17 zorder 16:
        align (0.9, 0.6) zoom 0.7
    pause 0.15
    k "Официант?"
    k "Мы хотим сделать заказ!"
    scene bg niigata cafe local inside with dissolve:
        blur 15.0
    wai "Что выбираете?"
    k "Караагэ, 1 порция; тонкацу, 2 порции; тайяки, 5 порций; окономияки, 1 порция; рамэн, 1 порция; мисо-суп, 1 порция; чай со льдом...{w}6 стаканов."
    "Как она всё это быстро запомнила?"
    wai "Угу."
    wai "Караагэ, 1 порция..."
    "Ладно, забираю слова назад, этот список уже четвёртый раз повторяется."
    "Ещё немного и он мне в мозг въестся."
    k "Да, всё верно."
    wai "Спасибо."
    k "..."
    k "...ждём..."
    mc "Тогда, может, маршрут обсудим?"
    show prefecture_niigata:
        anchor (0.5, 0.5) xalign 0.5 ypos 250 zoom 1.35 rotate 30
    show screen impose_text("Префектура Ниигата", "#737373", s=40, x=450, y=20) as t0
    show screen impose_text("Река Шинано", "#54acff", x=588, y=365) as t1
    show screen impose_text("Район\nХигаши", "#737373", x=790, y=120) as t2
    show screen impose_text("Район\nТюо", "#737373", s=18, x=680, y=150) as t3
    show arrow_explanation as ar1:
        pos (760, 155) zoom 0.4 rotate -80
    show screen impose_text("Мы где-то\nздесь", "#ff0000", s=15, x=800, y=225) as art1
    with dissolve
    pause 0.5
    n "Моё мнение по этому вопросу не меняется."
    m "Но, по-хорошему, нам бы и на улице нужно пройтись."
    n "Мы и так во всю по улицам шляемся."
    n "А нам ещё обратно пешком возвращаться."
    n "Поэтому только ТЦ-шка."
    play sound object_appearance
    show arrow_explanation as ar2:
        pos (720, 150) zoom 0.4 xzoom -1 rotate 80
    show screen impose_text("ТЦ KoKoRo\n(смотрел по картам,\nона на станции Ниигата)", "#ff0000", s=15, x=610, y=210) as art2
    pause 0.5
    mc "Ну раз ты так ратуешь за торговый центр, то что мы там делать будем?"
    mc "Еда не в счёт: если вы и будете есть, то быстро насытитесь."
    n "Ну..."
    n "Аркадные автоматы там...{w}ещё что-нибудь..."
    y "Кажется, эта прогулка выйдет такой же странной, как и пробежка..."
    m "Друзья, давайте без пессимизма и негатива..."
    m "Подойдём к этому вопросу с холодной головой."
    m "Котоноха, ты хорошо разбираешься в городе?"
    k "Более-менее..."
    m "Здесь есть какие-либо близлежайшие парки, достопримечательности?"
    k "В основном они в центре города."
    play sound object_appearance
    show arrow_explanation as ar3:
        pos (700, 50) zoom 0.4 xzoom -1 rotate -50
    show screen impose_text(
        "Да, я ещё глянул предложения Котонохи, они реально все\nна этом «острове», отделённом рекой Шинано",
        "#ff0000",
        s=15, x=770, y=70) as art3
    pause 0.5
    k "А так, только отдельные и маленькие места, которые в нашем случае не стоят посещения..."
    n "Вот именно."
    n "Придётся топать через Шинано, оно вам надо?"
    k "Подожди-ка..."
    k "Если мы дойдём до торгового центра, то можно будет и дойти до моих мест."
    n "Блин!"
    n "Вы после пробежки, а нам топать в соседний район, потом шляться по ТЦ, а потом ползти обратно!"
    play sound object_appearance
    show arrow_triple as ar4:
        pos (1100, 100) zoom 0.4 rotate 180
    show screen impose_text(
        "Берём в расчёт, что мы пройдём\nсуммарно около 6 километров,\nне считая ТЦ",
        "#ff0000",
        s=15, x=1010, y=175) as art4
    pause 0.5
    n "Если уж и выходить в ваши «океанариумные парки на свежем воздухе с атмосферой храма вперемешку с природой», то надо...{w}что я там хотела сказать..."
    n "А!"
    n "...надо, во-первых, воспользоваться транспортом, а во-вторых, быть морально настроенным!"
    n "А мне лень, так ещё и денег лишних нет."
    play sound object_appearance
    show arrow_triple as ar5:
        pos (1100, 220) zoom 0.4 rotate 180
    show screen impose_text("А если мы решимся пойти по\nместам Котонохи...", "#ff0000", s=15, x=1025, y=295) as art5
    pause 1.0
    play sound object_appearance
    show arrow_triple as ar6:
        pos (1070, 325) zoom 0.4 rotate 200
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar7:
        pos (1030, 390) zoom 0.4 rotate 220
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar8:
        pos (960, 435) zoom 0.4 rotate 250
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar9:
        pos (880, 455) zoom 0.4 rotate 265
    pause 0.15
    show screen impose_text(
        "Длина «острова» в 2 раза больше расстояния от нас до ТЦ,\nт.е. мы потратим примерно 12 километров на его полный обход",
        "#ff0000",
        s=15, x=380, y=485) as art9
    pause 1.0
    play sound object_appearance
    show arrow_triple as ar10:
        pos (310, 455) zoom 0.4 rotate 275
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar11:
        pos (230, 435) zoom 0.4 rotate 290
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar12:
        pos (160, 390) zoom 0.4 rotate 320
    pause 0.15
    play sound object_appearance
    show arrow_triple as ar13:
        pos (120, 325) zoom 0.4 rotate 340
    pause 0.15
    show screen impose_text("Смерть", "#ff0000", x=105, y=300) as art13
    pause 1.0
    mc "Кхгм..."
    k "Лень ей, видите ли..."
    n "А у вас прямо шило в попе топать через весь город ради «прогулки»."
    s "Тогда сходим к аркадным автоматам!"
    m "Ладно, после кафе идём в торговый центр."
    hide screen t0
    hide screen t1
    hide screen t2
    hide screen t3
    hide screen art1
    hide screen art2
    hide screen art3
    hide screen art4
    hide screen art5
    hide screen art9
    hide screen art13
    with dissolve
    scene bg niigata cafe local inside with dissolve:
        blur 15.0
    m "Только надо посмотреть, как к нему лучше пройти..."
    s "Е-е-е!"
    "Пока энтузиазмом горит только Сайори."
    "Хотя посмотрим, проявится ли он позже у остальных..."
    stop music fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street urban 1 day with wipeleft_scene
    "Мда, мы так усердно утоляли утренний голод, что я после разговора о ТЦ ничего не запомнил."
    "Разве что как Моника за всех картой расплатилась, а мы ей пообещали покрыть свои расходы наличкой."
    "...естественно, по возможности."
    "А ещё Сайори пожаловалась на всякие крошки, застрявшие в зубах, поэтому я ей купил маленькую упаковку жвачки."
    show monika forward green_hoodie_long happ cm oe at t11
    pause 0.2
    show monika om ce lpoint rhip
    m "Так, ребята, в путь!"
    show monika oe ldown
    m "Нацуки, корректируй меня, если собьюсь и пойду не туда."
    show natsuki turned black_shirt neut cm oe at t21
    show monika cm at t22
    n "Угу-угу."

    scene bg niigata street urban day 2
    show natsuki turned black_shirt neut cm e1b at t21 zorder 2
    show yuri turned windbreaker anno cm oe at t22
    with wipeleft_scene
    show natsuki oe
    show yuri om
    y "Всё-таки тофу приторный..."
    show natsuki curi om oe lhip rhip
    show yuri cm
    n "Ты ж его сейчас не всухомятку ела."
    show natsuki doub cm oe
    show yuri om ce lup rup
    y "Я чувствовала его нотки сквозь пряный бульон."
    show natsuki om
    show yuri angr cm oe
    n "А я чувствую твои нотки презрения из принципа сквозь извилистые речи."
    show kotonoha casual angr om oe at t31
    show natsuki cm at t32
    show yuri ldown rdown at t33
    k "Нацуки!"
    show kotonoha rhip
    show natsuki neut cm oe b1d ldown rdown
    show yuri neut cm e1d
    k "Вы же на этой неделе клялись, что будете принимать себя такими, какие вы есть!"
    show kotonoha cm
    show natsuki e1b
    s "Ого!"
    show sayori turned casual happ om oe at t41 zorder 2
    show kotonoha neut cm oe at t42
    show natsuki at t43
    show yuri anno cm oe at t44
    s "Когда успели?"
    show sayori neut cm oe
    show kotonoha om
    k "Они же пытались написать совместный стих."
    show sayori om e2b b1f
    show kotonoha cm
    s "Ой, точно, уже забыла..."
    show sayori cm at thide
    hide sayori
    show kotonoha at t31
    show natsuki anno om ce -b1d at t32
    show yuri neut cm e1d at t33
    n "Я хочу...{w}хочу..."
    show natsuki angr cm oe
    mc "...задавить оппонента своим «весом»."
    show kotonoha b3
    show natsuki om lhip rhip
    n "А за это я бы тебя прибила!"
    show natsuki vang cm oe
    mc "Сначала дотянись."
    show natsuki cross black_shirt vang cm ce
    n "ГХ!"
    show kotonoha om ce
    k "Всё, хватит."
    show kotonoha cm
    show yuri anno cm oe

    scene bg niigata street urban day 3
    show kotonoha casual happ cm oe rhip at t31
    show natsuki turned black_shirt neut cm oe at t32 zorder 2
    show yuri turned windbreaker neut cm e1c at t33
    with wipeleft_scene
    show kotonoha om
    show natsuki doub cm oe
    show yuri e1d
    k "Лучше что-нибудь другое обсудите."
    show kotonoha cm
    show natsuki om lhip rhip
    n "Наприме-е-ер?"
    show kotonoha neut cm e1b
    show natsuki cm
    k "..."
    show kotonoha om e1c
    show natsuki neut cm oe
    k "Как насчёт...{w}о-о-о..."
    show kotonoha nerv om ce
    show natsuki curi cm oe
    k "Юри, как твои руки?"
    show kotonoha cm
    show yuri shoc om oe lup rup at h33
    y "АУ!"
    show yuri lsur om oe ldown rdown
    y "С ними всё хорошо!"
    show kotonoha oe
    show natsuki anno om ce
    show yuri cm
    n "Прекрасная смена темы разговора..."
    show natsuki cm
    show yuri ce
    k "..."

    scene bg niigata street urban day 4
    show sayori turned casual happ cm oe at t41 zorder 2
    show kotonoha casual neut cm e1b at t42
    show natsuki turned black_shirt neut cm e1c at t43 zorder 2
    show yuri turned windbreaker neut cm e1c at t44
    with wipeleft_scene
    show sayori om ce
    show kotonoha oe
    show natsuki oe
    show yuri e1d
    s "О, знаю!"
    show sayori oe
    show natsuki curi cm oe
    s "Мы можем ещё кого-нибудь пригласить в наш клуб?"
    show sayori cm
    show kotonoha rhip
    show natsuki om
    show yuri anno cm oe
    n "Пф, будто кто-то прямо так захочет к нам вступить, ага..."
    show sayori neut cm oe
    show kotonoha om
    show natsuki cm
    k "Мы могли бы пригласить ещё Либитину, но она...{w}в общем, не любит клубную деятельность."
    show kotonoha cm
    show natsuki dist cm oe
    show yuri om
    y "Тут больше некого..."
    show sayori om e1b b1d
    show yuri cm
    s "Ме-е-е..."
    show sayori cm

    scene bg niigata street urban day 5
    show sayori turned casual neut cm oe at t51 zorder 2
    show kotonoha casual neut cm oe at t52
    show monika forward green_hoodie_long neut cm oe at t53 zorder 3
    show natsuki turned black_shirt neut cm oe at t54 zorder 2
    show yuri turned windbreaker neut cm e1d at t55
    with wipeleft_scene
    mc "Слушайте, если мы будем разрастаться, то нам придётся полностью трансформировать написание стихов."
    mc "Да, я уже говорил про это Монике, из-за чего мы и попробовали парные стихи...{w}но они не решили данную проблему."
    mc "Нам вшестером трудно будет поодиночке делиться, а тут ещё больше участников станет."
    show natsuki curi cm oe
    mc "Надо что-то с этим делать."
    show sayori curi cm oe
    show monika lsur cm oe
    show natsuki om lhip rhip
    show yuri lsur cm oe
    n "Перестать писать стихи?"
    show monika om
    show natsuki cm
    m "Это наше основное занятие!"
    show sayori neut cm oe
    show natsuki anno cm oe
    m "Мы не будем от него отказываться!"
    show monika cm
    show natsuki om
    show yuri neut cm e1d
    n "Литература -- не одни только стихи."
    show kotonoha happ cm oe rhip
    show monika neut cm oe b1b
    show natsuki cm
    mc "Забавно слышать подобное от человека, фанатеющего по манге."
    show natsuki doub om oe
    n "И чё?"
    show natsuki cm
    mc "Да ничё."
    show monika -b1b
    show natsuki neut cm oe
    show yuri om
    y "Я была бы не против организовать условный читательский уголок, где будут обсуждаться книги со всеми их смыслами и приёмами авторов..."
    show sayori nerv cm oe n2
    show kotonoha neut cm oe
    show natsuki ldown rdown
    show yuri flus om oe
    y "...однако опыт прошлого показывает, что подобное не приветствуется в нашем обществе..."
    show sayori mb
    show yuri cm
    s "Извини, Юри, но книжки очень гигантские!"
    show sayori tap casual nerv om e2 n2 at s51
    show yuri lsur cm oe
    s "Поэтому мы и не решились заниматься подобным, хе-хе..."
    show sayori turned casual neut cm oe n1 at t51
    show natsuki curi cm oe
    show yuri om
    y "Тогда можно было бы заниматься просмотром фильмов-экранизаций или обычных фильмов..."
    show sayori om b1d
    show yuri cm
    s "Но они тоже немаленькие!"
    show sayori cm
    show natsuki om
    n "А ещё нужно оборудование."
    show sayori -b1d
    show natsuki lhip
    show yuri e2c
    n "Тратить мобильный интернет и заряд на такое совершенно не хочется."
    show monika curi cm oe
    show natsuki neut cm oe
    show yuri om
    y "...а если мы будем анализировать короткие произведения, которые на прочтение займут в районе 10 минут?"
    show kotonoha happ cm oe
    show yuri oe
    y "И во время анализа мы будем дискутировать на ту или иную тему..."
    show sayori e2b
    show kotonoha om
    show natsuki ldown
    show yuri neut cm e1d
    k "Хм, а это уже интересно."
    show sayori oe
    show kotonoha cm
    show monika neut cm oe
    mc "Я бы даже сказал прекрасно: дискуссия будет сильнее вовлекать участников, чем стихи."
    show sayori happ cm oe
    show yuri happ cm oe
    mc "Да и в целом веселее будет, нагрузки ещё меньше, плюс польза от участия в адекватных спорах."
    mc "Моника, ты же состояла в Дискуссионном клубе?"
    mc "У тебя должен быть опыт в подобном."
    show monika dist om oe
    m "Да, но там же был сплошной балаган..."
    show monika cm
    mc "Всё равно."
    show monika neut cm oe
    show natsuki angr cm oe
    mc "Если Нацуки ещё немного над собой поработает, то наш состав для такого занятия очень подойдёт."
    show monika e1c
    m "М-м-м..."
    show natsuki om lhip rhip
    n "Эй, это что за недоверие?"
    show natsuki cm
    mc "Напомнить тофу?"
    show natsuki anno om ce
    n "Пф-ф-ф..."
    show monika happ om ce lpoint rhip
    show natsuki cm
    m "Я подумаю над таким предложением и озвучу своё решение завтра."
    show monika nerv mb oe ldown
    m "Наверное..."
    show monika cm
    show yuri ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_near_kokoro_noise fadein 3.0
    scene bg niigata kokoro entrance with wipeleft_scene
    "Что-то последние несколько минут мы провели в полной тишине...{w}так, стоп."
    mc "Мы уже пришли?"
    show natsuki turned black_shirt neut om oe at t11
    n "Ну да, это и есть {color=#fc7e23}KoKoRo{/color}."
    show natsuki cm b1d
    mc "Он больше смахивает на большую станцию, чем на торговый центр..."
    show natsuki om lhip rhip
    n "Потому что это его неосновной вход, дурень!"
    show natsuki ldown
    n "Мы пришли на угол."
    show natsuki cm
    mc "Ясно."
    show natsuki om -b1d
    n "Сама станция встроена с обратной стороны."
    show natsuki cm
    mc "Знаю."
    mc "Я же отсюда в Ниигату прибыл."
    show monika forward green_hoodie_long neut cm oe at t21
    show natsuki rdown at t22
    pause 0.2
    show monika om
    m "И где здесь находится игровой зал?"
    show natsuki curi om e1b
    show monika cm
    n "Где-то на третьем этаже..."
    show natsuki neut om oe
    n "О, вон там схема."
    n "Пойдём, посмотрим."
    show monika at thide
    hide monika
    show natsuki cm at thide
    hide natsuki
    pause 0.2
    "Как-то тут странно..."
    "Люди в основном ходят внизу, явно пользуются станцией, а в самом торговом центре практически никого."
    show natsuki turned black_shirt neut om oe lhip rhip at t11
    n "Люди, за мной!"
    show natsuki cm b1d
    k "Вы вообще на схему смотрели?"
    show natsuki om ldown rdown
    n "Да, уже всё прикинули, пошли!"
    show natsuki cm
    $ renpy.music.set_volume(0.2, 3, "noise_1")

    scene black with wipeleft_scene
    "Пока что тут ничего сверхпримечательного..."
    "Коридоры как коридоры."
    s "Ой, р-ребята..."
    m "Что случилось?"
    s "Где тут ближайший туалет?..."
    n "Ох, серьёзно?"
    y "Кажется, вон там, на первом этаже..."
    n "Блин, мы ещё спускаться будем..."
    k "Нацуки, не ной."
    k "Я бы тоже сходила."
    m "Хорошо, идёмте, пока есть возможность."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    $ renpy.music.set_volume(1.0, 0, "noise_1")
    scene bg niigata kokoro toilet with wipeleft_scene
    "Да уж, зов Сайори побудил сходить не только её, но и всю нашу группу, поскольку...{w}да что б потом не отвлекаться."
    "Так, всё, облегчились -- вышли."
    "Нечего время на мысли тратить."

    scene black with wipeleft_scene
    pause 0.5
    play sound building_door_open
    pause 1.0
    mc "Я вернулся."
    n "Ха, успешно?"
    mc "Аналогичный вопрос в твой адрес."
    n "Да иди ты, ха-ха-ха!"
    mc "К игровым автоматам?"
    mc "Так веди, давай."
    n "Ну так пошли, чего стоим?"
    "Надо будет потом найти место, куда можно будет присесть, когда они беситься будут."
    "Будет-будут-будет-будут, бу-бу-бу!"
    "Почему меня вечно заедает на одном слове?"
    n "А может, сократим путь?"
    m "Как?"
    n "Да вот, лифты."

    scene bg niigata kokoro f1 elevator
    show natsuki turned black_shirt happ cm oe rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Не будем мучиться, сразу поднимемся на третий этаж."
    show natsuki anno cm oe
    mc "Мы столько пешком прошли, а тут вдруг лень стало?"
    show natsuki om rdown
    n "Тебе так влом нажать на пару кнопочек и мгновенно очутиться на нужном этаже?"
    show natsuki cm
    mc "Даже спорить не хочу."
    show natsuki neut cm oe
    mc "Жми уже."
    show natsuki happ cm e1b
    call window_close

    scene black with dissolve
    pause 0.5
    play sound elevator_button_outside
    pause 0.5
    play sound elevator_mall_arrive
    pause 10.0

    call window_open
    n "Заходим!"

    scene bg niigata kokoro elevator inside with dissolve_cg
    pause 0.25
    mc "Аж матовый металл..."
    show sayori turned casual happ cm e1b at r54 zorder 3
    show kotonoha casual happ cm e1b at r55
    "Просторная и чистая кабина..."
    show monika forward green_hoodie_long happ cm oe at l53 zorder 2
    "И причём это неосновной лифт."
    show yuri turned windbreaker happ cm e1c at l52
    "У {color=#fc7e23}KoKoRo{/color} явно нет проблем с деньгами..."
    call window_close

    play sound elevator_button_inside
    show sayori oe
    show yuri oe
    pause 0.5
    play sound elevator_mall_door_close
    show kotonoha oe
    pause 1.0
    show natsuki turned black_shirt happ cm oe at l51 zorder 2
    pause 4.0
    play sound elevator_mall_move
    show natsuki e1b
    show yuri e1b
    show monika e1b
    show kotonoha e1c
    show sayori e1c
    pause 8.0
    show natsuki neut cm e1b
    show yuri neut cm e1c
    show monika e1c
    show kotonoha e1b
    pause 8.6
    show natsuki happ cm oe
    show yuri happ cm oe
    show monika oe
    show kotonoha oe
    show sayori oe
    pause 5.0
    show natsuki neut cm oe
    show yuri neut cm e1d
    show monika neut cm oe
    show kotonoha neut cm oe
    show sayori neut cm oe

    call window_open
    mc "...и?"
    play sound elevator_button_inside
    pause 1.0
    show natsuki curi cm oe
    show monika e2a
    show sayori curi cm oe
    mc "......"
    show monika om
    m "Макс, что не так?"
    play sound elevator_button_inside
    show monika cm
    pause 0.5
    play sound elevator_button_inside
    pause 1.0
    show yuri lsur cm oe
    mc "...ну мы приехали...{w}на третий этаж."
    show yuri om
    show sayori e1a
    y "Ты же не хочешь сказать, что мы..."
    play music literature_club_hellevator_incident fadein 3.0
    show natsuki pout cm e2a
    show yuri pani mj oe
    show monika lsur cm oe
    show kotonoha lsur cm oe
    show sayori shoc md oe
    mc "Да, мы сократили себе время прогулки, а не путь, который можно было пройти ногами!"
    show yuri cm
    mc "Дверь вообще не открывается!"
    show yuri om lup rup at h52
    y "КАК НЕ ОТКРЫВАЕТСЯ?!"
    show natsuki pani cm oe
    show yuri cm
    show sayori curi cm oe
    mc "Панель вся сдохла, кнопка вызова диспетчера тоже не работает."
    mc "Твою МАТЬ!" with vpunch
    show natsuki om
    n "Через что ещё тут можно выйти?!"
    show natsuki cm
    show monika doub om ce
    m "СТОП-СТОП-СТОП!"
    show natsuki pout cm e2a
    show yuri lsur cm oe
    show monika lsur om oe
    m "Успокойтесь!"
    show monika neut om ce
    show kotonoha neut cm oe
    show sayori neut cm oe
    m "Самое важное...{w}в критических ситуациях..."
    show natsuki oe
    show yuri ldown rdown
    show monika happ om oe lpoint
    show sayori happ cm oe
    m "...никогда не паниковать!"
    show yuri neut cm e1d
    show monika cm ldown
    show sayori om
    s "Да, Моника права!"
    show natsuki lsur cm oe
    show yuri e2a
    show monika neut cm e2a
    show kotonoha lsur cm oe
    show sayori ce
    s "Если мы будем волноваться, то начнём часто дышать, из-за чего весь кислород закончится и мы задохнёмся."
    show sayori cm
    kmny "......"
    show sayori neut cm oe
    mc "..."
    show natsuki pani cm oe
    show yuri pani cm oe
    show monika shoc cm oe
    show kotonoha sad cm oe
    show sayori pani om oe lup rup at h54
    s "ОКЕЙ, ВСЕ ДРУЖНО ПЕРЕСТАЁМ ДЫШАТЬ!!!"
    show natsuki ce
    show yuri ce
    show monika ce
    show kotonoha e4b
    show sayori vsur om ce ldown rdown
    s "ХА-А-А-А-А-А-А--{nw}"
    show sayori cm
    mc "САЙОРИ, ПРЕКРАТИ!" with vpunch
    show natsuki oe
    show yuri mj oe
    show monika mj oe
    show kotonoha oe
    show sayori e1a
    mc "Лифт не настольно герметичный, чтобы мы тут задохнулись!"
    show natsuki pout cm e2a
    show yuri lsur cm oe
    show monika lsur md oe
    show kotonoha neut cm oe
    show sayori curi cm e1a
    mc "К тому в каждой шахте есть вентиляция, которая постоянно работает!"
    show sayori om
    s "А, да?..."
    show natsuki shoc cm oe
    show yuri om e2b lup rup
    show kotonoha vsur cm oe
    show sayori neut cm oe
    y "М-мне попадалась одна новость, как женщина в другой стране застряла в лифте на целый месяц и умерла там от голода и обезвоживания..."
    show yuri cm
    show monika shoc om oe
    show kotonoha om e4b b2
    show sayori pani om ce
    kms "А-А-А-А-А!" with vpunch
    show yuri ce
    show monika cm
    show sayori cm
    k "Ужас!"
    show natsuki pout om ce
    show yuri neut cm e2a
    show kotonoha cm
    show sayori oe
    n "...выглядит всё так, будто мы должны кого-то убить, чтобы выжить..."
    show natsuki cm
    show monika om e4c
    show kotonoha oe
    show sayori ce
    m "НЕТ!"
    show natsuki pani cm oe
    show yuri shoc cm oe at s52
    show monika mj
    y "У-У-У!..."
    show natsuki om at h51
    show yuri mj
    show monika oe
    n "ЭЙ!"
    show natsuki ce
    show sayori oe
    n "Перестаньте часто дышать!"
    show natsuki cm
    show yuri at t52
    mc "ПРЕКРАТИТЕ ПАНИКУ!!!" with vpunch
    show yuri lsur cm oe ldown rdown
    show monika lsur md oe
    show sayori sad cm oe
    mc "Хватит!"
    show natsuki pout cm oe
    mc "Вы сами себя губите!"
    show monika neut cm oe
    show kotonoha neut cm oe -b2
    show sayori neut cm oe
    mc "Лучше проверьте, если ли здесь связь или Интернет."
    show yuri e2b
    mc "Нам нужно связаться с лифтёрами или хоть с кем-нибудь."
    show natsuki e1b
    show kotonoha e1b rhip
    show sayori curi cm oe
    window hide

    python in phone.system:
        internet_connection = False
        battery_level = 47
        clock = (11, 18)

    show screen phone() with Dissolve(0.5)
    $ plot_pause()

    window auto
    show sayori om
    s "...нету."
    show monika om
    show sayori cm
    m "Не ловит..."
    show monika cm
    y "...м-м-м..."
    show natsuki om
    n "Нет ничего!"
    show natsuki cm
    show kotonoha om
    k "Тоже."
    show kotonoha cm
    mc "И у меня..."
    window hide

    hide screen phone with Dissolve(0.5)

    $ phone.system.internet_connection = True

    window auto
    show natsuki pani cm oe
    show yuri neut cm e2a
    show monika e2a
    show kotonoha oe
    show sayori neut cm e2a
    mc "Хорошо, предлагаю первой убить Нацуки."
    show natsuki om
    n "А?!"
    show natsuki lhip rhip
    show sayori curi cm oe
    n "Сам панику разводишь!"
    show natsuki curi cm oe
    show yuri neut cm e1d
    show monika oe
    show sayori om
    s "Подождите, у меня появилась идея..."
    show natsuki ldown rdown
    show sayori cm
    mc "Что?"
    show natsuki om
    show sayori neut cm oe
    n "Только не говори мне, что ты хочешь кричать в дверь--{nw}"
    show natsuki cm
    show yuri e2a
    show monika e2a
    show kotonoha vsur cm oe
    show sayori happ om oe
    s "У нас нет иного выбора!"
    show sayori cm
    pause 0.1
    hide sayori with easeoutright
    show natsuki pani cm ce
    show yuri pani cm ce lup rup
    show monika pani cm e4c
    show kotonoha e4b b2 rdown
    s "{sc=5}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!{/sc}" with vpunch
    show monika oe
    s "{sc=3}ПОМОГИТЕ, МЫ ЗДЕСЬ ЗАСТРЯЛИ!!!{/sc}"
    show natsuki oe
    show yuri oe
    show monika om
    show kotonoha oe
    m "САЙОРИ, не ори так громко, ты просто тратишь силы!--{nw}"
    show natsuki ce
    show yuri ce
    show monika cm e4c
    show kotonoha e4b
    s "{sc=5}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!{/sc}" with vpunch
    s "{sc=3}ПОЖАЛУЙСТА, ПОМОГИТЕ, МЫ ЗАСТРЯЛИ!!!{/sc}"
    s "{sc=3}У НАС СЕМЬИ, МЫ ХОТИМ К НИМ ВЕРНУТЬСЯ!!!{/sc}"
    show monika oe
    s "{sc=2}А ЕЩЁ Я ХОЧУ ГУЛЯТЬ!!!{/sc}"
    s "{sc=2}И СЪЕСТЬ МУРИ-МУРИ-САН!!!{/sc}"
    show natsuki oe
    show monika mj
    show kotonoha oe
    s "{sc=1.5}У-у-у...{w}у-у-у!{/sc}"
    show natsuki pout cm oe
    show yuri oe
    show kotonoha sad cm oe -b2
    s "{sc=1.5}...пожалуйста!...{/sc}"
    show yuri mj
    show kotonoha om
    k "С-Сайори, не расстаривайся..."
    show natsuki neut cm oe
    show yuri neut cm e1d
    show monika neut cm oe b1c
    show kotonoha neut cm oe
    show sayori turned casual anno om e1b at r54
    s "Нэ-э-э, это не сработало."
    show yuri vang mj oe ldown rdown
    show kotonoha anno cm oe rhip
    show sayori cm
    k "..."
    show natsuki angr cm oe
    show yuri om
    show monika b1e
    show sayori doub cm oe
    y "...М-Моника уже тебе это сказала, прежде чем ты начала повторно РВАТЬ нам перепонки!"
    show yuri mj
    show sayori om
    s "Екскью-ю-юзьми, я стараюсь помочь вытащить нас всех отсюда!"
    show natsuki neut cm oe
    show yuri angr cm oe
    show monika -b1e
    show kotonoha neut cm oe
    show sayori neut cm oe
    mc "Не, тебе надо в актрисы идти..."
    show sayori happ cm oe
    mc "Тебя там с руками и ногами оторвут за такой талант."
    show sayori om ce lup rup at h54
    s "Хе-хе, я старалась!"
    show yuri neut cm e1d
    show kotonoha om
    show sayori cm ldown rdown
    k "С другой стороны, у нас реально нет выбора."
    show sayori oe
    k "Надо издавать шумы, чтобы на нас обратили внимание."
    show natsuki om
    show kotonoha cm
    n "Шум?"
    show natsuki cm
    pause 0.1
    show natsuki e1b
    hide natsuki with easeoutleft
    pause 0.1
    play sound elevator_door_knock
    show yuri pani cm oe lup rup at h52
    show monika lsur cm oe
    show kotonoha sad cm e4b
    show sayori flus om oe
    with vpunch
    pause 0.5
    show yuri om
    y "НАЦУКИ!"
    show yuri cm
    show monika om
    show kotonoha oe
    m "Не надо ломать кабину!"
    show natsuki turned black_shirt angr om oe lhip rhip at l51
    show yuri mj ldown rdown
    show monika cm
    show sayori anno cm oe
    n "Это всяко лучше, чем ОР!"
    show natsuki cm
    mc "Да успокойтесь вы уже в конце концов!"
    show natsuki neut cm e1d ldown rdown
    show yuri lsur cm oe
    show monika md
    show sayori neut cm oe
    mc "Хотя бы одну минуту тишины дайте!"
    show natsuki om
    n "Она тебе ничего не даст!"
    show natsuki pani cm oe
    show sayori flus cm oe
    mc "Я тебе сейчас по жопе дам, если ты не прекратишь!"
    show natsuki om ce at h51
    show yuri pani om ce
    show monika cm
    show kotonoha e4b
    n "{sc=3}А-А-А, НАСИЛИЕ!!!{/sc}" with vpunch
    show natsuki cm
    mc "Какое насилие?!"
    show natsuki oe
    show yuri oe
    show monika om
    show kotonoha oe
    show sayori happ cm oe
    m "Нацуки, тихо!"
    show natsuki pout cm oe
    show yuri mj
    show monika cm
    show kotonoha neut cm oe
    show sayori om rup
    s "У меня есть идея, как нам успокоиться и настроиться на позитивную волну!"
    show yuri vsur om ce
    show monika neut cm oe
    show sayori cm rdown
    y "...только без криков, прошу..."
    show yuri cm
    show monika om
    m "И что за идея?"
    show natsuki curi cm oe
    show yuri neut cm e1d
    show monika cm
    show sayori om ce lup rup at h54
    s "Шутки!"
    show sayori cm
    mc "...шутки?"
    show sayori om oe ldown rdown
    s "Про лифты."
    show kotonoha om
    show sayori cm
    k "Не думаю, что они сейчас уместны..."
    show kotonoha cm
    show sayori om lup
    s "Покупатель приехал в дом осматривать квартиру у продавца."
    show sayori ldown rup
    s "\"Хорошая у вас квартира. Только тесновата слегка...\" -- \"Да подождите, мы ещё из лифта не вышли!\""
    play sound joke
    show sayori cm rdown
    pause 2.0
    show natsuki anno cm oe
    "..."
    show yuri anno om oe
    y "Какой ужас..."
    show yuri cm
    show monika curi om oe
    m "Макс, кнопки точно не заработали?"
    show monika cm
    mc "Да, не надо их трогать."
    show yuri neut cm e1d
    show monika e1b
    show sayori om e2b
    s "Хорошо, как насчёт другой..."
    hide monika with easeoutleft
    show sayori ce
    s "Бизнесмен зашёл в лифт вместе со своим финансовым аналитиком и спросил: \"Скажи мне чётко: вверх или вниз?\""
    play sound joke
    show sayori cm
    pause 2.0
    show natsuki om ce
    show kotonoha e1b
    n "Я сейчас от стыда помру..."
    play sound elevator_button_inside
    show natsuki cm
    show kotonoha oe
    show sayori om e2a rup
    s "Два пьяных человека ползут по рельсам."
    play sound elevator_button_inside
    show natsuki oe
    show sayori lup rdown
    s "Один смотрит на них и говорит: \"Какая лестница длинная! И перилла широкие...\""
    play sound elevator_button_inside
    show sayori laug om ce ldown
    s "А другой отвечает: \"Да не парься, вон, лифт сверху спускается!\""
    play sound joke
    show sayori cm
    pause 2.0
    play noise_1 elevator_button_inside
    show yuri laug cm oe
    show kotonoha happ om ce
    k "Хи-хи..."
    show yuri lsur cm oe
    show kotonoha neut om oe
    show sayori happ cm oe
    k "Хи..."
    stop noise_1
    show kotonoha cm
    mc "...Моника, я же сказал не трогать!"
    m "Ха-ха, у меня просто просыпается клаустрофобия..."
    show yuri neut cm e1d
    show sayori om
    s "Заходит программист в лифт, а ему надо на 12-й этаж."
    show sayori ce
    s "Hажимает на \"1\", потом на \"2\", после чего лихорадочно ищет кнопку отправки."
    play sound joke
    show sayori cm
    pause 2.0
    play sound elevator_button_inside
    mc "..."
    play sound elevator_button_inside
    show natsuki vang mj oe
    show sayori om e2a rup
    s "На днях парфюмер популярной компании выпустил новый аромат, но остальные пассажиры лифта сделали вид, что этого не заметили."
    play sound joke
    show sayori cm rdown
    pause 0.4
    stop sound
    play noise_1 elevator_button_inside
    show natsuki om ce at h51
    show yuri doub cm oe
    show kotonoha anno cm oe
    show sayori neut cm oe
    n "Фу, Сайори, перестань, меня уже во всю воротит!"
    stop noise_1
    show natsuki oe
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "И Моника, хватит тыкать на кнопки!"
    show natsuki pani om ce at h51
    n "Я сейчас натурально сойду с ума!"
    show natsuki cm
    m "Я проверяю, работают ли кнопки в лифте!"
    show yuri anno cm oe
    mc "Моника, по-моему, у тебя просто паника."
    show natsuki pout cm e2a
    show kotonoha sad cm e1b
    m "Да, мне страшно!"
    show yuri om
    y "Я тоже начинаю сходить с ума..."
    show natsuki oe
    show yuri neut om e1d lup rup at h52
    show kotonoha neut cm oe
    y "Слушайте!"
    show natsuki curi cm oe
    show yuri ldown
    show kotonoha rdown
    show sayori curi cm oe
    y "У вас не осталась жевательная резинка?"
    show yuri anno om oe
    y "Она сейчас нужна как нельзя кстати."
    show natsuki neut cm oe
    show yuri neut cm e1d
    show sayori happ om ce lup rup at h54
    s "О-о-о, точно, жвачка!"
    show yuri rdown
    show sayori cm ldown rdown
    s "Хм-хм-хм..."
    show sayori lup gum with dissolve
    pause 0.5
    show yuri lsur cm oe
    show sayori curi om oe
    s "А, одна подушечка осталась..."
    show sayori cm
    "..."
    show kotonoha happ cm oe
    show sayori neut cm oe
    mc "Ты всю упаковку успела съесть?"
    show sayori om b1d
    s "Вкусно же!"
    show yuri om
    show sayori cm
    y "М-можно?"
    show yuri happ cm oe
    show sayori happ om ce rup -b1d at h54
    s "Конечно!"
    show sayori oe rdown
    s "На."
    show sayori cm at t42 zorder 3
    pause 0.5
    show natsuki curi cm oe
    show yuri shoc om e4b lup rup
    show kotonoha lsur cm oe
    show sayori ce ldown -gum
    y "Амф-ф-ф!" with vpunch
    show yuri cm
    show kotonoha om
    k "Сайори, аккуратнее!"
    show yuri oe
    show kotonoha cm
    show sayori at t54
    mc "Ты прямо на шарнирах..."
    show yuri md
    "Кажется, тут уже все, кроме Котонохи, с ума посходили."
    show kotonoha neut cm oe
    "Меня тоже начинает потихоньку крыть..."
    show natsuki pout cm oe
    show yuri lsur cm e1b
    show monika forward green_hoodie_long flus om ce at l53 zorder 4
    show sayori neut cm oe
    m "Что же нам делать?!"
    show natsuki neut cm oe
    show monika cm
    show kotonoha om e1b rhip
    k "Я бы вслушалась в звуки за дверью и позвала на помощь, если кто-то будет рядом..."
    show natsuki neut om oe lhip rhip
    show monika neut cm oe
    show kotonoha cm oe
    n "Прекрасно, слушай."
    show natsuki cm
    show yuri ce ldown rdown
    show kotonoha om
    k "А почему я сразу?"
    show natsuki cross black_shirt angr om oe
    show kotonoha cm
    n "Потому что я сосредоточиться на своих мыслях не могу, мне ПЛОХО!"
    show natsuki cm
    mc "Стойте на месте, я сам этим займусь."
    show natsuki neut cm oe

    scene black with dissolve
    pause 0.25
    "Чую я, что нам тут ещё торчать и торчать..."
    stop music fadeout 2.0
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    y "Ух, не думаю, что я больше хочу жевать эту...{w}жвачку..."
    n "Пускать её по кругу было отвратительной идеей..."
    "Меня сейчас тошнить начнёт от их слов..."
    s "Эй, жвачка -- всё ещё жевачка, верно?"
    s "Ам!"
    k "УМФ!..."
    m "Е-е-еу-у-у, Сайори!"
    y "Я больше никогда не буду жевать жвачки в своей жизни..."
    "Даже не хочу знать, в каком она была состоянии, что аж Котоноху пробрало..."
    m "Макс, там никого?"
    mc "Всё ещё тишина."
    n "Кажется, сюда больше никто не придёт, и мы все умрём..."
    k "Давай без натянутого пессимизма."
    n "Предлагаю нам перед торжественной гибелью поделиться одним из своих секретов."
    mc "Это что за клуб анонимных признаний?"
    n "Это вообще-то Литературный клуб!"
    s "Давайте я первая скажу!"
    s "Помните, у меня в спальне есть мистер Коровка и мистер Птиц?"
    k "Кто это?"
    mc "Большие плюшевые игрушки."
    k "А..."
    s "Так вот, я с ними иногда разговариваю..."
    n "Мы и так это знаем, Сайори."
    s "Откуда?!"
    n "Ты сама нам это сказала, когда пригласила первый раз в гости."
    s "А-а-а..."
    k "Хе-хе-хе..."
    k "Давайте я следующая."
    k "Один из моих секретов заключается в том, что...{w}я очень ненавижу мистику и всякую жуть."
    n "Мы это тоже знаем."
    k "Только ты и Юри."
    s "Я тоже не сторонница подобного..."
    n "М-м, что-то у вас жидко всё выходит..."
    n "Следующая я."
    n "Знаете, почему я переехала с семьёй в Ниигату?"
    "Опа..."
    n "Потому что мой папа, когда был полицейским, попал на вызов, где один человек устроил...{w}драку в Акихабаре, куда вызвали целых 17 скорых."
    n "И при этом некоторые люди погибли."
    s "ОХ!"
    m "Ничего себе..."
    k "Я же говорила, что не люблю жуть!"
    n "Ой, ну простите, наша ранимость!"
    k "Фи..."
    "Драка...{w}17 скорых?"
    "Надо будет узнать поподробнее..."
    y "Давайте я дальше..."
    y "Но я хотела бы сказать 2 секрета."
    n "Не томи!"
    y "Первый...{w}помните моё признание с руками?"
    y "Я заглушала переживания по одному болезненному для меня событию, про которое боюсь рассказать кому-то из не очень близких людей..."
    y "Но поскольку я с вами сроднилась, то всё-таки расскажу о нём..."
    y "Мой папа погиб в авиакатастрофе, когда он возвращался из Филиппин."
    y "Тогда мне было 13 лет."
    y "Я до сих пор не могу подавить в себе переживания по этому поводу..."
    s "И ты держала это в себе всё проведённое с нами время?!"
    y "...да..."
    s "Юри, мы же с тобой!"
    s "Не надо ничего скрывать!"
    m "Д-да, мы тебя всегда поддержим!"
    m "Такое нельзя скрывать, иначе оно накопится в нечто негативное..."
    m "Обращайся к нам за помощью, если она нужна, хорошо?"
    k "Юри..."
    k "Никогда бы не подумала, что с тобой стряслось нечто подобное..."
    y "Ох..."
    s "О, обнимашки!"
    "...неужели Юри стала расти над собой, раз решилась на такой шаг?"
    "Выходит, я на неё по-настоящему повлиял..."
    y "...спасибо...{w}за то, что вы есть..."
    s "Кстати, почему Макс и Нацуки такие неудивлённые?"
    mc "А?"
    n "А?"
    y "У-У-У МЕНЯ остался второй секрет, более безобидный..."
    s "Эй!"
    n "...это был секрет Юри, а я с ней давно дружу, в отличие от всех вас!"
    n "Что тут говорить?"
    s "Тогда откуда Макс его узнал?!"
    y "...я-я-я....{w}э-э-э..."
    mc "Да мы просто совместный стих составляли, а потом как-то разговорились и вот...{w}вышли на это..."
    s "А-а-а..."
    "ФУХ, спас Юри от недопонимания остальных."
    s "И ты молчал!"
    n "САЙОРИ, секрет!"
    n "ЛИЧНЫЙ."
    n "И сегодня Юри захотела его раскрыть!"
    y "В-в-всё, давайте о более п-позитивных вещах поговорим..."
    s "...ладно, просто мы же всегда поддержим и поможем, о таком молчать не надо..."
    y "Д-д-да!"
    y "Э-э, п-помните «Портрет {color=#407fff}Маркова{/color}», на котором я так сильно концентрируюсь?"
    n "Да ты каждый раз в него с головой проваливаешься..."
    y "Так вот, в этой книге нет чего-то особенного."
    y "Просто она интересная, чем мне и понравилась..."
    mc "Забавно..."
    m "Да уж, хах..."
    m "Ну что, моя очередь?"
    s "Угусь!"
    m "Мой секрет заключается в том, что у меня...{w}есть парень!"
    kny "{sc=3}ЧТО?!{/sc}"
    "...это и есть то самое аккуратное подталкивание Юри к «страшной» правде?"
    s "Ничего себе!"
    s "Кто же это?!"
    "Подождите, а когда Сайори нам стала подыгрывать?"
    "Или она сама догадалась не шокировать Юри?"
    m "А это уже второй секрет~"
    m "Но обещаю, что в будущем вы все всё узнаете."
    n "А если к этому времени ты этого парня отошьёшь?"
    m "Ну...{w}тогда не узнаете!"
    n "А то не помню, чтобы у тебя хоть кто-то был."
    y "Согласна, Моника должна пользоваться популярностью среди парней..."
    m "Было несколько...{w}смельчаков до моего переезда, но...{w}в общем, надеюсь, они извлекли пользу из своего горького опыта, благодаря чему найдут свои половинки..."
    k "Позитивненько..."
    n "Я уже хотела пошутить, что ты их убила."
    m "Ха-ха..."
    s "Эх, вот бы нам пригласить побольше парней!"
    n "Чтобы у вас начался гормональный дисбаланс?!"
    n "Нам уже хватило того конфликта неделю назад."
    n "А теперь представь, что он умножится в несколько раз."
    y "Нацуки, не будь такой радикальной!"
    y "С чего ты решила, что мы не научимся себя контролировать?"
    n "...не обязательно мы себя."
    n "А вот, например...{w}они себя."
    n "Кто знает, что там у них в голове?"
    s "А мы знаем!"
    s "Макс!"
    mc "А."
    s "Твоя очередь говорить секрет."

    scene bg niigata kokoro elevator inside
    show natsuki turned black_shirt neut cm oe at i51 zorder 2
    show yuri turned windbreaker happ cm oe at i52
    show monika forward green_hoodie_long happ cm oe at i53 zorder 3
    show sayori turned casual happ cm oe at i54 zorder 2
    show kotonoha casual happ cm oe rhip at i55
    with dissolve
    pause 0.25
    show natsuki anno cm oe
    mc "И какой секрет я должен сказать?"
    show sayori om
    s "Любой про себя."
    show sayori rup
    s "Заодно мы все узнаем, что у тебя в голове."
    show sayori cm rdown
    mc "...это прозвучало угрожающе."
    show natsuki neut cm oe
    mc "Так..."
    "..."
    show yuri neut cm e1d
    "И что мне такого сказать?"
    show natsuki curi cm oe
    "..."
    "О, знаю..."
    show natsuki neut cm e2a
    show yuri e2a
    show monika neut cm oe
    show sayori neut cm oe
    show kotonoha neut cm oe
    mc "В моей кровати спрятана железная телескопическая дубинка."
    show sayori curi cm oe
    show kotonoha rdown
    kmnsy "......"
    mc "Что?"
    show sayori neut cm oe
    mc "Правда же."
    show yuri neut cm e1d
    play sound elevator_button_outside volume 0.1
    pause 1.0
    show natsuki curi cm oe
    show yuri lsur cm oe
    show monika e2a
    show sayori lsur om oe lup rup at h54
    s "Кнопка снаружи!"
    show natsuki om lhip rhip
    show sayori me ldown rdown
    show kotonoha vsur cm oe
    n "Кнопка?!"
    show natsuki cm
    show kotonoha om
    k "Кнопка?!"
    show kotonoha cm
    mc "Тихо!"
    show monika oe
    show sayori neut cm oe
    $ koh_name = "???"

    scene black with dissolve
    pause 0.25
    koh "{size=15}Ну и что с этим дурацким лифтом?{/size}"
    mc "ЛЮДИ!!!"
    mc "Помогите, мы застряли!"
    koh "{size=15}...а-а?{/size}"
    mc "Вызовите персонал или диспетчера!"
    koh "{size=15}Стоп...{/size}"
    koh "{size=19}Вы как там застряли?{/size}"
    mc "Откуда я знаю?!"
    mc "Приехали на третий этаж, двери не открылись."
    mc "Кнопки перестали работать."
    mc "Мы ничего не можем сделать!"
    koh "{size=19}Я даже не знаю, кого именно позвать.{/size}"
    n "ДА КОГО-НИБУДЬ, ПОМОГИТЕ НАМ УЖЕ!!!" with vpunch
    koh "{size=19}Подожди-ка...{/size}"
    koh "{size=19}НАЦУКИ?!{/size}"
    $ koh_name = _("Кохаку")
    n "КОХАКУ?!"
    mc "О-о-о..."
    "Это какая-то ирония свыше?"
    koh "{size=19}Вот это уморительно!{/size}"
    m "НИЧЕГО СМЕШНОГО!" with vpunch
    koh "{size=19}И МОНИКА?!{/size}"
    koh "{size=19}Вы там всем клубом застряли?!{/size}"
    n "Какая разница?!"
    n "Позови кого-нибудь на помощь!"
    koh "{size=19}А с хрена ли я должна вам помогать?{/size}"
    koh "{size=15}К тому же не каждый день Литературный клуб застревает в лифтах...{/size}"
    mc "Ну ты и сволочь!"
    mc "Это ж надо быть такой мразью..."
    koh "{size=19}Заткни свой рот!{/size}"
    koh "{size=19}Вы все мне всё изгадили!{/size}"
    koh "{size=19}Вы все мне вечно мешаете!{/size}"
    koh "{size=19}Почему бы вам не прочувствовать хотя бы чуть-чуть того, что чувствую я?!{/size}"
    mc "Запах металла и повышенную температуру?"
    koh "{size=19}Вы там сидите ОДНИ!{/size}"
    koh "{size=19}Всем на вас сейчас глубоко плевать!{/size}"
    koh "{size=19}Вам тут никто не поможет!{/size}"
    koh "{size=19}И вам не вырваться из этого лифта, что бы вы ни делали!{/size}"
    koh "{size=15}Разве что дождаться обхода охраны ночью...{/size}"
    mc "Ой, дай угадаю: у тебя проблемы с родителями?"
    mc "Не ценят тебя, там...{w}а ты усердно стараешься, из кожи вон лезешь, чтобы доказать свою ценность."
    koh "{size=19}ПХ-Х?!{/size}"
    "Это было слишком очевидно."
    mc "Тогда смысл держать нас взаперти, если ты с этого ничего не получишь?"
    koh "{size=19}Не получу?!{/size}"
    koh "{size=19}Ещё как получу!{/size}"
    koh "{size=19}Я получу удовлетворение!{/size}"
    koh "{size=19}Удовлетворение от мести!{/size}"
    n "{sc=3}ИМЕННО ПОЭТОМУ Я ТЕБЕ НИЧЕГО НЕ ДАМ!{/sc}" with vpunch
    n "Ты просто сгнила!"
    n "В попытке что-то там кому-то доказать, ты постоянно преследовала свой эгоизм!"
    n "ИМЕННО ТЕБЕ было плевать на остальных в Клубе выпечки!"
    n "ИМЕННО ТЕБЕ было плевать на меня!"
    n "ИМЕННО ТЫ была источником всего негатива и грязи из-за своего грубого характера и тупых мозгов!"
    n "И всё это время тебе были нужны только эти дурацкие кексы ради призрачного признания твоих родителей?!"
    n "{sc=3}ТЫ ПРОСТО ЖАЛКОЕ И ГНИЛОЕ СУЩЕСТВО,\nНЕСПОСОБНОЕ УЧИТЬСЯ НА СВОИХ ОШИБКАХ!!!{/sc}" with vpunch
    n "{sc=4}И ИЗ-ЗА СВОЕЙ ГНИЛОСТИ ТЫ ТЕПЕРЬ ГАДИШЬ НА\nВСЕХ И ВСЯ, МЕШАЯ ВСЕМ НОРМАЛЬНО ЖИТЬ!!!{/sc}"
    n "{sc=5}УЙДИ ОТ МЕНЯ И МОЕГО КЛУБА!!!{/sc}"
    if persistent.censorship:
        n "{sc=5}ТЫ ВСЁ РАВНО НАМ НЕ ПОМОЖЕШЬ, ПОТОМУ ЧТО\nВСЯ ИЗДЕРЬМИЛАСЬ!{/sc}"
        n "{sc=6}ПОШЛА НАХРЕН ОТСЮДА!!!{/sc}"
    else:
        n "{sc=5}ТЫ ВСЁ РАВНО НАМ НЕ ПОМОЖЕШЬ, ПОТОМУ ЧТО\nВСЯ ИЗГОВНИЛАСЬ!{/sc}"
        n "{sc=6}ПОШЛА НАХЕР ОТСЮДА!!!{/sc}"
    "......"
    "............"
    "...ну ничего себе..."
    if persistent.censorship:
        koh "{size=19}...это вы...{w}вы меня издерьмили...{w}вы меня обили грязью...{/size}"
    else:
        koh "{size=19}...это вы...{w}вы меня изговнили...{w}вы меня обили грязью...{/size}"
    koh "{size=19}...я вас всех...{w}я вас всех ненавижу...{w}ВСЕХ!!!{/size}"
    play sound elevator_door_knock
    with vpunch
    pause 2.0
    "..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg niigata kokoro elevator inside
    show natsuki turned black_shirt neut cm e1b b1d at i51 zorder 2
    show yuri turned windbreaker anno cm oe at i52
    show monika forward green_hoodie_long dist cm oe at i53 zorder 3
    show sayori turned casual neut cm e2c at i54 zorder 2
    show kotonoha casual neut cm e1c rhip at i55
    with wiperight
    pause 0.25
    "Сколько мы так уже в тишине простояли?"
    "Минут 10?"
    "И всё ещё от криков отойти не можем."
    "Но зато вся паника улетучилась, ни у кого ничего не свербит."
    play sound elevator_mall_door_open
    show natsuki oe -b1d
    show yuri neut cm e1d
    show monika neut cm oe
    show sayori oe
    show kotonoha oe
    pause 2.0
    show natsuki e2a
    show yuri cry mc e1g lup rup
    show monika happ cm oe
    show sayori happ cm oe
    show kotonoha happ cm oe
    y "Ах, мы свободны!"
    show natsuki pani mc ce at lhide
    hide natsuki
    show yuri ma
    show kotonoha b2
    n "{sc=3}СВОБО-О-ОДА-А-А-А-А-А-А-А-А-А!!!{/sc}"
    show monika ce
    show sayori laug om ce lup rup at lhide
    hide sayori
    show kotonoha ce
    s "{sc=3}ВПЕРЁД!!!{/sc}"
    show yuri e4d

    scene black with wipeleft_scene
    pause 0.25
    k "Фу-у-у, какой тут свежий воздух..."
    sta_mall "От лица торгового центра мы приносим вам искренние извинения за столь долгое ожидание..."
    sta_mall "Вам не нужна какая-либо помощь?"
    m "Н-не стоит, с нами всё в порядке."
    mc "Но как вы смогли узнать, что мы здесь застряли?"
    mc "У нас полностью перестали работать кнопки, мы не смогли вызвать диспетчера."
    sta_mall "Одна из посетительниц сообщила нашей сотруднице о проблеме с данным лифтом."
    sta_mall "При этом она указала, что в нём застряло минимум 3 человека."
    mc "А, ага..."
    "...я в полнейшем замешательстве."
    y "Р-ребята, давайте уже пойдём отсюда..."
    y "Я очень соскучилась по лестницам и эскалаторам..."
    sta_mall "Не смею вас больше задерживать."
    sta_mall "Ещё раз примите наши извинения."
    sta_mall "Поломки лифтов у нас случаются крайне редко."
    m "Всё отлично, спасибо, мы пойдём."
    call window_close

    call plot_transition

    call window_open
    play noise_1 mall_noise fadein 3.0
    scene bg niigata kokoro f1 corridor
    show natsuki turned black_shirt neut cm oe b1d at t31 zorder 2
    show monika forward green_hoodie_long neut cm oe at t32 zorder 3
    show kotonoha casual neut cm oe at t33 zorder 2
    with wipeleft_scene
    show natsuki om lhip rhip
    n "Ох, ну и сколько они ещё в этом туалете торчать будут?"
    show natsuki cm
    show kotonoha om e1b rhip
    k "Нацуки, ты сама инициировала потерю времени, так что не гунди."
    show natsuki anno cm ce -b1d
    show kotonoha cm
    n "Ф-ф-ф..."
    show natsuki at t51
    show monika at t52
    show kotonoha oe at t53
    show yuri turned windbreaker happ cm oe at t54
    show sayori turned casual happ cm oe at t55 zorder 2
    pause 0.2
    show natsuki neut cm oe
    show monika happ cm oe
    show kotonoha happ cm oe rdown
    show sayori om ce
    s "Мы снова тут!"
    show natsuki ldown rdown
    show monika om
    show sayori cm
    m "Юри, стало легче?"
    show yuri om
    show monika cm
    show sayori oe
    y "Да, стоило только освежиться водой, как голова сразу пришла в норму."
    show yuri neut om e1b
    y "Всё-таки мне стало нехорошо от духоты..."
    show yuri happ cm oe
    show monika om ce
    show kotonoha ce
    m "Как бы то ни было, отлично!"
    show monika oe lpoint
    show sayori e1b
    show kotonoha oe
    m "Так что, идём к игровым автоматам, или у вас появились другие идеи?"
    show natsuki anno cm oe
    show yuri neut cm e1d
    show monika cm ldown
    show sayori neut cm e1b
    mc "Честно говоря, мне уже приключений за глаза хватило."
    show natsuki neut cm oe
    show yuri happ cm oe
    show sayori at thide
    hide sayori
    mc "Но мы уже такой путь проделали, что было бы глупо вот так взять и уйти."
    show natsuki om
    n "Давайте уже просто дойдём до цели нашей прогулки."
    show natsuki curi om oe
    show yuri neut cm e1d
    show monika neut cm oe
    show kotonoha neut cm oe
    n "Эй..."
    show natsuki rhip
    show yuri e2a
    show monika lsur cm oe
    show kotonoha lsur cm oe
    n "Где Сайори?"
    show natsuki cm
    show monika e1b
    mc "В смысле?"
    show natsuki neut cm oe
    show yuri e1d
    show monika om e2b
    show kotonoha neut cm oe
    m "Вон она, у магазина!"
    show monika cm

    play sound magic
    scene bg niigata kokoro shop food
    show sayori turned casual happ cm e1b at i11
    with dissolve_cg
    show sayori om
    s "Можно я куплю себе что-нибудь поесть?"
    show sayori cm
    mc "ЧЕГО?!" with vpunch
    mc "Ты когда проголодаться успела?!"

    play sound magic
    scene bg niigata kokoro shop clother
    show monika forward green_hoodie_long happ cm e1b at i21
    show kotonoha casual happ cm e1c at i22
    with dissolve_cg
    show monika om
    m "Ух ты, тут интересный выбор!"
    show monika cm
    show kotonoha ce
    k "Угу!"
    show monika om ce at thide
    hide monika
    show kotonoha at thide
    hide kotonoha
    m "Котоноха, как тебе вот эта блузка?"
    k "Хм-м-м..."
    mc "Ну вы-то куда?!"

    play sound magic
    scene bg niigata kokoro shop book
    show yuri turned windbreaker happ cm e1b at i11
    with dissolve_cg
    show yuri om
    y "Магазин книг..."
    show yuri ce lup rup
    y "Я не могу упустить шанс просмотра его ассортимента."
    show yuri cm
    mc "......"

    play sound magic
    scene bg niigata kokoro f1 corridor
    show natsuki turned black_shirt sad cm ce at i11
    with dissolve_cg
    show natsuki mh at s11
    mcn "О-о-о-о-о..."
    show natsuki cm
    mc "Может, ну их всех?"
    show natsuki doub cm oe at t11
    mc "Так сходим?"
    show natsuki om lhip rhip
    n "Ага, щас."
    show natsuki cm
    mc "Это была шутка."
    show natsuki sad om oe rdown
    n "Блин, точно..."
    show natsuki cm
    mc "Что?"
    show natsuki neut om oe ldown
    n "Уже 2 недели прошло, мне завтра надо будет проведать маму."
    show natsuki cm
    mc "Хм."
    show natsuki worr om oe
    n "Знаешь, это...{w}ходить до госпиталя одной как-то...{w}всегда боязно..."
    n "...несмотря на то, что я делала это кучу раз..."
    show natsuki neut cm oe b1d
    mc "Ты хочешь, чтобы я тебя за ручку сопроводил?"
    show natsuki om
    n "Я не настолько беспомощная."
    show natsuki -b1d
    n "Короче, не хочешь сходить со мной?"
    show natsuki cm b1d
    mc "Прямо до палаты?"
    show natsuki om rhip
    n "Кто ж тебя туда пустит?"
    show natsuki -b1d
    n "Останешься в зале ожидания и всё."
    show natsuki cm
    mc "М-м-м..."
    show natsuki curi cm oe
    mc "А другие?"
    mc "Разве тебе никто компанию не составляет?"
    show natsuki sad om oe
    n "Составляли, но это было раньше..."
    n "И вообще, я не думаю, что в случае опасности они...{w}смогут со всем справиться."
    show natsuki pout cm oe
    mc "То есть рассекать улицы нашего района -- это завсегда, а как сразу за него выходишь -- страшно."
    show natsuki om ce
    n "Вот ты не веришь, а мне позапрошлой зимой реально один поехавший дядька в поезде попался."
    show natsuki oe
    n "Постоянно оглядывался в мою сторону из другого конца вагона, а как только я его замечала, сразу делал вид, что не смотрит."
    n "А потом ещё вышел вместе со мной на станцию и начал издалека преследовать!"
    show natsuki neut om b1d
    n "Хорошо я тогда к работникам станции обратилась, они полицейских вызвали."
    n "Только этот засранец-сталкер быстро смылся."
    show natsuki mb e1b
    n "Но я хорошо разглядела его приметы, всё им в подробностях рассказала."
    show natsuki om oe -b1d
    n "Только не знаю, поймали его, не поймали..."
    show natsuki e1b
    n "Надеюсь, что поймали."
    show natsuki oe b1d lhip
    n "А теперь представь, сколько таких ещё шляется в людных местах?"
    show natsuki -b1d
    n "Мне каждой раз страшно одной появляться где угодно вдали от дома, поэтому по возможности прошу кого-нибудь составить мне компанию."
    n "В основном Юри, но иногда и других."
    show natsuki dist om oe ldown
    n "Но в последнее время все заняты, приходится одной кататься."
    n "И пока ничего плохого не случилось...{w}к счастью."
    show natsuki cm
    mc "Мда уж..."
    "Что-то у Нацуки всё в жизни ни к чёрту."
    show natsuki neut cm oe
    "У неё случалось хоть что-то приятное, кроме манги и кексов?"
    show natsuki curi om oe
    n "Ну так что?"
    show natsuki cm
    mc "Думаю-думаю, сейчас..."
    "Так-с, сопровождение до госпиталя, который я ещё вживую не видел..."
    show natsuki neut cm oe
    "Конечно, хотелось бы организовать нормальное свидание с Моникой, но у неё же родители будут..."
    show natsuki rdown
    "А больше я ничего не планировал."
    "Домашнее задание целиком сделал, никаких других дел не ожидается."
    show natsuki happ cm oe
    mc "Лады, прогуляюсь с тобой до госпиталя."
    show natsuki neut cm oe
    mc "Ты там долго бываешь?"
    show natsuki om
    n "Неа."
    show natsuki e1b
    n "Полчаса где-то, ну час максимум."
    show natsuki cm
    mc "Прекрасно."
    "Кстати, вот тогда завтра можно будет расспросить её поподробнее про ситуацию с отцом."
    show natsuki oe
    mc "Всё, пошли, заберём их уже."
    show natsuki happ cm oe
    mc "А то мы с таким успехом до ночи здесь просидим."
    show natsuki cross black_shirt laug om ce
    n "Ха, после Вас!"
    show natsuki ma
    mc "Как культурно с Вашей стороны, а?"
    $ renpy.music.set_volume(0.2, 2, "noise_1")
    call window_close

    call plot_transition

    call window_open
    scene bg niigata kokoro arcade with wipeleft_scene
    mc "Уф-ф-ф..."
    "Как же приятно сидеть со спокойной душой, пока они там бесятся и развлекаются."
    "Надеюсь, они не спустят тут много денег."
    "В среднем за одну игру автоматы требуют монету в 100 иен."
    "Дёшево, конечно, но мы-то обычные школьники, у которых и зарплаты нет."
    "Даже Моника на обеспечении родителей, хотя она богаче нас вместе взятых..."
    "..."
    "Может, тоже сыграть здесь во что-нибудь..."
    "Не, ну а что?"
    "Да, я подзамотался, но не просиживать же свою задницу на одном месте, верно?"
    "Иначе зачем мы сюда так пёрлись и сидели в застрявшем лифте?"
    "Только надо как-то всё купленное клубом добро рядом с собой положить..."
    "Накупили, блин, всякой всячины и удрали развлекаться."
    "А я теперь ни на метр отойти не могу."
    "..."
    "Хотя..."
    "Можно попробовать этот автомат передо мной."
    "И вещи не придётся перекладывать."
    mc "Ладно, решено."
    "Итак, это...{w}{color=#fc7e23}TetroMania{/color}?"
    mc "Тетрис?"
    mc "Серьёзно?"
    "Ничего против не имею, но не слишком ли примитивная игра для аркадных автоматов?"
    mc "Хм..."
    "..."
    "Да идите вы со своей примитивностью, тетрис -- это классика."
    "Сколько он там стоит..."
    "..."
    mc "100 иен за весь сеанс..."
    "...даже не за раунд?"
    mc "Фига се..."
    mc "Что ж, испытаем этот агрегат."
    stop noise_1 fadeout 3.0
    call window_close
    call skip_block_on

    scene black with dissolve_scene_full
    python:
        renpy.call_screen('tetris_game_guide')
        while True:
            tetris_game_object = tetris.Game()
            renpy.music.play(tetris.sfx_round, "music")
            tetris_quit = renpy.call_screen("tetris_game", tetris_game_object)
            renpy.music.stop(channel = "music")
            if not tetris_quit:
                break

    call skip_block_off
    call window_open
    "Фух, наигрался..."
    "Да, оказалось не так интересно, как я думал..."
    mc "Дурь какая-то..."
    s "Да ты чего, классно же отжигал!"
    mc "А?!" with vpunch

    $ renpy.music.set_volume(0.2, 0, "noise_1")
    play noise_1 mall_noise fadein 0.25

    scene bg niigata kokoro arcade
    show sayori turned casual laug cm ce at t31
    show monika forward green_hoodie_long laug cm ce at t32 zorder 2
    show kotonoha casual happ cm ce rhip at t33
    with dissolve
    pause 0.25
    show monika mb
    m "Не то слово!"
    show monika oe
    m "Я бы так не смогла."
    show monika cm
    show kotonoha om
    k "Хи-хи!"
    show sayori ma
    show kotonoha cm
    mc "И как долго вы здесь?"
    show sayori happ cm oe
    show monika happ cm oe
    show kotonoha om oe rdown
    k "Мы с Моникой подошли где-то к началу твоего последнего раунда."
    show sayori om
    show kotonoha cm
    s "А я чуть позже, потому что уже наигралась."
    show sayori cm
    mc "Так быстро?"
    mc "От силы полчаса прошло."
    show sayori nerv cm oe
    show monika nerv mb oe
    show kotonoha nerv cm oe rhip
    m "Вообще-то полтора часа..."
    show monika cm
    mc "Полтора?!"
    show sayori happ om ce
    s "Вот-вот!"
    show sayori lsur om oe
    show monika laug cm oe
    show kotonoha happ cm oe
    s "У меня уже глаза в кучке от моря света и звуков!"
    show sayori me
    show monika mb ce
    m "Кто бы сомневался, ха-ха!"
    show sayori laug cm ce
    show monika oe lpoint
    m "Ты чуть ли не каждый автомат хотела попробовать."
    show sayori ma
    show monika cm ldown
    mc "Так это, Моника..."
    show sayori happ cm oe
    show monika happ om oe
    m "Ась?"
    show sayori neut cm oe
    show monika cm
    show kotonoha neut cm oe
    mc "Не пора ли нам «пора»?"
    show monika neut cm oe
    m "?..."
    show sayori flus om oe
    show monika om
    m "А-а-а..."
    show kotonoha om
    k "Мы куда-то спешим?"
    show sayori cm
    show monika mh lpoint rhip
    show kotonoha cm
    m "Вообще-то да, я, по-моему, только Сайори про это говорила..."
    show sayori neut cm oe
    show monika ldown
    m "Подождите, давайте все соберёмся."
    show sayori happ cm oe
    show monika b1f
    m "Где Юри и Нацуки?"
    show sayori om rup
    show monika cm
    s "Они там из пистолетов стреляли."
    show sayori cm rdown
    show monika e1b at thide
    hide monika
    mc "Что, серьёзно?"
    show kotonoha happ cm oe
    mc "Их унесло в парный шутер?"
    show sayori om
    s "А почему нет?"
    show sayori om ce lup rup at h31
    s "Весело же!"
    show sayori cm
    mc "Это просто звучит немного абсурдно."
    show sayori oe ldown rdown at t51
    show natsuki turned black_shirt sad cm oe at t52 zorder 4
    show monika forward green_hoodie_long happ cm oe at t53 zorder 3
    show yuri turned windbreaker happ cm oe at t54
    show kotonoha at t55 zorder 2
    pause 0.2
    show monika om lpoint rhip
    show kotonoha ce
    m "Отлично, теперь все в сборе!"
    show natsuki om
    show monika cm ldown
    show yuri neut cm e1d
    n "Э-эх, доиграть не дали..."
    show natsuki anno om oe lhip rhip
    show yuri anno cm oe
    show kotonoha oe
    n "Мы только до финального уровня дошли!"
    show natsuki cm
    show yuri om
    y "Мы бы его всё равно не смогли пройти."
    show natsuki angr cm oe
    y "У моего персонажа осталось мало здоровья."
    show sayori neut cm oe
    show natsuki cross black_shirt angr om oe
    show monika neut cm oe
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "Потому что надо живее на всё реагировать, Юри!"
    show sayori curi cm oe
    show natsuki curi om oe
    n "Вот если бы на тебя лезло сразу 10 человек, желающие тебя укусить, то ты бы быстро что-нибудь предприняла для обороны, верно?"
    show natsuki cm
    show monika b1c
    show yuri anno om oe
    show kotonoha nerv cm oe
    y "Начнём с того, что такое бы никогда не случилось..."
    show sayori neut cm oe
    show monika mh
    show yuri cm
    m "Ребята, эй."
    show natsuki turned black_shirt neut cm oe
    show monika -b1c rdown
    show yuri neut cm e1d
    show kotonoha neut cm oe
    m "Послушайте меня."
    show monika lpoint
    show kotonoha rdown
    m "Мне вчера звонили родители, и они сказали, что приедут сегодня вечером."
    show monika happ om oe ldown
    m "Поэтому желательно к 18 часам я должна быть дома."
    show monika neut cm oe
    show yuri om
    y "Мы уже уходим?"
    show monika dist om oe
    show kotonoha sad cm oe
    show natsuki angr cm oe
    show yuri cm
    m "К сожалению..."
    show monika cm
    show natsuki om ce lhip rhip
    n "Ой, да ну вас нафиг!"
    show monika neut cm oe
    show kotonoha neut cm oe
    show natsuki oe
    n "Мы сюда тащились целую вечность ради того, чтобы поиграть тут от силы часик?"
    show kotonoha om e1c
    show natsuki cm
    k "Полтора часика..."
    show monika om
    show kotonoha cm
    m "Мы можем прийти сюда и в следующие выходные."
    show sayori happ cm oe
    show monika happ om oe
    show kotonoha happ cm oe
    show natsuki anno cm oe
    show yuri happ cm oe
    m "Нам же никто не запрещает так сделать, верно?"
    show monika cm
    show natsuki cross black_shirt anno om ce
    n "Эх, чёрт с вами..."
    show natsuki cm
    "Кажется, в Нацуки есть игровой азарт...{w}зачем мне эта информация?"
    show monika om rhip
    show natsuki e1b b1d
    m "Так что, друзья, все довольны сегодняшним днём?"
    show sayori om ce lup rup at h51
    show monika cm
    show kotonoha om ce
    show natsuki om
    show yuri om ce
    knsy "Да-а-а!"
    show sayori cm
    show kotonoha cm
    show natsuki cm
    show yuri cm
    mc "Да-а-а?..."
    show sayori oe ldown rdown
    show kotonoha oe
    mc "Лифт, конечно, немного всё испортил, но в целом..."
    show monika om rdown
    show yuri oe
    m "Потрясающе, надеюсь, мы в будущем не раз организуем подобный отдых."
    show sayori ce
    show monika om ce lpoint
    m "А теперь все дружно возвращаемся домой!"
    show monika cm ldown
    show kotonoha ce
    show yuri ce
    "...я даже договорить не успел."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    $ renpy.music.set_volume(1.0, 0, "noise_1")

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 evening
    show sayori turned casual happ cm oe at t51
    show monika forward green_hoodie_long happ cm oe at t52 zorder 3
    show natsuki turned black_shirt nerv cm ce at t53 zorder 4
    show yuri turned windbreaker dist cm oe at t54 zorder 2
    show kotonoha casual happ cm oe at t55
    with wipeleft_scene
    show natsuki om
    n "Допёрлись, ура-а-а..."
    show natsuki cm
    show kotonoha neut om e1b rhip
    k "А кто-то очень не хотел возвращаться..."
    show natsuki neut om oe b1d lhip rhip
    show kotonoha happ cm e1b
    n "Ничего не знаю!"
    show sayori neut cm oe
    show monika neut cm oe
    show natsuki sad om oe -b1d ldown rdown
    show kotonoha oe
    n "Я просто что-то вымоталась..."
    show natsuki cm
    show yuri om
    y "Соглашусь, у меня ноги начали подкашиваться..."
    show sayori curi om oe
    show natsuki anno cm oe
    show yuri cm
    s "Да мы прошли всего ничего!"
    show sayori cm
    show monika happ cm oe
    show natsuki om
    n "Батарейку спросить забыли."
    show sayori neut cm oe
    show monika om e1b
    show natsuki cm
    show yuri neut cm oe
    show kotonoha rdown
    m "Ну, раз мы дошли, то предлагаю разойтись по домам, пока есть силы."
    show monika cm oe
    show natsuki dist om ce
    n "Всё, аривидерчи."
    show natsuki e1a
    n "Юри, пошли."
    show sayori happ cm oe
    show natsuki cm
    show yuri happ om ce lup rup
    y "В-всем до завтра!"
    show yuri anno om oe
    y "Или до понедельника..."
    show sayori om ce
    show monika ce
    show yuri happ cm e1a
    s "Пока-пока!"
    show sayori cm
    show natsuki oe at thide
    hide natsuki
    show yuri cm ldown rdown at thide
    hide yuri
    pause 0.25
    show kotonoha neut cm oe
    pause 0.25
    show sayori oe
    show monika oe
    show kotonoha om at thide
    hide kotonoha
    k "Давайте я с вами, мне всё равно по пути."
    n "{size=19}Ну давай-давай!{/size}"
    n "{size=19}Только быстрее, а то я сейчас на месте грохнусь!{/size}"
    k "{size=19}До встречи, ребята!{/size}"
    show monika om
    m "Да, до встречи!"
    show monika cm
    mc "Угу."
    pause 0.25
    show sayori at t21
    show monika at t22
    pause 0.5
    show sayori om ce lup rup at h21
    s "А теперь идём встречать родителей Моники!"
    show sayori cm
    show monika ce

    scene black with wipeleft_scene
    "Родители..."
    "..."
    "...нет, я всё ещё нервный."
    "Тут на мозги давит всё подряд: новые люди, на которых надо произвести нормальное впечатление..."
    "...их СЛИШКОМ богатый статус (либо я чересчур его преувеличиваю)..."
    "...а ещё тот факт, что я парень Моники."
    "Я за себя ответить не в состоянии, а тут ещё за девушку, да ещё при статусе..."
    "Так, тьфу!" with vpunch
    "Во-первых, я не настолько сопливый дурачок, чтобы просто взять и кинуть всё на произвол судьбы."
    "Всё-таки Моника -- это мой выбор, который оказался взаимен."
    "А значит что?"
    "Правильно, нужно за это нести ответственность, а не пускаться в бестолковые размышления."
    "Во-вторых, я никогда никого не кидал."
    "Если мне отвечали искренностью, я всегда отвечал тем же."
    "Поэтому никогда в жизни я Монику не кину."
    "...если, конечно, она сама не захочет отколоться..."
    "..."
    "А как хоть её родителей зовут?..."
    mc "Моника, меня только что посетил жизненно необходимый вопрос."
    m "М-м?"
    mc "Как зовут твоих родителей?"
    s "О, а я тоже забыла!"
    m "Да{image=accent_low_register}{space=-15}йсуке и Хару{image=accent_low_register}{space=-15}ми."
    s "Точно..."
    mc "Дайсуке и Харуми..."
    mc "Понял, спасибо."
    m "Не переживай так, Макс."
    m "Ничего плохого не случится~"
    mc "А я напоминаю, что твои родители -- очень богатые и, вероятно, влиятельные люди."
    mc "Я всё ещё не могу прикинуть их примерную реакцию на то, что их дочь полюбила кого-то...{w}э-э-э, не столь богатого..."
    s "Но ведь я уже с ними знакомилась, и всё хорошо!"
    mc "Сайори, ты подруга, а не парень Моники, ага?"
    s "Да даже если бы была..."
    m "Нет-нет-нет, ребята, давайте не закапываться в этой теме..."
    m "Я скажу так: даже если мои родители тебя не примут, то я не изменю свою позицию."
    mc "...хорошо."
    s "Заявила, как настоящий лидер, хе-хе!"
    m "Хах, надо всё-таки поддерживать свои личностные качества."
    "Слова словами, а влияние всё равно не на её стороне."
    "Хотя, чёрт, хватит уже лепить стереотипные образы."
    "Пока не познакомлюсь с этими людьми, ничего не узнаю."

    scene bg monika house outside evening
    show monika forward green_hoodie_long happ cm oe at t21
    show sayori turned casual happ cm oe at t22
    with wipeleft_scene
    mc "О, это мы уже пришли?"
    show monika nerv mb oe
    m "Да, что-то мы...{w}слишком быстро сюда добрались."
    show monika cm
    show sayori om
    s "Ну, Макс шёл бодрым шагом, я за ним только и поспевала."
    show monika happ om ce
    show sayori cm
    m "А я за вами."
    show monika cm
    mc "Ну извините!"
    show monika neut cm oe
    mc "Зато точно не опоздали."
    show sayori neut cm oe
    m "..."
    mc "Что?"
    show sayori curi cm oe
    mc "Всё-таки опоздали?"
    show monika laug om e4c at h21
    show sayori neut cm oe
    m "Дядя Ма{image=accent_low_register}{space=-15}ртин!"
    show monika cm at thide
    hide monika
    "Какой ещё \"дядя Мартин\"?"
    show sayori happ cm oe
    um "{size=19}О-о-о, Моника, девочка наша!{/size}"
    mc "Кто этот дядька?"
    show sayori curi om e2b
    s "А, это...{w}э-э-э...{w}забыла, опять...{w}ну как там его..."
    show sayori happ om ce lup rup at h22
    s "...личный машиноводитель!"
    show sayori neut cm oe
    mc "Водитель."
    show sayori mh e2b ldown rdown
    s "А-а..."
    show sayori cm
    "Неудивительно, что у такого богатого человека будет собственный водитель...{w}иностранного происхождения..."
    show sayori oe
    m "{size=19}Ребята, давайте сюда!{/size}"
    show sayori happ om ce
    s "Идём!"
    show sayori cm
    "Ладно, пора уже знакомиться со всеми вами..."
    call window_close

    if persistent.add_random_menu == 14:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    hide sayori with dissolve
    pause 0.2
    scene bg monika house outside evening at monika_gate
    show monika forward green_hoodie_long happ cm oe at i31
    show uncle_martin happ cm oe at i32 zorder 2
    show sayori turned casual happ cm oe at i33
    with dissolve
    pause 0.25
    show uncle_martin om

    call window_open
    um "Здравствуйте, ребята."
    show uncle_martin cm
    show sayori om ce
    s "Здрасьте!"
    show monika b1b
    show uncle_martin om ce
    show sayori cm
    um "Ха-ха-ха, ты прямо как Моника: времена идут, а ты всё такая же озорная."
    show monika ce
    show uncle_martin cm
    show sayori tap casual nerv om oe at s33
    s "Э-хе-хе!"
    show monika oe -b1b
    show uncle_martin om oe
    show sayori turned casual happ cm oe at t33
    um "А вы кем будете, гостепочтенный юноша?"
    show uncle_martin cm
    mc "Я Макс, друг Моники, а также один из участников её школьного клуба."
    show uncle_martin om
    um "О как..."
    um "Вижу, Моника, ты потихоньку обрастаешь друзьями?"
    show monika om lpoint
    show uncle_martin cm
    m "Да, не сидеть же одной целую вечность!"
    show monika cm ldown
    show uncle_martin om ce
    um "Верно подмечено."
    show uncle_martin oe
    um "Можешь звать меня дядей Мартином, юноша."
    um "Я являюсь личным водителем отца Моники, а также просто её неродным дядей."
    show uncle_martin cm
    mc "Рад знакомству!"
    show uncle_martin om
    um "Взаимно."
    show monika sedu om oe
    show uncle_martin cm
    show sayori neut cm oe
    m "Кстати, Макс, врать нехорошо!"
    show monika ma
    show uncle_martin neut cm oe
    mc "Чего?"
    show monika om ce
    show sayori curi cm oe
    m "Никакой ты мне не друг!"
    show monika ma
    mc "???"
    show monika om oe
    show sayori e1a
    m "Ма-а-акс..."
    show monika happ om oe lpoint rhip
    show uncle_martin lsur cm oe
    show sayori nerv cm oe
    m "Дядя Мартин, он мой возлюбленный!"
    show monika cm ldown
    show uncle_martin om
    um "Возлю-ю-юбленный?"
    show uncle_martin cm
    mc "{size=17}ЁПТ!{/size}" with vpunch
    show sayori mb
    s "Как пафосно..."
    show sayori cm
    mc "{size=19}Моника, зачем так сразу?!{/size}"
    show monika om ce
    m "{size=19}Не вижу смысла молчать!{/size}"
    show monika cm
    show uncle_martin neut om oe
    show sayori neut cm oe
    um "Совет вам да любовь, но как бы твои родители тебе не воспрепятствовали..."
    show monika om oe
    show uncle_martin cm
    show sayori happ cm oe
    m "Ничего-ничего, это мой личный твёрдый выбор!"
    show monika ce
    m "Поэтому я готова дать отпор!"
    show monika cm
    show sayori neut cm oe
    mc "А ДАВАЙТЕ мы не будем ни с кем сражаться, мы даже с ними ещё не поговорили!"
    show monika oe
    mm "{size=19}Мартин, чего вы там на улице стоите?{/size}"
    mm "{size=19}Пригласи всех в дом, пусть посидят в гостиной!{/size}"
    show monika rdown
    show uncle_martin om
    um "Конечно, секунду."
    show uncle_martin happ om oe
    show sayori happ cm oe
    um "Давайте, ребята, пройдёмте во внутрь, пообщаемся в более комфортной обстановке."
    show uncle_martin cm
    show sayori om ce lup rup at h33
    s "С удовольствием!"
    stop noise_1 fadeout 2.0
    show monika ce
    show sayori cm ldown rdown
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day at monika_sofa
    show sayori turned casual happ cm e1b at e11
    with wipeleft_scene
    mc "Пф-ф-ф..."
    "Уже около 5 минут прошло."
    "Что они там все делают?"
    "И почему Сайори такая расслабленная?"
    show sayori ce
    "Меня внутри уже всего сжало."
    mc "Блин, Сайори, как ты умудряешься быть такой спокойной?"
    s "...м-м, м-м, м-м~"
    show sayori om oe
    s "А?"
    show sayori neut cm oe
    mc "...проехали."
    show sayori curi om e1a
    s "Чего?"
    show sayori cm oe
    mc "О, кто-то идёт..."

    $ md_name = _("Дайсуке-сан")

    scene bg monika house livingroom day with dissolve
    pause 0.5
    show monika_dad neut cm oe casual at t11 zorder 2
    pause 1.0
    show monika_dad om
    md "Ну здравствуй, Макс."
    show monika_dad cm
    show sayori turned casual happ cm oe at t33
    mc "Здравствуйте."
    show monika_dad om
    md "И рад видеть тебя, Сайори."
    show monika_dad cm
    show sayori ce
    s "Угусь!"
    show monika_dad om lup
    show sayori oe
    md "Давайте присядем, нечего напрягаться попусту."
    show monika_dad cm ldown
    call window_close

    hide monika_dad
    hide sayori
    with dissolve
    pause 0.2
    scene bg monika house livingroom day at monika_sofa
    show sayori turned casual happ cm oe at e21 zorder 2
    show monika_dad casual neut cm oe at e22
    with dissolve
    pause 0.25

    call window_open
    show monika_dad om
    md "Приятно осознавать, что у Моники появились, не побоюсь этого слова, друзья."
    md "Редко в нашей жизни встречаются люди, которым можно довериться без задних мыслей."
    md "Однако сейчас я хотел бы поговорить о другом."
    show sayori neut cm oe
    md "Сайори, можешь покинуть комнату на некоторое время?"
    md "Я хотел бы обсудить кое-какие вещи с Максом наедине."
    show sayori om
    show monika_dad cm
    s "...ох, конечно."
    show sayori happ cm oe
    show monika_dad om
    md "Можешь пока зайти в комнату к Монике, она сейчас там вместе с матерью и Мартином разбирает наши подарки."
    show sayori om ce
    show monika_dad cm
    s "Хорошо!"
    show sayori cm
    pause 0.2
    show sayori:
        ease 0.75 yoffset 100
    pause 0.9
    hide sayori with easeoutleft
    pause 0.5
    "Подарки...{w}наверное, Моника «заказывает» у родителей что-то «экзотическое», а они ей это привозят?"
    show monika_dad cm:
        ease 0.75 xcenter 640
    pause 1.0
    show monika_dad om
    md "Итак."
    md "Я ещё не представился."
    show monika_dad mc lup
    md "Меня зовут Дайсуке, я глава японского филиала американской компании {color=#fc7e23}Multi Orange Group{/color}."
    show monika_dad cm ldown
    "Одна из крупных IT-компаний, которую я иногда видел в Интернете, нифига себе..."
    show monika_dad om
    md "Как ты мог заметить, я не являюсь коренным японцем."
    md "Я родился в США, а моё истинное имя -- Дэн."
    $ md_name = _("М-р Дэн")
    md "Поэтому ты можешь называть меня просто мистером Дэном."
    show monika_dad cm
    mc "Угу."
    show monika_dad om
    md "Собственно говоря, мне Моника уже про тебя немного рассказала."
    md "И про отношения тоже."
    show monika_dad cm
    mc "...угу."
    show monika_dad om
    md "Мне искренне интересно, что именно сподвигло тебя на отношения с Моникой?"
    md "Был ли это выбор, основанный на её внешности, или здесь сыграло роль нечто более глубокое?"
    show monika_dad cm
    mc "...могу сказать, что она мне нравится как внешне, так и внутренне."
    md "Угум."
    mc "По характеру она очень со мной...{w}скажем так, коррелирует."
    show monika_dad om
    md "Насколько сильно?"
    show monika_dad cm
    mc "Достаточно серьёзно."
    md "Угум."
    mc "Мы схожи с ней в некоторых аспектах поведения, а также понимаем и уважаем друг друга."
    show monika_dad om
    md "Ясно."
    md "И давно вы в отношениях?"
    show monika_dad cm
    mc "Буквально одну неделю."
    show monika_dad om
    md "Всего лишь?"
    show monika_dad cm
    mc "Да."
    mc "Я переехал в Ниигату 3 недели назад, а вступил в клуб Моники практически 2 недели назад."
    show monika_dad om
    md "Переехал?"
    show monika_dad cm
    mc "Да."
    show monika_dad om
    md "Любопытно..."
    show monika_dad cm
    "Я уже понял, что он меня изучает, поэтому не хочу «выкладывать» всю информацию ему на стол."
    show monika_dad om lup
    md "Не думаешь ли ты, что твои чувства к Монике могут угаснуть со временем?"
    show monika_dad cm ldown
    mc "...иногда меня посещали такие мысли, но всё-таки я сделал свой твёрдый выбор."
    mc "Могу сказать, что, в отличие от остальных сверстников, я старался подойти к этому выбору более ответственно и осознанно."
    md "Хм-м-м..."
    "Кажется, он не ожидал от меня такого ответа..."
    show monika_dad om
    md "Похвально, что ты с холодной головой стараешься принимать важные для тебя решения..."
    md "Но думал ли ты про будущее?"
    show monika_dad lup
    md "Я сейчас имею в виду, что ты, вероятнее всего, пойдёшь получать высшее образование, верно?"
    show monika_dad cm ldown
    mc "Да."
    show monika_dad om
    md "И тебе придётся снова переехать, но уже в другой город на период всего обучения, поскольку хорошие крупные вузы находятся далеко от Ниигаты."
    show monika_dad cm
    mc "...да, я это понимаю."
    show monika_dad om
    md "А Монике придётся улететь в Америку, где она на первое время получит образование и работу."
    show monika_dad cm
    mc "...в Америку?"
    show monika_dad om
    md "Тебя это удивляет?"
    show monika_dad cm
    mc "Но почему ей не остаться здесь и поступить в какой-нибудь престижный вуз..."
    show monika_dad mc
    md "Повторяю: в Америке она получит образование {b}и{/b} работу."
    show monika_dad cm
    mc "И что это за работа такая, что ей придётся ради неё аж страну менять?"
    show monika_dad om
    md "Связана с моей компанией, но не с японским отделом."
    show monika_dad cm
    mc "Не могу понять, что вы имеете в виду."
    show monika_dad om lup
    md "...скажу так: слишком много «нюансов», из-за которых Моника здесь не сможет получить образование и дальнейшее карьерное развитие."
    show monika_dad cm ldown
    mc "...совсем?"
    show monika_dad om
    md "Совсем."
    show monika_dad cm
    mc "Угу..."
    show monika_dad om
    md "Понимаю, возможно, ты расстроен подобной новостью, но ты должен знать, что это неизбежно."
    show monika_dad cm
    mc "Прекрасно осознаю."
    show monika_dad om
    md "Отношения сейчас ей только навредят, поскольку она ещё не готова к настоящей взрослой жизни."
    md "Ведь ими необходимо заниматься, как только найдёшь своё место в обществе."
    show monika_dad cm
    mc "...а в чём проблема отношений с нормальным человеком?"
    show monika_dad om lup
    md "Это же очевидно: её мотивация и цель будут сбиты чувствами и эмоциями."
    show monika_dad ldown
    md "А уж к чему это приведёт, одному только лишь Богу известно."
    show monika_dad cm
    "Богу...{w}это у вас в Америке, а у нас -- духи с многобожием!"
    mc "Какова вероятность, что Моника не займётся отношениями за океаном?"
    show monika_dad om
    md "У меня будет больше времени и возможности её контролировать."
    show monika_dad cm
    mc "А вы её саму вообще спрашивали?"
    show monika_dad om
    md "Мы уже с ней всё обсудили."
    $ nightmare_active = True
    show monika_dad angr om oe
    md "И почему я должен отчитываться перед тобой по личным отношениям со своей дочерью?"
    show monika_dad cm
    mc "Вы издеваетесь?"
    mc "Я парень вашей дочери, причём не тупой среднестатистический обрыган, у которого в голове из желаний только прилюдно пососаться и поиметь девушку во все дыры!"
    mc "Я тот, кто понимает её чувства и помогает со всем, если есть такая возможность, получая при этом взаимность с её стороны!"
    mc "Она заслуживает поддержки, особенно психологической, которой, судя по её рассказам, она от Вас не получает!"
    mc "И ВЫ просто ХОТИТЕ вот так взять и ВЫРВАТЬ из неё эту поддержку!"
    show monika_dad om lup
    md "Во-первых, успокой свой пыл, никому твои эмоции тут неинтересны."
    show monika_dad ldown
    md "Во-вторых, ты серьёзно думаешь, что я поверю в то, что какой-то 18-летний ученик за жалкие пару недель смог хоть как-то повлиять на Монику?"
    md "Это даже звучит абсурдно."
    show monika_dad cm
    mc "..."
    show monika_dad om
    md "Макс."
    md "Я не позволю тебе повлиять на её будущую жизнь."
    md "Потому что ты её просто поломаешь своей молодёжной дурью."
    show monika_dad lup
    md "Ты не знаешь истинного положения вещей, но при этом пытаешься что-то диктовать."
    show monika_dad neut om oe ldown
    md "Поэтому образумься: расстанься с Моникой, пока это не зашло слишком далеко, чтобы минимизировать негативные последствия."
    md "...которые, в свою очередь, неизбежно наступят, если ты продолжишь гнуть свою линию."
    md "И больше всего пострадает при этом сама Моника."
    show monika_dad cm
    mc "........................"
    m "{size=19}Хэй, папа!{/size}"
    m "Спасибо за духи, у них очень тонкий и приятный аромат!"
    s "У меня теперь точно голова в кучку..."
    mm "Ха-ха-ха, папа в этот раз постарался с поиском!"
    m "А, вы разговариваете..."
    mc "В который раз убеждаюсь: все вы, люди, -- откровенные уроды."
    show monika_dad angr cm oe
    mc "Эгоистичные и умеющие только гадить!"
    m "...что?"

    scene bg monika house livingroom day
    show sayori turned casual neut cm e2a at i31
    show monika forward green_hoodie_long lsur cm oe at i32 zorder 2
    show monika_mom casual angr cm oe rhip at i33 zorder 3
    with dissolve
    pause 0.25
    mc "Сайори, пошли отсюда нахрен."
    show sayori curi om oe
    s "А?!"
    show sayori e1a
    s "Почему?"
    show sayori pani cm oe
    mc "{sc=3}ПОШЛИ!{/sc}" with vpunch

    scene black with wipeleft_scene
    if persistent.censorship:
        md "{size=15}Малолетний дурак...{/size}"
    else:
        md "{size=15}Малолетний мудак...{/size}"
    m "{size=19}Папа, что ты ему наговорил?!{/size}"
    mm "{size=17}Дайсуке, ты опять за своё?!{/size}"
    call window_close

    if persistent.add_random_menu == 15:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 evening
    show sayori turned casual vsur cm oe at t11
    with wipeleft_scene
    mc "Ура, подальше от этого места..."
    show sayori om
    s "Так что случилось?!"
    show sayori cm
    mc "Случилось?!"
    show sayori e1a
    mc "Меня вежливо послали нахрен!"
    show sayori om
    s "Почему?!"
    show sayori pani cm oe
    mc "Потому что эта мразь хочет отправить Монику туда, за океан, в Америку!"
    mc "Чтобы она там получила образование с работой, да там же и осела в компании, где он работает!"
    mc "И никаких ей отношений нельзя, потому что это собьёт её с пути успешного успеха!"
    mc "И компромиссы не принимаются по причине: \"Нафиг надо мне с тобой возиться?!\""
    show sayori vsur cm e1a
    mc "И желания Моники мы тоже учитывать не будем, ибо: \"А чё она такая с самомнением? Ещё ж молодая и тупая, не осознаёт перспективность своего будущего\"!"
    if persistent.censorship:
        mc "ТЬФУ, ТВОЮ МАТЬ!" with vpunch
    else:
        mc "ТЬФУ, БЛЯТЬ!" with vpunch
    s "О-о..."
    show sayori sad cm oe
    if persistent.censorship:
        mc "Аргх, у меня только начала выстраиваться более-менее адекватная личная жизнь, а тут ХРЕНАК, и тебя уже обгадили, потому что «потому»!"
    else:
        mc "Аргх, у меня только начала выстраиваться более-менее адекватная личная жизнь, а тут ХЕРАК, и тебя уже обосрали, потому что «потому»!"
    mc "И что только не возьми, подобное случается каждый, абсолютно..."
    show sayori vsur cm e1a
    mc "{sc=3}КАЖДЫЙ!{/sc}" with vpunch
    show sayori pani cm oe
    if persistent.censorship:
        mc "{sc=3}ЧЁРТОВ!{/sc}" with vpunch
    else:
        mc "{sc=3}СРАНЫЙ!{/sc}" with vpunch
    mc "{sc=3}РАЗ!{/sc}" with vpunch
    if persistent.censorship:
        mc "Почему я просто не могу избавиться от всех этих идиотов НАХРЕН, чтобы зажить нормальной жизнью..."
    else:
        mc "Почему я просто не могу избавиться от всех этих идиотов НАХЕР, чтобы зажить нормальной жизнью..."
    mc "{sc=2}Но не-е-ет, я же ОБЯЗАН вариться среди этих\nтварей, видя их мерзкие отторгающие рожи!{/sc}"
    mc "{sc=3}ДЕРЬМО, А НЕ ЖИЗНЬ, И САМОЕ МЕРЗКОЕ, ЧТО НЕ\nЯ ЭТО ВЫБРАЛ!{/sc}"
    show sayori om ce lup rup at h11
    s "Макс-Макс-Макс, тихо, хватит, пожалуйста, успокойся-успокойся-успокойся!"
    show sayori cm
    mc "Да всё уже, Сайори, не переживай...{w}я перегорел."
    show sayori sad cm oe ldown rdown
    mc "Ни эмоций, ни настроения, которое было полчаса назад."
    mc "Извини, что взорвался, но такое уже далеко не первый раз происходит, реально, меня это уже откровенно выбешивает."
    show sayori vsur cm oe
    mc "А ещё теперь голова кружиться начала, блин..."
    show sayori om
    s "Тебе не нужна помощь?!"
    show sayori cm
    mc "Нет, успокойся, ничего критичного."
    show sayori sad cm oe
    mc "Пф-ф-ф..."
    s "...ум-м..."
    show sayori worr om oe
    s "Я даже не знаю, что сказать, чтобы поддержать тебя..."
    show sayori neut cm oe
    mc "...и не надо."
    mc "Твоего существования уже достаточно."
    mc "Тем более мне надо самому всё это переварить и обдумать на холодную голову."
    mc "Лучше пойдём домой, ноги болят."
    show sayori om
    s "М-м...{w}хорошо..."
    show sayori cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    $ nightmare_active = False

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "..."
    "..."
    mc "Ф-ф-ф..."
    "..."
    "...странно, что Моника никому про планы своего отца не рассказывала..."
    "По крайней мере, Сайори перед уходом сказала, что о них лично не знала, чего уж говорить про остальных..."
    "Так что не я один шокирован такой информацией."
    mc "..."
    mc "И что же...{w}с этим делать?..."
    "Будто жизнь продолжает надо мной издеваться."
    "У меня только-только худо-бедно начались дарованные свыше отношения, а сейчас они уже висят на волоске, который так и норовит разорваться."
    "В этой проблеме я совершенно бессилен."
    "Я никак не могу повлиять на богатого, властного и уверенного в себе человека."
    "Тем более у меня нет того жизненного опыта, который он пережил..."
    mc "Да, я не отрицаю, что Моника получит офигенное высшее образование и работу, с которой она будет грести большие бабки."
    mc "Но...{w}это буквально против её воли."
    mc "Да и отношения..."
    mc "Не, ну хорошо, предположим, что она улетела."
    mc "Можно же общаться дистанционно."
    mc "...а дальше что?"
    mc "Пройдёт пара месяцев, потом полгода, потом год, а дальше вообще несколько лет."
    mc "За это время мы точно к друг другу охладеем, у неё, может, новый парень появится, получше и побогаче меня..."
    mc "Я-то уж точно за границу выехать не смогу."
    mc "А если и смогу, то случится это хрен-пойми-когда, к тому моменту уже поздно будет."
    mc "М-м-м..."
    mc "А если Моника сама захочет сюда приехать или найдёт способ пристроить меня рядом с собой?"
    mc "Но это тогда вообще какое-то нахлебничество!"
    mc "Да и звучит, как инфантильный бред."
    mc "Кто будет напрягаться, тратить время, деньги и нервы ради того, чтобы пристроить к себе левого человека, который в работе может оказаться полным нулём?"
    mc "...нет, вся это ситуация -- это реально провал."
    mc "У меня нет вариантов, что можно сделать."
    mc "Да я буквально сейчас подросток, который из себя ничего не представляет."
    mc "..."
    mc "...провал..."
    mc "Вечно всё через жопу, и никак иначе."

    phone register "mc_m_chat":
        time year 2018 day 28 month 4 hour 19 minute 2
        "m" "Макс... Прости, что такое произошло... Я это совсем не ожидала"

    play phone_sound new_message_mc
    pause 1.0
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 45
        clock = (19, 2)

    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Моника, извини, давай завтра всё обсудим"
        "mc" "Сейчас я дико устал"
        "m" "Конечно("
        "m" "Обязательно выспись"
        "mc" "Ты тоже"
        "mc" "И не ругайся с родителями из-за меня, ладно?"
        "m" "Ладно"

    phone end discussion transition

    call skip_block_off
    mc "Выспаться..."
    mc "Ха, а Сайори-то забыла про своё желание выспаться на моей кровати..."
    mc "Хотя к ней отец вернулся спустя 2 недели, пока мы у Моники торчали, неудивительно."
    mc "..."
    mc "Опять я в слух всё сказал."
    mc "Да пошло оно...{w}так даже как-то проще, что ли..."
    mc "Но вот вся внутренняя грязь никуда не девается."
    mc "Как бурлило дерьмо внутри, так и бурлит."
    mc "..."
    mc "Психолога этого ещё искать..."
    mc "Да пошёл он нахрен!"
    mc "Тратить тут ещё время на человека, который забил на меня..."
    mc "..."
    mc "Что-то боль в ногах и голове усилилась..."
    mc "Либо просто тело уже ослабло окончательно."
    mc "..."
    mc "Ещё что-то там было по другим проблемам...{w}да пусть идут нахрен!"
    mc "Знаете, я тоже человек, который хочет, блин, отдохнуть!"
    mc "А нету этого отдыха."
    mc "И не предвидется, пока на работу не выйду, а это лет через 5 минимум."
    mc "За это время сдохнуть кучу раз можно."
    mc "..."
    mc "Домашнее задание я сделал."
    mc "..."
    mc "Не хочу я о школе думать, блевотина чёртова..."
    mc "Только Литературный клуб кое-как скрашивает картину, да и то с переменным успехом."
    mc "..."
    mc "Странно, я хоть и разбитый, но силы на мелкую рутину у меня остались."
    mc "Хотя мозг отрубается будто быстрее обычного."
    mc "Аргх, не понимаю!"
    mc "У меня будто есть желание что-то поделать, но при этом силы быстро покидают."
    mc "......"
    mc "Вообще расслабиться не могу!"
    mc "Написать стих, чтобы окончательно себя добить?"
    mc "Эта рутина точно отяготит и вырубит нафиг."
    mc "Только в этот раз я могу прерваться в любой момент, потому что в клубе никто не говорил об обмене стихами в следующий понедельник."
    mc "Собственно говоря...{w}где ручка и тетрадный лист..."

    call poem_act_1_day_13

    pause 5.0

    $ nightmare_active = True

    call nightmare_act_1_day_13
    $ _history_list.clear()

    return
