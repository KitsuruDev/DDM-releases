
label act_1_day_9:

    play sound none_transition
    scene black
    show screen new_day(episode)
    pause 4.0
    hide screen new_day
    scene black
    with dissolve_scene_full

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d8.unlocked == False:
        $ ach_a1_d8.unlock()
        pause 7.0
    else:
        pause 3.0

    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    scene bg monika house bedroom morning with dissolve_scene_full
    call autosave
    "...да, я не выспался."
    "Опять, снова -- называйте это, как хотите."
    "Чувствуется сплошное раздражение."
    "Но и сказать, что очень рано встал, тоже нельзя."
    "По ощущениям где-то через полчаса после кошмара начало подниматься солнце."
    "В итоге, я не выдержал, пошёл заниматься утренней рутиной."
    "Заодно переоделся в свою форму и приготовил себе кашу, которую только что съел."
    "Теперь вот принёс порцию Монике, которую надо сейчас поднять."
    mc "Мони..."
    m "{cps=20}М-м-м...{/cps}"
    mc "Подъём, Моника!"
    mc "Нас ждёт очередной замечательный день в чёртовой школе!"
    m "{cps=20}Ма-а-акс...{w}ещё 5 минут...{/cps}"
    mc "Нет, Мони, всё, просыпайся."
    m "{cps=20}Умф-ф-ф...{/cps}"
    show monika forward body pants neut om eyes_tsed_2 at e11
    m "{cps=20}С добрым у-у-у--{/cps}{nw}"
    show monika shoc om oe n4 at tfast
    m "--тром?!"
    show monika cm
    m "П-почему..."
    show monika md
    mc "Ты без одежды?"
    show monika curi md oe
    mc "А ты не помнишь?"
    show monika om e1b
    m "А-а-а...{w}кексы, чаепитие, вино..."
    show monika oe
    m "Ты нёс меня до дома..."
    show monika ce
    m "Что-то...{w}на этом всё размывается..."
    show monika md
    mc "Ничего такого не было, если что."
    show monika neut cm oe
    mc "Юри через Сайори принесла тебе имбирь, который ты уже съела."
    show monika e2a
    mc "Ты полностью разделась из-за жары."
    mc "Пыталась меня в таком образе поцеловать, но тебя начало тошнить и потом вырвало."
    show monika oe
    mc "К счастью, я успел довести тебя до туалета."
    mc "Потом мы переместились сюда и ты сразу легла, а я сделал своё и твоё домашнее задание."
    mc "Тебе, кстати, надо быстро переписать его своим почерком."
    mc "Но сначала вон на столе, каша."
    mc "Твоя порция."
    mc "Свою я уже съел."
    show monika sad om e4c
    m "Подожди, Макс, у меня голова сейчас взорвётся!"
    show monika md
    mc "Тебе всё ещё плохо?"
    show monika dist om oe
    m "Н-нет, с состоянием всё в порядке, разве что немного помятая..."
    show monika neut om oe
    m "Я образно выразилась."
    show monika cm
    mc "Я так понимаю, ночь ты тоже не помнишь?"
    show monika om
    m "Нет."
    show monika cm
    mc "Ты иногда дрыгалась."
    mc "Приходилось тебя успокаивать."
    show monika e2a
    mc "А один раз ты меня пихнула, причём когда мне кошмар снился."
    show monika worr cm e1a
    mc "В итоге, я нормально не выспался."
    mc "Короче, примерно то же самое, что и вчера, только с кошмаром."
    show monika om
    m "Ох..."
    show monika happ cm oe b1b
    mc "Хорошо я решил с тобой остаться."
    show monika om
    m "...ах, спасибо..."
    show monika cm
    mc "Вроде про всё рассказал..."
    show monika brow
    mc "В общем, ешь кашу, она лёгкая, желудок не нагрузится сильно."
    m "М-м."
    show monika e1b b1b
    mc "И больше НИКАКОГО алкоголя, ладно?"
    show monika oe
    mc "Мне твоё здоровье жалко."
    show monika om
    m "Согласна..."
    show monika worr om oe brow
    m "Вышло всё в разы тяжелее, чем я думала..."
    show monika cm
    "Вот поэтому не надо недооценивать что-либо."
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day with wipeleft_scene
    m "{size=19}Всё, Макс, я готова!{/size}"
    mc "Отлично."
    show monika forward happ cm oe school_bag at t11
    pause 0.2
    show monika neut om eyes_tsur_3
    m "Выходит, я даже не развязывала свой бант?"
    show monika cm
    mc "Хм, да..."
    "Я так к нему привык, что даже этого не заметил..."
    show monika happ om oe
    m "Ну и ладно."
    show monika lean happ om oe school_bag at h11
    m "Я уже так наловчилась его завязывать, что совсем не ощущаешь."
    show monika cm
    mc "Я, конечно, рад за тебя, но ты всё выключила и закрыла?"
    show monika forward happ om oe school_bag
    m "...думаю, да."
    show monika cm
    mc "Тогда берём сумки и выходим."
    show monika ce
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg monika house outside day
    show monika forward happ cm e1b school_bag at t11
    with wipeleft_scene
    show monika neut om oe
    m "Кстати, ты говорил про кошмар..."
    show monika cm
    mc "А, снова всякая хрень приснилась."
    show monika worr cm e1a
    mc "Резко из-за неё тогда вскочил."
    show monika om
    m "У тебя нет каких-нибудь психологических проблем?"
    show monika cm
    mc "Моника, я так с ходу не отвечу."
    show monika neut cm oe
    mc "Но, кроме кошмаров, нет ничего особенного."
    show monika om e1b
    m "Странно."
    show monika cm
    mc "Думаю, это из-за нервов."
    show monika oe
    mc "Пройдёт условная неделька и уже буду в норме."
    show monika om lpoint
    m "Смотри, лучше обсуди это с тем психологом."
    show monika cm ldown
    mc "Если я смогу его найти и если он захочет меня слушать."
    show monika e2b
    s "{size=16}Пха!{/size}"
    s "{size=18}Пхе!{/size}"
    s "{size=20}Ха-а-а...{/size}"
    show sayori turned nerv me ce n2 school_bag at l21
    show monika curi cm oe at t22
    pause 0.5
    m "Сайори?"
    show sayori mh
    show monika neut cm oe
    s "Что ж вы так...{w}рано?"
    show sayori neut mf e4a
    s "Фу-у-у..."
    show sayori cm
    mc "Разве?"
    show sayori om oe b1d
    s "Да!"
    show sayori e2b -b1d rup
    s "Я вышла с запасом на всякий случай, потом подумала, что, вот, опять придётся ждать, зря так рано пошла..."
    show sayori oe rdown
    s "А вы, оказывается, уже на улице!"
    s "Пришлось нестись на всех парах."
    show sayori e2c
    s "И вот я...{w}тут."
    show sayori curi cm oe
    show monika om
    m "Но зачем?..."
    show sayori om
    show monika cm
    s "Как зачем?"
    show sayori happ om oe
    show monika happ cm oe
    s "Тебя проведать!"
    show sayori cm
    show monika om ce
    m "А, спасибо, Сайори, со мной всё отлично."
    show sayori neut om oe b1f
    show monika cm
    s "Да?"
    show sayori -b1f
    show monika nerv cm e2c at s22
    s "А то вчера мне Макс сказал, что ты была в плачевном состоянии."
    show sayori cm
    mc "Ну это было вчера."
    show sayori happ cm oe
    show monika happ cm oe at t22
    mc "Потом Монике значительно полегчало, особенно после имбиря."
    "Во время поедания её сонное скривившееся лицо всем своим видом так и кричало об улучшении самочувствия."
    mc "Спасибо, Сайори."
    show sayori om ce lup rup at h21
    s "На то я вице-президент!"
    show sayori laug cm oe ldown rdown
    show monika om ce
    m "Нет, на то ты и Сайори, ха-ха!"
    show sayori tap nerv om oe school_bag at s21
    show monika cm
    s "Э-хе-хе~"
    show sayori turned happ cm oe school_bag at t21
    show monika oe
    mc "А как там дела с Юри?"
    show sayori om
    s "Сегодня утром она мне написала, что всё оки-доки."
    show sayori neut cm oe
    show monika neut cm oe
    mc "Не будем к ней заходить, чтобы удостовериться?"
    show sayori om e2b
    s "Ну..."
    show sayori oe
    s "Нацуки вчера говорила, что зайдёт к ней."
    show sayori happ cm oe
    show monika happ om oe lpoint
    m "Как раз, если вдруг что -- напишет нам."
    show monika cm ldown
    mc "Ладно."
    mc "Предлагаю потихоньку двигаться к школе, пока есть время."
    show sayori happ om ce lup rup at h21
    show monika ce
    s "Ок-ке!"
    show sayori cm ldown rdown

    scene bg niigata street suburban 11 day
    show sayori turned happ cm e1b school_bag at t21
    show monika forward happ cm e1c school_bag at t22
    with wipeleft_scene
    show sayori om
    show monika oe
    s "Интересно, кто такая эта Котоноха?"
    show sayori cm oe
    show monika om lpoint
    m "Не терпится познакомиться?"
    show sayori ce
    show monika cm ldown
    s "Угусь!"
    show sayori neut cm oe
    show monika neut cm oe
    mc "А вы хотя бы обсудили, где и когда всё будет происходить?"
    show sayori curi om e2b
    s "Э-э-э..."
    show sayori cm
    mc "Мда."
    show sayori neut cm oe
    show monika mh lpoint rhip
    m "Тут вариантов немного: либо большая перемена ближе к середине дня, либо после уроков."
    show sayori happ om oe
    show monika cm ldown
    s "Лучше на перемене."
    show sayori ce
    show monika laug ma oe rdown
    s "Потому что тогда Котоноха сможет прямо сегодня вступить в наш клуб!"
    show sayori cm
    mc "Ну ты такие ожидания не возводи."
    show sayori neut cm oe
    mc "Мало ли, что там может случится."
    mc "Вдруг ей не захочется."
    show sayori happ cm oe
    show monika happ om oe
    m "Макс прав, но и унывать не будем."
    show monika lpoint
    m "Главное, чтобы Нацуки кекс не забыла."
    show monika laug cm oe ldown
    mc "Ага, главный козырь?"
    show sayori ce
    show monika om ce
    m "Ха-ха-ха!"
    show monika cm

    scene bg school gate 1
    show sayori turned happ cm ce school_bag at t21
    show monika forward happ cm e1b school_bag at t22
    with wipeleft_scene
    show sayori oe
    show monika oe
    mc "Ладно, ребят, пора расходиться."
    show monika om
    m "Увидимся в клубе."
    show sayori om ce lup rup at h21
    show monika cm
    s "Да, до скорого!"
    show sayori cm at thide
    hide sayori
    show monika ce at thide
    hide monika
    pause 1.0
    "Потенциальное пополнение, значит?"
    "Надеюсь, по характеру Котоноха будет нормальным человеком..."
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("s")

    call window_open
    scene black with dissolve_scene_full
    play noise_1 school_corridor_light_noise fadein 3.0 volume 0.5
    s "{cps=25}У-у-у-у-у-ум-м-м-м-м-м...{/cps}"
    "{cps=25}Двигаться совершенно не хочется...{/cps}"
    "{cps=25}Всё тело вялое...{/cps}"
    "{cps=25}...{/cps}"
    mi "Не спи -- замёрзнешь."
    s "{sc=2}Кья?!{/sc}" with vpunch

    scene bg school new_class_sayori day
    show mrs_ida happ omb ce at t11
    with dissolve
    mi "Ха-ха-ха!"
    show mrs_ida om oe
    mi "У нас тут прохлада из-за сквозняков, а ты прямо под ними заснула."
    show mrs_ida cm
    s "Я не спала!"
    s "Ух..."
    show mrs_ida om be
    mi "Ой, да ладно."
    show mrs_ida -be
    mi "Я же знаю, что ты не заядлая любительница социологии."
    show mrs_ida cm
    s "Не сказала бы так..."
    show mrs_ida om
    mi "Тем не менее под конец ты утомилась и легла на парту."
    show mrs_ida cm
    s "..."
    "Ну всего лишь один раз..."
    show mrs_ida neut om oe
    mi "Уже большая перемена началась."
    show mrs_ida happ om oe
    mi "Предлагаю тебе не терять время и заняться своими делами."
    mi "Или встретиться с друзьями."
    show mrs_ida cm
    "Большая перемена..."
    s "Ох, точно..."
    s "Я побежала, Ида-сэнсэй!"
    show mrs_ida ce
    s "До свидания!"
    show mrs_ida om
    mi "Удачи~"
    show mrs_ida cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 school_corridor_hard_noise fadein 3.0
    scene bg school f3 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    with wipeleft_scene
    "И где же искать Нацуки?"
    "Здесь так шумно и дискомфортно..."
    "Возможно, стоит ей написать, но прочтёт ли?"
    s "Ай..."
    "В туалет захотелось..."
    s "Бу-у-у!"
    "Придётся идти в конец коридора--{nw}"
    show natsuki turned fc neut cm oe school_bag at t11 zorder 2
    pause 0.2
    show natsuki happ om oe lhip rhip
    n "О, а вот и ты."
    n "Не прогадала с коридором."
    show natsuki neut cm oe
    s "Нацуки?"
    show natsuki om ldown rdown
    n "Да, я."
    n "Кекс у меня."
    show natsuki rhip
    n "Котоноха сейчас в межкорпусном коридоре на втором этаже."
    n "Если ты хочешь поговорить с ней, то сделать это надо прямо сейчас."
    show natsuki e1b
    n "В противном случае она уйдёт, либо будет слишком мало времени для разговора."
    show natsuki angr cm oe
    s "Но я--{nw}"
    show natsuki om lhip
    n "Сайори, время!"
    show natsuki ldown rdown
    n "Пошли!"
    show natsuki cm
    s "Стой, Нацуки, я же хочу--{nw}"
    hide natsuki
    show natsuki turned fc angr om ce school_bag at el11 zorder 2
    with dissolve
    n "Потом, всё потом!"
    show natsuki cm

    scene black with wipeleft_scene
    s "Да нет же!"
    s "Я реально--{nw}"
    n "Я же сказала: \"Потом!\""
    n "Нельзя упускать шанс!"
    s "На-а-ацу-у-уки-и-и!"
    "Ну почему именно сейчас?!"
    window hide

    pause 5.0

    window auto
    n "Так, вот она!"
    n "Вот кекс."
    n "Ноги в руки и вперёд!"
    s "А ты?!"
    n "А у меня дела!"
    n "Если хочешь, могу Макса на помощь отправить."
    s "Конечно!"
    n "Поняла, напишу ему."
    s "Я вообще думала, что мы вместе будем!"
    n "Жизнь жестока, Сайори, мне надо решить вопрос с одним учителем."
    n "Всё, вперёд!"
    s "Ких-х!"
    "Толкать-то зачем?!"

    scene bg school f2 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    with wipeleft_scene
    "Всё хорошо, Сайори, ты справишься..."
    "Ты быстро разговоришь Котоноху, подаришь ей кекс и побежишь в туалет."
    "Ты же вице-президент!"
    "Твоя обязанность -- завлекать новых людей!"
    "У тебя есть в этом хороший опыт!"
    show kotonoha neut cm e1b rhid at t22 zorder 3
    "А вот и она..."
    "Итак, мой выход!"
    show kotonoha oe
    s "П-привет!"
    show kotonoha happ om oe lup
    k "О...{w}привет."
    show kotonoha cm ldown rdown
    s "Я..."
    k "..."
    s "Э-э-э..."
    "Из-за живота все мысли скомкались!"
    show kotonoha neut cm oe
    "Как же я там хотела сказать?!"
    show kotonoha om
    k "Ой, ты же из..."
    show kotonoha happ cm oe
    s "...Литературного клуба."
    show kotonoha om
    k "Да, точно."
    k "Сайори?"
    show kotonoha cm
    s "Да!"
    show kotonoha om ce
    k "Ох, я угадала!"
    show kotonoha cm
    s "Э-хе-хе~"
    show kotonoha om oe lself rhip
    k "Просто мне иногда Нацуки и Юри рассказывали о ваc."
    show kotonoha cm ldown
    s "У-у, как раз я..."
    show kotonoha neut cm oe
    "{sc=1}Ай...{/sc}"
    "{sc=1}Я вытерплю!{/sc}"
    show kotonoha om
    k "Ты только не стесняйся, Сайори."
    show kotonoha happ om ce rdown
    k "Мне не менее волнительно, хе-хе."
    show kotonoha cm oe
    s "В общем..."
    "{sc=1}Животик, прекрати, дай мне закончить начатое!{/sc}"
    $ l_name = "???"
    s "Я хотела тебя при--{nw}"
    show libitina forward sad cm oe at t21 zorder 2
    show kotonoha neut cm oe
    pause 0.2
    show libitina om ce
    l "Извини, Котоноха, немного задержалась..."
    show libitina cm
    play music libitina_playful
    "{sc=1}Кто это вообще?!{/sc}"
    show libitina neut cm oe
    show kotonoha om
    k "Ничего-ничего, я понимаю."
    show libitina shy happ om oe
    show kotonoha happ cm oe rhip
    l "О, я вижу, ты зря время не теряешь, хах?"
    show libitina forward happ om oe
    l "Привет."
    show libitina cm
    s "П-привет!"
    show libitina sad om oe
    l "Извини, если напугала."
    show libitina happ cm oe
    s "Всё хорошо!"

    if persistent.add_random_menu == 10:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    $ l_name = _("Либитина")
    show libitina om
    l "Если что, меня зовут Либити{image=accent_low_register}{space=-15}на."
    show libitina cm
    s "А я Сайори!"
    show libitina om ce
    l "Приятно познакомиться!"
    show libitina cm
    s "Угусь~"
    "{sc=1}Какое необычное имя...{/sc}"
    show libitina oe
    show kotonoha om
    k "Сайори, так ты что-то хотела, да?"
    show kotonoha cm
    s "Да, я..."
    "{sc=1}Кекс...{/sc}"
    "{sc=1}...нет, я не кекс...{/sc}"
    show kotonoha neut cm oe rdown
    s "...я хотела..."
    "{sc=1.5}Как я его отдам Котонохе на глазах Либитины?!{/sc}"
    "{sc=1.5}Она же её подруга, тоже кекс захочет!{/sc}"
    "{sc=1.5}Или её тоже пригласить в клуб?{/sc}"
    show libitina neut cm oe
    show kotonoha lsur cm oe
    s "...хотела тебя пригласить к нам в клуб!"
    "{sc=1.5}Терпитерпитерпитерпитерпи--{/sc}{nw}"
    show kotonoha om
    k "Оу..."
    show libitina happ cm oe
    show kotonoha happ omb ce
    k "Ха-ха-ха!"
    show kotonoha om oe rhip
    k "На самом деле, я уже думала над этим."
    show libitina shy happ om oe
    show kotonoha cm
    l "Ты всё-таки решила податься в клубную деятельность?"
    show libitina cm
    show kotonoha nerv om oe
    k "Ну это громко сказано..."
    show libitina neut om eb
    show kotonoha neut cm oe
    l "Просто уже последний год, да и ты всё ещё «вольная особа»..."
    show libitina cm
    "{sc=1.5}Она что, «аристократка», чтобы такими\nсловечками разбрасываться?!{/sc}"
    show libitina oe
    show kotonoha om
    k "В Литературном не так много людей, часть из которых я уже знаю."
    show kotonoha e1b
    k "Тем более меня уже не первый раз туда приглашают..."
    show libitina forward neut cm oe
    show kotonoha cm
    "{sc=1.5}Если это правда, то мои шансы на успех\nстремительно растут!{/sc}"
    show libitina om
    show kotonoha oe
    l "Ох, что это у тебя, Сайори?"
    show libitina cm
    show kotonoha rdown
    s "А?"
    s "Где?"
    show libitina om
    l "В руках."
    show libitina cm
    s "А-а-а!"
    s "Это кекс."
    show libitina happ cm oe
    show kotonoha happ om oe
    k "Кекс?"
    show kotonoha cm
    s "...да, для тебя!"
    s "Но отдам его только тогда, когда ты решишься."
    show kotonoha ce
    show libitina shy happ om ce
    l "Хе-хе, интересный ход..."
    show libitina cm
    s "Ага!"
    show libitina forward happ cm oe
    show kotonoha oe
    s "Так что думаешь, Котоноха?"
    show kotonoha e1b rhip
    k "Хм..."
    show libitina om oe
    show kotonoha nerv cm oe
    l "...как бы съесть тот кексик, да?"
    show libitina shy happ om eb
    l "А если он выпечен самой Нацуки?"
    show libitina cm
    show kotonoha happ omb ce
    k "Ха-ха-ха!"
    show libitina om ce
    show kotonoha cm
    l "Ха-ха-ха!"
    show libitina cm
    "{sc=3}А-а-а, мне ещё сильнее в туалет захотелось!{/sc}"
    "{sc=3}Макс, помоги, я больше не могу терпеть!{/sc}"
    call window_close

    $ l_name = "???"

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(0.2, 0, "music")
    stop noise_1
    play noise_1 wind

    call window_open
    scene bg school old_rooftop day
    mc "Ф-ф-ф..."
    mc "А-а-а..."
    "Свежий воздух и тишина..."
    call skip_block_on

    pause 1.0
    play phone_sound new_message_mc
    pause 1.0
    play phone_sound new_message_mc
    pause 1.0

    $ contact_list["mc"].append("mc_n_chat")

    python in phone.system:
        cellular_data = True
        wifi = False
        battery_level = 78
        clock = (12, 42)

    phone register "mc_n_chat":
        time year 2018 day 24 month 4 hour 12 minute 41
        "n" "Макс, слышишь тут это"
        "n" "У Сайори с Котонохой разговор сейчас есть"

    mc "Что там такое..."
    phone discussion "mc_n_chat"
    $ plot_pause()
    phone discussion "mc_n_chat":
        "mc" "В клуб вербует?"
        "n" "Да"
        "n" "И ей не помешает помощь"
    stop music fadeout 3.0
    $ phone.system.clock = (12, 43)
    "Вы угораете?"
    "Я только пришёл сюда подышать!"
    phone discussion "mc_n_chat":
        "mc" "А ты?"
        "n" "Мне надо разобраться в одном вопросе с одним учителем, поэтому нини"
        "mc" "А остальные?"
        "n" "Без понятия"
        "n" "Так, ты ей друг или кто???"
        "mc" "Слушай, а ловко ты это придумала..."
    $ phone.system.clock = (12, 42)
    phone discussion "mc_n_chat":
        "mc" "Я даже в начале не понял"
        "mc" "Молодец"
        "n" "ХОРОШ ТУТ УМНИЧАТЬ!!!"
        "n" "Другого времени просто нет!"
        "n" "Давай, руки в ноги и бегом ей на помощь!"
        "mc" "Где она?"
        "n" "Межкорпусный коридор, 2 этаж"
        "mc" "Ясно, иду"
        "mc" "И не надо тут мне командовать"
        "n" "Бебебе!"
    $ phone.system.clock = (12, 42)
    phone discussion "mc_n_chat":
        "mc" "С бабаба"
        "n" "Иди давай уже!"

    phone end discussion transition

    call skip_block_off
    mc "Вот вы все...{w}торопливые..."

    scene black with wipeleft_scene
    "Будто эта Котоноха вот-вот и испарится с концами."
    "Нет, я понимаю, что Сайори умеет в коммуникацию, но..."
    stop noise_1 fadeout 3.0
    "Ни Юри, ни Моники в качестве подстраховки..."
    "Первая хоть знакома с Котонохой."
    "Ай, чёрт с вами!"
    "Толку от этих размышлений..."
    call window_close

    call plot_transition

    $ l_name = "???"
    play noise_1 school_corridor_hard_noise fadein 3.0
    pause 1.0

    call window_open
    "Опа, вот и Сайори..."
    l "{size=19}А стоит ли тебе вступать в какие-либо клубы?{/size}"
    "Так, стоп."
    l "{size=19}У тебя будет меньше времени и больше дел...{/size}"
    "Почему их 3 человека?"
    l "{size=19}С Юри и Нацуки ты и так общаешься.{/size}"
    "Котоноха, наверное, та, к которой сейчас обращаются..."
    "По комплекции схожа с Юри, прямо как говорили..."
    k "{size=19}Не знаю...{/size}"
    k "{size=19}Но почему бы просто не попробовать?{/size}"
    s "{size=19}Мы были бы рады, если бы у нас появился новый участник...{/size}"
    "Бедная Сайори, вся на нервах, переминается с ноги на ногу..."
    l "{size=19}Котоноха, прими тот факт, что последний учебный год более нагруженный, нежели остальные.{/size}"
    l "{size=19}Надо будет ещё к выпускным экзаменам готовиться и выбирать вектор дальнейшего развития жизни, если ты ещё этим не занималась.{/size}"
    k "{size=19}Я понимаю.{/size}"
    s "{size=19}У нас не так сложно!{/size}"
    s "{size=19}Всего лишь небольшие стихи, которые не каждый день пишем...{/size}"
    l "{size=19}...а также проводить время с членами клуба, участвовать в различной деятельности и так далее.{/size}"
    s "{size=19}Но ведь в этом и смысл.{/size}"
    s "{size=19}Мы становимся друзьями, которые держутся друг за друга.{/size}"
    l "{size=19}Да, Сайори, я это осознаю, однако, к сожалению, сейчас не самое удачное время для нечто подобного.{/size}"
    l "{size=19}Хотя потом, если так подумать, никаких клубов не будет...{/size}"
    k "{size=19}Умф...{/size}"
    "Так, всё, надоело стоять в стороне."
    "Надо помочь."

    $ renpy.music.set_volume(1.0, 0, "music")

    scene bg school f2 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    show libitina forward neut cm ce at t31 zorder 2
    show sayori turned neut cm oe b1b school_bag at t32 zorder 3
    show kotonoha neut cm e1b at t33 zorder 2
    with wipeleft_scene
    play music libitina_playful
    show libitina oe
    show sayori lsur om oe -b1b lup rup at h32
    show kotonoha lsur cm oe
    s "О-о-о, Макс!"
    show sayori cm ldown rdown
    pause 0.1
    hide sayori
    show sayori turned pani cm oe school_bag at e11 zorder 3
    with dissolve
    pause 0.25
    show sayori om
    s "Вот, держи!"
    show sayori cm
    mc "Апф, а-а-а-а--{nw}"
    show sayori om
    s "Дальше ты сам!"
    show sayori cm ce at lhide
    play sound sayori_hide_fast
    hide sayori
    pause 0.2
    mc "..."
    show libitina at t21
    show kotonoha neut om oe at t22
    k "Что это с ней?"
    show libitina om ce
    show kotonoha cm
    l "Сама в неведении..."
    show libitina cm
    mc "Хм..."
    k "..."
    l "..."
    show libitina happ cm oe
    show kotonoha happ cm oe
    mc "...здрасьте?"
    show libitina om ce
    l "Ха-ха-ха!"
    show libitina cm
    show kotonoha om rhip
    k "Ты тоже из Литературного клуба?"
    show libitina oe
    show kotonoha cm
    mc "Да, неделю назад вступил."
    mc "Имя моё вы и так уже услышали..."
    show kotonoha om lself
    k "Я Котоноха, часто пересекаюсь с Юри и Нацуки."
    $ l_name = _("Либитина")
    show libitina om
    show kotonoha cm ldown
    l "Либитина, подруга."
    show libitina cm
    mc "Будем знакомы."
    mc "Однако..."
    show kotonoha neut cm oe rdown
    mc "У вас слишком необычные имена для японской школы."
    show libitina shy happ om ce
    l "Интересно слышать подобное замечание от человека с именем «Макс», хе-хе-хе..."
    show libitina cm
    show kotonoha sad om oe
    k "Да ну!"
    show libitina forward happ cm oe
    show kotonoha happ om oe
    k "Может, моё имя и непопулярное, но оно чисто японское."
    show kotonoha neut om e4a
    k "Обозначает лист дерева -- символ жизни и обновления."
    show kotonoha cm
    mc "А, угу..."
    show kotonoha happ cm oe rhip
    "Странно, что оно ввело меня в резонанс..."
    show libitina om
    l "А моё да, иностранное."
    show libitina neut om ce
    l "Происходит от латинского слова {color=#fc7e23}libitum{/color} -- воля и желание."
    show libitina shy neut om eb
    show kotonoha angr cm oe
    l "Хотя в римской мифологии богиня с таким именем имела дело со смертью и погребальными обрядами..."
    show libitina cm
    show kotonoha anno om oe
    k "Кх, опять твоя жуть!"
    show libitina oe
    show kotonoha angr om oe
    k "Откуда у тебя такая заинтересованность...{w}подобным?"
    show libitina forward neut om oe
    show kotonoha cm
    l "Разве это важно?"
    show libitina eb
    l "Эта информация тебе ничего не даст..."
    show libitina cm
    show kotonoha om ce
    k "Бех-х!"
    show libitina happ cm oe
    show kotonoha cm
    mc "То есть, если я правильно понял, ты иностранка?"
    show libitina om ce
    show kotonoha neut cm oe
    l "Угадал."
    show libitina oe
    l "Англия."
    show libitina cm
    show kotonoha happ cm oe
    mc "Ничего себе..."
    "Ну и кадр..."
    show libitina ce
    show kotonoha e1b
    "Ещё один богач среди бедного среднего класса?"
    show libitina om
    show kotonoha oe
    l "А-ха-ха, да ладно тебе."
    show libitina oe
    l "Душой мне больше здесь нравится."
    show libitina cm
    mc "Хм..."
    show libitina neut cm oe
    show kotonoha neut cm oe
    mc "Но не престижней ли получить образование там?"
    show libitina happ cm oe
    mc "В О{image=accent_high_register}{space=-15}ксфорде, например, или где-то ещё..."
    show libitina om
    l "Для меня особо сильной разницы нет."
    show libitina cm
    mc "Не сказал бы..."
    mc "Разве что Токи{image=accent_low_register}{space=-15}йский университет на похожем уровне, но туда трудно попасть, да и сильная нагрузка в учёбе--{nw}"
    show libitina om
    show kotonoha happ cm oe
    l "Именно туда я и хочу поступить."
    show libitina cm
    show kotonoha ce
    mc "ЧТО?!" with vpunch
    mc "Туда?!"
    show libitina shy happ om oe
    l "Да."
    show libitina forward happ cm oe
    show kotonoha oe
    mc "Ты уверена, что оно того стоит?"
    show libitina om
    l "Абсолютно: я уже всё проанализировала и обдумала."
    show libitina neut om eb
    l "У меня были ещё варианты с Университетом Тохо{image=accent_low_register}{space=-15}ку в префектуре Сенда{image=accent_low_register}{space=-15}й и с О{image=accent_high_register}{space=-15}сакским университетом в одноимённой префектуре..."
    show libitina happ om oe
    l "...но моих сил и знаний хватит для Токийского."
    show libitina cm
    show kotonoha ce
    mc "Ну и ну..."
    "Я сейчас сдохну от своей слабости и ничтожности."
    show libitina eb
    "Как вы, сверхразумы, вообще существуете?"
    "Откуда столько уверенности и знаний?"
    "Откуда такой склад ума?"
    "Как это у вас получается?!"
    show libitina oe
    show kotonoha oe
    mc "Так, ладно, что-то мы заболтались..."
    show kotonoha neut cm oe rdown
    mc "О чём вы разговаривали с Сайори?"
    "Не буду ж я в лоб говорить, что это всё спланировано..."
    show kotonoha om
    k "Она меня приглашала в ваш клуб."
    show kotonoha sad om ce
    k "А я не успела озвучить своё решение..."
    show libitina om ce
    show kotonoha happ cm ce
    l "Виной всему этот апетитный кексик~"
    show libitina cm
    show kotonoha om
    k "Ха-ха-ха!"
    show kotonoha cm
    mc "Ясно."
    show libitina oe
    show kotonoha neut cm oe
    mc "Так что думаешь?"
    show libitina neut cm oe
    show kotonoha e1b rhip
    k "М-м-м..."
    show libitina om
    l "Скоро выпуск, Котоноха, не забудь."
    show libitina cm
    show kotonoha anno om ce
    k "Да знаю я, знаю..."
    show libitina shy neut om oe
    show kotonoha cm
    l "Можно поинтересоваться?"
    show libitina cm
    show kotonoha neut cm e4a
    mc "М-м?"
    show libitina om
    show kotonoha oe
    l "Если Котоноха получит этот кекс после своего выбора, то могу ли я откусить от него маленький кусочек на пробу?"
    show libitina forward neut cm oe
    mc "Сайори обещала его отдать, когда Котоноха согласится вступить в клуб?"
    show libitina om
    l "Не совсем, но, в целом--{nw}"
    show libitina happ cm oe
    show kotonoha happ om oe lself
    k "Я согласна!"
    show libitina om ce
    show kotonoha cm ce ldown
    l "Ха-ха-ха-ха-ха!"
    show libitina cm
    show kotonoha oe
    mc "Правда?"
    show libitina oe
    show kotonoha om rdown
    k "Да, отметём все сомнения в сторону."
    show libitina om
    show kotonoha cm
    l "Ладно, это твой выбор."
    show libitina cm
    mc "Класс."
    mc "Держи."
    show kotonoha om ce
    k "Спасибо~"
    show kotonoha cm oe
    mc "Можете поделиться друг с другом."
    show libitina om
    l "Да, было бы здорово."
    show libitina neut cm oe
    show kotonoha rhip
    mc "Либитина, а ты не хочешь составить компанию?"
    "А вдруг получится?"
    show libitina worr om ce
    show kotonoha ce
    l "Нет-нет, у меня учёба много времени забирает, извини."
    show libitina cm
    show kotonoha om
    k "{size=19}У неё просто стихи писать не очень получается!{/size}"
    show libitina happ cm ce
    show kotonoha cm
    mc "{size=19}А-а-а, ага.{/size}"
    show libitina om oe
    l "Я всё слышала!"
    show libitina cm
    show kotonoha om
    k "Хе-хе-хе!"
    show libitina om
    show kotonoha cm
    l "Кстати, Макс, ты про своё имя не рассказал."
    show libitina cm
    show kotonoha oe
    mc "А..."
    mc "А что про него рассказывать?"
    mc "Родители назвали меня в честь музыкальной группу {color=#fc7e23}MAX{/color}, потому что они встретились на одном из её концертов."
    mc "Вот и вся история."
    show libitina shy neut om eb
    l "Хм, я думала, что ты тоже переехал в эту страну."
    show libitina happ cm oe
    mc "Неа, проще: я здесь родился."
    show libitina forward happ om oe
    l "Ясно."
    show libitina cm
    "Макс-Макс, Макс-Макс..."
    "Сколько раз я уже сказал про эту музыкальную группу?"
    show libitina shy happ om oe
    show kotonoha nerv cm oe
    l "Всё, Котоноха, теперь, когда ты в Литературном клубе, жду от тебя «глубокие» по чувствам и смыслу стихотворения."
    show libitina cm
    show kotonoha om
    k "Ну ты перебарщиваешь..."
    show libitina forward happ cm ce
    show kotonoha ce
    k "Хорошо будет, если меня на два четверостишия хватит!"
    show libitina om
    show kotonoha cm
    l "Ха-ха-ха!"
    show libitina cm oe
    show kotonoha neut cm oe rdown
    mc "Точно, тебе надо сегодня после уроков встретиться с кем-то из наших либо сразу прийти к..."
    mc "...блин, номер кабинета забыл..."
    show kotonoha happ cm oe
    mc "В общем, на втором этаже старого корпуса где-то в центре мы расположены."
    show kotonoha om
    k "Поняла."
    show libitina neut cm oe
    show kotonoha neut cm oe
    mc "Хотя чего я..."
    show libitina happ cm oe
    mc "Могу прямо сейчас показать."
    show kotonoha om lup
    k "Нет-нет, не надо, я без труда вас найду."
    show kotonoha happ cm oe ldown
    mc "Точно?"
    show kotonoha om ce rhip
    k "В крайнем случае напишу Юри или Нацуки."
    show kotonoha cm oe
    mc "Хорошо, будем ждать тебя."
    k "Угу."
    mc "Тогда на этом пока всё."
    mc "Извините, что задержал..."
    show kotonoha om
    k "Ничего-ничего."
    show libitina om
    show kotonoha cm
    l "Да, не нагружайся."
    show libitina shy happ om eb
    l "Всё-таки не каждый день в клуб приглашают."
    show libitina cm oe
    mc "Ладно, до встречи."
    show libitina forward happ cm oe
    show kotonoha om ce lup rhid
    k "Пока!"
    show libitina om
    show kotonoha cm ldown
    l "До встречи."
    show libitina cm
    stop music fadeout 3.0

    scene black with wipeleft_scene
    "Почему-то в моей голове был стереотип, что иностранцы прям сильно будут отличаться от коренных японцев."
    "А тут совсем не так: что Фукка, что Либитина..."
    "..."
    "Так..."
    "Надо всё рассказать Сайори."
    "Только куда её унесло?"
    "В туалет?"
    "По делам?"
    "Не найду же..."
    s "О, Макс, они уже ушли?"

    scene bg school f2 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    show sayori turned neut cm oe school_bag at t11 zorder 2
    with wipeleft_scene
    mc "А-а, вернулась?"
    show sayori happ cm oe
    mc "Да, Котоноха согласилась на вступление."
    show sayori dist om ce
    s "Фу-у-ух..."
    show sayori happ cm oe
    mc "После уроков зайдёт к нам, а там уже введём в курс дела."
    show sayori neut om oe
    s "Ты кекс отдал?"
    show sayori happ cm oe
    mc "Да, видишь?"
    mc "Руки пустые."
    show sayori om ce
    s "Хе..."
    show sayori cm oe
    mc "К слову, он реально сработал."
    mc "Ну или я про него рассказал уже на финишной прямой..."
    mc "В общем, пока что всё."
    show sayori om
    s "Большое спасибо."
    show sayori sad om ce
    s "Без тебя бы было намного труднее..."
    show sayori cm
    mc "Да, это хорошо, что я пришёл."
    show sayori pout cm oe
    mc "Нацуки побежала вперёд паровоза и чуть тебя под колёса не затянула."
    show sayori mg
    s "Ме-е-е..."
    show sayori mh
    s "Я как назло захотела в туалет: только отправилась, а она меня потащила."
    show sayori cm
    mc "Ясно..."
    "Теперь понятно, куда так Сайори рванула."
    "Я бы тоже бежал без оглядки..."
    show sayori neut cm oe
    mc "Окей, эта часть уже пройдена."
    show sayori om
    s "Ага."
    show sayori happ om oe
    s "Тогда я поищу Монику, хочу её обрадовать лично."
    show sayori cm
    mc "Само собой."
    show sayori om
    s "Я побежала."
    show sayori ce lup rup at h11
    s "Пока-пока!"
    show sayori cm ldown rdown at thide
    hide sayori
    mc "Пока, Сайо...{w}ри."
    "Торпеда..."
    stop noise_1 fadeout 5.0
    call window_close

    call window_dialog_long_transition

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    "Так, ура, ещё один учебный день позади."
    "Надо скорее двигать в клуб."
    "Как там обстоят дела с Котонохой?"
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om ce lup
    mi "Ох, Макс, после всего того, что с тобой случилось, теперь я могу быть за тебя спокойна окончательно~"
    show mrs_ida cm
    mc "Да, это уж точно..."
    show mrs_ida om oe ldown
    mi "Вижу, торопишься в клуб?"
    show mrs_ida cm
    mc "Да, у нас сегодня пополнение, надо всё проконтролировать."
    show mrs_ida omb ce
    mi "Ух ты!"
    show mrs_ida om oe
    mi "Неужели Литературный клуб вышел из тени и стал обрастать постоянными участниками?"
    show mrs_ida cm
    mc "Смею предположить, что да."
    mc "Пока всё идёт позитивно."
    show mrs_ida om
    mi "Очень хорошо."
    mi "Ну тогда иди, нельзя пропускать такое событие."
    show mrs_ida cm
    mc "Конечно."
    show mrs_ida ce
    mc "До свидания, Ида-сэнсэй."
    show mrs_ida om
    mi "Удачи, Макс!"
    show mrs_ida cm

    scene black with wipeleft_scene
    "Что-то я весь прямо на иголках в последнее время..."
    "Несусь быстрым шагом по коридору."
    "Да всё ж нормально, чего тут волноваться?"
    "Но нет, сердце не слушается и продолжает ускоренно стучать."
    "Котоноха не такая беспомощная, нас легко найдёт..."
    "А может, не из-за этого волнуюсь..."
    "Новый человек в привычном для тебя месте немного выбивает из волны, пока к нему не привыкнешь."
    "Но с другой стороны, надо клуб развивать, иначе он загнётся."
    "Сама Моника этого хочет."
    "Да и не только она..."
    "Ой, всё, хватит!"
    "Уже на душе мерзко от нервов становится."
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    y "{size=19}Вот здесь и находится наш Литературный клуб.{/size}"
    "Фух, полегче стало..."
    k "{size=19}Буду знать.{/size}"
    y "{size=19}Там практически все в сборе за исключением Макса...{/size}"

    scene bg corridor
    show yuri turned happ cm oe school_bag at t21
    show kotonoha happ cm oe school_bag at t22
    with wipeleft_scene
    show yuri om lup
    y "...но с ним ты и так уже познакомилась, да?"
    show yuri cm
    mc "Ага."
    show yuri shoc om oe rup at h21
    show kotonoha lsur cm oe
    y "Кья?!"
    show yuri mj
    show kotonoha happ om ce rhip
    k "Ха-ха, а вот и Макс!"
    show yuri laug cm oe ldown rdown
    show kotonoha cm oe
    mc "Ознакомление с клубом идёт полным ходом?"
    show yuri om
    y "Д-да, мы только что хотели войти..."
    show yuri cm
    mc "А, ну так давайте."
    show yuri happ cm oe
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    play music t3 fadein 3.0
    scene bg school literature_club board day
    show yuri turned neut cm e1d school_bag at t43
    show kotonoha neut cm oe school_bag at t44 zorder 2
    with wipeleft_scene
    m "{size=19}Нацуки, в следующий раз так не делай!{/size}"
    n "{size=19}Да что вы все прикопались?!{/size}"
    n "{size=19}Нормально всё прошло, н-о-р-м-а-ль-н-о!{/size}"
    m "{size=19}А если бы нет?{/size}"
    n "{size=19}Никто бы не умер.{/size}"
    m "{size=19}Понимаешь, у нас и так проблема с людьми, нам нужно подходить к их привлечению очень ответственно.{/size}"
    m "{size=19}А ты чуть Сайори не подставила, который пришлось судорожно импровизировать.{/size}"
    n "{size=19}Да какая ты зануда...{/size}"
    s "{size=19}Моника, всё хорошо, успокойся...{/size}"
    m "{size=19}Ух...{/size}"
    "Ха, не мне одному это не понравилось."
    "Но давайте сейчас без вот этого, а?"
    s "{size=19}А-А-А, ТОЧНО!{/size}"
    s "{size=19}Мы сервиз не помыли и не отнесли обратно!{/size}"
    n "{size=19}Блин...{/size}"
    "Они не заметили 3 фигуры в дверях, что ли?"
    mc "Кхм-кхм."
    m "{size=19}А?!{/size}"
    show kotonoha anno cm oe rdown
    n "{size=19}Коха?{/size}"
    show natsuki turned anno cm oe at t41
    show monika forward neut cm oe at t42 zorder 2
    show kotonoha om
    k "Ко-ТОНО-ха."
    show natsuki neut cm oe
    show yuri laug om oe
    show kotonoha neut cm oe
    y "Всем привет..."
    show monika happ cm oe
    show yuri cm
    "Поздно уже для такой фразы..."
    show monika om
    show yuri happ cm oe
    show kotonoha happ cm oe
    m "Довольно быстро, мы только недавно пришли."
    show monika cm
    show yuri ce
    show kotonoha om rhip
    k "Это всё Юри спасибо."
    show natsuki angr cm oe
    show monika neut cm oe
    show yuri neut cm e1d
    show kotonoha neut cm oe
    s "{size=19}Ай-ай-ай!{/size}"
    hide natsuki with easeoutleft
    n "{size=19}Сайори, что ты творишь?!{/size}"
    s "{size=19}Сервиз пытаюсь достать!{/size}"
    n "{size=19}Дай я помогу, пока ничего не полетело!{/size}"
    show kotonoha om
    k "Сервиз?"
    show monika happ om ce n2 at t21
    show yuri happ cm oe
    show kotonoha cm
    m "А-а-а, тут мы один чай от Юри пробовали, ничего особенного..."
    show monika cm
    show yuri om
    show kotonoha happ cm oe
    y "Могу как-нибудь позже угостить."
    show monika n1
    show yuri cm
    show kotonoha om ce rdown
    k "Хе-хе, не стоит."
    show monika curi om e1b
    show kotonoha cm
    m "Э-э-э, в общем..."
    show monika happ om oe lpoint rhip
    show kotonoha oe
    m "Добро пожаловать в Литературный клуб!"
    show monika ldown rdown
    m "Я Моника, занимаю должность президента."
    show monika cm
    show kotonoha om ce
    k "Приятно познакомиться!"
    show monika om lpoint
    show kotonoha cm oe
    m "Давай я всё покажу и расскажу в общих чертах."
    show monika cm ldown
    show kotonoha om
    k "Конечно."
    show monika om at thide
    hide monika
    show kotonoha cm at thide
    hide kotonoha
    m "{size=19}Посколько наша основная деятельность -- стихи, то...{/size}"
    show yuri neut cm e1d at t11
    mc "Правильно понимаю, что Котоноха тебе написала?"
    show yuri happ om oe
    y "Да, сначала она написала про своё вступление, а потом мы договорились о встрече, и я её сопроводила."
    show yuri cm
    mc "Вот как."
    show yuri e1b
    "Логичный ответ на мой тупой вопрос из воздуха."
    show yuri worr om ce
    y "Эх, Нацуки опять в своём репертуаре..."
    show yuri oe
    y "Могла бы и получше время найти."
    y "Или меня попросить поговорить сначала..."
    show yuri cm
    mc "Ой, проехали."
    show yuri neut cm e1d
    mc "Что сделано, то сделано, чего тут думать..."
    show yuri e1b
    y "..."
    show yuri angr om e2b
    y "Эй, стойте!"
    show yuri cm
    hide yuri with easeoutleft
    y "{size=19}Давайте я всё сама отмою и отнесу, иначе от сервиза ничего не останется.{/size}"
    s "{size=19}Хорошо-хорошо!{/size}"
    n "{size=19}Да без вопросов.{/size}"
    y "{size=19}Только сумку сниму...{/size}"
    n "{size=19}А теперь, Сайори, пошли исправлять бардак на полках.{/size}"
    s "{size=19}Нэ-э-э-э-э...{/size}"
    "Мда, а мне столбом стоять изволите?"
    "Кстати, подождите..."
    "У нас-то сегодня ничего нет: никто ничего не писал."
    "Это значит, что я смогу уйти пораньше?"
    m "{size=19}В принципе, на этом всё.{/size}"
    k "{size=19}Хм, я думала, у вас тут сложнее...{/size}"
    m "{size=19}Нет, мы никого ни к чему не принуждаем и сильных нагрузок не даём.{/size}"
    m "{size=19}Клуб, в первую очередь, должен быть местом, которое будет вызывать теплоту, а не отторжение.{/size}"
    "Да, Моника очень хороший президент."
    show monika forward happ cm oe at t21 zorder 3
    show kotonoha neut cm e1b at t22 zorder 2
    pause 0.2
    show kotonoha om
    k "Значит, мне придётся писать стихи..."
    show monika om
    show kotonoha happ cm oe
    m "По мере своих возможностей."
    show monika cm
    show kotonoha om ce
    k "Я просто немножко волнуюсь, ха-ха-ха!"
    show monika om ce
    show kotonoha cm
    m "Не переживай, всё будет просто."
    show monika cm
    "Ну-ка, меня осенило..."
    show monika oe
    show kotonoha oe
    mc "Моника, вопрос."
    show monika om
    m "Да, Макс?"
    stop music fadeout 3.0
    show monika neut cm oe
    show kotonoha neut cm oe rhip
    mc "Если мы будем разрастаться, то наша «система» обмена стихами будет крайне неудобной и сложной."
    show monika curi md oe
    mc "Не стоит ли нам попробовать что-то...{w}более «оптимизированное»?"
    mc "Да, я знаю, что наедине делиться проще, но это удобно лишь в маленьких группах."
    show monika e1b
    m "М-м-м..."
    show monika happ om oe lpoint
    m "У меня как раз недавно возникла одна интересная идея на эту тему..."
    show monika cm ldown
    mc "Ну?"
    show monika om ce
    m "Совместные стихотворения."
    show monika cm
    show kotonoha om rdown
    k "Ох..."
    show monika neut cm oe
    show kotonoha cm
    mc "И как ты планируешь это реализовать?"
    show monika happ cm oe
    mc "У нас не особо много времени из-за уроков, а тут надо ещё договариваться с кем-то и составлять общий стих..."
    "...да, я просто не хочу усложнять себе жизнь."
    show monika om
    m "Да ладно тебе, не думаю, что это такая проблема."
    show monika lpoint
    m "Просто теперь ты будешь составлять стих с кем-то в паре: либо вживую, либо дистанционно по мессенджеру."
    show monika cm ldown
    mc "И какова будет структура таких стихотворений?"
    show monika om
    m "Всё зависит от самих авторов."
    m "Четверостишия, строфы, один человек всё напишет или уже непосредственно перед обменом совместно -- ограничений нет."
    show monika ce
    m "Мы же экспериментируем, верно?"
    show monika cm
    mc "Хм..."
    show monika oe
    show kotonoha om e1c
    k "Тогда..."
    show monika neut cm oe
    show kotonoha oe
    k "Можно я на завтра пока ничего писать не буду?"
    k "Хочу посмотреть, как пройдёт весь процесс обмена."
    show monika happ om oe
    show kotonoha happ cm oe
    m "...хорошо, Котоноха, потому что такое будет у нас впервые."
    show monika cm
    "А меня в первый же день запрячь, значит, можно было?"
    show monika neut cm oe
    show kotonoha neut cm oe
    mc "В таком случае нас пятеро: по парам не разобьёмся."
    show monika e1b
    m "Хм..."
    show monika oe
    show kotonoha lsur om oe
    k "...но если надо, то могу попробовать!"
    show monika neut om oe
    show kotonoha cm
    m "Нет-нет, всё хорошо, не надо."
    show monika cm
    show kotonoha neut cm oe rhip
    mc "А, точно..."
    mc "Моника, я же ещё не писал в твоём стиле."
    mc "Можно было бы это сейчас закрыть."
    mc "И тогда бы ты спокойно распределилась с остальными."
    show monika om e1b
    m "Хах..."
    show monika happ om oe
    m "Почему бы и нет?"
    show monika neut mh oe lpoint
    show kotonoha happ cm oe
    m "Идея хорошая, только надо остальным всё рассказать."
    show monika cm ldown
    s "{size=19}Фу!{/size}"
    n "{size=19}Не \"фу\", а ура!{/size}"
    y "{size=19}Ребят, я помыла сервиз.{/size}"
    y "{size=19}Отнесу его сейчас в Клуб выпечки, хорошо?{/size}"
    show monika om
    show kotonoha neut cm oe
    m "Подожди, Юри, положи его здесь."
    show sayori turned neut cm oe at l51 zorder 2
    show natsuki turned neut cm oe at l52
    show monika mh lpoint at t53
    show kotonoha rdown at t54
    m "Друзья, есть одна важная информация."
    show monika ldown
    show kotonoha happ cm oe
    m "Макс и Котоноха уже в курсе, если что."
    show sayori curi om e1a
    show monika cm
    show yuri turned neut cm e1d at r55
    s "Что такое?"
    show sayori neut cm oe
    show natsuki curi cm oe lhip rhip
    show monika happ om oe
    m "Это касательно стихотворений."
    show monika cm
    show yuri curi om oe
    y "Что-то новое?"
    show natsuki om
    show yuri cm
    n "Новое?"
    show sayori curi cm oe
    show natsuki cm
    show monika om
    show yuri neut cm e1d
    m "Да."
    show sayori neut cm oe
    show monika neut mh ce
    m "Так вот..."
    show monika cm
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg school literature_club board day
    show sayori turned happ cm oe at i51 zorder 2
    show natsuki turned neut cm oe lhip rhip at i52
    show monika forward happ cm oe at i53 zorder 3
    show kotonoha happ cm oe at i54 zorder 2
    show yuri turned neut cm e1d at i55
    with wiperight
    show monika om lpoint
    m "Поэтому всем, кроме Макса и Котонохи, нужно распределиться по парам и попробовать составить совместный стих на завтра."
    show sayori om ce lup rup at h51
    show natsuki curi cm oe
    show monika cm ldown
    show yuri anno cm oe
    s "Я выбираю Монику!"
    show sayori cm ldown rdown
    mc "Прям сразу?"
    show sayori om
    show natsuki anno cm oe ldown rdown
    show monika ce
    s "Угусь!"
    show sayori neut cm oe
    show natsuki om ce
    show monika neut cm oe
    show kotonoha neut cm oe
    n "Распределились..."
    show natsuki cm
    show yuri shy neut m2 oe at s55
    y "Умф..."
    show monika mg b1b
    m "Ой, слушайте, я знаю, что вы не очень любите стили друг друга, но попробуйте составить что-то вместе."
    m "Может, таким образом у вас получится проработать проблемы и прийти к взаимопониманию?"
    show monika cm
    ny "..."
    mc "Блин, серьёзно, хватит уже."
    show natsuki e1b b1d
    mc "Вы ж вроде как помирились, не?"
    show monika e1c -b1b
    show kotonoha om e1b
    k "{size=15}Разве они так сильно конфликтуют из-за этого?{/size}"
    show monika om
    show kotonoha cm
    m "{size=15}К сожалению.{/size}"
    show monika cm oe
    show kotonoha oe
    mc "Если так, то без проблем напишите стих."
    show monika om e1c
    show kotonoha lsur cm oe
    m "{size=15}Один раз дошло до опасного конфликта.{/size}"
    show monika cm oe
    mc "Нечего тут дуться."
    show kotonoha om
    k "{size=15}О-о-о...{/size}"
    show kotonoha e1b
    k "{size=15}Не думала, что всё так серьёзно.{/size}"
    show sayori sad cm oe
    show kotonoha cm oe
    show sayori om
    s "Ради нас..."
    show natsuki angr cm ce -b1d
    s "Пожалуйста..."
    show sayori neut cm oe
    show natsuki om lhip rhip
    show monika happ cm oe
    show kotonoha happ cm oe
    n "Бе-е-е, да-да-да, хватит!"
    show natsuki anno om e1b b1d ldown rdown
    n "Если Юри не будет против, то я соглашусь."
    show sayori happ cm oe
    show natsuki cm
    show yuri om
    y "...хорошо..."
    show natsuki neut cm e1b -b1d
    show yuri turned neut om oe b1d lup rup at t55
    y "Я постараюсь."
    show sayori ce
    show monika om ce
    show kotonoha ce
    show yuri cm
    m "Вот и отлично!"
    show sayori oe
    show natsuki oe
    show monika oe lpoint rhip
    show kotonoha oe
    show yuri e1d -b1d ldown rdown
    m "Итак, друзья!"
    show monika ldown rdown
    m "Раз мы с этим разобрались--{nw}"
    play sound door_knock
    show sayori curi cm oe
    show natsuki curi cm oe
    show monika neut cm oe
    show kotonoha neut cm oe
    pause 1.26
    show monika curi om oe
    m "А?"
    show monika mj
    mc "Там кто-то пришёл?"
    show sayori neut cm oe
    show monika neut cm oe
    show kotonoha om
    k "Да, силуэт..."
    show sayori om
    show kotonoha cm
    s "Я проверю!"
    show sayori cm zorder 3
    call window_close
    hide sayori with easeoutright

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    s "{size=19}Привет?{/size}"
    e "{size=19}Хай-хай!{/size}"
    m "Привет!"
    "...Эми?"

    scene bg club_day
    show emi turned uniform_waist_jacket happ cm oe lhip rhip at t21
    show sayori turned neut cm oe at t22
    with wipeleft_scene
    n "Эми?"
    n "Ты что тут делаешь?"
    show emi om ce
    e "И я тебя рада видеть, На-цу-ки."
    show emi cm
    n "Аргх, ну привет-привет!"
    show emi om oe
    e "Вот, другой разговор!"
    show emi angr om ec
    show sayori curi cm oe
    e "Ребят, верните должок, пока нас Кохаку не сожрала заживо."
    show emi happ cm oe
    y "Cервиз?"
    show emi om
    show sayori neut cm oe
    e "В точку!"
    show emi cm
    y "Сейчас, мы его уже подготовили, сегодня хотели обратно передать..."
    show emi sedu cm oe
    mc "Кохаку на взводе после вчерашнего?"
    show emi cross uniform_waist_jacket sedu om oe
    show sayori curi cm oe
    e "Ха-ха, ты даже не представляешь, как у неё подгорело."
    show emi laug om ce
    e "Моника знатно зажгла ей зад своей обалденной фразочкой."
    show emi cm
    m "Э-э-э..."
    show sayori om
    s "Это что она такое сказала?!"
    show emi happ cm oe
    show sayori cm
    m "Н-ничего особенного!"
    show emi om ce
    show sayori pout cm e1a
    e "А вот секрет!"
    show emi cm
    show sayori om oe
    s "Ну не хотите говорить, как хотите..."
    show emi oe
    show sayori cm
    y "Эми, вот."
    show emi turned uniform_waist_jacket happ om oe
    e "Вижу, секунду..."
    show emi cm at thide
    hide emi
    pause 2.0
    show sayori neut cm oe
    e "О-о-окей."
    e "Извиняюсь, что помешала!"
    show sayori b1b
    e "Мне пора!"
    show sayori om
    s "Да ну!"
    show sayori happ om ce -b1b lup rup at h22
    s "У нас весело, побудь с нами!"
    show sayori cm
    e "Не-не, меня в клубе ждут."
    show sayori oe ldown rdown
    e "Спасибо, что приготовили сервиз."
    show sayori om
    s "А может, к нам вступишь?"
    show sayori cm
    e "К вам-то, ха?"
    show sayori curi cm oe
    e "А у вас кухни нет!"
    e "Лучше б вы Фукку об этом спросили..."
    pause 0.5
    play sound closet_open
    pause 0.75
    show sayori om
    s "Фукка?..."
    show sayori cm

    scene bg school literature_club board day
    show natsuki turned neut cm oe lhip rhip at t52
    show monika forward neut cm oe at t53 zorder 3
    show kotonoha neut cm oe at t54 zorder 2
    show yuri turned neut cm e1d at t55
    with wipeleft_scene
    show natsuki om e1b
    n "Время идёт, а она всё та же..."
    show natsuki cm
    show sayori turned neut cm oe at l51 zorder 2
    pause 0.5
    show sayori om b1f
    show natsuki oe
    show kotonoha rhip
    s "Фукка -- это та, которая ходила в музыкальную комнату вместе с тобой, Моника?"
    show natsuki ldown rdown
    show sayori cm
    show monika om
    m "Да."
    show sayori -b1f
    show monika dist om oe
    m "Замкнутая девушка, которая теперь в Клубе выпечки..."
    show sayori om
    show monika neut cm oe
    s "Она может перейти к нам?"
    show sayori cm
    show monika om e1b
    m "Не знаю."
    show monika oe
    m "Нацуки, ты говорила, Кохаку к ней лояльна?"
    show natsuki om lhip rhip
    show monika cm
    n "Ага, не думаю, что Фукка захочет к нам перескочить."
    show natsuki cm
    show monika dist om oe
    m "Однако из-за этого клуба она не практикуется в музыкальном классе..."
    show kotonoha rdown
    m "Не успела я взять её к себе."
    show sayori om b1f
    show monika cm
    s "А как ты \"не успела\"?"
    show sayori cm -b1f
    show monika neut om oe lpoint
    m "Если бы я принимала решение сейчас, то пригласила бы её без всяких задних мыслей и размышлений."
    show natsuki neut cm oe
    show monika ldown
    m "Но в самом начале становления Литературного клуба я старалась находить именно тех людей, которые могли быть связаны с выбранной тематикой..."
    show natsuki dist om ce lhip rhip
    show monika dist cm oe
    n "Короче говоря, мы ничего не можем с этим сделать."
    show sayori worr cm oe
    show natsuki neut cm oe
    show kotonoha om e1b
    show yuri dist cm oe
    k "Как-то у вас здесь всё сложно..."
    show natsuki happ om oe
    show kotonoha cm
    n "Ха, а ты думала!"
    show monika oe
    show kotonoha neut cm oe
    n "Добро пожаловать в клубную деятельность."
    show sayori om
    show natsuki cm
    s "Печалька..."
    show sayori neut cm oe
    show natsuki neut cm oe ldown rdown
    show monika neut cm oe
    show yuri neut cm e1d
    mc "Кстати, какие тут примерные наказания за нарушения школьных правил?"
    show monika om
    m "Ты ещё не знаешь?"
    show monika cm
    mc "Я обычно всё соблюдаю, поэтому бегло просмотрел на сайте, успокоился и забыл."
    show monika om e1b
    show kotonoha rhip
    m "Ну, если кратко..."
    show monika oe lpoint
    m "При лёгком нарушении (нецензурная брань, мелкое хулиганство и тому подобное) будет сделано замечание -- первая ступень нарушения."
    show monika ldown
    m "При среднем нарушении (драка, порча имущества, травля и так далее) или при несколько лёгких будет сделан выговор с извещением родителей -- вторая ступень нарушения."
    m "Также к выговору могут дать «исправительную» работу вне очереди или дополнительную: уборка в школе, всякая нудность с бумагами под присмотром учителей и так далее..."
    show natsuki e2a
    m "А если же будет тяжкое нарушение (даже перечислять не буду) или несколько средних, то будет осуществлён перевод в другую школу."
    show sayori e1b
    show monika cm
    show kotonoha e1b
    mc "Мдэ-э-э..."
    show natsuki e2b rhip
    show monika e1b
    "Весело у вас, однако..."
    "Зато эффективно, наверное."
    show sayori oe
    show natsuki happ om oe
    show monika oe
    show kotonoha oe
    show yuri curi cm oe lup
    n "А, так вот!"
    show natsuki ce
    show yuri ldown
    n "У нас ещё не всё потеряно!"
    show natsuki oe lhip
    show yuri neut cm e1d
    n "Бьюсь об заклад, у Кохаку будет выговор."
    show natsuki neut cm oe
    mc "Откуда такая уверенность?"
    mc "Мелкое нарушение -- да, но среднее..."
    show sayori e2a
    show natsuki ldown rdown
    mc "А провоцировать и подставлять её до тяжкого мы точно не будем."
    mc "Как и до любого другого."
    show monika dist om oe
    show yuri anno cm oe
    m "Макс прав, это будет очень низко с нашей стороны..."
    show natsuki me e1b
    show monika cm
    n "Хм..."
    show sayori oe
    show natsuki cm
    show monika neut cm oe
    show yuri neut cm e1d
    mc "Да и вообще, что станет с Клубом выпечки, когда Кохаку, условно, выгонят из него?"
    show natsuki curi cm oe
    mc "Останется 4 человека максимум."
    mc "Один может отвалиться, другую заберём -- итого 2."
    mc "Клуб выпечки благополучно сдохнет, не говоря уже о поддержке всякого кухонного оборудования с продуктами."
    show natsuki om lhip rhip
    n "Не верю, что после смены президента никто туда не потянется."
    show natsuki doub cm oe
    mc "Смены?"
    show natsuki om
    n "Эми, алло."
    n "Она завзятый повар."
    show natsuki curi cm oe
    mc "А Фукка любила гитары, и где она теперь?"
    show natsuki e1b
    n "..."
    mc "История повторяется, только причина развала другая."
    show monika e1c
    show kotonoha om e1b
    k "{size=15}Ой, а можно я пока номерами обменяюсь с Сайори?{/size}"
    show monika om
    show kotonoha happ cm e1b
    m "{size=15}Да, конечно.{/size}"
    show natsuki neut cm oe
    show monika cm oe
    show kotonoha oe rdown at thide
    hide kotonoha
    show yuri at t33
    mc "Поэтому надо учитывать и такой вариант развития событий."
    show sayori e1c
    show natsuki ldown rdown
    show monika om e1b
    m "{size=17}Сайори, подойди к Котонохе.{/size}"
    show sayori happ om e1c
    show monika cm
    s "{size=17}А, минутку!{/size}"
    show sayori cm ce at thide
    hide sayori
    show natsuki at t31
    show monika oe at t32
    show yuri om
    y "Мы могли бы объединиться с Клубом выпечки."
    y "Это улучшило бы наши взаимоотношения с его составом, а также сохранило бы сам клуб."
    show yuri cm
    mc "...честно, звучит сумбурно."
    mc "Как это будет реализовываться?"
    mc "И как мы будем помогать клубу, особенно когда нам самим как бы нужно развиваться?"
    show yuri anno cm oe
    show natsuki e4a
    show monika dist cm oe
    "..."
    mc "Вот!"
    mc "Лучше мы потратим силы на себя, чем будем отдавать их непонятно кому с вероятностью, что в нас благополучно плюнут."
    show sayori turned happ cm oe at t51 zorder 2
    pause 0.2
    show sayori om
    show natsuki neut cm e1b ldown rdown at t52
    show monika happ cm oe at t53
    show yuri neut cm e1d
    s "Моника, я переслала тебе и Максу номер Котонохи."
    s "Ваши она уже записала."
    show sayori cm
    show monika om
    m "О, хорошо, спасибо."
    show natsuki oe
    show monika cm
    show kotonoha happ cm oe at t54 zorder 2
    show yuri at t55
    mc "Значит, на сегодня всё?"
    show monika om
    m "Выходит, что да."
    show yuri e1c
    m "Пары по стихам на завтра распределены."
    show monika ce lpoint rhip
    show yuri e1d
    m "Итак, друзья!"
    show monika oe ldown rdown
    m "Наше собрание окончено."
    show natsuki e1d
    show monika lean happ om oe at h53
    show yuri dist cm oe
    m "Не забудьте, что стихотворения на завтра вы пишете вместе с теми, кто вам достался в паре."
    show natsuki e1c
    show monika forward happ om oe lpoint
    m "Макс пока пишет один, Котоноха освобождена."
    show monika neut om oe ldown
    show kotonoha neut cm oe
    show yuri neut cm e1d
    m "Больше никаких вопросов, пока мы тут все месте?"
    show monika cm
    mc "Нет, в принципе..."
    show sayori om
    show natsuki om
    show monika happ cm oe
    show yuri om
    nsy "Нет."
    show sayori cm
    show natsuki cm
    show monika om ce
    show kotonoha happ cm oe
    show yuri cm
    m "Вот и отлично!"
    show natsuki oe
    show monika oe
    m "Всё, всем до завтра!"
    show sayori om ce lup rup at h51
    show kotonoha ce lup rhid
    show monika cm
    s "Пока-пока!"
    show sayori cm ldown rdown
    show kotonoha ldown rdown
    mc "До встречи."
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    show kotonoha at thide
    hide kotonoha
    show yuri e1b at thide
    hide yuri
    pause 0.5
    k "{size=19}Я уверена, что у вас хорошо получится!{/size}"
    "Проведём Монику до дома, раз уж тут остались..."
    show sayori oe at t21
    "Тем более парень я её или кто?"
    show monika forward neut om oe school_bag at t22
    m "У?"
    show monika curi om oe
    m "Почему вы всё ещё здесь?"
    show sayori om ce
    show monika neut cm oe
    s "Я тут, потому что Макс!"
    show sayori cm
    mc "А я..."
    show sayori oe
    show monika dist cm oe
    mc "Может, составить тебе компанию до дома?"
    show monika om
    m "Но вам совершенно не по пути..."
    show monika neut cm oe
    mc "Какая разница?"
    show sayori ce
    mc "Заодно и Сайори с нами прогуляется."
    show monika om e1b
    m "Ну..."
    show sayori oe
    show monika happ om oe lpoint
    m "Хорошо, я не против."
    show sayori om
    show monika cm ldown
    s "Тогда идём!"
    show sayori cm
    show monika ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show monika forward happ cm e1b school_bag at t21
    show sayori turned happ cm e1c school_bag at t22
    with wipeleft_scene
    "Что-то очень много всего в голове: Клуб выпечки, вино, психолог, руки..."
    show monika oe
    show sayori neut cm oe
    "И мысли постоянно ускользают, как желе: не за что зацепиться."
    show monika neut cm oe
    "Мозг утомился..."
    show monika om
    show sayori curi cm oe
    m "Какой-то взгляд у тебя мутный, Макс."
    show monika cm
    show sayori om
    s "Заболел?"
    show sayori neut cm oe
    mc "Нет, устал."
    show monika e1b
    m "Хм..."
    show monika oe
    mc "Кстати, Моника, тебе плохо не было после вчерашнего?"
    show monika happ cm oe
    mc "А то мало ли..."
    show monika om ce
    m "Я в порядке, будто ничего не было, ха-ха!"
    show monika cm
    show sayori dist om ce
    s "Фух, метод Юри эффективно подействовал..."
    show monika om oe lpoint
    show sayori happ cm oe
    m "Да, я её уже поблагодарила."
    show monika cm ldown
    mc "Это классно, но, пожалуйста, повторю ещё раз: больше не надо таких выкрутасов."
    show monika e1d b1f n3
    show sayori neut cm oe
    mc "Это нам всем вчера очень повезло, что практически ни на кого не наткнулись и что всё более-менее обошлось..."
    show monika om
    show sayori anno cm oe
    m "Да ладно, Макс, тебе не понравилось?"
    show monika cm
    mc "Неа!"
    show monika ce -b1f
    "Даже ощущение вплотную полуголого женского тела не изменит мой ответ."
    show monika om n1
    show sayori neut cm oe
    m "Ха-ха-ха, ладно, я уже соглашалась на твои слова."
    show monika lean happ om ce n3 school_bag at h21
    show sayori curi cm oe
    m "Но ничего не обещаю~"
    show monika cm
    show sayori mh
    s "Но ведь ты только что пообещала..."
    show monika forward happ om oe n1 school_bag lpoint
    show sayori cm e1a
    m "Это не совсем обещание."
    show monika cm ldown
    show sayori mh
    s "Обещание-необещание?"
    show monika om
    show sayori cm
    m "Нестабильное обещание."
    show monika cm
    show sayori mh
    s "Но нестабильное обещание уже не будет обещанием или будет недообещанием?"
    show monika om e1b
    show sayori cm
    m "Я думаю--{nw}"
    show monika laug cm ce
    show sayori laug cm oe
    mc "У меня сейчас голова взорвётся, люди!"
    show sayori ce
    mc "Хватит."
    show monika om
    show sayori om
    ms "Ха-ха-ха!"
    show monika cm
    show sayori cm
    mc "Всё."
    show monika happ cm ce
    show sayori happ cm oe
    mc "Тихо..."
    show monika oe
    mc "Мне чуть реально не поплохело."
    show monika om ce
    show sayori e1b
    m "Всё, молчим."
    show monika cm

    scene bg monika house outside day
    show monika forward happ cm oe school_bag at t21
    show sayori turned happ cm oe school_bag at t22
    with wipeleft_scene
    show monika om
    show sayori neut cm oe
    m "Пришли."
    show monika cm
    show sayori worr om oe
    s "Эх..."
    show monika om lpoint
    show sayori neut cm oe
    m "Сайори, я с тобой свяжусь ближе к вечеру, а там и стих составим, хорошо?"
    show monika cm ldown
    show sayori happ om ce lup rup at h22
    s "Конечно!"
    show sayori ldown rdown
    s "Буду ждать!"
    show monika om ce
    show sayori cm oe
    m "Всё, до завтра!"
    show monika cm
    mc "До завтра."
    show sayori om
    s "Пока!"
    show monika oe at thide
    hide monika
    show sayori cm
    pause 0.2

    scene black with wipeleft_scene
    mc "Пф-ф-ф..."
    s "Что такое?"
    mc "Устал, уже говорил."
    mc "А ещё домашнее задание ковырять, плюс стих писать..."
    s "Да, дел невпроворот."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 24,
            description = "Внезапно! Литературный клуб пополнился ещё одним участником -- Котонохой, подругой Юри и Нацуки. Возможно, это был просто вопрос времени..."
        )

        current_day = (24, _("ВТ"))

    python in phone.system:
        battery_level = 73
        clock = (18, 47)

    show screen phone_calendars() with Dissolve(0.5)
    $ plot_pause()
    hide screen phone_calendars with Dissolve(0.5)

    window auto
    mc "Ух, блин..."
    "Ощущаю себя как-то вяло."
    "Отголоски вчерашнего дня с плохим сном?"
    "Пораньше лечь сегодня, что ли..."
    "..."
    "Хм, а если я чувствую сейчас себя немного опустошённым и разбитым из-за того, что я...{w}да как это сформулировать...{w}ощутил, какого быть вместе с девушкой?"
    "Как будто не хватает какого-то тепла с нежностью или что-то в этом духе..."
    "..."
    mc "Что я несу в своих мыслях?"
    "Как я умудрился за неделю ТАК кардинально поменяться?"
    "..."
    "Ладно, рано расслабляться."
    "Надо составить стихотворение и искать аккаунт психолога."
    "Эх, такое чувство, будто я никогда не смогу расслабиться в этой жизни."
    "То это, то то, то пятое, то десятое..."
    "А если ничего из дел нет, то никак не можешь получить удовольствие от отдыха."
    mc "Чёртова жизнь..."
    "Нафиг ты мне такая нужна?"
    "Самая важная ценность человека, блин..."
    mc "Так, листок и ручка..."

    call poem_act_1_day_9

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc6, music=False)
    "Хм-м-м..."
    "Уже намного лучше, чем всё прошлое вместе взятое."
    "Странное ощущение удовлетворённости..."
    "Но ведь это хорошо."
    "Стих готов."
    "Поэтому пора заниматься другой задачей..."
    "Третий заход поисков."
    "Интересно, я вообще смогу его найти?"
    "А то выясниться, что банально дурью маюсь."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg bedroom with wiperight
    "..."
    "Ожидаемо."
    "Я реально помаялся дурью."
    mc "Ах-х-х..."
    "Главное, что мне не нравится во всём этом поиске, -- это куча потраченных сил."
    "Ради какого-то плёвого разговора из разряда: \"У моей подруги жопа, поможете?\" -- \"Да без проблем!\""
    "И всё."
    "И никого не волнует, сколько ты до этого корячился."
    "Всем плевать."
    "Откровенно."
    "..."
    "Уже нет сил ни на возмущение, ни на что-либо ещё."
    "Да, усну сегодня пораньше, хоть высплюсь."
    "Всё равно вялость никуда не денется -- передохнуть особо не выйдет..."
    call window_close

    call nightmare_act_1_day_9
    $ _history_list.clear()

    $ nightmare_active = False

    return
