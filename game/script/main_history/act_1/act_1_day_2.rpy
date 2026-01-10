
label act_1_day_2:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d1.unlocked == False:
        $ ach_a1_d1.unlock()

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
    mc "{cps=20}Ф-ф-ф...{/cps}"
    "Радовался вчера, что не был разбитым?"
    "Теперь меня плющит по классике."
    "Абсолютно любой внешний раздражитель сейчас воспринимается в штыки."
    "Вроде бы уснул не поздно, по адекватному распорядку дня..."
    "Но нет, организму всё мало сна, ещё тянет спать."
    mc "Ах-х-х..."
    "Вставай, давай."
    "Ежедневная рутина ждёт."
    "Эх, если бы такие моменты можно было пропустить по щелчку пальцев..."
    "К примеру, просто..."
    play sound fingers_snap
    mc "Раз!{w=0.5}{nw}"
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "Так, ключи, мобильник..."
    mc "Всё на месте."
    "Сколько бы ни занимался перепроверкой вещей, всё равно кажется, что что-то забыл."
    "Но это лишь обычное сомнение в готовности перед выходом."
    "Ведь так?"
    "Я же точно ничего не забыл?..."
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
    "Кучевые облака..."
    "Сегодня передали, что внезапно прибудет короткий, но мощный ливень."
    "Снова сюда очередную тучу заносит, снова всё высохнет за считанные часы..."
    "Нет, я понимаю, что Ниигата находится чуть выше центра Японии, но, может, хватит?"
    "Сезон дождей всегда был в первой половине лета."
    "А сейчас разгар весны!"
    "Природа, что с тобой происходит?"
    s "{size=19}Ура, ты вышел!{/size}"
    play music sayori_happy fadein 3.0
    show sayori turned happ cm ce school_bag at l11
    pause 0.5
    show sayori tap pout om oe school_bag at s11
    s "Я уже тебя заждалась!"
    show sayori neut cm oe
    mc "Ха, ты прислушалась к моему совету?"
    show sayori turned happ cm ce lup rup school_bag at h11
    s "Угусь~"
    show sayori om oe ldown rdown
    s "У меня появилось в запасе целых 15 минут!"
    show sayori cm
    "Вот это я понимаю, оптимизация..."
    show sayori om lup
    s "Поэтому, покончив с делами, я сразу пришла к тебе."
    show sayori dist om oe ldown
    s "Думала, что мы успеем с тобой прогуляться где-нибудь..."
    show sayori tap angr om oe school_bag at s11
    s "А ты у нас соня!"
    show sayori cm oe
    mc "Если б я таким был, ты бы меня вообще не дождалась."
    show sayori pout om oe
    s "Все эти 15 минут ушли на ожидание тебя, мф-ф-ф..."
    show sayori cm
    mc "Я бы раньше не встал, потому что я не батарейка модели «Сайори»."
    show sayori turned laug om ce school_bag at t11
    s "Хе-хе-хе!"
    show sayori happ om oe
    s "Кстати, ты же ведь не забыл стих?"
    show sayori cm oe
    mc "Шутишь?"
    mc "Я не для того вчера потратил больше получаса, чтобы просто взять и забыть этот...{w}«шедевер»."
    show sayori om ce lup rup at h11
    s "Мне не терпится прочитать, что у тебя получилось!"
    show sayori cm ce ldown rdown
    mc "Откуда такое рвение?"
    show sayori om oe
    s "Мне же интересно, какие таланты могут быть скрыты в моём друге!"
    show sayori curi om oe lup
    s "Вдруг ты будущий поэт?"
    show sayori cm oe
    call window_close
    play sound flashback_start
    pause 0.2
    stop noise_3
    $ renpy.music.set_volume(0.2, 0, "music")

    scene white
    scene black with dissolve
    scene bg bedroom
    show gray zorder 3:
        alpha 0.25
    show vignette zorder 4:
        alpha 0.5
    with dissolve
    call window_open
    "Ну и фуфло."
    "Нет, к чёрту, я не буду это переписывать."
    call window_close
    play sound flashback_end
    pause 0.575
    $ renpy.music.set_volume(1.0, 0, "music")

    scene white
    scene black with dissolve
    play noise_1 street_suburban_noise fadein 1.0
    scene bg residential_day
    show sayori turned curi cm oe school_bag at i11
    with dissolve
    call window_open
    "{color=#fc7e23}Bruh{/color}."
    show sayori neut cm oe
    mc "Ты слишком преувеличиваешь, Сайори..."
    show sayori sad om oe
    s "Но ведь всё может быть!"
    show sayori cm oe
    mc "Не в моём случае."
    "Так, нет, слишком пессимистично выходит, надо сменить тему разговора."
    show sayori neut cm oe
    mc "Ты тоже стих сочинила, да?"
    show sayori happ om ce lup rup at h11
    s "Конечно!"
    show sayori nerv om oe ldown rdown at s11
    s "Было трудновато..."
    show sayori happ om ce at t11
    s "...но я справилась!"
    show sayori cm ce
    mc "Молодец, ты заслужила поглаживание."
    call window_close

    hide sayori
    show sayori turned happ cm ce school_bag at e11
    with dissolve
    pause 2.0
    show sayori nerv cm ce n3 with dissolve
    pause 2.0
    hide sayori
    show sayori turned nerv cm ce n3 school_bag at i11
    with dissolve
    pause 0.5

    call window_open
    mc "Всё, нам пора, пойдём."
    show sayori happ om ce n1 lup rup at h11
    s "Ок-ке!"
    show sayori cm ce ldown rdown at t11

    scene bg niigata street suburban 10 day
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori neut cm oe
    mc "Сайори, вы же раньше писали стихи, верно?"
    mc "Выходит, у тебя уже набита рука?"
    show sayori om oe
    s "Ну..."
    stop music fadeout 3.0
    show sayori dist om oe
    s "Да, но я будто совсем не развиваюсь в этом."
    show sayori cm
    "О как..."
    mc "С чего это вдруг?"
    show sayori om
    s "Не знаю."
    show sayori worr om ce
    s "Я не могу это объяснить."
    show sayori cm
    mc "Может, ты просто этого не замечаешь?"
    show sayori neut cm oe
    mc "В любом деле, если ты в нём работаешь, ты всегда становишься лучше."
    mc "Даже если эти действия кажутся довольно однотипными."
    show sayori e1c
    s "Хм..."
    show sayori oe
    mc "Как минимум я уверен, что такой человек, как ты, не может быть в простое."
    show sayori laug cm ce
    mc "Большое количество энергии в одном место не даст соврать, а?"
    show sayori om
    s "Ха-ха-ха!"
    show sayori cm
    "Ей уже получше, отлично."
    show sayori happ cm ce
    "Но этот её редкий, но меткий пессимизм мне совершенно не нравится."
    show sayori e1b
    "Бывало уже пару таких случаев за всё время общения, благо я их выворачивал на что-то позитивное..."

    scene bg school gate 1
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    "Эх, снова этот вход..."
    show sayori om oe
    s "Расходимся."
    s "Встретимся в клубе, Макс!"
    show sayori cm oe
    mc "Хорошо."
    show sayori cm ce at thide
    hide sayori
    pause 1.0
    "Надеюсь, не заблужусь в старом корпусе..."
    "Клуб-то на втором этаже, а туда попасть пока можно только либо через первый, либо через третий, как мы выяснили опытным путём."
    "Везде сплошной ремонт..."
    "Сколько можно?"
    "У нас что, всемирный месяц сверления мозгов?"
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("s")

    call window_open
    "Что-то мне...{w}нехорошо..."
    "Голова кружится..."
    "Когда уже урок закончится..."
    call window_close

    pause 2.0
    play noise_1 school_corridor_light_noise fadein 5.0 volume 0.5
    play sound school_bell
    pause 12.0

    call window_open
    s "Ух-х..."
    "Наконец-то..."
    "Надо...{w}доползти до крыши..."
    "Там тишина и свежий воздух..."
    stop noise_1 fadeout 1.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 wind fadein 3.0
    scene bg school new_rooftop 1 day with wipeleft_scene
    s "Пх-х-х..."
    "Мне стало жарковато по пути..."
    "Я заболела?"
    "Нет, не думаю..."
    "Просто утомилась..."
    "Посижу тут немного и пойду..."
    window hide

    pause 7.0

    window auto
    "Ну не-е-ет!"
    "Даже сейчас мне лезут противные мысли в голову."
    "Хватит..."
    "Я хочу отдохнуть."
    window hide

    pause 4.0

    window auto
    "Ну не рассказывала я Максу про клуб, и что?"
    "Я точно знаю, что он бы скепти...{w}спепчечи...{w}чески к нему отнёсся."
    "А сейчас он не отказался вступить в него, потому что...{w}Моника."
    "Не знаю, что она смогла такого сделать, чтобы привлечь его внимание."
    s "{size=19}У-у-у...{/size}"
    "Она...{w}стройнее и красивее, да..."
    "У неё голос приятнее."
    "Всё приятнее!"
    s "{size=19}Точно.{/size}"
    s "{size=19}Я поняла.{/size}"
    s "{size=19}Она его в себя влюбила!{/size}"
    "Вот и весь секрет."
    "Это я просто никому не нужная дурочка, поэтому ничего и не выходит..."
    "..."
    s "{size=19}Какая я бестолковая и бесполезная...{/size}"
    s "{size=19}А ещё некрасивая...{/size}"
    "Ни фигуры, ни голоса, ни хорошего характера..."
    "У меня даже стихи писать нормально не получается!"
    "Да, не так давно мы их начали, где-то...{w}ближе к концу осени?"
    "За всё это время я как писала отсебятину, так и пишу до сих пор."
    "Что пришло в голову, так и легло..."
    "Но ради кого стараться?"
    "Ради клуба?"
    "Я...{w}да нет у меня сил на такое..."
    "Каждый стих...{w}это просто мой плевок эмоциями на бумагу."
    "Мне они не нравятся, хоть они и светло-грустные."
    "Я будто...{w}скапливаю в себе эту жидкость из эмоций...{w}точнее, она сама скапливается...{w}и всё скапливается...{w}почему скапливается?"
    "Ведь в детстве я всегда была радостной, ничего такого не было."
    "А может, потому что я привыкла быть весёлой?"
    "Но это же глупо."
    "У меня совершенно нет сил разбираться во всём этом..."
    "Я чувствую себя слабой..."
    "...и при этом слабость вызывается чем-то внутри...{w}в животе...{w}или в голове..."
    s "{size=19}Кх-х-х...{/size}"
    s "{size=19}Какой же я вице-президент Литературного клуба?{/size}"
    s "{size=19}Дурочка, которая даже в себе разобраться не может...{/size}"
    s "{size=19}Вот кто я...{/size}"
    s "{sc=0.5}С-слышите?{/sc}"
    s "{sc=1}Вот!...{/sc}"
    "{sc=1}...{w}ком в горле!{/sc}"
    s "{sc=1}......{/sc}"
    "{sc=1}Как же...{w}больно...{/sc}"
    s "{sc=1.5}Я!{/sc}"
    s "{sc=1}КХА!{/sc}"

    scene black with dissolve
    pause 0.25
    "{sc=1}Мой кадык...{w}колет...{/sc}"
    "{sc=1}Слёзы наворачиваются...{/sc}"
    "{sc=1}Я не хочу плакать...{w}но они текут...{w}противно...{/sc}"
    "{sc=1}Ничего не могу с этим сделать...{/sc}"
    s "{sc=0.5}Ничего не могу...{/sc}"
    window hide

    pause 5.0

    window auto
    play music sayori_my_confession_piano
    m "{size=19}Сайори?{/size}"
    s "Мо...{w}ни?..."
    "У меня нет сил даже открыть глаза..."
    m "У тебя лицо заплаканное!"
    m "Что случилось?"
    s "Я..."
    "Показать истинные чувства?..."
    "...зависть Монике?"
    "Свою слабость?!"
    "Разве ЭТО истинные чувства?!"
    s "...уже всё забыла."
    "Честно же...{w}моя голова устала..."
    m "Так быстро?"
    s "Ну..."
    "Ей так это интересно?..."
    m "Хорошо, не буду тебя теребить."
    s "..."
    m "..."
    s "Почему...{w}ты всё ещё здесь?"
    "..."
    "Села вплотную ко мне..."
    m "Как я могу бросить свою подругу в таком состоянии?"
    s "..."
    s "...я лишь сейчас...{w}обуза для тебя..."
    m "Э?"
    m "Почему?"
    s "Потому что я...{w}слаба..."
    "Зачем...{w}зачем я это говорю?..."
    m "Сайори?"
    s "Вот истинная я..."
    m "Нет-нет, ошибаешься."
    m "Ты не можешь быть такой в силу всей тебя: начиная от внешности и заканчивая душой."
    s "Душа?..."
    m "Душа."
    m "У тебя очень хорошая и светлая душа, Сайори."
    m "Но знаешь, что мне не нравится в твоём случае?"
    s "...что?"
    m "Ты слишком мало получаешь взамен за свои старания."
    m "И даже готова отказаться от этого малого в угоду другим."
    m "Мне никогда это в тебе не нравилось с самого начала, потому что ты заслуживаешь большего."
    s "...я даже не знаю, что это..."
    m "И это очень плохо."
    m "Все видят твой позитивный настрой, заряжаются им по полной..."
    m "Но мало кто благодарит тебя за это или делает что-то хорошее в ответ."
    s "...я ничего не могу с этим поделать..."
    m "Мне очень жаль, Сайори, что тебе приходится переживать подобное и чувствовать из-за этого опустошённость..."
    s "Мне тоже...{w}жаль..."
    m "Но всё, что я могу сделать -- это посоветовать быть собой."
    m "Я понимаю, что тебе иногда нравится твоя жизнерадостность, но ты тратишь очень много сил на неё."
    m "А они тебе нужны, Сайори."
    s "..."
    m "Особенно в мире, где большинство людей отнюдь не с добрыми побуждениями."
    s "...нет...{w}не хочу..."
    m "Ох, Сайори..."
    m "Это ради твоего же блага."
    m "Мне самой больновато смотреть на то, как ты угасаешь в такие моменты."
    s "..."
    "Ком в горле...{w}снова..."
    m "...не буду настаивать."
    m "Но подумай над этим, хорошо?"
    s "..."
    m "А сейчас лучше отдохни."
    m "Можешь полежать у меня на плече."
    m "Всё равно я тоже утомилась, пока поднималась по лестнице, ха-ха..."
    s "...угу."
    "..."
    "Приобняла меня..."
    "Стало теплее и спокойнее..."
    "..."
    "У Моники даже кожа мягче и нежнее..."
    "..."
    "Я просто...{w}не могу...{w}перестать быть жизнерадостной..."
    "И если перестану быть...{w}я сломаюсь..."
    m "Ой..."
    m "Кажется, дождь начинается..."
    s "...тучки?"
    m "Тучки с горизонта."
    m "Да ещё какие!"
    m "Там такая муть под ними из-за дождя..."
    s "У..."
    "Тучки..."
    $ currentpos = get_pos(channel="music")
    stop music fadeout 3.0
    m "Ай."
    m "На меня капнуло."
    s "...тоже."
    pause 1.0
    play noise_2 rainfall
    m "{sc=3}А-А-А-А-А!{/sc}"
    s "{sc=3}ЛИВЕНЬ?!{/sc}"
    m "{sc=3}ХА-ХА-ХА!!!{/sc}"
    m "{sc=3}БЫСТРЕЙ ВО ВНУТРЬ!!!{/sc}"
    s "{sc=3}СЕЙЧАС!!!{/sc}"
    m "{sc=3}СУМКУ ПРИКРОЙ!!!{/sc}"
    s "{sc=3}ХОРОШО!!!{/sc}"
    stop noise_1 fadeout 3.0
    stop noise_2 fadeout 3.0
    call window_close

    call window_dialog_long_transition("mc")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    "А вот и очередной конец учебного дня."
    "Благо ливень уже прошёл: боялся, что попаду в него, когда домой пойду."
    "Поэтому кто куда, а я...{w}а-а-а, точно, не домой...{w}теперь в Литературный клуб...{w}позориться своим творением..."
    mc "Тьфу..."
    "Так, оно тут?"
    "Да, на месте..."
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Вижу, клуб уже влияет на тебя положительно."
    show mrs_ida omb ce lup
    mi "Прямо бодрее сегодня стал~"
    show mrs_ida cm
    mc "Э-э-э, возможно..."
    show mrs_ida om ldown
    mi "А ты всё опасался вступать."
    show mrs_ida oe
    mi "О, вижу, уже пробуешь себя в стихах?"
    show mrs_ida cm
    mc "Угу."
    show mrs_ida om lup rhold
    mi "Если не возражаешь, можно посмотреть из любопытства?"
    show mrs_ida cm
    "Этого мне только не хватало!"
    show mrs_ida neut cm oe ldown rdown
    mc "Нет-нет-нет, Ида-сэнсэй, именно ЭТОТ стих, уж извините, я показывать не буду."
    mc "Но если получится что-то качественное, то могу, конечно."
    show mrs_ida om ce
    mi "Ой, ладно, не нервничай, я всё понимаю."
    show mrs_ida happ om oe
    mi "Просто немного разыгралась на эту тему."
    mi "Ведь в твоём возрасте я тоже увлекалась стихотворениями."
    mi "Жанр «хайку» у меня не очень получался, а вот всякие четверостишия -- запросто!"
    show mrs_ida omb ce lup rhold
    mi "Эх, помню, как тогда впервые встретилась со своим мужем в похожем клубе, столько стихотворений друг другу посвятили, хе-хе-хе~"
    show mrs_ida om oe ldown rdown
    mi "Причём писали специально завуалированно, чтобы никто, кроме нас, ничего не понял."
    show mrs_ida cm
    "Теперь понятно, откуда у неё такое желание сбагрить меня в Литературный клуб."
    mc "Простите, Ида-сэнсэй, но мне пора идти, у нас вот-вот должно начаться собрание..."
    show mrs_ida om
    mi "Конечно-конечно."
    show mrs_ida ce
    mi "Некрасиво заставлять девушек ждать встречи с джентельменом~"
    show mrs_ida cm

    scene black with wipeleft_scene
    "Если бы миссис Иду сделали главой по решению демографической проблемы, то график рождаемости в нашей стране извернулся бы по резкой параболе и устремился вверх."
    call window_close

    call plot_transition

    call window_open
    scene bg corridor with wipeleft_scene
    "Итак, я на месте."
    "Дверь..."
    "Как же я не люблю подобные моменты."
    "Вот вроде бы просто надо взять и открыть её."
    "Но светить всем своей туалетной бумажкой, поддерживать разговор и принимать активное участие в клубной деятельности как-то вообще не хочется..."
    "Аргх, чего я думаю?"
    "У меня будто выбор есть?"
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    play music t3 fadein 3.0
    scene bg school literature_club board day with wipeleft_scene
    mc "Здра-а-авствуйте."
    show sayori turned happ om ce lup rup at t22
    s "Ух ты, Макс пришёл!"
    show sayori cm ce ldown rdown
    show yuri turned happ cm oe at l21
    pause 0.7
    show yuri om oe lup rup
    y "О, п-привет, ты всё-таки ответственно подошёл ко вступлению в клуб..."
    show sayori cm oe
    show yuri pout cm oe ldown rdown
    n "{size=19}Ха, да что Вы, что Вы, мы польщены Вашим официальным визитом, господин!{/size}"
    show sayori laug cm oe
    show yuri lsur cm oe
    mc "Я тоже польщён, что подсобка класса счастлива меня видеть в этом месте!"
    n "{size=19}ГРХ!{/size}"
    show sayori cm ce
    show yuri laug om ce lup rup
    y "Ха-ха-ха!"
    show sayori happ cm ce
    show yuri anno om oe at s21
    y "{size=19}Надо взять себе на заметку...{/size}"
    show sayori cm oe
    show yuri cm oe
    mc "Стойте, а где наш президент?"
    show sayori om oe
    s "Моника постоянно слегка задерживается, из-за чего приходит позже всех."
    show sayori ce
    s "А всё потому, что учится играть на рояле!"
    show sayori cm
    show yuri mf e1d
    mc "Рояль?"
    show sayori oe
    show yuri happ om oe ldown rdown at t21
    y "Её семья привила любовь к клавишной музыке, поэтому в свободное время Моника практикуется в музыкальном классе, причём довольно успешно."
    show yuri flus om oe rup lup at s21
    y "Конечно, корректнее сказать, что это классическая музыка, но президент больше любит «современные» композиции..."
    show yuri happ cm oe ldown rdown at t21
    mc "Ну и ну."
    show sayori e1c
    "Значит, Моника у нас умница, музыкант, лидер и просто красавица?"
    show yuri e1b
    "Интересно, как сильно её дрючили воспитанием в детстве?"
    show sayori cm oe
    show yuri e1d
    mc "Как она только не устаёт от стольких дел?"
    show sayori om ce lup rup at h22
    show yuri happ cm ce
    s "Мы её поддерживаем!"
    show sayori cm ce ldown rdown at t22
    "Оно и видно."
    show sayori cm oe
    show yuri cm oe
    mc "Ясненько..."
    mc "Тогда, значит, мы просто ждём Монику, после чего начинаем стихотворную эпопею?"
    show sayori om oe
    s "Да!"
    show sayori cm oe
    show yuri om oe
    y "Можешь пока заняться своими делами."
    show sayori neut cm oe
    show yuri anno om oe
    y "А если их у тебя нет, то...{w}у-у-у..."
    show sayori flus om oe
    show yuri shy happ om oe at s21
    y "...ты любишь читать...{w}книги?"
    show sayori lsur om oe
    show yuri cm oe
    s "Ах, точно, я пока поделаю домашнюю работу, там как раз немного."
    show sayori cm oe
    show yuri neut cm oe
    mc "Да, хорошо."
    show sayori at thide
    hide sayori
    show yuri happ cm oe
    mc "Книги, говоришь?..."
    show yuri turned worr cm oe at t21
    mc "Честно сказать, я не заядлый читатель."
    show yuri curi cm oe lup at t11
    mc "Однако, если попадётся что-то захватывающее и интересное, могу проглотить за раз."
    mc "Но это случается крайне редко."
    mc "Я раньше вообще по визуальным новеллам был, сейчас уже как-то нет желания их проходить."
    show yuri om oe
    y "Визуальные новеллы?..."
    show yuri cm oe ldown
    n "{size=19}Фе, недосимуляторы свиданий и прочий сопливизм...{/size}"
    "Начинаются стереотипы..."
    show yuri happ cm ce
    mc "Промах, Нацуки!"
    mc "Я в такое ни ногой."
    n "{size=19}Кх-х-х...{/size}"
    show yuri om ce
    y "Хе-хе..."
    show yuri cm oe
    mc "Среди новелл тоже много чего интересного есть, если усердно поискать."
    show yuri curi cm oe
    mc "От научной фантастики с петлями времени и тайными организациями до расследования загадочной гибели населения колонизаторского корабля в далёком будущем."
    show yuri lsur om oe lup rup at s11
    y "Ох..."
    show yuri cm oe
    n "{size=19}Хм, где-то про такое я уже слышала...{/size}"
    show yuri ldown rdown at t11
    mc "Долго рассказывать, тем более давно всё проходил..."
    mc "Но, можно сказать, что подобные новеллы тоже своего рода книги, только с анимированной картинкой и звуком."
    show yuri om oe
    y "Это...{w}интересно..."
    show yuri flus om oe
    y "Надо будет посмотреть и попробовать..."
    show yuri cm oe
    mc "Ха, заинтриговал?"
    show yuri happ om ce
    y "Безусловно."
    show yuri cm oe
    mc "Ну ладно, а что насчёт тебя?"
    mc "Ты же ведь про книги не просто так заговорила, верно?"
    show yuri om oe
    y "Да, в последнее время я читаю «Портрет {color=#407fff}Маркова{/color}»."
    show yuri cm oe
    mc "Не слышал о такой."
    show yuri om oe
    y "Если кратко, то там повествуется о старшекласснице, которая переезжает жить к своей младшей сестре."
    show yuri dist om oe
    y "К слову, с ней она давно не общалась..."
    show yuri om ce
    y "Но вскоре после этого её жизнь становится донельзя странной."
    y "Она становится целью заключённых, сбежавших из ближайшей тюрьмы, в которой проводят эксперименты на людях..."
    show yuri anno om ce
    y "И вот, когда её жизнь в опасности, ей приходится выбирать, кому доверять."
    show yuri lsur om ce
    y "Что бы она ни делала, в результате она обрывает почти все свои связи, и её жизнь начинает разваливаться..."
    show yuri anno om oe
    y "И-или нет, не так..."
    show yuri flus cm oe lup rup at s11
    y "У-у-у..."
    show yuri ce
    y "Всё в голове перемешалось, слишком много всего..."
    mc "Ух..."
    "А по Юри и не скажешь, что она читает что-то подобное..."
    "Но, судя по всему, «Портрет {color=#407fff}М-а-р-к-о-в-а{/color}» ей очень нравится."
    show yuri happ cm oe ldown rdown at t11
    mc "Звучит крайне нестандартно."
    mc "А можно глянуть?"
    show yuri nerv om oe
    y "К-конечно, я как раз хотела продолжить чтение и предложить..."
    show yuri shy happ om oe n5 at s11
    y "...тебе тоже...{w}ознакомиться и почитать..."
    show yuri cm oe
    "Вот так сразу?"
    show yuri n1
    mc "Хорошо, но только недолго."
    show yuri turned happ cm ce lup rup at t11
    y "Угу!"
    call window_close
    stop music fadeout 3.0
    scene black with dissolve_scene_full

    pause 3.0
    if cg_a1_d2_y.unlocked == False:
        $ cg_a1_d2_y.unlock()

    scene y_cg1_base with dissolve_cg
    play music t6
    call window_open
    "Мда..."
    "Читать с такого кривого ракурса нифига не удобно."
    "Но смотря на Юри, которая сразу утонула глазами в книге...{w}можно и потерпеть."
    "Просто не хочу нарушать такую хрупкую идилию."
    window hide

    pause 6.0

    window auto
    show y_cg1_exp1 at cgfade
    y "...ты прочитал?"
    mc "А..."
    "Чёрт, я слишком сильно отвлёкся."
    mc "Да, можно переворачивать."
    y "Давай."
    hide y_cg1_exp1
    "Листать страницы тоже неудобно."
    "Сначала рукой надо пнуть лист с моей стороны..."
    play sound page_turn
    pause 1.5
    "...чтобы Юри подхватила и прижала его со своей."
    window hide

    pause 3.0

    window auto
    show y_cg1_exp1 at cgfade
    mc "А почему «Портрет {color=#407fff}Мар-ко-ва{/color}» так называется?"
    hide y_cg1_exp1
    y "Сюжет в ней очень схож с принципом чередования случайных событий, вероятность свершения которых зависит от достигнутых предыдущих."
    y "Этот принцип, иными словами, -- цепь Маркова."
    y "Она была введена русским математиком {color=#407fff}Марковым{/color}-старшим где-то в начале XX века и использовалась им в теории вероятности."
    y "Саму математику я не очень понимаю, тем более высшую, поэтому ничего более подробного сказать не могу."
    mc "Да, интересно..."
    "Кстати, видел это когда-то, но забыл."
    "Да и я тоже не математик, чего уж тут говорить..."
    window hide

    pause 3.0

    window auto
    "Чёрт, солнце так слепит..."
    "И ведь не скажешь, что был ливень."
    "Всё настолько яркое..."
    "Даже волосы Юри на свету приобрели пурпурный оттенок."
    "Хм, они так необычно переливаются..."
    window hide

    pause 4.0

    window auto
    show y_cg1_exp2 at cgfade
    show y_cg1_exp1 at cgfade
    y "Кажется, ты смотришь совсем не в книгу..."
    mc "...а, да?"
    show y_cg1_exp3 at cgfade
    hide y_cg1_exp2
    hide y_cg1_exp1
    y "Я-я тебя понимаю!"
    y "Бывает трудно сконцентрироваться при чтении в одиночку!"
    show y_cg1_exp1 at cgfade
    y "А мы тут сидим вдвоём..."
    hide y_cg1_exp1
    y "И я, возможно, слишком быстро прыгаю глазами по строкам, потому что уже прочитала множество различных книг за всё время..."
    show y_cg1_exp1 at cgfade
    y "И-извини!"
    mc "Ой, нет, не надо извиняться, всё нормально."
    mc "Но ты права, что-то я вообще не могу сосредоточиться..."
    hide y_cg1_exp1
    y "М-мы можем пока остановиться..."
    mc "Да..."

    scene bg club_day
    show yuri turned flus cm oe lup rup at s11
    with dissolve_cg
    "Блин, не хватало, чтобы она чувствовала себя виноватой из-за моей дурости."
    mc "Прости."
    "Так, если тактическое поглаживание с Сайори работает отменно, то и с Юри сработает?"
    show yuri vsur om oe
    y "Н-нет, Макс, что ты!"
    show yuri flus cm ce
    y "Всё норма--{nw}"
    stop music fadeout 3.0
    call window_close

    hide yuri
    show yuri turned flus cm ce lup rup at e11
    with dissolve
    pause 2.0
    show yuri sedu cm ce n3 ldown rdown with dissolve
    pause 2.0
    hide yuri
    show yuri turned sedu cm ce n3 at i11
    with dissolve
    pause 3.0
    play music t3 fadein 3.0

    call window_open
    show yuri shoc om oe lup rup at h11
    y "Э-э-э-э-э?!"
    show yuri cm
    mc "А?"
    show yuri shy happ cm oe n5 at s11
    y "Угх..."
    "Вот это я не ожидал."
    "Она так сильно засмущалась?"
    show natsuki turned neut om oe lhip rhip at t44
    n "Эй, Юри."
    n "Ты покраснела, как помидор."
    show natsuki cm oe
    y "..."
    show natsuki anno om oe
    n "Макс, что ты с ней сделал?"
    show natsuki cm oe
    mc "Всего лишь погладил, избавив от надуманной вины."
    show natsuki curi cm oe ldown rdown
    s "Погладил?!"
    show natsuki happ cm ce
    show sayori turned happ om ce lup rup at l11 zorder 2
    pause 0.7
    s "Я тоже хочу!"
    show sayori cm ce
    mc "Ох, Сайори..."
    call window_close

    hide sayori
    show sayori turned happ cm ce lup rup at e11 zorder 2
    with dissolve
    show natsuki cm oe
    pause 2.0
    show natsuki pout cm oe
    show sayori nerv cm ce n3 ldown rdown with dissolve
    pause 2.0
    hide sayori
    show sayori turned nerv cm ce n3 at i41 zorder 2
    with dissolve
    pause 0.5

    call window_open
    mc "Подзарядка батарейки прошла успешно?"
    show sayori happ om ce lup rup n1 at h41
    s "Да!"
    show yuri angr om oe n1 zorder 2
    show natsuki shoc om oe
    show sayori flus om oe zorder 3
    show monika lean happ om oe zorder 1 at t11
    m "А теперь что насчёт Моники?"
    show yuri turned happ mn ce lup rup zorder 1 at t42
    show natsuki laug cm ce
    show sayori laug cm ce ldown rdown zorder 1
    show monika forward laug cm ce zorder 1 at t43
    mc "Эй-эй-эй, имейте совесть!"
    mc "Я только первый день в клубе, а вы меня используете по-чёрному!"
    show monika happ om ce lpoint zorder 2
    m "Хорошо, тогда за тобой должок."
    show monika cm ce ldown
    mc "..."
    show yuri happ cm oe ldown rdown
    show natsuki happ cm oe
    show sayori happ cm oe
    show monika om oe lpoint rhip
    m "Итак, друзья!"
    show monika om ce
    m "Пора делиться своими стихотворениями!"
    show monika cm oe ldown rdown
    show natsuki cm ce at thide
    hide natsuki
    show yuri cm ce at thide
    hide yuri
    show sayori cm ce
    hide sayori with easeoutleft
    pause 0.5
    show monika at t11
    pause 0.1
    show monika lean happ om oe at h11
    m "Макс, ты же не забыл его написать, верно?"
    show monika cm oe
    mc "Что ж вы все так во мне сомневаетесь..."
    show monika forward happ om ce
    m "Просто хочу удостовериться!"
    show monika cm
    mc "Да-да, он у меня с собой."
    show monika om ce
    m "Очень хорошо!"
    show monika om oe lpoint rhip
    m "Ладно, пока все готовятся, введу тебя в курс дела."
    show monika ldown rdown
    m "Мы разбиваемся на пары, делимся друг с другом стихами, обсуждаем их содержания."
    show monika lpoint
    m "Таким образом, мы разбираемся в ошибках, помогаем друг другу и даём возможность более робким членам клуба принять активное участие!"
    show monika ldown
    m "Ведь одно дело обсуждать чей-то стих всей группой, а другое -- с кем-то наедине."
    show monika cm oe
    mc "А вы так не путаетесь?"
    show monika om ce
    m "Пока до такого не доходило, ха-ха!"
    show monika om oe
    m "Ничего сложного же, так что всё в порядке."
    show monika lpoint
    m "Можешь начинать!"
    show monika nerv om oe ldown at s11
    m "Только не с меня, хочу морально подготовиться и перечитать своё стихотворение..."
    show monika cm oe
    mc "Хорошо, попробуем..."
    stop music fadeout 3.0
    show monika at thide
    hide monika
    pause 3.0
    "И с кого бы мне начать?"
    "Хотя это глупый вопрос..."
    "Конечно же с Сайори."
    "Тем более она сейчас стоит одна в другом конце класса, в то время как Юри и Нацуки уже вовсю обмениваются стихами."
    "Отсюда Сайори кажется совсем нелюдимой, будто уставилась в пустоту..."
    "Что-то произошло?"
    "Надо потом на всякий случай спросить Монику: она же часто с ней общается."

    scene bg school literature_club board day
    show sayori turned dist cm oe lclose rclose at t44
    with wipeleft_scene
    play music t5 fadein 3.0
    mc "Хэй, Сайори."
    show sayori lsur cm oe ldown rdown at t11
    s "О!"
    show sayori happ om ce lup rup at h11
    s "Макс!"
    show sayori om oe ldown rdown
    s "Ты пришёл показать мне свой стих?"
    show sayori cm oe
    mc "Ага, как доверенному лицу в этом обществе."
    show sayori om ce
    s "Ха-ха-ха!"
    show sayori happ om ce lup rup at h11
    s "Скорее, я слишком долго ждала этот момент!"
    show sayori cm ce ldown rdown
    mc "Вот, держи--{nw}"
    call window_close

    hide sayori with dissolve
    show sayori turned happ cm oe at face
    pause 0.3
    play sound paper_torn_out
    show sayori cm ce lup poem_paper
    pause 0.001
    with vpunch
    show sayori rup at t11

    call window_open
    mc "Тихо-тихо!"
    show sayori rdown
    mc "Не так резко!"
    call window_close

    show sayori e2b
    pause 5.0
    show sayori neut
    pause 5.0
    show sayori laug
    pause 5.0
    show sayori om oe

    call window_open
    s "Макс..."
    show sayori om ce
    s "Это очень забавно!"
    show sayori cm ce
    mc "Забавно?"
    show sayori happ om ce rup at h11
    s "Да!"
    show sayori om oe rdown
    s "У тебя интересно вышло!"
    show sayori e2b
    s "Здесь есть как юмор, так и серьёзные вещи!"
    show sayori cm
    mc "Разве?..."
    show sayori neut om
    s "Этот стих..."
    show sayori flus cm oe
    s "Он как будто веселый и немножко грустный одновременно."
    mc "Э-э-э, есть такое..."
    show sayori happ om ce
    s "Но очень мило смотреть, как ты стараешься найти в нём вдохновение!"
    show sayori om oe
    s "Мне понравилось!"
    play sound paper_torn_out
    show sayori cm oe
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    show sayori neut cm oe
    mc "Спасибо, а то я уж думал, что всё плохо."
    show sayori sad om oe
    s "Нет, у тебя классно вышло для первого раза!"
    show sayori neut cm oe
    mc "Хорошо, теперь твоя очередь."
    show sayori nerv om oe at s11
    s "А вот мой стих не очень хороший, хе-хе..."
    show sayori neut cm oe at t11
    mc "Сайори, ты же меня знаешь, я тебя всегда поддержу."
    mc "Давай я почитаю."
    call show_poem(poem_s1)
    "Нихрена себе..."
    show sayori nerv cm oe
    mc "Да ты меня переплюнула в два счёта!"
    show sayori tap nerv om oe at s11
    s "Э-хе-хе..."
    show sayori turned neut cm oe at t11
    mc "У тебя чувствуется лёгкость."
    mc "А я себя в какие-то рамки загнал, либо пытался выжать невыжимаемое."
    mc "Кстати..."
    show sayori happ cm oe
    mc "Ты это написала сразу после того, как проснулась?"
    show sayori om ce lup rup at h11
    s "Да!"
    show sayori om oe ldown rdown
    s "Как ты угадал?"
    show sayori flus om oe
    mc "Последняя строчка тебя выдала."
    show sayori cm ce at s11
    s "Ой..."
    show sayori cm oe
    mc "Я и сам слегка есть захотел, ха."
    show sayori nerv cm oe n3 at t11
    mc "Короче говоря, мне очень понравилось, так держать."
    show sayori om ce
    s "Спасибо."
    show sayori cm
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    pause 1.0
    show sayori happ cm oe n1
    mc "Ладно, пойдём другим покажем свои листы."
    show sayori om ce lup rup at h11
    s "Ок-ке!"
    show sayori cm ce ldown rdown

    scene black with wipeleft_scene
    "Вот, Сайори хотя бы оживилась."
    "Сразу принялась за Юри..."
    "Эй, к ним и Моника подошла со своим листком."
    "А как же парный обмен?"
    "Разве так можно?"
    "Или меня как новичка развели?"
    mc "Мда..."
    "В любом случае мне досталась лишь..."

    scene bg closet
    show natsuki turned fc neut cm oe lhip rhip at t11
    with wipeleft_scene
    show natsuki om
    n "Ну давай, показывай, чего стоишь?"
    show natsuki cm
    "...Нацуки."
    show natsuki anno cm oe
    "Учитывая её характер..."
    show natsuki om
    n "Эй, не тупи."
    show natsuki cm
    "...с ней нельзя быть расслабленым."
    show natsuki doub om oe
    n "Ты вообще здесь, а?"
    show natsuki anno cm oe
    mc "Да тут я, тут."
    mc "Держи."
    call window_close

    play sound paper_torn_out
    show natsuki lup poem_paper with dissolve
    pause 1.0
    show natsuki ff neut cm e1b
    pause 7.0
    show natsuki e2b me
    pause 7.0
    show natsuki e2a
    pause 2.0
    show natsuki md
    pause 2.0
    play sound paper_torn_out
    show natsuki ldown with dissolve
    pause 1.0

    call window_open
    mc "..."
    mc "...и?"
    show natsuki mf
    n "Мф-ф..."
    n "Пф-ф..."
    show natsuki laughter om at tremble
    n "{sc=3}ПХА-ХА-ХА-ХА-ХА-ХА-ХА!!!{/sc}"
    show natsuki cm
    "...иного от неё я не ожидал."
    mc "Тихо!"
    show natsuki om
    n "{sc=3}Не могу, это слишком ржачно!{/sc}"
    show natsuki cm
    mc "Издеваешься?!"
    show natsuki om
    n "{sc=3}Пха-ха-ха-ха-ха-ха-ха!!!{/sc}"
    show natsuki turned fc laug om oe lhip rhip at h11
    n "Теперь я спокойно могу поделиться с тобой своим стихотворением!"
    show natsuki cm ce
    mc "Это в каком смысле?"
    show natsuki om oe
    n "В том, что ты этим шедевром установил планку качества."
    show natsuki ce
    n "Ни-и-изкую планку качества!"
    show natsuki cm
    "Ну ты и засранка..."
    "Ладненько, сейчас глянем её «произведение искусства»."
    mc "Давай уже, показывай свой плод писательских трудов."
    mc "Оценю твою «планку качества»."
    show natsuki happ om oe
    n "Ха, да держи!"
    show natsuki cm
    call show_poem(poem_n1)
    mc "..."
    show natsuki curi cm oe
    mc "Это чё...{w}всё?"
    show natsuki om ldown rdown
    n "Что?"
    show natsuki anno cm oe
    mc "Это весь стих?"
    show natsuki om
    n "Да, разве не видно?"
    show natsuki cm
    mc "Ну, я попытался на него «зыркнуть»."
    show natsuki angr cm oe
    mc "Но он «тут же кончился»."
    show natsuki om ce lhip rhip
    n "Тьфу!"
    show natsuki oe
    n "Не надо мне тут каламбуры устраивать!"
    show natsuki cross ff angr om oe
    n "Это полноценный и скомпанованный стих, дурень!"
    show natsuki vang oe mj
    mc "Прямо как твой рост?"
    show natsuki turned fc vang cm oe at h11
    n "ГРХ!"
    mc "Что ж, вполне хорошо, я доволен."
    "...своим отыгрышем."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    mc "Но мне пора."
    show natsuki om lhip rhip
    n "Эй, стой, мы ещё не--{nw}"

    scene black with wipeleft_scene
    "Кажется, мы общались слишком громко..."
    "Но вовремя, однако, я отлип."
    "Сайори, подмигнув мне, схватила с собой Монику..."
    "И помчалась прямо к Нацуки, цундерный архетип."
    "Что-то меня понесло...{w}к Юри."

    scene bg club_day
    show yuri turned happ cm oe at t11
    with wipeleft_scene
    show yuri om oe lup
    y "Макс?"
    show yuri cm ce
    mc "Собственной персоной."
    show yuri om oe ldown
    y "Кто первый начнёт?"
    show yuri worr cm e1a
    mc "Давай я, мне уже терять нечего."
    show yuri om oe
    y "Это всё из-за Нацуки?"
    show yuri cm e1a
    mc "Отчасти, но я переиграл её «критику»."
    show yuri happ cm ce
    mc "Так что всё нормально."
    mc "Вот."
    show yuri cm oe
    call window_close

    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0

    call window_open
    mc "Открыт к любым замечаниям."
    call window_close

    show yuri e1b
    pause 4.0
    show yuri neut cm e1b
    pause 4.0
    show yuri mf
    pause 4.0
    show yuri e2b
    pause 2.0
    show yuri laug cm oe rup
    pause 3.0
    show yuri happ om ce

    call window_open
    y "Этот стих поднимает настроние, хе-хе..."
    show yuri om e1b rdown
    y "Видно, что ты старался обнаружить ту невидимую нить вдохновения, за которую трудно ухватиться."
    y "Ведь каждый из нас должен найти свой источник этого чувства, хоть порой это бывает непросто."
    show yuri oe
    y "Твои поиски уже приносят результат."
    y "У тебя есть некое ощущение написания стихов."
    show yuri anno om e1b
    y "Но, поскольку ты начинающий в этом деле, у тебя в некоторых местах сбит слог, из-за чего нарушаются темп и ритм."
    y "Также видно, что ты пытаешься писать в определённом строгом стиле, продумав каждую рифму, абсолютно всё до мелочей."
    show yuri dist om ce rup
    y "Однако в этом и кроется главная ошибка новичков."
    show yuri happ om oe rdown
    y "Попытайся написать следующее стихотворение более свободно, без всяких ограничений."
    show yuri flus cm oe rup at s11
    y "Конечно, я не виню тебя, у всех первый раз выходит комом..."
    show yuri happ om oe rdown at t11
    y "Просто нужно практиковаться и тогда всё получится."
    y "Отточив использование различных методов и навыков написания стихов, ты сможешь с лёгкостью изрекаться о чём угодно."
    show yuri cm oe
    mc "Ох..."
    show yuri lsur cm oe
    "Сразу видно, что Юри -- образцовый член Литературного клуба."
    show yuri flus cm oe rup at s11
    y "Я-я..."
    show yuri lsur cm oe
    mc "Нет-нет, я как раз хотел с тобой согласиться."
    show yuri happ cm oe rdown at t11
    mc "Спасибо за дельный совет, я прислушаюсь к нему."
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    mc "Что ж, тогда можно твой стих прочитать?"
    show yuri happ om ce
    y "Да, прошу!"
    show yuri cm ce
    call show_poem(poem_y1)
    show yuri laug cm oe
    "Вроде бы я и ожидал что-то такое..."
    "Но, чёрт побери, как же это красиво написано."
    "Во всех смыслах."
    show yuri lsur cm oe
    "Правда, контекст я не очень понял..."
    show yuri flus cm oe lup rup at s11
    y "П-прошу прощения за мой корявый почерк!"
    mc "Корявый?!"
    show yuri lsur cm oe
    mc "Да такой печатать на всеобщее обозрение нужно."
    show yuri happ cm oe ldown rdown at t11
    mc "Очень хороший стих, пропитан символизмом."
    show yuri cm ce
    mc "У тебя явно писательский талант."
    play sound paper_torn_out
    pause 1.0
    show yuri om oe
    y "Большое спасибо за похвалу, Макс, я это ценю."
    show yuri curi cm oe
    mc "А ты не планируешь в будущем связать свою жизнь с печатью?"
    mc "Ну, там написание всяких книг, стихов, прочего..."
    show yuri dist om oe rup
    y "Честно говоря, у меня уже была подобная мысль, но я ещё окончательно не решилась..."
    show yuri cm
    mc "Ясненько."
    show yuri neut om e1d
    y "Ещё, насчёт символизма стихотворения..."
    show yuri anno om ce
    y "Я сравнила персонажа с привидением."
    y "Он томится в комфортном месте, не в силах избавиться от оков прошлого..."
    show yuri lsur om ce
    stop music_poem fadeout 6.0
    y "И вскоре остаётся ни с чем."
    y "Становится пустотой."
    show yuri cm ce
    mc "..."
    show yuri om oe rup lup at s11
    y "Э-э, Макс?"
    y "Что-то не так?"
    show yuri cm oe
    mc "...а?"
    show yuri ldown rdown at t11
    mc "Нет-нет-нет, всё в порядке."
    mc "Просто перевариваю смысл твоего стиха в голове..."
    show yuri e2b mb
    y "Есть что-то в этом особенное, да?"
    show yuri ma
    "Ага, когда это «особенное» -- моё грёбаное состояние из-за двух кидал: друга и психолога."
    "Зачем я только про них вспомнил..."
    show yuri cm oe lup rup at h11
    "Да твою ж ты мать, когда ты о них уже забудешь, а?!" with vpunch
    "Сколько можно себя выжирать из-за этого и постоянно ныть?"
    "Уже даже «отомстить» смог, но не-е-ет, ничерта состояние не поменялось!"
    "Каждый раз, когда я вспоминаю это дерьмо, меня начинают пожирать мысли."
    show yuri vsur cm oe at s11
    "Почему вы все такие мрази?"
    "Ни на кого нельзя надеяться!"
    "Раздражает-раздражает-раздражает!"
    show yuri shoc om oe
    y "Макс?!"
    show yuri vsur cm oe
    mc "Всё хорошо -- всё хорошо -- всё хорошо!"
    mc "Всего лишь слегка задумался, ха-ха-ха..."
    show yuri at t11
    mc "Не переживай, я в норме."
    show yuri sad om oe
    y "Х-хорошо..."
    show yuri lsur cm oe ldown rdown
    mc "Ладно, спасибо за компанию, но мне ещё надо Монике показать своё творение."
    show yuri flus om oe
    y "Да, я понимаю, всё нормально."
    show yuri lsur cm oe
    mc "Извини за моё поведение."
    show yuri flus cm oe lup rup at s11
    y "Н-не стоит себя корить, у всех иногда бывают плохие мысли..."
    show yuri lsur cm oe
    mc "Всё равно."

    scene black with wipeleft_scene
    "Осталась только Моника."
    "...где она?"
    "А, она осталась с Сайори."
    "Юри уже ушла к Нацуки, они там что-то живо обсуждают."
    "Лишь бы не мою выходку..."
    "..."
    "Эй..."
    "Мне совершенно не нравится, что Сайори снова вернулась в своё сидячее состояние с лицом мрачнее тучи."
    "Моника активно с ней шепчится, но по её взгляду ей тоже это не нравится."
    "Да что происходит?"
    "..."
    "А, всё, увидела меня."
    "Значит так: сначала стихи, потом сразу спрошу про Сайори."

    scene bg school literature_club board day
    show monika forward happ cm oe at t11
    with wipeleft_scene
    play music t5 fadein 3.0
    show monika lean happ om oe at h11
    m "Ну что, Макс, готов делиться своим стихотворением?"
    show monika cm oe
    mc "Естественно, я тебя ради этого и ждал."
    show monika forward happ om oe at t11
    m "Отлично, давай посмотрим!"
    call window_close

    show monika cm oe
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show monika e1b
    pause 4.0
    show monika neut cm
    pause 6.0
    show monika happ cm
    pause 3.0
    show monika laug cm e2b
    pause 3.0
    show monika happ om ce

    call window_open
    m "Ха-ха-ха!"
    show monika om oe
    m "Хорошая работа, Макс!"
    m "Ты очень постарался!"
    show monika cm oe
    mc "Да..."
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    show monika om oe
    m "Видно, что ты уже пытаешься писать в собственном стиле."
    show monika lean happ om oe at h11
    m "К слову, я заметила у тебя смесь всех стилей участниц нашего клуба!"
    show monika cm oe at t11
    mc "В смысле, это как?"
    show monika forward happ om oe lpoint
    m "Ты же ведь успел прочитать их стихотворения?"
    show monika cm oe ldown
    mc "Да, перед тобой."
    show monika om oe lpoint rhip
    m "Так вот, пройдёмся по порядку."
    show monika ldown rdown
    m "Сайори пишет достаточно плавно и легко."
    show monika neut om oe
    m "Обычно стихотворения описывают её внутреннее состояние и выходят светло-грустными, как она сама мне однажды выразилась."
    show monika happ om oe
    m "У тебя тоже есть нечто подобное, но с большей самоиронией и жёсткостью."
    show monika cm oe
    mc "Да уж..."
    show monika happ om oe lpoint rhip
    m "Далее -- Нацуки."
    show monika ldown rdown
    m "Она всегда пишет простыми словами, в большинстве случаев четверостишиями."
    show monika om ce
    m "В отличие от Сайори, её стихи больше направлены на окружение, при этом Нацуки преломляет их через свою призму милоты, ха-ха!"
    show monika om oe lpoint
    m "Кстати, на будущее: она не любит, когда её называют милой."
    show monika neut cm oe ldown
    mc "Почему?"
    show monika dist om oe
    m "Это тоже касается темы с хранением её манги, так что..."
    show monika happ om ce
    m "Расскажу тебе ещё чуть позже!"
    show monika cm ce
    mc "Опять интриги..."
    show monika laug mb oe
    m "Сейчас не самое время, прости."
    show monika cm
    mc "...хорошо, не настаиваю."
    show monika happ om oe rhip
    m "Ладно, продолжим."
    show monika rdown
    m "Твоё стихотворение тоже поделено на четверостишия, плюс в некоторых местах слова стоят в простом значении, то есть без всякого подтекста."
    show monika cm oe
    mc "Хм..."
    show monika om oe lpoint rhip
    m "Ну и осталась Юри."
    show monika om ce ldown rdown
    m "Не устану это повторять -- она у нас прирождённый поэт!"
    show monika oe
    m "Её стихи пропитаны контекстным смыслом, используется разнообразие метафор и эпитетов, некоторых приёмов, связанных с рифмовкой, и так далее..."
    m "Хотя обычно, если стихотворения небольшие, Юри не рискует использовать что-то «литературно-профессиональное»."
    show monika neut mh e1b
    m "Всё-таки что бы мы ни говорили, до мастерского уровня ей далеко..."
    show monika laug mb ce
    m "Так, что-то я заговорилась, хах..."
    show monika ma
    mc "Ничего, мне интересно слушать."
    show monika happ om oe lpoint rhip
    m "Время у нас не резиновое, поэтому вернёмся к теме разговора."
    show monika ldown rdown
    m "Юри часто прибегает к использованию пространственных значений слов."
    m "У тебя я тоже заметила нечто такое, хоть и не в таком глубоком значении."
    show monika om ce
    m "Как-то так!"
    show monika cm
    mc "Даже не верится..."
    show monika om oe
    m "Может быть, это выглядит крайне натянуто, однако факт -- есть факт."
    show monika neut cm oe
    mc "Я вообще писал как мог, у меня совершенно нет чувства собственного стиля."
    show monika dist om ce
    m "Знаешь, тогда мы можем поступить следующим образом..."
    show monika happ om oe lpoint
    m "В течение трёх следующих встреч ты попробуешь составить по одному стихотворению на каждый стиль участницы клуба."
    show monika ldown
    m "Таким образом мы выявим, в каком направлении у тебя лежит душа."
    show monika cm oe
    "Ограничение своими рамками сменяется ограничением другими..."
    "Нет, здесь надо смотреть на это как на шаблон."
    "Учитывая, что это поможет мне сэкономить кучу времени на создание стиха..."
    mc "А что?"
    show monika cm ce
    mc "Звучит неплохо."
    show monika om ce
    m "Договорились."
    show monika om oe
    m "С кого начнёшь?"
    show monika cm oe
    mc "С Сайори."
    "Очевидно же."
    show monika om oe lpoint rhip
    m "Тогда завтра буду ждать тебя с первым экспериментальным стихом!"
    show monika cm oe ldown rdown
    mc "Хорошо."
    show monika lsur om oe lpoint at h11
    m "Ох, точно!"
    show monika nerv om oe ldown
    m "Я уже хотела заканчивать, но тебе же ещё не показала свой листок."
    show monika happ om ce
    m "Вот, держи."
    show monika cm ce
    call show_poem(poem_m1)
    "Довольно абстрактно..."
    "Не могу понять, что именно Моника имела в виду, но, возможно, что-то связанное с внешним миром?"
    "И собственным представлением окружения, которое изменилось после первого «взгляда» на этот мир."
    show monika cm oe
    mc "Ох, этот стих оказался сложнее в понимании, чем я себе представлял."
    show monika om ce
    m "Не пугайся, у меня так часто выходит."
    show monika cm oe
    mc "Любишь абстрактность?"
    show monika neut om oe
    m "Не могу точно сказать..."
    show monika e1b
    m "Просто на меня иногда внезапно наваливается вдохновение с образами."
    show monika curi cm ce
    m "Как бы лучше выразиться..."
    show monika happ om oe lpoint
    m "О, озарение."
    show monika e1b ldown
    m "Да, так будет корректнее."
    show monika cm oe
    mc "Понимаю..."
    play sound paper_torn_out
    pause 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    mc "Стих мне понравился, но больше нечего сказать, извини."
    mc "Критик из меня никакущий."
    show monika om ce
    m "Не переживай, это нормально."
    show monika om oe
    m "Я уже давно занимаюсь написанием стихотворений, достигнув некого продвинутого уровня относительно любителя, если так можно выразиться, хах."
    m "А учитывая специфичность выражения моих мыслей, в твоей реакции нет ничего плохого."
    show monika cm oe
    mc "Но мне всё равно понравилось."
    show monika om ce
    m "Да, спасибо."
    show monika om oe lpoint rhip
    m "Ладно, думаю, пора заканчивать наш обмен стихами."
    show monika cm oe ldown rdown at thide
    hide monika
    pause 0.5
    "Один я здесь криворукий."

    scene bg club_day
    show monika forward happ cm oe at t11
    with wipeleft_scene
    show monika om oe lpoint rhip
    m "Итак, друзья!"
    show sayori turned happ cm oe at t41
    show monika cm oe ldown rdown at t42 zorder 2
    show natsuki turned neut cm oe at t43
    show yuri turned happ cm oe at t44
    pause 0.75
    show monika om oe
    m "Как вам первый обмен стихами в этом учебном году?"
    show sayori om ce lup rup at h41
    show monika cm oe
    s "Было очень интересно!"
    show sayori cm ce ldown rdown at t41
    show natsuki e1b
    show yuri om e1b
    y "Довольно продуктивно."
    show natsuki om
    show yuri cm
    n "Вполне."
    show sayori cm oe
    show monika lean happ om oe at h42
    show natsuki cm oe
    show yuri cm oe
    m "А ты, Макс, что думаешь?"
    show monika cm oe at t42
    mc "А что мне думать?"
    mc "За меня уже всё сказали, добавить нечего."
    show sayori cm ce
    show monika forward happ om ce
    show yuri cm ce
    m "Отлично!"
    show monika om oe
    show natsuki e1c
    m "Завтра примерно в это время снова организуем такое же мероприятие."
    show sayori neut cm oe
    show monika lpoint
    show natsuki cm oe
    show yuri neut cm e1d
    m "...с одним небольшим «но»."
    show sayori curi cm oe
    show monika cm oe ldown
    show natsuki curi cm oe
    show yuri curi cm oe
    nsy "???"
    show monika om ce
    m "Поскольку Макс у нас новичок, мы решили сделать следующее..."
    show sayori flus cm oe
    show monika om oe lpoint rhip
    show natsuki doub cm oe
    show yuri happ cm oe
    m "В течение трёх последующих встреч он попробует написать собственные стихотворения на основе ваших."
    show monika ldown rdown
    m "Иными словами, мы посмотрим, в каком направлении ему лучше развиваться."
    show sayori e1a
    show monika lean happ om oe at h42
    m "Что считаете по этому поводу?"
    show sayori happ om ce lup rup at h41
    show monika cm oe at t42
    s "Так пробовать что-то новое -- всегда здорово!"
    show sayori cm oe ldown rdown at t41
    show yuri om e1b lup
    y "Я думаю, это правильное решение: Максу необходимо найти основу в этом деле."
    show sayori neut cm oe
    show monika forward happ cm oe
    show natsuki om oe lhip rhip
    show yuri neut cm e1d ldown
    n "Ты серьёзно думаешь, что он сможет что-то сварганить в моём стиле?"
    show natsuki cm oe
    "Иронично, но поверхностность Нацуки слишком «поверхностная» и исковерканная, в хорошем смысле этого слова."
    "Короче, писать в таком ключе я точно не смогу."
    show sayori happ cm ce
    show monika om oe lpoint rhip
    show natsuki neut cm oe ldown rdown
    show yuri happ cm oe
    m "А это мы как раз и выясним."
    show sayori neut cm oe
    show monika neut om ce ldown rdown
    show natsuki e2a
    show yuri neut cm e1d
    m "Итак, первым «прототипом» для нашего новоиспечённого участника послужит..."
    show sayori flus om ce at h41
    show monika happ om ce
    show natsuki anno cm oe
    show yuri e1b
    m "...Сайори!"
    show sayori om oe at t41
    show monika cm ce
    s "Я?!"
    show sayori cm oe
    show monika om oe
    show yuri e1d
    m "Да, но в любом случае никто не будет обделён."
    show sayori happ cm e4c
    show monika neut cm oe
    show monika cm oe
    show natsuki dist om oe
    n "{color=#fc7e23}Meh{/color}."
    show natsuki neut om oe
    show yuri angr cm oe
    n "Не поприкалываться завтра..."
    show natsuki neut cm e1c
    show yuri om oe
    y "Как грубо, Нацуки!"
    show natsuki happ cm oe
    show yuri lsur cm oe
    mc "Не в мою смену."
    show natsuki happ om ce lhip rhip
    n "\"А это мы как раз и выясним!\""
    show monika om ce
    show natsuki cm ce
    show yuri anno cm oe
    m "Всё, хватит."
    show sayori cm oe
    show monika happ om oe
    show natsuki neut cm oe ldown rdown
    show yuri happ cm oe
    m "Раз мы договорились, то Юри и Нацуки могут быть свободны!"
    show monika cm oe
    show natsuki om
    n "Угу, до завтра."
    show natsuki e1c
    n "Пошли, Юри."
    show natsuki cm at thide
    hide natsuki
    show yuri om
    y "До завтра."
    show yuri cm at thide
    hide yuri
    show monika at t22
    show sayori at t21
    pause 1.0
    show monika om oe lpoint
    m "Сайори, тебе придётся одолжить Максу на вечер своё сегодняшнее стихотворение."
    show sayori om ce lup rup at h21
    show monika cm oe ldown
    s "Я и не против, двумя руками «за»!"
    show sayori om oe ldown rdown at t21
    s "Макс, держи!"
    show sayori cm
    play sound paper_torn_out
    pause 1.0
    mc "Окей..."
    show monika om ce
    m "Ну, в принципе, всё!"
    show sayori cm ce
    show monika oe
    m "Вы свободны."
    show sayori neut cm e2a
    show monika lsur cm oe at h22
    m "Ой, стойте!"
    stop music fadeout 3.0
    show sayori cm oe
    show monika neut om oe lpoint at t22
    m "Макс, останься буквально на минуту, мне надо кое-что рассказать."
    show monika cm oe ldown
    "Чёрт, точно!"
    mc "Да, я тоже хотел кое-что обсудить."
    "Моника меня заболтала."
    show monika happ om oe
    m "Сайори, подождёшь Макса в коридоре буквально пару минут?"
    show sayori happ om ce lup rup at h21
    show monika cm oe
    s "Ок-ке!"
    show sayori cm ce ldown rdown at thide
    hide sayori
    pause 2.0
    show monika neut om oe at t11
    m "Так вот..."
    show monika cm
    mc "Сайори, да?"
    show monika om ce
    m "Значит, мы думаем об одном и том же."
    show monika oe lpoint
    m "Замечал у неё когда-нибудь некую подавленность, грусть?"
    show monika ldown
    m "Особенно в последнее время."
    show monika cm oe ldown
    mc "Шутишь?"
    mc "Она всегда была счастливой и энергичной."
    mc "Бывали редкие моменты подавленности, но они быстро проходили."
    mc "Хотя вот сегодня во время обмена стихами Сайори прямо убитой была."
    mc "О чём ты там с ней шепталась, если не секрет?"
    show monika om e1b
    m "Это..."
    show monika ce b1b
    m "С ней всё сложно..."
    show monika cm
    mc "Говори, как есть, Моника, пожалуйста."
    mc "Я же за неё, как друг, переживаю."
    show monika om
    m "Ох..."
    show monika mh oe -b1b lpoint
    m "В общем, сегодня я встретила Сайори на крыше."
    show monika ldown
    m "Она сидела на коленях, понурив голову с заплаканным лицом."
    show monika cm
    mc "...с чего это?"
    show monika mh
    m "Я тоже сначала не поняла."
    show monika dist mh oe
    m "Но когда разговорилась с ней, то...{w}ну, я ожидала такое."
    show monika neut cm oe
    mc "Чего?"
    show monika om
    m "Смотри."
    show monika lpoint
    m "Всё это время Сайори постоянно излучает позитив, правильно?"
    show monika cm ldown
    mc "Да."
    show monika om
    m "На это уходит много энергии."
    show monika cm
    mc "Тоже да."
    show monika curi om oe rhip
    m "Но ты видел хоть какие-нибудь моменты, когда Сайори достойно отплачивали за её старания?"
    show monika neut mh oe
    m "В плане, она часто поддерживает друзей, старается их взбодрить, повысить им настроение..."
    show monika curi om oe
    m "А вот было ли такое, чтобы окружающие тоже пытались поддержать Сайори, подарить ей любовь и тому подобное?"
    show monika md
    mc "Хм..."
    show monika neut cm oe rdown
    mc "Ну...{w}э-э-э..."
    mc "Со своей стороны я пытаюсь что-то такое делать, но не знаю, насколько это эффективно..."
    mc "Насчёт остальных не знаю, честно."
    show monika om
    m "Вот я всегда стараюсь ей отплатить взаимностью."
    show monika dist om oe
    m "Юри и Нацуки тоже в курсе её проблемы, но в силу «особенностей» своих характеров у них не получается сделать то же самое должным образом..."
    show monika neut cm oe
    mc "А больше, я так понимаю, Сайори в школе ни с кем не общается?"
    show monika om
    m "Думаю, да, а кто тут ещё будет?"
    show monika b1b
    m "Даже если такие люди и есть, то вряд ли они близки, как мы с тобой."
    show monika -b1b
    m "Всё-таки ты с Сайори тоже не первый день общаешься, должен это понимать."
    show monika cm
    mc "Да-да..."
    mc "Бу-у-у..."
    show monika dist cm oe
    mc "Ну и что делать?"
    show monika om
    m "У меня нет идей."
    show monika neut om oe b1b
    m "Как видишь, моего внимания и внимания клуба недостаточно."
    show monika cm -b1b
    mc "А если условно посвятим какой-нибудь день целиком Сайори?"
    show monika om
    m "Нет, Макс, не поможет."
    show monika lpoint
    m "Это будет выглядеть натянуто и фальшиво, что закопает её ещё больше."
    show monika ldown
    m "Вот, кстати, на крыше она сказала, что считает себя обузой."
    show monika b1b
    m "Так что такое только укрепит её уверенность в этом."
    show monika cm -b1b
    mc "А если попросить её не напрягаться?"
    show monika om lpoint
    m "Уже пробовала, она не хочет скидывать с себя эту маску."
    show monika dist om oe ldown
    m "Но вот почему, не знаю..."
    show monika cm
    mc "М-м-м..."
    show monika neut cm oe
    mc "Ты, кстати, так ничего про шептания и не сказала."
    show monika mh b1b
    m "Ой, Макс, я всего лишь сказала ей не хмуриться и не бояться выговориться, если захочет это сделать."
    show monika cm
    mc "А, понятно."
    show monika flus om oe -b1b
    m "Не знаю я, что с ней делать..."
    show monika neut mh oe
    m "Но тебя проинформировала."
    show monika happ cm oe b1b
    mc "Спасибо и на этом, Моника."
    show monika neut cm oe
    mc "Постараюсь поговорить с Сайори на эту тему."
    show monika om
    m "Да, ты ближе всех к ней, тебя она должна послушать лучше, чем остальных."
    show monika -b1b lpoint
    m "К тому же ты будешь писать стих в её стиле, так что удели Сайори чуть больше времени и внимания."
    show monika ce b1b ldown
    m "Только прошу, аккуратно."
    show monika cm
    mc "Пф, это даже не обсуждается."
    show monika happ om oe
    m "Не забудь держать меня в курсе, хорошо?"
    show monika cm
    mc "Само собой."
    show monika -b1b
    mc "Ох, вступил в клуб, называется..."
    show monika om oe
    m "Да ладно, не вздыхай, не так это и плохо."
    show monika ce
    m "Просто у нас всё «своеобразненько», хах."
    show monika cm
    mc "Ну-ну."
    show monika oe
    mc "До завтра, Моника."
    show monika om
    m "До завтра, Макс!"
    show monika cm
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show sayori turned neut cm oe school_bag at t11
    with wipeleft_scene
    show sayori om ce lup rup
    s "Ви-и-и..."
    show sayori sedu mb oe ldown rdown
    s "Неужели всё?"
    show sayori neut cm oe
    mc "Извини за задержку, но этот разговор был необходим."
    show sayori om
    s "Настолько всё серьёзно?"
    show sayori cm
    mc "Да."
    show sayori curi cm oe
    mc "Потому что это касается тебя, Сайори."
    show sayori om
    s "Что?"
    show sayori cm
    mc "Пойдём, объясню по пути."
    show sayori neut cm oe
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    play noise_1 street_suburban_noise fadein 3.0
    call window_open
    scene bg niigata street suburban 10 afternoon
    show sayori turned dist cm oe school_bag at t11
    with wipeleft_scene
    show sayori om
    s "Выходит, ты знаешь, что сегодня мне было нехорошо..."
    show sayori cm
    mc "Угу."
    show sayori om ce
    s "И то, что мы чуть с Моникой не промокли..."
    show sayori neut cm oe
    mc "Так, а это уже не знаю."
    show sayori happ cm oe
    mc "Вы под ливень попали?"
    show sayori om ce
    s "Мы быстро спрятались, поэтому мы сухонькие."
    show sayori cm
    mc "Да уж."
    show sayori neut cm oe
    mc "Но так насчёт твоего состояния..."
    s "М-м?"
    mc "Это же всё не на ровном месте, верно?"
    show sayori curi cm oe
    mc "Тебя что-то тревожит, Сайори?"
    show sayori om
    s "Да нет..."
    show sayori cm
    mc "А если честно?"
    show sayori neut om e2b
    s "Нет..."
    show sayori cm
    "Блин, я так ничего не добьюсь."
    "Надо как-то вывернуть разговор на её маску..."
    show sayori oe
    mc "А вообще, я давно хотел у тебя спросить, но всё забываю..."
    show sayori laug ma oe
    mc "Тяжело быть «батарейкой» с кучей энергии в одном месте?"
    show sayori om
    s "Кхм, Макс..."
    show sayori neut cm oe
    mc "Ладно, если серьёзно, то это же трата сил в большом количестве."
    mc "Ты не устаёшь от такого?"
    show sayori om e2c
    s "Ну..."
    show sayori oe
    s "Бывает, под вечер в сон клонит так, что до кровати с трудом доползаешь..."
    show sayori happ om oe
    s "А так ничего, нормально."
    show sayori neut cm oe
    mc "А упаднические моменты?"
    show sayori worr om oe
    s "Давай не будем об этом..."
    show sayori cm
    mc "Нет, как раз-таки надо."
    show sayori neut cm oe
    mc "Тут такой парадокс: ты не хочешь об этом говорить, потому что это больно, но я хочу с тобой об этом поговорить, чтобы такое больше не происходило, а значит, чтобы не было больно."
    show sayori vsur cm oe
    s "Э-э-э..."
    show sayori worr cm e1a
    mc "Короче, Сайори, из-за чего у тебя в такие моменты падает настроение?"
    show sayori om oe
    s "Это не столь важно..."
    show sayori neut cm oe
    mc "Я за тебя переживаю."
    show sayori om
    s "Зачем?"
    show sayori e2b
    s "Со мной всё в порядке."
    show sayori cm e2a
    mc "Нет же!"
    show sayori oe
    mc "Сайори, ты мой друг."
    show sayori b1b
    mc "И я хочу позаботиться о своём друге."
    show sayori e1b
    mc "И я прекрасно понимаю, что ты не любишь напрягать окружение."
    show sayori oe -b1b
    mc "Однако что ты скажешь на то, что я хочу напрячься и помочь тебе?"
    show sayori mf e2b at s11
    s "У-у..."
    show sayori cm
    s "..."
    show sayori sad om ce lclose rclose at t11
    s "...не надо, Макс."
    show sayori md
    mc "Надо, Сайори, надо."
    show sayori oe
    mc "Я уже понял, что у тебя на автомате эта маска жизнерадостности доминирует."
    mc "А ты ещё ярый альтруист."
    mc "Но пойми: если ты не научишься контролировать это состояние, то будешь из-за него мучиться."
    show sayori e1b
    mc "И если ты не будешь подпитываться добротой и помощью окружающих, то рано или поздно сломаешься."
    mc "А это никому из нас не надо."
    show sayori ce
    mc "Как минимум мне и твоим родителям точно."
    show sayori om
    s "Эх..."
    show sayori oe
    s "Но я...{w}Макс, я тогда точно сломаюсь, если стану другой."
    show sayori md
    mc "Почему?"
    show sayori om e1b
    s "Я не знаю, как жить по-другому."
    show sayori md
    mc "Как это?"
    show sayori oe
    mc "Просто собой быть и не париться."
    show sayori om
    s "Но ведь я и так своя..."
    show sayori neut cm oe
    mc "Ты точно в этом уверена?"
    mc "Когда ты своя, то ты получаешь удовольствие от жизни без всякого напряжения и усталости."
    show sayori worr cm oe
    mc "...что в твоём случае видно лишь поверхностно."
    show sayori om at s11
    s "Тогда я не знаю, что делать..."
    show sayori cm
    mc "Я, честно, тоже..."
    show sayori neut cm oe at t11
    mc "Хотя подожди, есть идея."
    show sayori om
    s "Какая?"
    show sayori cm
    mc "Попробуй с этого дня потихоньку, медленно и размеренно сбавлять излишний позитив, заменяя его искренними эмоциями."
    show sayori om e1b
    s "Звучит сложно..."
    show sayori cm
    mc "А тут больше никак."
    show sayori om oe
    s "Разве от этого что-то поменяется?"
    show sayori cm
    mc "Поменяется, ещё как."
    mc "Ведь одно дело, когда ты выдавливаешь чувства, а другое -- даёшь выйти им самим."
    show sayori worr mf e2b
    s "У-у..."
    show sayori om ce
    s "Не знаю, попробую..."
    show sayori cm
    mc "Рад слышать."
    "Фу-у-ух..."
    "Я уж надеялся на более трудный разговор."
    show sayori dist cm oe
    "Надеюсь, мой совет {b}реально{/b} поможет облегчить ей жизнь."

    scene bg house
    show sayori turned dist ma oe school_bag lclose rclose at t11
    with wipeleft_scene
    show sayori dist mb oe
    s "Вот мы и снова пришли..."
    show sayori ma
    mc "Ага."
    show sayori neut om oe
    s "Тогда я..."
    show sayori cm e2a
    mc "Стой."
    show sayori oe
    mc "Пообещай мне, что с этого дня ты будешь становится истинной собой."
    show sayori laug om oe ldown rdown
    s "Ладно-ладно!"
    show sayori anno mi ce
    s "Торжественно клянусь, что я стану Сайористой Сайори."
    show sayori laug om ce
    s "А это значит, что я смогу клянчить у тебя печенье каждый день без зазрения совести!"
    show sayori cm
    mc "Ох, чёрт..."
    mc "Мой кошелёк в гробу перевернётся."
    show sayori om
    s "А-ха-ха!"
    show sayori happ om oe
    s "Ладно, жду завтра твой новый стих!"
    show sayori cm oe
    mc "Постараюсь написать."
    show sayori om ce
    s "Удачи!"
    show sayori cm
    mc "До встречи!"
    call window_close
    show sayori at thide
    hide sayori
    pause 0.5
    stop noise_1 fadeout 2.0

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "С уроками покончено."
    "..."
    mc "Ай..."
    "Голова разболелась..."
    "С чего это вдруг?"
    "Причём боль только у правого виска."
    "А мне ещё в таком состоянии стих надо составить..."
    "Это какое-то издевательство."
    "Почему мне нельзя просто взять и расслабиться после всего, что было за день..."
    "Я всего лишь хочу отдохнуть, а не заниматься какой-то хренью, которая, кроме сжигания времени, мне ничего полезного не даст."
    "Но не-е-ет, Макс должен попробовать различные стили, чтобы открыть в себе пОэТиЧеСкИй ТаЛаНт."
    "Какие, нафиг, стихи, если через этот учебный год уже выпуск?"
    "Мне это как-то поможет в жизни?"
    "Ничерта."
    "А никого это даже не волнует."
    "Администрация школы очень хочет, чтобы все ученики были вовлечены во внеурочную деятельность."
    "Идите вы все к чёрту со своими клубами."
    "Вместо того, чтобы заниматься чем-то ПО-НАСТОЯЩЕМУ полезным или просто передохнуть, я должен сейчас сидеть и клепать стих."
    "..."
    "......"
    "А теперь серьёзно."
    "Мне Моника пошла навстречу с этой клубной деятельностью, а Сайори одолжила своё творение."
    "Нечего тут возмущаться."
    "К тому же на моих плечах состояние самой Сайори."
    "А мой следующий стих поможет уделить ей чуть больше времени."
    "Ладно, побыстрее его сделаю, чтобы не закопаться."
    "Где там этот «пример»..."
    "..."
    "Нашёл."
    "..."
    "...от него несёт...{w}сладковатым запахом?"
    "Вроде такой запах у волос Сайори."
    "Ну, она же рано утром стих писала, так?"
    "Вероятно, просто уткнулась лбом в стих из-за сонливости и пролежала так пару минут."
    "Это же Сайори, ха."
    "Так, надо внимательно прочитать стих и осознать его структуру."
    call show_poem(poem_s1, music=False)
    mc "Хм..."
    "Немного сбитый ритм, в первом четверостишии...{w}как там это...{w}кольцевая рифма, вот: первое с четвертым, второе с третьим."
    "Во втором четверостишии уже перекрёстная рифма: через строку."
    "А дальше вообще мешанина."
    "Сайори совсем не напрягалась."
    "Как пришла идея, так и легла сразу."
    "Но такое утром немудрено: голова в это время не варит."
    "Всё, попробуем стиль Сайори..."

    call poem_act_1_day_2

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc2, music=False)
    "Ну, как-то..."
    "Нет, конечно, это уже посерьёзнее и получше, чем первый стих, однако...{w}Сайори это точно не порадует..."
    "Да, придумал я этот стих быстрее, чем прошлый, плюс он более свободный по стилю, но...{w}хрень же!"
    "Блин, виски..."
    "Левый тоже запульсировал вслед за правым."
    "В общем, устал я, сосредоточиться никак не могу..."
    "Пора отдохнуть..."
    call window_close

    return
