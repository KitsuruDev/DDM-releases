
label prologue_day_1:

    python:
        contact_list["mc"].clear()
        contact_list["mc"].extend(["mc_mcm_chat", "mc_s_chat"])

    $ quick_menu = False

    scene black
    with dissolve_scene_full

    pause 3.5
    play sound ringtone_vibration
    pause 4.0

    call window_open
    "Чёртова вибрация, всегда передёргивает от её неожиданности."
    "Кому я на этот раз понадобился?"
    call skip_block_on
    call window_close

    pause 1.0
    stop sound
    pause 0.5

    phone call "mc_mom" video
    show bg morioka office inside onlayer call_layer:
        align (0.6, 0.2)
    show mc_mom neut cm oe at tphone onlayer call_layer
    with dissolve
    pause 0.25

    if not persistent.first_phone_call:
        show hint_phone_call at hint_position onlayer front

    call window_open
    call skip_block_off
    phone_mc "Алло."

    if not persistent.first_phone_call:
        $ persistent.first_phone_menu_apps = True
        $ renpy.save_persistent()
        hide hint_phone_call onlayer front

    show mc_mom om
    phone_mcm "Солнышко, привет."
    show mc_mom cm
    phone_mc "Привет, мам--{w=0.5}{nw}"
    show mc_mom sedu cm oe
    phone_mc "Эй-эй, почему видеосвязь?!"
    show mc_mom om
    phone_mcm "Хочу насмотреться на своего сына перед его скорым отъездом."
    show mc_mom cm
    phone_mc "А что, уже документы в новой школе приняли?"
    show mc_mom neut om oe
    phone_mcm "Да, папа сейчас написал, что все бумаги наконец-то одобрены."
    show mc_mom cm
    phone_mc "Фух, отлично."
    show mc_mom om
    phone_mcm "После весенних каникул будешь уже заниматься там."
    show mc_mom cm
    phone_mc "Угу."
    show mc_mom om bd
    phone_mcm "Не забудь подготовиться к переезду."
    show mc_mom cm
    phone_mc "Да, конечно, уже это делаю."
    show mc_mom om brow
    phone_mcm "Ты же помнишь, как можно добраться до нашего дома в Ниига{image=accent_call_low_register}{space=-15}те?"
    show mc_mom cm
    phone_mc "Помню я, помню."
    phone_mc "Уже столько раз там бывали, смогу спокойно соориентироваться."
    phone_mc "И телефон к тому же всегда под рукой."
    show mc_mom om
    phone_mcm "Хорошо."
    phone_mcm "Оплату электричества и воды берём на себя, поэтому за это не беспокойся."
    show mc_mom cm
    phone_mc "Угу."
    show mc_mom angr om oe
    phone_mcm "Но и не транжирь много денег!"
    show mc_mom cm
    phone_mc "Я похож на транжиру?"
    show mc_mom sedu om oe
    phone_mcm "А мало ли!"
    show mc_mom neut om oe
    phone_mcm "Так, ещё будем делать тебе переводы на карту раз в месяц."
    show mc_mom cm
    phone_mc "Угу."
    show mc_mom om eg
    phone_mcm "Ключи от дома у тебя есть, практически все твои важные вещи перевезли..."
    show mc_mom oe
    phone_mcm "Вроде бы всё."
    show mc_mom cm
    phone_mc "По-моему, да, больше ничего такого не осталось."
    phone_wor "И{image=accent_call_high_register}{space=-15}дзуми-cан, вот пак документов, можете ознакамливаться."
    show mc_mom happ om ce
    phone_mcm "Хорошо, секунду!"
    show mc_mom angr om oe
    phone_mcm "И хоть в новой школе заведи себе друзей, а то обычно ни с кем не общаешься."
    show mc_mom cm
    phone_mc "Мам!..."
    show mc_mom anno cm oe
    phone_mc "Не волнуйся ты так, разберусь я с этим, уже не маленький."
    show mc_mom om
    phone_mcm "Ну-ну!"
    phone_mcm "А то другие там гуляют-разговаривают, а ты дома сидишь."
    show mc_mom cm
    phone_mc "Ох-х-х..."
    show mc_mom om
    phone_mcm "Не охай."
    show mc_mom cm
    phone_mc "Больше ничего нового, важного?"
    show mc_mom neut om oe
    phone_mcm "Нет, наверное..."
    show mc_mom cm
    phone_mc "Хорошо, тогда я отключусь, закончу сбор своих мелких вещей."
    show mc_mom happ om oe
    phone_mcm "Ладно, солнышко, не буду тебя отвлекать."
    show mc_mom cm
    phone_mc "Всё, пока."
    show mc_mom om ce
    phone_mcm "Пока-пока."
    show mc_mom cm
    pause 0.2
    call window_close

    phone end call "30/03/2018"
    hide bg morioka office inside onlayer call_layer
    hide mc_mom onlayer call_layer
    with dissolve

    call window_open
    "..."
    "Даже я так не волнуюсь за свой переезд, как моя мама."
    "Нормально ж всё...{w}подождите..."
    "Этот разговор же был чуть меньше недели назад."
    call window_close

    pause 0.2
    play sound station_announcement fadein 7.0
    play noise_2 station_noise fadein 7.0
    pause 5.0

    call window_open
    scene bg morioka station morioka platform with dissolve_scene_full
    call autosave
    "..."
    mc "...блин."
    "Сморило так, что незаметно вырубился."
    "..."
    mc "Ах, точно!"
    "Надо отписаться, что я уже добрался досюда."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = False
        battery_level = 98
        clock = (10, 7)

    phone discussion "mc_mcm_chat"

    if not persistent.first_phone_typing:
        show hint_phone_typing at hint_position onlayer front

    $ plot_pause()

    if not persistent.first_phone_typing:
        hide hint_phone_typing onlayer front
        $ persistent.first_phone_typing = True
        $ renpy.save_persistent()

    phone discussion "mc_mcm_chat":
        time year 2018 month 4 day 2 hour 10 minute 7
        "mc" "Всё, я успел прийти на станцию. Поезд скоро подойдёт"
    mc "Аргх, Интернет!"
    window hide

    if not persistent.first_phone_menu_action:
        show hint_phone_menu at hint_position onlayer front

    call phone_status_bar_button('cellular_data', disable = False)

    if not persistent.first_phone_menu_action:
        hide hint_phone_menu onlayer front
        $ persistent.first_phone_menu_action = True
        $ renpy.save_persistent()

    window auto
    $ phone.system.clock = (10, 8)
    mc "Другое дело."
    phone discussion "mc_mcm_chat":
        "mc_mom" "Отлично!"
        "mc_mom" "Извини, что мы с папой не можем лично с тобой попрощаться"
        "mc_mom" "Много дел на работе"
        "mc" "Да ладно, я всё понимаю"
        "mc_mom" "Удачи тебе! Ты со всем справишься, верим в тебя!"
        "mc_mom" "И помни: мы все тебя любим!"
        "mc" "Спасибо за поддержку!"
    $ phone.system.clock = (10, 9)
    phone discussion "mc_mcm_chat":
        "mc_mom" "И обязательно отпишись ещё раз, когда доберёшься до дома! Мы за тебя волнуемся!"
        "mc" "Да-да, обязательно"
    "О, уже поезд виднеется вдалеке..."
    "Отрубаемся от сети."
    window hide

    call phone_status_bar_button('cellular_data', disable = True)

    phone end discussion transition

    call skip_block_off
    "Вообще как-то не ощущается, что я переезжаю жить в новое место."
    "Один."
    "Настрой сейчас такой, будто вышел на прогулочку в какое-нибудь культурное место: музей, парк..."
    "...но я сейчас буквально меняю свою жизнь."
    "Хотя чего тут нового: та же ситуация, только в профиль."
    "С другой стороны, всё зависит от нового школьного общества..."
    "...на которое я не делаю ставку даже после всех этих разговоров про социальные взаимодействия, которые мне изрядно надоели."
    "Учёба и формирование финансовой основы под ногами должно быть на первом месте, а всё остальное -- потом."
    "Иначе получиться полная бурда."
    call window_close

    play noise_1 station_train_arrival
    queue noise_1 train_doors_open
    queue noise_1 train_waiting
    scene black with dissolve_cg

    pause 24.5

    stop noise_2 fadeout 8.0
    play sound mc_steps

    pause 4.0

    queue noise_1 train_doors_close

    pause 5.5

    stop noise_1

    pause 1.0

    call window_open
    clt "Жаль, что ты нас покидаешь."
    clt "Всё-таки один из способных и преуспевающих учеников."
    clt "Хотя, когда дело касается общения, ты всегда остаёшься один."
    clt "Разве что разговариваешь с парочкой сверстников, но не более."
    clt "Даже перетасовки классов не могут исправить твоё положение."
    mc "Никто из одноклассников меня не привлекает."
    clt "Я понимаю, но у тебя дальше взрослая жизнь."
    clt "Социальные навыки в ней являются необходимостью."
    clt "А раз ты переходишь в другую школу, то воспользуйся шансом наверстать упущенное."
    clt "Не каждому он даётся -- терять его совершенно глупо."
    mc "Хорошо."
    clt "Если тебе по силе были все учебные предметы, то и с этим ты тоже успешно справишься."
    call window_close

    pause 1.0

    play noise_1 train_moving_1 fadein 6.0

    pause 20.0

    call window_open
    scene bg train zorder 1
    show train_window_field zorder 0
    with dissolve_scene_full
    mc "Фух-х-х..."
    "Опять срубило..."
    "Но неудивительно: солнце, пара пересадок, большие толпы на городских станциях..."
    "Зато теперь наконец-то долгая поездка по пригороду и полям в полупустом продуваемом вагоне на мягком сиденье."
    "Самое то, чтобы...{w}нормально выспаться?"
    "Но я сейчас уже в бодром состоянии."
    "Если попытаюсь уснуть намеренно, то голова разболится, она и так сейчас ватная."
    "А делать больше и нечего."
    mc "{size=19}Натуральное издевательство.{/size}"
    "Остаётся только лицезреть пейзажи за окном."
    "Может, они помогут мне плавно уснуть..."
    call window_close

    pause 10.0

    play phone_sound new_message_mc
    pause 2.0

    $ quick_menu = True
    call skip_block_on

    python in phone.system:
        cellular_data = True
        battery_level = 97
        clock = (11, 21)

    phone register "mc_s_chat":
        time year 2018 day 2 month 4 hour 11 minute 21
        "s" "Я так рада что ты будешь жить рядом со мной! (> ω <)"

    phone discussion "mc_s_chat"
    $ plot_pause()
    mc "{size=19}Уведомление?{/size}"
    "Я Интернет не вырубил?"
    "Классно."
    "Столько раз залезал в мобильник, что на автомате не заметил."
    "Надеюсь, трафик не сгорел..."
    "Ой, ладно, хотя бы сообщение от Сайо{image=accent_low_register}{space=-15}ри увидел."
    "Странно, что она часто про меня вспоминает..."
    "Зато всегда пытается поддержать разговор, где бы я ни был."
    "Сайори -- настоящий друг."
    "Точнее, единственный...{w}но настоящий."
    $ phone.system.clock = (11, 22)
    "До сих пор не могу в это поверить..."
    "Так!" with vpunch
    "Очередной провал в себя, а?"
    "Никак не могу контролировать эту хрень."
    "Всё, пора уже что-нибудь напечатать."
    phone discussion "mc_s_chat":
        "mc" "Я тоже рад!"
    "Гениально..."
    "Мог бы и получше что-нибудь придумать."
    phone discussion "mc_s_chat":
        "s" "Я подумала и решила что встречу тебя на станции Ниигата!"
    mc "{size=19}Чё?...{/size}"
    $ phone.system.clock = (11, 23)
    "Стоп, не-не-не, Сайори, у меня голова кругом, давай не будем сегодня встречаться, пожалуйста..."
    "Ты же не обсуждала эту идею со своей матерью?"
    phone discussion "mc_s_chat":
        "s" "И я уже обсудила это с мамой! Не думай что всё будет проходить втёмную! (> . <)"
    "..."
    "У меня УЖЕ нет выбора, чёрт побери."
    "В который раз убеждаюсь: Сайори -- прирождённый манипулятор."
    "Думаешь, что она всего лишь миленькая и рассеянная девушка 17-ти лет, на которую не каждый обратит внимание..."
    "...а уже и не осознаешь, как попал в её липкие сети, из которых никогда не выберешься."
    $ phone.system.clock = (11, 24)
    "Подождите, она уже девушка...{w}17-ти лет?..."
    "Блин, как время летит--{nw}"
    "Аргх, хватит!" with vpunch
    "Сейчас не до раздумий!"
    "Ответ-ответ-ответ..."
    phone discussion "mc_s_chat":
        "mc" "Мне ещё час ехать, не меньше"
        "mc" "Ты ещё не вышла?"
        "s" "Ну..."
        "s" "Я немного продвинулась в этом процессе (´• ω •)"
        "mc" "Насколько?..."
        "s" "А ещё сегодня на улице очень хорошая погода! И как раз под твой приезд! (* ^ ω ^)"
    $ phone.system.clock = (11, 25)
    phone discussion "mc_s_chat":
        "mc" "Сайори, ты уходишь от вопроса"
        "s" "Нуууу..."
        "s" "Я тут..."
        "s" "Сижу..."
        "mc" "На станции?..."
        "s" "Да (_ _*)"
    "..."
    "Она не размышляла, встречать меня или нет."
    "Она {b}планировала{/b} встретить меня, даже не обсудив эту идею со мной."
    phone discussion "mc_s_chat":
        "mc" "Блин, Сайори..."
        "mc" "Тебе ещё час там торчать, зачем так торопиться?"
        "s" "Мой лучший друг переезжает ко мне, это же самое лучшее событие из всех! Такое нельзя пропускать!\n(^ ω ^)"
    $ phone.system.clock = (11, 26)
    "Вот и ворчи потом на это чудо..."
    "Одни искренние положительные эмоции, которых не дождёшься от большинства."
    "И мало того, так ещё направленные исключительно в твою сторону."
    "...однако это не оправдывает её свершившиеся действия."
    phone discussion "mc_s_chat":
        "mc" "Ты хоть где примерно сидишь?"
        "s" "Около выхода на улице. Тут в теньке прохладно (= ω =)"
        "mc" "Ладно, жди тогда. И смотри, отсидишь себе одно место, потом болеть будет"
        "s" "Ничего я себе не отсижу -- тут мягко!\n(# > . <)"
    mc "{size=19}Пф...{/size}"
    $ phone.system.clock = (11, 27)
    "Отрубаемся на этой странной ноте."
    window hide

    call phone_status_bar_button('cellular_data', disable = True)

    phone end discussion transition

    call skip_block_off
    mc "{size=19}Мда...{/size}"
    "Это же теперь ей надо билет на автобус купить до нашего района..."
    "Не поеду же я на нём один?"
    "Чёрт тебя побери, Сайори..."
    "Я с тобой дружу всего чуть больше полугода, но уже столько хлопот навидался..."
    "Вот честно, зачем мне другие друзья, когда есть Сайори?"
    "У меня просто сил на других не остаётся."
    "К слову, о силах..."
    "Я снова размяк."
    "Снова подремать, что ли?"
    "Только надо сначала билет на сайте купить..."
    call window_close

    pause 0.25

    scene black with Dissolve(4.0)
    stop noise_1 fadeout 6.0

    pause 3.0

    call window_open
    dir "Досадно, что из-за событий, на которые невозможно повлиять, приходится терять трудоспособных учеников."
    mc "...ну...{w}моей семье нужны деньги на моё будущее обучение в вузе..."
    dir "Знаю, это было риторическое предложение."
    mc "Простите."
    dir "Не за что."
    dir "Ты должен радоваться, что тебя переводят в лучшую школу Ниигаты."
    dir "Целый учебный комплекс на 600 человек, в котором несколько лет назад сделали капитальный ремонт основного корпуса."
    dir "Есть всё необходимое оборудование, помещения, инфраструктура..."
    dir "И это тебе станет доступным."
    mc "...угу."
    dir "..."
    mc "..."
    dir "Всё."
    dir "Все твои документы, которые нужно передать в новое учебное заведение."
    mc "Хорошо."
    dir "Удачи в дальнейшей жизни."
    mc "Спасибо."
    mc "До свидания."
    dir "И ещё..."
    mc "???"
    dir "Я слышал, что у тебя есть проблемы с социализацией среди одноклассников."
    dir "В новой школе она может быть решена, если ты приложишь к этому силу."
    mc "...угу."
    dir "Пообещай, что ты это сделаешь."
    mc "...я найду себе друзей в новой школе."
    dir "У тебя начнётся новая жизнь."
    mc "У меня начинётся новая жизнь."
    call window_close

    pause 1.0

    play noise_1 train_moving_2 fadein 6.0
    queue noise_1 train_doors_open_inside
    queue noise_1 train_waiting

    pause 24.5
    show screen new_day(episode) with dissolve_scene_full
    play noise_2 metro_station_noise fadein 6.0
    play sound mc_steps
    stop noise_1 fadeout 4.0

    pause 4.0

    hide screen new_day
    scene bg niigata station niigata platform 2
    with dissolve_scene_full
    pause 1.0
    play sound mc_inhale
    pause 1.5
    call window_open
    "Наконец-то я приехал..."
    "..."
    "...что-то все поезда встряли."
    "И мой тоже."

    scene bg niigata station niigata platform 1 with dissolve
    pause 0.25
    "Ещё ремонт где-то устроили, грохочат на всю платформу..."
    mc "Ум-м-м..."
    "Так, сколько времени на циферблате?"
    mc "Практически 12 часов..."
    "А голова уже вся в тумане..."
    "Будто её отбойным молотком пробили несколько раз во время поездки."
    "И, конечно, именно сейчас надо что-то там ковырять на станции, стуча своими инструментами мне по мозгам."
    "Другого времени не было?"
    "Хотя когда им ещё этим заниматься, если всё работает чуть ли не круглосуточно..."
    mc "Угх-х-х..."
    "Не могу собраться с мыслями..."
    mc "Так!"
    "Сейчас я спускаюсь в южный выход..."
    "Запрыгиваю в автобус..."
    "И спокойно доезжаю до--{nw}"
    mc "Сайори!" with vpunch
    "Блин..."
    "Для кого ж ещё я второй билет купил?"
    "Ах, но вот абсолютно всегда в любом плане будет один пункт, который отправляет его целиком в помойку."
    "Теперь вместо спокойной поездки до дома нужно сначала откопать Сайори в большой толпе."
    "А потом принимать всем телом и мозгом её позитивное настроение."
    "Учитывая, что я сейчас серьёзно пожёван..."
    "...этот небольшой остаток пути будет длиться для меня долго и «счастливо»."
    mc "Эх, ладно, хватит ныть..."
    "Бросать Сайори я точно не собираюсь."
    "Надо её найти."
    "Вероятно, до сих пор снаружи у выхода сидит."
    "Ну или во внутрь уже зашла..."
    "Короче, пока ей писать не буду: сделаю сюрприз в виде внезапного появления."
    call window_close

    scene black with dissolve_cg
    play sound mc_steps
    pause 1.0
    play noise_1 station_escalator fadein 3.0
    pause 1.0
    play noise_3 train_doors_close
    pause 4.775
    stop noise_2 fadeout 10.0
    stop noise_3
    play sound station_train_departure fadeout 14.0
    pause 15.0
    play noise_2 mc_steps
    stop noise_1 fadeout 3.0
    pause 3.0
    stop noise_2

    call window_open
    scene bg niigata station niigata entrance inside with Dissolve(1.0)
    mc "Хм..."
    "Не думал, что тут так пусто."
    "Здесь же ещё есть встроенный торговый центр, обычно людей огромное количество."
    "..."
    "Нет, не вижу здесь Сайори, всё-таки она снаружи."
    "Надеюсь, там будет так же пусто..."
    call window_close

    scene black with Dissolve(1.0)
    play noise_2 mc_steps
    play noise_3 street_full_noise fadein 10.0
    pause 5.0
    stop noise_2

    call window_open
    scene bg niigata station niigata entrance outside day
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    with dissolve_scene_full
    "Потрясающе, кто бы сомневался..."
    "И как мне искать в такой толпе рыжий шарик с красным бантом?"
    mc "Пф-ф-ф..."
    "Беру свои слова назад."
    "Вряд ли она сейчас сидит на лавочке в таком аншлаге."
    "Возможно, стоит где-то рядом, чтобы не пропустить меня."
    "Где же ты, Сайори?..."
    window hide

    pause 7.0
    show sayori turned casual dist cm oe zorder 1:
        xcenter 350 yanchor 1.0 ypos 0.82
        on show:
            zoom 0.73*0.71 alpha 0.0
            easein 0.25 zoom 0.73*0.73 alpha 1.0
        on hide:
            easein 0.25 zoom 0.73*0.68 alpha 0.0
    pause 1.5

    window auto
    "О, вот она!"
    "Крикнуть?"
    "Но очень не хочется привлекать внимание толпы..."
    "Лучше энергично помашу ей рукой, должна заметить."
    call window_close

    call screen swing_hand

    pause 3.0
    show sayori flus cm oe lup rup:
        easein 0.1 yoffset -20
        easeout 0.1 yoffset 0
    pause 1.25
    show sayori ldown rdown
    hide sayori
    pause 5.0

    call window_open
    "...и?"
    "Куда она делась?"
    window hide

    pause 5.0

    window auto
    "Издевательство какое-то!"
    "Может быть--{nw}"
    call window_close

    show sayori turned casual lup rup mc e4c zorder 3 at movein_hugs
    pause 0.3
    play sound ram_attack
    scene white
    pause 0.1
    scene black
    show particle_star
    with dissolve

    call window_open
    mc "{sc=3}АРГХ-Х-Х!--{/sc}{nw}" with vpunch
    s "{sc=2}А-а-а-а-а!!!{/sc}"
    s "{sc=2}Ты в порядке?!{/sc}"
    mc "М-м-м-м, голова..."

    scene bg niigata station niigata entrance outside day
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    show sayori turned casual lup rup vsur cm oe at t11 zorder 3
    with dissolve_scene_full
    play music t2 fadein 2.0
    mc "Ты меня так до инфаркта доведёшь..."
    mc "Предупреждать надо!"
    show sayori tap casual pout om oe at s11
    s "Злюка!"
    show sayori cm
    mc "После такого -- неудивительно!"
    "Тьфу..."
    "Сделал сюрприз, называется."
    "Разве так встречают приезжих?"
    "Хотя этот удар меня больше взбодрил, чем принёс дискомфорт."
    "Да и вообще, мы наконец-то снова встретились вживую за последние полгода!"
    "С ума сойти, столько времени прошло..."
    "Так что глупо злиться на это недоразумение."
    show sayori nerv m4 oe
    s "...прости."
    show sayori m2
    mc "Ай, проехали."
    "Сердце на куски разрывается от одного её взгляда."
    "Так и хочется погладить по голове."
    show sayori cm
    mc "Но ты заслужила одно наказание, которое я сейчас применю по всей строгости."
    call window_close

    hide sayori
    show sayori tap casual nerv cm oe at e11 zorder 3
    with dissolve
    pause 2.0
    show sayori turned casual lsur om oe n3 with dissolve
    pause 2.0
    hide sayori
    show sayori turned casual lsur cm oe n3 at i11 zorder 3
    with dissolve
    pause 0.5

    call window_open
    mc "Всё, достаточно."
    show sayori happ om e4c lup rup n1 at h11
    s "Мало!"
    show sayori cm
    mc "Лопнешь!"
    show sayori mc at h11
    s "Не лопну!"
    show sayori cm
    mc "Откуда у тебя столько энергии?"
    show sayori om oe ldown rdown
    s "У меня её всегда много!"
    show sayori cm
    "Ха, этот разговор может длиться вечно."
    "Я бы его, конечно, поддержал..."
    show sayori e1b
    "Но мои ноги скоро выйдут из этого чата."
    show sayori oe
    mc "Давай лучше закончим мой «переезд»."
    show sayori laug cm oe
    mc "Иначе тебе придётся нести обратно не только себя, но и меня."
    show sayori om ce
    s "Размечтался!"
    show sayori oe
    s "Ты быстрее доползёшь до дома, чем я тебя донесу!"
    show sayori cm
    mc "Какая тяжёлая у меня жизнь: не на кого положиться..."
    "Иронично, но ведь, не будь Сайори и моих родителей, так бы и вышло."
    show sayori om ce
    s "Ладно, не помирай!"
    show sayori happ om oe
    s "Следующая станция -- «Автобусная остановка»!"
    show sayori cm
    mc "Скорее бы."
    play sound sayori_hide_fast
    show sayori ce at lhide
    hide sayori
    "АПФ!"
    mc "Не так же быстро!"
    call window_close

    call plot_transition

    call window_open
    scene bg niigata station niigata bus information
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    show sayori turned casual happ cm ce zorder 3 at t11
    with wipeleft_scene
    mc "Сайо..."
    show sayori oe
    mc "...ри..."
    show sayori neut cm oe
    mc "Я..."
    show sayori curi cm oe
    mc "...так, блин..."
    show sayori vsur cm oe lclose rclose
    mc "...сдохну..."
    mc "...а-а-а-а..."
    "Отдышаться...{w}срочно..."
    call window_close

    pause 4.0
    show sayori pout cm oe
    pause 3.0
    show sayori doub cm oe
    pause 3.0
    show sayori om
    stop music
    play music_none_loop music_stop

    call window_open
    s "Ты вообще не занимался пробежками с того обещания?"
    show sayori cm
    mc "Э-э...{w}ой..."
    play sound flashback_start
    stop noise_3

    scene white
    scene black with dissolve
    $ quick_menu = False
    scene bg residential_day:
        blur 15.0
    with dissolve_scene_full
    centered "~полгода назад..."
    $ quick_menu = True
    play music sayori_flashback fadein 2.0

    scene bg residential_day
    show gray zorder 3:
        alpha 0.25
    show vignette zorder 4:
        alpha 0.5
    show sayori turned happ cm oe school_bag at t11
    with dissolve
    mc "Кстати, у вас в школе недавно же был фестиваль спорта?"
    mc "Как там его..."
    show sayori om ce lup rup at h11
    s "Ундокай!"
    show sayori cm ldown rdown
    mc "Да, точно."
    show sayori oe
    mc "Вы какое место заняли?"
    show sayori mc ce lup rup at h11
    s "Первое!"
    show sayori om oe lup
    s "Мы шли наравне с классом, который был на год младше нас."
    show sayori ldown
    s "Но мы оторвались от них в эстафете."
    show sayori mc ce lup rup at h11
    s "Я пробежала свой отрезок быстрее всех!"
    show sayori om oe rdown
    s "Даже судьи были сильно удивлены!"
    show sayori cm ldown
    mc "Ну и ну..."
    mc "Не думал, что ты у нас такая скоростная."
    show sayori tap nerv om oe school_bag at s11
    s "Я просто люблю бегать."
    show sayori turned happ om oe school_bag at t11
    s "Знаешь, ты тоже так можешь!"
    show sayori cm
    mc "Зачем оно мне?"
    show sayori tap nerv om oe school_bag at s11
    s "Бегать вместе со мной, конечно же!"
    s "И заодно укрепить своё здоровье."
    show sayori pout cm oe
    s "А то ты любишь сидеть за своим компьютером, ковыряться в каких-то строках с непонятными буквами..."
    mc "Эй, вообще-то, во-первых, это называется изучение программного языка."
    mc "А во-вторых, я периодически прогуливаюсь и хожу по делам."
    mc "Тем более к тебе, вот, иногда приезжаю."
    show sayori turned pout om e1a school_bag at h11
    s "Этого всё равно мало!"
    show sayori cm
    mc "Неа, этого выше крыши хватает."
    show sayori om
    s "Ты даже не пробовал заниматься пробежками!"
    show sayori neut cm oe
    mc "Нет желания и времени, честно..."
    show sayori tap nerv m4 oe school_bag at s11
    s "...бегать со мной по утрам?"
    show sayori cm
    mc "..."
    mc "......"
    mc "Пф-ф-ф-ф-ф..."
    show sayori neut cm oe
    mc "Хорошо-хорошо, я попробую один раз."
    show sayori turned happ mc ce lup rup school_bag at h11
    s "УРА!"
    show sayori cm
    mc "Стоп..."
    show sayori neut cm oe ldown rdown
    mc "Мне же скоро уезжать обратно, буквально завтра."
    show sayori tap pout cm oe school_bag at s11
    s "У-у-у-у-у, я только обрадовалась..."
    mc "Что поделать--{nw}"
    show sayori turned happ om oe school_bag at t11
    s "Значит, попробуешь без меня!" with vpunch
    show sayori ce
    s "Заодно будешь подготовленным к совместным пробежкам!"
    show sayori cm
    mc "А-а-а-а-а--{nw}"
    show sayori sedu mb oe
    s "Ты уже согласился, даже не пытайся этого избежать."
    show sayori cm
    mc "Я соглашался на бег с тобой, а не с собой."
    show sayori happ om oe
    s "Ну так это будет тренировка!"
    show sayori neut om oe b1d
    s "А когда приедешь снова, обязательно проверю тебя на практике!"
    show sayori cm
    mc "Ё-моё, Сайори..."
    show sayori happ cm oe -b1d
    mc "С тобой опасно договариваться."
    show sayori om ce
    s "Э-хе-хе~"
    show sayori cm
    play sound flashback_end
    stop music fadeout 0.5

    scene white
    scene black with dissolve
    play noise_4 street_full_noise fadein 2.0

    scene bg niigata station niigata bus information
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    show sayori turned casual doub cm oe lclose rclose zorder 3 at i11
    with dissolve
    mc "..."
    s "..."
    "..."
    show sayori neut cm oe
    mc "Подожди..."
    mc "Сколько сейчас времени?"
    show sayori curi mh oe
    s "А-а..."
    show sayori om
    s "На табло 12:08."
    show sayori cm
    mc "12:08..."
    show sayori neut cm oe
    mc "А билеты у меня...{w}по-моему, на 10 минут..."
    show sayori om b1f
    s "Какие билеты?"
    show sayori cm
    "А, вон он где стоит!"
    show sayori curi cm oe brow
    mc "Нет времени объяснять!"
    mc "Бери мою руку!"
    show sayori om
    s "Чего?--{nw}"

    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        ease 0.5 zoom 2.5 yoffset 370

    show sayori e2d
    s "Что ты делаешь--{nw}"
    show sayori pani om ce
    s "И-И-И-И-И-И!!!{nw}" with vpunch
    play sound sayori_hide_fast
    call window_close

    scene black with wipeleft_scene
    play noise_2 mc_steps_outside_run
    play noise_3 sayori_steps_run
    pause 1.0
    play noise_1 bus_waiting fadein 3.0
    pause 1.0
    stop noise_4 fadeout 7.0

    scene bg niigata station niigata bus waiting at run_center
    with wipeleft_scene
    pause 2.0

    scene black with wipeleft_scene
    stop noise_2
    stop noise_3
    pause 0.5
    play sound bus_doors
    stop noise_1 fadeout 3.5
    pause 4.0
    play noise_3 bus_inside_1 fadein 4.0

    call window_open
    scene bg bus
    show sayori turned casual neut cm oe lclose rclose at e22
    with dissolve_scene_full
    mc "Фу-у-ух..."
    "Бедные мои ноги..."
    show sayori om
    s "То есть ты купил для меня электронный билет на автобус?"
    show sayori cm
    mc "Конечно."
    mc "Или ты хочешь сказать, что пешком до станции шла?"
    show sayori om e1b
    s "Пешком."
    show sayori cm
    mc "Ё-моё..."
    "Хотя у неё столько энергии..."
    show sayori om oe
    s "Так ты вообще не занимался пробежками?"
    s "А то сейчас слишком быстро выдохся..."
    show sayori cm
    mc "...ну да, извини."
    mc "У меня была куча дел."
    mc "А ещё оформление документов на перевод в вашу школу."
    mc "В общем, ужас..."
    show sayori om
    s "Понятно."
    show sayori cm
    "Это правда."
    "...но я лучше умолчу тот факт, что банально про них забыл."
    show sayori dist om oe
    s "Я, в принципе, так и думала..."
    show sayori cm
    mc "Сайори, это не повод для трагедии."
    mc "Кто нам мешает начать бегать по утрам в ближайшее время?"
    show sayori anno om oe
    s "Снова пообещаешь и ничего не сделаешь?"
    show sayori cm
    mc "В тот раз я был занят."
    mc "В этот я свободен...{w}пока что."
    show sayori om
    s "Честно?"
    show sayori cm
    mc "Куда уж честнее..."
    show sayori neut cm oe
    mc "Особенно с мыслью, что ты живёшь в доме напротив."
    mc "А я же ведь один."
    mc "Вот не выйду один раз на пробежку, и больше меня никто не увидит."
    mc "А последнее, что я увижу перед своей смертью в кровати..."
    show sayori laug cm oe
    mc "...это Мистера Коровку."
    show sayori om ce
    s "Всё-всё, я тебе верю!"
    show sayori happ om oe
    s "Когда начнём?"
    show sayori cm
    mc "Как резко!"
    mc "Ну не прямо сейчас же..."
    show sayori om
    s "Тогда давай завтра?"
    show sayori cm
    "Я уже жалею о переезде..."
    "Это конец моей спокойной жизни."
    mc "Так сразу?"
    show sayori doub om oe
    s "Ты что-то имеешь против?"
    show sayori cm
    mc "...нет."
    show sayori happ om ce
    s "Отлично, завтра утром приду за тобой!"
    show sayori cm
    mc "Будто ты меня похитить собираешься."
    show sayori om
    s "В этом нет смысла."
    s "Ты и так рядом живёшь."
    show sayori happ cm oe
    mc "Да-а..."
    show sayori e1b
    "\"Рядом живёшь\", \"рядом живёшь\"..."
    "Я ещё до дома не доехал."
    "А тут уже наполеоновские, то есть сайоривские планы..."
    show sayori neut cm e1b
    call window_close

    pause 4.0
    show sayori dist cm oe
    pause 2.0

    call window_open
    show sayori om
    s "Знаешь, пока я тебя ждала, меня сморило..."
    s "...и я немного вымоталась."
    show sayori cm
    "Целый час торчать в шумной толпе, так ещё и в ясную погоду, естественно."
    mc "Бывает."
    window hide

    pause 5.0

    window auto
    show sayori mg e1a b1a n3
    s "Я..."
    show sayori oe -b1a
    s "Ну..."
    show sayori cm ce
    s "...м-м-м..."
    show sayori mg e1a b1a
    s "Можно я посплю у тебя на плече?"
    show sayori me
    mc "Когда угодно."
    show sayori mg ce -b1a
    s "Спасибо..."
    show sayori cm
    window hide

    pause 5.0

    window auto
    "Хм..."
    "Даже у такой батарейки, как Сайори, может наступить разрядка."
    "Всё-таки я рад, что она мой друг."
    "Без неё моя жизнь была бы более «серой» и тягостной, что бы я ни думал..."
    window hide

    pause 5.0

    window auto
    "Так задремать снова захотелось..."
    "...но нам осталось-то ехать примерно 5 минут."
    "Ай, ладно, прикрою глаза ненадолго."
    call window_close

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    stop noise_3 fadeout 6.0

    pause 6.0

    hide black onlayer front
    scene black

    show layer master

    pause 3.0
    play noise_3 bus_inside_2 fadein 4.0
    pause 33.402
    stop noise_3
    play noise_4 bus_waiting fadein 4.0
    play sound bus_doors
    play noise_3 street_suburban_noise fadein 4.0
    pause 4.0
    play noise_1 mc_steps
    play noise_2 sayori_steps
    pause 4.0
    stop noise_1
    stop noise_2
    play sound bus_doors
    pause 4.0
    stop noise_4 fadeout 2.0
    play sound bus_departure fadein 0.5
    pause 7.0

    call window_open
    scene bg niigata shelter bus
    show sayori turned casual happ cm oe at t11
    with dissolve_scene_full
    mc "Умф-ф-ф..."
    "Так, мы...{w}неужели...{w}в нашем районе Хига{image=accent_low_register}{space=-15}ши..."
    show sayori neut cm oe
    "Осталась пройти ещё немного, и я торжественно грохнусь в кровать."
    show sayori om
    s "Макс."
    show sayori cm
    mc "А?"
    show sayori laug om oe
    s "Хватит витать в облаках!"
    show sayori ce
    s "Или ты уже в предвкушении мягкой постели?"
    show sayori cm
    mc "Как ты угадала?"
    show sayori happ om ce lup rup at h11
    s "Я же твой друг, как ни крути!"
    show sayori cm oe ldown rdown
    mc "Ха, ладно, пошли."

    scene bg niigata street suburban 2 day
    show sayori turned casual happ cm e1b at t22
    with wipeleft_scene
    show sayori oe
    mc "Сайори, вопрос..."
    show sayori om
    s "Да?"
    show sayori neut cm oe
    mc "А ты в основном как бегаешь?"
    show sayori om oe b1f
    s "В каком плане?"
    show sayori cm
    mc "Ну, конкретный маршрут по району, во сколько начинаешь, сколько времени уходит..."
    show sayori -b1f
    mc "Просто хочу заранее узнать, чтобы не было всяких казусов."
    show sayori happ om oe rup
    s "Обычно в свободные дни я выхожу в 7 утра..."
    "Я в это время сплю без задних ног."
    s "...и бегаю в свободном и спокойном темпе целый час."
    show sayori cm rdown
    mc "Угу..."
    show sayori om
    s "Пробегаю весь район по кругу, обязательно прохожу через небольшой парк рядом."
    show sayori cm
    "А, да, я там периодически бывал, уютное место."
    show sayori curi om e2b
    s "Что ещё..."
    show sayori cm
    s "...м-м-м..."
    show sayori happ om ce lup rup at h22
    s "Всё!"
    show sayori cm oe ldown rdown
    mc "А по рабочим дням?"
    show sayori neut cm oe
    mc "Когда, например, учишься?"
    show sayori happ om oe
    s "Выхожу на час раньше или приходится пропускать."
    show sayori cm
    "Да, глупый вопрос."

    scene bg niigata street suburban 1 day
    show sayori turned casual happ cm oe at t22
    with wipeleft_scene
    mc "Придётся мне вставать в выходные на час раньше..."
    show sayori om ce
    s "Быстро привыкнешь!"
    show sayori cm
    mc "Не знаю..."
    show sayori om oe lup
    s "Пробежки дают хороший заряд бодрости."
    show sayori ldown rup
    s "А также поддерживают твоё тело в хорошем физическом состоянии."
    show sayori cm rdown
    mc "...если грамотно этим заниматься."
    show sayori happ om ce lup rup at h22
    s "Я тебя научу!"
    show sayori cm ldown rdown
    mc "Да, верю-верю."

    scene bg house
    show sayori turned casual happ cm oe at t22 zorder 2
    with wipeleft_scene
    mc "Кажется, пришли."
    show sayori flus om oe
    s "Уже?"
    show sayori cm
    "В смысле, \"уже\"?"
    "Мы сюда целую вечность тащились."
    mc "Ага."
    $ sm_name = _("Мама Сайори")
    $ sd_name = _("Отец Сайори")
    show sayori_mom home_clothes happ cm oe at t21 zorder 1
    pause 0.2
    play music t2 fadein 3.0
    show sayori_mom om rhip
    show sayori lsur cm oe
    sm "Ты наконец-то вернулась, дорогая?"
    show sayori_mom cm
    show sayori happ om e4c lup rup at h22
    s "Мама!"
    show sayori_mom ce rdown at t42
    show sayori cm at t11
    pause 0.5
    "Прошло всего лишь полдня..."
    "А такое чувство, будто они год не виделись."
    if persistent.add_random_menu == 3:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()
    show sayori_dad happ cm oe at t22
    pause 0.2
    show sayori_dad om
    show sayori flus cm oe
    sd "Ха-ха-ха!"
    show sayori_mom oe
    show sayori om e4c at h11
    show sayori_dad cm
    s "Папа?!"
    show sayori_mom laug cm oe
    show sayori cm oe
    show sayori_dad om eb
    sd "Дайте я тоже присусежусь и обниму свою любимую жену и дочурку!"
    show sayori_mom ce
    show sayori laug om ce
    show sayori_dad cm at t43
    pause 0.5
    s "Хи-и-и-и!!!"
    show sayori_mom om
    show sayori cm
    sm "А-ха-ха!"
    show sayori_mom cm
    "Весело."
    "Я здесь явно лишний."
    "Ощущаю себя дурачком."
    "..."
    "Люди, я, конечно, понимаю, что вы друг друга сильно любите, но можно мне пойти домой?"
    show sayori_mom om at t31
    show sayori happ cm ce ldown rdown at t32
    show sayori_dad at t33
    sm "Всё-всё, хватит."
    show sayori_mom happ om oe rhip
    show sayori oe
    show sayori_dad oe
    sm "Здравствуй, Макс!"
    show sayori_mom cm
    show sayori_dad om
    sd "Привет."
    show sayori_dad cm
    mc "Здравствуйте, э-э-э..."
    show sayori neut cm oe
    mc "...простите, я снова ваши имена забыл..."
    $ sm_name = _("Юко-сан")
    $ sd_name = _("Мамору-сан")
    show sayori angr om oe
    s "Ю{image=accent_high_register}{space=-15}ко-сан -- мама, Мамо{image=accent_low_register}{space=-15}ру-сан -- папа, Макс!"
    s "Уже полгода дружишь, а всё запомнить не можешь!"
    show sayori cm
    mc "Ну извините меня, простого смертного, у которого и так голова ни к чёрту."
    show sayori anno cm ce
    show sayori_dad om
    sd "Ха-ха-ха, с Сайори не забалуешь."
    show sayori_mom om lpoint
    show sayori laug cm oe
    show sayori_dad cm
    sm "Смотрю, моё жизнерадостное солнышко доставило тебя до дома в целости и сохранности?"
    show sayori_mom cm ce ldown
    show sayori tap casual nerv om oe at s32
    s "Ма-а-ам..."
    show sayori_mom oe
    show sayori turned casual happ cm ce at t32
    mc "Да, Сайори выполнила свою задачу на все 100 процентов."
    show sayori_mom om ce
    sm "Ха-ха, рада слышать!"
    show sayori_mom cm
    show sayori_dad om eb
    sd "В этом она у нас молодчинка!"
    show sayori_dad cm
    "Сайори от своей матери практически ничем не отличается."
    show sayori oe
    "Разве что одеждой, возрастом и ростом."
    show sayori_mom oe
    show sayori neut cm oe
    show sayori_dad oe
    "Ну и немного тембором голоса."
    show sayori_mom neut cm oe
    show sayori om
    show sayori_dad neut cm oe
    s "Папа, ты снова в костюме?"
    show sayori sad om oe
    show sayori_dad sad cm oe
    s "Опять уедешь в командировку?"
    show sayori cm
    show sayori_dad om
    sd "Извини, лучик, но я срочно понадобился на работе."
    show sayori worr om oe
    show sayori_dad cm
    s "Понятно..."
    show sayori_mom happ cm oe
    show sayori cm
    show sayori_dad happ om oe
    sd "Да ладно тебе, не расстраивайся!"
    show sayori neut cm oe
    sd "Уеду всего на пару недель."
    show sayori e1b
    sd "Не успеешь соскучиться, как я уже буду дома."
    show sayori om
    show sayori_dad cm
    s "Надеюсь..."
    show sayori cm oe
    mc "Ладно, вы уж меня извините, но мне нужно завершить свой переезд до конца."
    show sayori sad cm oe
    mc "Разгрузиться, окончательно обустроиться..."
    show sayori_dad om
    sd "Да, само собой."
    show sayori om
    show sayori_dad cm
    s "Уже прощаться?..."
    show sayori cm
    mc "Разлука до утра -- не приговор."
    show sayori_mom om rhip
    show sayori neut cm oe
    sm "Солнышко, ты же с ним каждый день будешь видеться!"
    show sayori_mom ce lpoint
    show sayori happ cm oe
    sm "К тому же вы ещё вместе будете бегать по утрам."
    show sayori_mom cm ldown
    show sayori om
    s "Да, я с ним уже договорилась!"
    show sayori cm
    "ВОТ, Я ЖЕ ГОВОРИЛ!"
    "Она манипулятор!"
    show sayori_mom oe
    show sayori neut cm oe
    show sayori_dad om eb
    sd "Хо-хо, боюсь представить, как вы заниматься будете!"
    show sayori_dad oe
    sd "Макс, если что, сильно не усердствуй."
    show sayori_mom laug cm oe
    show sayori laug cm oe
    sd "Наша ракета успеет пролететь целый круг по земной орбите и подхватить тебя на втором."
    show sayori_mom ce
    show sayori om
    show sayori_dad cm
    s "Па-а-ап!"
    show sayori cm
    mc "Ха-ха-ха, ладно..."
    show sayori_mom happ cm oe
    show sayori happ om oe
    s "Завтра утром приду!"
    show sayori cm
    mc "Угу, постараюсь проснуться пораньше."
    show sayori_mom om lpoint
    sm "Всё, не будем тебя задерживать."
    show sayori_mom ce ldown
    sm "До встречи!"
    show sayori_mom cm
    show sayori_dad om
    sd "Пока!"
    show sayori om ce
    show sayori_dad cm
    s "До завтра!"
    show sayori cm
    mc "До завтра!"
    call window_close

    stop music fadeout 3.0
    show sayori_mom rdown at thide
    hide sayori_mom
    show sayori at thide
    hide sayori
    show sayori_dad at thide
    hide sayori_dad
    pause 1.5

    call window_open
    scene black with wipeleft_scene
    "Интересно, насколько далеко вперёд распланирована моя жизнь без моего же ведома?"

    scene bg residential_day with wipeleft_scene
    "Даже не верится..."
    "Остались считаные шаги..."
    call window_close

    scene black with dissolve_scene_full
    play noise_1 mc_steps_outside
    pause 6.0
    stop noise_1
    play sound house_door_open
    pause 1.227
    stop noise_3 fadeout 4.0
    play noise_1 mc_steps_outside
    pause 2.0
    stop noise_1
    play sound house_door_close

    call window_open
    scene bg mc house hallway day with dissolve_scene_full
    "..."
    "Тишина..."
    "Неужели..."
    mc "...я дома?"
    "ДА!" with vpunch
    "Так бы прокричали мои ноги, если бы умели говорить."
    "Но нужно сделать ещё пару рывков."
    "Сначала разгрузить свою наплечную сумку и переодеться..."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 3.0
    stop noise_1
    play sound bag
    pause 11.144
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1
    play sound closet_open
    pause 1.0

    call window_open
    scene bg bedroom with dissolve
    "Блин, как будто специально моя спальня с гардеробом расположена на втором этаже."
    "Чтобы я окончательно умер, ага..."
    "Ладно, приступим к переодеванию."
    call window_close

    scene black with dissolve
    pause 0.25
    play sound wardrobe_door_open
    pause 1.802
    play sound mc_dressing_up
    pause 7.984
    play sound wardrobe_door_close
    pause 2.270

    call window_open
    scene bg bedroom with dissolve
    "Ха, довольно быстро."
    "Одна из причин, почему я люблю тёплую погоду."
    "Что ж, теперь туалет..."
    "Не сказать, что сильно хочется, но я сюда достаточно долго тащился."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    "Хм..."
    "А чем я займусь, когда со всем закончу?"
    "Можно было бы что-нибудь глянуть из видео, благо там всегда есть что-то интересное."
    "Хотя в последнее время с ними очень туго..."
    "Когда образуется нечастое свободное время, то видосы, как назло, иногда то отсутствуют, то выпускаются с различными задержками."
    "Или вообще в этот день не выходят из-за «выходного» у автора или ещё какой-либо причины."
    "Издевательство же!"
    "Не иначе..."
    "Ох, блин!"
    "Надо ещё отписаться о приезде."
    "Чуть из головы не вылетело."
    call window_close

    play noise_1 toilet
    pause 5.4
    play sound closet_open
    pause 1.75
    play sound closet_close
    stop noise_1
    pause 2.0
    play noise_1 mc_steps_house
    pause 2.0
    stop noise_1
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    scene bg mc house bathroom day with dissolve
    "О, да..."
    "Моя ванная в стиле «минимализм», где количество средств личной гигиены каждого вида варьируется от одной до двух штук..."
    "Причём этих видов тоже мало."
    play noise_1 sink_open
    "Но зато всё на своих местах."
    "Обожаю чёткий порядок."
    "Никогда не любил бардак: он всегда режет глаз, не говоря уже о том, как неудобно пользоваться в нём вещами."
    "А ведь странно, что, когда у одних это чувство вырабатывается путём долгого и упорного труда, у меня оно уже было чуть ли не с детства."
    "Помню, очень не любил разбрасываться игрушками где попало..."
    "Всегда испытывал чувство стыда за причинённые ими неудобства."
    stop noise_1
    play sound sink_close
    "А ещё стыдился за то, что родители тратили на них деньги."
    "Потому что мне многого было не надо: я и так понимал, что со всем наиграться не смогу."
    "Да, я понимал, что меня хотят порадовать, но...{w}всё равно..."
    mc "Так..."
    "Что там дальше?"
    "А, надо поесть."
    "Дома пусто, но я принёс кое-что с собой..."
    "Завтра обязательно схожу в магазин."
    "...в любом случае живот даст о себе знать."
    call window_close

    scene black with dissolve
    pause 0.25
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0
    play noise_1 mc_steps_house
    pause 4.0
    stop noise_1

    call window_open
    scene bg kitchen with dissolve
    "А с собой я притащил...{w}полуфабрикат в пластиковом лотке в виде пюре и котлеты."
    "И то один..."
    mc "Да здравствует самостоятельная жизнь."
    "Ладно, пару раз проткнуть ножом плёнку и..."
    "..."
    "Какой он объёмный, а..."
    mc "Лезь в микроволновку."
    mc "Лезь в эту чёртову микроволновку, хренов ты лоток!"
    "..."
    "Фу, ура, втиснул."
    "Поставлю на пару минут."
    call window_close

    play noise_1 microwave_warming_up
    pause 8.0

    call window_open
    "Чёрт, сообщение..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = False
        clock = (15, 2)

    phone discussion "mc_mcm_chat"
    "А ещё вай-фай..."
    "Хотя бы не мобильный Интернет, ха-ха."
    "Зря здесь роутер устанавливали?"
    window hide

    call phone_status_bar_button('wifi', disable = False)

    phone discussion "mc_mcm_chat":
        "mc" "Я приехал. Всё в порядке."
    "Ну, мне больше нечего написать."
    "Думаю, достаточно."
    "Отрублюсь-ка я от вай-фая на всякий случай..."
    window hide

    call phone_status_bar_button('wifi', disable = True)

    phone end discussion transition

    call skip_block_off
    play music mc_house_tired fadein 3.0
    "Может быть, я слишком безэмоционален?"
    "Нет, эмоции у меня есть, с ними всё в порядке."
    "Но они будто перекрываются на каком-то начальном уровне..."
    "Будто их сдерживают массивные гермодвери."
    "А если так подумать, зачем мне эти эмоции?"
    "Ничего хорошего в моей жизни толком не происходит."
    "Поделиться нечем и не с кем."
    "Разве что с Сайори, но...{w}я не хочу разделять с ней весь этот негативный и скучный маразм."
    "Особенно, когда она умудрилась сохранить со взрослением весь свой оптимизм."
    "Я это потерял быстро."
    "Возможно, из-за отсутствия мотивации, смысла и поддержки."
    "Часто после этого выжирал себя по разным полувесомым и весомым причинам."
    "...а не из-за всякой херни, как это любят делать выпендрёжники для привлечения внимания."
    "Короче, балансировал на грани то ли апатии, то ли чего-то такого..."
    "В те моменты пытался найти того, кто реально меня поймёт, при этом боясь приложить усилия."
    "Потому что останавливал меня страх сделать первый шаг."
    "Честно, зачем стараться строить песочный замок со всеми мелкими деталями, когда его гарантированно смоет к чертям первая прибрежная волна?"
    "И всё-таки я общался через соцсети с одним человеком до Сайори."
    "Уже не помню его имени, давно это было..."
    "Ничего супер-пупер особенного, просто тогда он был примерно на одинаковом со мной уровне во всех аспектах."
    "Общались о чём угодно, развлекались..."
    "В общем, постоянно поддерживали связь, при этом не навязываясь друг другу."
    "Потом я как-то чисто случайно встретил одного психолога."
    "Всё ещё не понимаю, почему он редко, но интересовался мной, как человеком в целом."
    "Ладно, не суть..."
    "Так вот, переписывался с ним часто."
    "Каждый разговор для меня был неким счастьем."
    "Был чем-то даже полезен."
    "Я полностью открылся этому человеку и не был им отвергнут, хотя совершенно не знал, как его зовут."
    "Мы с ним прошли несколько интересных тестов."
    "Он делал у себя какие-то записи."
    "Что-то вроде анкеты на меня."
    "Без всяких личных данных, кроме имени и возраста, естественно."
    "По ходу дела я втянул ещё своего бывшего друга."
    "Или нет...{w}или он меня..."
    "В голове уже такая каша..."
    "...помню, в одном из тестов результат друга вызвал некий диссонанс у психолога, а ещё у его коллег по работе, которым он показывал этот самый результат."
    "В хорошем смысле или в плохом..."
    "Как бы то ни было, с ним он стал работать усиленнее."
    "Ну значит, в хорошем, что тут думать?"
    "Ведь если так прикинуть, то другу это было жизненно необходимо."
    "С ним всё было не очень хорошо в психологическом плане."
    "Он серьёзно нуждался в помощи, хоть и неявно, а я ничего не мог сделать."
    "Но тут началось основное «веселье» всей этой истории: психолог стал часто пропадать."
    "Кое-как мы продолжали тестирования, которые я ждал с нетерпением (спойлер: их было буквально раз, два и обчёлся. Хи-хи-хи с ха-ха-ха)."
    "Потом всё плавно затихло."
    "Мы особо не контактировали друг с другом, не говоря уже о самих тестах."
    "Даже если он и был в сети, он работал с другом."
    "Но однажды психолог вышел со мной на связь и предложил мне писать рецензии в конце каждого дня."
    "В них было всё по эмоциям: как я себя чувствовал, что происходило, моё отношение к этому и так далее..."
    "Разумеется я согласился, потому что цеплялся за любую инициативу с его стороны."
    "Итак, я начал строчить рецензии на каждый день."
    "Писал."
    "Он периодически отвечал."
    "Писал."
    "Ждал ответа."
    "Писал."
    "Потом он стал реже отвечать."
    "Писал."
    "Писал."
    "Тишина."
    "Писал."
    "Писал."
    "Я хотел ответа."
    "Писал."
    "Писал..."
    "Писал......"
    "Ответа не было..."
    "А прошла вся мерзкая на тот момент осень (из-за всяких мелких, но значительных проблем) и часть зимы -- где-то 5 месяцев."
    "Потом, естественно, психолог опять вышел на связь."
    "За это время он успел аж пожениться, переехать со своей семьёй в другую страну, решить множество жизненно важных проблем..."
    "Короче говоря, он тотально занимался личной жизнью."
    "Но, как назло, у моего друга тоже это началось."
    "Появилась девушка, которая его «аннексировала»."
    "После этого буквально за месяц активные и ежедневные разговоры скатились в гробовое молчание."
    "И этот чёртов «друг» даже не умудрился остановить наше общение «официально»."
    "Так было тяжело написать что-то в духе: \"Извини, не до тебя\" или \"Да пошёл ты нахрен, ты мне надоел\"?!"
    "Свинство, твою мать!"
    call window_close

    stop noise_1
    play sound microwave_finish
    pause 10.0

    call window_open
    scene bg kitchen at mc_kitchen_table_alone
    with dissolve
    "И всё это происходило в тот момент, когда я так нуждался в их грёбаном общении."
    "Вот серьёзно, таких плевков от жизни я ещё ни разу не получал."
    "За что?"
    "Что я, блин, сделал, а?!"
    mc "Пф-ф-ф..."
    "...хорошо, даже так, я всё ещё продолжал писать психологу эти рецензии."
    "По инерции."
    "Я уже не хотел видеть его ответы."
    "Я просто строчил стены текстов, потому что привык так делать."
    "То ли мне это помогало, то ли я просто останавливаться не хотел, без понятия."
    "Конечно, психолог продолжал мне отвечать."
    "Редко, без особых действий..."
    "Но его единичные фразы скатывались в некую риторичность, которая мне тогда была на руку."
    "Не было сил и желания реагировать."
    "Итак, уже было начало следующего лета -- ровно целый год писанины рецензий."
    "Внезапно психолог пообещал провести какой-то мотивационный тест или что-то в этом духе."
    "Для меня это было невероятным счастьем."
    "Но перед началом мы с ним разъехались по делам на пару недель: жизнь продолжала вставлять палки в колёса."
    "За время ожидания я навоображал себе кучу всего..."
    "Я очень хотел поучаствовать в этом тестировании."
    "Жаждал."
    play sound semi_finished_product
    pause 2.0
    "Но..."
    "Догадайтесь с трёх раз."
    "Раз...{w=1.0}два...{w=1.0}три!{w=1.0}{nw}"
    "Правильно!"
    "Стоило только мне вернуться, как я быстро осознал, что абсолютно НИЧЕГО не произошло."
    "Психолог снова «умер»."
    "Друг окончательно «сдох» вслед за ним."
    "Я остался один."
    "Снова."
    "...обожаю эту грёбаную жизнь."
    "С таких выкрутасов мой социальный недоголод достиг такого уровня, что окончательно трансформировался в социальное отторжение."
    "Я всё ещё зачем-то писал рецензии."
    "Но с каждым разом я каменел, мерзел и становился менее эмоциональным."
    "Я стал превращаться в другое существо, которому было плевать на прошлые связи и которого выматывали эти социальные контакты."
    "Я полюбил одиночество."
    "Я стал более стойким и самостоятельным."
    "Тем более тогда я увлёкся изучением языка {color=#fc7e23}Python{/color}...{w}с закосом написания на нём визуальных новелл."
    "Без понятия, откуда у меня возникло желание возиться с чем-то подобным..."
    "Нет, я сам язык так ещё изучал, чтобы в дальнейшем связать с ним мою будущую профессию (уж больно мне он понравился)."
    "По крайней мере, каждый раз, когда я садился, изучал синтаксисы и писал код, пытаясь создать собственную игру, я получал моральное удовольствие."
    "Это была единственная вещь, которая хоть как-то помогала мне расслабиться в этой жизни."
    "Всё остальное меня просто изматывало в той или иной степени."
    "Мод, к слову, я делал на базе одной «необычной» новеллы."
    "Как там она называется?..."
    "..."
    "Чёрт, не помню."
    "Да и мод, в целом, тоже."
    "Вышел коротким и невзрачным."
    "Зря время и силы потратил."
    "...но он хотя бы работоспособен, ха-ха..."
    "Сейчас я перестал этим заниматься, остаётся всё меньше времени на нечто подобное, но сам язык, как и говорил, не бросил."
    "Куда ж время всё уходит..."
    "..."
    "Блин, что-то я уехал от темы..."
    "А, вспомнил!"
    "Где-то ещё через полгода психолог с другом объявились."
    "И тут я им высказал всё, что накопил за весь период тишины."
    "Было...{w}забавно, да...{w}смотреть, как они нелепо пытались уладить ситуацию."
    "В итоге, я их послал откровенно далеко и навсегда, тем самым разорвав с ними связь."
    "С меня хватит!"
    "К черту все эти отношения и дружбы!"
    "Одни только нервы от них и сплошное дерьмо, которое обязательно всплывёт и испоганит твою жизнь."
    "Единственным исключением является лишь Сайори, с которой я познакомился где-то через пару месяцев после всего вышесказанного, когда стал сюда периодически приезжать."
    "Это было примерно...{w}ближе к середине второго года старшей школы."
    "Не так давно, если подумать..."
    "Короче, ничего я ей про это не рассказывал, нафиг надо?"
    "Да и она не интересовалась, справедливости ради."
    "..."
    "Хм, с ней есть одна странность..."
    "Несмотря на её чрезмерную радость и активность, она никогда меня не выматывала."
    "Парадокс?"
    "В общем, мы стали прекрасно общаться."
    "Сайори постоянно подпитывает меня своей энергией, которой иногда не хватает."
    "..."
    "Хм..."
    "Мы уже общаемся так, будто дружим с самого детства."
    "Интересно, как бы всё сложилось, если бы Сайори была моим другом {b}именно{/b} с детства?"
    "Были бы у неё другие чувства ко мне?"
    "Что-то нечто...{w}большее?"
    "Не знаю..."
    "Вообще у меня никогда не было и нет желания возиться с любовными отношениями."
    "Проблем хватает по горло, люди выматывают..."
    "О..."
    "Я уже всё съел."
    "Чёрт, это я так сильно провалился в себя?!"
    "Сколько можно?!" with vpunch
    "Как это раздражает!"

    scene bg kitchen with dissolve
    play sound trashcan
    pause 4.0
    "Вечно меня переполняют чувства, которые хотят выплеснуться наружу."
    "Вот только никоим образом это не происходит."
    "В итоге, вот, пожалуйста, постоянные провалы в себя."
    "Пока что серьёзных проблем это ещё не приносило..."
    "А может, это вопрос времени?"
    "Ой, да плевать, честно, всё равно никак не исправить."
    stop music fadeout 4.0
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1

    call window_open
    scene bg bedroom with dissolve
    "Всё..."
    "Теперь можно со спокойной душой плюхнуться в кровать и смотреть различные видео (если они, конечно, есть)."
    "Голова никакая, блин..."
    "Уже начинает проступать пульсирующая боль."
    "Ненавижу такое..."
    "Благо она началась конкретно сейчас, а не раньше, иначе бы добила меня ещё на полпути."
    mc "{cps=30}{bt=0.5}Фу-у-у...{/bt}{/cps}"
    "{cps=30}{bt=0.5}...еле на ногах стою...{/bt}{/cps}"
    "{cps=30}{bt=1.0}...а надо ещё до кровати доползти...{/bt}{/cps}"
    "{cps=30}{bt=1.5}...а-а-а-а-а...{/bt}{/cps}"
    call window_close

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    scene black
    hide black onlayer front

    jump prologue_day_2




label prologue_day_2:

    $ episode = _("Пролог\nДень 2")
    $ save_name = episode.replace('\n', '. ')

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_pr_d1.unlocked == False:
        $ ach_pr_d1.unlock()

    pause 7.0
    hide loading_sign_mc with dissolve
    pause 1.0

    play noise_1 sayori_alarm_clock
    pause 4.0

    scene bg bedroom at mc_bed
    show sayori turned cat_shirt happ cm ce at face
    with shake(time=2.0, dist=40)
    play sound ram_attack
    show white:
        alpha 1.0
        linear 0.25 alpha 0
    show sayori pani cm ce lup rup
    show sayori at tfast
    pause 0.3
    play sound fall
    hide sayori with easeoutbottom
    pause 5.75

    scene black
    show screen new_day(episode)
    stop noise_1 fadeout 0.5
    pause 2.0
    hide screen new_day

    call window_open
    scene bg bedroom
    show sayori turned cat_shirt pout cm oe at t11
    with dissolve_scene_full
    call autosave
    mc "Кто ж так друзей будит?!"
    s "..."
    mc "Сайори!"
    s "..."
    mc "Ты будешь со мной разговаривать?"
    s "..."
    mc "...ох, ну извини, я рефлекторно ударил тебя в лоб."
    show sayori worr cm oe
    mc "Потому что будильник был СЛИШКОМ громким."
    show sayori tap nerv m2 oe at s11
    s "...прости."
    mc "В следующий раз буди не так радикально, ладно?"
    show sayori cm e2
    s "Угу..."
    mc "Подожди..."
    show sayori neut cm oe
    mc "А как ты ко мне зашла?"
    show sayori turned happ om oe lup at t11
    s "Ха, сначала я подошла к дому..."
    show sayori ldown
    s "Подумала: если дверь закрыта, то придётся тебе позвонить на телефон и ждать снаружи, ведь дверной звонок тебя не разбудит."
    s "Но перед этим я решила на всякий случай дёрнуть дверь..."
    show sayori ce lup rup at h11
    s "...и она открылась!"
    show sayori cm ldown rdown
    mc "Серьёзно?..."
    "Я так вчера устал, что забыл закрыть входную дверь?..."
    show sayori happ om oe
    s "Зато без проблем тебя разбудила."
    show sayori nerv om oe at s11
    s "Практически..."
    show sayori cm
    mc "Ладно, дай мне хотя бы переодеться..."
    show sayori happ om oe ldown rdown at t11
    s "Хорошо!"
    show sayori cm ce at lhide
    play sound sayori_hide_fast
    hide sayori
    mc "Не надо носиться по дому!"
    s "{size=19}Оке-е-ей!{/size}"
    "Не хватало, чтобы она ещё куда-то врезалась..."
    "Эх, раз всё так быстро началось, то тогда сразу переоденусь во что-нибудь спортивное."
    call window_close

    scene black with dissolve
    pause 0.25
    play sound wardrobe_door_open
    pause 1.802
    play sound mc_dressing_up
    pause 7.984
    play sound wardrobe_door_close
    pause 2.270

    call window_open
    scene bg bedroom with dissolve
    "Спортивные шорты и футболка -- всё в чёрном цвете."
    "Прямо как у Сайори, хе."
    "..."
    "Эй..."
    "Кто вообще бегает в чёрном в ясную погоду?"
    "Ай, да пофиг, другой одежды всё равно нет."
    "Так, теперь надо быстро забежать в туалет, и тогда я буду готов."
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day
    show sayori turned cat_shirt happ cm oe at t11
    with wipeleft_scene
    mc "Всё, я готов."
    show sayori om ce lup rup at h11
    s "Отлично!"
    show sayori oe ldown rdown
    s "Побежим сначала по улочкам в небыстром темпе."
    s "Когда добежим до парка, то там немного ускоримся, а потом передохнём."
    show sayori sedu cm oe
    mc "Надеюсь, «небыстрый темп» по-настоящему небыстрый?"
    show sayori mb
    s "Можешь быть уверен."
    show sayori cm
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

    call window_open
    scene bg residential_day
    show sayori turned cat_shirt happ cm e1b at t11
    with dissolve_scene_full
    "Раннее утро имеет один весомый плюс: солнце ещё не успело всё прогреть, а значит, нет сумасшедшей жары."
    show sayori oe
    mc "Ну что, побежали?"
    play music set_ablaze fadein 1.0
    show sayori mc e4c b2a lup rup at h11
    s "ВПЕРЁД!!!"
    play sound sayori_hide_fast
    show sayori ldown rdown at lhide
    hide sayori
    mc "СТОЙ, КУДА ТЫ РВАНУЛА, ПОДОЖДИ МЕНЯ!"
    play noise_2 mc_steps_outside_run
    play noise_3 sayori_steps_run

    scene bg niigata street suburban 1 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j43
    with wipeleft_scene
    mc "{sc=2}Вот это...{w}я понимаю, пробежка!{/sc}"
    "{sc=2}...вдох-выдох-вдох-выдох...{/sc}"
    show sayori mc
    s "{sc=2}А то!{/sc}"
    show sayori mn
    "{sc=2}Слишком резкое начало после долгого перерыва!{/sc}"
    "{sc=2}Надо выровнить темп, чтобы войти в раж!{/sc}"
    show sayori mc at j11
    s "{sc=2}Не отставай!{/sc}"
    show sayori at thide
    hide sayori
    pause 0.5
    "{sc=2}Блин, я так помру!{/sc}"

    scene bg niigata street suburban 2 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j21
    with wipeleft_scene
    "{sc=2}Пока дыхание в норме, темп поймал...{/sc}"
    mc "{sc=2}Летишь, как пуля!{/sc}"
    show sayori mc
    s "{sc=2}А-ха-ха!{/sc}"
    show sayori mn at j22
    "{sc=2}Держать дыхание!{/sc}"
    "{sc=2}...вдох-выдох-вдох-выдох...{/sc}"
    "{sc=2}Нельзя сбиваться!{/sc}"
    show sayori at thide
    hide sayori
    "{sc=2}И тормозить!{/sc}"

    scene bg niigata street suburban 3 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j11
    with wipeleft_scene
    mc "{sc=3}Пха, горка!{/sc}"
    show sayori mc
    s "{sc=3}Не преграда!{/sc}"
    show sayori mn
    "{sc=3}На что я подписался?!{/sc}"
    "{sc=3}Где медленный темп?!{/sc}"
    show sayori at thide
    hide sayori
    "{sc=3}...вдох-выдох-вдох-выдох...{/sc}"

    scene bg niigata street suburban 4 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j43
    with wipeleft_scene
    mc "{sc=3}Аккуратнее...{w}тут машины!{/sc}"
    "{sc=3}Чёрт, бегать по таким улочкам себе дороже!{/sc}"
    show sayori mc
    s "{sc=3}Рано утром их очень мало!{/sc}"
    s "{sc=3}Мы бежим по «спокойным» улицам!{/sc}"
    show sayori mn
    "{sc=3}Откуда у неё столько дыхания на слова?!{/sc}"
    "{sc=3}...вдох-выдох-вдох-выдох...{/sc}"
    mc "{sc=3}Всё равно!{/sc}"
    show sayori mc
    s "{sc=3}Ок-ке!{/sc}"
    show sayori mn

    scene bg niigata street suburban 5 day at jugging
    show sayori turned cat_shirt mn e4c b2a at j43
    with wipeleft_scene
    mc "{sc=3}Мы уже...{w}ближе к центру?{/sc}"
    show sayori mc
    s "{sc=3}Да!{/sc}"
    s "{sc=3}Ещё километр, и будем в парке!{/sc}"
    show sayori mn
    "{sc=3}ЧЕГО-О-О?!{/sc}"
    show sayori at thide
    hide sayori
    "{sc=3}Я обязательно выживу!{/sc}"

    scene bg niigata street suburban 6 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j21
    with wipeleft_scene
    mc "{sc=3}Ты всегда...{w}бегаешь по...{w}этому маршруту?{/sc}"
    show sayori mc
    s "{sc=3}Да, я к нему привыкла!{/sc}"
    s "{sc=3}Как в первый раз пробежала...{w}так и бегаю!{/sc}"
    show sayori mn
    "{sc=3}А-а-а, тоже начала выдыхаться!{/sc}"
    "{sc=3}Но я дохну быстрее!{/sc}"

    scene bg niigata street suburban 7 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j22
    with wipeleft_scene
    "{sc=3}Мы вообще где?!{/sc}"
    "{sc=3}Я тут ни разу не был!{/sc}"
    mc "{sc=3}Да тут легко...{w}заблудиться!{/sc}"
    show sayori mc
    s "{sc=3}Если знаешь местность...{w}нет!{/sc}"
    show sayori mn
    "{sc=3}...вдох-выдох-вдох-выдох...{/sc}"

    scene bg niigata street suburban 8 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j11
    with wipeleft_scene
    show sayori mc
    s "{sc=3}Скоро выйдем на улицу...{w}откуда до парка рукой\n подать!{/sc}"
    show sayori mn
    mc "{sc=3}Наконец-то!{/sc}"
    "{sc=3}Силы ещё есть, не всё так плохо!{/sc}"
    "{sc=3}Держать дыхание!{/sc}"

    scene bg niigata street suburban 9 day at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j11
    with wipeleft_scene
    show sayori mc
    s "{sc=3}Ещё чуть-чуть!{/sc}"
    show sayori mn
    "{sc=3}Твою ж, точно!{/sc}"
    "{sc=3}Парк на небольшом крутом холме!{/sc}"
    "{sc=3}Помогите!{/sc}"

    scene bg niigata park japanese entrance stairs at jugging
    show sayori turned cat_shirt mn e4c b2a n2 at j22
    with wipeleft_scene
    show sayori mc
    s "{sc=3}Наверх!{/sc}"
    show sayori mn
    show sayori at thide
    hide sayori
    mc "{sc=3}Не споткнись!{/sc}"
    "{sc=3}Cамому бы не навернуться!{/sc}"
    "{sc=3}Лестница меня точно добьёт!{/sc}"

    scene bg niigata park japanese path 1
    show sayori turned cat_shirt mn e4c b2a n2 at j22
    with wipeleft_scene
    stop noise_2
    mc "{sc=3}СТОЯТЬ!{/sc}"
    stop music fadeout 0.5
    stop noise_3
    show sayori vsur cm oe -b2a at h22
    pause 2.0
    mc "{sc=3}Я...{w}всё...{/sc}"
    show sayori sad cm oe
    pause 1.5
    mc "{sc=2}Пха-а-а...{/sc}"
    pause 1.5
    mc "{sc=1}...а-а-а-а-а...{/sc}"
    show sayori om
    s "Я слишком увлеклась..."
    show sayori cm
    mc "{sc=1}Всё...{w}порядок...{w}просто...{w}дых...{/sc}"
    show sayori om
    s "Надо немного походить, иначе сердце загонишь."
    s "А потом передохнём в тени."
    show sayori cm
    mc "{sc=1}Д...{w}давай...{/sc}"
    "Тело кипит..."
    "Сердце бешено стучит..."
    show sayori worr cm oe
    "Нельзя так резко всё делать..."
    show sayori om
    s "Я перестаралась..."
    show sayori cm
    mc "Не бери...{w}в голову..."

    scene bg niigata park japanese path 2
    show sayori turned cat_shirt sad cm oe n2 at t11
    with wipeleft_scene
    mc "Фу-у-у-у-ух..."
    "Тень, ура..."
    show sayori om
    s "Тебе лучше?"
    show sayori cm
    mc "Я только начал остывать..."
    show sayori worr om oe
    s "Просто--{nw}"
    show sayori cm
    mc "Сайори..."
    show sayori sad cm oe
    mc "Хватит загонять себя."
    mc "Буквально остыну минут 5 и буду как новенький..."
    show sayori om
    s "Ты слишком вымотался."
    show sayori cm
    mc "Нет, всё нормально."
    mc "Моя же вина, что не занимался пробежками."
    show sayori worr om oe
    s "Но я реально--{nw}"
    show sayori sad cm oe
    mc "Сайори..."
    "Тактическое поглаживание!"
    call window_close

    show layer master:
        align (0.5, 0.5) anchor (0.5, 0.5)
        easein 1.15 zoom 2.0 yoffset 200
        5.1
        easeout 1.15 zoom 1.0 yoffset 0

    pause 2.25
    show sayori neut cm ce
    pause 2.0
    show sayori n4 with dissolve
    pause 4.0

    call window_open
    mc "Уже лучше?"
    show sayori laug om oe
    s "Эй, это я должна у тебя спрашивать!"
    show sayori cm ce
    mc "Ха-ха!"
    "Другое дело."

    scene bg niigata park japanese path 1
    show sayori turned cat_shirt happ cm oe at t11
    with wipeleft_scene
    show sayori om
    s "Если мы отдохнули, то предлагаю небольшое разнообразие."
    show sayori cm
    mc "Разнообразие?..."
    show sayori om ce lup rup at h11
    s "Да!"
    show sayori oe rdown
    s "Мы пробежим парк разными маршрутами."
    show sayori cm ldown
    mc "Теперь понятно, почему мы сюда вернулись."
    mc "Кстати, я же плохо парк помню..."
    show sayori om rup
    s "Да он небольшой: дорожки тут не такие запутанные, развилок мало."
    show sayori cm rdown
    mc "...хорошо, а где мы тогда встретимся?"
    show sayori om
    s "У другого выхода, который с аркой."
    s "На ней ещё глициния растёт."
    show sayori cm
    "Ну, я точно знаю, что выходов тут всего два..."
    show sayori om
    s "Так что?"
    show sayori cm
    mc "Только это соревнование и ничего больше на сегодня."
    show sayori laug cm oe
    mc "Мой живот уже даёт о себе знать."
    mc "И ноги тоже."
    show sayori om ce
    s "Ок-ке, обратно пойдём пешком."
    show sayori happ om oe
    s "А сейчас твой путь свернёт налево вот на эти камни, по которым ты выйдешь на тропинку, а по ней уже выйдешь на другую тропинку с аркой и прудом, где и прибежишь к выходу!{w=1.0}{nw}"
    show sayori mc e4c b2a lup rup at h11
    s "Вперёд!{w=0.25}{nw}"
    show sayori cm ldown rdown at thide
    hide sayori
    mc "Стой, я ничего не...{w}понял."
    "По этой дорожке налево, потом ещё одна, потом..."
    mc "Ой, тьфу, по месту разберёмся."
    "Надеюсь, что её слова про простоту парка -- правда..."
    call window_close

    scene black with wipeleft_scene
    play noise_2 mc_steps_outside_jogging
    pause 5.0
    stop noise_2

    scene bg niigata park japanese path 4 with dissolve
    pause 0.25
    with vpunch
    pause 0.2

    call window_open
    mc "Блин, чуть не навернулся!"
    "Кто эти булыжники отшлейфовал?!"
    "Скользкие донельзя!"
    "Да, это дорожка не такая дикая, как я думал, но будто здесь огромные толпы шарятся."
    mc "Мда..."
    "Хм, впереди виднеется нормальная дорога..."

    scene bg niigata park japanese path 3
    with wipeleft_scene
    mc "Да, по ней перемещаться в разы проще!"
    "Ещё тут сплошная тень с лёгким ветром..."
    "Бежать здесь явно одно удовольствие."
    "Так, явно отсюда направо..."
    "Там инфраструктуры становится больше, а значит, и выход с аркой там же."
    "Ладно, Сайори права, тут реально тяжело запутаться."
    "Побежали дальше."
    call window_close

    scene black with wipeleft_scene
    play noise_2 mc_steps_outside_jogging
    pause 4.0

    call window_open
    "..."
    "А что, если Сайори уже прибежала и ждёт меня на выходе?"
    mc "Чёрт..."
    "Такое ощущение, что я слишком задержался."
    "Надо ускориться."
    mc "Ай, блин!" with vpunch
    "Опять чуть не навернулся!"
    "Надо смотреть под ноги!"
    "Иначе либо вывихну себе лодыжки, либо полечу обнимать землю!"
    call window_close

    $ m_name = "???"

    scene bg niigata park japanese torii
    show monika forward white_dress happ cm e1b at i11:
        xoffset 50
        linear 1.0 xoffset 0
    show layer master at run_center:
        linear 2.0 yoffset 100
    with dissolve
    pause 1.0
    show monika oe
    pause 0.2
    show monika neut cm oe
    pause 0.2
    show monika s_scream
    pause 0.2
    play sound ram_attack
    stop noise_2
    scene white
    pause 0.1
    scene black
    show particle_star
    with dissolve

    call window_open
    m "{sc=3}А-А-АХ!!!{/sc}{nw}"
    mc "{sc=3}А-А-А-А-А-А--{/sc}{nw}"
    play sound falldown
    mc "{sc=3}АЙ!!!{/sc}"
    m "Ты в порядке?!"
    mc "О-о-о-о-о..."
    "Добегался!"
    mc "Д-да, сейчас встану..."

    scene bg niigata park japanese torii
    show monika forward white_dress shoc cm oe at t11
    with dissolve_scene_full
    play music t8 fadein 3.0
    show monika om
    m "Ты меня напугал!"
    show monika cm
    "Да у меня самого душа в пятки ушла..."
    show monika lsur cm oe
    mc "Ох, прости..."
    mc "Слишком задумался и тебя не заметил..."
    show monika om
    m "Аккуратнее в следующий раз!"
    show monika cm
    mc "Постараюсь..."
    "Как можно было не заметить кого-то настолько...{w}белого?"
    "И сколько можно проваливаться в себя?!"
    show monika neut me ce
    "Разве так сложно смотреть вперёд?"
    "Устроил себе, блин, проблему на ровном месте!"
    "Чуть девушку не сбил..."
    "Ладони теперь все в пыли и в мелких ссадинах."
    show monika pout cm oe
    "Молодец!"
    show monika om
    m "Эй..."
    show monika cm
    mc "???"
    show monika om
    m "Обычно местные здесь пробежками не занимаются."
    show monika e1b
    m "Нет, занимаются, конечно, но достаточно редко..."
    show monika oe
    m "Поэтому немного странно видеть в этом месте того, кто всерьёз этим увлекается."
    show monika cm
    "Всерьёз?"
    "Не слишком ли люди завышают своё мнение о других?"
    mc "Да я...{w}просто недавно переехал жить в этот район из другого города."
    mc "В прошлом уже бывал тут."
    show monika happ om oe
    m "Понятно..."
    show monika cm
    "А вообще она что, агент спецслужб, чтобы это выяснять у незнакомца?"
    show monika neut cm oe
    mc "Ладно, извини ещё раз, но мне надо спешить."
    "Сайори небось уже заждалась..."
    show monika lsur cm oe
    "Так что, раз-два и--{nw}"
    show monika om
    m "С-стой!"
    show monika cm
    mc "Что?"
    show monika happ om e1b b2b n2
    m "Возможно, это прозвучит немного глупо, но..."
    show monika happ oe
    m "...может, представимся друг другу?"
    show monika cm
    "После того, как я её чуть не сбил?"
    "Этот разговор начинает набирать ненормальные обороты."
    show monika -b2b n1
    mc "...почему нет?"
    show monika rhip
    "Странно, но рукопожатие с женским полом всегда выглядело для меня абсурдным..."
    mc "Макс."
    show monika om
    $ m_name = _("Моника")
    m "Мо{image=accent_low_register}{space=-15}ника."
    show monika cm
    "Хм, интересное имя..."
    show monika rdown
    mc "Будем теперь знакомы?"
    show monika happ om ce
    m "Ха-ха, да!"
    show monika cm
    mc "..."
    show monika oe
    m "..."
    show monika neut mh oe lpoint
    m "Хм, а твоё имя неяпонского происхождения..."
    show monika cm ldown
    mc "А, есть такое."
    show monika curi md oe
    mc "Слышала когда-нибудь про музыкальную группу {color=#fc7e23}MAX{/color}?"
    show monika om
    m "Э-э-э..."
    show monika nerv mb e1b
    m "...возможно..."
    show monika happ om oe lpoint
    m "Я особо не слежу за поп-культурой."
    show monika cm ldown
    mc "Это группа приобрела популярность в конце 90-ых годов."
    mc "Тогда они отправились в свой первый тур, который включал несколько концертов."
    show monika vsur cm oe
    mc "И на одном из них встретились мои родители."
    show monika om
    m "Ух ты..."
    show monika cm
    mc "Да, вот так вот вышло."
    show monika happ cm oe
    mc "И решили назвать меня в честь этой группы."
    show monika om
    m "Понятненько."
    show monika cm
    "А вообще будем честны: «Моника» тоже не совсем по-японски звучит..."
    show monika e1b
    "Может, поинтересоваться?"
    "Или...{w}я и так тут время уже потерял..."
    show monika neut cm oe
    mc "Ой, знаешь, меня просто на выходе один человек ждёт, вот и поспешил..."
    show monika mh b1b
    m "А, ясно."
    show monika happ om oe -b1b lpoint rhip
    m "Давай тогда сейчас обменяемся контактами, пока ты не ушёл?"
    show monika ldown
    m "У тебя же телефон с собой?"
    show monika cm
    "Блин, а может, и агент."
    "Как ещё объяснить её заинтересованность мной, да ещё и такое прямое?"
    show monika ce rdown
    mc "...хорошо, давай, только быстро."
    "Ладно, связь с ней лишней не будет."
    "Наверное..."
    call window_close

    call plot_transition(different_scene = False)
    $ contact_list["mc"].append("mc_m_chat")

    call window_open
    scene bg niigata park japanese torii
    show monika forward white_dress happ cm oe at i11
    with wiperight
    mc "Напишу сегодня где-то в начале второй половины дня, когда точно освобожусь..."
    show monika om lpoint
    m "Я тоже примерно в это время буду свободна."
    show monika cm ldown
    mc "Вот и отлично, как раз тогда и поговорим."
    mc "Всё, ладно, до скорого!"
    show monika om ce
    m "До встречи!"
    show monika cm at thide
    hide monika
    stop music fadeout 3.0
    pause 3.0
    "Мда..."
    "Я только вчера переехал...{w}а событий уже выше крыши накопилось за 1.25 дня."
    "По моим меркам, естественно."
    "Всё, хорош жечь время!"
    "Сайори ждёт."
    call window_close

    scene black with wipeleft_scene
    play noise_2 mc_steps_outside_jogging
    pause 7.0
    stop noise_2
    play noise_2 mc_steps_outside_jogging_wood
    pause 2.0

    scene bg niigata park japanese bridge 1 at run_center
    with wipeleft_scene
    pause 2.5

    scene black with wipeleft_scene
    pause 3.0
    stop noise_2

    call window_open
    "СТОП!"

    scene bg niigata park japanese bridge 2 with wiperight
    "Тут что-то не так..."
    mc "Где вода?"
    "Дно, что ли, чистят?"
    "Эх, чёрт, тут такой прикольный вид был..."
    "Что-то везде какие-то странности: то на станции ремонт с остановкой поездов, то вода из пруда «испарилась»..."
    "Так, всё!" with vpunch
    "Хватит в себя проваливаться!"
    call window_close

    scene black with wipeleft
    play noise_2 mc_steps_outside_jogging_wood
    pause 2.0
    stop noise_2
    play noise_2 mc_steps_outside_jogging
    pause 7.0
    stop noise_2

    call window_open
    scene bg niigata park japanese off entrance arc wall
    show sayori turned cat_shirt anno cm oe at t11
    with wipeleft_scene
    mc "Ура, я наконец-то прибежал!"
    show sayori om
    s "Ты задержался на целых 10 минут."
    show sayori cm
    "Чёрт побери, Моника!"
    "Хотя это больше моя вина..."
    "Пока не буду про неё рассказывать."
    mc "Я же давно здесь не был, Сайори."
    show sayori neut cm oe
    mc "И ещё умудрился навернуться по пути."
    show sayori worr cm oe
    mc "Все руки грязные."
    show sayori om
    s "Зря я затеяла это соревнование..."
    show sayori neut cm oe
    mc "Наоборот, мне понравился маршрут."
    mc "Там практически никого не было."
    mc "И было прохладно в тени."
    show sayori om
    s "Тебе реально понравилось?"
    show sayori cm
    mc "Честно?"
    show sayori happ cm oe
    mc "Да."
    show sayori om e4c lup rup at h11
    s "Я так рада!"
    show sayori cm ldown rdown
    "Её простота иногда будоражит мозг."
    "Вся серьёзность вмиг улетучилась."
    show sayori cm oe
    mc "Подожди, а где тут арка?"
    show sayori om
    s "В паре шагов от тебя."
    show sayori cm

    scene bg niigata park japanese off entrance arc 1
    show sayori turned cat_shirt nerv cm oe at t22
    with wipeleft
    mc "Серьёзно?..."
    mc "С обратной стороны её вообще не заметишь."
    show sayori om
    s "Когда у глицинии были яркие цветы и листья, то арку можно было увидеть сразу..."
    show sayori cm

    scene bg niigata park japanese off entrance arc 2 with dissolve
    pause 0.25
    mc "Что-то она...{w}засохла."
    "Значит, лиана сейчас, оказывается, голая."
    "Класс."
    mc "И как я должен был заметить эту глицинию, если бы прибежал первым?"
    s "Ну..."
    s "Я в любом случае прибежала бы быстрее тебя!"
    "Ха, хитрый ход."
    mc "Ладно, засчитано."

    scene bg niigata park japanese off entrance arc 1
    show sayori turned cat_shirt happ cm oe at t22
    with dissolve
    pause 0.25
    mc "Думаю, пора домой."
    show sayori nerv om oe
    s "Да, есть хочется..."
    show sayori cm
    mc "Нечего носиться, как угорелая."
    show sayori happ om ce
    s "Э-хе-хе~"
    show sayori cm

    scene bg niigata park japanese off entrance
    show sayori turned cat_shirt happ cm e1b at t22
    with wipeleft_scene
    mc "Кстати, насчёт поесть..."
    show sayori oe
    s "М-м-м?"
    mc "Я сегодня планировал сходить в магазин за продуктами."
    mc "Не хочешь составить компанию?"
    show sayori anno cm ce
    s "Хм-м-м..."
    mc "Интригуешь?"
    show sayori angr cm ce
    s "Хм-м-м-м-м-м-м-м-м..."
    mc "Ну, раз не хочешь, то--{nw}"
    show sayori happ om ce lup rup at h22
    s "Да!"
    show sayori cm ldown rdown
    mc "Да к \"не хочешь\" или \"пойдёшь\"?"
    show sayori om oe
    s "Пойду обязательно."
    show sayori cm
    mc "Договорились."
    mc "Зайду за тобой, как буду готов."
    show sayori om ce
    s "Угусь!"
    show sayori cm
    call window_close

    call plot_transition

    call window_open
    scene bg house
    show sayori turned cat_shirt happ cm oe at t11
    with wipeleft_scene
    mc "Пришли."
    show sayori om
    s "Через сколько мы, примерно, пойдём в магазин?"
    show sayori cm
    mc "Думаю..."
    show sayori laug cm oe
    mc "Хм-м-м..."
    show sayori om ce
    s "Не надо меня пародировать!"
    show sayori happ cm oe
    mc "Ладно-ладно, минут 30."
    show sayori om ce lup rup at h11
    s "Ок-ке!"
    show sayori ldown rdown
    s "Успею принять душ!"
    show sayori cm at thide
    hide sayori
    stop noise_3 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "30 минут..."
    play music mc_daijoubu fadein 3.0
    "Последую-ка примеру Сайори: смою с себя всю гадость из пота и грязи."
    "Одежду потом поменяю."
    "Какая разница: на улице жарко, я один."
    "Никто не помрёт, если я в одном полотенце пройдусь до спальни."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    scene bg mc house bathroom day with dissolve
    "Осталось только раздеться и освежиться."
    "Я аж в предвкушении."
    call window_close

    scene black with dissolve
    pause 0.25
    play sound mc_dressing_down
    pause 7.0
    play noise_1 shower_open
    pause 13.0
    call window_open
    "Всё, наконец-то заработал."
    mc "Фу-у-у..."
    "Теплая вода, которая стекает по всему телу..."
    "Нет ничего лучше, чем принятие душа."
    "Была бы воля, простоял бы как можно дольше."
    "Но у меня всего полчаса..."
    "А ещё платить лишние расходы за воду очень не хочется."
    mc "Ф-ф-ф..."
    "Моника..."
    "Вообще я только сейчас осознал, насколько всё было...{w}странно."
    "Любой другой бы пригрозил мне или просто ушёл."
    "Но Монике приспичило со мной пообщаться."
    "Вроде бы отлично, новые связи, чего тут думать?"
    "Тем более с девушкой."
    "...но чем я ей вдруг стал так интересен?"
    "Мы не пересекались до этого, не знаем друг друга хоть на каплю."
    "Этот вопрос не с любовного ракурса, это вообще не обсуждается."
    "А просто..."
    "...да блин, я её чуть не сбил!"
    "А если бы она головой треснулась о землю?"
    "Чёрт со мной, я бы вытерпел, а вот она?"
    "И разве люди после ПОДОБНОГО хотят общаться?"
    "Бред полнейший..."
    "Но может, я сегодня смогу выяснить у неё ответ на этот вопрос?"
    "Мы же ведь договорились на переписку."
    "...даже это звучит странно."
    "Что со мной или с ней не так?"
    "..."
    mc "А-а..."
    "Сегодня 3-е апреля, да?"
    "Учёба начинается 6-ого..."
    "Пара дней осталась до последнего учебного года, выходит."
    "Конечно, не очень это всё приятно, к тому же я не успел выдохнуть от прошлой школы и всей связанной с ней суматохи, но..."
    "Для меня это просто очередная смена рутины."
    "Свободная меняется на учебную -- ничего интересного."
    "Даже забавно: пока там у всех гормоны в одном месте бурлят, компании орут и бездумно веселятся, я просто живу по инерции."
    "Целей в жизни пока что нет."
    "Друзей тоже."
    "Живу только ради Сайори и своих родителей."
    "Хотя в то же время я не ощущаю пустоту..."
    "Я чувствую душевную каменность."
    "Мне просто плевать на всю эту школьную движуху в обществе."
    "Нет сил в ней участвовать."
    "И если бы этот сплошной круговорот событий засосал меня целиком, то я разорвался бы нахрен."
    "Всё-таки надо уметь ценить одиночество."
    "Однако в моём случае это переросло в некую скрытую одержимость."
    "Благо никто до этого не докапывается, а то у меня банально не хватит сил и желания (сколько раз я это уже повторяю?...) всё высказать по этому поводу."
    "А пока будешь говорить, запутаешься и скажешь всё неверно, потом придётся это пояснять, а потом пояснять пояснение и так далее..."
    mc "Ох-х-х..."
    "А сколько времени прошло?"
    "По-хорошему пора заканчивать."
    call window_close

    stop noise_1
    play sound shower_close
    pause 7.8
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1

    call window_open
    scene bedroom with dissolve
    "Переодеться бы во что-нибудь нормальное..."
    "Было же что-то..."
    "А ну-ка, посмотрим, что у нас тут?"
    call window_close

    scene black with dissolve
    pause 0.25
    play sound wardrobe_door_open
    pause 1.802
    play sound mc_dressing_up
    pause 7.984
    play sound wardrobe_door_close
    pause 2.270

    call window_open
    scene bg bedroom with dissolve
    "Чёрную футболку сменила чёрная футболка с длинным рукавом."
    "Как там она называется?..."
    "..."
    "Лонгслив, тьфу."
    "Откуда я это помню?"
    "Понапридумывают разных маразматических слов, блин, потом вся голова засоряется бредом."
    "..."
    "Возьму наплечную сумку и мобильник."
    "Спасибо XXI веку за электронную карту прямо в смартфоне."
    "...и за то, что в этом районе магазины их могут принимать."
    "Хотя у этой системы есть и свои весомые минусы..."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1

    call window_open
    scene bg mc house hallway day with dissolve
    "Так, всё взял: телефон, сумку, пакет и кошелёк."
    "...мало ли, всегда надо подстраховываться."
    "Всё закрыл, всё выключил..."
    "Да, всё."
    "Теперь можно со спокойной душой идти к Сайори."
    stop music fadeout 3.0
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
    pause 6.0
    stop noise_1

    call window_open
    scene bg house with dissolve_scene_full
    "Итак...{w}тишина."
    "Ха, я даже на 5 минут раньше обещанного пришёл."
    "Можно было бы пока подождать здесь..."
    "Но а может, стоит позвонить в дверь?..."
    "Где только эта кнопка?"
    "Всегда терял её из виду..."
    "А, точно, сбоку справа от самой двери."
    "Кому вообще пришло в голову установить её так криво?"
    call window_close

    pause 1.5
    play sound doorbell_sayori
    pause 4.0

    call window_open
    "Вообще никого."
    "Никто не услышал?"
    call window_close

    pause 0.6
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 4.0

    call window_open
    "..."
    "Возможно, Сайори в самом разгаре подготовки..."
    "А я её тут терроризирую дверным звонком."
    "Ладно, мне не трудно подождать."
    "Посмотрю на окружение...{w}послушаю птиц...{w}пожарюсь на солнце..."
    window hide

    pause 5.0

    window auto
    "..."
    "...и?"
    "Что там можно делать?"
    "Ё-моё, почему такие банальные вещи начинают растягиваться, как сопля?"
    "Проще одному сходить."
    "Но я же ведь договорился!"
    "А значит, что, уйдя, я кину Сайори."
    window hide

    pause 5.0

    window auto
    "......"
    "Да какие же с вами проблемы..."
    "Нет, я ещё позвоню."
    "Задолбаю-замучаю, но своего добьюсь."
    call window_close

    pause 0.5
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 0.75

    call window_open
    show sayori_mom home_clothes happ cm oe at t11
    mc "А-А-A-A-А--{nw}"
    mc "Ой..."
    show sayori_mom laug cm oe
    mc "Извините..."
    show sayori_mom om ce rhip
    sm "А-ха-ха, не напрягайся, Макс!"
    show sayori_mom happ om oe
    sm "Я сама её поторапливала, но она слишком увлеклась душем."
    show sayori_mom cm
    mc "Ясно."
    "Тоже душ понравился, значит?"
    "А мы точно не брат и сестра?"
    show sayori_mom om lpoint
    sm "Она выйдет через пару минут."
    show sayori_mom cm ldown
    mc "Хорошо."
    show sayori_mom neut mi oe rdown
    sm "А, и ещё..."
    show sayori_mom lpoint
    sm "Моему солнышку тоже надо прикупить некоторые продукты, так что помоги ей, если понадобится."
    show sayori_mom happ cm oe ldown
    mc "Да, конечно."
    show sayori_mom om ce
    sm "Заранее спасибо!"
    show sayori_mom cm at thide
    hide sayori_mom
    pause 1.0
    "Ладно, подождём..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg house with wiperight
    "................"
    "Ну блин, Сайори..."
    "Считаю до трёх, после чего ломлюсь в дверь."
    "Раз...{w=1.0}два...{w=1.0}три!--{nw}"
    show sayori turned casual nerv om ce at t11
    s "Ура, я вышла!"
    show sayori cm
    "Наконец-то..."
    show sayori e1a
    mc "Кто-то очень сильно не хотел покидать приятный душ, да?"
    show sayori tap casual nerv om oe at s11
    s "Э-хе-хе~"
    show sayori cm
    mc "К слову, ты опоздала ровно на 10 минут."
    show sayori e2 m1
    s "...хе-хе..."
    show sayori neut cm oe
    mc "Ладно уж, пошли."
    show sayori turned casual happ cm oe at t11
    mc "Продукты сами себя не купят."
    show sayori om ce rup lup at h11
    s "Ок-ке!"
    show sayori cm ldown rdown

    scene bg niigata street suburban 10 day
    show sayori turned casual happ cm oe at t11
    with wipeleft_scene
    mc "А что конкретно тебе надо взять?"
    show sayori curi om e2b
    s "Грибы, зелень, мясо, ещё по мелочи--{nw}"
    show sayori neut cm oe
    mc "Ладно, я понял."
    mc "Нам придётся немного разойтись в стеллажах."
    mc "Мне нужна готовая еда."
    show sayori sad om oe
    s "Ты всё ещё не умеешь готовить?..."
    show sayori md
    mc "Да, времени на это тоже не было."
    show sayori worr cm oe

    scene bg niigata street suburban 11 day
    show sayori turned casual neut cm oe at t11
    with wipeleft_scene
    show sayori om
    s "А простая еда?"
    show sayori cm
    mc "Простая еда на то и простая."
    show sayori e1b b1f
    mc "Одной ей сыт не будешь."
    show sayori doub cm ce -b1f
    s "Хм-м-м..."

    scene bg niigata street suburban 15 day
    show sayori turned casual happ cm oe at t11
    with wipeleft_scene
    show sayori om
    s "А если я тебя научу парочке простых рецептов?"
    s "Я редко что-то готовлю, но у меня что-то получалось."
    show sayori neut cm oe
    mc "Боюсь, из головы всё выветрится."
    show sayori om b1d
    s "Но надо же с этим что-то делать!"
    show sayori cm
    mc "Надо..."

    scene bg niigata street urban 1 day
    show sayori turned casual happ cm oe at t22
    with wipeleft_scene
    mc "Ладненько, мы на месте."
    show sayori ce
    mc "По корзинке и вперёд!"
    show sayori oe
    mc "Только ждём друг друга рядом с кассой, чтобы не разойтись."
    show sayori happ om
    s "Хорошо!"
    show sayori cm
    stop noise_3 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_3 shop_noise fadein 1.0
    "М-м-мда..."
    "Всё-таки если постоянно сидеть на одних полуфабрикатах, то желудок повесится с такой жизни."
    "Нет, конечно, благодаря им я довольно минималистичен в своих покупках..."
    "Вон, на неделю всего лишь одна корзинка, ещё всякая всячина сверху."
    "...но с этим реально надо что-то делать."
    "Особенно когда я буду жить в общежитии вуза, если он будет далеко от дома."
    play music shop_food_music fadein 3.0

    scene bg niigata shop food 2
    show sayori turned casual curi cm oe at sayori_shop
    with dissolve_scene_full
    "Что-то Сайори значительно отстаёт от меня по готовности."
    mc "Ну как?"
    show sayori om
    s "И тут нет."
    show sayori worr om oe
    s "Неужели..."
    show sayori lsur om oe
    s "А, вот!"
    call window_close

    pause 0.5
    show sayori happ cm ce
    pause 0.5
    show sayori lup packing_bran with dissolve
    pause 1.0
    hide sayori
    show sayori turned casual happ cm ce lup packing_bran at e11
    with dissolve
    pause 1.0
    show sayori ldown -packing_bran with dissolve
    pause 1.0
    hide sayori
    show sayori turned casual happ cm ce at sayori_shop
    with dissolve
    pause 0.5

    call window_open
    "Хм..."
    show sayori oe
    "Какая-то упаковка отрубей..."
    "Ещё один продукт, утяжеляющий корзинку Сайори."
    "...в моих руках."
    "Хотя я тоже себе прикупил отруби."
    show sayori e1b
    "Лёгкая каша с молоком по утрам пойдет хоть на какую-то пользу."
    show sayori oe
    mc "Что ещё?"
    show sayori om
    s "Зелень!"
    show sayori cm

    scene bg niigata shop food 1
    show sayori turned casual curi cm oe at sayori_shop(x = 1000)
    with wipeleft_scene
    "Да-а-а, тут куча всего: бутылочки какие-то, лук, что-то непонятное..."
    show sayori happ om ce
    s "А вот и пёстрый пучок!"
    show sayori cm
    call window_close

    pause 0.5
    show sayori lup packing_onion with dissolve
    pause 1.0
    hide sayori
    show sayori turned casual happ cm ce lup packing_onion at e11
    with dissolve
    pause 1.0
    show sayori ldown -packing_onion with dissolve
    pause 1.0
    hide sayori
    show sayori turned casual happ cm ce at sayori_shop(x = 1000)
    with dissolve
    pause 0.5

    call window_open
    "...горох, фиг пойми какие корни..."
    show sayori happ om oe
    s "Теперь за грибами!"
    show sayori cm
    "...что это за белое вытянутое нечто?..."
    show sayori neut cm oe
    "Совершенно не помню, как оно называется..."
    show sayori angr cm oe
    "А это капуста, или я просто тупой, ничего определить не могу?"
    show sayori om
    s "Алло!" with vpunch
    show sayori cm
    mc "А!"
    show sayori om
    s "Грибы!"
    show sayori cm
    mc "Грибы..."
    show sayori doub cm oe
    mc "...а, понял."

    scene bg niigata shop food 3
    show sayori turned casual happ cm ce at sayori_shop(x = 1000)
    with wipeleft_scene
    "Теперь корзинку Сайори вершат грибы."
    show sayori om oe
    s "Ещё надо..."
    "И тут тоже они."
    show sayori e1b
    "Странно, что в детстве я всегда хотел съесть какой-нибудь мясистый свежий гриб прямо без очистки."
    show sayori curi om e2b
    "Потом я попробовал маринованные, и вроде бы это было то, что я хотел...{w}вот только соль с маслом знатно перебивали ощущение."
    show sayori happ om ce
    "Хотя да, это было всего лишь глупое и наивное желание детства."
    show sayori oe
    s "...и всё!"
    show sayori cm
    mc "Да, хорошо."
    "Что-то я активно в себя ухожу..."
    "Надо это сдерживать!"

    scene bg niigata shop food 4
    show sayori turned casual happ cm ce at sayori_shop(x = 1000)
    with wipeleft_scene
    "О-хо-хо, да ну, не верю своим глазам!"
    "Тут те самые балончики с кремом слева внизу стоят!"
    show sayori e1b
    "В детстве их очень обожал."
    "Да и в целом сейчас люблю крем."
    show sayori lsur cm oe
    "А ещё всякую пенку на напитках, особенно на кофе."
    show sayori happ cm ce
    "Но потом желание распробовать быстро улетучивается, когда превышаешь норму потребления..."
    "Рот начинает противно вязнуть, всё становится безвкусным и мерзким, фу."
    show sayori om
    s "И-и-и..."
    show sayori oe
    s "Всё!"
    show sayori cm
    mc "Тогда идём на кассу."
    show sayori ce

    scene bg niigata shop food 5
    show sayori turned casual lsur om oe at e22
    with wipeleft_scene
    s "Ха-а-а-а..."
    show sayori cm
    "Ну или не идём на кассу..."
    show sayori vsur om oe
    s "C...{w}сэнбэй!"
    show sayori curi om oe
    s "Э-э-э, у меня нет на него лишних денег!"
    show sayori cm
    "...и я даже догадываюсь, почему."
    show sayori sad ml oe lup rup
    s "Макс, купи-купи-купи!"
    show sayori mk
    mc "Но это всего лишь рисовое печенье..."
    show sayori ml
    s "Ты же знаешь, что оно одно из моих любимых!"
    show sayori mk
    "Да у Сайори всё печенье любимое."
    "Более того, она гроза любого печенья."
    show sayori e2a ldown rdown
    "Как-то раз, когда я был у неё в гостях, она умудрилась съесть одну упаковку из 20-ти штук за пару минут."
    "А там, между прочим, была и моя порция!"
    "Зря в туалет тогда отошёл..."
    show sayori tap casual pout cm oe b1
    s "У-у-у-у-у..."
    mc "Хм..."
    "Да вроде бы дешёвые..."
    "Тем более ради счастья Сайори..."
    show sayori neut cm oe -b1
    "...возьму одну с шоколадом и положу себе в корзинку."
    show sayori turned casual mc e4c b2a lup rup
    s "СПАСИБО!"
    show sayori mo
    mc "Тихо!"
    show sayori ldown rdown
    mc "Не надо кричать на людях!"
    stop music fadeout 2.0
    stop noise_3 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_3 street_suburban_noise fadein 3.0
    scene bg niigata street urban 1 day
    show sayori turned casual happ cm ce at t11
    with wipeleft_scene
    "Две корзинки в моих руках сменились двумя пакетами."
    "А сэнбэй сразу же улетел на руки Сайори."
    "Подождите..."
    show sayori oe
    mc "А где?..."
    show sayori om
    s "Сэнбэй?"
    s "Я уже съела."
    show sayori cm
    "..."
    show sayori e1b
    "Что и не требовалось доказать, потому что это очевидно."

    scene bg house
    show sayori turned casual happ cm oe at t11
    with wipeleft_scene
    mc "Держи свой пакет, он достаточно лёгкий."
    show sayori om
    s "Спасибо, Макс!"
    show sayori ce
    s "Ты очень мне помог!"
    show sayori cm oe
    mc "Да ладно тебе, обычное дело."
    show sayori om
    s "Всё, я побежала, до завтра!"
    show sayori cm
    mc "До завтра."
    show sayori at thide
    hide sayori
    pause 2.0
    "Что ж, мне тоже пора домой."
    call window_close

    scene black with dissolve_scene_full
    play noise_1 mc_steps_outside
    pause 6.0
    stop noise_1
    play sound house_door_open
    pause 1.227
    stop noise_3 fadeout 4.0
    play noise_1 mc_steps_outside
    pause 2.0
    stop noise_1
    play sound house_door_close

    call window_open
    scene bg mc house hallway day with dissolve_scene_full
    mc "Фух..."
    "Теперь нужно помыть руки, разгрузить продукты, переодеться, поесть..."
    "Кстати, сколько времени?"
    "..."
    "О, где-то 13:25..."
    "Хм, никогда не понимал 12-часовой формат времени."
    "Неудобно же."
    "Как люди им пользуются?..."
    "А некоторые заведения и бизнесмены так вообще используют 26-часовой формат."
    "Фигня какая-то..."
    "Ладно, не об этом."
    "В общем, как раз всё быстро закончу и приступлю к тому, что меня слегка будоражит..."
    "Дистанционный разговор с незнакомой девушкой."
    "...со странной незнакомой девушкой."
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "Фу-у-у-у..."
    "Тело размякло..."
    "Как же хочется в такие моменты просто расслабиться и отдохнуть под какое-нибудь видео..."
    "Но...{w}Моника..."
    "Хватит рассусоливаться."
    "Просто сядь."
    "Уверенно возьми телефон."
    call skip_block_on

    python in phone.system:
        battery_level = 90
        clock = (13, 55)

    phone discussion "mc_m_chat"
    $ plot_pause()
    "И...{w}включи этот чёртов вай-фай."
    window hide

    call phone_status_bar_button('wifi', disable = False)

    window auto
    "Надо будет его на всякий случай оставлять включённым дома, мало ли там Сайори напишет...{w}или ещё кто-нибудь..."
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        time year 2018 day 3 month 4 hour 13 minute 55
        "mc" "Привет. Пишу тебе, как и обещал. Я освободился. Извини, если задержался"
    "М-м-м..."
    "Как-то так себе звучит..."
    "Точнее, совершенно никак: банальное нагромождение предложений."
    "Хотя как ещё написать?"
    "Ничего в голову толком не лезет, мозги в кашу..."
    $ phone.system.clock = (13, 56)
    phone discussion "mc_m_chat":
        "m" "Привет! Я тоже сейчас свободна"
    play music mc_house_lofi_bliss fadein 3.0
    "О, отлично, есть контакт!"
    "Начинаем налаживать связь с внешним миром."
    window hide

    pause 3.0
    $ phone.system.clock = (13, 57)
    pause 2.0

    window auto
    "Ну и что?"
    "Что ей написать?"
    "\"Почему ты захотела общаться со мной, когда я чуть тебя не сбил?\""
    "\"Откуда у тебя такой интерес ко мне?\""
    "\"Кто ты вообще такая?\""
    "А-а-а!" with vpunch
    "Ну какой же ты тупой!"
    "Давай, думай!"
    $ phone.system.clock = (13, 58)
    "Время идёт, нельзя медлить!"
    phone discussion "mc_m_chat":
        "m" "Хах, да, я тебя понимаю..."
        "m" "Непривычно общаться с девушкой после того казуса, да?)"
    "..."
    "...она читает мои мысли?"
    "С другой стороны, Моника тоже осознаёт абсурдность ситуации..."
    "Всё, блин, надо что-то написать."
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Да, если честно..."
        "m" "Ладно, не переживай, это уже в прошлом"
    "Ага, легко сказать, а вот на деле?"
    phone discussion "mc_m_chat":
        "m" "Надо жить проще и позитивнее"
        "m" "Прямо как одна моя хорошая подруга)"
        "m" "Она просто квинтэссенция хорошего настроения"
    $ phone.system.clock = (13, 59)
    "Что?!" with vpunch
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Я, конечно, могу ошибиться, но..."
        "mc" "Это Сайори?"
        "m" "А как ты угадал? 0_0"
        "mc" "Я теперь живу напротив её дома"
        "mc" "К тому же мы с ней друзья"
        "m" "А, так ты тот самый Макс, про которого она иногда рассказывала?"
    "Сайори успела кому-то про меня наболтать?"
    "Хм..."
    "А про Монику она вообще ничего не говорила."
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Судя по всему, да"
        "mc" "И что же она рассказала, если не секрет?"
        "m" "Много чего)"
    $ phone.system.clock = (14, 0)
    phone discussion "mc_m_chat":
        "m" "Возраст, например, чем занимаешься..."
        "m" "Но в целом ничего личного, честно"
        "mc" "Надеюсь"
        "m" "Хаха, не парься, всё нормально)"
    "Разве я похож на нервного с того конца связи?"
    phone discussion "mc_m_chat":
        "m" "Значит, ты только недавно переехал?"
        "mc" "Да, вчера буквально"
        "m" "Ну... Эээ, с переездом!"
        "mc" "Спасибо"
    $ phone.system.clock = (14, 1)
    phone discussion "mc_m_chat":
        "m" "Будешь учиться в нашем потоке?"
        "mc" "Думаю, да, куда я денусь"
        "mc" "Как у вас тут с учёбой?"
        "m" "Так же, как и везде, наша школа ничем особо не отличается от других"
        "m" "За исключением 2 вещей"
        "mc" "И каких же?"
        "m" "1: статус нашей школы довольно высокий, хотя не могу сказать точно..."
        "mc" "Знаю"
        "m" "Короче, у нас есть ученики неяпонского происхождения"
        "mc" "Да?"
        "m" "Их мало, но встретить можно"
        "mc" "Ясно"
        "m" "2: наша школа идёт нам настречу"
        "mc" "В каком плане?"
        "m" "У нас всего 5 рабочих дней, дресс-код обязателен, но разрешены мелкие поблажки, участие в клубной деятельности рекомендуется, но необязательна"
    $ phone.system.clock = (14, 2)
    phone discussion "mc_m_chat":
        "mc" "Да ладно, не верю"
        "mc" "Подобные школы в нашей стране очень трудно найти, если они вообще существуют"
        "m" "А тебе повезло!"
        "m" "И всем нам"
        "m" "Не будет сильной и бессмысленной нагрузки"
        "mc" "Это да"
    "А ещё учитываем то, что начало учебного года здесь не 1-ого апреля, а 6-ого."
    "Что может быть ещё лучше?"
    phone discussion "mc_m_chat":
        "m" "Кстати, насчёт клубов..."
        "mc" "?"
        "m" "Я являюсь президентом одного из них"
    $ phone.system.clock = (14, 3)
    phone discussion "mc_m_chat":
        "mc" "Президент?!"
        "m" "Хахаха)"
        "m" "Могу кратенько написать, как им стала"
        "mc" "Давай"
        "m" "Раньше (в прошлом учебном году) я состояла в Дискуссионном клубе"
        "m" "Вроде бы так называется..."
        "mc" "Но, я так понимаю, ты оттуда ушла?"
        "m" "Да("
        "m" "Я сначала думала, что там прямо настоящие обсуждения разных тем с применением ораторских навыков..."
        "m" "А в итоге всё скатывалось в очень неприятный балаган"
    $ phone.system.clock = (14, 4)
    phone discussion "mc_m_chat":
        "mc" "Да уж"
        "m" "Так вот, остальные клубы были мне не по душе, а вступить куда-то хотелось"
        "m" "Но раз я человек нестандартный, то и решила эту проблему подобающе"
        "mc" "Создала собственный клуб, да?"
        "m" "Именно!"
        "m" "Литературный клуб \"Доки-Доки\"!"
        "mc" "Ух ты..."
        "mc" "А почему \"Доки-Доки\"?"
        "m" "Это просто неофициальное название"
        "m" "Сайори, когда только вступила, часто говорила \"Оки-Доки!\""
    $ phone.system.clock = (14, 5)
    phone discussion "mc_m_chat":
        "m" "На это потом обратила внимание Юри, одна из наших участниц"
        "m" "Она решила преобразовать название в \"Доки-Доки\", которое звучит как стук сердца"
        "m" "В общем, она любит всё такое с необычным подтекстом)"
        "m" "А я же в свою очередь закрепила это в качестве дополнения к названию клуба"
        "mc" "Интересно вышло"
        "m" "Согласна"
        "mc" "И как клуб развивается? Успешно?"
        "m" "Ну..."
        "m" "Не очень, честно говоря..."
    $ phone.system.clock = (14, 6)
    phone discussion "mc_m_chat":
        "mc" "А что так?"
        "m" "В нём всего четыре человека: я, Сайори, Юри и Нацуки"
        "m" "Про последних чуть подробнее позже, может, расскажу"
        "mc" "Хм..."
    "И про клуб Сайори особо ничего не рассказывала..."
    "Или я просто уже не помню?"
    phone discussion "mc_m_chat":
        "m" "Знаешь, хоть наш клуб и называется Литературным, но всё, что мы делаем связанное с литературой -- это только пишем стихи"
    $ phone.system.clock = (14, 7)
    phone discussion "mc_m_chat":
        "m" "А ещё храним в кладовке целый стеллаж манги Нацуки"
        "m" "Хотя манга литературой не является..."
        "m" "Не в обиду, если что!"
        "mc" "Да не, всё нормально"
    "Ух, нифига себе..."
    "Я за всю жизнь в руках держал лишь пару томиков, да и то несколько лет назад."
    "Как-то не выходило погрузиться во всё это..."
    "То денег, то времени, то места для хранения банально не было."
    $ phone.system.clock = (14, 8)
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Выходит, она так любит мангу?"
        "m" "Даже не представляешь, насколько сильно)"
        "mc" "Но почему она хранится именно в вашем клубе?"
        "m" "Ну..."
        "m" "Я... Как-нибудь попозже тебе расскажу"
        "mc" "Ладно, не буду настаивать"
    "Что такое серьёзное может быть у этой участницы, что Литературный клуб хранит у себя всю её мангу?"
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "И ваш клуб больше ничем, кроме стихов, не занимается?"
    $ phone.system.clock = (14, 9)
    phone discussion "mc_m_chat":
        "m" "Когда-то я пробовала пристрастить всех к чтению и обсуждению книг, но только Юри это было по душе"
        "m" "А так... Ничего особенного"
        "mc" "А новые люди хоть приходят?"
        "m" "Мы пытались заманивать новых участников, но никто не задерживался"
        "mc" "Прямо вообще никто?"
        "m" "Да("
        "mc" "Это даже странно"
        "m" "У одних нет времени, другие уже распределены по клубам, а третьи просто не хотят..."
        "m" "Поэтому как-то вот так"
        "mc" "Да уж, тяжело вам в этом плане..."
    $ phone.system.clock = (14, 10)
    phone discussion "mc_m_chat":
        "m" "А что делать?"
        "m" "Против желания других не пойдёшь"
        "m" "А так иногда хочется, чтобы пришёл кто-то новый..."
        "m" "Литературный клуб оживился бы..."
    "Ха...{w}ха-ха-ха..."
    "Я понял!"
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "А, дай угадаю..."
        "mc" "Ты хочешь предложить мне членство в твоём клубе?"
        "m" ":)"
    $ phone.system.clock = (14, 11)
    "Элементарно."
    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        "mc" "Хорошо, я подумаю где-то в течение недели после начала учёбы, но ничего не обещаю"
        "mc" "Я никогда не пробовал писать какие-либо стихи"
        "m" "Научишься, у нас тоже не шедевры)"
        "mc" "Зная себя, могу предположить, что по сравнению со мной, может, и шедевры..."
        "m" "В любом случае твой труд было бы интересно изучить"
        "mc" "Хм..."
        "m" "Ой, мне надо скоро будет отойти"
        "m" "Спасибо за разговор, было приятно пообщаться!"
    python in phone.system:
        battery_level = 89
        clock = (14, 12)
    phone discussion "mc_m_chat":
        "mc" "Стой, один небольшой вопрос"
        "m" "Да?"
        "mc" "Может, это прозвучит грубо и глупо, но всё же..."
        "mc" "Почему ты решила общаться со мной?"
        "m" "Ну..."
        "m" "У тебя искренние глаза)"
        "m" "А я ценю искренних людей"
        "mc" "Вот как..."
        "mc" "Спасибо за ответ"
        "m" "Пожалуйста!"
    $ phone.system.clock = (14, 13)
    phone discussion "mc_m_chat":
        "m" "Всё, мне пора, до встречи!"
        "mc" "До встречи"
    window hide

    call phone_status_bar_button('wifi', disable = True)

    phone end discussion transition

    call skip_block_off
    "...это самый странный ответ из всех возможных."
    "\"Искренние глаза\"?"
    "Что в них искреннего?"
    "Учитывая, сколько я скрываю в себе, никакой искренностью там совершенно не пахнет."
    "Короче, понятнее не стало."
    mc "Пф-ф-ф, ладно..."
    "Теперь на сегодня всё."
    "Можно откиснуть с чистой совестью."
    "Надо наслаждаться такими моментами, пока есть время."
    "А то там впереди эта учёба и «взрослая жизнь»..."
    "Даже думать не хочется..."
    call window_close

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    stop music fadeout 6.0
    pause 6.0

    hide black onlayer front
    call window_dialog_long_transition("s", transition = False)

    $ sm_name = _("Мама")

    call window_open
    scene bg sayori house bedroom night with dissolve_scene_full
    call autosave
    s "Хм-хм-хм~"
    "Интересно, как там--{nw}"
    play phone_sound new_message_sayori
    pause 1.0
    s "О!"
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 67
        clock = (21, 44)

    phone register "s_m_chat":
        time year 2018 day 3 month 4 hour 21 minute 44
        "m" "Хэй, Сайори, я поговорила с твоим другом"

    phone discussion "s_m_chat":
        "m" "Извини, поздновато пишу, сейчас только освободилась"
        "s" "Ой, не переживай!"
        "s" "Это же ведь отлично что вы наконец то поговорили! (> ω <)"
    $ phone.system.clock = (21, 45)
    phone discussion "s_m_chat":
        "s" "И что же он сказал?"
        "m" "Подумает где-то неделю"
        "m" "Но, скорее всего, Макс согласится стать полноценным членом нашего клуба)"
        "s" "Ура! (^ ω ^)"

    phone end discussion transition

    call skip_block_off
    s "Э-хе-хе~"
    "Наш план сработал!"
    "Сначала спланированная встреча в парке, потом спланированный разговор..."
    "Теперь Макс точно вступит в Литературный клуб!"
    "Наверное..."
    "Меня он вряд ли бы послушал."
    "Если он полгода не занимался пробежками, то и здесь он пообещал бы вступить в клуб и не вступил бы..."
    "Это игнорирование меня?"
    "Я ему надоедаю?"
    "Нет-нет, неправильно."
    "Иначе бы он не общался со мной..."
    "..."
    s "Ум-м-м!"
    s "Думай-думай-думай!"
    "......."
    "...нет, не думается."
    "Я не могу описать это словами."
    "Но ведь Монику Макс воспринял всерьёз."
    "Да?"
    "Или не совсем..."
    s "Ой-й-й..."
    "У меня сплошная каша в голове..."
    s "Вот бы стать плюшевой коровкой!"
    s "Сидишь в тёплой комнате и ничего не делаешь."
    s "Тогда бы всё стало намного проще..."

    show layer master:
        pos (640, 360) anchor (0.5, 0.5)
        ease 5.0 zoom 2.5 xoffset -500 ypos 20

    s "Да, мистер Коровка?"
    play music sayori_boring
    mr_cow "Нет."
    s "Что нет-то?"
    mr_cow "Ты не учитываешь множество вещей."
    s "Хочешь сказать, тяжело быть плюшевой коровкой?"
    mr_cow "Я не про это."
    s "А про что?"
    mr_cow "Сайори, ты забываешь самое главное."
    s "Что же, мистер Коровка?!"
    mr_cow "{b}Себя{/b}, Сайори."
    s "{b}Меня{/b}?"
    mr_cow "Если станешь таким же, как я, то ты перестанешь быть Сайори."
    s "М-м-м-м-м..."
    s "Не вижу в этом минусов."
    mr_cow "Не вижу в этом плюсов."
    s "Разве?"
    mr_cow "Абсолютно."
    mr_cow "Ведь ты самый близкий и значимый для Макса и для своей семьи, а ещё для Моники и её клуба."
    mr_cow "Что будет с ними, когда они потеряют ту Сайори, которую знают?"
    mr_cow "И увидят вместо неё плюшевую корову?"
    s "..."
    s "Ничего особенного, наверное..."
    mr_cow "Ложь."
    mr_cow "Все будут серьёзно переживать."
    s "Опять ты со своими тучками!"
    s "Я же всё в шутку говорила!"
    mr_cow "Ложь."
    s "Тц!"
    s "..."
    s "...хорошо, я не верю тебе, мистер Коровка, что все будут переживать, что я превращусь в плюшевую коровку!"
    s "Точка."
    mr_cow "Запятая."
    mr_cow "Ты должна мне поверить."
    s "Почему ты такой серьёзный?..."
    mr_cow "Потому что это далеко не первый разговор."
    mr_cow "А сейчас ты думала, что тебя всерьёз не воспринимают."
    s "...м-м-м..."
    mr_cow "Сайори, тебе надо научиться ценить себя."
    s "От плюшевой игрушки слышу."
    mr_cow "Иначе это никогда не прекратится и станет только хуже."
    mr_cow "А для этого тебе надо посмотреть на всё полностью открытыми глазами."
    s "Я и так на всё своими глазами смотрю."
    s "Ви-и-и-и."
    mr_cow "Ты же не учитываешь, как клуб рад твоему присутствию или как Макс тебе помогает, ни разу не отвернувшись."
    s "Вдруг он просто из уважения меня слушает?"
    s "Или обидеть не хочет..."
    mr_cow "Тогда бы вы столько не общались."
    s "М-м-м..."
    s "Но это всё равно значит, что я приношу хлопоты!"
    mr_cow "Нет."
    s "Откуда тебе это знать?!"
    s "ТЫ, коровка, с ним никогда не разговаривал!"
    mr_cow "Я чувствую всё то, что чувствуешь ты."
    s "Я чувствую, что моё воображение всё слишком преувеличивает..."
    s "...как обычно!"
    mr_bird "А-а-а ми-и-истер-р-р Кар-р-ро-о-овка абсолютно кр-р-ра-а-ав."
    s "Мистер Птиц?!"
    s "Ты всё время подслушивал?!"
    mr_bird "Кар-р-р!"
    mr_bird "Все бы тебя бр-р-ро-о-осили, если бы твои слова-а-а были кр-р-ра-а-авдой!"
    s "..."
    s "Так, Коровка и Птиц!"
    s "Я никогда в своей жизни не буду верить плюшевым игрушкам--{nw}"
    play sound closet_open
    pause 1.0
    sm "Лучик?"

    $ currentpos = get_pos(channel="music")
    stop music fadeout 0.5
    play music_none_loop oops

    show layer master

    show sayori_mom home_clothes laug cm ce at t11
    s "КЬЯ!" with vpunch
    show sayori_mom om
    sm "Ха-ха-ха!"
    show sayori_mom cm oe
    s "Ты меня напугала!"
    show sayori_mom happ om oe lpoint rhip
    sm "Вообще-то я постучалась перед тем, как войти."
    show sayori_mom cm ldown
    s "...разве?"
    show sayori_mom om ce
    sm "Может, ты так усердно разговаривала с Коровкой и Птицем, что не услышала меня."
    show sayori_mom cm
    s "У-у-у..."
    show sayori_mom oe
    "Как-то стыдно..."
    show sayori_mom sad cm oe rdown
    "Надеюсь, мама ничего не услышала!"
    show sayori_mom mi
    sm "Лучик, ты очень вяло выглядишь..."
    sm "Что-то случилось?"
    show sayori_mom cm
    s "Ничего!"
    show sayori_mom neut cm oe rhip
    s "Просто устала."
    show sayori_mom happ om ce
    sm "Ха-ха-ха, ну раз так, то хорошенько отдохни."
    show sayori_mom cm
    s "Конечно!"
    show sayori_mom om oe lpoint
    sm "Но если тебя что-то будет беспокоить, то можешь со мной это обсудить."
    show sayori_mom cm ldown
    s "Угусь~"
    show sayori_mom e1b rdown at thide
    hide sayori_mom with easeoutleft
    pause 0.75
    sm "{size=19}Кстати, я вернула твою ручку, спасибо за неё!{/size}"
    s "А, пожалуйста!"
    pause 0.15
    play sound closet_close
    pause 1.0
    "Наверное, мама снова нашла какой-то интересный рецепт в журнале..."

    show layer master:
        pos (640, 360) anchor (0.5, 0.5)
        ease 5.0 zoom 2.5 xoffset -500 ypos 20

    mr_bird "Ай-ай-ай, скр-р-р-ыва-а-ать себя нехор-р-рошо-о-о!"
    s "Ты хочешь, чтобы моя мама беспокоилась по таким пустякам?!"
    mr_cow "Сейчас Сайори права."
    $ audio.sayori_boring_1 = "<from " + str(currentpos) + " loop 0>mod_assets/music/characters/s/boring.ogg"
    play music sayori_boring_1 fadein 0.5
    mr_bird "Кар-р-р?!"
    mr_bird "Ты бр-р-росил нашу филосо-о-офскую мысль р-р-ра-а-ади мнимого споко-о-ойствия?!"
    mr_cow "Нет, ты неправильно понял."
    mr_bird "Всё я по-о-онял!"
    s "Успокойтесь оба, всё нормально!"
    mr_bird "Какой нор-р-рма-а-ально?!"
    mr_bird "ОН пр-р-ре-е-едал нашу др-р-ру-у-ужбу р-р-ради фальшивого споко-о-ойствия!"
    mr_cow "Родители не смогут понять проблему в полной мере, только сверстники способны осознать её целиком."
    mr_bird "Я всю жизнь пр-р-ро-о-ожил ради чувств Сайо-о-ори!"
    mr_bird "А ТЫ..."
    mr_bird "Ты пр-р-ро-о-осто взял и согласился скр-р-ры-ы-ыть их в ответственный момент, когда недавно заявлял обр-р-ра-а-атное!"
    mr_cow "Ты меня не слышишь."
    mr_bird "Опр-р-рове-е-ер-р-ргни!"
    s "Ребята, хватит..."
    mr_cow "Нам нужно раскрыться Максу и клубу."
    mr_bird "Ты не довер-р-ря-я-яешь р-р-роди-и-ителям?!"
    mr_cow "Доверяю."
    mr_bird "Так а какого хр-р-ре-е-ена ты не хочешь р-р-раскр-р-рыва-а-аться перед ними?!"
    mr_bird "Какой же ты др-р-ру-у-уг после этого, а-а-а?!"
    mr_cow "Никто никого не слышит."
    mr_bird "Вс-с-сё-ё-ё!"
    mr_bird "Я полетел отсю-ю-юда!"
    mr_bird "Меня больше не-е-ет!"
    mr_bird "Я полетел кида-а-аться в невидимые стё-ё-ёкла!"
    s "Птиц, успокойся!"
    mr_bird "С-С-Сайо-о-ори!"
    mr_bird "Почему он тако-о-ой?!"
    mr_bird "Пр-р-реда-а-атель и лицеме-е-ер-р-р?!"
    mr_cow "Хватит каркать."
    mr_bird "Ты не кор-р-ро-о-ова!"
    mr_bird "Ты свинья-я-я!"
    s "МОЯ ГОЛОВА!" with vpunch
    s "Всё кругом идёт!"
    s "Вас наслушаешься -- в петлю полезешь!"
    s "Не вернусь сюда, пока тучки не рассеятся!"
    s "Бе-е-е!"
    stop music fadeout 1.0

    scene black with wipeleft_scene
    mr_bird "{size=19}Кар-р-р?!{/size}"
    mr_cow "{size=19}Докаркался, пернатый?{/size}"
    call window_close

    pause 1.0
    call plot_transition

    call window_open
    scene bg sayori house livingroom night with wipeleft_scene
    s "Мама?"
    show sayori_mom happ om oe rhip glasses at t11
    sm "Что такое?"
    show sayori_mom cm
    s "Э-э-э...{w}нергии много, а скоро спать ложиться..."
    show sayori_mom om ce
    sm "Хах, хочешь, чтобы я тебе что-то почитала на сон грядущий?"
    show sayori_mom cm
    s "Угусь~"
    show sayori_mom om oe
    sm "Тогда присаживайся."
    show sayori_mom cm

    scene black with dissolve
    pause 0.25
    s "Уф!"
    sm "Я недавно нашла одну очень добрую интерпретацию сказки, которую ещё нигде не видела."
    s "Какой именно?"
    sm "Про богиню солнца -- Аматэра{image=accent_low_register}{space=-15}су."
    s "Хм..."
    "На самом деле я не очень люблю сказки, но мама их так рассказывает, что весь мир забывается..."
    sm "Советую закрыть глазки, чтобы проще было слушать."
    s "Да, я уже."
    sm "Готова?"
    menu:
        "Слушать очень внимательно (kwargs=#00e2e5, #a8ffff)":
            $ tale_amaterasu_full = True
        "Слушать вполуха (kwargs=#00e2e5, #a8ffff)":
            $ tale_amaterasu_full = False
        "Стоит ли вникать в сказку или лучше расслабиться?..."
    s "Да."
    sm "Тогда я начинаю."
    sm "Кхм-кхм..."
    play music amaterasu
    window hide
    sm_nvl "Когда-то давным-давно богиня солнца, Аматэрасу, вступила на трон в далёком голубом небосводе." with Dissolve(1.0)
    sm_nvl "Её сияние служило радостной вестью всему на свете."
    if tale_amaterasu_full == True:
        sm_nvl "Орхидеи и ирис, цветы вишен и слив, целые рисовые поля -- все отвечали ей улыбкой, а озёра и воды отражали её свет в тысячах сверкающих бликах."
    sm_nvl "Но у Аматэрасу был брат, владыка океанов и месяца, -- Сусано{image=accent_low_register}{space=-15}о."
    nvl hide Dissolve(1.0)
    nvl clear

    call window_dialog("mc")

    scene bg bedroom
    show dark
    with dissolve_cg
    pause 0.5
    window auto
    mc "Да что ж не спится..."
    "Почему-то я уверен, что Сайори сейчас дрыхнет без всяких задних мыслей."
    "А я тут, как дурак, верчусь, уснуть не могу."
    sm "Он очень завидовал славе и всепокоряющей власти сестры."
    "Да-а-а, как же ей всё-таки проще живётся, чем мне..."
    sm "Её голос и улыбка излучали свет, который проникал в отдалённые места."
    if tale_amaterasu_full == True:
        sm "Её рисовые поля всегда приносили урожай с избытком, находились ли они на откосе горы, в густой долине или подле бушующего водопада."
        sm "Её фруктовые деревья всегда склонялись под тяжестью сочных плодов."
    else:
        sm "Её рисовые поля всегда приносили урожай с избытком, ..."
    sm "А голос Сусаноо не был так чист, его улыбка не была такой сияющей."
    sm "Его поля часто затопляло, и они гибли."
    "Ой, ладно, надо спать, чтобы завтра пораньше начать готовиться к учёбе..."
    "Ни капли нормального расслабления..."
    scene black with dissolve_cg

    call window_dialog("s")

    window hide
    sm_nvl "Зависть и досада бога месяца не имели границ, но Аматэрасу была бесконечно терпелива к нему и всё прощала." with Dissolve(1.0)
    sm_nvl "Однажды она сидела во дворе своего небесного жилища и занималась пряжей..."
    sm_nvl "...как вдруг с небосвода к её ногам упал раненый пегой конь -- любимец всех богов."
    sm_nvl "Аматэрасу думала, что завистливый Сусаноо ранил его, чтобы так отомстить ей."
    sm_nvl "Она содрогнулась от страха, отвела коня на лечение своим воинам, приказала его защищать, а сама удалилась в пещеру небесного жилища."
    sm_nvl "Весь мир погрузился во мрак."
    sm_nvl "Радость и добродушие, душевная чистота и мир, надежда и любовь — всё исчезло с угасшим светом."
    if tale_amaterasu_full == True:
        sm_nvl "Злые духи, которые таились по тёмным углам, отважились выйти на волю и бродить повсюду."
        sm_nvl "Их ужасающий смех и помрачающие разум песни наполняли ужасом сердца тех, кто их слышал."
    else:
        sm_nvl "Злые духи, ..., стали бродить повсюду."
    sm_nvl "Боги не могли смириться со всем этим: они собрались и стали думать, что делать."
    sm_nvl "Все знали, что только одна Аматэрасу способна всё исправить."
    sm_nvl "Но чем им побудить вернуться ей в этот мир мрака и раздора?"
    sm_nvl "Долго думали боги, и, наконец, был найден план, как вывести богиню из заточения."
    sm_nvl "Они заставили Сунаноо раскаяться за свою зависть перед Аматэрасу, предложив ему держать зеркало перед входом в пещеру."
    sm_nvl "Потом одна часть богов занялась изготовлением ширмы из рисовой соломы, чтобы закрыть ей вход в пещеру, когда богиня выйду наружу."
    sm_nvl "Другая часть богов готовила музыкальные инструменты, чтобы развеселить Аматэрасу."
    sm_nvl "Как только все приготовления были завершены, Сусаноо подошёл к пещере с зеркалом в руках."
    sm_nvl "Своим громким голосом он попросил Аматэрасу выйти наружу, но она его не послушала."
    nvl hide Dissolve(1.0)
    nvl clear

    call window_dialog("m")

    scene bg monika house bedroom night 1 with dissolve_cg
    pause 0.5
    window auto
    "Наконец-то..."
    m "Наконец-то мы окончательно станем официальным клубом спустя ПОЛГОДА!"
    m "А-А-А-А-А, как я же я рада!" with vpunch
    sm "Тогда началось великое торжество, в котором Уцу{image=accent_call_high_register}{space=-15}ма, богиня радости, громко запела и стала водить хоровод."
    m "Всё-всё, Моника, успокойся, тебе надо уснуть..."
    m "Это ведь всего лишь очередной новенький, который так же покинет нас через несколько дней после вступления, но..."
    sm "Она играла на бамбуковой флейте, а множество мириадов божеств сопровождали её своими музыкальными инструментами."
    m "Нет, он ТОЧНО останется с нами!"
    m "Сообщу о нём остальным в тот же день, когда он нас навестит."
    m "Пусть это будет приятным сюрпризом..."
    sm "Радость взяла свое."
    m "И-И-И-И-И, я не могу успокоиться!"
    sm "Ряды богов становились всё оживлённее и оживлённее, и в итоге все засмеялись так, что небо содрогнулось словно от грома."
    m "Ха-ха-ха, как же я рада!" with vpunch
    scene black with dissolve_cg

    call window_dialog("s")

    window hide
    sm_nvl "От этого Аматэрасу опасливо выглянула из своего убежища и спросила: \"Что это значит?\"" with Dissolve(1.0)
    sm_nvl "\"Я думала, небо и земля погружены во мрак, но вижу свет. Уцума пляшет, и все боги смеются!\""
    if tale_amaterasu_full == True:
        sm_nvl "А сама Уцума ответила ей: \"Я могу танцевать, и боги могут смеяться, потому что среди нас теперь есть божество, чья красота подобна твоей!\""
    else:
        sm_nvl "А сама Уцума ответила ей: \"...потому что среди нас теперь есть божество, чья красота подобна твоей!\""
    sm_nvl "\"Погляди-ка!\""
    sm_nvl "Аматэрасу бросила взор на зеркало в руках Сусаноо и страшно изумилась, заметив в нём богиню сверхъестественной красоты."
    sm_nvl "Она вышла из пещеры, и перед входом тотчас же была опущена ширма рисовой соломы."
    sm_nvl "Богиня увидела улыбающееся лицо Сусаноо и почуствовала тепло, которое никогда не испытывала за всё время."
    sm_nvl "Свет богини рассеял мрак и злых духов, а вместе с ними страхи и горе."
    sm_nvl "И воскликнули тогда божества: \"Да не покинет нас богиня солнца!\""
    nvl hide Dissolve(1.0)
    nvl clear
    window auto
    s "{cps=20}Да не покинет нас...{w}богиня солнца...{/cps}"
    call window_close

    call window_dialog("mc")
    $ sm_name = _("Юко-сан")

    return
