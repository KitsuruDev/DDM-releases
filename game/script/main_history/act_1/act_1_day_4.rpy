
label act_1_day_4:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d3.unlocked == False:
        $ ach_a1_d3.unlock()

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
    mc "{cps=20}Умф-ф-ф-ф...{/cps}"
    "Опять эти ваши утры..."
    "Так хочется понежиться в кровати..."
    "Чёртова школа со своим распорядком дня."
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    "..."
    "......"
    mc "Я.{w} НИЧЕГО.{w} НЕ.{w} ЗАБЫЛ."
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
    "Вроде бы взбодрился, сонливости уже нет..."
    "...но такое ощущение, будто меня насильно вытолкали с кровати на улицу."
    s "Хэй!"
    show sayori turned happ cm oe school_bag at l11
    pause 0.7
    show sayori laug om oe
    s "Вот теперь это точно ты!"
    show sayori cm oe
    mc "Да, в этот раз я как обычно..."
    show sayori happ om oe
    s "Зато выспался, ведь так?"
    show sayori cm oe
    mc "Ну как сказать..."
    show sayori om ce lup rup at h11
    s "Говори как есть!"
    show sayori curi cm oe
    mc "И да, и нет."
    show sayori om oe ldown rdown
    s "Значит, нет?"
    show sayori cm oe
    mc "Да."
    show sayori neut cm oe
    mc "То есть нет."
    show sayori laug cm ce
    mc "Тьфу, я запутался!"
    show sayori happ cm oe
    mc "Давай лучше пойдём в школу, пока я окончательно не поломался."
    show sayori om ce lup rup at h11
    s "Ок-ке!"
    show sayori cm ce ldown rdown

    scene bg niigata street suburban 10 day
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    "О, надо спросить её про Нацуки."
    "И про Юри бы ещё не помешало."
    mc "Сайори..."
    show sayori neut om oe
    s "Эх?"
    show sayori cm oe
    mc "Ты вчера успешно довела Нацуки до дома?"
    show sayori happ om ce lup rup at h11
    s "Конечно!"
    show sayori om oe ldown rdown
    s "Ещё я с ней по пути поговорила."
    show sayori curi om oe
    s "Она сказала, что ты в чём-то там оказался прав..."
    show sayori neut om oe
    s "Поэтому она сожалеет, что написала последний стих про ненависть к паукам и к Э{image=accent_high_register}{space=-15}ми."
    show sayori happ om ce
    s "А исправить это Нацуки решила новым стихом."
    show sayori cm ce
    mc "О как..."
    show sayori neut cm oe
    mc "Кажется, я вчера произвёл на неё сильное впечатление..."
    show sayori curi om oe
    s "А что тогда было?"
    show sayori cm oe
    mc "Пытался рассказать ей, как тяжело быть пауком, но потом уехал в своих мыслях куда-то в сторону."
    show sayori neut cm oe
    mc "Вообще, кстати, я тут на досуге над этой ситуацией поразмышлял и у меня появилось одно предположение..."
    "Да, такое же, как и с Юри -- проблема с семьёй."
    mc "Сайори, что там у Нацуки дома творится?"
    mc "В плане, семья, жизнь, прочее?"
    show sayori lsur om oe
    s "О-о..."
    show sayori neut om e2b
    s "Ну..."
    show sayori cm oe
    mc "Я понимаю, что лезу не в своё дело...{w}да и Моника обещала просветить, правда, непонятно когда...{w}но всё же."
    show sayori om oe
    s "Знаешь, пусть лучше она сама всё расскажет."
    s "Ей намного виднее, чем нам."
    show sayori worr om oe
    s "...и я не хочу говорить на эту тему, извини..."
    show sayori cm oe
    mc "Хорошо, твоё право."
    "Опять вы всё тянете до последнего..."
    show sayori neut cm oe
    mc "А насчёт Юри?"
    show sayori curi om oe
    s "А что с ней?"
    show sayori cm oe
    mc "Просто..."
    show sayori neut cm oe
    mc "Ты читала её последнее стихотворение про енота?"
    show sayori happ om ce lup rup at h11
    s "Да!"
    show sayori om ce ldown rdown
    s "Енотики забавные!"
    show sayori cm ce
    mc "Енотики..."
    "Сайори как всегда в своём духе беззаботности, причём искреннем."
    "Это радует, но не отменяет мой вопрос."
    show sayori neut cm oe
    mc "В этом стихотворении могло быть какое-нибудь...{w}нестандартное или необычное сравнение?"
    show sayori om oe
    s "Разве там такое есть?"
    show sayori cm oe
    mc "Вот я и спрашиваю."
    show sayori curi cm ce
    s "Хм-м-м..."
    show sayori neut om oe
    s "Возможно, но я ничего такого не заметила."
    show sayori cm oe
    mc "Ясно..."
    show sayori happ cm oe
    "К чёрту, не буду втягивать её в подобное разбирательство."
    show sayori cm ce
    "Хоть я ей доверяю, но вдруг она случайно проболтается, из-за чего поползут слухи и прочая хрень?"
    "А такое только усугубит и без того отвратительную ситуацию."

    scene bg school gate 1
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om ce lup rup at h11
    s "Увидимся в клубе!"
    show sayori cm ce ldown rdown
    mc "Да, увидимся..."
    show sayori at thide
    hide sayori
    pause 1.0
    "Придётся ждать окончание уроков в слегка выбитом состоянии."
    "Пока не разберусь с Юри и Нацуки, не успокоюсь."
    stop noise_3 fadeout 3.0
    call window_close

    call window_dialog_long_transition("y")

    call window_open
    scene bg school library with dissolve_scene_full
    y "Снова ничего привлекательного..."
    "Конечно, я всё ещё читаю «Портрет Маркова», но нужно уже найти несколько книг на будущее..."
    "Или одну большую."
    "Но здесь ничто не цепляет мой взгляд..."
    "..."
    "Нет, я не могу сосредоточиться даже на этом!"
    "Стоит только задуматься, как сразу вспоминается Макс."
    "Он подозрительно добр и отзывчив."
    "А ещё хороший собеседник."
    "У меня таких людей, кроме семьи, Котонохи и Нацуки, в жизни не было..."
    "Клуб я тоже ценю!"
    "Но...{w}я не чувствовала себя такой раскрепощённой..."
    "И при такой близости--{nw}"
    k "{size=19}А, Юри, ты здесь.{/size}" with vpunch
    y "Э-э?!"
    show kotonoha happ cm ce at t11
    y "К-Котоноха!"
    show kotonoha oe
    play music yuri_romanticism fadein 3.0
    y "Привет..."
    show kotonoha om ce lup
    k "Не надо приветствий, мы уже здоровались в классе утром."
    show kotonoha cm ldown
    y "Точно..."
    show kotonoha om oe
    k "Вижу, снова ищешь, что почитать?"
    show kotonoha cm
    y "Да, но тут искать уже бесполезно..."
    show kotonoha om rhip
    k "Не переживай, можешь потом скататься вместе с мамой в библиотеку Токама{image=accent_low_register}{space=-15}чи -- там же гигантские стеллажи, точно найдётся что-то новое."
    show kotonoha neut om oe
    k "Жаль только, что она далеко расположена -- замучаешься добираться, особенно в одиночку."
    show kotonoha e1b
    k "Так ещё и билеты на Шинкансэ{image=accent_low_register}{space=-15}н ударят по кошельку..."
    show kotonoha cm oe
    y "Это я знаю..."
    show kotonoha om
    k "Выглядишь немного нервной."
    show kotonoha sad om oe rdown
    k "Что-то случилось?"
    show kotonoha cm
    y "А-а?"
    y "Ну..."
    show kotonoha happ om ce
    k "Юри, не переживай, я же твоя подруга, ничего никому не расскажу."
    show kotonoha cm
    y "У-у..."
    show kotonoha oe
    y "В общем..."
    y "К нам в Литературный клуб..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg school library
    show kotonoha happ cm oe at i11
    with wiperight
    y "Теперь я не могу перестать о нём думать..."
    show kotonoha omb ce
    k "Неужели у тебя появился парень?"
    show kotonoha cm
    y "Н-нет!"
    show kotonoha om oe
    k "Юри, ты влюбилась, признай это."
    show kotonoha cm
    y "Разве такое возможно за столь короткий срок?..."
    show kotonoha om
    k "Как видишь."
    show kotonoha e1b
    k "Некоторые умудряются и с первого взгляда пронзить себе сердце, а тут у тебя целых несколько дней в его компании."
    show kotonoha cm oe
    y "Умф..."
    show kotonoha om ce
    k "Даже и не знаю, что сказать."
    show kotonoha oe rhip
    k "Но тебе в любом случае нужно сделать первый шаг, пока есть такой шанс."
    show kotonoha cm
    y "..."
    show kotonoha om ce
    k "Юри, не стесняйся!"
    show kotonoha cm
    y "......"
    show kotonoha om oe lself
    k "О, знаю!"
    show kotonoha ldown rdown
    k "Ты видела вчера новость про то, как команда от одной специализированной школы взяла золото по какой-то там олимпиаде на федеральном уровне?"
    show kotonoha neut om oe
    k "Специализированной в плане того, что в этой школе обучаются ученики с различными физическими пороками."
    show kotonoha cm
    y "Э-э-э, да?"
    show kotonoha happ om oe lup
    k "Я запомнила, как один из участников признался в любви к своей девушке на камеру, зная, что она это посмотрит."
    show kotonoha neut om oe ldown
    k "Вся соль в том, что у него проблемы с сердцем."
    show kotonoha happ om ce
    k "Но он не побоялся общества и сделал такое волнительное, но важное признание в своей жизни!"
    show kotonoha oe lup
    k "Ты тоже так можешь, Юри!"
    show kotonoha ldown
    k "У тебя всё получится."
    show kotonoha cm
    y "Ух..."
    show kotonoha om rhip
    k "Всё, что тебе нужно, -- сделать первый шаг."
    show kotonoha e1b
    k "А там уже будет понятно по обстановке."
    show kotonoha cm oe
    y "...а если...."
    show kotonoha neut cm oe rdown
    y "Макс откажет?"
    show kotonoha happ om oe
    k "Значит, вместо отношений получишь полезный опыт."
    show kotonoha cm
    y "Опыт?..."
    show kotonoha om
    k "Да."
    show kotonoha sad omt ce
    k "Первый шаг может даться тяжело."
    k "Он может искалечить душу и сердце..."
    show kotonoha happ om oe lself rhip
    k "Но когда ты его сделаешь, то преодолеешь свой страх и будешь способна на очень многое."
    show kotonoha cm ldown
    y "Ты так думаешь?..."
    show kotonoha omb ce rdown
    k "Конечно!"
    show kotonoha oe
    k "Я верю в тебя, Юри!"
    show kotonoha ce
    k "Перед тобой никто не устоит!"
    show kotonoha cm
    y "Хорошо..."
    show kotonoha om oe lup
    k "Если понадобится помощь, то можешь обращаться в любое время."
    show kotonoha cm ldown
    y "Угу!"
    y "Спасибо, Котоноха..."
    show kotonoha om ce
    k "Не стоит, я лишь подметила сухие факты."
    show kotonoha cm oe
    y "Я...{w}попробую сегодня."
    show kotonoha omb
    k "Отлично!"
    show kotonoha ce lup
    k "Главное -- не сдавайся!"
    show kotonoha cm ldown
    stop music fadeout 3.0

    scene black with wipeleft_scene
    "Я стала чувствовать себя намного увереннее..."
    "У меня всё получится..."
    "У меня всё получится."
    "У меня всё получится!"
    call window_close

    call window_dialog_long_transition("mc")
    play noise_1 school_corridor_empty_noise fadein 3.0

    call window_open
    scene bg school new_class_mc day with dissolve_scene_full
    "..."
    "Да-да, снова в клуб."
    "Уже нет желания комментировать эту рутину в очередной раз."
    "..."
    "Прямо тишина здесь, непривычно без миссис Иды..."
    "Вроде бы она была на замене урока у какого-то класса, по словам другого учителя."
    "Хм, кстати, он уже ушёл..."
    "И никого не напрягает, что пустой кабинет просто взят и открыт нараспашку?"
    call window_close

    call plot_transition

    call window_open
    scene bg school old_corridor door with wipeleft_scene
    "Дверь..."
    "Надо открыть дверь..."
    call skip_block_on

    call screen club_door_lock_screen
    pause 0.5
    mc "Не понял..."
    call screen club_door_lock_screen
    pause 0.5

    call skip_block_off
    "..."
    "Я рано сюда пришёл?"
    "Да нет, примерно в то же время, что и в прошлые разы."
    "Через окно никого не видно..."

    scene bg corridor with dissolve
    "Ребят, не надо мне высасывать время."
    "У меня нет никакого удовольствия прожигать его, сидя в коридоре, когда я мог бы уже что-то сделать, чтобы пораньше освободиться."
    "..."
    "......"
    mc "{size=19}Да ну вас всех к чёрту...{/size}"

    scene bg school old_corridor wall with wipeleft_scene
    "Хотя чего я тут возмущаюсь?"
    "Особенно когда с утра хотел разобраться с Юри и Нацуки."
    "..."
    "Блин, такое ощущение, что я разделился на несколько частей, которые пытаются доминировать друг над другом с переменным успехом."
    "Вот, например, только что это возмущение."
    "Одна часть меня приняла Литературный клуб и уже успешно влилась в эту «бурную», если это так можно назвать, жизнь."
    "Другая...{w}будто не хочет ни под каким предлогом это принимать."
    "Всё ещё сопротивляется тому, что налаженный механизм распорядка дня не соответствует «стандартам» этой новой жизни."
    "...аргх, да что со мной такое?"
    "Почему у меня не получается быть проще?"
    "Я даже мысли изречь нормально не могу."
    "Всё куда-то в языковые дебри уходит..."
    "Вот, опять!"
    "Раздражает-то как..."
    show natsuki turned neut cm e1b school_bag at r11
    pause 0.7
    show natsuki om oe lhip rhip
    n "Ха."
    show natsuki fc neut cm oe
    mc "Странно, я ожидал увидеть кого-то другого в такую «рань»."
    show natsuki om
    n "Не поверишь, я тоже."
    show natsuki anno cm oe ldown
    mc "Там закрыто, если что."
    show natsuki om oe
    n "Думаешь, я не знаю?"
    n "Мне Моника не просто так ключи передала."
    show natsuki cm
    "Я и так не в духе, хватит издеваться."
    show natsuki neut cm oe
    mc "Она задержится?"
    show natsuki om oe
    n "Да, ненадолго."
    show natsuki cm oe
    mc "А другие где?"
    show natsuki om e1b rdown
    n "Без понятия."
    n "Сайори и Юри я не нашла."
    show natsuki oe
    n "И не вижу смысла искать: сами придут, никуда не денутся."
    show natsuki cm oe
    mc "Ясно."
    mc "Впускай тогда уж, надоело бесцельно торчать в коридоре."
    call window_close
    show natsuki ff e1b
    hide natsuki with easeoutleft

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show natsuki turned neut cm e1b at t44
    with wipeleft_scene
    mc "Насчёт вчерашнего..."
    show natsuki fc curi om oe at t11
    n "А?"
    show natsuki cm
    mc "Ты извини, я перестарался."
    show natsuki neut om oe
    n "А, это."
    show natsuki happ om oe lhip rhip
    n "Не парься, ты всё сказал правильно."
    show natsuki cm
    mc "М-м..."
    "Так-то да..."
    "Но неужто Нацуки так быстро переменилась?"
    show natsuki om
    n "Тщательно обдумав твои слова, я поменяла свою позицию по паукам."
    n "Как раз сегодня прочитаешь мой новый стих, увидишь."
    show natsuki cm
    mc "Хорошо."
    "Каким образом она успела мне так довериться?"
    show natsuki sedu om oe ldown rdown
    n "А пока никого нет..."
    show natsuki cm
    mc "...то что?"
    show natsuki happ om ce
    n "Поможешь мне с кладовкой."
    show natsuki oe
    n "Мне надо доразобрать новую мангу."
    show natsuki sad om oe
    n "Осталось там немного, но всё никак не доделаю начатое."
    show natsuki cm e1a
    mc "Ох, ладно..."
    show natsuki anno om oe
    n "Не умирай, ещё успеешь."
    show natsuki cm
    mc "И не планировал."
    show natsuki neut cm oe

    scene bg closet
    show natsuki turned fc neut cm oe at t11
    with wipeleft_scene
    show natsuki om lhip rhip
    n "Итак, твои основные задачи: подать мне ту коробку на полу и держать крутящийся стул."
    show natsuki anno cm oe
    mc "Два вопроса."
    show natsuki om ldown rdown
    n "...каких?"
    show natsuki neut cm oe
    mc "Первый: почему бы тебе не вынуть томики из коробки и поставить на полку?"
    show natsuki sedu om ce lhip rhip
    n "Потому что это лимитированная коробка для таких заядлых читателей-коллекционеров, как я."
    show natsuki neut cm oe
    mc "И что в ней такого?"
    show natsuki om ldown rdown
    n "Она уже выступает в роли полки для серии томов, которые шли в комплекте."
    show natsuki e1b
    n "Останется только поставить её туда, где есть свободное место."
    show natsuki angr cm oe
    mc "Так вынь всё, поставь, а потом обратно засунь."
    show natsuki om
    n "Я всё остальное разгребала, а до неё только сейчас добралась, умник!"
    n "К тому же мне лень, а тут ты прохлаждаешься."
    show natsuki cm
    mc "Окей, второй вопрос."
    show natsuki anno cm oe
    mc "Почему тебе не поменять стул?"
    show natsuki om lhip rhip
    n "А деревянные стулья умеют выдвигаться вверх?"
    show natsuki doub cm oe
    mc "А подложить что-нибудь?"
    show natsuki om
    n "Что?"
    n "Узкие томики манги, плоские глянцевые учебники?"
    n "Или тебя, может?"
    show natsuki cm
    mc "Я просто спросил."
    show natsuki om
    n "А я просто ответила."
    show natsuki cm ldown rdown
    mc "Ясно, проехали."
    show natsuki angr cm oe
    mc "Начинай свою операцию, злюка."
    show natsuki cross ff angr om ce
    n "Сам ты злюка!"
    show natsuki cm
    call window_close

    scene black with dissolve_cg
    pause 3.0

    call window_open
    play music t6
    mc "Ох..."
    "Здесь реально куча манги на полках..."
    mc "Да тут прям целая кладовка!"
    "{s}Не берём в расчёт, что сама кладовка в целых ~3 квадратных метра.{/s}"
    n "А то!"
    n "Так..."
    n "Аккуратно посередине..."
    n "Всё, я забралась, подавай коробку."
    mc "Сейчас..."
    "Не маленькая, как я думал..."
    "А ещё увесистая, зараза..."
    mc "Держи."
    n "Та-а-ак..."
    n "Есть."
    n "Теперь удерживай стул."

    if cg_a1_d4_n_1.unlocked == False:
        $ cg_a1_d4_n_1.unlock()
    scene n_cg2_bg
    show n_cg2_base
    with dissolve_cg
    mc "Знаешь, а здесь довольно уютно."
    n "Угу!"
    call window_close

    pause 1.5
    show n_cg2_exp2 at n_cg2_wiggle
    show n_cg2_base at n_cg2_wiggle
    pause 2.0

    call window_open
    n "Ай-яй-яй!"
    mc "Осторожно!"
    show n_cg2_exp1 at cgfade
    hide n_cg2_exp2
    n "Стул держи!"
    mc "Я это и делаю!"
    mc "Сама не крутись!"
    show n_cg2_exp3 at cgfade
    hide n_cg2_exp1
    n "Легко сказать..."
    call window_close

    pause 1.0
    hide n_cg2_exp3
    pause 3.0
    show n_cg2_exp2 at n_cg2_wiggle_loop
    show n_cg2_base at n_cg2_wiggle_loop
    pause 2.0

    call window_open
    mc "Чёрт тебя дери, Нацуки!"
    mc "Хорош крутиться!"
    n "{bt=7}Коробка тяжёлая!{/bt}"
    mc "Может, я лучше её возьму?!"
    n "{bt=7}Нет, это уже дело принципа!{/bt}"
    n "{bt=7}Ещё чуть-чуть и поставлю!{/bt}"
    n "{bt=7}Только держи этот дурацкий стул!{/bt}"
    mc "Да держу я, держу!"

    scene black with dissolve_cg
    n "{bt=7}Ещё немножко!...{/bt}"
    n "{bt=7}...{/bt}"
    n "Ура!"
    n "Получилось!"
    mc "Фух..."
    n "Вздыхаешь так, будто бомбу обезвредил!"
    mc "С тобой никакая бомба не сравнится..."
    n "Это комплимент?"
    mc "Считай, как хочешь."
    n "Тогда...{w}спасибо..."
    "Честное слово, она странная."
    n "Эй, тут есть один прикольный томик."
    n "Не хочешь глянуть?"
    mc "Ну давай уж, всё равно пока никто не пришёл."
    n "Только сейчас...{w}дотянусь..."
    mc "О, нет..."
    n "Ай."
    mc "Не..."
    n "Ай!"
    mc "Надо..."
    n "Схватила!--{nw}"
    mc "Трясти-и-ись!--{nw}"
    n "А-А-А-А-А-А!--{nw}"
    "РУКИ ЗА ЗАТЫЛОК--{nw}"
    call window_close

    stop music
    play sound fall2
    pause 3.0

    call window_open
    mc "Ох-х-х, твою мать..."
    "Вовремя я руки под себя подложил..."
    "Иначе бы треснулся знатно..."
    n "Ты в порядке?!"
    mc "А ты?!"
    n "Значит, в порядке."
    "Моя спина...{w}вдавливающаяся в пол всем телом Нацуки, которая совершенно не норовит слезть с меня."
    mc "Эй..."
    mc "Возможно, это прозвучит грубо..."
    mc "Но я рад, что ты «плоская»."
    n "Ч-что...{w}что ты только что сказал?!"
    mc "Меня бы расплющило, будь всё иначе, ха-ха-ха!"
    n "{sc=2}БАКА-А-А!!!{/sc}"
    mc "Ай..."
    "..."
    "...она меня один раз слегка ударила в грудь и сильнее сжала всем телом."
    "Что с ней сегодня происходит?"
    mc "Ты меня сейчас раздавишь."
    n "Нет."
    mc "И вообще, может, встанешь?"
    n "Н-нет..."
    mc "Почему?"
    n "Я...{w}не хочу..."
    mc "Нацуки, что с тобой случилось?"
    n "..."
    n "Пожалуйста...{w}дай мне полежать ещё чуть-чуть..."
    n "Мне давно не было так приятно и спокойно..."
    mc "Да мне не жалко, но...{w}ты на себя не похожа."
    n "Плевать..."
    mc "А если кто-то увидит?"
    n "Плевать..."
    n "Они знают, как у меня всё плохо."
    n "Они поймут..."
    mc "Что-то я в этом не уверен..."
    "Спрашить её сейчас напрямую о проблеме точно тупо."
    "Всё-таки придётся ждать Монику..."
    window hide

    pause 5.0

    window auto
    "Да ну, она задремала?"
    "Не прошло и минуты."
    "Либо она делает вид, что спит."
    "Хотя зачем..."
    "..."
    "Блин, неудобно-то как..."
    "Когда на тебе спит кто-то тёплый и компактный, это прикольно, но под спиной у меня паркетный пол."
    "А ещё ремень, который впился в мою талию."
    "Лишь бы тело не затекло..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    y "Э-э-э?!"
    "Приехали..."

    scene bg school literature_club board day
    show layer master:
        anchor (0.2, 0.3) zoom 1.5 rotate 180
    show yuri turned lsur cm oe at i11:
        ypos 1.35
    with dissolve_scene_full
    show yuri om oe
    y "Макс?..."
    show yuri cm oe
    mc "Она ставила коробку."
    mc "Я держал стул."
    mc "Потом она нашла какой-то томик, решила его взять."
    mc "Взяла."
    mc "Но на меня навернулась."
    mc "А я..."
    mc "Упал, провалялся, ты перед глазами."
    show yuri anno om oe lup rup
    y "У...{w}угу..."
    show yuri neut cm e1d
    mc "Я всё ещё не понимаю, что с ней творится."
    show yuri ldown rdown
    mc "Моника скоро подойдет?"
    show yuri dist om oe
    y "Н-не знаю, я никого не встретила..."
    show yuri cm oe
    mc "Эх, понятно..."
    "Куда ж вы все запропастились?"
    show yuri neut cm e1d
    mc "Я пока попробую разбудить Нацуки."
    show yuri om
    y "Хорошо..."
    show yuri flus cm oe
    y "А я займусь...{w}перечитыванием своего стиха...{w}н-нет, мне надо в уборную..."
    hide yuri with easeoutright
    pause 1.0
    "...почему Юри такая нервная?"
    "Да что тут вообще творится?!"

    scene black with dissolve
    pause 0.25
    "Так..."
    mc "Эй, Нацуки."
    mc "Нацуки."
    mc "Нацуки!"
    n "Мф-ф-ф..."
    mc "Вставай, давай, доброе утро, кто-то там томик обещал!"
    n "О-о-о..."

    scene bg closet
    show natsuki turned neut cm e0a at t11
    with dissolve_scene_full
    show natsuki om
    n "Сколько я проспала?..."
    show natsuki cm
    mc "Недолго."
    show natsuki om
    n "И что было, пока я была без сознания?"
    show natsuki cm oe
    mc "Нас заметила Юри, которой я всё постарался объяснить."
    show natsuki curi cm oe
    mc "Сейчас она ушла в туалет."
    show natsuki om e1c
    n "Надеюсь, она не напридумывала у себя в голове лишнего..."
    show natsuki cm
    "И этот человек утверждал, что все всё правильно поймут."
    show natsuki flus cm oe
    n "Ладно, где томик..."
    show natsuki happ om ce lhip rhip
    n "О, вот, держи!"
    show natsuki cm

    if cg_a1_d4_n_2.unlocked == False:
        $ cg_a1_d4_n_2.unlock()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    play music t6
    "Не видел раньше такого..."
    "На обложке красуется арт в киберпанковском стиле."
    "Высотки по бокам с неоновыми вывесками, дождь, мокрый асфальт, который отражает весь падающий на него свет..."
    "Но примечательны тут два единственных персонажа по центру."
    "Первый похож на какого-то высокотехнологичного боевого андроида с механическим телом и с черным гладким и угловатым по форме стеклом на лице."
    "Сам андроид стоит в агрессивной стойке, будто готов наброситься на самого читателя."
    "Вместо рук у него импланты, смахивающие на лапы богомола, дополненные лезвиями и прочей оружейной приблудой."
    "Наверное, они трансформируются, а не постоянно в таком виде находятся."
    "Второй персонаж -- стоящая за спиной полубоком голограмма девушки в школьной форме японского фасона с длинными каштановыми волосами, завязанными в хвост белым бантом."
    "Стойте..."
    "Она подозрительно смахивает на Монику..."
    mc "Необычные персонажи..."
    show n_cg1_exp1 at cgfade
    n "Есть в них что-то цепляющее, да?"
    mc "Ага..."
    mc "Тебе эта голограмма не напоминает Монику?"
    hide n_cg1_exp1
    n "А?"
    show n_cg1_exp2 at cgfade
    n "Хм..."
    n "Похожа..."
    hide n_cg1_exp2
    n "Хотя нет, отличия имеются, даже в цвете волос."
    show n_cg1_exp1 at cgfade
    n "Но если бы Моника занималась косплеем, то могла бы спокойно взять этого персонажа!"
    mc "Наверное..."
    hide n_cg1_exp1
    mc "А в чём, примерно, сюжет заключается?"
    show n_cg1_exp2 at cgfade
    n "Я ещё толком не читала, знаю только самое начало...{w}и весь сюжет частично..."
    mc "Всё равно расскажи."
    window hide
    hide n_cg1_exp2
    n_nvl "Существовало множество различных корпораций, которые яростно конкурировали друг с другом." with Dissolve(0.5)
    show n_cg1_exp2 at cgfade
    n_nvl "Не помню, на территории какой страны...{w}да и неважно."
    n_nvl "В этой вселенной само государство распалось, власть перешла корпорациям из-за их сильного влияния на общество."
    n_nvl "Но никто из них не хотел разделять её между собой."
    hide n_cg1_exp2
    n_nvl "Сначала корпорации сражались друг с другом экономически в различных сферах, когда государство было цело."
    n_nvl "После его развала пали официальные законы, а вместе с ним и ограничения, которые сдерживали корпорации от открытых конфликтов с применением оружия."
    n_nvl "И вот, спустя некоторое время произошёл скачок в технологиях."
    n_nvl "Научный отдел корпорации..."
    show n_cg1_exp2 at cgfade
    n_nvl "Угх, не помню названия...{w}что-то на «А»..."
    hide n_cg1_exp2
    show n_cg1_exp5 at cgfade
    n_nvl "...разработал новые устройства: чипы, импланты и прочие гаджеты, -- которые устанавливались прямо в тело."
    n_nvl "Большинство из них были дорогими, но зато они давали сильные способности и массу новых возможностей."
    n_nvl "Таким образом, грызня за власть началась сильнее."
    n_nvl "Воровство технологий, широкие и яростные конфронтации, заказные убийства и прочие радикальные меры борьбы..."
    hide n_cg1_exp5
    n_nvl "Однако среди этой мешанины были два основных гиганта: как раз эта «А» и ещё «Б»."
    show n_cg1_exp2 at cgfade
    n_nvl "У этой корпорации я тоже не помню название, поэтому просто «Б»."
    hide n_cg1_exp2
    n_nvl "Так вот, в таком жестоком мире жил один {color=#fc7e23}IT{/color}-инженер."
    n_nvl "Причём жил вполне обеспеченно: квартира в красивом небоскрёбе, высокооплачиваемая работа в корпорации «Б»..."
    show n_cg1_exp5 at cgfade
    n_nvl "...но личная жизнь была скудной, если не пустой: у инженера абсолютно не было ни друзей, ни отношений, -- никого вообще!"
    n_nvl "Практически всё своё время он пробыл в одиночестве."
    nvl hide Dissolve(0.5)
    window auto
    mc "Ох..."
    hide n_cg1_exp5
    show n_cg1_exp2 at cgfade
    n "Да, это отвратительно, когда ты никому не нужен и когда никто тебя не поддержит."
    window hide
    hide n_cg1_exp2
    n_nvl "В общем, с психологическим здоровьем у него были серьёзные проблемы." with Dissolve(0.5)
    show n_cg1_exp5 at cgfade
    n_nvl "Всю свою взрослую жизнь он проживал по инерции, каждый день угасая всё сильнее и сильнее, не в силах что-либо поменять..."
    nvl hide Dissolve(0.5)
    hide n_cg1_exp5
    show n_cg1_exp3 at cgfade
    window auto
    mc "...но?"
    n "Да, \"но\"."
    window hide
    hide n_cg1_exp3
    n_nvl "Мир решил добить его окончательно." with Dissolve(0.5)
    n_nvl "Однажды по пути домой на одной из улиц он угодил в военную стычку между корпорациями «А» и «Б»."
    n_nvl "Из этой потасовки он спастись не успел: его жизненно важные органы были прострелены в кашу."
    nvl hide Dissolve(0.5)
    window auto
    mc "Мда..."
    show n_cg1_exp2 at cgfade
    n "Ага."
    hide n_cg1_exp2
    n "А ирония этой ситуации заключается в том, что выстрелы прилетели со стороны солдат «Б»."
    window hide
    n_nvl "Мозг инженера со встроенным чипом сохранения сознания, к удивлению, оказался цел, однако времени на оживление было в обрез." with Dissolve(0.5)
    n_nvl "А поскольку сам главный герой был достаточно ценным сотрудником, солдаты «Б» оперативно доставили его в реанимацию."
    show n_cg1_exp5 at cgfade
    n_nvl "Тело восстановить не удалось."
    n_nvl "Тогда было решено использовать экспериментальное тело андроида, к разработке которого, кстати, инженер и приложил руку."
    n_nvl "Чип с сознанием извлекли, подключили к новому телу."
    n_nvl "Так у него началась новая жизнь."
    hide n_cg1_exp5
    n_nvl "Он стал первым человеком-андроидом, привлеча тем самым внимание киберпсихологов, изучающих влияние имплантов на психику."
    show n_cg1_exp5 at cgfade
    n_nvl "Прошёл где-то месяц."
    n_nvl "На главном герое решили протестировать новоиспечённый боевый имплант -- «Клинки богомола»."
    n_nvl "Киберпсихологи выступили против этой идеи как со стороны морали, так и со стороны уникальности пациента, но интересы корпорации были выше."
    hide n_cg1_exp5
    show n_cg1_exp2 at cgfade
    n_nvl "Ей нужны были новые солдаты, а не ковыряние в мозгах."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n_nvl "И очень зря: все импланты в той или иной степени выводят рассудок из строя."
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n_nvl "Из-за этого может развиться киберпсихоз."
    n_nvl "Психическая болезнь, сопровождающаяся внезапными припадками агрессии, сбитым восприятием окружения и так далее..."
    hide n_cg1_exp2
    show n_cg1_exp5 at cgfade
    n_nvl "Что позже и случилось с главным героем..."
    n_nvl "А в совокупности с новым имплантом и телом он поневоле превратился в нестабильную машину для убийств."
    n_nvl "В этот момент главный герой осознал, до чего довел его корпораторский мир, и перестал надеяться на кого-либо вообще."
    n_nvl "В одном из тестирований тела он взбунтовался и сбежал, хоть и с трудом."
    n_nvl "Теперь герой снова оказался в одиночестве, только в этот раз полнейшим изгоем с невероятной ненавистью к корпорациям."
    nvl hide Dissolve(1.0)
    nvl clear
    window auto
    mc "Эй, а голограмма?"
    n "Он встретит её не сразу."
    n "Только когда окажется в комплексе корпорации «А» вместе с какой-то бандой..."
    n "Искуственный интелект и образ этой голограммы будут перенесены в чип, который главный герой подключит к себе."
    n "В итоге, девушка станет его напарником и даже спутником по жизни."
    mc "Весело..."
    hide n_cg1_exp5
    show n_cg1_exp1 at cgfade
    n "Она всё время будет переубеждать его взгляды на жизнь, доказав тем самым, что существует истинные чувства, счастье и настоящая любовь, которых он достоин."
    n "От неё, естественно, ха."
    n "В конце концов, как я себе проспойлерила, своего она добьётся."
    n "Но это только подогрело мой интерес."
    hide n_cg1_exp1
    show n_cg1_exp2 at cgfade
    n "Так что вот такой сюжет, если крайне кратко его пересказывать."
    hide n_cg1_exp2
    mc "Даже так, это очень впечатляет."
    mc "Может, когда-нибудь будет свободное время, тоже куплю себе эту мангу."
    n "Она недорогая, но залипательная."
    mc "И всё-таки..."
    mc "Не думал, что тебе будет нравиться что-то подобное."
    show n_cg1_exp1 at cgfade
    n "Внешность обманчива, да?"
    mc "Ха, точно."
    hide n_cg1_exp1
    show n_cg1_exp2 at cgfade
    s "Приве-е-ет~"
    m "Ого, ребята, вы все в сборе?"
    n "Эх, пора закругляться..."
    mc "Жаль..."

    scene bg closet
    show natsuki turned fc happ cm oe at t11
    with dissolve_cg
    mc "Спасибо за посиделку."
    stop music fadeout 3.0
    show natsuki om
    n "Спасибо, что не скинул меня."
    show natsuki cm
    mc "Ха-ха!"
    show natsuki om ce
    n "Ха-ха-ха!"
    play music t5 fadein 3.0
    show natsuki cm ce at t22
    show sayori turned happ cm oe at l21
    pause 0.7
    show sayori om
    s "Ребят, чего смеётесь?"
    show natsuki cm oe
    show sayori ce lup rup at h21
    s "Я тоже хочу!"
    show sayori cm ce ldown rdown
    mc "Да так, ничего интересного."
    show sayori angr om oe
    s "Враки!"
    show sayori cm oe
    mc "У собаки."
    show sayori om oe
    s "У собаки нету враки!"
    show sayori cm oe
    show natsuki neut cm oe
    mc "Стоп."
    show sayori vsur cm oe
    show natsuki laug cm oe
    mc "Это что, печенье на той парте?"
    show sayori om oe
    hide sayori with easeoutleft
    s "ГДЕ?!"
    show natsuki cm ce

    scene black with wipeleft_scene
    "Проще простого."
    s "ВРАКИ!"
    "Хоть и коварно..."
    "Кстати, а когда Юри успела вернуться?"
    "Я её вообще не заметил."
    "Сидит с листком стиха так, будто угасла..."
    "Тогда разберусь с ней при обмене."
    "Где там моё творение..."
    "..."
    "Есть, вот оно."

    scene bg club_day
    show monika forward happ cm oe at t43 zorder 2
    with wipeleft_scene
    show yuri shy neut cm oe at t41
    show sayori turned neut cm oe at t42
    show monika happ om oe lpoint rhip
    show natsuki turned happ cm oe at t44
    m "Итак, друзья!"
    show yuri at s41
    show monika ldown rdown
    show sayori happ cm oe
    m "Время делиться стихами!"
    show monika cm oe
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    pause 0.2
    stop music fadeout 3.0
    show yuri e1
    show monika neut om oe
    m "Но перед этим..."
    show sayori turned neut cm oe at t42
    show natsuki turned neut cm oe at t44
    m "...ещё одно объявление."
    show monika happ om ce n2 lpoint
    m "Я выйду на минутку с Максом, хочу с ним кое-что обсудить."
    show monika cm ce ldown
    "Так, вот сейчас уже неприкольно."
    "Но мне это на руку."
    mc "Хорошо..."
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school old_corridor wall
    show monika forward neut cm oe at t11
    with wipeleft_scene
    show monika flus om oe
    m "Извини, что так резко..."
    show monika cm e1a
    mc "Всё нормально, Моника."
    mc "Лучше скажи, что случилось."
    show monika om oe
    m "Я думаю, ты и сам уже заметил."
    show monika cm e1a
    mc "Юри?"
    show monika om
    m "Да."
    m "Не знаешь, что с ней?"
    show monika cm
    mc "Без понятия, сам хотел спросить."
    mc "Она на себя не похожа."
    show monika om oe
    m "Согласна, что-то её сдавливает..."
    show monika e1a
    m "Я пыталась выяснить, почему, но всё тщетно, не хочет раскрываться."
    show monika neut cm oe
    mc "Попробую с ней поговорить, когда дойдёт очередь."
    show monika om ce
    m "Спасибо, Макс."
    show monika om oe
    m "Я знала, что на тебя можно рассчитывать."
    show monika happ cm oe
    mc "Такими темпами тебе придётся сделать второй пост вице-президента клуба."
    show monika om ce
    m "Ха-ха, да!"
    show monika cm oe
    mc "Ладно, пока мы здесь, можно узнать одну вещь?"
    show monika om oe
    m "Конечно, какую?"
    show monika neut cm oe
    mc "Ты обещала рассказать про Нацуки."
    show monika flus mb oe
    m "Ой, точно..."
    show monika neut om ce
    m "В общем..."
    show monika om oe
    m "У неё серьёзные проблемы в семье."
    m "Причём это мягко сказано..."
    show monika cm oe
    mc "Я уже догадался."
    mc "Так в чём конкретно они выражены?"
    show monika flus om oe
    m "Родители Нацуки часто конфликтовали между собой."
    m "Отец из-за каких-то проблем с работой плохо зарабатывал, а податься куда-то ещё он не мог -- не было выбора."
    show monika neut om oe
    m "Хотя жить кое-как на заработанные средства можно было."
    show monika dist om oe
    m "Мать чем дольше с ним жила, тем больше его ненавидела."
    show monika flus om oe
    m "Они часто кричали друг на друга из-за всяких конфликтов..."
    show monika curi md oe
    mc "Подожди, но ведь было что-то первопричиной этому?"
    show monika neut cm oe
    mc "Не внезапно же они начали ссориться."
    show monika dist om oe
    m "Честно, ничего про это не знаю."
    show monika neut om oe
    m "Я лишь пересказываю то, что поведала мне сама Нацуки."
    show monika cm oe
    mc "Хорошо, продолжай..."
    show monika om oe lpoint
    m "Один раз их конфликт достиг предельной точки."
    show monika ldown
    m "Мать решила съехать."
    m "Подала на развод."
    m "Было судебное разбирательство имущества и родительских прав."
    show monika cm oe
    mc "Короче говоря, с кем останется Нацуки?"
    show monika om oe
    m "Да."
    m "И она хотела остаться с матерью."
    show monika om ce
    m "Всё могло бы закончиться на этой ноте."
    m "Но в процессе этих разборок мать попала в аварию на каршеринговом автомобиле."
    m "На перекрёстке в неё справа влетел мини-грузовик."
    m "Прямо в водительское сиденье."
    show monika cm ce
    mc "Чёрт побери..."
    show monika om oe
    m "Помимо различных переломов у неё было повреждение головы..."
    m "В общем, её сразу привезли в госпиталь «Ни{image=accent_low_register}{space=-15}ши-Ниига{image=accent_low_register}{space=-15}та Тю{image=accent_low_register}{space=-15}о», где диагностировали состояние как тяжёлое."
    show monika flus om oe
    m "Врачи думали, что мать Нацуки останется инвалидом на всю жизнь."
    show monika neut om oe
    m "Но, к счастью, современная медицина победила: сейчас она очень медленно, но верно идёт на поправку, находясь в том же госпитале."
    m "Нацуки раз в две недели по выходным самостоятельно её навещает, а отец вообще этого не делает."
    m "Эта трагедия по нему сильно ударила, хоть он и часто ругался со своей женой..."
    show monika dist om oe
    m "Он так сильно винит себя за свою никчёмность, что просто не смог снова показаться ей на глаза."
    show monika neut cm oe
    mc "Да ему психиатр, блин, нужен."
    show monika om oe
    m "Вот-вот."
    m "Но вместо обращения за помощью, может, из-за бедности и собственных комплексов, отец стал пить."
    m "Нечасто, да, но до такой степени, что его пробивает на некотролируемую агрессию."
    m "А выплёскивал он её на всё, что было под рукой."
    show monika flus om oe
    m "...в том числе и на Нацуки..."
    show monika cm e1a
    mc "Своего рода, домашнее насилие?"
    show monika om
    m "...угу."
    show monika lpoint
    m "Вместе с этим он решил взять себя в руки и стать «ответственным» отцом."
    show monika worr om oe ldown
    m "И как ты можешь понять, получилось у него это, мягко говоря, не очень..."
    show monika neut om oe
    m "Он стал строже относиться к Нацуки."
    m "Поэтому, как раз, вся манга перекочевала к нам в клуб."
    show monika neut cm oe
    mc "А почему же тогда снова не подать в суд, только в этот раз за побои, предоставив компромат?"
    show monika curi cm oe
    m "А кто это сделает?"
    show monika neut om oe lpoint
    m "Дом частный, близких соседей нет."
    m "Родственников тоже, по крайней мере, неизвестно, что там вообще с ними, связи нет."
    m "Сама Нацуки не знает, что делать, ей страшно."
    show monika om ce ldown
    m "И даже если кто-то подаст в суд и она его выиграет..."
    show monika curi cm oe
    m "Куда ей деваться?"
    show monika neut om oe lpoint
    m "Дом закреплён за отцом, а она прав на него не имеет."
    m "Родственников, которые могли бы взять её к себе, нет."
    show monika dist om oe ldown
    m "Мы тоже не можем взять Нацуки: у меня родители не разрешают, другие обеспечить не смогут."
    m "Нет, я понимаю, что ей недавно стало 18, может сама выбирать, где жить, но самого выбора нет от слова совсем."
    show monika neut om oe
    m "Разве что единственный вариант -- это туда, куда мать хотела её отвести, но..."
    show monika dist om oe
    m "Нет, это тоже не рассматривается, потому что нужно переделывать кучу документов."
    show monika neut om oe
    m "В итоге, остаётся ждать, когда её мать полностью выздоровеет, а это случится нескоро."
    m "Она в ловушке, Макс."
    show monika cm oe
    mc "Мда..."
    mc "Это так оставлять нельзя."
    show monika flus om e1a
    m "Я знаю, но что мы можем сделать?..."
    show monika oe
    m "Мы всего лишь жалкая горстка учеников старшей школы."
    show monika cm
    "Как бы отвратительно это ни звучало...{w}но Моника права, мы ничего не можем."
    show monika e1a
    mc "Как минимум поддержать её морально и материально."
    show monika mb oe
    m "Уже это делаем, хах..."
    show monika om e1a
    m "Но сильно ситуация от этого не меняется."
    show monika cm
    mc "Наша помощь всё равно важна, даже в таком ущербном виде."
    show monika neut cm oe
    mc "Пусть мы только и можем её реализовать, но зато Нацуки будет держаться."
    show monika dist om oe
    m "Ты прав..."
    show monika neut cm oe
    mc "А тогда почему она ненавидит «милоту» в свой адрес?"
    show monika om lpoint
    m "Я уверена, что это её защитный комплекс."
    show monika ldown
    m "Она хочет, чтобы её воспринимали всерьёз, считались с ней на равных."
    show monika dist om oe
    m "В общем, отец её довёл..."
    show monika cm oe
    mc "Теперь всё понятно."
    show monika neut cm oe
    mc "Спасибо, что рассказала, Моника."
    show monika om ce
    m "Не стоит."
    show monika happ cm oe
    mc "Ладно, пора возвращаться, а то нас уже заждались, наверное."
    show monika om ce lpoint
    m "Ты снова прав, ха-ха!"
    show monika cm ce ldown
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    play music t5 fadein 3.0
    scene bg club_day
    show monika forward happ cm oe at t42
    with wipeleft_scene
    show monika om ce lpoint
    m "Мы снова здесь!"
    show monika cm ce ldown
    m "..."
    show monika neut cm oe
    m "..."
    mc "Они там что-то бурно обсуждают..."
    show monika dist om oe
    m "Хотя бы Юри уже не такая грустная."
    show monika cm oe
    mc "Это точно."
    show monika happ om oe at t11
    m "Раз они там, то покажешь мне свой стих?"
    show monika cm oe
    mc "С удовольствием."
    call window_close

    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show monika e1b
    pause 4.0
    show monika neut cm
    pause 4.0
    show monika vsur cm e2b
    pause 6.0
    show monika om

    call window_open
    m "Поразительно..."
    show monika happ om ce
    m "Макс, ты продолжаешь меня радовать!"
    show monika cm ce
    mc "Да?..."
    show monika om oe
    m "Абсолютно!"
    show monika om e1b
    m "Мне очень понравилась часть с описанием камней, она у тебя шикарно получилась!"
    show monika nerv mb oe
    m "Остальная, конечно, растянута и довольно нескладна..."
    show monika happ om oe
    m "Как я поняла, ты пытался скопировать стиль Юри досконально?"
    show monika cm oe
    mc "Ну да, а как ещё?"
    mc "Сначала было тяжело, но когда вошёл в раж, то слова сами ложились на бумагу."
    show monika om ce
    m "И это тебе надо зафиксировать."
    show monika om oe
    m "Немного подогнав стиль под себя, ты с лёгкостью стал двигаться по «сюжету»."
    show monika cm oe
    mc "Я заметил."
    show monika om ce
    m "Что ж, отлично!"
    show monika cm ce
    play sound paper_torn_out
    show monika ldown with dissolve
    pause 1.0
    show monika lean happ om oe at h11
    m "Но можно узнать одну вещь?"
    show monika cm oe
    mc "Копируешь мои слова?"
    show monika forward happ om ce
    m "Ха-ха-ха!"
    show monika cm ce
    mc "\"Конечно, какую?\""
    show monika om e1b
    m "Эти камни..."
    show monika om oe
    m "...за ними закреплены живые образы, не так ли?"
    show monika cm oe
    mc "В точку."
    mc "Вышло это сумбурно..."
    show monika om
    m "Интересно..."
    show monika ce
    m "Но ты точно попал с описанием участниц и меня в частности."
    show monika cm
    mc "Вот так прямо попал?"
    show monika om oe
    m "Да."
    show monika sedu om ce
    m "Может быть, ты начинаешь нами проникаться, хе-хе?"
    show monika ma oe
    mc "А-а..."
    show monika neut om oe
    m "Э..."
    show monika worr mb oe n2 at s11
    m "Да, это прозвучало немного странно..."
    show monika ce
    m "Я что-то от радости за твой стих разыгралась..."
    show monika ma
    mc "Ладно, бывает."
    show monika happ cm oe n1 at t11
    mc "У меня самого периодически такое случается, главное, себя в руках держать."
    show monika om e1b
    m "Да, надо."
    show monika cm oe
    mc "Что ж, теперь твоя очередь."
    show monika om oe lpoint
    m "А, точно!"
    show monika om ce ldown
    m "Держи."
    show monika cm ce
    call show_poem(poem_m3)
    "Орхидея?"
    "Мне нравятся подобные необычные цветы."
    show monika cm oe
    mc "Как человек, который симпатизирует этому виду растений, скажу: ты в точности описала орхидеи."
    show monika lean happ om ce at h11
    m "Льстишь!"
    show monika cm ce
    mc "А вот и нет."
    show monika om oe at h11
    m "А вот и да!"
    show monika cm oe
    mc "Снова разыгралась?"
    show monika forward happ om ce
    m "Да, ха-ха!"
    show monika om oe
    m "В общем, спасибо за похвалу!"
    show monika cm oe
    mc "Всегда пожалуйста."
    play sound paper_torn_out
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    pause 1.0
    show monika om oe lpoint
    m "Приму её за комплимент."
    show monika ce ldown
    m "И описание с изумрудом тоже."
    show monika cm
    mc "У тебя сердце не разорвётся от такого количества?"
    show monika om oe
    m "Для твоих слов всегда найдётся место."
    show monika cm
    mc "Неужто ты мне так доверяешь?"
    show monika cm
    mc "Ведь мы за всё время виделись и общались суммарно неделю..."
    show monika om oe
    m "Важно не сколько мы встречались, а как хорошо друг друга понимаем."
    show monika laug mb oe
    m "Хоть я о тебе пока мало знаю, но этого достаточно, чтобы понять, что ты хороший человек."
    show monika neut cm oe
    mc "Я бы не сказал, что я хороший, совершенно..."
    show monika happ om oe lpoint
    m "У всех есть своя тёмная сторона, Макс."
    show monika ldown
    m "Невозможно быть полностью «светлым»."
    show monika neut cm oe
    mc "Даже так..."
    show monika om oe lpoint
    m "Ты должен акцентироваться на позитивных вещах."
    show monika lean happ om oe at h11
    m "Если ты не будешь этого делать, то я помогу тебе с этим, даже против твоей воли."
    show monika cm oe
    mc "Спасибо, сам как-нибудь..."
    mc "Пойду пока покажу свой стих другим."

    scene black with wipeleft_scene
    "...мда, сегодня невероятно странный день."
    "Нацуки с непонятным поведением, забитая Юри и Моника со своими полуромантическими «наездами»."
    "Вообще с каких пор я стал кого-то привлекать?"
    "Внешность никакая, тем для общения -- кот накакал..."
    "Да даже коты гадят больше."
    "Эта заинтересованность Моники всё больше вводит меня в диссонанс."
    mc "О..."
    "Сайори увела Юри в сторону, они там со стихами копошатся."
    "Вот и хорошо, пусть немного зарядит её своим позитивом."
    "А я пока разберусь с Нацуки."

    scene bg closet
    show natsuki turned fc pout md oe at t11
    with wipeleft_scene
    mc "А вот и я."
    show natsuki om
    n "Макс, с Юри и правда что-то не так."
    show natsuki cm
    mc "Да-да, я это уже обсудил с Моникой."
    mc "Разберусь с этим, когда дойдёт очередь."
    show natsuki sad om oe
    n "Просто мы с Сайори пытались её немного развеселить, а она ни в какую..."
    show natsuki cm
    mc "Ясно."
    show natsuki neut cm oe
    mc "Давай пока сменим тему."
    mc "Почитай."
    call window_close

    play sound paper_torn_out
    show natsuki lup poem_paper with dissolve
    pause 1.0
    show natsuki ff e1b
    pause 6.0
    show natsuki e2b
    pause 8.0
    show natsuki neut cm oe
    pause 0.5
    show natsuki om oe

    call window_open
    n "Это ещё лучше, чем в прошлый раз."
    show natsuki e1b
    n "И интереснее..."
    n "Камни прикольные."
    show natsuki md
    mc "Знал, что ты обратишь на них внимание."
    show natsuki om
    n "Рубин особенно."
    show natsuki md
    mc "Хм..."
    show natsuki flus cm oe
    n "Он просто...{w}интересен мне в некоторой степени."
    show natsuki dist om oe
    n "Или не так, не знаю, как сказать..."
    show natsuki neut om oe
    n "Но что-то в нём есть такое."
    show natsuki cm oe
    mc "Рад, что тебе понравилась эта часть."
    show natsuki om oe
    n "Короче, стих прикольный."
    show natsuki cm oe
    play sound paper_torn_out
    show natsuki ldown with dissolve
    pause 1.0
    show natsuki fc happ om oe lhip rhip
    n "А теперь вот, то, что я обещала тебе показать."
    show natsuki cm
    call show_poem(poem_n3)
    show natsuki curi cm oe
    mc "Удивительно..."
    "Удивительно, что я смог вот так взять и повлиять на кого-то без задней мысли..."
    show natsuki om oe ldown rdown
    n "Что?"
    show natsuki neut cm oe
    mc "Не думал, что ты резко поменяешь свою позицию на правильную."
    show natsuki om
    n "Было бы глупо упираться в неправильную."
    show natsuki cm
    mc "Но всё-таки некоторые люди так делают, даже если они знают, что это ложь."
    show natsuki nerv cm ce
    mc "Так что твоё осознание и исправление ошибки заслуживает уважения."
    show natsuki om
    n "Cпасибо..."
    show natsuki cm
    mc "Хороший стих."
    mc "Возвращаю."
    play sound paper_torn_out
    stop music_poem fadeout 6.0
    pause 1.0
    "Юри всё ещё оккупирована, так что можно немного поговорить."
    mc "Мне, кстати, интересно..."
    show natsuki curi om oe
    n "А?"
    show natsuki neut cm oe
    mc "А как ты вообще попала в Литературный клуб?"
    show natsuki om
    n "А..."
    show natsuki happ om oe
    play music t6
    n "Ха..."
    show natsuki ce lhip rhip
    n "Ха-ха!"
    show natsuki oe
    n "Дело было так..."
    call window_close

    call window_dialog_fast_transition("n")

    $ currentpos = get_pos(channel="music")
    $ audio.t6o_1 = "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    stop music
    play music t6o_1

    call window_open
    scene bg school new_class_natsuki day
    show gray zorder 1:
        alpha 0.25
    show vignette zorder 2:
        alpha 0.5
    n "В прошлом году я числилась в Клубе выпечки."
    n "Но пришлось его покинуть и выбрать новый."
    mc "Почему?"
    n "Лидер сменился."
    n "При старом всё было хорошо: дружный коллектив, атмосфера..."
    n "Но единственная проблема заключалась в том, что состав клуба был из учениц второго года старшей школы, а сам лидер -- третьего."
    n "Плюс у неё что-то там было очень серьёзное в личной жизни."
    n "Поэтому она выпустилась из школы раньше положенного, а на смену пришла фифа с большим мнением о себе!"
    n "Видите ли, у неё есть предрасположенность командовать..."
    n "Чем только другие думали, когда её выбирали..."
    mc "Классика."
    n "Ага, только из-за этой «классики» мы развалились."
    n "Нас было человек 10, а осталось 4."
    n "На момент моего ухода, по крайней мере..."
    mc "Да уж..."
    n "Кстати, Эми до сих пор состоит в этом клубе."
    mc "Да?"
    n "Угу."
    mc "Вы уже помирились?"
    n "...да мы и не ссорились..."
    mc "То есть ты просто свои мысли в стихи заложила?"
    n "Ну да, нельзя?"
    n "И вообще, не съезжаем с темы..."

    play noise_1 school_corridor_hard_noise fadein 3.0
    scene bg school f3 new_corridor
    show gray zorder 2:
        alpha 0.25
    show vignette zorder 3:
        alpha 0.5
    show crowd_foreground zorder 1
    show crowd_background zorder 0
    with wipeleft_scene
    n "Короче, мне нужно было найти новый клуб."
    n "Я решила посмотреть, какие имеются и чем там люди занимаются."
    mc "...и ты пошла в старый корпус."
    n "Ага."
    stop noise_1 fadeout 3.0

    scene black with wipeleft_scene
    n "Всё моё изучение свелось к прогулкам по коридору и заглядываниям в дверные окна."
    n "Почему?"
    n "Потому что я никого там не знала."
    n "А к неизвестным у меня доверия нет."
    mc "Понимаю..."
    n "И вот, когда я шла по одному коридору на втором этаже и засмотрелась в окно..."
    play sound ram_attack
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 0.25
    n "...то случайно наткнулась на одну ученицу, которая открывала дверь в класс."
    mc "Дай угадаю: ей оказалась Моника?"

    scene bg corridor
    show gray zorder 2:
        alpha 0.25
    show vignette zorder 3:
        alpha 0.5
    show monika forward happ cm oe school_bag at i11
    with dissolve
    pause 0.25
    n "Да."
    n "Она меня спросила:"
    show monika om lpoint
    m "Ты же одна из бывших участниц Клуба выпечки?"
    show monika cm ldown
    n "Я ответила:"
    n "Да."
    show monika ce
    n "И знаешь, что она мне сказала?"
    mc "Что?"
    show monika lean happ om oe school_bag at h11
    m "Подружка-манджушка, ты ошиблась дверью."
    show monika neut om oe
    m "Клуб выпечки этажом ниже."
    show monika m1
    n "Я не выдержала такой наглости и ответила:"
    show monika angr cm oe
    n "ДА ПОШЛА ТЫ!"
    stop music
    play music_none_loop music_stop
    mc "Так, стоп!" with vpunch
    call window_close

    call window_dialog_fast_transition("mc")

    call window_open
    play music t5 fadein 3.0
    scene bg closet
    show natsuki turned fc curi cm oe at i11
    mc "Серьёзно, так и было?"
    show natsuki sad om oe
    n "Не совсем, конечно..."
    show natsuki md
    mc "А если честно?"
    show natsuki neut om oe
    n "Немного преувеличила."
    show natsuki cm
    mc "..."
    show natsuki angr om ce
    n "Ой, ладно, не было ничего такого."
    show natsuki neut om oe
    n "Моника сразу решила меня приютить в свой ещё зародившийся клуб."
    n "А я не была против, потому что...{w}да выбора не было."
    show natsuki anno om oe
    n "Пошутить не даёшь, душнила."
    show natsuki cm
    mc "Да, я."
    show natsuki curi om oe
    n "Эй..."
    n "Тебя там Сайори подзывает."
    show natsuki cm
    mc "Ох, тогда мне пора."

    scene black with wipeleft_scene
    "К Юри теперь прилипла Моника."
    "Надо быстренько переговорить с Сайори."

    scene bg school literature_club board day
    show sayori turned sad cm oe at t11
    with wipeleft_scene
    show sayori om oe
    s "Макс, я хочу потом провести Юри до дома, поэтому..."
    show sayori cm oe
    mc "Снова тебя не искать?"
    s "Угу."
    show sayori neut cm oe
    mc "С ней настолько всё плохо?"
    show sayori om oe
    s "Вроде уже полегче, но ещё да."
    show sayori angr cm oe
    mc "Ты только себя не загони, пожалуйста."
    show sayori angr om oe
    s "За меня не переживай!"
    show sayori om ce
    s "Пока Юри легче не станет, не станет легче и мне."
    show sayori cm ce
    mc "Да как тут за вас не переживать..."
    show sayori neut cm oe
    mc "Ладно, с Юри я ещё поговорю, а сейчас можешь почитать мой стих."
    show sayori happ om ce lup rup at h11
    s "Хорошо!"
    show sayori cm ce ldown rdown
    call window_close

    play sound paper_torn_out
    show sayori lup poem_paper with dissolve
    pause 1.0
    show sayori e1b
    pause 6.0
    show sayori neut cm e2b
    pause 10.0
    show sayori happ om ce

    call window_open
    s "Он прекрасный!"
    show sayori cm ce
    mc "Да ну..."
    show sayori om oe
    s "Серьёзно!"
    show sayori e2b
    s "Ты красиво описал камни!"
    show sayori ce
    s "Мне особенно нравятся синий сапфир, потому что люблю небесный цвет."
    show sayori om oe
    s "Макс, ты же ведь специально описал именно их?"
    show sayori curi om e2b
    s "Как будто тут все участницы Литературного клуба..."
    show sayori neut cm oe
    mc "Как мне говорила Юри: \"Читатель должен сам догадаться, о чём было стихотворение\"."
    mc "Так что этот вопрос остаётся открытым."
    mc "Но по секрету скажу: ты мыслишь правильно."
    show sayori doub cm ce
    s "Хм-м-м..."
    show sayori happ om oe
    s "Будем считать, что так!"
    show sayori cm oe
    play sound paper_torn_out
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    mc "Давай тогда твой стих гляну."
    show sayori om ce lup rup at h11
    s "Вот!"
    show sayori cm ce ldown rdown
    call show_poem(poem_s3)
    "Это забавно в некоторой степени."
    show sayori neut cm oe
    mc "Мне кажется, что двух бутербродов тебе будет мало."
    show sayori curi om oe
    s "Мне их за глаза с утра хватает!"
    show sayori cm oe
    mc "Уверена?"
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    play music t5c fadein 2.0
    mc "А если это будет бутерброд с печеньем?"
    show sayori nerv mb oe at s11
    s "А..."
    show sayori cm
    mc "Вот такими на тебя точно не напасёшься."
    show sayori happ cm ce at t11
    pause 0.2
    show sayori om ce lup rup at h11
    s "Печенье очень вкусное, перед ним невозможно устоять!"
    show sayori shoc cm oe ldown rdown
    mc "...поэтому я прячу пару упаковок у себя дома в потаённых местах."
    show sayori vang om ce lup rup at h11
    s "ЧТО?!"
    show sayori vang om oe ldown rdown
    s "Завтра с утра устрою обыск!"
    show sayori mj oe
    mc "Попробуй, не сможешь отыскать."
    show sayori om ce
    s "Это вызов!"
    show sayori mj ce
    mc "Ох, Сайори..."
    mc "С тобой точно никогда не заскучаешь."
    show sayori tap nerv om oe at s11
    s "Э-хе-хе~"
    show sayori turned happ cm ce at t11
    mc "Ладно, хороший стих, ты молодец."
    play sound paper_torn_out
    pause 1.0
    stop music fadeout 6.0
    show sayori neut cm oe
    mc "Попробую выяснить, что там с Юри творится."
    show sayori flus om oe
    s "Только поаккуратнее!"
    show sayori cm oe
    mc "Конечно."

    scene black with wipeleft_scene
    "Чем ближе я подхожу к этой лавандовой девушке...{w}тем больше мне становится не по себе."
    "Будто у всего окружения повышается чувствительность к любым раздражителям."
    "Малейшее колебание: хоть механическое, хоть звуковое -- может разорвать всё вдребезги."
    "Хочется остановиться, но неизбежного не избежишь..."
    "Решить проблему надо."
    "Так что..."

    scene bg club_day
    show yuri shy neut cm oe at s11
    with wipeleft_scene
    "...я должен проявить инициативу, иначе всё станет только хуже."
    show yuri n2
    mc "Юри?..."
    show yuri n4
    y "..."
    mc "Что случилось?"
    show yuri m2 n5
    y "..."
    mc "Мы можем побыть за дверями, если ты не хочешь говорить при посторонних, я спокойно тебя выслушаю."
    y "..."
    show yuri m4
    y "{size=19}...да...{w}вай...{/size}"
    show yuri cm

    scene black with wipeleft_scene
    "Так, уже хорошо."
    "Я боялся, что она вообще ничего не скажет."
    "Пока идём в коридор, надо жестом показать Сайори, что скоро вернёмся."
    "Моника и Нацуки, к слову, провожают нас волнующим взглядом."
    "Неприятно быть у всех на виду, но что поделать..."
    call window_close

    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school old_corridor wall
    show yuri shy neut m2 oe at s11
    with wipeleft_scene
    mc "Так, вроде никого..."
    mc "Юри."
    mc "Расскажи, что всё-таки случилось."
    show yuri e1 m2
    mc "Мы все за тебя переживаем."
    show yuri om oe
    y "Я..."
    show yuri m2
    y "..."
    mc "Не стесняйся."
    show yuri m3
    mc "Вспомни, как ты уверенно критикуешь мои стихи."
    show yuri ce
    y "...хе-хе...."
    mc "Вот-вот."
    show yuri cm oe
    mc "Давай ещё раз, только немного поувереннее."
    show yuri om oe
    y "Я..."
    show yuri turned lsur om oe lup rup at t11
    y "Я хотела с тобой поговорить."
    show yuri e2b
    y "Н-но..."
    show yuri at s11
    y "...вы с Нацуки там...{w}лежали...{w}я не хотела вам мешать..."
    show yuri cm
    "Тьфу, серьёзно?!" with vpunch
    show yuri oe
    mc "Ха-ха..."
    mc "Ха-ха-ха!"
    show yuri at t11
    mc "Юри, выбрось это из головы, ничего такого не было."
    show yuri ldown rdown
    mc "Я вообще не ожидал, что она в сон провалится после того, как на меня свалится из-за томика на дальней полке."
    show yuri anno om oe
    y "...у...{w}угу..."
    show yuri cm oe
    mc "Я уж думал, что что-то плохое случилось..."
    show yuri happ cm oe
    mc "Не пугай меня так больше, ха-ха!"
    show yuri om ce
    y "Хе-хе..."
    show yuri anno om oe lup rup at s11
    y "{size=19}Но я люблю ужастики...{/size}"
    show yuri neut cm e1d at t11
    mc "Подожди, а что ты хотела обсудить?"
    show yuri dist om oe ldown rdown
    y "Ну..."
    show yuri ce at s11
    y "...то, что..."
    show yuri sedu cm oe
    y "...я тебя---{nw}"
    show yuri pani om oe lup rup at t11
    y "Кхм, нет!{nw}"
    show yuri sad om oe
    y "Э-это...{nw}"
    show yuri pani om ce
    y "А-а-а-а--{nw}"
    show yuri laug om oe ldown rdown
    y "--хотела найти, ты же ведь обещал подумать над смыслом моего стиха, который я тебе отдала в качестве примера, да?"
    show yuri happ cm oe
    "Меня немного торкнуло от её резких звуков..."
    mc "Стих..."
    mc "Да, у меня появилась одна мысль."
    mc "Кстати, держи, а то забуду."
    play sound paper_torn_out
    pause 1.0
    mc "Так вот, мысль..."
    mc "Не знаю, стоит ли её озвучивать или нет..."
    show yuri om ce lup rup
    y "Давай, а то моё сердце уже выпрыгивает от волнения."
    show yuri cm ce
    "С Юри явно что-то не так..."
    show yuri cm oe ldown rdown
    mc "Я перечитал твой стих несколько раз."
    show yuri neut cm e2a
    mc "И каждый раз я цеплялся за строфы про нож..."
    show yuri flus md oe
    mc "...они меня напрягают."
    show yuri e2a
    mc "Юри."
    mc "Учитывая твою любовь к аллегориям, я хочу задать тебе один вопрос..."
    show yuri n2
    mc "Ты любишь что-то резать ради эйфории?"
    show yuri cm oe
    y "У-у-у..."
    mc "Нет-нет, извини за такое грубое предположение!"
    show yuri om e1a
    y "Стой!"
    show yuri oe
    y "Это..."
    show yuri om ce lup rup
    y "...просто крайне неожиданный вопрос..."
    show yuri md ce
    mc "Я понимаю, но--{nw}"
    show yuri worr om oe
    y "Дай мне минутку..."
    show yuri cm oe
    mc "Хорошо."
    show yuri cm ce
    y "..."
    show yuri om ce
    y "..."
    show yuri dist om ce
    y "..."
    show yuri dist om oe -n2 ldown rdown
    y "{size=10}Первый шаг...{/size}"
    y "{size=10}Чтобы его сделать, я должна быть уверенной.{/size}"
    y "{size=10}А если я его сделаю, то должна быть открытой.{/size}"
    show yuri om ce
    y "{size=10}Ему придётся это узнать.{/size}"
    show yuri lup rup
    y "{size=10}У меня всё получится...{/size}"
    show yuri cm ce
    "Что она бормочет?"
    show yuri sedu cm oe ldown rdown
    y "Макс..."
    y "Чтобы ответить на твой вопрос, мне придётся раскрыть один свой секрет."
    show yuri e1b
    y "Я это делаю только с теми, кому очень-очень-очень доверяю."
    show yuri oe
    y "Пообещай, что ты никому ничего не расскажешь."
    show yuri md
    "Меня это начинает волновать..."
    mc "Конечно, я могила."
    show yuri anno om ce
    y "Хорошо..."
    show yuri om e1b
    y "Только давай сначала отойдем на первый этаж под лестницу."
    show yuri cm
    "Крайне волновать..."
    mc "Ладно..."

    scene bg school f1 old_stairwell center
    show yuri turned worr cm oe at t11
    with wipeleft_scene
    show yuri om oe
    y "Я..."
    show yuri cm oe
    "Только не говорите мне, что--{nw}"
    call window_close

    show yuri cm ce
    show yuri rcutdown with dissolve
    pause 1.5

    call window_open
    y "..."
    mc "Твою мать..."
    "Она резала {b}себя{/b}."
    mc "Твоя рука..."
    show yuri om oe
    y "Ты был прав..."
    show yuri lsur cm oe
    mc "Можно посмотреть?"
    show yuri om oe
    y "...д-да..."
    show yuri cm
    call window_close

    hide yuri
    show yuri turned lsur cm oe rcutdown at face
    with dissolve_cg
    pause 1.5
    show yuri rcut with dissolve_cg
    pause 2.0

    call window_open
    "Чёрт побери..."
    "Она хоть раны обеззараживает?!"
    "А бинты?!"
    "А если что-то случится?!"
    "Некоторые до сих пор слегка сочатся!"
    mc "Ты так себе инфекцию занесёшь!"
    show yuri worr cm oe
    y "..."
    mc "Нет, так дело не пойдёт..."
    "Намусолю пару пальцев и «обработаю» свежие рубцы, хоть таким образом!"
    "Всё равно у меня никаких болезней никогда не было, ничем её не заражу."
    show yuri sedu cm ce
    y "...ох..."
    "Какого хрена, Юри?!"
    y "{size=10}...эти...{w}ощущения...{/size}"
    "Травмировать такое хорошее тело?!"
    "Зачем?!"
    mc "Зачем ты вообще подобным занимаешься?!"
    show yuri cm oe
    y "А-а-а?"
    show yuri sad om oe
    y "Я-я..."
    show yuri worr om oe
    y "...я сейчас не вспомню..."
    show yuri cm oe
    mc "В твоей жизни было что-то негативное?"
    mc "Или тебе просто нравится подобное?"
    show yuri om oe
    y "...не знаю, я не могу сейчас сказать точно..."
    show yuri cm oe
    mc "Блин, Юри, это {b}ненормально{/b}."
    mc "Тебя надо как-то от этого отучить."
    show yuri worr om ce
    y "...у-ух..."
    show yuri om oe
    y "...спасибо за «обработку» ран..."
    show yuri cm oe
    mc "Да толку от этого \"спасибо\", мне тебя жалко."
    show yuri lsur om oe
    y "Знаешь, раз ты узнал этот секрет..."
    show yuri om ce
    y "...то вот мой второй стих, продолжение прошлого..."
    show yuri cm ce
    mc "М-м?"
    call show_poem(poem_y3, music=False)
    "Он меня только добил..."
    "Хотя стоп."
    mc "\"Потеря части души\"..."
    "Юри потеряла кого-то ценного, испытывает из-за этого чувство вины, которое утоляет порезами?"
    show yuri om oe
    y "Э-это аллюзия на...{w}чувства из детства..."
    show yuri cm
    "...что не отменяет моё предположение."
    show yuri neut cm e1d
    mc "Хорошо, пока спрячь свою руку."
    call window_close

    show yuri rdown with dissolve
    pause 0.25
    hide yuri
    show yuri turned neut cm e1d at e11
    with dissolve

    call window_open
    mc "Обязательно, когда сможешь рассказать про ЭТО, подчёркиваю, ОБЯЗАТЕЛЬНО, просвети меня в курс дела."
    show yuri om
    y "Угу..."
    show yuri worr cm oe
    mc "Просто пойми: твои раны могут вскрыться на каком-нибудь обследовании в медкабинете или на физкультуре, что породит множество проблем."
    mc "Хотя у нас уже была физ-ра, как ты умудрилась скрыть?"
    show yuri om
    y "Я просто...{w}себя раньше не резала, а это...{w}буквально на днях..."
    show yuri cm
    mc "Мда..."
    show yuri neut cm e1d
    mc "Если ты это не прекратишь, то, учитывая наше бестолковое школьное общество, начнётся высмеивание и травля."
    mc "Чем быстрее мы ликвидируем твою зависимость, тем будет лучше в первую очередь для тебя."
    y "..."
    mc "Ладно, сейчас мы пока ничего не можем сделать..."
    show yuri lsur cm oe
    mc "Хотя нет, ты можешь."
    mc "Когда придёшь домой, нормально обработай руку и оставь открытой, чтобы быстрее всё зажило."
    show yuri om oe
    y "Хорошо..."
    show yuri cm oe
    mc "А у тебя дома знают про {b}это{/b}?"
    show yuri flus om oe
    y "Мама уехала на пару недель по работе, я одна."
    show yuri md
    mc "Фух, хоть так."
    "Да, надо восстановить связь с тем психологом, Юри срочно нужна помощь."
    show yuri neut cm e1d
    mc "Итак, теперь пока точно всё."
    mc "Поэтому сейчас мы вернёмся в клуб и сделаем вид, что весь наш разговор был только в том коридоре, хорошо?"
    show yuri worr om oe
    y "Д-да..."
    show yuri cm oe
    call window_close

    call plot_transition

    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show yuri turned neut cm e1b at t11
    with wipeleft_scene
    "Моника, Сайори и Нацуки искоса пронзили меня удивлёнными глазами."
    "Ну а я что?"
    "Легонько им кивнул, показав, что всё в порядке."
    play music t5 fadein 3.0
    "Создаётся такое впечатление, что они симулируют обмен стихами, чтобы Юри не напрягалась."
    show yuri e1d
    mc "Ладно, раз я уже прочитал твой стих, то теперь моя очередь показать свой."
    mc "Как обычно, критикуй, как знаешь."
    show yuri om
    y "Хорошо."
    show yuri cm
    call window_close

    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0
    show yuri e1b
    pause 6.0
    show yuri happ cm e1b
    pause 5.0
    show yuri e2b
    pause 8.0
    show yuri om ce rup

    call window_open
    y "Неожиданно много строф, хе-хе."
    show yuri cm ce
    mc "Да, меня в этот раз на слова понесло..."
    show yuri om oe rdown
    y "Судя по всему, ты решил чётко следовать моему стилю, так?"
    show yuri cm oe
    mc "Да."
    show yuri om e1b
    y "Примечательно здесь то, что чем дальше ты писал, тем более свободным становился."
    show yuri flus om oe rup
    y "Сначала ты пытался писать длинными строфами, загнав себя в рамки моего стиля, что вышло, честно говоря, неудачно..."
    show yuri happ om e1b rdown
    y "Но ближе к середине они уменьшаются, а вместе с ними, напротив, увеличивается лёгкость в чтении."
    y "Ты уже начинаешь писать больше в своём стиле, что благоприятно сказывается на самом стихотворении, не забывая при этом использовать символизм."
    y "Наилучшая часть..."
    show yuri cm oe
    mc "...часть с описанием самоцветов, да?"
    show yuri om ce rup
    y "Конечно!"
    show yuri cm ce
    mc "Каждый это подметил."
    show yuri om oe rdown
    y "И неспроста: я вижу, ты вложил в них образы тех, кто тебе близок в данный момент?"
    show yuri cm oe
    mc "А ты догадливая, хах."
    show yuri om ce rup
    y "Это вышло потрясающе!"
    show yuri e1b rdown
    y "Строфы с аметистом...{w}вызывают у меня особые чувства..."
    show yuri cm
    mc "Значит, не зря старался."
    show yuri om ce rup
    y "Очень хорошая работа, Макс!"
    show yuri om oe
    y "За 3 дня написать стихотворение такого уровня достойно похвалы."
    show yuri cm oe rdown
    mc "Ох, спасибо."
    play sound paper_torn_out
    show yuri ldown with dissolve
    pause 1.0
    mc "Но мне кажется, ты немного преувеличиваешь..."
    show yuri om oe
    y "Нисколько, это абсолютно заслуженно."
    show yuri cm oe
    mc "Ну, раз ты так говоришь, значит, так оно и есть."
    mc "Спасибо ещё раз за твоё мнение."
    show yuri om ce lup rup
    y "Спасибо за такой хороший стих."
    show yuri om oe
    y "Надеюсь, в последующие разы ты будешь радовать нас ещё более интересными плодами своих творческих работ."
    show yuri cm oe ldown rdown

    scene black with wipeleft_scene
    "Юри заметно оживилась."
    "Прямо от души отлегло..."
    "Но проблема с порезами никуда от этого не делась, надо думать, как её решить..."
    "Вечером после домашней работы подумаю."

    scene bg club_day
    show monika forward happ cm oe at t11 zorder 2
    with wipeleft_scene
    show monika om oe lpoint rhip
    m "Итак, друзья!"
    show monika cm oe ldown rdown at t41
    show natsuki turned happ cm oe at t42
    show yuri turned happ cm oe at t43
    show sayori turned happ cm oe at t44
    pause 0.5
    show monika om oe
    m "Третий обмен стихами подошёл к концу."
    show monika lean happ om oe at h41
    m "Вижу, он прошёл довольно продуктивно и положительно по сравнению с прошлым."
    show monika cm oe
    show yuri om ce lup rup
    y "Конечно!"
    show yuri cm oe ldown rdown
    mc "Есть такое."
    show sayori om oe lup rup at h44
    s "Да!"
    show natsuki om oe lhip rhip
    show sayori cm ce ldown rdown
    n "Соглашусь."
    show monika forward happ om ce
    show natsuki cm oe
    show yuri e1b
    m "Очень хорошо!"
    show monika om oe lpoint
    show yuri oe
    show sayori cm oe
    show natsuki neut cm oe ldown rdown
    m "Ввиду того, что Макс уже попробовал стили Сайори и Юри, на очереде остаётся стиль Нацуки."
    show monika cm oe ldown
    show natsuki om oe
    n "Я должна одолжить ему один из своих стихов, ясно."
    show monika om ce
    show natsuki cm oe
    m "Правильно!"
    show monika om oe lpoint
    m "Поэтому, Юри и Сайори, вы можете быть свободны!"
    show monika cm oe ldown
    show yuri om oe
    y "До завтра."
    show yuri cm oe at thide
    hide yuri
    show sayori om ce
    s "Всем пока!"
    show sayori cm ce at thide
    hide sayori
    show monika at t21
    show natsuki at t22
    pause 0.5
    show monika om oe lpoint
    m "Так, Нацуки, у тебя есть что на примете?"
    show monika cm oe ldown
    show natsuki curi om e1b
    n "Я вот думаю..."
    n "Либо первый стих, либо последний..."
    show natsuki neut cm oe
    mc "Тот, который я сегодня видел, был более показательным и понятным."
    show natsuki om oe
    n "Хочешь его взять?"
    show natsuki cm oe
    mc "Да давай."
    show natsuki om oe lhip rhip
    n "Окей, твой выбор."
    show natsuki cm oe
    play sound paper_torn_out
    pause 1.0
    show natsuki happ cm oe
    mc "Благодарю."
    show monika om oe
    m "Что ж, Макс, это последний экспериментальный стих."
    show monika lpoint
    show natsuki neut cm oe ldown rdown
    m "Попрошу тебя завтра принести с собой ещё два прошлых, а также самый первый."
    show monika ldown
    m "Хочу проанилизировать их на выходных, а потом обсудить с тобой твой стиль."
    show monika cm oe
    mc "Всё так серьёзно?"
    show monika om ce lpoint
    show natsuki dist cm oe
    m "Мы же ведь Литературный клуб, верно?"
    show monika om ce ldown
    m "Значит, и к таким вещам должны подходить ответственно!"
    show monika cm oe
    show natsuki neut cm oe
    mc "Хорошо, что на выходных я ничего не планировал..."
    show monika om ce
    m "Вот и отлично!"
    show monika om oe lpoint
    show natsuki happ cm oe
    m "Ладно, с этим решено, можете быть свободны!"
    show monika cm oe ldown
    show natsuki om oe
    n "До завтра."
    show natsuki cm oe
    mc "Удачи."
    show monika om ce
    m "До свидания!"
    show monika cm ce
    stop music fadeout 3.0
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show natsuki turned neut cm e1b school_bag at t11
    with wipeleft_scene
    mc "Ой, фу, опять голова вскипела..."
    show natsuki om
    n "А Юри прям повеселела."
    show natsuki curi om oe
    n "Что там с ней было?"
    show natsuki cm
    mc "Ничего такого."
    mc "Когда она нас увидела в кладовке, то с чего-то подумала, что своим присутствием помешала нашему «времяпрепровождению»."
    show natsuki om
    n "А?..."
    show natsuki fc curi om oe
    n "Серьёзно?"
    show natsuki cm
    mc "У меня была абсолютно такая же реакция."
    show natsuki sad om oe
    n "Иногда Юри меня поражает..."
    show natsuki cm oe
    mc "Ну, знаешь..."
    show natsuki curi cm oe
    mc "Все мы разные."
    show natsuki angr om oe
    n "Ну не настолько же!"
    show natsuki cross ff om ce school_bag
    n "Убиваться по такой фигне -- тупо!"
    show natsuki anno cm oe
    mc "Слушай, ей и так тяжело даётся взаимодействие с социумом, даже, казалось бы, с близким, а тут твои неожиданные выкрутасы."
    show natsuki turned fc angr om oe school_bag
    n "Стул крепче держать надо было!"
    show natsuki cm oe
    mc "Нифига себе."
    mc "Нечего тянуться до книжки через всю полку."
    show natsuki cross ff vang cm ce school_bag
    n "Грх!"
    mc "То-то."
    show natsuki angr cm ce
    "..."
    show natsuki neut cm oe
    mc "Прощаемся до завтра?"
    show natsuki turned fc pout om oe school_bag
    n "А может, составишь компанию?"
    show natsuki sad om oe
    n "Одной скучно."
    n "Обычно я с Юри возвращаюсь или с Сайори, но ни той, ни другой уже нет."
    show natsuki neut cm oe
    mc "...и далеко до твоего дома идти?"
    show natsuki om oe
    n "Не особо, не успеешь откинуться."
    show natsuki happ cm oe
    mc "Ладненько, пошли."

    scene black with wipeleft_scene
    "Странно, а Моника вообще не поинтересовалась насчёт Юри...{w}да и Сайори тоже..."
    "Возможно, они и так всё поняли."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show natsuki turned fc neut cm oe school_bag at t11
    with wipeleft_scene
    mc "Моника мне всё-таки рассказала про твоё положение."
    show natsuki dist om oe
    n "Ясно."
    show natsuki cm oe
    "..."
    "Сказать мне больше нечего по этому поводу."
    show natsuki anno om ce
    n "Знаешь, меня это всё достало..."
    n "Отец постоянно пытается строить из себя примерного родителя."
    n "Следит за каждым моим перемещением по дому, если не спит."
    n "Постоянно перегибает палки..."
    show natsuki angr om ce lhip rhip
    n "Ему самому отец нужен!"
    n "Я себя и так контролирую, меры прекрасно знаю."
    show natsuki vang om ce
    n "Но нет, я же его дочурка, а он «образцовый семьянин», тьфу!"
    show natsuki pout om oe ldown rdown
    n "Когда это уже закончится?"
    n "Когда выздоровеет моя мама?"
    n "Когда я наконец стану жить своей нормальной жизнью?"
    n "Когда, Макс?..."
    show natsuki cm oe
    mc "Откуда я знаю?"
    mc "Шестое чувство подсказывает, что скоро..."
    show natsuki om oe
    n "Да когда это \"скоро\" настанет?!"
    show natsuki cm oe
    mc "Если я сказал \"скоро\", то это реально скоро."
    mc "В течение..."
    show natsuki angr cm oe
    mc "...этого года, может быть..."
    show natsuki om oe
    n "За такой срок после всего того, что произошло?!"
    show natsuki cross ff angr om oe school_bag
    n "Это ты так меня утешить пытаешься?"
    show natsuki cm oe
    mc "Блин, Нацуки, что ты завелась?"
    mc "Это всего лишь предположение."
    show natsuki anno om oe
    n "Лучше молчи, а?"
    show natsuki om ce
    n "Оно меня только раздражает."
    show natsuki cm ce
    mc "Ну и как хочешь."
    "Тоже мне..."
    "Сама спросила, сама и возмутилась."
    show natsuki sad cm ce
    "Кто ж вас, девушек, разберёт?"
    "Иногда эта распущенность по эмоциям так бесит..."
    "Тяжело себя контролировать?"
    "Хоть чуть-чуть?"
    show natsuki turned fc sad om oe school_bag
    n "Я знаю, это может прозвучать глупо..."
    n "Но тебе я могу доверять, поэтому..."
    show natsuki pout om oe
    n "Макс, если бы со мной что-нибудь случилось..."
    n "Ты бы дал мне пожить у себя на время?"
    show natsuki cm
    mc "Ну и вопросы..."
    show natsuki om
    n "Пойми, я заметила, как отец в последнее время с каждым днём начинает чаще и дольше выходить из себя."
    show natsuki e1b
    n "И остановить это я никак не могу."
    show natsuki ce
    n "В один момент он просто сорвётся и порвёт меня..."
    show natsuki oe
    n "Мне нужно безопасное место, куда он не доберётся."
    n "И ты, Макс, единственный, кто может дать мне это место."
    show natsuki cm
    mc "Я всё ещё не пойму, почему родственники тебя взять не могут?"
    mc "Моника говорила, что связи с ними нет, но это звучит, словно бред какой-то."
    show natsuki om
    n "Сейчас с ними реально нет связи."
    show natsuki e1b
    n "Я даже никого из них не видела за последние пару лет."
    n "Да и отношения у нас не очень..."
    show natsuki e4a
    n "Не хочу их видеть, они всё равно не помогут."
    show natsuki cm
    mc "Понятно..."
    show natsuki e1b
    "Со своими, к слову, я тоже нечасто вижусь..."
    show natsuki neut cm oe
    mc "Если говорить о моём доме, то разве он будет для тебя безопасным?"
    mc "Да, я живу один, денег на себя хватает с запасом..."
    mc "Но мы все в одном районе живём."
    show natsuki om
    n "Это лучше, чем ничего..."
    show natsuki cm
    mc "М-м-м..."
    mc "Ладно."
    show natsuki happ cm oe b2b
    mc "Если будет что-то плохое, то сразу пиши и беги ко мне."
    mc "Но боюсь, что это не поможет."
    mc "Если твой отец рассвирепеет, то он запросто выбьет дверь или окно."
    show natsuki mb
    n "Всё равно спасибо, Макс."
    show natsuki ce
    n "Даже если такое случится, то у нас будет время вызвать полицию или чем-нибудь отбиться, правильно?"
    show natsuki cm
    mc "Звучит это всё, конечно, слишком авантюрно и бредово..."
    show natsuki oe
    mc "...но ты права."
    show natsuki pout om oe -b2b
    n "Всё-таки я очень надеюсь, что мама выздоровеет быстрее, чем произойдёт что-то ужасное."
    show natsuki ce
    n "Лишь бы съехать к чертям."
    show natsuki neut cm oe
    mc "А ты вообще знаешь, где мой дом?"
    show natsuki om
    n "Сайори уже рассказывала."
    n "Она напротив тебя живёт, а её дом я помню."
    show natsuki cm
    mc "Хоть так..."

    scene bg natsuki house outside day
    show natsuki turned happ cm ce school_bag at t11
    with wipeleft_scene
    mc "Ничего себе..."
    show natsuki neut cm oe
    mc "У тебя довольно просторно тут..."
    show natsuki om oe lhip rhip
    n "Угу, этот дом отец купил ещё тогда, когда я была маленькой."
    show natsuki cm oe ldown rdown
    "Выходит, условно за полтора десятка лет он из-за чего-то скатился..."
    show natsuki e1b
    "Что могло на него так повлиять?"
    "Или здесь было нечто комплексное, что привело его к такому бедственному во всех смыслах положению?"
    show natsuki dist om oe
    n "Пора расходиться, пока он нас не увидел."
    show natsuki cm oe
    mc "Да..."
    show natsuki happ om ce
    n "До завтра."
    show natsuki cm oe
    mc "До завтра."
    $ nd_name = _("Отец Нацуки")
    nd "{size=19}Ты уже вернулась, Нацуки?{/size}"
    show natsuki shoc om oe at h11
    n "!!!"
    if persistent.add_random_menu == 7:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()
    show natsuki_dad turned neut cm e1b at t21
    show natsuki vsur cm oe at t22
    pause 1.0
    show natsuki_dad oe
    nd "..."
    show natsuki_dad cross neut cm oe
    mc "..."
    mc "Здравствуйте..."
    show natsuki_dad om
    nd "Здрасьте."
    show natsuki_dad cm
    show natsuki cm ce
    mc "..."
    nd "..."
    mc "Э-э-э--{nw}"
    $ nd_name = _("Тамоцу-сан")
    show natsuki_dad turned neut om oe rup
    show natsuki curi cm e2a
    nd "Тамо{image=accent_low_register}{space=-15}цу-сан."
    show natsuki_dad cm rdown
    mc "...Макс."
    show natsuki_dad cross neut cm oe
    nd "М-м."
    mc "Я Нацуки компанию составил."
    nd "Угу."
    mc "Ну...{w}мне уже пора."
    show natsuki_dad om
    nd "Удачи."
    show natsuki_dad cm

    scene black with wipeleft_scene
    nd "{size=17}Это кто ещё такой?{/size}"
    n "{size=17}Новенький из нашего клуба.{/size}"
    nd "{size=17}Уже решила под шумок отношения начать?{/size}"
    n "{size=17}Нет, папа!{/size}"
    nd "{size=17}В этом возрасте они сведут тебя на обочину этой жизни, Нацуки.{/size}"
    nd "{size=17}Ты должна усердно учиться, чтобы потом достойно содержать себя.{/size}"
    nd "{size=17}Никаких отношений, пока не начнёшь себя достойно обеспечивать.{/size}"
    n "{size=17}Да не было никаких отношений, папа!{/size}"
    n "{size=17}Я даже не думала об этом...{/size}"
    nd "{size=17}Вот и хорошо.{/size}"
    "Ну и бред."
    "С одной стороны, он прав, а с другой..."
    "Куда так всё затягивать?"
    "Если у него такой подход абсолютно везде, то у Нацуки образуется куча комплексов, которые будут вставлять ей палки в колёса."
    "Хотя почему они образуются?"
    "Уже имеются, чёрт вас всех дери."
    "Что за общество, блин..."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg kitchen with wipeleft_scene
    "После всех выполненных дел меня что-то разобрало поесть..."
    "В итоге стою здесь, на кухне, грызу апельсин."
    "Вкусный, и запах приятный."
    "Шкурка снимается на ура."
    "Не прогадал со свежестью, хе."
    "..."
    mc "Хм..."
    "Сегодня был крайне нагруженный день."
    "Мой мозг всё ещё гудит от большого количества информации..."
    "Юри со своими порезами...{w}Нацуки с отцом...{w}а если добавить сверху самоотдачу Сайори..."
    mc "Это какой-то пипец!"
    "Как звёзды должны были сойтись, чтобы люди с такими проблемами объединились в одном клубе, да ещё и жили рядом?"
    "Причём проблемы-то серьёзные."
    "Надо решить их как можно скорее."
    "Сначала подумаем, что делать с Юри..."
    mc "Хм-м-м..."
    "Очевидно первое: восстановить связь с психологом и вывести на него саму Юри."
    "Но для этого надо найти его аккаунт."
    "Да и после всего случившегося...{w}будет крайне тяжело и стыдно с ним общаться."
    "Поиск надо начать либо в эти выходные, либо на следующей неделе."
    "Откладывать точно нельзя."
    "Второе: не допустить повторных порезов."
    "То есть надо выяснить, что послужило причиной такого поведения, разобраться с этим, а ещё проконтролировать Юри по возможности."
    "Ну и поддержать морально, в конце концов."
    "Мда, и это всё на ближайшее время."
    "Теперь Нацуки..."
    "..."
    "Вот здесь вообще задница."
    "Я могу предоставить Нацуки временное жильё..."
    "Но бюрократию никто не отменял."
    "А что ещё?"
    "Ничего."
    "Потрясающе."
    "Остаётся только вместе с ней надеяться, что её мать успеет реабилитироваться в ближайшее время."
    "..."
    mc "Блин, ещё стих писать..."
    call window_close
    play sound trashcan
    pause 4.0

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1

    call window_open
    scene bg bedroom with dissolve
    mc "Стих, значит..."
    call show_poem(poem_n3, music=False)
    "Ну а что тут?"
    "Преимущественно четверостишия."
    "Простое написание без всяких глубоких смыслов..."
    "Но важность с актуальностью от этого никуда не теряется."
    "Рифма тоже простая: через строку."
    mc "Попробуем..."

    call poem_act_1_day_4

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc4, music=False)
    "Простенько, без всякого напряга."
    "Даже читается практически без запинок."
    "Пойдёт."
    "А пока я хочу развеяться."
    "Разгрузить голову..."
    call window_close

    return
