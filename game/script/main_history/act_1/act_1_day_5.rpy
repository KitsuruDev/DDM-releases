
label act_1_day_5:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d4.unlocked == False:
        $ ach_a1_d4.unlock()

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
    mc "{cps=20}Пф-ф-ф-ф...{/cps}"
    "Потянулся, и в глазах поплыло..."
    "Так, приди в себя."
    "Не хватало тут ещё головокружения и тошноты."

    phone register "mc_s_chat":
        time year 2018 day 20 month 4 hour 6 minute 8
        "s" "Ты же помнишь что сегодня будет? Поиск печенья! Я уже у твоей двери! Просыпайся! Открывааай! (> ω <)"

    play phone_sound new_message_mc
    pause 0.5
    mc "А?..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 74
        clock = (6, 9)

    phone discussion "mc_s_chat"
    $ plot_pause()
    phone end discussion transition

    call skip_block_off
    scene black with dissolve
    pause 0.25
    mc "Ох-х-х..."
    "Кто ходит в гости по утрам, так это только, блин, Сайори..."
    "...и вообще..."
    "...я опять вай-фай забыл вырубить?"
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    play music suspicion fadein 2.5
    s "{size=19}П-е-{w=0.5}ч-е-н-ь-{w=0.5}е!!!{/size}"
    "Как бы мне ни хотелось спокойствия и тишины..."
    s "{size=19}Я видела твою макушку в спальне через окно!{/size}"
    "...я должен открыть эту дверь."
    s "{size=19}Ты там на полпути уснул, что ли?!{/size}"
    "Кто ж вчера ей разрешил устроить рейд?"

    scene bg mc house peephole sayori with dissolve
    s "{size=19}Макс!{/size}"
    s "{size=19}Я слышала, что ты отодвинул глазок!{/size}"
    s "{size=19}Открывай!{/size}"
    call window_close

    scene black with dissolve
    pause 2.0
    play sound house_door_open
    play noise_3 street_suburban_noise fadein 1.0
    pause 4.0
    stop noise_3 fadeout 1.0
    play sound house_door_close

    call window_open
    scene bg mc house hallway day
    show sayori turned nerv cm ce school_bag at t11
    with dissolve_scene_full
    show sayori om ce
    s "Наконец-то!"
    show sayori cm ce
    mc "Я не виноват, что ты так рано пришла-а-а..."
    show sayori anno om oe
    s "Мог бы и догадаться, ведь я тебе говорила, что приду."
    show sayori pout cm oe
    mc "Умф-ф..."
    "Ну зашибись..."
    "Что за утро..."
    show sayori neut om oe
    s "Ладно."
    show sayori happ om oe
    s "Где печенье?"
    show sayori cm oe
    mc "На кухне в шкафах где-то завалялось, поищи там."
    mc "Только обувь и сумку сними."
    show sayori cm ce
    call window_close

    call plot_transition

    call window_open
    scene bg kitchen
    show sayori turned happ cm ce cookie_crumbs at t11
    with wipeleft_scene
    show sayori om ce
    s "Вкусно!"
    show sayori cm ce
    "Прощай, единственная пачка печенья..."
    "Мне она всё равно ни к чему."
    show sayori mp ce
    show sayori lup cookie with dissolve
    pause 0.5
    show sayori cm ce
    show sayori ldown -cookie with dissolve
    pause 0.5
    show sayori neut mouth_eating oe
    mc "Как, кстати, вчера всё прошло?"
    show sayori om oe
    s "Ты о чём?"
    show sayori mouth_eating oe
    mc "О сопровождении Юри."
    show sayori om e1b
    s "А, это..."
    show sayori happ om oe
    s "Она стала в разы веселее."
    s "Ты её раскрепостил."
    show sayori cm oe
    mc "Понятненько."
    show sayori neut om oe
    s "А из-за чего она была такой грустной?"
    show sayori cm oe
    mc "Пустяк полнейший, Нацуки подтвердит."
    show sayori e1b
    s "Хм..."
    show sayori happ om oe
    s "Главное, что всё прошло, не так ли?"
    show sayori cm oe
    mc "Ага."
    show sayori curi om oe
    s "Эй!"
    s "Это всё?"
    show sayori cm oe
    mc "Да, больше нет."
    show sayori om oe at thide
    hide sayori
    s "Да ну!"
    s "Больше нет моего счастья?"
    mc "Эх, Сайори, поверь мне, не в печенье счастье..."
    s "Ты что, с ума сошёл?"
    show sayori turned curi cm oe cookie_crumbs at t11
    pause 0.2
    show sayori om
    s "А в чём же ещё?"
    show sayori neut cm oe
    mc "Чёрт, пора мне одеваться, время поджимает."
    mc "Подождешь меня снаружи или у выхода?"
    show sayori om
    s "Здесь посижу."
    show sayori cm
    mc "Как хочешь, только ничего не трогай."
    stop music fadeout 2.5
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg residential_day
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om oe
    s "Сегодня твой последний иксе...{w}ексепе...{w}э-к-с-п-е-риментальный стих, да?"
    show sayori cm oe
    mc "Да."
    show sayori neut cm oe
    mc "Моника вчера мне сказала, чтобы сегодня я принёс их все для анализа."
    show sayori curi om oe
    s "Анализа?"
    show sayori cm oe
    mc "Она хочет изучить мои наклонности в стилях и понять, куда мне стремиться."
    show sayori nerv om oe at s11
    s "А-а-а..."
    show sayori neut cm oe
    mc "На выходных придётся с ней встретиться для обсуждения этого вопроса."
    show sayori curi cm ce
    s "Хм..."
    mc "Как-то это всё слишком серьёзно, не находишь?"
    show sayori om e1a at t11
    s "Так ведь на кону твой стиль, Макс, естественно!"
    show sayori cm
    mc "Сайори, для меня стихи -- просто стихи: что в голову пришло, так и легло."
    mc "Только в скомпанованном виде."
    show sayori neut om oe
    s "Это ты так думаешь."
    show sayori cm oe
    mc "С чего это?"
    show sayori happ om oe
    s "А ты сам вспомни свои стихотворения."
    show sayori lup
    s "Ты стараешься соблюдать некоторые рамки, при этом учитывая различные особенности стилей, сами стихи выходят непростыми по смыслу..."
    show sayori neut cm oe ldown
    mc "Просто вдохновение."
    show sayori lsur om oe lup rup at h11
    s "Вот!"
    show sayori happ om oe ldown rdown
    s "А это уже о чём-то, да говорит!"
    show sayori cm oe

    scene bg niigata street suburban 10 day
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    mc "Ну не знаю..."
    show sayori om ce lup rup at h11
    s "Так что Литературный клуб на тебя влияет позитивно!"
    show sayori neut cm oe ldown rdown
    mc "Пока не вижу особых изменений внутри себя, да и в перспективе..."
    show sayori sad om oe at s11
    s "Ну-у-у!"
    show sayori happ om oe lup at t11
    s "У тебя же появились новые друзья, не так ли?"
    show sayori cm oe ldown
    mc "Друзья..."
    show sayori om oe
    s "Это уже хорошо!"
    s "Всяко лучше, чем быть в одиночестве, когда все проводят время либо с друзьями, либо со своими половинками."
    show sayori neut cm oe
    mc "Зная, какие у них интересы и увлечения, я лучше один побуду и получу от этого больше удовольствия."
    s "Ум-м..."
    show sayori worr cm oe
    s "..."
    "Я подметил, что мне совсем не везёт на людей."
    "Точнее, редко везёт, но лучше от этого не становится..."
    "Ладно, сменим тему разговора."
    show sayori neut cm oe
    mc "Мне тут интересно стало..."
    show sayori om
    s "Что?"
    show sayori happ cm oe
    mc "Почему ты решила носить бантик на голове?"
    show sayori om
    s "Вообще-то это ободок с бантиком."
    show sayori cm
    mc "А, ну да..."
    show sayori om e1c
    s "Мне он просто понравился."
    show sayori oe
    s "Родители купили мне его, когда мне было 14."
    show sayori cm
    mc "Ясненько."
    show sayori curi om e2b
    s "Правда, когда я подросла, то он стал иногда слетать с волос..."
    show sayori neut cm oe
    mc "Купи себе новый."
    show sayori om
    s "Не..."
    show sayori cm
    mc "Почему?"
    show sayori dist om oe
    s "Бантик слишком детский..."
    show sayori anno om oe
    s "А летом мне будет 18!"
    show sayori neut cm oe
    mc "Тогда что-нибудь другое."
    mc "Или ты вообще откажешься от своей фишки-аксессуара?"
    show sayori lsur om oe
    s "Нет-нет, так неинтересно!"
    show sayori happ om oe
    s "На день рождения я хочу себе шёлковую ленту."
    show sayori cm
    mc "Лента?"
    show sayori om
    s "Я видела один прикольный узел, который напоминает кроличьи ушки."
    show sayori e2b
    s "Если надеть эту ленту так, что будут видны только эти ушки, то..."
    show sayori om ce lup rup at h11
    s "Это будет в разы лучше бантика!"
    show sayori cm
    mc "Хм..."
    show sayori ldown rdown
    "Как-то я представил себе эту картину...{w}и не понял, как выглядит узел."
    show sayori neut cm oe
    mc "Но с лентой возиться придётся: завязывать, поправлять..."
    show sayori om
    s "Я знаю."
    show sayori happ om oe rup
    s "Но зато можно регулировать её размер."
    show sayori cm rdown
    mc "Это да..."
    show sayori neut cm oe
    mc "А цвет у ленты какой будет?"
    show sayori curi om e2b
    s "Э-э-э..."
    s "Мне кажется..."
    show sayori flus om oe
    s "...ой, не знаю..."
    show sayori cm
    mc "Синий?"
    show sayori worr om oe
    s "Нет, синий плохо сочетается, хоть мне он нравится..."
    show sayori neut cm oe
    mc "Окей, красный."
    show sayori om
    s "Ярко."
    show sayori laug cm oe
    mc "...даже не думай, что я буду скакать по всей палитре цветов."
    show sayori ce
    s "Хах..."
    show sayori lsur om oe lup rup at h11
    s "О!"
    show sayori happ om oe ldown rdown
    s "Я думаю, темновато-зелёный был бы оптимальным цветом."
    show sayori cm
    mc "Зелёный?"
    mc "Неожиданный выбор."
    show sayori ce
    mc "Мой любимый цвет."
    show sayori om
    s "Хе-хе!"
    show sayori oe
    s "Просто он лучше всего сочетается с цветом моих волос."
    show sayori cm

    scene bg school gate 1
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori oe
    mc "Что-то я забыл, какого числа у тебя день рождения..."
    show sayori nerv mb oe
    s "Я тоже не помню."
    show sayori happ om ce
    s "Но ближе к нему вспомним."
    show sayori cm
    mc "Надеюсь..."
    show sayori om oe
    s "Увидимся в клубе."
    show sayori cm
    mc "Увидимся."
    show sayori ce at thide
    hide sayori
    pause 1.0
    "Тогда можно с подарком не мучиться."
    "Кстати, а что насчёт дней рождения участниц Литературного клуба?"
    "У Нацуки, судя по рассказам, уже прошло."
    "А у Моники и Юри?"
    "Их же тоже надо будет поздравлять, дарить что-то, праздник организовывать всем клубом..."
    mc "Сколько ж хлопот..."
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("y")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school f1 old_stairwell right with dissolve_scene_full
    "Тишина...{w}любимая книга в руках...{w}и свободное время..."
    "Что ещё нужно для морального и физического отдыха?"
    "Приятное спокойствие...{w}но я всё ещё в возбуждённом состоянии, ух..."
    "Я просто не могу взять и выдохнуть."
    y "{size=19}...Макс...{/size}"
    "Он всё больше и больше захватывает моё воображение."
    "Я не могу это контролировать..."
    "Я чувствую...{w}как заливаюсь румянцем...{w}как начинает сильнее биться сердце..."
    "Надо успокоиться и прийти в норму!"
    y "Вдох-х-х..."
    y "...вы-ы-ыдох..."
    show kotonoha happ cm oe at l11
    pause 0.7
    show kotonoha om ce lup rhid
    play music yuri_romanticism fadein 3.0
    k "Знала, что ты здесь будешь."
    show kotonoha oe ldown rdown
    k "Решила пока закинуть вещи в класс и с тобой побыть."
    show kotonoha cm
    y "П-привет!..."
    show kotonoha neut cm oe
    k "Хм?"
    show kotonoha happ om ce
    k "Выглядишь немного нервной, прямо как вчера, ха-ха-ха!"
    show kotonoha cm
    y "...угх..."
    show kotonoha om oe lself rhip
    k "И мне кажется, я знаю, почему."
    show kotonoha ldown rdown
    k "Кстати, как раз хотела у тебя спросить: как прошёл «первый шаг»?"
    show kotonoha cm
    y "...Макс узнал меня поближе и решил немного обо мне позабиться..."
    y "...наверное..."
    show kotonoha omb
    k "Ого-го!"
    show kotonoha ce
    k "Юри, невероятно!"
    show kotonoha cm
    y "Э-э?"
    show kotonoha om oe lup
    k "Теперь у тебя есть «официальный» парень!"
    show kotonoha cm ldown
    y "Н-нет, всё не так!"
    show kotonoha om ce
    k "Наконец-то моя подруга полноценно познаст любовные отношения!"
    show kotonoha cm
    "Я сейчас растворюсь от стыда!"
    show kotonoha oe
    y "Ви-ви-ви-ви-ви-ви-ви--{nw}"
    show kotonoha om ce
    k "Тихо, успокойся!"
    show kotonoha oe
    k "Я знаю, это очень волнительно..."
    show kotonoha ce
    k "...но мне безумно интересно мотивировать тебя на дальнейшие действия!"
    show kotonoha cm
    y "...и-и-и-и-и-и--{nw}"
    show kotonoha oe at t22
    show natsuki turned neut cm oe school_bag at l21
    pause 0.7
    show natsuki om oe lhip rhip
    n "О, здрасьте."
    show natsuki cm oe
    show kotonoha om ce lup rhid
    k "Привет, Нацуки!"
    show kotonoha cm ldown rdown
    y "......"
    show natsuki curi om oe ldown rdown
    show kotonoha oe
    n "Что с Юри опять произошло?"
    show natsuki om oe
    show kotonoha neut cm oe
    n "Коха, ты её сломала?"
    show natsuki neut cm oe
    show kotonoha anno om oe
    k "Ох, любишь же ты моё сокращённое имя..."
    show natsuki om oe
    show kotonoha cm
    n "Мне так удобнее."
    show natsuki pout om oe lhip rhip
    show kotonoha neut cm oe
    n "Так, вообще: я подумала заглянуть к Юри на огонёк, пока между классами шла, а тут...{w}такое."
    show natsuki curi om oe
    n "Что с ней случилось?"
    show natsuki lsur cm oe
    show kotonoha happ om ce
    k "У неё теперь есть официальный парень!" with vpunch
    show kotonoha cm
    "{sc=3}ЗАЧЕМ ТЫ ЭТО СКАЗАЛА?!{/sc}"
    show natsuki nerv om oe ldown rdown
    show kotonoha oe
    n "Да ладно, не верю..."
    show natsuki cm oe
    show kotonoha om
    k "Факт есть факт."
    show natsuki laug om oe lhip rhip
    show kotonoha cm
    n "И кто же этот «соблазнитель»?"
    show natsuki ma oe
    show kotonoha om
    k "Это--{nw}"
    show natsuki lsur cm oe
    show kotonoha lsur cm oe
    y "Стой, не говори, что это Макс!!!"
    n "..."
    k "..."
    "..."
    "{sc=3}ЧТО Я СКАЗАЛА?!{/sc}"
    show natsuki anno om ce
    show kotonoha happ cm ce
    n "Тьфу ты."
    show natsuki neut om oe
    n "Хотя это было понятно изначательно."
    show natsuki sedu om oe
    show kotonoha oe
    n "Вчера в коридоре вдвоём «стихами обменивались» аж минут 10, а потом ты счастливой вернулась."
    show natsuki cm oe
    show kotonoha om ce
    k "Ох, вот как?"
    show kotonoha cm
    "{sc=3}Не-е-е-е-е-е-ет!!!{/sc}"
    show natsuki neut om oe
    show kotonoha oe
    n "Кстати, о стихах..."
    show natsuki cross curi om oe school_bag
    show kotonoha neut cm oe
    n "Коха, почему ты всё-таки к нам не вступишь?"
    show natsuki cm oe
    show kotonoha om
    k "Я так не говорила."
    show natsuki doub om ce
    show kotonoha cm
    n "Хорошо, перефразирую: почему ты так долго думаешь?"
    show natsuki cm oe
    show kotonoha happ omb ce
    k "Я ещё не готова, ха-ха-ха!"
    show kotonoha om oe
    k "Мне же придётся развить своё вдохновение, а с ним у меня некоторые проблемы."
    show natsuki om oe
    show kotonoha cm
    n "Отговорка."
    show natsuki cm oe
    show kotonoha om ce
    k "Вот и нет."
    show natsuki om oe
    show kotonoha cm
    n "А вот и да!"
    show natsuki neut cm oe
    show kotonoha oe
    y "Нацуки..."
    show natsuki anno cm oe
    y "...пусть она сама решит..."
    show natsuki turned om oe lhip rhip school_bag
    n "Ты вообще молчи, лучше о своём следующем «свидании» думай."
    show natsuki cm oe
    y "Это грубо!"
    show natsuki neut cm oe
    show kotonoha neut om oe rhip
    k "Но она права, Юри."
    k "Тебе каждый раз придётся делать шаги, чтобы быть ближе и ближе к Максу."
    show kotonoha sad om ce
    k "Если ты перестанешь их совершать, то весь результат сойдёт на нет."
    show kotonoha nerv om oe
    k "Мало ли кто его ещё соблазнит?"
    show natsuki cross nerv cm e1b school_bag
    show kotonoha cm
    y "Умф-ф..."
    show natsuki om
    n "Да уж, кто этих парней разберёт..."
    show natsuki doub om oe
    show kotonoha happ cm oe
    n "Ты же теперь его потенциальная девушка: чмокни его в щёку."
    show natsuki turned doub om oe lhip rhip school_bag
    show kotonoha lsur cm oe rdown
    n "Чего тут сиськи мять?"
    show natsuki cm
    show kotonoha om
    k "Последняя фраза была лишней, Нацуки..."
    show natsuki curi om oe
    show kotonoha cm
    n "Но ведь она это и делает, буквально."
    show natsuki cm
    "Я сейчас...{w}сгорю от стыда..."
    show natsuki angr cm oe ldown rdown
    show kotonoha nerv om ce lup rhip
    k "Юри, забудь это недоразумение."
    show natsuki om
    show kotonoha cm ldown
    n "Это ты про меня?"
    show natsuki anno cm oe
    show kotonoha sad om oe
    k "Я про ту фразу!"
    show natsuki neut cm oe
    show kotonoha neut om oe
    k "Нацуки в действительности дело говорит: ты должна повышать планку захода в его пространство."
    show kotonoha happ om oe
    k "Ты должна поцеловать его."
    show natsuki curi cm oe
    show kotonoha cm
    y "Я?..."
    "Мне...{w}поцеловать Макса..."
    call window_close

    call window_dialog_fast_transition

    call window_open
    scene bg club_day
    show gray zorder 1:
        alpha 0.25
    show vignette zorder 2:
        alpha 0.5
    show mc turned lsur cm oe at e11
    y "Макс..."

    show black zorder 3 with dissolve
    pause 0.25
    y "Тю~"

    hide black
    show mc happ cm oe n3
    with dissolve
    show mc om
    mc "Юри!"
    mc "Ты меня соблазнила."
    show mc ce
    mc "Теперь меня не остановить!"
    show mc cm
    y "{sc=3}Э-э-э-э-э-э?!{/sc}" with vpunch

    scene black with dissolve
    y "Н-не надо, Макс..."
    y "Перестань..."
    y "Ох, стой, не надо..."
    call window_close

    call window_dialog_fast_transition

    call window_open
    scene bg school f1 old_stairwell right
    show natsuki turned angr cm e4c b1b lhip rhip school_bag at i21
    show kotonoha happ cm ce n3 at i22
    pause 0.2
    show natsuki mq
    n "Сама перестань!" with vpunch
    show natsuki cm oe -b1b
    show kotonoha om oe n1
    k "Завидуешь, Нацуки?"
    show natsuki mq e4c b1b at h21
    show kotonoha cm
    n "Божечки-кошечки!"
    n "Да идите вы все со своими отношениями!"
    show natsuki ldown rdown
    n "Фу!"
    show natsuki cm
    hide natsuki with easeoutleft
    show kotonoha at t11
    show kotonoha om ce
    k "Всё-таки завидует, хе-хе..."
    show kotonoha oe
    k "Юри."
    show kotonoha cm
    y "Ах, помедленнее..."
    show kotonoha neut om oe
    k "Юри!"
    show kotonoha cm
    y "Нежнее, Макс..."
    show kotonoha sad om oe
    k "Ох, социальный голод на тебя очень плохо влияет..."
    show kotonoha cm
    stop noise_1 fadeout 5.0
    stop music fadeout 5.0
    call window_close

    call window_dialog_long_transition("mc")
    play noise_1 school_corridor_empty_noise fadein 3.0

    call window_open
    scene bg school new_class_mc day with dissolve_scene_full
    "Снова тишина без миссис Иды..."
    "Снова в клуб..."
    "Прошло всего чуть меньше недели, а ноги уже сами по рефлексу ведут меня туда."
    call window_close

    call plot_transition
    $ h_name = "???"

    call window_open
    pause 1.0
    "Так, сейчас надо повернуть--{nw}"
    n "{size=17}Да отстань ты от меня уже, а?!{/size}"
    "Нацуки?"
    h "{size=17}Стой...{/size}"
    n "{size=17}Я тебе сейчас врежу со всей дури!{/size}"
    n "{size=17}И плевать, что скажет глава школьного совета или преподаватели!{/size}"
    "Кто это?"
    h "{size=17}Я от тебя сейчас ничего не хочу.{/size}"
    n "{size=17}Так отвали нахрен!{/size}"
    h "{size=17}Я хотел бы извиниться за тот случай в понедельник.{/size}"
    "Это тот, кто бежал тогда за Нацуки?"
    n "{size=17}С чего вдруг у тебя проснулась совесть?{/size}"
    h "{size=17}Просто это было...{w}слишком грубо и неправильно с моей стороны.{/size}"
    h "{size=17}Я тогда сам не свой был, не знаю, что на меня нашло...{/size}"
    h "{size=17}Прости.{/size}"
    n "{size=17}...{/size}"
    n "{size=17}Долго же ты думал...{/size}"
    h "{size=17}В качестве извенения я хотел бы предложить тебе--{nw}{/size}"
    n "{size=17}...короче, чтобы больше такого не вытворял, понял?!{/size}"
    n "{size=17}И это не значит, что я с тобой буду общаться.{/size}"
    h "{size=17}Да я понимаю твою реакцию, но я хотел бы--{/size}{nw}"
    n "{size=17}Зашибись, свободен.{/size}"
    h "{size=17}--предложить тебе прогуляться и купить тебе парфе--{/size}{nw}"
    n "{size=17}ИДИ В ЗАДНИЦУ, ДОСТАЛ УЖЕ!{/size}"
    h "{size=17}Ты даже не дослушала--{/size}{nw}"
    $ h_name = _("Хироши")
    n "{size=17}О-о, Макс, приве-е-ет!{/size}"
    "А?!"
    "Как она меня заметила?!"

    scene bg school f3 new_corridor
    show natsuki turned fc happ cm oe school_bag at t11
    with wipeleft_scene
    show natsuki oe
    mc "Хах, привет."
    show natsuki om lhip rhip
    n "Тоже идёшь в клуб?"
    show natsuki cm
    mc "Ага."
    show natsuki om
    n "Пошли вместе, заодно проверишь мой стих."
    n "Только ключа от клуба у меня нет, Монику не видела, значит, если что, постоим в коридоре, как вчера."
    show natsuki neut cm oe
    mc "Да ну, тратить время впустую?"
    show natsuki om e1b
    n "Ага..."
    show natsuki cm ldown rdown
    hide natsuki with easeoutleft
    pause 0.5
    "Какая-то она чрезмерно общительная."
    "Нет, я уже понял, что она пытается избавиться от внимания того парня, но...{w}что у них случилось?"

    scene black with wipeleft_scene
    mc "Нацуки, кто это был?"
    n "А?"
    n "Да так...{w}не засоряй голову."
    mc "...ну, если вдруг нужна помощь или что-то такое -- ты обращайся."
    n "Угу-угу."
    "Не нравится мне, что она всё нивелирует, но лезть в её личную жизнь точно не буду."
    "Если ей вдруг понадобится помощь, то пусть её попросит, мы ей не откажем."

    scene bg corridor
    show natsuki turned worr cm oe school_bag at t11
    with wipeleft_scene
    show natsuki curi om e1b
    n "Та-а-ак, погоди-ка..."
    n "Что-то здесь не так."
    show natsuki cm oe
    mc "Ну, вроде всё на месте."
    show natsuki om lhip rhip
    n "А ты не увидел?"
    show natsuki cm
    mc "Что?"
    show natsuki om
    n "Дверь в клуб приоткрыта."
    show natsuki cm
    mc "Да ну..."
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    mc "И правда..."

    scene bg school literature_club board day
    show natsuki turned pani cm e2b school_bag at t11
    with wipeleft_scene
    show natsuki pani om oe at h11
    n "{size=19}Кто шуршит в моей кладовке?!{/size}"
    show natsuki cm oe
    mc "{size=19}Тихо!{/size}"
    show natsuki om oe
    n "{size=19}Просто так никто туда не полезет!{/size}"
    show natsuki pout cm oe
    mc "{size=19}Без понятия, с какой целью, но это может быть только кто-то из нашего клуба.{/size}"
    show natsuki lhip rhip
    mc "{size=19}Посмотри, сумку тут ничью не видишь?{/size}"
    show natsuki e1b
    n "{size=19}М-м-м...{/size}"
    show natsuki worr om oe
    n "{size=19}Вон там, фиолетовая...{/size}"
    show natsuki pout om e1b
    n "{size=19}Юри...{/size}"
    show natsuki cm
    mc "{size=19}Так, отлично.{/size}"
    show natsuki vang om oe
    n "{size=19}Чего отличного?{/size}"
    n "{size=19}Она снова полезла в МОЮ кладовку и что-то там копошится!{/size}"
    show natsuki cm
    mc "{size=19}Да что ты так распереживалась?{/size}"
    show natsuki pout om oe
    n "{size=19}Потому что помнишь понедельник?{/size}"
    show natsuki angr cm oe
    mc "{size=19}Да, она знатно тебе прописала...{/size}"
    show natsuki om
    n "{size=19}А сказать, из-за чего?{/size}"
    show natsuki cm
    mc "{size=19}Кладовка?{/size}"
    show natsuki om ce
    n "{size=19}Угадал, она там всё переворотила, пока чистила класс к твоему приходу, на что я дико возмутилась.{/size}"
    show natsuki cm
    mc "{size=19}Вы аж класс чистили, нифига себе...{/size}"
    show natsuki pout om oe
    n "{size=19}Ты мне лучше скажи, что мы делать будем?{/size}"
    show natsuki cm
    mc "{size=19}А чё делать-то?{/size}"
    show natsuki pani cm oe ldown rdown
    mc "{size=19}Подойдём и поговорим прямо сейчас.{/size}"
    show natsuki om
    n "{size=19}Она меня убьёт!{/size}"
    show natsuki pout cm oe
    mc "{size=19}Не в мою смену.{/size}"

    scene black with wipeleft_scene
    mc "Юри?"
    mc "Привет--{nw}"
    play sound book_fall
    y "А-а-А-а-А-а-А--{nw}"
    n "А-А-А!!!--{nw}"
    mc "ЛОВЛЮ!!!--{nw}"
    play sound hugs
    pause 2.0
    mc "...устоял."
    "..."
    "Что-то очень мягкое у меня на груди...{w}дикое сердцебиение чувствуется...{w}а ещё сладковатый запах волос дурманит голову..."

    scene bg closet
    show yuri turned vsur cm oe n4 at e11 zorder 2
    show natsuki turned laug cm oe at i44
    with dissolve_scene_full
    y ".................."
    mc "...ты цела?"
    show natsuki om ce lhip rhip
    n "ПХА-ХА-ХА-ХА!!!"
    show yuri e2c
    show natsuki oe
    n "Ребята, целуемся!"
    show yuri mk oe
    show natsuki cm
    y "Э-э-Э-э-Э--{nw}"
    show yuri sedu cm ce
    show natsuki lsur cm oe
    mc "Стоп, что--{nw}"
    show natsuki shoc om oe ldown rdown at h44
    n "НЕТ, ЮРИ!!!{nw}"

    show black zorder 3 with dissolve
    pause 0.25
    y "М-м-м!{nw}"
    mc "ПФ-Ф-Ф-Ф-Ф-Ф-Ф--{nw}"
    y "--пфу..."
    mc "Кх-х-хпф-ф-фпфпфе-е-е!"

    hide black
    show yuri nerv cm e2b lup rup n3 at s21
    show natsuki shoc cm oe at i22
    with dissolve
    pause 0.25
    mc "Так, алё, я не понял, это чё?!"
    y "Угх-х..."
    show natsuki ce
    n "...внезапная шутка вышла из-под контроля..."
    mc "Ну у вас и шутки, блин..."
    show yuri ce
    show natsuki pout cm oe
    y "П-прости, Макс..."
    mc "Да...{w}ничего..."
    show yuri lsur cm oe
    mc "Забудем этот инцидент..."
    show natsuki om e1b
    n "Да уж..."
    show yuri n1 ldown rdown at t21
    show natsuki oe lhip rhip
    n "Юри, ты лучше скажи, что ты в кладовке делала?"
    show yuri om
    show natsuki cm
    y "Я?..."
    show yuri e2b
    y "У-у..."
    call window_close

    call window_dialog_fast_transition("y")

    call window_open
    play music t6o
    scene bg school new_class_yuri day
    show gray zorder 1:
        alpha 0.25
    show vignette zorder 2:
        alpha 0.5
    y "{size=19}Да что ж такое...{/size}"
    "Я всё ещё не в себе..."
    "Сердце колотится."
    "Но по ощущениям будто я на облаке..."
    stop noise_1 fadeout 3.0

    play noise_2 school_corridor_hard_noise fadein 3.0
    scene bg school f3 new_corridor
    show gray zorder 2:
        alpha 0.25
    show vignette zorder 3:
        alpha 0.5
    show crowd_foreground zorder 1
    show crowd_background zorder 0
    with wipeleft_scene
    "Стоит чем-нибудь заняться, чтобы отвлечься и успокоиться..."
    "Но чем?"
    stop noise_2 fadeout 3.0

    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school literature_club board day
    show gray zorder 1:
        alpha 0.25
    show vignette zorder 2:
        alpha 0.5
    with wipeleft_scene
    y "Никого..."
    "На нервах пришла раньше всех?"
    y "Угх..."
    y "Заняться-заняться-заняться..."
    "Думай-думай..."
    "Убраться в классе?"
    "Нет..."
    "Убраться в кладовке?"
    "..."
    "Или...{w}посмотреть из любопытства её состав..."
    "Что же в манге такого интересного, что Нацуки столько её накупила?"

    scene black with wipeleft_scene
    y "Хм..."
    "Лишь бы ничего не переворотить..."
    "..."
    "Сплошные цветные обложки с непонятными персонажами..."
    "Да ну, ерунда какая-то..."
    "Лучше почитать какую-нибудь книжку."
    "Тут не развивается воображение."
    "Множество всяких клише, бессмысленных и пустых эпизодов..."
    "..."
    "А это что?..."
    y "Тора...{w}Д...{w}э?"
    "Что за название такое?"
    "Какая-то...{w}романтическая комедия?"
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    y "Да что ты думаешь?"
    y "Просто покажи ей свои чувства!"
    y "Зачем придумывать такой сложный план?"
    y "Ведь чувства -- это то, что хочет получить девушка в ответ--{nw}"
    n "{size=17}Кто шуршит в моей кладовке?!{/size}"
    y "!!!" with vpunch
    mc "{size=17}Тихо!{/size}"
    "Нет-нет-нет-нет-нет!"
    "Надо срочно вернуть эту мангу обратно!"
    "Но почему именно она должна быть на самой высокой полке?!"
    "Я так не дотянусь, нужно что-то поставить под ноги!"
    n "{size=17}Чего отличного?{/size}"
    n "{size=17}Она снова полезла в МОЮ кладовку и что-то там копошится!{/size}"
    "Плохо дело!"
    "Кроме компьютерного кресла, нечего поставить..."
    "Придётся аккуратно на него встать..."
    "Так..."
    "Осторожно, Юри, ты слишком большая для такого стула..."
    "Как бы...{w}меня грудь не перевесила...{w}неудобно держать баланс..."
    n "{size=17}Ты мне лучше скажи, что мы делать будем?{/size}"
    mc "{size=17}А чё делать-то?{/size}"
    "Ещё есть время!"
    "Не надо слушать разговор, надо акцентироваться на равновесии..."
    "Та-а-ак..."
    "Ещё немножко..."
    "Ещё чуть-чуть..."
    "Ох, встала во весь рост!"
    "Ой, не-е-ет!"
    "Соседние томики покосились из-за пустого места!"
    "Выровню их одной рукой, а другой всуну недостающий..."
    mc "Юри?"
    mc "Привет--{nw}" with vpunch
    play sound book_fall
    "А-А-А, ЗАЧЕМ Я ДЁРНУЛАСЬ, Я ТЕРЯЮ РАВНОВЕСИЕ--{nw}"
    y "А-а-А-а-А-а-А--{nw}"
    call window_close

    stop music fadeout 0.38
    call window_dialog_fast_transition("mc")

    call window_open
    scene bg closet
    show yuri shy neut m2 oe n5 at s21
    show natsuki turned curi cm oe at i22
    n "..."
    show natsuki om
    n "Юри..."
    show natsuki lhip rhip
    n "Если ты так хочешь почитать мою мангу, то можешь просто попросить."
    show natsuki neut om oe
    n "Ты моя подруга, тебе я доверяю."
    show natsuki curi om e1b ldown rdown
    n "Если ты только не удумаешь сделать с ней что-то плохое..."
    show natsuki cm oe
    y "..."
    show natsuki neut cm oe
    mc "Знаете, я пока проветрюсь ненадолго в коридоре, а то что-то голова плыть начала..."
    show natsuki laug mb oe lhip rhip
    n "Кхм, окей."
    show natsuki ma
    mc "Что за смешок?"
    show natsuki nerv om ce
    n "Нет, ничего-ничего, иди уже."
    show natsuki cm
    mc "Ладно..."

    scene black with wipeleft_scene
    "Почему...{w}Юри {b}это{/b} сделала?..."
    "Хорошо, предположим сразу напрямую -- она в меня влюбилась."
    "А теперь включаем логику и пытаемся проанализировать этот вариант."
    "Всё время, что я провёл с ней, -- это обмен стихами, позавчерашняя прогулка и...{w}ну и руки выделим, как отдельное событие."
    "Причём эти руки она показала мне из-за того, что сильно доверяет."
    "Собственно говоря, каким образом за такое короткое время?"
    "Как это вообще работает--{nw}"
    play sound closet_open
    s "Привет, ребята!{nw}"
    play sound hit_wood
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 0.25
    mc "АЙ!"
    s "ОЙ!"
    m "Макс, не ушибся?!"
    mc "Сайори...{w}м-м-м...{w}аккуратнее, пожалуйста."
    s "Прости..."
    mc "Дайте я развеюсь."
    mc "Заодно стих перепроверю."
    m "Конечно, только недолго."
    mc "Да-да-да, понимаю..."
    "Чёрт, как же она смачно мне заехала..."
    "Больно-то как..."
    call window_close

    pause 1.0
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor with wipeleft_scene
    "Хочу просто побыть в тишине, чтобы сбросить напряжение и собраться с мыслями..."
    "А то уже чувствую, как начинаю раздражаться."
    "Ещё держусь, но могу порваться."
    "Так, желательно сейчас уйти подальше от клуба, а то обязательно кто-нибудь выскочит и начнёт донимать своими расспросами про моё состояние, что меня ещё больше выбесит."
    "Где был торговый автомат, который я видел краем глаза?"
    "На третьем этаже?"
    "У меня есть с собой кое-какая мелочь, можно что-нибудь купить и охладиться."
    call window_close

    call plot_transition

    call window_open
    scene bg school f3 old_corridor with wipeleft_scene
    mc "А вот и ты..."
    "Так, автомат, чего ж тут у тебя?"
    "Вода -- 100 иен."
    "Всякие соки -- от 130 до 160 иен."
    "Газировки..."
    "Ещё какая-то хрень..."
    mc "Люди -- полнейшие извращенцы."
    "Столько химии..."
    mc "Оп."
    "А вот это что?"
    "«Матча Сода»?"
    "Газированное подобие зелёного чая?"
    "140 иен."
    mc "М-м-м..."
    "Ладно, попробуем из любопытства."
    call window_close

    scene black with wiperight
    pause 3.0
    play sound vending_machine_drinks
    pause 22.323
    play sound soda_open
    pause 2.0

    call window_open
    "Ирония ситуации в том, что я сам только что купился на эту химию."

    scene bg school old_corridor wall zorder 1
    show matcha_soda zorder 2
    with wipeleft_scene
    "На вкус...{w}как газированный холодный зелёный чай...{w}с какими-то странными мелкими желеобразными волокнами."
    "Не сопли, надеюсь?"
    "..."
    mc "Тьфу, что за мысли..."
    "Но этот напиток всяко лучше, чем ничего."
    "Я хотя бы уже нормально себя чувствую."
    "..."
    "Не знаю, что на меня нашло..."
    "Мог бы сразу отпустить Юри, а не пялиться ей в глаза, прижавшись к ней всем телом."
    "Опять какой-то приступ идиотизма..."
    "Так возбудила близость к девушке?"
    "Нежности и совокупления захотелось?"
    mc "Знаешь что, социальный голод?"
    mc "Иди ты нахрен."
    "Это уже ненормально."
    "...хотя чего я, у меня же толком друзей и приятелей не было."
    "То увлечения другие, то по характеру никак, то что-то другое..."
    "Можно сказать, детство в этом плане ушло в помойку."
    "Хотя бы родители обо мне заботились хорошо, не без перегибания палок, конечно..."
    "А теперь юношество творит такую дичь, которая тоже гроша стоить не будет...{w}или нет?"
    "Всё-таки для меня Литературный клуб -- находка из разряда вон выходящего."
    "4 девушки, которым я, внезапно, небезразличен, причём в хорошем плане."
    "Звучит, как сюжет дешёвой визуальной новеллы."
    "Однако мне крайне не нравятся их скелеты в шкафах и странные действия..."
    "А ведь я ещё не всё узнал, лишь самую малость."
    "И если не разгрести этот бардак, то всё выйдет плачевно."
    "Меня и так совесть покусывает, будто я уже что-то могу сделать."
    "Кстати, что там по стиху?"
    "Только сначала банку на подоконник поставлю..."
    hide matcha_soda with dissolve
    call show_poem(poem_mc4, music=False)
    "Какой же это всё-таки...{w}бред."
    "Вечером я был более лояльный и замыленный, всё было не так заметно..."
    "Вот если бы этот стих написала Сайори, немножко перефразировав под себя, то я бы оценил это совершенно по-другому."
    "Это стих её стиля."
    "Она должна была его написать, а не я."
    "А у меня какая-то дурацкая недопародия в перемешку со стилем Нацуки."
    show matcha_soda zorder 2 with dissolve
    y "Макс?..."

    scene bg school f3 old_corridor
    show yuri turned neut cm e1d at t11
    show matcha_soda zorder 2
    with wipeleft_scene
    mc "Юри?"
    mc "Что ты тут делаешь?"
    show yuri dist om oe
    y "Я..."
    show yuri neut om e1d
    y "...от волнения вышла в туалет."
    y "А потом решила прикупить себе что-нибудь попить."
    show yuri cm
    "...прямо как я?"
    "Охотно верю."
    "Не из-за меня ли?"
    "Ох, точно!"
    show yuri curi cm oe
    mc "Кстати, пока никого нет..."
    show yuri om oe
    y "Да?"
    show yuri lsur cm oe
    mc "Ты обработала себе руки, как я просил?"
    show yuri om oe
    y "Конечно, сразу!"
    show yuri
    y "Вот..."
    show yuri cm
    call window_close

    pause 0.2
    show yuri rbandages with dissolve_cg
    pause 0.5
    show yuri neut om e1d

    call window_open
    y "Они быстро зажили."
    show yuri cm
    mc "Это хорошо."
    show yuri rdown with dissolve_cg
    pause 0.5
    mc "Может, расскажешь, почему ты это делаешь?"
    show yuri flus cm oe
    y "Я-я..."
    show yuri worr om oe
    y "Я ещё не готова..."
    show yuri cm oe
    mc "Хорошо, не тороплю."
    show yuri cm ce
    "Мда, набор микротем, а не разговор."
    show yuri dist om ce
    y "Ох..."
    show yuri worr om oe
    y "Я забыла взять с собой монеты..."
    show yuri lup rup
    y "«Матча Сода»..."
    show yuri cm oe
    "Пф-ф-ф..."
    show yuri lsur cm oe
    mc "Держи."
    show yuri om oe
    y "Н-но это же твоя..."
    show yuri cm oe
    mc "Нет, не хочу больше."
    show yuri neut cm e1d ldown rdown
    mc "Она практически целая, сделал всего один глоток."
    hide matcha_soda with dissolve
    show yuri lup rup matcha_soda_hup with dissolve
    pause 0.5
    show yuri happ om ce
    y "Спасибо, Макс!"
    y "Ты очень добр."
    show yuri cm oe
    mc "Тебе она так нравится?"
    show yuri om oe
    y "Это мой самый любимый напиток."
    y "Я его часто покупаю."
    y "Ты тоже любишь Матча Соду?"
    show yuri cm oe
    mc "Просто взял попробовать из любопытства."
    show yuri om e1b
    y "Понятно."
    show yuri neut cm e1d
    mc "Ладно, пора обратно идти, не хочется никого задерживать."
    show yuri worr om oe
    y "Ох, хорошо..."
    show yuri cm oe

    scene black with wipeleft_scene
    y "И, кстати, Макс..."
    mc "Что?"
    y "Прости...{w}за тот случай..."
    mc "Ой, Юри, забыли."
    y "Просто...{w}это было так неожиданно и близко...{w}я не совладела собой..."
    mc "...а?"
    y "У-ум..."
    mc "Я понимаю, весна, гормоны, хочется...{w}хочется, но постарайся держать себя в руках."
    mc "Не хотелось бы, чтобы под твою любовную раздачу попал кто-то извне."
    mc "А то кончится это плачевно."
    y "О-ох, хорошо..."
    mc "Да и если тебе так сильно хочется..."
    mc "Ты же ведь пока одна живёшь?"
    mc "Ну...{w}одна...{w}ну ты поняла."
    y "М-Макс..."
    mc "Да, извини, это было лишнее..."
    "Но а как ей ещё напряжение снимать?"
    "Не порезами же?"
    call window_close

    call plot_transition

    call window_open
    play music t5 fadein 3.0
    scene bg school literature_club board day with wipeleft_scene
    mc "Всё, мы здесь, готовы к обмену."
    show monika forward neut cm oe at t11
    pause 0.2
    show monika om oe
    m "Всё в порядке?"
    show monika happ cm oe
    mc "Да."
    show monika om ce
    m "Отлично!"
    show monika om oe lpoint rhip
    m "Итак, друзья!"
    show sayori turned happ cm oe at t41
    show monika cm oe ldown rdown at t42 zorder 2
    show natsuki turned happ cm oe at t43
    show yuri turned happ cm oe at t44
    pause 0.5
    show monika om ce
    m "Доставайте свои стихотворения: начинаем обмен!"
    show monika cm ce
    hide sayori with easeoutleft
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    pause 0.5
    show monika om oe at t11
    m "Что ж, Макс, показывай свой последний экспериментальный стих."
    show monika cm oe
    mc "Вот, держи."
    call window_close

    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show monika e1b
    pause 6.0
    show monika mn
    pause 6.0
    show monika om ce

    call window_open
    m "Забавно вышло!"
    show monika e1b
    m "Простой, лёгкий по чтению."
    show monika oe
    m "У тебя получился полноценный стиль Нацуки!"
    show monika cm
    mc "Да ну, схожесть есть, но не настолько же."
    show monika om
    m "Говорю как есть."
    show monika cm oe
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    show monika om ce
    m "Очень хорошо, Макс!"
    show monika om oe lpoint
    m "Теперь мне нужно будет детально всё изучить."
    show monika cm oe ldown
    mc "Да, я помню, остальные два стиха у меня с собой."
    mc "Передам их, когда закончу с этим."
    show monika om oe
    m "Конечно."
    show monika cm oe
    mc "Теперь твоя очередь, Моника."
    show monika om ce
    m "Да, прошу!"
    show monika cm ce
    call show_poem(poem_m4)
    "Нифига себе..."
    mc "У меня нет слов..."
    show monika om e1b
    m "В этот раз у меня было особое вдохновение."
    show monika oe
    m "Поэтому и вышло достаточно продуктивно."
    show monika cm oe
    mc "Но это реально невероятно."
    show monika flus om oe
    m "Было бы ещё так постоянно..."
    show monika cm oe
    mc "Моника, если вдруг устанешь или нужна будет помощь, дай знать."
    show monika happ cm oe b1b
    mc "Я же теперь неформально твоя левая рука...{w}или правая?"
    show monika om oe
    m "Ты участник моего клуба, а не рука, Макс."
    show monika om ce -b1b
    m "Но спасибо за поддержку, я это ценю."
    show monika cm oe
    mc "Только не сдавайся и почаще отдыхай."
    show monika om ce
    m "Само собой, ха-ха!"
    show monika om oe lpoint
    m "Ты очень заботливый!"
    show monika cm oe ldown
    mc "Просто я за вас переживаю..."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    pause 1.0
    mc "Хорошо, не буду задерживаться, покажу стих остальным."

    scene black with wipeleft_scene
    "Значит, и с Моникой не всё так радужно?"
    "Может, у неё нет человека, который бы о ней позаботился?"
    "А родители?"
    "Что-то я начинаю путаться в этой каше..."

    scene bg club_day
    show sayori turned happ cm oe at t11
    with wipeleft_scene
    show sayori om ce lup rup at h11
    s "О, а вот и ты, Макс!"
    show sayori cm ce ldown rdown
    mc "Угу."
    show sayori sad om oe
    s "Ты был тогда совсем не свой..."
    s "С тобой всё хорошо?"
    show sayori cm oe
    mc "Честно?"
    mc "Не знаю, был не в себе..."
    show sayori om e2b at s11
    s "Ох..."
    show sayori cm oe
    mc "Но всё уже прошло."
    mc "И надеюсь, не повторится."
    show sayori neut om oe at t11
    s "Ты можешь мне выговориться, если тебе плохо."
    show sayori cm oe
    mc "Сайори, не парься, всё нормально."
    mc "Спасибо."
    show sayori dist om ce
    s "Если так..."
    show sayori happ om oe b1b
    s "...то я рада."
    show sayori cm oe
    mc "Давай лучше о другом поговорим."
    show sayori -b1b
    mc "Вот мой стих."
    show sayori om ce lup rup at h11
    s "О, точно!"
    show sayori cm ce ldown rdown
    call window_close

    play sound paper_torn_out
    show sayori lup poem_paper with dissolve
    pause 1.0
    show sayori e1b
    pause 11.0
    show sayori happ om ce

    call window_open
    s "Прямо как у Нацуки!"
    show sayori cm ce
    "Что-то такое я и ожидал услышать."
    show sayori cm oe
    mc "Ага."
    show sayori om oe
    s "Ну..."
    show sayori nerv om oe
    s "...хе-хе..."
    show sayori neut om oe
    s "Мне больше нечего сказать, извини."
    show sayori cm oe
    mc "Да, я тебя понимаю."
    play sound paper_torn_out
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    show sayori angr cm oe
    mc "Оценивать стих про апельсин после того полугодовалого случая у тебя в гостях, когда при чистке кожуры этот фрукт выстрелил тебе в глаза соком, довольно трудно."
    show sayori om ce
    s "Фу!"
    s "Даже вспоминать не хочу!"
    show sayori vang cm ce
    mc "Пха-ха, ты тогда вокруг кухонного стола бегала, как хомяк, полный энергии."
    show sayori om ce
    s "Бе-е-е!"
    show sayori mj ce
    mc "Ладно-ладно, молчу."
    show sayori anno cm e1b
    mc "Всё-таки это довольно неприятно."
    show sayori neut cm oe
    mc "Знаешь, давай я лучше твой стих гляну."
    show sayori happ cm oe
    mc "Уверен, мне будет что по нему сказать."
    show sayori om oe
    s "Хм-хм-хм, читай."
    show sayori cm oe
    call show_poem(poem_s4)
    "По-моему, это самое позитивное и бодрое стихотворение из всех, которые я у неё видел."
    mc "У меня самого аппетит разыгрался."
    show sayori tap nerv om oe at s11
    s "Э-хе-хе~"
    show sayori turned happ cm oe at t11
    mc "Мне этот стих больше всего понравился."
    s "М-м-м?"
    mc "На душе тепло от него стало."
    mc "Ты молодец, Сайори."
    show sayori om e2b at s11
    s "Спасибо..."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    show sayori cm
    pause 1.0
    show sayori oe at t11
    mc "Раз с этим всё, то обменяюсь ещё с Нацуки и Юри."
    show sayori om oe
    s "Хорошо."
    show sayori cm oe

    scene black with wipeleft_scene
    "Хоть у кого-то здесь всё в порядке."
    "А пока на очереде освободившаяся Нацуки."

    scene bg closet
    show natsuki turned neut cm oe at t11
    with wipeleft_scene
    mc "Я снова тут."
    show natsuki om oe
    n "Видела, вы с Юри вместе вернулись из коридора."
    show natsuki cm oe
    mc "Да, так совпало, и?"
    show natsuki sedu om oe lhip rhip
    n "Неужто тебе было мало контакта у кладовки?"
    show natsuki cm oe
    mc "Ты на что намекаешь?..."
    show natsuki om ce
    n "Ну, мало ли..."
    show natsuki om oe
    n "Вы подозрительно оба вышли из клуба, хоть и не вместе."
    n "А в коридоре практически никого, сама Юри была не против того поцелуя, а её тело такое мягкое--{nw}"
    show natsuki anno cm oe ldown rdown
    mc "Так, Нацуки, хватит с меня твоих приколов."
    mc "Лучше почитай мой стих, пока мы вдвоём от стыда не сдохли."
    show natsuki om oe
    n "Пф-ф-ф, душнила."
    show natsuki cm oe
    play sound paper_torn_out
    show natsuki lup poem_paper with dissolve
    pause 1.0
    show natsuki neut cm oe
    mc "Заодно свой «пример» забери."
    play sound paper_torn_out
    pause 1.0
    "Надо было отдать его ещё перед клубом, но у меня он из головы вылетел."
    call window_close

    show natsuki e1b
    pause 10.0
    show natsuki om

    call window_open
    n "Не так плохо, как я думала."
    show natsuki cm oe
    mc "Сомневалась?"
    show natsuki om oe
    n "Учитывая твои первые стихи, вполне."
    show natsuki e1b
    n "Ты более-менее устаканился по написанию."
    show natsuki cm
    mc "Да, есть такое ощущение."
    show natsuki om oe
    n "В общем, продолжай в том же направлении."
    show natsuki cm oe
    play sound paper_torn_out
    show natsuki ldown with dissolve
    pause 1.0
    show natsuki fc happ om oe lhip rhip
    n "Окей, а теперь мой."
    show natsuki cm ce
    call show_poem(poem_n4)
    "Снова еда?"
    "Сговорились, что ли?"
    "А если серьёзно, то это...{w}пока её самое спокойное стихотворение."
    "Но когда она вообще кормила клуб кексами?"
    "Сайори говорила, что по каким-то особым случаям..."
    show natsuki cm oe
    mc "Стих очень хороший, с каждым разом всё лучше и лучше."
    show natsuki neut cm oe
    mc "Но у меня есть один вопрос."
    show natsuki curi om oe ldown rdown
    n "Какой?"
    show natsuki cm oe
    mc "Ты пишешь, что кормишь клуб кексами."
    show natsuki neut cm oe
    mc "Когда это...{w}именно происходит?"
    show natsuki om oe
    n "Когда как, не каждый день же."
    show natsuki cm oe
    mc "В основном по официальным и личным праздникам?"
    show natsuki om oe
    n "Иногда."
    show natsuki e1b
    n "Когда удаётся что-то испечь дома."
    show natsuki doub cm oe
    mc "Папа тебе это разрешает?"
    show natsuki doub om oe
    n "Естественно, да."
    show natsuki neut cm oe
    mc "Я почему-то думал, что он над тобой все гайки закрутил."
    show natsuki om oe
    n "Нет, ему самому кексы нравятся."
    show natsuki lhip rhip
    n "Их первоначально мама готовила, она меня этому научила."
    n "А одна манга укрепила моё увлечение, дав несколько интересных рецептов."
    show natsuki cm oe
    mc "Прикольно."
    mc "Продолжай поддерживать этот талант."
    show natsuki sedu cm oe
    mc "Кто знает, может, в будущем станешь каким-нибудь популярным японским кондитером, ха."
    show natsuki cross ff sedu om ce
    n "Мои кексы будут самыми лучшими в мире!"
    show natsuki cm
    mc "Ох, ладно, возвращаю, а то ты ещё бизнес-план по захвату мира выпечки придумаешь."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    pause 1.0
    show natsuki happ cm oe
    mc "Пойду, «добью» обмен."
    n "Угу."
    show natsuki e1b

    scene black with wipeleft_scene
    "Осталась лишь Юри."
    "Сейчас она одна стоит и пялится в свой стих."
    "Самое время..."

    scene bg club_day
    show yuri turned happ cm oe at t11
    with wipeleft_scene
    show yuri om oe
    y "И снова здравствуй, Макс."
    show yuri cm oe
    mc "Говоришь так, будто мы сегодня никогда не виделись."
    show yuri om oe
    y "Кстати, видел стихотворение Моники?"
    show yuri cm oe
    mc "Да, оно очень классное."
    show yuri om ce lup rup
    y "Не то слово!"
    show yuri oe rdown
    y "Мне нравится, как она передала в нём свои внутренние переживания."
    show yuri cm ldown
    mc "Хм."
    mc "А прошлые стихи?"
    show yuri om oe
    y "Они тоже хорошие, но конкретно этот вызвал у меня наибольший резонанс."
    show yuri cm oe
    mc "...да, соглашусь."
    show yuri om ce
    y "Интересно, какой будет твой?"
    show yuri neut cm e1d
    mc "О-о-о, нет, Юри, не возлагай большие надежды."
    show yuri om
    y "Мне будет интересно почитать в любом случае."
    show yuri lsur om e1d
    y "Ты же ведь старался, не так ли?"
    y "Значит, как минимум ты заслуживаешь внимания со стороны."
    show yuri cm
    mc "Как знать..."
    show yuri happ om oe
    y "Можно?"
    show yuri cm oe
    mc "Да, конечно."
    call window_close

    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0
    show yuri e1b
    pause 9.0
    show yuri happ om ce rup

    call window_open
    y "Вижу, стиль Нацуки дался тебе очень легко."
    show yuri e1b rdown
    y "Он достаточно простой, но слишком поверхностный."
    show yuri cm
    mc "Я уже заметил."
    show yuri flus om oe rup
    y "Конечно, для новичков он является наилучшим выбором, однако нельзя на нём заостряться."
    show yuri rdown
    y "Данный стиль сковывает полёт фантазии и выражение внутреннего мира писателя."
    y "И, как следствие, заложенную идею самого стиха."
    show yuri cm e1d
    mc "Ты, конечно, права, Юри, но не слишком ли критично относишься к этому?"
    mc "Просто из всего клуба только ты заядлая писательница, а Нацуки всего лишь любитель, у которого совершенно другие увлечения."
    show yuri om oe
    y "Ну...{w}я знаю..."
    show yuri e1d
    y "Но мне всё равно неприятно наблюдать за подобным простоем, когда можно было бы реализовать весь потенциал."
    show yuri cm
    mc "Каждому своё."
    show yuri lsur cm oe
    mc "Главное, чтобы ты свой реализовала."
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    show yuri om oe
    y "Спасибо..."
    show yuri cm oe
    mc "За что?"
    show yuri om oe
    y "За заботу?..."
    show yuri cm oe
    mc "Хм, но это просто факт."
    show yuri om e2b
    y "Даже так..."
    show yuri neut cm e1d
    mc "Ладно, давай твой почитаю, время не резиновое."
    show yuri lsur om oe lup rup
    y "Ох, держи!"
    show yuri happ cm ce
    call show_poem(poem_y4)
    "Любит же она всё завуалировать..."
    "Хотя этот стих, как и прошлый, стало проще читать."
    "И почему-то...{w}я здесь увидел лесенку...{w}или это у меня уже писательский бзик..."
    mc "Красиво написано."
    show yuri om oe
    y "Спасибо..."
    show yuri cm oe ldown rdown
    mc "..."
    y "..."
    "Ну и что я ещё скажу?"
    show yuri neut cm e1d
    mc "Хотелось бы что-то ещё сказать, но слова в голову не лезут..."
    show yuri om
    y "Тогда не стоит выжимать их из себя, Макс."
    show yuri happ om oe lup
    y "Мне достаточно того, что ты получил удовольствие от чтения."
    show yuri cm
    mc "...о, ладно..."
    show yuri ldown
    mc "Возвращаю."
    play sound paper_torn_out
    pause 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    mc "Мне понравился стих."
    show yuri om e1b
    y "Ты меня немножко испугал таким поведением, хех..."
    show yuri oe
    y "Думала, уйдёшь снова в себя как при первом обмене."
    show yuri neut om e1d
    y "Кстати, у тебя же тогда это неслучайно было, ведь так?"
    y "Тебе как-нибудь помочь выговориться?"
    show yuri cm
    mc "А-а-а, нет, Юри, спасибо, я в порядке..."
    show yuri happ cm oe
    mc "Спасибо за обмен."

    scene black with wipeleft_scene
    "Нет-нет-нет, не говорите мне, что это знаки внимания Юри..."
    "Не хватало, чтобы кто-то такой хрупкий влюбился в нестабильного и бестолкового меня."
    "А если я не приму эту любовь с её стороны?"
    "Лицо Юри при отказе на её признание представили?"
    "Она и так с душевной травмой, а тут это сверху добавится."
    "Так и до летального исхода недалеко..."
    "Стоп, Макс, хватит таких мыслей!" with vpunch
    "Успокойся, хорош нервничать..."
    "Надо поскорее вернуться домой и сбросить напряжение через музыку."
    "Но сначала сдам стихи и спрошу Сайори, пойдёт ли она вместе со мной."

    scene bg school literature_club board day
    show monika forward happ cm oe at t11
    with wipeleft_scene
    mc "Моника, вот, бери."
    play sound paper_torn_out
    pause 1.0
    show monika om ce
    m "Спасибо большое."
    show monika cm oe
    mc "Я так понимаю, ты свяжешься со мной, чтобы обсудить время и место встречи?"
    show monika om oe
    m "Безусловно."
    show monika lpoint
    m "Думаю, это можно будет устроить завтра, даже с утра."
    show monika cm oe ldown
    mc "Так рано?"
    show monika om oe
    m "Нет, где-то к часам 10 или 11."
    show monika cm oe
    mc "Хорошо, пойдет, напишешь мне потом."
    show monika neut cm oe
    mc "Полагаю, обмен завершён?"
    m "Хм?"
    stop music fadeout 6.0
    show monika om oe lpoint
    m "Нет, Макс, Юри и Нацуки ещё не обменялись."
    show monika happ om oe ldown
    m "Подождём их и тогда закончим."
    show monika cm oe
    mc "Окей, как скажешь."

    scene black with wipeleft_scene
    "Блеск."
    "Почему задержка происходит именно тогда, когда я хочу поскорее свалить домой?"
    "Не из разряда \"Ы-ы-ы, НаДаЕлО, ХаЧу ДаМоЙ\", а потому что чрезмерно напряжён."

    scene bg club_day
    show yuri turned dist cm oe lup_item poem_paper at t21
    show natsuki turned anno cm ce lup poem_paper at t22
    with wipeleft_scene
    "Что-то они тоже не в духе..."
    "Почему?"
    "Были же в нормальном состоянии."
    show natsuki om ce
    n "{size=15}Опять твои слова с перекрученным смыслом...{/size}"
    show yuri e1a
    n "{size=15}Нельзя писать попроще, а?{/size}"
    show natsuki cm ce
    y "М-м?"
    show yuri om
    show natsuki neut cm oe
    y "Ты что-то сказала, Нацуки?"
    show yuri cm
    show natsuki curi om oe
    n "А?"
    show natsuki dist om oe
    n "Нет, просто мысли вслух."
    show yuri neut cm e1d
    show natsuki neut om oe
    n "Пожалуй, можно сказать, что твой стих вышёл довольно...{w}изящным."
    show yuri happ om oe rup
    show natsuki cm oe
    y "Ох, спасибо..."
    show yuri cm oe rdown
    play sound paper_torn_out
    show natsuki ldown with dissolve
    pause 1.0
    show yuri om oe
    y "Я тоже закончила чтение."
    show yuri cm oe
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    show yuri om oe
    y "Поэтому от себя скажу, что он..."
    show yuri e1b lup rup at s21
    show natsuki angr cm oe
    y "...милый..."
    show yuri neut cm e1d
    show natsuki om oe
    play music t7 fadein 3.0
    n "Милый?"
    show yuri ldown rdown at t21
    show natsuki lhip rhip
    n "Ты хоть понимаешь, что готовка кексов -- ничерта не мило?"
    show natsuki om ce
    n "Это одна морока, которую невозможно назвать «милой»!"
    show yuri flus md e1d
    show natsuki cross vang om ce
    n "Кто вообще придумал это тупое слово?"
    n "Звучит отвратительно!"
    show yuri om
    show natsuki cm ce
    y "Я-я это поняла!"
    show yuri oe lup rup
    show natsuki neut cm oe b1d
    y "Просто..."
    show yuri cm at s21
    show natsuki turned -b1d
    y "...может, некорректно выразилась..."
    show yuri om e1d
    show natsuki angr cm oe
    y "...возможно, милое не то, о чём твой стих, а именно стихотворный слог, тому подобное..."
    show yuri cm
    show natsuki om oe lhip rhip
    n "А с каких пор МОЙ СТИЛЬ можно охарактеризовать таким детским и дурацким словом?"
    show natsuki cm oe
    "Иронично, но в её стиле есть что-то такое..."
    show yuri om at t21
    y "Т-ты неправильно трактуешь смысл..."
    show yuri cm
    show natsuki cross doub om ce
    n "Да?!"
    show natsuki oe
    n "У него есть другое значение?"
    show yuri om
    show natsuki cm
    y "Положительное!"
    show yuri vsur cm oe at s21
    show natsuki turned angr om ce lhip rhip
    n "Да мне плевать, что ты там у себя в голове подумала, «милый» имеет одно-единственное значение и никаких больше!"
    show yuri angr om oe ldown rdown at t21
    show natsuki cm ce
    y "Вообще, знаешь что?"
    show natsuki vang cm oe ldown rdown
    y "Твой стиль только так и можно охарактеризовать!"
    show yuri cm oe
    show natsuki om oe at h22
    n "ЧЕГО?!"
    show natsuki cm oe
    "Охренеть..."
    "Мне это не нравится."
    "Если они не угомонятся, то мне придётся встрять между ними, даже если понадобится наорать."
    show yuri om oe
    y "Повторить для глухих?"
    show yuri cm oe
    show natsuki om oe
    n "Издеваешься?!"
    show yuri om ce
    show natsuki cm oe
    y "Нацуки, уже столько времени прошло, а ты совершенно не выросла в написании стихов."
    show yuri anno om ce
    y "Я постоянно модернизирую свой стиль, тем самым привнося в него новое дыхание и просторы для творчества..."
    show yuri angr om ce
    y "...а ты всё такая же закостенелая дурочка, которая не делает ровным счётом НИЧЕГО, чтобы стать ЛУЧШЕ!"
    show yuri om oe
    y "Не пора ли вырасти?"
    show yuri cm oe
    show natsuki cross om ce
    n "Нихрена себе, важная, вся из себя отважная!"
    show natsuki angr om oe
    n "Я нашла СВОЙ стиль и НЕ СОБИРАЮСЬ его менять, потому что у меня к нему душа лежит!"
    n "К тому же Макс похвалил меня и отметил, что с каждым разом выходит всё лучше и лучше!"
    show yuri dist om ce
    show natsuki cm oe
    y "Макс и мои стихи оценивает положительно, прошу заметить."
    show yuri oe
    y "В первый раз он был даже поражён, в хорошем смысле этого слова..."
    show yuri neut cm e1d
    show natsuki turned sedu om ce lhip rhip
    n "О, правда?"
    show yuri vsur cm oe
    show natsuki om oe
    n "А не потому ли, что ты постоянно пытаешься его впечатлить, Юри?"
    show yuri shoc om oe lup rup at s21
    show natsuki cm oe
    y "Э-э-э?!"
    show yuri mk
    show natsuki om ce
    n "И не у тебя ли недавно сиськи волшебным образом выросли на один размер благодаря новому чёрному бюстгальтеру?"
    show natsuki cm
    "Значит, она реально на меня запала..."
    show yuri vsur om ce
    y "Это...{w}нет, я никогда..."
    show yuri vang om oe ldown rdown at t21
    show natsuki doub cm oe
    y "А может, ты просто завидуешь, что Макс проводит со мной время?"
    show yuri mj
    show natsuki om oe
    n "С чего вдруг?"
    show yuri vang cm oe
    n "Разве я похожа на ту, которая так мечтает о душевном и физическом контакте с ним?"
    show yuri ce
    show natsuki cm oe
    y "МГХ!"
    show yuri oe
    show natsuki sedu om oe
    n "Напомнить, что было сегодня на одной из перемен?"
    show yuri om oe
    show natsuki cm oe
    y "М-молчи!"
    show yuri cm oe
    "Зря я вступил в этот клуб..."
    "Быть яблоком раздора (без своего же ведома) совершенно не хочется."
    show yuri ce
    m "Д-девочки...{w}хватит, успокойтесь..."
    show natsuki om oe
    n "Что, язык проглотила?"
    show natsuki cm oe
    s "Ребята, давайте жить дружно!"
    show yuri om oe at h21
    show natsuki vang om oe at h22
    ny "Заткнитесь и не мешайте!!!" with vpunch
    show yuri cm oe at thide
    hide yuri
    show natsuki cm oe at thide
    hide natsuki
    pause 0.2
    show monika forward lsur om oe at t21
    show sayori turned vsur cm oe at t22
    m "Надо что-то делать!"
    show monika cm oe
    show sayori om ce lup rup at h22
    s "Макс, прошу, успокой их!"
    show sayori cm ce
    mc "Подождите...{w}сейчас..."
    "Их взаимное подливание масла в огонь начинает бесить..."
    stop music fadeout 3.0

    scene black with dissolve
    pause 0.25
    y "Ты постоянно мне мешаешь!"
    y "Сегодня, например, я тебе уже говорила, что ты всё своим приколом испортила!"
    y "Уже начинаю сомневаться в дружбе с тобой!"
    n "Знаешь, что?!"
    n "Да, я тоже думаю, что ошиблась с выбором подруги!"
    "Как же...{w}бесит..."
    $ quick_menu = False

    show bg club_day
    show yuri turned vang mj oe at t21
    show natsuki turned vang cm oe lhip rhip at t22
    with dissolve
    play music t7a
    queue music t7g
    show yuri om oe
    y "{cps=50}Зачем я вообще трачу на тебя время?!{/cps}{w=2.0}{nw}"
    show yuri mj oe
    show natsuki om oe
    n "{cps=50}А я откуда знаю?!{/cps}{w=2.0}{nw}"
    show natsuki ce
    n "{cps=50}Хотя, может, потому что ты мямля!{/cps}{w=2.0}{nw}"
    show yuri om oe
    show natsuki cm oe ldown rdown
    y "{cps=50}Ты всего лишь мелкая засранка, которая выставляет меня в дурном свете!{/cps}{w=2.0}{nw}"
    show yuri mj oe
    show natsuki om oe
    n "{cps=50}Да ты совсем крышей поехала, ходячая сисяндра?!{/cps}{w=2.0}{nw}"
    show layer master at heartbeat(1.5, 0, 1.0)
    show yuri om oe
    show natsuki cm oe
    y "{cps=50}ТЫ КАК МЕНЯ НАЗВАЛА?!{/cps}{w=1.0}{nw}"
    show yuri cm oe
    show natsuki om ce lhip rhip
    n "{cps=50}А что, неправда?!{/cps}{w=1.0}{nw}"
    n "{cps=50}Я же говорила, у тебя грудь на размер увеличилась!{/cps}{w=1.0}{nw}"
    show yuri ce
    show natsuki cm ce
    y "{cps=50}КХ-Х-Х-Х-Х!!!{/cps}{w=1.0}{nw}"
    mc "{cps=50}Заткнитесь.{/cps}{w=1.0}{nw}"
    show natsuki om oe
    n "{cps=50}Ты проиграла, Юри, смирись уже!{/cps}{w=1.0}{nw}"
    show yuri om oe
    show natsuki cm oe ldown rdown
    y "{cps=50}Проиграть такой соплячке, как ты?!{/cps}{w=1.0}{nw}"
    show yuri cm oe
    show natsuki om oe
    n "{cps=50}Я тебе сейчас дам, нахрен!{/cps}{w=1.0}{nw}"
    show yuri om oe
    show natsuki cm oe
    y "{cps=50}Что ты сможешь мне дать?!{/cps}{w=0.5}{nw}"
    y "{cps=50}По жопе?!{/cps}{w=0.5}{nw}"
    show yuri cm oe
    show natsuki om oe
    if persistent.censorship:
        n "{cps=50}Достаточно, чтобы утихомирить такую гадину, как ты!{/cps}{w=0.49}{nw}"
    else:
        n "{cps=50}Достаточно, чтобы утихомирить такую тварь, как ты!{/cps}{w=0.5}{nw}"
    show yuri yand cm oe
    show natsuki cm oe
    mc "{cps=50}Заткнитесь!{/cps}{w=0.5}{nw}"
    show yuri om oe
    if persistent.censorship:
        y "{cps=50}{sc=3}АХ ТЫ ЗАРАЗА!{/sc}{/cps}{w=0.47}{nw}"
    else:
        y "{cps=50}{sc=3}АХ ТЫ СУКА!{/sc}{/cps}{w=0.5}{nw}"
    show yuri cm oe
    "{cps=50}{sc=3}БЕСИТ!{/sc}{/cps}{w=0.5}{nw}"
    show natsuki om oe
    n "{cps=50}{sc=3}САМА НАЧАЛА И САМА ЖЕ НА МЕНЯ НАЕХАЛА!{/sc}{/cps}{w=0.5}{nw}"
    show yuri om oe
    show natsuki cm oe
    y "{cps=50}{sc=3}НА ТАКУЮ НАДОЕДЛИВУЮ МРАЗЬ МОГУ, А-ХА-ХА!{/sc}{/cps}{w=0.5}{nw}"
    show yuri cm oe
    "{cps=50}{sc=3}БЕСИТ-БЕСИТ-БЕСИТ-БЕСИТ-БЕСИТ--{/sc}{/cps}{w=0.5}{nw}"
    window hide

    show layer master
    show noise zorder 5:
        alpha 0
        linear 4 alpha 0.4

    show yuri om oe
    show natsuki lhip rhip
    pause 0.5
    show yuri cm oe
    show natsuki om oe
    pause 0.5
    show yuri om ce
    show natsuki cm oe
    pause 0.5
    show yuri cm ce
    show natsuki om ce
    pause 0.5
    show yuri om oe
    show natsuki cross cm ce
    pause 0.5
    show yuri cm oe
    show natsuki om ce
    pause 0.5
    show yuri om ce
    show natsuki turned cm oe lhip rhip
    pause 0.5
    show yuri vang cm oe
    show natsuki yand om oe
    pause 0.5
    show yuri om oe
    show natsuki cm oe

    window auto
    "{sc=3}ПОЧЕМУ ТАК ТЯЖЕЛО ЗАТКНУТЬСЯ?!{/sc}"
    show yuri cm ce
    show natsuki cross om oe
    "{sc=3}ПОЧЕМУ НАДО ДРУГ ДРУГА ПРОВОЦИРОВАТЬ?!{/sc}"
    show yuri om ce
    show natsuki vang cm oe
    "{sc=3}ПОЧЕМУ?!{/sc}"
    show yuri cm oe at thide
    hide yuri
    show natsuki om oe at thide
    hide natsuki
    pause 0.2
    show monika forward neut cm e0b at t41
    show sayori turned neut cm e0b lclose rclose at t21
    pause 0.2
    show sayori om
    s "Макс?..."
    show monika om
    show sayori cm
    m "Сайори..."
    show monika cm at thide
    hide monika
    show sayori at thide
    hide sayori
    pause 0.3
    m "Зажми уши и закрой глазки..."
    s "Мне страшно, Моника!"
    show yuri turned vang cm oe at t21
    show natsuki turned vang om oe lhip rhip at t22
    n "Макс!"
    n "Она края потеряла, угомони её!"
    show yuri om oe
    show natsuki cm oe
    y "{sc=3}Я?!{/sc}"
    show yuri yand om oe
    if persistent.censorship:
        y "{sc=3}СКАЗАЛА МЕРЗАВКА СО СВОИМ СЛОВОМ «МИЛЫЙ»!{/sc}"
    else:
        y "{sc=3}СКАЗАЛА СУЧКА СО СВОИМ СЛОВОМ «МИЛЫЙ»!{/sc}"
    show natsuki pani cm oe ldown rdown
    y "{sc=3}ДА ВСЕМ ПЛЕВАТЬ, ЧТО У ТЕБЯ СДВИГИ В БАШКЕ\nИЗ-ЗА ОТЦА-ПОЛУДУРКА!{/sc}"
    show yuri cm oe
    show natsuki om ce
    n "Т-ты!..."
    stop music
    play music_none_loop music_stop
    hide noise
    show yuri pani om oe lup rup at h21
    show natsuki cm ce at h22
    mc "{sc=3}МОЛЧА-А-А-А-А-А-А-А-АТЬ!!!{/sc}" with vpunch
    window hide

    pause 2.0
    show yuri cm oe
    show natsuki pout cm oe
    pause 0.5
    show yuri vsur cm oe

    $ nightmare_active = True

    call window_open
    if persistent.censorship:
        mc "Наконец-то, блин, тишина!"
    else:
        mc "Наконец-то, блять, тишина!"
    show yuri lup rup at s21
    mc "Какого хрена вы здесь устроили, а?!"
    mc "Почему нельзя взять и прийти к компромиссу?!"
    mc "Почему надо постоянно самоутверждаться за счёт друг друга и бояться признать за собой ошибки, считая это за слабость?!"
    y "..."
    n "..."
    show yuri om
    y "...что с тобой...{w}Макс?..."
    show yuri cm
    show natsuki om ce
    n "...ты меня напугал!"
    show yuri angr cm oe
    show natsuki cm
    "...что?"
    "Они мои слова услышали?..."
    show yuri ce ldown rdown at t21
    show natsuki oe
    y "Кхм..."
    show yuri om oe
    y "Нет, он вовсе не напугал."
    show yuri cm
    show natsuki angr om oe lhip rhip
    n "Говорю как есть!"
    show yuri vang om oe
    show natsuki cm
    y "НАЦУКИ!" with vpunch
    y "Даже я осознаю, что всё это глубокий перебор!"
    y "Извинись перед всем клубом за своё поведение!"
    show yuri cm
    show natsuki om
    n "Что?"
    n "Значит, мои слова не такая уж и ложь?"
    show natsuki ce
    n "И вообще, это говорит мне ТОТ, КТО только что оскорблял меня благими матами за ни за что!"
    show yuri ce
    show natsuki cm
    y "Кх-х-х..."
    show natsuki anno om ce ldown rdown
    n "Пф-ф-ф..."
    show natsuki cm
    "Провал."
    "Моя агрессия растаяла на глазах..."
    "Я что, боюсь перегнуть палку?"
    show yuri angr cm oe
    mc "Давайте теперь тоже самое, только на чистую и холодную голову."
    show natsuki neut cm oe b1d
    mc "Причины вашей ненависти друг к другу?"
    show yuri om ce lup rup
    y "Я просто хочу от Нацуки одного."
    show yuri oe
    show natsuki doub cm oe -b1d
    y "Отнесись к стихам серьёзней."
    show yuri ldown rdown
    show natsuki om lhip rhip
    n "Кх, как можно серьёзно относиться к такой ерунде?"
    show yuri om
    show natsuki cm
    y "Ерунде?--{nw}"
    show yuri cm
    show natsuki angr om oe
    n "А знаешь, что я от тебя хочу?"
    show yuri vsur cm oe
    show natsuki vang om oe
    n "Я хочу от тебя внимания!"
    n "Чтобы ты перестала меня игнорировать и начала проводить время со мной!"
    show natsuki cross vang om oe
    n "А ты забила себе всю голову отношениями!"
    show yuri me
    show natsuki cm
    y "Э..."
    show natsuki turned vang om ce
    n "Хватит с меня этого."
    show natsuki oe
    n "Пойду к себе домой...{w}одна."
    show yuri sad cm oe
    show natsuki cm ce at thide
    hide natsuki
    mc "С-стой, Нацуки!"
    mc "Мы только начали решать ваши распри!"
    mc "Побудь с нами ещё, чтобы закрыть их раз и навсегда!"
    show natsuki turned fs neut cm oe at t22
    pause 0.2
    show yuri ce
    show natsuki om
    n "...отстань от меня."
    n "Ты ничего об этом не знаешь."
    show natsuki ff angr om oe lhip rhip
    n "Я не обязана выслушивать ваши фальшивые доводы по этому поводу!"
    show yuri lsur cm oe
    show natsuki e2b b1d ldown rdown
    n "Вы вообще здесь лишние!"
    show natsuki oe -b1d
    n "А ты всего лишь новичок, который не прожил здесь и недели!"
    show natsuki ce
    show yuri pout cm oe
    n "Посторонний!"
    show yuri om
    show natsuki vang cm oe
    y "Ложь."
    y "Если бы он был посторонним, он не старался бы проводить с нами время и помогать, когда есть такая возможность."
    show yuri cm
    show natsuki cross vang om oe
    n "...ну и что с того, что он уделял время?"
    show yuri neut cm e1d
    n "Мне нужен тот клуб, который был изначально!"
    show yuri nerv cm oe n2
    show natsuki ce
    n "Без перевозбуждённой Юри, которая из кожи вон лезет, как бы произвести на Макса впечатление."
    show yuri ce
    n "Без чрезмерно «правильного» лидерства Моники, которая стала закручивать гайки со стихами, тоже уделяя особое внимание Максу."
    show natsuki oe
    n "Тут только Сайори не изменилась!"
    show natsuki ce
    n "Не знаю, хорошо это или плохо..."
    show natsuki cm
    m "Нацуки, пожалуйста, хватит..."
    show yuri cry cm e1a
    mc "Вот именно, хватит."
    show yuri om
    show natsuki oe
    y "Нацуки..."
    y "Извинись."
    show yuri cm
    show natsuki turned vang cm oe
    n "Н..."
    show natsuki om
    n "Не надо тут надумывать лишнего из-за моих слов!"
    show natsuki ce
    n "Вы сами себя так ведёте!"
    n "И если вы серьёзно считаете, что всё прекрасно идёт своим чередом, то очень зря!"
    show natsuki cm
    call window_close

    show sayori turned cry md b1d lclosefist rclosefist zorder 2 at l43
    pause 0.5
    show yuri vsur mk oe lup rup at h21
    show sayori lup rdown
    show natsuki pani om ce n2 at h22
    play sound slap
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 1.0
    show sayori lclose rclose at t11
    show natsuki cm oe

    call window_open
    "...А-А-А?"
    show sayori mh
    s "{sc=0.5}Нацуки...{/sc}"
    show yuri ldown rdown
    show natsuki pout cm e1g
    s "{sc=0.5}Ты сама...{w}ведёшь себя не лучше..."
    show sayori lclosefist rclosefist
    s "{sc=0.5}Ты разрушаешь клуб...{/sc}"
    s "{sc=0.5}Извинись...{/sc}"
    show sayori md
    n "{sc=0.5}...хах...{/sc}"
    show natsuki e4d
    n "{sc=0.5}...угх...{/sc}"
    call window_close

    show natsuki e1g zorder 3 at t43
    pause 0.5
    show yuri e4c lup rup at h21
    show sayori cm e4c -b1d lup rup n2 at h11
    show natsuki pani cm ce lup
    play sound slap
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 1.0
    show yuri oe
    show natsuki ldown at t22

    call window_open
    s "{sc=0.5}...у-ум-м!...{/sc}"
    show sayori ldown rdown
    show natsuki oe
    hide sayori with easeoutleft
    m "Сайори?!"
    m "Дай посмотрю!"
    show yuri cm ldown rdown
    show natsuki ce
    if persistent.censorship:
        mc "Так, нахрен!" with vpunch
    else:
        mc "Так, блять!" with vpunch
    n "Н-н..."
    show natsuki pout cm e1g
    mc "Либо ты извиняешься за своё поведение, либо проваливаешь отсюда к чёрту!"
    mc "Выбирай."
    show natsuki e4d
    n "...угх..."
    show yuri worr om ce
    y "Признайся ты уже."
    show yuri cm
    n "...кх-х..."
    show yuri cry cm e1a
    show natsuki mg
    n "{sc=0.5}Всё ясно...{/sc}"
    n "{sc=1}Вы выбрали его вместо меня.{/sc}"
    show natsuki fs cry om e2 b1 n4
    n "{sc=1}Ладно.{/sc}"
    show natsuki om ce -b1
    n "{sc=2}Тогда я ухожу отсюда!{/sc}"
    show yuri worr cm oe
    show natsuki cm
    m "Нацуки, опомнись!"
    show natsuki om oe
    n "{sc=2}Я уже с момента прихода Макса об этом\nдумала!{/sc}"
    show natsuki ce
    n "{sc=2}Это место только меня разрушает!{/sc}"
    show yuri ce
    show natsuki cm
    show sayori turned cry cm oe zorder 2 at l41
    pause 0.5
    show sayori om
    s "{sc=2}Нацуки!!!{/sc}"
    s "{sc=2}Не расстраивай весь клуб окончательно!{/sc}"
    s "{sc=2}Не надо так!{/sc}"
    show sayori cm
    show natsuki turned ff cry om e1h b1e lhip rhip
    n "{sc=2}Хватит говорить от лица клуба, будто всем тут\nбудет грустно от моего ухода!{/sc}"
    show yuri e1a
    show natsuki cm
    m "Нацуки, перестань рубить с плеча!"
    show natsuki ldown rdown -b1e
    m "Конечно, ты виновата в этом конфликте, но это не значит, что мы тебя ненавидим!"
    show natsuki om
    n "{sc=2}Виновата?{/sc}"
    show natsuki fs cry om ce
    n "{sc=2}...да всё ясно: я вас всех достала, вот и ухожу!{/sc}"
    play music t9
    show sayori e1h
    show yuri oe
    n "{sc=2}Сайонара!{/sc}"
    show natsuki cm at thide
    hide natsuki
    m "Нет же, подумай!"
    show yuri e1a
    show sayori om at t11
    s "{sc=3}НА-ЦУ-КИ-И-И!!!{/sc}"
    show sayori cm e4e
    hide sayori with easeoutleft
    show yuri ce
    mc "Сайори, стой!"
    m "Сайори!..."
    show monika forward sad om e4d at t22
    m "У-у-у, ну бли-и-ин!..."
    m "Ну почему всё так?!"
    show monika cm
    mc "Тихо, Моника, успокойся..."
    show yuri e1a
    show monika om e1g
    m "Не могу, Макс!"
    m "Нацуки -- часть нас!"
    m "Мы не можем её бросить!"
    m "Сайори только что из-за этого убежала!"
    show monika e4d
    m "И я толком ничего не сделала, чтобы это предотвратить!"
    show yuri om
    show monika cm
    y "П-простите...{w}я опять не сдержалась..."
    show yuri oe lup
    y "Постараюсь...{w}завтра поговорить с Нацуки..."
    show yuri cm e1a ldown
    show monika om e1g
    m "Пожалуйста, Юри!"
    m "Ты должна её вразумить!"
    show monika e4d
    m "И мы должны исправиться..."
    show yuri om
    show monika cm
    y "Хорошо...{w}я пойду..."
    show yuri cm oe at thide
    hide yuri
    pause 0.2
    show monika om
    m "У-у-у..."

    scene black with dissolve
    pause 0.25
    "Нужно побежать за Сайори или нет?!"
    "Так, у неё дома есть мать."
    "А ещё её захватила буря эмоций, которая не спала, -- значит, нет смысла сейчас что-то с ней делать: я всё только усугублю и испорчу..."
    "С Нацуки отец, а Юри вроде бы отпустило..."
    "Значит, Моника!"
    "Нужно её успокоить, чтобы ей стало легче..."
    m "Я знала, что что-то такое произойдёт, я знала..."
    mc "Моника, ты в этом не виновата."
    mc "Ты здесь больше всех работаешь и стараешься."
    mc "Не знаю, благодарил тебя кто-то за твой труд или нет, но большое тебе спасибо."
    m "Этого мало, Макс..."
    m "Видишь, что произошло?"
    m "Я мало работала."
    m "Я не уследила за состоянием участников..."
    m "Я не предотвратила конфликт..."
    m "Я.{w} Плохой.{w} Лидер..."
    "Так, поглаживание по голове..."
    mc "Моника, не впадай в уныние!"
    mc "Ты же не робот: не можешь за всем сразу уследить и всё проконтролировать."
    mc "Ты живой человек, который и так много чего делает для нас."
    mc "И я хочу, чтобы ты не угасала, а продолжала вкладывать силы в клуб и в нас."
    mc "А мы тебе обязательно потом отплатим..."
    "...вот только как?"
    m "......"
    "Обняла?..."
    "Я чувствую её дыхание и сердцебиение..."
    "...однако я сказал всего лишь обычные слова, что тут такого?"
    stop music fadeout 6.0
    m "Макс...{w}я устала..."
    m "Мне нужно восстановиться..."
    mc "Проводить тебя до дома?"
    m "...если ты не против..."
    mc "Конечно нет."
    mc "Пойдём, заодно развеешься на свежем воздухе."
    m "Хорошо, сейчас..."
    stop noise_1 fadeout 2.0
    call window_close

    $ nightmare_active = False

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 10 afternoon
    show monika forward dist cm oe school_bag at t11
    with wipeleft_scene
    show monika om
    m "Ф-ф-ф..."
    show monika pout om ce
    m "Фу-у-у..."
    show monika cm
    "Ну и задница у нас на ровном месте образовалась..."
    show monika md
    "Скорее, мыльный пузырь раздулся и лопнул."
    show monika neut cm oe
    mc "Получше стало?"
    show monika om e1b
    m "Да, немного отлегло..."
    show monika cm
    "Чёрт, надо было мне быть увереннее, а не стоять тупым столбом."
    "Хотя...{w}если бы я додавил тогда свой всплеск агрессии...{w}то тогда бы виноват был я, а ситуация бы не поменялась."
    show monika oe
    "Ну и проблема Нацуки точно не решилась."
    "Всё стало бы ещё хуже."
    show monika flus cm e1a
    "Но разве не было хоть какого-нибудь способа это предотвратить?"
    show monika om
    m "Нам нужно что-то с этим делать, Макс."
    show monika cm
    mc "Знаю..."
    show monika neut cm oe
    mc "К Сайори завтра по-любому наведаюсь."
    show monika mh lpoint
    m "Нет, надо сначала разобраться с Нацуки, иначе в этом не будет никакого смысла."
    show monika flus om oe ldown
    m "Она должна извиниться перед Сайори."
    show monika cm
    mc "Ну, да..."
    show monika neut cm oe
    mc "Но ты мне лучше другое скажи: неужели она настолько одинокая?"
    show monika dist cm oe
    mc "Ладно я ещё, с одной лишь Сайори общаюсь, но она?"
    show monika om
    m "Как видишь..."
    show monika neut om oe lpoint
    m "Кстати, я же тебе недорассказала про неё..."
    show monika cm ldown
    mc "Что именно?"
    show monika om
    m "...помимо семейных проблем у Нацуки была ещё одна: её иногда донимали одноклассники."
    show monika dist om oe
    m "Пик их издевательств пришёлся на начальный период средней школы."
    show monika ce
    m "Благо сами «издевательства» не были серьёзными."
    show monika neut cm oe
    mc "Что-то из разряда \"её вещь спрятали под другую парту, дёрганья за волосы, обзываловки\" и прочее дерьмо, на которое способен тупой малолетний ученик?"
    show monika dist om oe
    m "Да, что-то примерно такое..."
    show monika cm
    mc "А сейчас как?"
    show monika neut om oe
    m "К счастью, пошло на спад."
    show monika lpoint
    m "Можно сказать спасибо защитному механизму Нацуки в виде агрессии."
    show monika flus om oe ldown
    m "Но даже сейчас могут проскакивать такие эпизоды..."
    show monika neut om oe
    m "Коротко говоря, они стали редкие, но меткие."
    show monika cm
    mc "Насколько меткие?"
    show monika om lpoint
    m "К примеру, этой зимой в декабре она подралась с одним учеником."
    show monika ldown
    m "Подробностей не помню, но зато помню фингал на её правом глазу."
    show monika cm
    mc "Фига себе..."
    show monika om ce
    m "Ей тогда Юри помогла отделаться от этого ученика."
    show monika oe
    m "Так что вот так."
    show monika lpoint
    m "Единственное, что меня радует, так это то, что за Нацуки впряглась сама Рэ{image=accent_low_register}{space=-15}йко-сан."
    show monika cm ldown
    mc "Кто такая Рэйко-сан?"
    show monika om
    m "Ты её видел в понедельник."
    show monika cm
    mc "...?"
    show monika curi om oe
    m "Ну помнишь, меня позвала одна девушка, когда мы тебя с Сайори в клуб вели?"
    show monika cm
    mc "А, так это она была?"
    show monika happ cm oe
    mc "Глава школьного совета?"
    show monika om
    m "Правильно."
    show monika neut cm oe
    mc "А чем Нацуки её зацепила?"
    show monika dist om oe
    m "Рэйко в курсе её проблемы, возможно, поэтому..."
    show monika ce
    m "Да и сама Нацуки часто попадала в мелкие передряги, с которыми разбиралась Рэйко."
    show monika neut om oe lpoint
    m "Потому что если некое нарушение школьного устава выходит за рамки, в которых действуют полномочия дежурных, этим занимается глава школьного совета."
    show monika cm ldown
    mc "Ясненько..."
    mc "Она Рэйко не достала подобными случаями?"
    show monika om
    m "Во-первых, виновата всё-таки не она, а во-вторых, не знаю..."
    m "Даже если и да, то Рэйко осознаёт всю ситуацию вокруг Нацуки."
    show monika cm
    mc "Понятно."

    scene bg niigata street suburban 11 afternoon
    show monika forward neut cm e1c school_bag at t11
    with wipeleft_scene
    show monika oe
    mc "Как я понял, Нацуки просто хотела внимания, потому что одна."
    show monika worr om oe
    m "Да, а мы..."
    show monika ce
    m "Мы как-то не думали, что она этого хочет."
    show monika cm
    mc "С другой стороны, понять её можно."
    show monika neut cm oe
    mc "Главная подруга плавно, но быстро перестаёт с ней общаться из-за того, что..."
    show monika happ om ce
    m "Влюбилась в тебя, да, ха-ха?"
    show monika cm
    mc "...мда."
    "Где-то я это уже видел..."
    show monika om oe
    m "Да ладно тебе, Макс, важно то, что именно Юри её услышала."
    show monika lpoint
    m "Очень надеюсь, что она разберётся с ней во всех нюансах, а уже через неё мы вернём Нацуки в строй."
    show monika cm ldown
    mc "Доверяй, но проверяй."
    show monika om
    m "Посмотрим, как будет завтра."
    show monika cm

    scene bg niigata street suburban 15 day
    show monika forward neut cm e1b school_bag at t11
    with wipeleft_scene
    show monika happ cm oe
    mc "Не хватало мне ещё влюблённости со стороны в такой период, вот честно."
    show monika lean happ om oe school_bag at h11
    m "Хах, волнуешься?"
    show monika cm oe
    mc "Нет."
    show monika forward neut cm oe school_bag
    mc "Я серьёзно."
    mc "Мне это только проблемы в жизни прибавит в геометрической прогрессии."
    show monika om
    m "Я бы не сказала, что Юри такая уж сложная для тебя девушка."
    show monika happ om oe
    m "Скрытая -- да, но очень хорошая."
    show monika cm
    mc "Моника..."
    show monika ce
    mc "Не надо меня сватать."
    hide monika
    show monika lean happ cm oe school_bag at e22
    with dissolve_cg
    show monika om
    m "Тем более она уже очень взрослая."
    show monika ce
    m "За такую девушку парни друг друга убить готовы!"
    show monika cm
    mc "Моника!"
    hide monika
    show monika lean happ cm ce school_bag at i11
    with dissolve_cg
    show monika om
    m "Ха-ха-ха!"
    show monika cm
    mc "Я рад за её половозрелость и красоту, но..."
    show monika oe
    mc "...да как сказать-то..."
    show monika forward neut cm oe school_bag
    mc "...я не готов брать такую ответственность на себя, особенно когда у меня нет материальной основы и финансовой подушки."
    mc "И когда я психологически не готов."
    show monika b1b
    mc "Всё это закончится плачевно."
    show monika mh
    m "Ты слишком на себя накручиваешь, Макс."
    show monika happ om oe -b1b lpoint
    m "Другие бы не раздумывали и сразу согласились с ней встречаться."
    show monika neut cm oe ldown
    mc "Ага, сегодня они встречаются, завтра перепихиваются, а дальше что?"
    mc "Это тебе не смазливая романтическая новелла, где выбрал чей-то рут, то есть персонажа, и дошёл с ним до счастливого конца."
    show monika b1b
    mc "Любовь -- это выбор человека, с которым ты свяжешь свою жизнь."
    show monika om
    m "Любовь -- это в первую очередь чувство к кому-то, а уже потом выбор."
    show monika e1b
    m "К слову, я заметила, что ты не даёшь волю эмоциям, что плохо."
    show monika cm oe -b1b
    mc "Предлагаешь мне стать эмоциональным истериком?"
    show monika om
    m "Нет, просто ты слишком сильно их сдерживаешь."
    m "Это бьёт по нервной системе, потому что они копятся внутри тебя."
    show monika dist om ce
    m "И в один прекрасный момент эти чувства болезненно и некотролируемо вырвутся наружу."
    show monika cm
    mc "Я пока не ощущал в себе такого."
    show monika flus om e1a
    m "Макс, рано или поздно это может произойти."
    show monika oe
    m "Если бы рядом с тобой была любимая девушка, которая тебя поддерживает, то ты бы гарантированно избежал этого."
    m "По крайней мере, она бы значительно сгладила всю боль..."
    show monika cm
    mc "...гхм..."
    show monika neut cm oe
    mc "Моника, но ведь ты забываешь, через какие тернии надо пройти, чтобы добиться такого человека."
    mc "А если этот человек ещё отвергнет?"
    show monika anno cm oe
    mc "Или ещё какая-нибудь хрень произойдёт?"
    show monika om
    m "Макс."
    m "Ты просто боишься любви."
    show monika neut mh oe
    m "Но в этом нет ничего страшного."
    show monika cm
    mc "Да не любви я боюсь..."
    mc "А проблем, которая она может принести, даже несмотря на то, что я, ответственный человек, готов их решать."
    show monika om
    m "Но боишься."
    show monika cm
    mc "Хватит с меня этих мнимых розовых облаков, которых может и не быть после невероятно трудного и избитого пути."
    mc "Ты мне сейчас психолога напоминаешь, с которым я общался несколько лет назад по мессенджеру."
    show monika flus cm e1a
    mc "Он мне тоже понавесил подобной лапши на уши, надеясь на хороший исход, а в итоге всё скатилось вот в это дерьмо, стоящее перед тобой."
    show monika om ce
    m "Макс..."
    show monika e1a
    m "Тебе просто не хватает человека, на которого ты можешь положиться."
    show monika lpoint
    m "Положиться не только в делах, но и в чувствах."
    show monika cm ldown
    mc "Может, и так."
    mc "И что с того?"
    mc "Что мне с этим делать, Моника?"
    show monika om oe
    m "Не знаю, честно..."
    show monika e1a
    m "Я бы сказала не побояться сделать первый шаг навстречу Юри, но ты это отвергнешь..."
    show monika cm
    mc "Отвергну."
    mc "Уже говорил, почему."
    show monika oe

    scene bg niigata street suburban 16 day
    show monika forward neut cm e1b school_bag at t11
    with wipeleft_scene
    show monika om oe
    m "А если это будет кто-то другой?"
    show monika cm
    mc "Другой?..."
    show monika happ cm oe
    mc "И кто?"
    show monika om ce
    m "А это я уже не могу сказать, хах."
    show monika cm
    mc "М-м..."
    show monika neut cm oe
    mc "Думаю, ничего бы не поменялось."
    show monika e1b
    m "Хм..."
    show monika oe
    mc "И вообще, почему ты без парня?"
    show monika nerv cm oe
    mc "Или он у тебя есть?"
    show monika mb ce at s11
    m "Ха-ха..."
    show monika om
    m "Так вышло, что у меня никого не было..."
    show monika happ cm oe at t11
    mc "Пф-ф-ф, не верю, что у такой девушки с лидерским характером и красивой фигурой не было парней."
    show monika lean happ om oe school_bag at h11
    m "Льстишь, Макс!"
    show monika cm
    mc "Неа."
    show monika forward happ cm oe school_bag
    mc "Это даже странно."
    show monika om e1b
    m "Думаю, я просто их не замечала, если они проявляли знаки внимания..."
    show monika oe
    m "Всё равно их проблема, надо быть увереннее в своих намерениях."
    show monika cm
    mc "Верно..."
    show monika neut om oe lpoint
    m "Хотя нет, вру: было пару человек, которые хотели завести со мной отношения, но..."
    show monika happ om e1b ldown
    m "Ни один из них мне не подходил."
    show monika cm
    mc "То есть не понравились."
    show monika nerv mb oe
    m "...да, но это ужасно звучит..."
    show monika cm
    mc "Но ведь это нормально."
    show monika neut cm oe
    mc "Мне тоже много кто не нравится."
    show monika om e1c
    m "Ну, так-то да..."
    show monika cm

    scene bg monika house outside day
    show monika forward neut cm ce school_bag at t11
    with wipeleft_scene
    show monika om
    m "В общем, за свою жизнь я не встретила того человека, с кем была бы готова связать свои узы."
    show monika happ cm oe
    mc "Вот это ты поэтично выразилась, конечно..."
    show monika om ce
    m "Хах."
    show monika neut om oe
    m "Хотя, знаешь..."
    show monika happ cm oe
    mc "Что, такой человек уже нашёлся, да?"
    show monika lean happ om oe school_bag at h11
    m "...думаю, да~"
    show monika cm
    mc "И кто же, если можно поинтересоваться?"
    show monika forward happ om oe lpoint rhip school_bag
    m "А это уже моя личная жизнь."
    show monika ce ldown rdown
    m "Должна же быть у каждой девушки нотка таинственности, состоящая из секретов."
    show monika cm
    mc "Хорошо, не лезу."
    show monika oe
    mc "Кстати, сзади тебя...{w}{b}это{/b} твой дом?"
    show monika om
    m "Он самый."
    show monika nerv cm oe
    mc "Вот это охренительная резиденция?!"
    show monika mb
    m "Ты слегка преувеличиваешь..."
    show monika cm
    mc "Ну-ну."
    mc "Мой дом тебе в подмётки не годится."
    show monika happ om ce
    m "Главное, что я на одном психическом уровне с тобой, ведь так?"
    show monika cm
    mc "Да, конечно..."
    show monika oe
    mc "Так, ещё раз, ты мне завтра напишешь, куда мне подходить и во сколько, верно?"
    show monika om lpoint
    m "Лучше сам напиши, как проснёшься."
    show monika ldown
    m "Я встану пораньше, буду сразу на связи."
    m "Проверю твой стиль вместе с тобой."
    show monika cm
    mc "Понял."
    show monika om
    m "Как придёшь, обсудим твой стиль и дальнейшие действия."
    show monika cm
    mc "Да-да."
    mc "Ладно."
    mc "До завтра?"
    show monika om ce
    m "До завтра, Макс."
    show monika cm
    mc "Надеюсь, на этом \"завтра\" всё уже вернётся на круги своя."
    show monika lean happ om oe school_bag at h11
    m "Мы же Литературный клуб!"
    show monika ce
    m "Все держимся друг за друга, что бы ни произошло."
    show monika cm
    mc "Ага..."
    call window_close

    show monika forward happ cm ce school_bag
    pause 0.5
    show monika at thide
    hide monika
    pause 1.0

    call window_open
    scene black with wipeleft_scene
    mc "Ух-х-х..."
    "Что-то я находился..."
    "А ещё до дома надо дойти..."
    "..."
    "ТАК, СТОП!" with vpunch
    "Я же тут тоже не был!"
    "А прошли мы совсем не малый отрезок пути!"
    mc "А-а-а-а-а..."
    "Где мои спасительные карты в телефоне..."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "..."
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 20,
            description = "Потрясающе. Я невольно стал яблоком раздора для Литературного клуба, из-за чего он сегодня \"развалился\". Нацуки взбесилась тем, что Юри забила на неё из-за влюблённости в меня. А уход Нацуки ударил по Сайори. Это какой-то полный кабздец... Завтра с Моникой начнём восстанавливать состав клуба до прежнего состояния."
        )

        current_day = (20, _("ПТ"))

    python in phone.system:
        battery_level = 49
        clock = (20, 7)

    show screen phone_calendars() with Dissolve(0.5)
    $ plot_pause()

    window auto
    mc "Уже 8 часов вечера?"
    window hide

    hide screen phone_calendars with Dissolve(0.5)

    window auto
    mc "Чё-ё-ёрт...."
    "Еле-еле всё закончил..."
    "Меня ещё почему-то сваливает с ног в самом прямом смысле..."
    "Да, я утомился и нанервничался, но не до такой же степени."
    "Будто пробежал марафон в 30 километров и готов сдохнуть."
    "Ноги, руки, да все мышцы -- всё ослабло."
    "Всё приходится делать через силу."
    "Нет, надо срочно лечь."
    "Не могу больше ни стоять, ни сидеть, ни двигаться вообще."

    scene black with dissolve
    play sound hugs
    pause 1.0
    mc "Уф-ф-ф..."
    "Лучше не стало..."
    "Такую слабость я ощущал только при ознобе, когда серьёзно болел."
    "Что со мной происходит?"
    "И почему у меня бодрый мозг при таком убитом теле?"
    "Как же ломит, блин..."
    window hide

    pause 3.0

    window auto
    "Как же хорошо, что завтра выходной..."
    "Я бы умер, если бы это был рабочий день."
    window hide

    pause 3.0

    window auto
    "Да в задницу этот выходной!"
    "Нам нужно восстановить клуб..."
    "МНЕ нужно вернуть Сайори в прежнее состояние."
    "Я не могу быть спокойным, когда она там дома лежит и убивается."
    "А я знаю, что она убивается."
    "Потому что я знаю её характер и отношение к этому клубу."
    "Меня гложет только та мысль, что Сайори дома не одна."
    "Её мама, уверен, уже заботится о ней."
    "Но боюсь, что этого недостаточно..."
    "..."
    "...а если бы Сайори жила одна, как я сейчас?"
    "Что бы..."
    "...не-е-ет..."
    "...я не хочу об этом думать..."
    "В жопу такие мысли..."
    "..."
    "......"
    "И ведь всё равно лезут в голову!"
    mc "Мозг, скотина, слышишь меня?"
    mc "Иди нахрен со своими дурными мыслями!"
    mc "Достал меня."
    mc "Нет, чтоб подумать о чём-то приятном..."
    "..."
    "Да у меня уже думать сил нет..."
    "И пошевелиться не могу..."
    "И рот будто склеился..."
    "..."
    "Всё..."
    "Надо спать..."
    "Надо спать......"
    call window_close

    call nightmare_act_1_day_5
    $ _history_list.clear()

    $ nightmare_active = True

    call window_open
    scene bg bedroom at mc_bed
    show dark:
        align (0.5, 0.5) zoom 1.25
    mc "{sc=3}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А--{/sc}{nw}" with shake(time=2.0)
    mc "{sc=1}--а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а-а...{/sc}{nw}"
    mc "{sc=0.5}......{/sc}"
    mc "..."
    mc "Это..."
    play music mc_after_nightmare
    mc "Это был сон?..."
    mc "Это РЕАЛЬНО был сон?"
    mc "Сто-о-оп."
    mc "Стоп-стоп-стоп..."
    "Как {b}это{/b} могло быть сном?"
    "Я только что {b}чувствовал{/b} всё до мельчайших деталей!"
    "Сайори {b}висела{/b}!"
    "Она была...{w}{b}холодной{/b}!"
    "У неё {b}не было пульса{/b}!"
    "Меня {b}рвало{/b}!"
    "Мне было {b}больно{/b}!"
    "..."
    "Но если {b}это сон{/b}, то почему я здесь?"
    "Ночью?"
    "В своей пижаме из шорт и футболки!"
    mc "КАК?!"
    "Подождите..."
    "Комната Сайори была полнейшим бардаком, а этого быть не может..."
    "Она никогда не запускала свою комнату до такого состояния."
    "А ещё календарь был странный, как я заметил слева краем глаза..."
    "Почему он был перечёркан красным маркером?"
    "И порван снизу!"
    "Сайори ни за что бы так не сделала со своими вещами, даже если это календарь!"
    "Так всё-таки {b}это{/b} был сон или нет?!"
    mc "Да твою ж ты мать!"
    "Мне надо снова прийти к Сайори!"
    "Мне надо убедиться, что это был {b}сон{/b} и что она {b}жива{/b}!"
    mc "Сколько времени?!"
    call window_close

    scene bg bedroom
    show dark
    with dissolve
    pause 2.0
    play sound light_turning_on
    hide dark
    show white:
        alpha 1
        linear 0.25 alpha 0
    pause 1.0

    call window_open
    show layer master at stress
    mc "3 ночи?!"
    if persistent.censorship:
        mc "{sc=3}ДА ПЛЕВАТЬ!!!{/sc}" with vpunch
    else:
        mc "{sc=3}ДА НАСРАТЬ!!!{/sc}" with vpunch
    "Мне ВАЖНА жизнь Сайори!"
    call window_close

    scene black with dissolve
    pause 0.2
    play noise_1 mc_steps_house_run
    pause 4.0
    stop noise_1

    scene bg mc house hallway night
    show layer master at stress
    with dissolve
    pause 1.0
    play sound light_turning_on
    scene white
    scene bg mc house hallway night light with dissolve
    pause 1.0
    call window_open
    mc "{sc=2}Где грёбаная ветровка?!{/sc}"
    mc "{sc=2}...{/sc}"
    mc "{sc=2}Вот!{/sc}"
    mc "{sc=2}Пф-ф-ф...{/sc}"
    mc "{sc=2}Застёгивайся, скотина!{/sc}"
    play sound clothes_zipping
    pause 3.0
    mc "{sc=3}ЕСТЬ!{/sc}"
    call window_close

    scene black with dissolve
    pause 0.2
    play sound house_door_open
    pause 1.227
    play noise_1 mc_steps_outside
    pause 2.0
    stop noise_1
    play sound house_door_close
    pause 2.0
    play noise_1 mc_steps_outside_jogging
    pause 4.5
    stop noise_1

    scene bg sayori house outside night
    show dark zorder 2:
        alpha 0.5
    show layer master at stress
    with dissolve_scene_full
    pause 1.5
    play sound doorbell_sayori
    pause 4.0

    call window_open
    "..."
    call window_close

    pause 0.6
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 1.0
    play sound doorbell_sayori
    pause 4.0

    call window_open
    show sayori_mom home_clothes shoc cm oe s_anno_cm_oe at t11
    sm "У-у-у-ум-м-м-м..."
    show sayori_mom om rhip -s_anno_cm_oe
    sm "Макс?"
    sm "Что случи--{nw}"
    show sayori_mom cm
    mc "Сайори..."
    show sayori_mom rdown
    mc "Она дома?"
    mc "С ней всё в порядке?"
    stop music fadeout 3.0
    show layer master
    show sayori_mom curi om e1a lpoint
    sm "Д-да, она спит."
    show sayori_mom worr om oe ldown
    sm "Вчера, правда, была подавленной, что-то плохое произошло..."
    show sayori_mom cm
    mc "Фу-у-ух..."
    show sayori_mom curi cm e1a
    "Всё в порядке!"
    show sayori_mom om
    sm "Макс, что случилось?"
    show sayori_mom cm
    mc "Всё в порядке..."
    show sayori_mom pani ml oe
    sm "Ты весь бледный!"
    show sayori_mom mj
    mc "Всё нормально."
    mc "Извините за беспокойство..."
    show sayori_mom curi cm e1a
    mc "Завтра обязательно навещу Сайори, как раз по поводу её состояния."
    mc "Так что не переживайте на этот счёт..."
    show sayori_mom om
    sm "Хорошо..."
    show sayori_mom cm
    mc "Я пойду...{w}спать..."

    scene black with wipeleft_scene
    "Это был...{w}всего лишь кошмар..."
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "Уже 4 часа утра, а я всё ещё не могу прийти в себя..."
    "Не могу взять, успокоиться и уснуть."
    mc "Это ненормально!"
    "Что со мной произошло?"
    "С чего вдруг мне приснился кошмар?"
    "В моей жизни были и более стрессовые ситуации, чем срач Нацуки, -- вариант с причиной кошмара в дневных переживаниях откидывается..."
    "..."
    mc "Чёрт..."
    "...неужели мой психотип дал трещину и стал разваливаться?"
    "Когда-то давно мне психолог об этом писал."
    "Точнее так: если не получать позитивные эмоции и «не работать с пациентом», то развитие психотипа чревато расстройствами психики."
    "И, как следствие, сильным личностным кризисом..."
    mc "Ха...{w}ха-ха..."
    "Можно меня поздравить: у меня это началось."
    "..."
    "Ну не может {b}это{/b} быть просто вон из ряда выходящим случаем!"
    "Настолько подробных снов за всю мою бестолковую жизнь у меня никогда не было!"
    mc "Как же...{w}плохо..."
    "Глаза слегка плывут..."
    "Я реально не могу уснуть."
    "Я сбился и потерял настрой."
    "И при этом измотан донельзя..."
    "..."
    "Тетрадь..."
    "..."
    "Может...{w}написать стих...{w}об {b}этом{/b}?"
    "Может, так я успокоюсь?"
    "..."
    "У меня нет других вариантов."
    "Если это мне не поможет, то я не знаю, что делать."
    "Мой организм разваливается на глазах."
    "..."
    "Что ж, ручка в руке..."

    call poem_act_1_day_5

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc5, music=False)
    mc "Я...{w}не хочу это комментировать..."
    "Я чувствую, как моё сердце стало тяжелее биться."
    "Началась ещё большая слабость в мышцах рук и ног..."
    "Может, теперь...{w}отрубиться на кровати?..."
    "Только вырубить свет...{w}и дойти до неё..."
    "Меня покидают силы..."
    call window_close

    $ nightmare_active = False

    return
