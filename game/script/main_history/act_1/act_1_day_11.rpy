transform custom_fade(a=1.00):
    on show:
        alpha a - 0.1
        linear 1.0 alpha a
    on hide:
        alpha a
        linear 1.0 alpha 0




label act_1_day_11:

    play sound none_transition
    scene black
    pause 3.0

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d10.unlocked == False:
        $ ach_a1_d10.unlock()
        pause 7.0
    else:
        pause 3.0

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
    mc "{cps=20}Глаза слипаются...{/cps}"
    "{cps=20}...{/cps}"
    mc "{cps=20}А-а-аргхх-х-х...{/cps}"
    "{cps=20}Чувствую себя разбитым...{w}трудно пошевелиться...{w}плющит со всей силой к полу...{/cps}"
    mc "{cps=20}Нихрена я не выспался...{/cps}"
    call window_close

    call plot_transition

    call window_open
    scene bg mc house hallway day with wipeleft_scene
    mc "Закрыл...{w}закрыл...{w}закрыл...{w}всё."
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
    "Блин, у меня снова картинка перед глазами поплыла."
    "Надо прийти в себя."
    play sound mc_inhale
    pause 2.5
    "..."
    "Вот, уже получше..."
    play sound screamer_meme
    show sayori turned vang mc ce lup rup school_bag at e11 with moveinbottom
    s "{sc=3}БА-А-А-А-АМ!!!{/sc}{nw}" with vpunch
    show sayori ma
    mc "А-А-А, Сайори?!"
    show sayori happ om oe ldown rdown at tfast
    s "Утречка!"
    show sayori cm
    mc "Нифига себе утречко!"
    show sayori anno cm oe
    mc "Ты зачем так выскочила?!"
    show sayori tap pout om oe school_bag at s11
    s "Ну ты был такой задумчивый, что в мою сторону не посмотрел."
    show sayori nerv om oe
    s "А я решила не упускать такой шанс."
    show sayori turned laug cm oe school_bag at t11
    s "Хи-хи-хи!"
    show sayori happ cm ce
    mc "Не надо так больше."
    show sayori neut cm oe
    mc "Пожалуйста."
    mc "Хотя бы в ближайшее время."
    show sayori curi mf e1a
    s "У-у-у?"
    show sayori neut om oe
    s "Ты, кстати, нервно выглядишь..."
    show sayori b1b
    s "У тебя появились темноватые круги под глазами."
    show sayori cm
    mc "В курсе."
    show sayori om b1c
    s "...тебе снова снился кошмар?"
    show sayori cm
    mc "Да."
    mc "Это уже явно какая-то психическая болезнь."
    mc "И я абсолютно не понимаю, как с ней бороться."
    show sayori vsur om oe -b1c lup rup at h11
    s "Тогда тебе нужен специалист, пока не стало слишком поздно!"
    show sayori cm
    mc "Какой?"
    show sayori neut cm oe b1c ldown rdown
    mc "Психолога, про которого я рассказывал, я так и не нашёл."
    mc "А на какие-то записи и приёмы у меня нет ни времени, ни денег, ни доверенности."
    show sayori curi cm oe -b1c
    mc "Откуда мне знать, что мне там нашьют?"
    show sayori om
    s "Как что?"
    show sayori neut om oe
    s "Их работа -- помогать другим."
    show sayori cm
    mc "Для кого-то работа, а для кого-то деньги и ниша для просиживания штанов."
    mc "И в большинстве случаев как раз второе."
    show sayori b1c
    mc "Вон, мне как-то тот психолог поведал одну короткую историю..."
    mc "Пойдём, по пути расскажу."
    show sayori mg
    s "У, угусь..."
    show sayori cm

    scene bg niigata street suburban 10 day
    show sayori turned neut cm oe school_bag at t11
    with wipeleft_scene
    mc "Так вот, работал он как-то в одной стране из СНГ."
    mc "Уже не помню, какой именно..."
    mc "В общем, пришёл к ним пациент жаловаться на апатию."
    mc "Казалось бы, он сделал всё правильно: явился, рассказал, чтобы это диагностировали, а далее вылечили."
    show sayori b1f
    mc "И знаешь что?"
    s "???"
    show sayori flus cm oe -b1f
    mc "Врач хотел влупить ему шизофрению."
    mc "Нормально, да?"
    show sayori om
    s "Ух..."
    show sayori cm e1a
    mc "Это хорошо, что вовремя пресекли этот дебилизм."
    mc "А теперь представь, какие последствия были бы, если это официально вписали?"
    show sayori worr cm oe
    mc "Пациент бы всю жизнь жалел о таком визите."
    mc "Грубо говоря, пришёл с мелкими расстройствами -- ушёл с тяжёлыми."
    mc "И всем на это смачно плевать."
    show sayori me ce
    s "Уф-ф-ф..."
    show sayori neut om oe b1c
    s "Но мы же в Японии живём, тут прогресс выше..."
    show sayori cm
    mc "Выше..."
    mc "Поверь, Сайори, даже здесь «халтуры» полно."
    show sayori e1b
    mc "Только выражена она в более мелких вещах и размазана тонким слоем."
    show sayori oe -b1c
    mc "Короче, остаётся полагаться на себя."
    show sayori om
    s "Но ты же сам сказал, что не знаешь, как с этим бороться."
    show sayori cm
    mc "...ну да."
    "Я выстрелил себе в колено."
    mc "В этом и парадокс."
    show sayori om b1c
    s "Ничем хорошим это не кончится."
    show sayori cm
    mc "Да чёрт побери, нет вариантов у меня, НЕТ!"
    mc "И сил, и времени на решение этого маразма нет."
    show sayori om
    s "И поэтому ты будешь мучиться и смотреть, как это нечто развивается во что-то плохое?"
    show sayori cm
    mc "А у меня выбор есть?"
    "Его реально нет."
    show sayori e1b
    s "..."
    mc "Вот она, Сайори, прекрасная взрослая жизнь."
    show sayori om
    s "Эх..."
    show sayori cm
    "Один вопрос: \"Чем я это заслужил?\""
    "Хотя какая тут к чёрту справедливость..."

    scene bg school gate 1
    show sayori turned flus cm oe school_bag at t11
    with wipeleft_scene
    show sayori om lup rup at h11
    s "Ой, точно!"
    show sayori neut om oe ldown rdown
    s "Сегодня передавали дождь после полудня."
    show sayori b1f
    s "Ты взял зонтик?"
    show sayori cm -b1f
    mc "Да, с собой."
    show sayori shoc cm ce
    s "Фух."
    show sayori md
    mc "Ты-то хоть не забыла?"
    show sayori happ om ce
    s "Неа!"
    show sayori oe
    s "Мне мама напомнила."
    show sayori cm
    mc "Ха, понятно."
    show sayori om ce lup rup at h11
    s "Ладно, до встречи в клубе!"
    show sayori cm ldown rdown
    mc "До встречи."
    show sayori at thide
    hide sayori
    pause 1.0
    "..."
    mc "Блин..."
    mc "По средам же физ-ра на первом уроке."
    mc "А я такой убитый..."
    stop noise_3 fadeout 3.0
    call window_close

    call window_dialog_long_transition("y")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school f1 old_stairwell right with dissolve_scene_full
    y "Ф-ф-ф..."
    "Как же хорошо, что мои руки успели зажить к сегодняшнему дню..."
    "Если бы не Макс, то...{w}этот урок физкультуры был бы фатальным..."
    "Чем я только руководствовалась, когда..."
    "Нет-нет-нет, я не должна об этом думать!"
    "Иначе это состояние вернётся снова!"
    "Оно и так меня пожирает..."
    "Всё, хватит!" with vpunch
    "..."
    "......"
    "Но теперь весь клуб об этом знает, у-у-у..."
    "Мне и так стыдно за свою безконтрольность, а тут теперь это у всех на слуху..."
    "Неужели это Макс всё разболтал?"
    "Нацуки точно не при чём, это подтверждает её реакция на слова Сайори."
    "Зачем же Макс так поступил?"
    "Я же просила его держать это в секрете..."
    "..."
    "А может...{w}он так обо мне заботится?"
    "...я могу его понять, что он сильно шокировался от моего изъяна."
    "Но...{w}неужели он так обо мне переживает?"
    "Он тоже...{w}любит меня?"
    "А тогда почему он часто проводит время с Моникой?"
    "А если он уже полюбил её?"
    "А если все мои попытки слабы и бессмысленны?"
    "А если, а если, а если, а если, а если--{nw}"
    n "{size=19}...она здесь.{/size}"
    y "А?"
    show natsuki turned neut cm oe school_bag at l21 zorder 2
    show kotonoha happ cm oe school_bag at l22
    pause 0.5
    show kotonoha om ce lup rhip
    k "А вот и наша бедная Юри."
    show natsuki cross neut cm oe
    show kotonoha oe ldown
    k "Никого нет поблизости?"
    show natsuki om
    show kotonoha cm
    n "Не."
    show natsuki cm
    show kotonoha om rdown
    k "Хорошо, обстановка та, что надо."
    show natsuki turned happ cm oe lhip rhip
    show kotonoha ce
    k "Юри!"
    show kotonoha cm
    y "Э?"
    show natsuki laug om ce
    show kotonoha lsur cm oe
    n "Стягивай с себя одежду!"
    show natsuki cm
    y "А-а-а?!"
    show kotonoha angr om oe rhip
    k "Ай, Нацуки!"
    show natsuki om
    show kotonoha cm
    n "Ха-ха-ха!"
    show natsuki happ om oe
    n "Но ведь доля правды есть?"
    show natsuki cm
    show kotonoha anno om oe
    k "А-а-агх..."
    show natsuki neut cm oe ldown rdown
    show kotonoha neut om oe
    k "Не слушай её: просто стяни свои рукава."
    show kotonoha rdown
    k "Я хочу увидеть состояние твоих порезов."
    show natsuki curi cm oe
    show kotonoha cm
    y "З-з-зачем?"
    y "С ними всё в порядке!..."
    show kotonoha sad om oe
    k "Я буду аккуратна!"
    show kotonoha neut om oe
    k "К тому же никто, кроме нас, их не увидит."
    show kotonoha cm
    y "...умф..."
    show natsuki dist om ce rhip
    n "Я же говорила, она будет стесняться."
    show natsuki pout om oe
    n "Для неё показ рук всё равно, что показ интимной части тела."
    show natsuki cm
    "Я сейчас от стыда растворюсь..."
    show natsuki neut cm oe
    show kotonoha om e4a
    k "Прекрасно это осознаю."
    show natsuki rdown
    show kotonoha oe
    k "Юри, ты можешь мне доверять."
    show kotonoha happ om oe b2
    k "Я же твоя подруга, забыла?"
    show kotonoha cm
    y "..."
    "Почему я вообще впала в ступор?"
    "Я же ведь реально могу ей доверять..."
    show kotonoha -b2
    y "..."
    show natsuki worr cm e1a
    show kotonoha neut cm oe
    y "...вот."
    hide natsuki
    hide kotonoha
    show natsuki turned worr cm e1a school_bag at e21
    show kotonoha neut cm oe school_bag at e22
    with dissolve
    pause 0.5
    k "Хм-м-м..."
    show natsuki om
    n "Не настолько видные, как я думала..."
    show natsuki neut mb oe
    show kotonoha happ cm oe
    n "Вовремя тебя Макс заставил бинты наложить."
    show natsuki ma
    show kotonoha om
    k "Да, я думала, что будет хуже."
    show natsuki happ cm oe
    show kotonoha cm
    y "Ах-х, щекотно!"
    show kotonoha om ce
    k "Хе-хе."
    show natsuki neut cm oe
    show kotonoha neut om oe
    k "Правда, если приглядеться, то видны лёгкие следы..."
    show natsuki pout om oe
    show kotonoha cm
    n "Шрамы?"
    show natsuki cm
    show kotonoha sad om oe
    k "К сожалению..."
    show natsuki neut cm oe
    show kotonoha neut om oe
    k "Однако в глаза не бросаются."
    k "Не знаю, Юри, как у тебя так...{w}получилось {b}это{/b} сделать, но даже в {b}таком{/b} деле ты сохранила свою грациозность."
    show kotonoha cm
    y "О-о..."
    show natsuki anno cm oe
    show kotonoha sad om oe
    k "Но прошу: не надо травмировать своё красивое тело."
    k "Ты точно такое не заслуживаешь."
    show natsuki om
    show kotonoha cm
    n "Этими словами ты ничего не добьёшься."
    show natsuki dist om ce
    show kotonoha neut cm e1b
    n "Я раньше ей это говорила, Макс это говорил, уверена в этом."
    show natsuki oe
    n "Но Юри нас не слушает."
    show natsuki neut om oe b1d
    show kotonoha oe
    n "Да, Юри?"
    n "Мы все до сих пор не знаем, почему ты это делаешь."
    show natsuki cm
    y "..."
    show natsuki pout cm oe -b1d
    show kotonoha om
    k "Личная травма?"
    show natsuki om
    show kotonoha cm
    n "Да понятно, что травма."
    show natsuki e1b
    n "Что-то случилось не по её воле, а она на себя это накручивает."
    show natsuki oe
    n "Вот только это всё, что нам известно."
    n "А нам нужна причина."
    show natsuki anno om oe
    n "Причина покрыта мраком, как уже сказала."
    show natsuki angr om oe
    n "Потому что Юри у нас молчуша!"
    show natsuki cm
    y "Я не буду об этом говорить!"
    y "Не буду..."
    show natsuki pout cm oe
    show kotonoha lsur cm oe
    y "Мне страшно в этом копаться..."
    show kotonoha om
    k "Страшно?"
    show kotonoha cm
    y "Я не хочу переживать это вновь..."
    show natsuki om
    show kotonoha neut cm oe
    n "Ты сама себе противоречишь!"
    n "Если бы ты это не переживала, то не схватилась бы за нож."
    n "Не хочешь переживать -- вынь его из руки, положь обратно и расскажи про корень проблемы тем, кто хоть как-то может помочь."
    n "Мы же с тобой уже разговаривали на эту тему!"
    show natsuki cm
    y "..."
    show kotonoha lsur cm oe
    "Не думай, не думай, не думай, не думай, не думай..."
    show kotonoha om
    k "Юри-и-и..."
    k "Вернись к нам."
    show kotonoha cm
    y "А?"
    show kotonoha nerv om oe
    k "У тебя так резко ушёл взгляд куда-то вдаль, что я на секунду испугалась."
    show natsuki e1b
    show kotonoha cm
    y "Ох..."
    show natsuki om
    n "Мдэ."
    show natsuki cm oe
    show kotonoha neut cm oe
    y "Я...{w}э-э-э...{w}вы закончили?"
    show natsuki neut cm oe
    show kotonoha om
    k "О, да, можешь натягивать рукава."
    show kotonoha cm
    y "Хорошо."
    hide natsuki
    hide kotonoha
    show natsuki turned neut cm oe school_bag at i21
    show kotonoha neut cm oe school_bag at i22
    with dissolve
    pause 0.5
    "Не знаю почему, но хочется поскорее уединиться и забыться в книге."
    "Ощущение такое, будто мне руками мысли взбаламутили..."
    show natsuki curi cm oe
    y "Ещё раз простите, н-но я вспомнила, что мне надо кое-что доделать, поэтому мне придётся вас покинуть--{nw}"
    show natsuki pout cm e2a
    show kotonoha sad om oe
    k "Конечно-конечно, мы тебя не держим."
    show natsuki mh at h21
    show kotonoha cm
    n "Что?!"
    show natsuki cm
    show kotonoha happ cm oe rhip
    y "Встретимся в клубе, если что!"
    show kotonoha ce

    scene black with wipeleft_scene
    "Какая я нервная!"
    n "{size=19}Коха, ты понимаешь, что ты дала ей сбежать?{/size}"
    "Куда же мне уйти, куда же мне уйти..."
    k "{size=17}Ну...{w}и?{/size}"
    "Может, к торговому автомату на третьем этаже?"
    n "{size=15}Что \"и\"?{/size}"
    n "{size=14}Она опять убежала от проблемы!{/size}"
    "Или на крышу, или на крышу, или на крышу..."
    n "{size=13}Мы только к этой теме подошли, и такой облом!{/size}"
    "ДА, на крышу!"
    "Подышать свежим воздухом, который успокоит мой разум."
    "И даст почитать."
    "А ведь из-за мыслей я даже не открыла книгу--{nw}"
    play sound hit
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 0.25
    y "АЙ!"
    mc "Чёрт!"
    mc "Юри, ты не ушиблась?!"

    scene bg school f2 old_stairwell center
    show mc turned pani ma oe at t11
    with dissolve
    pause 0.25
    y "М-М-Макс?!"
    show mc om
    mc "Ну, в порядке?!"
    show mc pout ma oe
    y "Н-нет...{w}то есть да!"
    y "Да..."
    show mc cross pout om oe
    mc "Что-то ты совсем не в духе."
    show mc neut om oe
    mc "Хотя и я сегодня тоже не в своей тарелке."
    show mc cm
    y "У-у-у..."
    "..."
    "О-о-о..."
    show mc turned curi cm oe
    "А что, если..."
    show mc om
    mc "Ты, кстати, куда-то спешила?"
    show mc cm
    y "А-а-а, да!"
    show mc neut cm oe
    y "Э-э-э, не совсем, но...{nw}"
    show mc om e1e
    mc "Поспокойнее, Юри, у нас полно времени."
    show mc cm
    y "Не хотел бы ты подышать свежим воздухом?"
    show mc doub om e1c
    mc "...а?"
    show mc cm
    y "Я хотела почитать в тишине на крыше, но поняла, что это довольно...{w}рутинно."
    show mc neut cm oe
    y "Поэтому...{w}если ты...{w}составишь компанию, то я буду рада...{w}да..."
    show mc cross neut cm oe
    mc "Хм..."
    "Кажется, снова гормоны вошли в дело..."
    "Состояние, которое было пару минут назад, улетучилось начисто."
    "Теперь хочется провести время с Максом...{w}к тому же сейчас такой хороший повод!"
    show mc turned happ om oe
    mc "Ладно, почему нет?"
    mc "Одному проветриваться скучнее."
    show mc cm
    y "Хах, тогда идём!"
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_dialog("mc")

    call window_open
    play noise_1 wind fadein 3.0
    scene bg school old_rooftop day
    show yuri turned neut cm e1b school_bag at t11
    with wipeleft_scene
    "Уф, ветерок..."
    "Хоть от физ-ры отойду."
    show yuri e1d
    mc "Хм, пока довольно солнечно..."
    show yuri om
    y "Ты этому удивлён?"
    show yuri cm
    mc "Нет, просто сегодня передавали, что будет дождь где-то в промежутке между 12 и 18 часами."
    show yuri flus om oe
    y "Ах, точно, я про него уже забыла..."
    show yuri md
    mc "Ты брала с собой зонт?"
    show yuri neut om e1d
    y "...нет."
    show yuri cm
    mc "А если промокнешь по пути домой?"
    show yuri om
    y "Приложение в моём телефоне показывало, что осадки, вероятнее всего, придут к 4 или 5 часам после полудня."
    show yuri happ om oe
    y "Так что я успеваю."
    show yuri cm
    mc "Ладно, хоть так."
    show yuri neut om e1b
    y "К тому же зонтик громоздкий для моей сумки, его ручка будет торчать наружу, что не очень удобно."
    show yuri cm
    mc "Ясненько..."

    scene bg school old_rooftop day at old_rooftop_fence
    show yuri turned neut cm e1b school_bag at e22
    with dissolve_cg
    pause 0.5
    "Мда, снова натянутые разговоры..."
    "Но даются, на удивление, легко."
    show yuri happ om e1b
    y "Есть что-то в множестве падающих капель воды, правда?"
    show yuri cm
    mc "М-м...{w}наверное..."
    "Если дождь слабый, без всяких порывов ветра, то он даже успокаивает и создаёт особую атмосферу."
    "А вот если он льёт, как сумасшедший, и бьёт по окнам, то кажется, будто твой дом вырывается с корнем или на улице обрывается абсолютно всё, что висит."
    show yuri om
    y "Их шум создаёт релаксацию для мыслей."
    y "Всегда, когда идёт дождь, я становлюсь спокойной."
    show yuri neut om e1b
    y "Если это только не тайфун..."
    show yuri cm
    mc "Ха..."
    show yuri happ om oe
    y "Самое интересное, что Монике тоже нравится лёгкий летний дождь."
    show yuri cm
    mc "Да?"
    show yuri ce
    y "Угу."
    "Ещё одна крупица в картину Моники."
    show yuri oe
    "Не забыть бы потом все эти мелочи...{w}а ведь забуду!"
    show yuri e1b
    "..."
    "Что-то как-то вяло разговор идёт..."
    "Надо о чём-нибудь её спросить..."
    show yuri oe
    mc "Юри."
    show yuri om
    y "Да, Макс?"
    show yuri neut cm e1d
    mc "У тебя до клуба разве не было друзей или парня?"
    mc "А то ты очень местами скованная и волнующаяся, что не очень вяжется с твоим...{w}взрослым образом."
    show yuri e1b
    y "М-м-м..."
    show yuri om e1d
    y "Их практически не было."
    show yuri worr om oe
    y "Возможно, мои интересы не нашли поддержки у окружающих..."
    show yuri cm
    mc "Это печально."
    show yuri mb ce
    y "Не я выбирала, какой появлюсь на свет, хе-хе..."
    show yuri neut cm e1d
    mc "Но ведь всё-таки кто-то с тобой был?"
    show yuri om
    y "Родители."
    show yuri cm
    mc "Это понятно, я сверстников имел в виду."
    show yuri anno om oe
    y "Сверстники..."
    show yuri neut om e1d
    y "Котоноха и Нацуки."
    show yuri e1b
    y "В последнее время ещё Либитина, но она больше как знакомая, появляющаяся исключительно с первой."
    show yuri cm e1d
    mc "Вообще удивительно, как ты могла подружить с Нацуки."
    mc "Если бы я оценивал её развитие психотипа, то поставил бы ниже тебя."
    mc "Но это не значит, что он хуже или глупее."
    mc "Ну, я думаю, ты поняла."
    y "М-м."
    show yuri curi md oe
    mc "Почему вас тянет к друг другу?"
    show yuri om
    y "...у меня нет ответа на этот вопрос."
    show yuri dist om oe
    y "Вероятно, нас свело общее несчастье."
    show yuri cm
    mc "Одиночество?"
    show yuri neut cm e1d
    y "Угу."
    show yuri om
    y "Она ведь тоже была одна во времена средней школы..."
    show yuri cm
    mc "Да, Нацуки уже рассказывала."
    show yuri om
    y "И про прозвище?"
    show yuri happ cm oe
    mc "И про прозвище."
    show yuri om ce
    y "Хе-хе..."
    show yuri e1b
    y "Мы тогда случайно пересеклись у правой лестницы на первом этаже старого корпуса."
    y "Это очень тихое и уютное место, которое я выбрала для погружения в миры книг."
    show yuri cm
    mc "Не бывал там ещё."
    show yuri om oe
    y "Могу как-нибудь сводить."
    show yuri cm
    mc "Ха, можно."
    show yuri om e1b
    y "В общем, я сидела на лестнице и читала, как сейчас помню, красную книгу с глазом на обложке."
    show yuri neut om e1b
    y "Она была про компьютерную игру в средневековом сеттинге, которой школьники, учившиеся в Англии, тайно делились друг с другом."
    show yuri cm
    mc "Звучит нестандартно."
    show yuri neut om e1d
    y "Да, но мне книга не очень понравилась."
    show yuri flus om oe
    y "То есть мне она не понравилась не из-за того, что плохо сделана, нет, она написана хорошо..."
    show yuri dist om oe
    y "А из-за того, что...{w}не моё это: атмосфера и всё в таком духе."
    show yuri cm
    mc "Понятно."
    show yuri flus cm oe
    y "Что-то я опять отвлеклась..."
    show yuri e1d
    mc "Да ладно, не парься."
    show yuri neut cm e1d
    mc "Что там дальше было?"
    show yuri om
    y "Ну, Нацуки сначала меня не заметила."
    show yuri e1b
    y "Она подошла к торговому автомату, который стоит там до сих пор, чтобы купить себе газировку."
    show yuri happ om e1b
    y "Я от неожиданности, что кто-то мог прийти в такое тихое место, начала икать."
    show yuri ce
    y "И первый раз я икнула так громко, что Нацуки резко дёрнулась и чуть не выронила бутылку."
    show yuri cm
    mc "Пхе, весело."
    show yuri om oe
    y "Не то слово."
    y "Но тогда мы обе получили порцию адреналина."
    show yuri cm
    mc "И с того момента вы стали часто проводить время вместе?"
    show yuri om ce
    y "Да."
    show yuri e1b
    y "Иногда читали: я -- книгу, она -- мангу."
    y "Иногда перекусывали."
    y "Иногда просто разговаривали."
    y "Но всегда старались проводить время вместе."
    show yuri neut cm e1d
    mc "И прям без конфликтов?"
    show yuri om
    y "Практически."
    show yuri e1b
    y "Редко доходило до чего-то такого..."
    show yuri e1d
    y "А если и доходило, то мы быстро восстанавливали отношения."
    show yuri cm
    mc "Хм..."
    mc "А Котоноха?"
    show yuri om
    y "Мы с ней повстречались уже в старшей школе и сразу нашли общий язык."
    show yuri happ om e1b
    y "Нацуки даже подмечала, что я с ней очень похожа."
    show yuri cm
    mc "Ха, есть такое."
    show yuri neut cm e1d
    mc "Кстати, теперь понятно, почему Нацуки так болезненно отреагировала в пятницу..."
    show yuri worr om oe
    y "Д-да, я что-то совсем в себя погрузилась и забыла про неё."
    show yuri cm
    mc "Вообще я часто наблюдал у вас разлады, особенно на фоне стихотворений."
    show yuri neut cm e1d
    mc "Почему так вышло?"
    show yuri om
    y "...на этот вопрос у меня тоже нет ответа."
    show yuri curi cm oe
    mc "Отношения изживают себя?"
    show yuri e1b
    y "У-у..."
    mc "Ну, бывает такое, что когда люди полностью познают друг друга, то их начинает взаимно отторгать."
    show yuri neut cm e1d
    mc "Хотя, с другой стороны, Нацуки за тебя цепляется..."
    show yuri om
    y "Тут всё сложно и непонятно даже мне."
    show yuri cm
    mc "Подожди."
    show yuri curi md e2a
    mc "А может ли быть такое, что Нацуки своего рода твой паразит?"
    show yuri om
    y "Э?"
    show yuri md
    mc "А-а-а, я в том плане...{w}она так привыкла к тебе, что не захочет отпустить, когда придётся это сделать."
    show yuri neut cm e1d
    mc "А это приведёт уже к пагубным последствиям как для тебя, так и для неё самой."
    show yuri om e1b
    y "Я не смотрела на всю ситуацию под таким углом..."
    show yuri cm
    mc "Самое время посмотреть."
    mc "Если выяснится, что моё предположение верно, то лучше начать уже сейчас разрывать отношения, пока они не усугубились."
    mc "А если нет, то...{w}не надо это делать."
    show yuri dist om oe
    y "Честно, парочка моментов подходит под твоё описание, но не более."
    show yuri neut om e1d
    y "Наоборот, некоторые действия и фразы с её стороны настолько пропитаны искренней дружбой и ответственностью, что меня они поражают."
    show yuri worr mb oe
    y "Вот бы она всегда такой была..."
    show yuri ma
    mc "Хм-м, вот как значит..."
    "Наверное, моё предположение верно, но с одним жирным «но»."
    show yuri dist cm oe
    "Нацуки способна отдавать себе отчёт, хоть и с трудом."
    "И способна развиваться и прислушиваться к окружающим, которым доверяет."
    show yuri ma
    mc "Однако вы всё равно часто конфликтуете."
    show yuri mb
    y "Хех, взросление..."
    show yuri neut cm e1d
    mc "Или образование новых проблем, которые вам мешают?"
    show yuri om
    y "Скорее, всё комплексно."
    show yuri happ om oe
    y "Как бы то ни было, мы работаем над этим."
    show yuri e1b
    y "Да и невозможно обойти конфликты стороной."
    show yuri cm
    mc "М-м..."
    show yuri om ce
    y "Ах, довольно мило видеть, как ты за нас волнуешься."
    show yuri cm
    mc "Вы же часть клуба, как тут не волноваться?"
    show yuri oe
    mc "Было бы странно, если бы я был равнодушным."
    show yuri om
    y "Это точно."
    show yuri cm
    "..."
    show yuri e1b
    "Что-то у меня голова поплыла..."
    "Кажись, надышался кислородом."
    mc "Фу, меня как-то штормить начало."
    show yuri neut cm e1d
    mc "Пойду тогда обратно."
    show yuri lsur om oe
    y "Ой, уже?"
    show yuri worr om oe
    y "Ладно..."
    show yuri happ om ce
    y "Удачи!"
    show yuri cm
    mc "Удачи."

    scene black with wipeleft_scene
    stop noise_1 fadeout 6.0
    mc "Уф-ф-ф..."
    "Потихоньку история Литературного клуба перестаёт быть мраком."
    "Хотя есть ли там что-то из ряда вон выходящее?"
    "Клуб -- как клуб, ничего такого."
    play noise_1 school_corridor_empty_noise fadein 6.0
    "Хм, состою в нём всего полторы недели, а я уже с ним так сроднился..."
    mc "Неотъемлемая часть..."
    n "{size=19}О, Макс.{/size}"
    k "{size=19}Привет!{/size}"
    mc "А?"

    scene bg school f2 old_stairwell center
    show kotonoha happ cm oe school_bag at t21
    show natsuki cross neut cm oe school_bag at t22
    with dissolve
    pause 0.25
    mc "А, здрасьте."
    show kotonoha neut cm oe
    show natsuki curi om oe
    n "Ты Юри не видел?"
    show kotonoha lsur cm oe
    show natsuki neut cm oe
    mc "Я с ней только что разговаривал на крыше."
    show natsuki turned sedu cm oe school_bag
    mc "Она туда подышать и почитать пошла."
    show kotonoha happ cm oe
    show natsuki ce
    mc "А тебе зачем?"
    show kotonoha neut cm oe
    show natsuki om
    n "Нужно!"
    show natsuki happ om oe lhip rhip
    n "Коха, за мной!"
    show natsuki cm at thide
    hide natsuki
    mc "..."
    show kotonoha at t11
    pause 0.2
    show kotonoha om rhip
    k "Я её руки посмотрела."
    show kotonoha happ om oe
    k "Ты, кстати, молодец: заставил Юри пойти на хороший шаг."
    show kotonoha ce
    k "Рубцы практически не видны."
    show kotonoha cm
    mc "Ага..."
    show kotonoha neut om oe
    k "В общем, после осмотра она переволновалась и ушла быстрым шагом."
    show kotonoha cm
    mc "А-а-а, теперь понятно."
    show kotonoha nerv cm oe
    mc "Вы её хотите додолбать?"
    show kotonoha neut cm e1c
    n "{size=19}Где ты там?!{/size}"
    show kotonoha om
    k "Иду-иду!"
    show kotonoha nerv om e1a
    k "Н-нет, уладить всё..."
    show kotonoha ce
    k "Ну ты понял!"
    show kotonoha cm
    mc "...понял, наверное."
    show kotonoha rdown at thide
    hide kotonoha
    pause 1.0
    "Мда, весело вам..."
    "Туда-сюда бегают, развлекаются."
    "Что ж, а мне куда?"
    "Времени ещё полно."
    "Торчать где-то, как придурок, совершенно не хочется."
    "В мобильнике ничего интересного нет, там полнейшая тишина, как обычно."
    "Пха, когда я в последний раз видел уведомление о сообщении от кого-либо, кроме мессенджера по контактам телефона?"
    "А ведь раньше это было нечто ожидаемым и волнующим."
    "Постоянно открывал сообщения об уведомлениях, как упаковку на подарках."
    "А теперь...{w}теперь я удивляюсь, как раньше от этого зависел."
    "Таким наивным и добрым был..."
    "Зря."
    "Очень {b}зря{/b}."
    "Но я уже неоднократно поднимал эту тему."
    "Хватит мусолить одно и то же -- отвратно, блин!"
    "На нытьё больше смахивает."
    "Или я просто не могу избавиться от всего того осадка, что получил от тех событий..."
    y "{size=19}Хах-хах-хах-хах-хах...{/size}"
    "Что это за звуки?"
    show yuri turned lsur om oe n2 school_bag at t11
    y "Пфу, ой, Макс, ты не ушёл?"
    show yuri cm
    mc "Да, застрял что-то на месте..."
    show yuri happ om ce
    y "Пойдём я тебе покажу своё тихое место."
    show yuri cm
    mc "Что?"
    show yuri oe
    mc "Ты же не говорила, что прямо сегодня."
    show yuri nerv om oe
    y "Планы поменялись."
    show yuri happ om ce
    y "Пойдём!"
    show yuri cm
    mc "Стой, Юри, не несись ты--{nw}"
    hide yuri
    show yuri turned laug cm ce n2 lup rup school_bag at e11
    with dissolve
    mc "ТА-А-А-А-А-А-А-АК!{nw}" with vpunch

    scene black with wipeleft_scene
    play noise_2 mc_steps_school_run
    play noise_3 yuri_steps_run
    mc "{sc=3}У меня ноги полузабитые!{/sc}"
    y "{sc=3}У меня тоже тело не в форме!{/sc}"
    mc "{sc=3}Ай, ступеньки!{/sc}"
    "{sc=3}Вроде бы помятый, а вроде бы ещё в тонусе,\nраз так быстро по ним спускаюсь!{/sc}"
    y "{sc=3}Фу, я немного вспотела!{/sc}"
    mc "{sc=3}Тогда хватит бежать!{/sc}"
    y "{sc=3}Н-нет, Макс, мы должны прийти к моему тихому\nместу!{/sc}"
    mc "{sc=3}Дай угадаю: ты просто убегаешь от Нацуки и\nКотонохи!{/sc}"
    y "{sc=3}Ты их видел?{/sc}"
    mc "{sc=3}Даже парочкой слов перебросился!{/sc}"
    mc "{sc=3}Что они тебе такого сделали?{/sc}"
    mc "{sc=3}Всё ж в порядке, разве нет?{/sc}"
    stop noise_2
    stop noise_3

    scene bg school f1 old_stairwell right
    show yuri turned flus mj e1a n2 school_bag at t11
    with dissolve
    show yuri cm ce
    y "Нет!" with vpunch
    mc "Почему?!"
    show yuri oe
    y "Они..."
    show yuri pani om ce lup rup at h11
    y "Я не хочу вспоминать прошлое!"
    show yuri nerv om oe
    y "Иначе сознание снова начнёт шалить..."
    show yuri mj
    mc "Шалить сознание?"
    show yuri sad cm ce ldown rdown
    mc "Хочешь сказать, что ты иногда видишь всякие размытые образы?"
    show yuri om oe
    y "...образ...{w}один...{w}да."
    y "Редко...{w}но...{w}у меня была пара эмоциональных моментов, когда он приходил..."
    show yuri ce
    y "Угх..."
    show yuri cm
    "Ё-моё, как тут всё запущено..."
    show yuri e1a
    mc "Ладно, я понял, забудь пока про всё это."
    show yuri neut cm e1d
    mc "Так..."
    show yuri lsur cm oe
    mc "Мы же пришли, правильно?"
    show yuri om lup rup
    y "Ой, да, точно!"
    show yuri neut om e1d ldown rdown
    y "Это та самая лестница, на которой я постоянно провожу время."
    show yuri happ cm oe
    mc "Уютненько..."
    show yuri om ce
    y "Именно."
    show yuri oe
    y "Мне здесь очень нравится."
    show yuri neut cm e1d
    mc "Леса строительные зачем-то тут стоят..."
    show yuri anno om oe
    y "Это...{w}не помню, с какого конкретного времени..."
    show yuri dist om oe
    y "Они, по-моему, около полугода здесь находятся."
    show yuri neut cm e1d
    mc "Серьёзно?"
    mc "Тут же ничего не делается."
    show yuri om
    y "Сама не знаю, почему их не убрали."
    show yuri e1b
    y "Но они не мешают."
    show yuri e1d
    y "Тут всё равно практически никто не ходит: все предпочитают центральную лестницу."
    show yuri happ om oe
    y "Ну а мне это на руку."
    show yuri cm
    mc "Ясненько."

    scene bg school f1 old_stairwell right at f1_old_stairwell_right_board with dissolve
    mc "А плакаты тут какие-то наклеенные...{w}почему на английском?"
    show yuri turned neut cm e1b school_bag at e22 with easeinright
    show yuri om
    y "Это Клуб английского языка их сделал."
    y "Они висят уже больше года точно."
    show yuri lup
    y "Были много где расклеены, но многие из них по мере неактуальности были содраны."
    show yuri happ om oe ldown
    y "Так что можешь считать их за раритет."
    show yuri cm
    mc "Прикольно..."
    show yuri neut e1d
    mc "Подожди, они с другими клубами сотрудничали?"
    show yuri e1b
    mc "Или схожей деятельностью промышляли?"
    show yuri om
    y "Ты про музыку и выпечку?"
    show yuri cm
    mc "Да."
    show yuri dist om ce
    y "Меня тоже посещала такая мысль..."
    show yuri neut om e1d
    y "Мне кажется, что они могли как-то договориться о временной кооперации."
    show yuri worr om oe
    y "...не знаю, я не в курсе всего того, что происходит с клубами."
    show yuri neut om e1d
    y "По крайней мере, Нацуки мне ничего не рассказывала про сотрудничество Клуба выпечки с кем-либо."
    show yuri cm
    mc "Хм..."
    "Не очень понятно, что там написано, из-за моего не очень хорошего уровня английского..."
    show yuri e1b
    "Можно было бы прогнать текст через переводчик, но мне лень."
    "Всё равно, пробежавшись глазами, я ничего такого интересного не выделил."
    "Разве что сам факт существования целого плаката с музыкой..."
    show yuri e1d
    "Музыкальный клуб давно сдох, а эта бумажка до сих пор здесь торчит в целости и сохранности."
    "...какое-то странное ощущение."
    show yuri om
    y "Макс?"
    show yuri cm
    mc "А, я что-то снова задумался..."
    show yuri happ om oe
    y "Ничего-ничего, эти плакаты меня тоже сначала сбивали с толку."
    show yuri cm
    mc "Своей старостью?"
    show yuri neut om e1b
    y "Да."
    show yuri dist om oe
    y "Это будто какой-то отголосок прошлого, который забыли убрать."
    y "Как фотография, только ненужная и лишняя."
    show yuri cm
    mc "Хм..."
    show yuri anno om oe lup
    y "Один раз я даже хотела их содрать и выкинуть..."
    show yuri cm
    mc "...но явно этого не сделала."
    show yuri neut om e1d ldown
    y "Да."
    show yuri happ om oe
    y "Решила их оставить, потому что они вписываются в антураж."
    show yuri dist om oe
    y "Пустая доска смотрелась бы...{w}пусто."
    show yuri neut cm e1d
    n "{size=17}Говорила же, она сюда вернётся!{/size}"
    show yuri lsur om oe
    y "О нет, опять они..."
    show yuri cm
    mc "Значит попробуем всё уладить."

    scene bg school f1 old_stairwell right
    show yuri turned lsur cm oe school_bag at i11
    with dissolve
    pause 0.25
    show kotonoha vsur om oe n4 school_bag at l31
    show natsuki turned flus cm ce n2 school_bag at l32 zorder 2
    show yuri at t33
    pause 0.5
    show kotonoha ce n3
    k "Пха!"
    show kotonoha m5
    show natsuki md
    k "Ха..."
    show kotonoha m6
    show natsuki om e1a
    n "Юри, стой на месте и..."
    show natsuki happ om oe b1f n1 lhip rhip
    show yuri neut cm e1d
    n "...ихи-хи, уже Макса подцепить успела?"
    show natsuki cm
    show yuri e2c n2
    y "..."
    show natsuki -b1f
    mc "Как видишь."
    show natsuki om ce
    show yuri n3
    n "С такой ловкостью она точно не пропадёт!"
    show kotonoha neut om ce n1
    show natsuki cm
    show yuri neut cm e1d n1
    k "Так, фух..."
    show kotonoha sad om oe lself rhip
    show natsuki neut cm oe ldown rdown
    k "Юри, прости, что заставили волноваться, честно!"
    show kotonoha ldown
    show natsuki pout cm oe
    show yuri b1b
    k "Я не думала, что ты так близко это воспримешь."
    show kotonoha cm
    show yuri flus om oe -b1b lup
    y "Ох...{w}да, прощаю..."
    show kotonoha neut cm oe
    show natsuki om
    show yuri neut cm e1d ldown
    n "Но только это не меняет ситуацию!"
    show natsuki lhip rhip
    n "Юри, почему--{nw}"
    show natsuki curi cm oe
    mc "Потому."
    mc "Нацуки, не надо."
    show natsuki angr cm oe
    mc "Хватит теребить Юри."
    show natsuki om
    show yuri lsur cm oe
    n "Эй, слышь, бойфренд неполноценный!"
    show natsuki cm
    mc "Что?"
    show natsuki om
    n "А-а-а..."
    show natsuki cross vang om ce school_bag
    show yuri neut cm e1d
    n "А ничто!"
    show kotonoha sad cm ce
    show natsuki mj
    mc "Вот и всё!"
    show kotonoha om
    k "Нацуки права, понимание проблемы не сдвинулось ни на сантиметр, но и ты, Макс, тоже прав..."
    show kotonoha m2
    show natsuki angr cm oe
    k "В общем, мы пока закроем тему, ладно?"
    show kotonoha lsur cm oe rdown
    show natsuki turned angr om oe lhip rhip
    show yuri lsur cm oe
    n "Никаких \"ладно\"!"
    show natsuki cm
    mc "Нацуки, успокойся, блин, пожалуйста!"
    show kotonoha neut cm oe
    show natsuki pout cm oe
    show yuri neut cm e1d
    mc "Я прекрасно понимаю, что ты очень переживаешь за свою подругу, но ты ей сейчас только боль и дискомфорт приносишь такими попытками."
    show natsuki ldown rdown
    mc "Ничего не случится, если вы обсудите эту тему чуть позже, когда Юри будет готова это рассказать."
    show natsuki curi cm oe
    mc "Да, Юри?"
    "Ведь расскажешь, да?"
    "Мне в первую очередь."
    y "..."
    show yuri shoc om oe lup rup at h33
    y "А!"
    show natsuki anno cm oe
    show yuri sad om oe
    y "Д-д-да..."
    show natsuki om ce
    show yuri cm
    n "Она никогда не будет готова..."
    show kotonoha rhip
    show natsuki cm
    show yuri ldown rdown
    mc "Откуда такая уверенность?"
    show natsuki pout om oe rhip
    show yuri worr cm oe
    n "Макс, аргх, пойми: каждый раз Юри избегает эту тему, как огня, а её странное поведение и проблема только усугубляются!"
    n "Сколько можно?!"
    show natsuki rdown
    n "Ну сколько можно, а?"
    show natsuki cm
    show yuri ce
    mc "И при этом ты молчала о проблеме до вчерашнего дня и ничего нам не говорила..."
    show natsuki e1b
    n "..."
    show yuri pout om ce
    y "В-всё, ребята, хватит!"
    show kotonoha lsur cm oe rdown
    show natsuki neut cm oe
    show yuri oe
    y "Расскажу я об этом Максу в ближайшее время!"
    show natsuki curi cm oe
    y "Давайте на этом закончим."
    show kotonoha neut cm oe
    show natsuki om
    show yuri cm
    n "Эй-эй-эй, а как же мне?"
    show kotonoha happ cm oe
    show natsuki angr cm oe
    show yuri neut cm e1d
    mc "Пха-ха, а тебе рано ещё -- маловата."
    show natsuki om at h32
    show yuri laug cm oe
    n "Я маловата?!"
    show kotonoha om ce rhip
    show natsuki cm
    show yuri om ce
    ky "Ха-ха-ха!"
    show kotonoha cm
    show natsuki cross vang cm oe school_bag
    show yuri cm
    n "Кх-х..."
    "Да уж, ответ на мой мысленный вопрос не заставил себя ждать..."
    show natsuki mj
    show yuri happ cm ce
    "Осталось только дождаться и сам рассказ."
    show kotonoha om oe
    show natsuki neut cm oe
    show yuri oe
    k "Кстати, я так понимаю, Юри, ты решила провести для Макса мини-экскурсию в своё укромное место?"
    show kotonoha cm
    show natsuki lsur cm oe
    n "Кпмф..."
    show natsuki nerv cm e1b
    show yuri om
    y "Да."
    show yuri om e1b
    y "Лестница, вот...{w}плакатики..."
    show natsuki neut cm oe
    show yuri cm
    mc "Точно."
    show kotonoha neut cm oe
    show natsuki turned curi cm oe school_bag
    show yuri neut cm e1d
    mc "Нацуки, вопрос."
    show natsuki om
    n "Что?"
    show natsuki cm
    mc "Один плакат связан с выпечкой."
    mc "А сам плакат от Клуба английского языка."
    show natsuki om
    n "Ну?"
    show natsuki cm
    mc "Он имел общее дело с Клубом выпечки?"
    show natsuki om
    n "Общее дело..."
    show natsuki neut om e1b b1b
    n "Да кто ж их знает?"
    show natsuki oe -b1b
    n "Возможно, с бывшим президентом и имели, когда-то про это краем уха слышала."
    n "Но уже куча времени с того момента прошло."
    show natsuki cm
    mc "Понятно."
    show natsuki curi om oe lhip rhip
    n "А тебе почему интересно стало?"
    show natsuki cm
    mc "Обычное любопытство."
    show kotonoha e1b
    show natsuki neut cm oe
    show yuri curi md oe
    mc "Да и промелькнула в голове одна мысль, что мы могли бы через Клуб английского языка охладить пыл Кохаку..."
    show natsuki anno om ce
    n "Как только что сказала, времени прошло дофига."
    n "Президент сменился, да и состав тоже."
    show kotonoha oe
    show natsuki neut om oe
    show yuri neut cm e1d
    n "Так что эта идея, мягко говоря, неактуальна."
    show natsuki cm
    mc "Мдэ, ладно."
    show natsuki ldown rdown
    "Ожидаемо."
    show kotonoha lsur om oe rdown at h31
    show natsuki pout cm oe
    k "Ох, я же обещала с Либитиной разобрать одну задачку по алгебре."
    show kotonoha happ om oe b2
    show natsuki cm
    k "Простите, отделюсь от вас."
    show kotonoha ce -b2 lup
    show natsuki pout cm oe
    show yuri happ cm oe
    k "До встречи в клубе!"
    show kotonoha cm ldown
    show yuri om ce lup
    y "До встречи!"
    show yuri cm ldown
    hide kotonoha with easeoutleft
    show natsuki at t21
    show yuri oe at t22
    pause 0.2
    show natsuki curi cm oe
    show yuri neut cm e1d
    mc "Ладно, и я пойду, пока время позволяет."
    show yuri lsur om oe
    y "Ох, тоже?"
    show natsuki om e1b
    show yuri cm
    n "Блин, только вчетвером собрались..."
    show natsuki cm
    show yuri neut cm e1d
    mc "Ничего, в клубе вшестером будем."
    show natsuki neut cm oe
    show yuri happ cm oe
    mc "Всё, до скорого."
    show yuri om ce lup rup
    y "До скорого!"
    show yuri cm

    scene black with wipeleft_scene
    "Чёрт, как ноги-то забиты..."
    "Чую, вечером по полу ползать буду."
    stop noise_1 fadeout 5.0
    call window_close

    call window_dialog_long_transition(transition = False)

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    "..."
    "Ну что..."
    "Как обычно, минус ноги."
    "А если точнее, то бедренные мышцы."
    "Даже зарядка на физ-ре не помогает."
    "Слишком много бега и ходьбы на ногах, особенно когда я давно целенаправленно этим не занимался."
    "Примерно такие же ощущения, как после пробежки с Сайори и похода в магазин."
    "И это причём уже третье занятие за этот год."
    mc "Ух, ё..."
    "Я обязательно выживу..."
    show mrs_ida sad cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Какой-то ты совсем выжатый..."
    show mrs_ida cm
    mc "Физ-ра."
    show mrs_ida neut cm oe
    mc "Много мышц давно не задействовались, теперь ломят."
    show mrs_ida om
    mi "М-м, вот оно что..."
    show mrs_ida happ om ce
    mi "Я уж боялась, что что-то плохое произошло."
    show mrs_ida cm
    "Вообще-то так и есть."
    show mrs_ida at thide
    hide mrs_ida
    "Но вот стоит ли рассказывать про эти кошмары?"
    "Если так подумать, то смысл?"
    "Что скажет миссис Ида?"
    "Или что посоветует, куда обратится?"
    "Это всё очень чревато."
    "Начиная от волнения самой миссис Иды и заканчивая волнением моих родителей и меня из-за того, что мне надо будет посещать кого-то там, где-то там..."
    "И хрен знает, что мне нашьют."
    "И как это в дальнейшем отразиться на моей жизни."
    "Одно дело в чате с кем-то переписываться, как с каким-то знакомым, другое -- посещать официальное заведение с кучей документов и отчётов."
    mi "Эй-эй."
    mc "Бр-р-р!" with vpunch
    show mrs_ida neut cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "У тебя был застывший взгляд."
    show mrs_ida cm
    mc "В себя провалился, извините."
    show mrs_ida sad cm oe
    mc "Со мной такое часто."
    show mrs_ida om
    mi "Ох..."
    show mrs_ida cm
    mc "Мне пора в клуб..."
    mc "До свидания, Ида-сэнсэй."
    show mrs_ida om
    mi "У-у, угу..."
    show mrs_ida cm

    scene black with wipeleft_scene
    "Кажется, всё равно придётся ей о кошмарах рассказать."
    "Моё состояние меня же и выдаёт..."
    call window_close

    call plot_transition

    call window_open
    scene bg corridor with wipeleft_scene
    mc "Пф-ф-ф..."
    "Что вчера полудохлый пришёл, что сегодня..."
    "Хорош разваливаться, а?"
    "Тебе только пару месяцев назад 18 стукнуло."
    "Хотя за это короткое время я успел изрядно погореть, даже не повидав истинной взрослой жизни..."

    scene bg school old_corridor door with dissolve
    pause 0.25
    mc "Всё, сейчас открою дверь и как развалюсь на стуле..."
    call skip_block_on

    call screen club_door_lock_screen
    pause 0.5
    mc "{sc=1}......{/sc}"
    call screen club_door_lock_screen
    pause 0.5

    call skip_block_off
    mc "{color=#fc7e23}Let{/color}...{w}{color=#fc7e23}let me in{/color}!"
    mc "{color=#fc7e23}LET ME I-I-I-I-Э-Э-Э-Э-Э-Э-Э-Э-Э--{/color}{nw}"
    y "Макс, у меня ключ." with vpunch
    mc "{sc=2}Пха-апх-х-хпх-х!{/sc}"

    scene bg corridor
    show yuri turned lsur cm oe lup rup school_bag at t11
    with dissolve
    mc "{sc=0.5}А-а-а...{/sc}"
    mc "Юри, не пугай меня так..."
    show yuri om ldown rdown
    y "Я сама чуть не испугалась."
    show yuri neut cm e1d
    mc "...просто у меня ноги дико ноют, очень хочется присесть."
    show yuri om e1b
    y "Ах, вот оно что..."
    show yuri cm e1d
    mc "Тебе ключ Моника передала?"
    show yuri om
    y "Да."
    y "Она, как обычно, чуть-чуть задержится за роялем."
    show yuri happ om e1b
    y "Видно, её сегодня посетило вдохновение..."
    show yuri cm oe
    mc "Пытается усердно выучить какую-то мелодию?"
    y "Угу."
    show yuri lsur om oe
    y "Ой, давай я тебя уже впущу, а то твои ноги потрясываются."
    show yuri cm
    mc "Да не, я в но..."
    "Блин."
    "А ноги-то реально дёргаются..."
    show yuri e2b
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show yuri turned neut cm e1d school_bag at t43
    with wipeleft_scene
    "{sc=1}А-а-а, свободное кресло!{/sc}"
    show yuri e1d

    scene bg club_day with wipeleft_scene
    mc "Фу-у-ух-х-х..."
    mc "Как хорошо..."
    show yuri turned worr cm e1a school_bag at t11
    pause 0.2
    show yuri om
    y "Прости, зря тебя сегодня гоняла и на ногах держала..."
    show yuri cm
    mc "Ой, Юри."
    show yuri neut cm e1d
    mc "Не доводи себя до фанатизма."
    mc "Нет тут ничего такого, всё в порядке."
    show yuri anno cm oe
    y "М-м..."
    show yuri at thide
    hide yuri
    pause 0.2
    "Эмпатия у неё хорошо развита, но слишком часто она перерастает в самобичевание."
    "Мне это абсолютно не нравится."
    "Да мне весь негатив в Юри не нравится!"
    "Если взять и пустить всё в свободное плавание, то корабль под именем «Юри» в один момент взорвётся и стремительно затонет."
    "Прямо как крупный авиносец Тайхо во времена Второй мировой."
    "Заехали буквально одной торпедой в носовую часть этой махины, а потом повреждённые баки с топливом стали высвобождать пары нефти."
    "Которые ещё и разнеслись по всему кораблю благодаря вентиляции и открытым дверям (типо так хотели их «выветрить»)."
    "В итоге, то ли из-за искр в электродвигателе, то ли из-за чего-то ещё, пары сдетонировали с чудовищной силой, разорвав нос корабля в щепки."
    "Крупный авианосец в течение нескольких часов превратился в затонувший разорванный труп из-за одной торпеды и неопытности экипажа."
    "И вот с Юри примерно такая же ситуация."
    "«Торпеда» в неё уже «успешно» пущена: негативная ситуация, в которой она была, произошла."
    "Эффект от неё, а-ля пары нефти, начал накапливаться, и накапливается до сих пор."
    "И если мы, в частности именно я, будем тупить или ничего с этим не делать, то любой повод, как искра, взорвёт Юри нахрен."
    "И вот тогда никто не сможет её восстановить."
    "Будем честны, в таком случае она схватится за нож и отнюдь не с целью получить порезы, что кончится...{w}фатально."
    show yuri turned happ cm oe at t11
    pause 0.2
    show yuri om
    y "О чём-то задумался?"
    show yuri cm
    mc "А, я...{w}да как обычно, в себя провалился."
    show yuri om e1b
    y "Понятно."
    show yuri cm oe
    n "{size=19}Йо!{/size}"
    mc "О, привет."
    show yuri om
    y "Снова привет, Нацуки."
    show natsuki turned neut cm oe school_bag at t21
    show yuri cm at t22
    pause 0.2
    show natsuki curi om oe lhip rhip
    n "Вы тут только вдвоём, да?"
    show natsuki cm
    mc "Ага."
    show natsuki dist om ce ldown rdown
    n "Значит, пойду мангу читать."
    show natsuki cm at thide
    hide natsuki
    show yuri om e1b at t11
    y "А я совместный с Моникой стих перепроверю."
    show yuri cm
    mc "Угу."
    show yuri ce at thide
    hide yuri
    pause 0.2
    "Один я тут дурачок, сижу на кресле перед всем классом..."
    "Ах, точно, у нас же с Нацуки вышла полная брехня, а не стих."
    "Значит, я буду не дурачком, а полнейшим идиотом."
    "..."
    "И этот человек ещё что-то говорил про самобичевание Юри..."
    s "{size=19}Привети-и-ик всем!{/size}"
    k "{size=19}Здравствуйте!{/size}"
    mc "О-о-о..."
    "Вяло помахал, конечно, но и так сойдёт."
    "Пусть пока они там все подтягиваются и готовятся -- дух переведу."
    "Хотя бы голова не пульсирует, и на том спасибо."
    s "{size=19}Юри, как руки?{/size}"
    s "{size=19}Всё хорошо?{/size}"
    y "{size=19}У-у-у...{/size}"
    k "{size=19}Сайори, мы уже проверяли сегодня, говорила же...{/size}"
    s "{size=19}Лучше лично спросить!{/size}"
    "Да что вы все, как сговорились..."
    "Нет, я хотел, чтобы наше окружение было в курсе проблемы Юри и помогало ей самой преодолевать вызванные трудности...{w}но не так настырно же."
    "Юри такими темпами по-настоящему задолбают."
    show sayori turned happ cm oe at t11
    pause 0.2
    show sayori om
    s "Макс, привет!"
    show sayori neut cm oe
    mc "Я уже махал вам, но привет."
    show sayori curi om oe
    s "Да?"
    show sayori e2b
    s "Не заметила..."
    show sayori cm
    mc "Бывает."
    show sayori neut om oe
    s "А ты почему тут?"
    show sayori cm b1d
    mc "Тело после физ-ры ломит."
    show sayori om
    s "Это потому что ты со мной практически не бегал!"
    show sayori cm -b1d
    mc "Поверь, Сайори, там были такие упражнения, которые делали более сильный упор на мышцы, незатрагиваемые при беге."
    show sayori sedu cm oe
    mc "Короче, эффект был бы тот же."
    show sayori mb
    s "Не оправдывайся."
    show sayori cm
    mc "Не оправдываюсь."
    show sayori mb
    s "Но ведь оправдываешься."
    show sayori laug cm oe
    mc "Сайори!"
    mc "...аргх."
    show sayori om ce
    s "Хи-хи-хи!"
    show sayori cm
    mc "Мышцы горят, время горит, нервы тоже."
    show sayori happ om oe
    s "Может, я тебе массаж сделаю?"
    show sayori cm
    mc "...внутренние бедренные мыщцы."
    show sayori neut cm oe
    mc "Не уверен, что это «хорошая» идея, особенно на людях."
    show sayori om b1f
    s "И ты будешь терпеть побаливание?"
    show sayori cm
    mc "Да?"
    show sayori -b1f
    mc "Сайори, всё норм, далеко не первый раз такое было."
    show sayori om e2b
    s "Или у меня дома можно."
    show sayori e2c
    s "Или у тебя..."
    show sayori cm
    mc "Сайори."
    show sayori laug ma oe
    mc "Давай не будем доводить ситуацию до абсурда."
    show sayori om
    s "Ладно-ладно!"
    show sayori happ om oe
    s "Но если что, обращайся сразу, хорошо?"
    show sayori cm
    mc "Само собой."
    show sayori at thide
    hide sayori
    pause 0.2
    "В моей голове всё ещё не может уложиться милосердие Сайори в мою сторону."
    "Что она во мне такого нашла?"
    "Хотя этот вопрос применим ко всем участникам клуба."
    "...а не тупо ли уже так думать?"
    "Если порыться в себе, то ответ найдётся сразу."
    "Но почему тогда до клуба все мои качества практически не поощрялись..."
    "Ай, сплошные парадоксы на парадоксах, которые парадоксами погоняют."
    m "{size=19}Ух, фу, я прибежала!{/size}"
    s "{size=19}А-а?{/size}"
    s "{size=19}Мони, куда ты так торопилась?!{/size}"
    m "{size=19}Я не опоздала?{/size}"
    y "{size=19}Нет, мы только-только вместе собрались.{/size}"
    m "{size=19}Фу-у-ух...{/size}"
    s "{size=19}Не надо так бегать, мы бы подождали!{/size}"
    m "{size=19}Но задерживать вас я не хочу.{/size}"
    m "{size=19}Ладно, не об этом.{/size}"
    m "{size=19}Все готовы к нашему второму обмену?{/size}"
    y "{size=19}Да?{/size}"
    n "{size=19}Да давайте уже, чего время тянуть...{/size}"
    m "{size=19}Ха, хорошо.{/size}"
    show kotonoha happ cm oe at t51
    show sayori turned happ cm oe at t52 zorder 2
    show monika forward happ cm oe at t53 zorder 3
    show natsuki turned neut cm oe at t54 zorder 2
    show yuri turned happ cm oe at t55
    pause 0.2
    play music t5 fadein 3.0
    show monika om lpoint rhip
    m "Итак, друзья!"
    show kotonoha neut cm oe
    show sayori neut cm oe
    show monika lsur om oe ldown rdown
    show natsuki curi cm oe
    show yuri lsur cm e2b
    $ currentpos = get_pos(channel="music")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music fadeout 3.0
    m "Ой, Макс, ты прямо не свой, как и вчера перед обменом..."
    show sayori curi cm oe
    show monika md
    show natsuki pout om oe lhip rhip
    show yuri neut cm e1d
    n "Ты, кстати, за вчерашнее не извинился!"
    show sayori neut cm oe
    show natsuki cm
    mc "Да блин, тихо, стойте!"
    show kotonoha happ cm oe rhip
    show sayori laug cm oe
    show monika laug cm oe
    show natsuki lsur cm oe
    show yuri laug cm oe
    mc "Первое: о Великая повелительница кексов и манги, снизойди до простого смертного и прими от него большое человеческое извинение за некотролирумое действие."
    show kotonoha ce
    show natsuki nerv om oe ldown rdown
    show yuri ce
    n "Да куда ж так пафосно?"
    show kotonoha om
    show monika ce
    show natsuki cm
    k "Хе-хе-хе!"
    show kotonoha cm
    show sayori happ cm oe
    show monika happ cm oe
    show natsuki neut cm oe
    show yuri neut cm e1d
    mc "Второе: я после физ-ры ещё не отошёл."
    show kotonoha oe
    show monika om e1b
    m "А-а-а..."
    show kotonoha neut cm oe
    show sayori om lup rup at h52
    show monika neut cm oe
    show natsuki curi ma oe
    show yuri lsur cm e2c
    s "Да, у Макса бедренные мышцы болят, особенно внутренние!"
    show sayori cm ldown rdown
    "Говорить такие подробности-то зачем?!"
    show sayori neut cm oe
    show natsuki mc lhip rhip
    show yuri neut cm e1d
    n "Теперь ты будешь ковылять в раскоряку?"
    show natsuki ma
    show yuri angr cm oe
    mc "Не надо строить из меня инвалида."
    show kotonoha rdown
    show natsuki doub cm oe ldown rdown
    show yuri om
    y "Нацуки, это грубо!"
    show sayori anno cm oe
    show monika anno cm oe
    show natsuki om
    show yuri cm
    n "Что, даже подколоть нельзя?"
    show monika angr om oe
    show natsuki cm
    m "Ребят, хватит!"
    show sayori neut cm oe
    show monika neut om ce
    show natsuki neut cm oe
    show yuri neut cm e1d
    m "Все локальные вопросы уже выяснены, поэтому..."
    play music t5c fadein 3.0
    show kotonoha happ cm oe
    show monika happ om oe lpoint rhip
    m "Итак, друзья."
    show sayori happ cm oe
    show monika ldown rdown
    show yuri happ cm oe
    m "Начинаем второй обмен совместными стихами."
    show natsuki e1b
    m "Подготавливайтесь и говорите, как будете готовы."
    show kotonoha e1b at thide
    hide kotonoha
    show sayori ce at thide
    hide sayori
    show monika cm at thide
    hide monika
    show yuri at thide
    hide yuri
    pause 0.2
    show natsuki at t11
    "Чую я, что Моника сегодня в нас разочаруется..."
    show natsuki oe
    "Ну или это только мы с Нацуки два дурачка."
    show natsuki curi cm oe
    "В любом случае, даже несмотря на все мои вчерашние уверенно сказанные слова, как-то стыдно показывать такой...{w}стих."
    show natsuki om
    n "Ну ты это...{w}готов?"
    show natsuki neut cm oe
    mc "Всегда готов."
    show natsuki e1b
    mc "Куда я денусь..."
    show natsuki om
    n "Ха..."
    show kotonoha happ cm oe rhip at t51 zorder 2
    show sayori turned happ cm oe at t52
    show natsuki cm zorder 2
    show monika forward happ cm oe at t54 zorder 3
    show yuri turned happ cm oe at t55
    pause 0.2
    show natsuki oe
    show monika om lpoint rhip
    m "Ну что, ребята, с кого начнём?"
    show kotonoha nerv cm oe
    show natsuki worr cm oe
    show monika cm ldown
    "..."
    show sayori neut cm oe
    show monika neut om oe
    show yuri neut cm e1d
    m "Снова нет желающих?"
    show monika cm
    "..."
    show kotonoha neut cm oe
    show monika om ce rdown
    m "Ой..."
    show kotonoha happ cm oe
    show sayori happ cm oe
    show natsuki neut cm oe
    show monika happ om oe
    show yuri happ cm oe
    m "Хорошо, моя пара выступит первой."
    show monika lpoint
    m "Юри?"
    show kotonoha at thide
    hide kotonoha
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki
    show monika cm ldown at t21
    show yuri e1b at t22
    pause 0.2
    play sound paper_torn_out
    show yuri lup_item poem_paper with dissolve
    pause 1.0
    show yuri om oe rup
    y "Вот."
    y "Держите стих."
    show yuri cm rdown
    mc "Я снова читаю?"
    show monika om
    m "Думаю, да, у тебя это прекрасно получается."
    show monika cm
    show yuri ldown -poem_paper with dissolve
    play sound paper_torn_out
    pause 1.0
    show monika neut cm oe
    show yuri neut cm e1d
    mc "При моём-то грубом голосе?"
    show yuri om
    y "Разве он грубый?"
    show yuri cm
    s "Присоединяюсь к вопросу!"
    n "Присоединяюсь к душнилам!"
    n "Макс, читай давай."
    show monika happ cm oe b1b
    show yuri anno cm oe
    mc "Ах-х..."
    mc "Так..."
    show monika -b1b
    show yuri happ cm oe
    stop music fadeout 3.0
    call show_poem(poem_my)
    "......"
    call window_close

    play sound applause_small
    show monika neut cm oe
    show yuri neut cm e1d
    pause 2.0
    show monika happ cm oe b1b n3
    show yuri laug cm oe n3
    pause 1.0
    show yuri shy happ cm oe n5 at s22
    pause 2.0
    show monika ce
    pause 1.0

    call window_open
    show monika om
    m "Ладно-ладно, хватит."
    show monika oe
    m "Вы немного преувеличиваете..."
    show monika cm
    s "Ничего не преувеличиваем!"
    mc "Да, это...{w}очень качественно."
    show monika n1 -b1b
    show yuri n1
    mc "Как будто этот стих написан одним человеком."
    show yuri turned happ cm oe lup rup at t22
    mc "Не знаю, как вам удалось войти в «суперпозицию», соединив стили друг друга..."
    n "Да-а-а, эту планку никто не перепрыгнет..."
    k "Не то слово!"
    show monika e1b
    show yuri om e1c
    y "Ух..."
    show monika om
    show yuri cm
    m "Может, вы и правы."
    show monika ce b1b
    show yuri neut cm e1d
    m "Но для меня подобный результат вполне обыденный."
    show monika neut cm oe -b1b
    show yuri ldown rdown
    mc "Однако прошлый стих тебе не очень понравился..."
    show monika om e1b
    m "Ну..."
    show monika cm oe
    mc "Моника, это не обыденность -- это достижение."
    show yuri happ cm oe
    s "Да, цени такой результат!"
    show monika happ cm oe b1b
    show yuri ce
    s "И Юри тоже!"
    show monika om ce
    m "Хах, конечно."
    show monika cm -b1b
    show yuri oe
    mc "И по смыслу очень классно вышло."
    show monika oe
    mc "Не думал, что вы вдохновитесь мифологией..."
    show yuri om
    y "В ней очень много идей, которые так и просятся стать частью творческого продукта."
    y "Поэтому надо этим пользоваться."
    show yuri cm
    mc "Хм..."
    show monika neut cm oe
    n "Но там свои заверченные примочки..."
    show yuri om
    y "В этом и смысл."
    show monika happ cm oe
    show yuri ce lup
    y "Мифология -- отражение восприятия народом окружения, пускающее корни из древности."
    show yuri dist om ce
    y "Божества, олицетворяющие явления природы, духи, олицетворяющие страхи и всякое..."
    show monika neut cm oe
    show yuri neut cm e1d
    k "Бр-р-р, Юри, тебя опять Либитина покусала?"
    show yuri om ldown
    y "Что?"
    show monika laug cm oe
    show yuri cm
    k "Давайте сменим тему разговора..."
    show monika mb ce
    m "Ха-ха-ха, хорошо."
    show monika cm
    play sound paper_torn_out
    pause 1.0
    show monika happ om oe lpoint rhip
    show yuri curi cm e1b
    m "Что насчёт как раз ваших работ?"
    show monika cm ldown rdown
    "..."
    show yuri neut cm e1d
    mc "Котоноха?"
    show monika at thide
    hide monika
    show yuri at thide
    hide yuri
    show sayori turned happ cm oe at t21
    show kotonoha neut om oe rhip at t22
    k "Э?"
    show sayori nerv cm oe
    show kotonoha nerv om oe
    k "А-а, интересно, но маловато..."
    show kotonoha cm
    m "Всё равно показывайте!"
    show sayori happ cm oe
    y "Да, очень любопытно."
    show kotonoha om ce
    k "Я смущаюсь!"
    show sayori om ce
    show kotonoha lsur cm oe
    s "Именно поэтому стих у меня."
    show sayori cm
    play sound paper_torn_out
    show sayori lup poem_paper with dissolve
    pause 1.0
    show kotonoha om
    k "Что?"
    show sayori neut cm oe
    k "Когда ты успела его забрать?"
    show sayori curi om oe
    show kotonoha cm
    s "В смысле?"
    show sayori neut om oe
    show kotonoha neut cm oe
    s "Я же перед обменом его взяла."
    show sayori cm
    show kotonoha om
    k "А-а-а..."
    show kotonoha happ om ce
    k "Ой, всё."
    show sayori happ cm oe
    show kotonoha nerv om oe
    k "Что-то я переволновалась..."
    show kotonoha cm
    y "Не переживай, всё в порядке вещей."
    show kotonoha ce
    m "Расслабься."
    show kotonoha om
    k "Хех..."
    show sayori om ce
    show kotonoha cm
    s "Так, нате!"
    show sayori cm
    play sound paper_torn_out
    show sayori ldown -poem_paper with dissolve
    pause 1.0
    show sayori oe
    show kotonoha happ cm oe
    mc "Приступим..."
    call show_poem(poem_ks)
    show sayori neut cm oe
    show kotonoha neut cm oe rdown
    m "Как-то...{w}маловато для пары?..."
    mc "Первый раз же."
    show sayori happ cm oe
    show kotonoha happ cm oe
    mc "В целом, читается очень складно, легко и позитивно."
    mc "Котоноха, молодец, сразу нашла свой стиль: спокойный и плавный."
    mc "И ты, Сайори, тоже молодец."
    y "Да, полностью согласна."
    show kotonoha rhip
    n "Угу, прикольно."
    show sayori ce
    show kotonoha om ce
    k "Ох, спасибо."
    show sayori om lup rup at h21
    show kotonoha cm
    s "Е-е-е!"
    show sayori cm ldown rdown
    play sound paper_torn_out
    pause 1.0
    show sayori oe
    show kotonoha oe
    m "Да, молодцы..."
    show sayori neut cm oe
    show kotonoha neut cm oe
    mc "Ты рассчитывала на весь исписанный лист, что ли?"
    m "Нет, но..."
    n "Моника, хватит мямлить!"
    n "Даже маленькие стихи -- это стихи!"
    y "Вот-вот."
    y "Некоторые писатели вообще по пару четверостиший пишут и на этом закачивают."
    y "Да и мы в прошлом тоже так делали..."
    m "...ух, простите."
    m "Я что-то слишком...{w}замечталась, наверное."
    mc "Да ладно уж."
    show monika forward happ cm oe at t11 zorder 3
    show yuri turned happ cm oe at t54
    show kotonoha at t55 zorder 2
    pause 0.2
    show sayori happ cm oe zorder 2
    show monika om lpoint
    show kotonoha happ cm oe
    m "Теперь ваш черёд?"
    show monika cm ldown
    mc "...да."
    mc "Наш..."
    show sayori neut cm oe
    show monika neut cm oe
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "А оно вам надо?"
    show sayori happ cm oe
    n "Можно было бы...{w}э-э-э..."
    show sayori om ce lup rup at h21
    show monika happ cm oe
    show yuri happ cm oe
    show kotonoha happ cm oe
    s "Ещё как надо!"
    show sayori cm ldown rdown
    show monika om ce
    m "Не томите, показывайте!"
    show sayori oe
    show monika cm
    show kotonoha om
    k "Мы не будем осуждать, верно?"
    show monika oe
    show yuri ce
    show kotonoha cm
    y "Угу."
    "Совесть-то как грызёт..."
    show yuri oe
    mc "Держите..."
    play sound paper_torn_out
    show monika lup poem_paper with dissolve
    pause 1.0
    show sayori neut cm oe
    show monika e1b
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "Только про себя читайте!"
    show monika neut om oe
    m "Но это неудобно."
    show monika cm
    show yuri angr cm oe
    n "Не развалитесь!"
    show yuri om
    y "Нацуки, успокойся."
    show monika e1b
    show yuri anno om oe
    y "Что там может быть тако..."
    show sayori curi cm oe
    show monika vsur md e2b
    show yuri mg b2a
    y "...о-о..."
    show sayori om
    show yuri me
    show kotonoha at t42 zorder 1
    s "Что там?!"
    show sayori cm e2c at t52
    m "..."
    "А-а-а, чёрт!"
    "Я не могу смотреть на их выражения лиц!"

    scene black with dissolve
    pause 0.25
    "Сердце предательски забилось..."
    k "Пха-ха, что это?"
    y "Астрогусь?..."
    s "Какой ещё астрогусь?"
    n "{size=19}Буэ-э...{/size}"
    "Я сейчас от стыда сдохну на месте!"
    m "Это...{w}снова какая-то вакханалия, а не стих..."
    s "Мдэ-э-э..."
    "{sc=2}НЕТ-НЕТ-НЕТ-НЕТ-НЕТ-НЕТ-НЕТ-НЕТ-НЕТ--{/sc}{nw}"
    m "Так."

    scene bg club_day
    show sayori turned neut cm e2c at t52 zorder 2
    show kotonoha lsur cm oe at t42
    show monika forward worr cm ce lup poem_paper at t11 zorder 3
    show yuri turned neut cm e2b at t54 zorder 2
    with dissolve
    pause 0.25
    show monika om
    m "Ребят..."
    show monika neut om ce
    show yuri e1d
    m "Пф-ф-ф..."
    show monika cm
    play sound paper_torn_out
    show monika ldown -poem_paper with dissolve
    pause 1.0
    show sayori b1c at t41
    show monika mh b1b
    show yuri lsur cm oe
    show kotonoha neut cm oe at t55
    m "При всём моём уважении к вашему старанию и проделанной работе, мне абсолютно не нравятся ваши результаты."
    show sayori worr cm oe -b1c
    show monika worr om oe
    m "Можно с уверенностью сказать, что мы потеряли практически полтора обмена."
    show monika cm
    show kotonoha om rhip
    k "Полтора?"
    show sayori neut cm oe
    show monika neut om oe lpoint
    show kotonoha cm
    m "Получился стих Макса вчера, плюс мой стих с Юри и твой с Сайори сегодня."
    show monika cm ldown
    show yuri om oe
    y "М-Моника, ты же не хочешь сказать, что--{nw}"
    show monika om ce
    show yuri cm
    m "Хочу."
    show sayori sad cm oe
    show monika oe b1d
    show yuri worr cm e2c
    show kotonoha sad cm oe
    m "Я предлагаю отказаться от парного формата и перейти обратно к одиночному, преждевременно."
    show sayori om
    show monika cm
    s "Да ну-у-у!"
    show monika -b1d
    s "Моника, мы только начали!"
    show sayori md
    show yuri lsur om oe
    y "Ещё не все пары были испробованы, а я уверена, что будущие комбинации принесут хороший и интересный результат."
    show sayori neut cm oe at t51
    show natsuki turned fs neut cm oe b3 at t52
    show monika at t53
    show yuri cm
    pause 0.2
    show natsuki om
    show monika curi md oe
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "Простите..."
    show natsuki ce
    show yuri e1d b1f
    n "Это всё из-за меня."
    show natsuki cm
    show monika om
    m "А?"
    show natsuki oe -b3
    show monika neut mh oe lpoint
    m "Нет, Нацуки, ты не так поняла."
    show natsuki ff pani om oe
    show monika cm e2a ldown
    show yuri -b1f
    n "Прекрасно поняла, не надо тут подлизываться!"
    show natsuki pout om oe
    show monika e1a
    n "Ты же сама только что сказала, у кого стихи нормальными вышли."
    show natsuki cm
    show yuri worr cm oe
    show kotonoha sad cm e1c
    m "..."
    show natsuki fs neut cm ce b2
    show monika dist cm oe
    m "..."
    show natsuki oe -b2
    show monika neut cm oe
    show yuri lsur om oe
    show kotonoha neut cm oe
    y "Но не это ли повод модернизировать свой стиль?"
    show natsuki ff pout om oe
    show yuri cm
    n "Я просто хотела повеселиться, а не заниматься стихотворной бюрократией в паре с кем-то на ночь глядя."
    show sayori sad md oe
    show natsuki fs neut om ce b2
    show monika b1b
    n "Повеселиться...{w}и всё!"
    show natsuki m2
    show kotonoha sad cm oe
    m "..."
    show yuri e2b
    show kotonoha om
    k "Нацуки, не грусти..."
    show sayori om
    show monika ce
    show kotonoha cm
    s "Да, не раскисай!"
    show sayori cm
    show monika -b1b
    n "..."
    show monika om
    show yuri neut cm e1d
    show kotonoha neut cm oe rdown
    m "Хорошо."
    show sayori neut cm oe
    show natsuki cm oe -b2
    show monika oe
    m "Мы попробуем ещё один раз."
    show sayori happ cm oe
    show yuri happ cm oe
    show kotonoha happ cm oe
    m "Но в этот раз хорошенько распределитесь."
    show sayori mc e4c lup rup at h51
    show natsuki ff pout cm oe
    show monika happ cm oe
    show yuri laug cm ce
    show kotonoha ce
    s "УРА!"
    show sayori cm ce ldown rdown
    show monika om lpoint
    show yuri happ cm oe
    show kotonoha oe rhip
    m "И первый выбирать будет сама Нацуки."
    show sayori oe
    show natsuki om
    show monika cm ldown
    n "Я?..."
    show natsuki cm
    show monika om
    m "Поскольку ты потерпела неудачу 2 раза, то тебе нужно выбирать первой, причём выбрать такого человека, с которым ты гарантированно сможешь объединиться."
    show natsuki e1b
    show monika cm
    n "..."
    show sayori neut cm oe
    show natsuki curi om e1c
    show yuri neut cm e1d
    show kotonoha neut cm oe
    n "Э-э-э..."
    show natsuki cm
    n "..."
    show natsuki e1b
    n "..."
    show sayori flus om oe
    show natsuki neut om e1b
    show yuri happ cm oe
    show kotonoha happ cm oe
    n "...Сайори."
    show natsuki doub cm oe
    s "Что, серьёзно?!"
    show sayori cm
    show natsuki om lhip rhip
    show monika ce
    n "Нет, блин, по приколу!"
    show sayori curi om e1a
    show natsuki cm
    s "А вдруг!"
    show sayori cm
    show natsuki om
    n "Только п--{nw}"
    show sayori neut cm oe
    show natsuki neut cm oe
    show monika om oe lpoint rhip
    show yuri ce
    m "Прекрасно, надеюсь, у вас всё получится!"
    show sayori happ cm oe
    show natsuki ldown rdown
    show monika ldown
    show yuri oe
    m "Теперь распределяются остальные участники."
    show kotonoha e1b b2
    m "Кто кого выбирает?"
    show monika cm
    show kotonoha oe -b1b
    mc "Так, мадамы вперёд."
    show natsuki curi cm oe
    show yuri neut cm e1d
    mc "В смысле, дамы."
    show sayori laug cm oe
    show monika laug cm oe rdown
    show yuri laug cm oe
    show kotonoha ce rdown
    mc "Тьфу, леди."
    show sayori ce
    show natsuki neut cm oe
    show yuri oe
    show kotonoha om
    k "Ха-ха, как благородно!"
    show sayori ma
    show monika happ cm oe
    show yuri happ om oe
    show kotonoha cm rhip -b2
    y "Целесообразнее будет, если Котоноха попробует написать стих вместе с тобой, Моника."
    show sayori happ cm oe
    show natsuki worr cm oe
    show monika e1c
    show yuri cm
    show kotonoha oe
    m "Хм-хм-хм..."
    show natsuki neut cm oe
    show monika om oe
    show kotonoha neut cm oe
    m "Соглашусь, мне надо зафиксировать её стиль."
    show sayori neut cm oe
    show monika neut cm oe
    show yuri neut cm e1d
    show kotonoha om
    k "Я правильно понимаю, что мне...{w}повезло в некоторой степени?"
    show monika om
    show kotonoha cm
    m "В каком плане?"
    show monika cm
    show kotonoha om e1b
    k "Ну, вы же говорили, что Макс пытался писать во всех ваших стилях..."
    show sayori happ cm oe
    show natsuki happ cm oe
    show monika happ cm oe
    show yuri happ cm oe
    show kotonoha nerv om oe
    k "А для меня это было бы очень трудно."
    show monika om rhip
    show kotonoha cm
    m "Хах, в некоторой степени можно сказать и так."
    show natsuki neut cm oe
    show monika ce rdown
    show kotonoha happ cm oe
    m "Так...{w}так...{w}пфу-у, заговорилась уже."
    show monika oe lpoint
    show yuri ce
    m "Юри, тебе выпадает Макс."
    show monika ldown
    m "А посему все пары на завтра распределены."
    show sayori ce
    show natsuki e1b
    show monika lean happ om oe at h53
    show yuri oe
    show kotonoha ce
    m "Как обычно, надеюсь на ваш творческий результат!"
    show sayori neut cm oe
    show natsuki pout cm oe
    show monika forward flus om e1a
    show yuri neut cm e1d
    show kotonoha oe
    m "И подойдите в этот раз с большей серьёзностью и взаимопониманием."
    m "И если вдруг у вас не будет получаться стих, то не заставляйте себя его дописывать."
    show sayori happ cm oe
    show kotonoha b2
    m "Ваши связи куда важнее, чем строчки на бумаге, даже со вложенными в них чувствами."
    m "И даже важнее, чем моё желание увидеть хорошие стихи."
    show natsuki e1b
    show monika ma
    mc "Конечно..."
    show sayori om ce lup rup at h51
    s "Оки-доки!"
    show sayori cm ldown rdown
    show monika happ cm oe
    y "Угу."
    show sayori oe
    show natsuki oe
    show monika om ce lpoint rhip
    show yuri happ cm oe
    show kotonoha -b1b
    m "Итак, друзья!"
    show natsuki neut cm oe
    show monika oe ldown rdown
    m "Внеочередной обмен закончен."
    show kotonoha rdown
    m "Можете расходиться по домам."
    show sayori ce at thide
    hide sayori
    show natsuki e1b at thide
    hide natsuki
    show monika cm
    show yuri ce at thide
    hide yuri
    show kotonoha ce at thide
    hide kotonoha
    pause 0.2
    show monika ce
    "И все дружно, кроме Моники, живо побежали к портфелям."
    "Всё-таки не я один жажду поскорее оказаться дома, вне зависимости от событий и мероприятий."
    show monika om oe
    m "Решил не спешить?"
    show monika neut cm oe
    mc "Куда мне с моими-то ногами..."
    show monika curi om e1b
    m "Ой, точно, уже из головы вылетело."
    show monika md at thide
    hide monika
    show sayori turned happ cm oe school_bag at t22
    pause 0.2
    show sayori om
    s "Макс, я с Нацуки пойду, нам надо обсудить будущую стихотворную работу!"
    show natsuki turned neut cm oe school_bag at t21
    show sayori cm
    mc "Окей."
    show sayori om ce
    show natsuki happ cm oe
    s "Всем пока-пока!"
    show sayori cm
    show natsuki om
    n "Пока."
    show natsuki cm
    mc "До завтра."
    show sayori oe
    show natsuki e1c
    pause 0.2
    hide sayori
    hide natsuki
    with easeoutleft
    k "{size=19}А, ты одна живёшь?{/size}"
    m "{size=19}Да, поэтому могу тебя к себе пригласить, чтобы поработать над стихом.{/size}"
    m "{size=19}Напишу, как освобожусь.{/size}"
    k "{size=19}Ловлю на слове!{/size}"
    show kotonoha happ cm oe rhip school_bag at t43
    pause 0.2
    show kotonoha om
    k "Побежала закрывать дела!"
    show kotonoha cm
    m "{size=19}Удачи!{/size}"
    show kotonoha ce rdown
    hide kotonoha with easeoutleft
    pause 0.2
    show yuri turned neut cm oe school_bag at t11
    pause 0.2
    show yuri om
    y "М-Макс..."
    show yuri cm
    mc "А?"
    show yuri mg e1b b1b
    y "У-у..."
    show yuri me
    y "..."
    show yuri cm e1d -b1b
    mc "Я понял, пойдём."
    show yuri happ om ce
    y "Хе..."
    show yuri cm
    mc "Моника, мы ушли."
    show yuri oe
    m "{size=19}Хорошо!{/size}"
    show yuri om
    y "До встречи!"
    show yuri cm
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show yuri turned happ cm e1b school_bag at t11
    with wipeleft_scene
    show yuri neut cm e1d
    mc "Только, Юри, говорю сразу: хоть сейчас у меня ноги отпустило, но они всё ещё «горят»."
    mc "Чую, в процессе ходьбы развалюсь пуще прежнего."
    mc "Поэтому дойдём до перекрёстка, а там разойдёмся, ладно?"
    show yuri om
    y "Конечно, я не заставляю."
    show yuri happ om e1b
    y "К тому же у меня тоже...{w}тело немножко ватное после физкультуры и после нашего забега..."
    show yuri cm
    mc "Ха..."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 11 afternoon
    show yuri turned happ cm e1b school_bag at t11
    with wipeleft_scene
    show yuri om
    y "Кстати, твоя с Нацуки реакция во время нашего чтения была...{w}своеобразной."
    show yuri cm oe
    mc "Пха, потому что мы знали, ЧТО настрочили."
    show yuri neut om e1d
    y "И тем не менее вы решились показать даже такой результат?"
    show yuri cm
    mc "Это я настоял, причём вполне уверенно."
    mc "А в итоге от уверенности осталось одно слово и сожаление о выборе."
    mc "Лучше б выбросили, честное слово."
    show yuri dist om oe
    y "Но тогда бы Нацуки вышвырнуло на человека, с которым она не смогла бы скооперироваться."
    show yuri cm
    mc "...верно."
    show yuri neut cm e1d
    mc "Но всё равно противный осадок на душе."
    show yuri worr om ce
    y "От этого невозможно уберечься, к сожалению..."
    show yuri cm
    "Фу, будто мне палкой внутренности взбаламутили, теперь настрой ещё больше выбит."
    "Надо сменить тему."
    show yuri neut cm e1d
    mc "Когда будем составлять стих?"
    show yuri e1c
    y "М-м-м..."
    mc "Можно либо сегодня ближе к вечеру у меня, либо..."
    show yuri e1d
    mc "Хотя нет, завтра точно будет неудобно на переменах сидеть и думать."
    mc "А за одну большую мы не успеем всё отполировать."
    show yuri happ cm oe
    mc "Поэтому...{w}сможешь сегодня у меня?"
    show yuri om
    y "Да, я так и планировала."
    show yuri e1b
    y "Хотя я думала, что мы можем это сделать у меня..."
    show yuri oe
    y "Но у тебя тоже можно."
    show yuri cm
    mc "Понятно, хорошо, что мы в одном ключе думаем."
    show yuri om
    y "Согласна."
    show yuri cm
    "Такое ощущение, что Юри распланировала всё на несколько шагов вперёд."
    show yuri e1b
    "Меня это начинает пугать."
    "Чем ближе она ко мне будет, тем больнее от меня отлепится в будущем."
    "Чёрт, да что же с ней делать?!"
    "Как мне это спустить на тормоза?"
    show yuri oe
    mc "В общем, Юри, я тебе напишу, как освобожусь."
    mc "Примерно к 6-ти вечера, а может, и раньше."
    show yuri om
    y "Поняла."
    show yuri cm
    mc "Если у тебя ноги тоже разболятся, то лучше дома останься, дистанционно всё придумаем."
    show yuri om ce lup
    y "Не переживай, я в хорошем тонусе."
    show yuri cm
    mc "Учти."
    show yuri oe ldown
    mc "А, ещё зонт всё-таки не забудь."
    show yuri om
    y "Надеешься на дождь?"
    show yuri cm
    mc "Не отпускает это чувство."
    mc "Не думаю, что ты хотела бы остаться у меня на целый день."
    show yuri om e1b
    y "Как знать..."
    show yuri cm
    "Блин, ляпнул двусмысленно..."
    "Голова мутная, мысли совершенно не контролируются."
    show yuri oe
    mc "Ну ладно, пойду к себе домой, пока ещё живой."
    show yuri om ce
    y "Буду ждать сообщения!"
    show yuri cm oe
    mc "Удачи."
    show yuri om rup
    y "Удачи, Макс!"
    show yuri cm rdown
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    mc "Ну...{w}всё?"
    "С ДЗ покончил, с бытовыми делами тоже..."
    "Комнату прибрал, как и вчера перед приходом Нацуки."
    "И, в довершение всего, окончательно развалился."
    "Не, голову отпустило."
    "Но ноги полностью умерли."
    "Ходить нормально вообще не могу."
    mc "Ох-х-х..."
    mc "Надо написать Юри, пока время и оставшиеся силы позволяют."
    call skip_block_on

    $ contact_list["mc"].append("mc_y_chat")

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 58
        clock = (17, 22)

    phone discussion "mc_y_chat"
    $ plot_pause()
    phone discussion "mc_y_chat":
        time year 2018 day 26 month 4 hour 17 minute 22
        "mc" "Привет, Юри. Я покончил со всеми делами, готов к составлению стиха"
        "mc" "Как там у тебя дела обстоят?"
    $ phone.system.clock = (17, 23)
    "Правда, теперь надо дождаться ответа..."
    phone discussion "mc_y_chat":
        "y" "Привет! Всё хорошо. Я тоже готова"
    "Она держала телефон под рукой, ожидая моё сообщение, что ли?"
    phone discussion "mc_y_chat":
        "mc" "Класс. Тогда давай ко мне, а то уже скоро вечер"
        "y" "Конечно, уже иду"
    $ phone.system.clock = (17, 24)
    phone discussion "mc_y_chat":
        "mc" "Я ещё раз погоду посмотрел, передают дождь в ближайшие полчаса"
        "y" "Видела, но спасибо за предупреждение"
        "mc" "Угу"

    phone end discussion transition

    call skip_block_off
    "Может, пока подумать над стихом?"
    "Надо ж какие-нибудь идеи предложить..."
    call window_close

    call plot_transition

    play noise_1 rain_inside fadein 2.0
    pause 0.25

    call window_open
    "Ну кто же знал, что приложение соврёт и в итоге дождь начнётся через 10 минут?!"
    mc "Значит, только голова промокла?"
    y "Д-да..."
    y "Я успела к тебе забежать."
    mc "А я еле успел до двери доковылять."
    y "Но ведь успел же?"
    mc "Ох, блин, Юри..."
    mc "Нет, чтоб зонтик открыть..."
    "Так, нашлось всё-таки полотенце в шкафу."
    "Не буду ж я ей своё из ванны давать, которым целиком вытираюсь после душа?"
    "И для рук тоже давать не буду."
    "А так хоть будет чистое и новое."
    mc "Вот, достал."
    mc "Держи."
    y "Спасибо..."
    "Чем больше узнаю про Юри, тем сильнее кажется, что она в душе ребёнок."
    "Ну я в том плане, что ей как будто...{w}э-э-э, не хватило воспитания?"
    "Её авантюрные выпады тому подтверждение."
    "Я услышал звонок в дверь только спустя около полминуты, как дождь хлынул."
    "Потом кое-как добежал до неё, потратив где-то ещё секунд 10."
    "И всё это время Юри была без зонта в одном лишь бежевом свитере!"
    "Кстати, да, почему она решила именно в такую погоду выйти не в ветровке с накидкой, а в каком-то свитере?"
    "Мало того, что от ливня он никак не спасёт, так в нём и свариться можно."
    "Даже в такую погоду здесь не так холодно: сырость после дождей быстро уходит."
    "В общем...{w}у Юри проблемы с психикой по всем фронтам."
    "И самое мерзкое, что она хрупкая."
    "Не прям сильно, да и не всегда, но хрупкая."
    y "Спасибо, Макс."
    mc "А, всё?"
    mc "Тогда я заберу полотенце--{nw}"
    y "Подожди..."

    if cg_a1_d11_y.unlocked == False:
        $ cg_a1_d11_y.unlock()
    scene y_cg3_base with dissolve_cg
    pause 0.25
    y "Можешь подержать его так ещё немного?..."
    mc "А?"
    show y_cg3_exp1 at cgfade
    y "Оно очень мягкое..."
    y "Очень приятное ощущение."
    y "Хочу его получше запомнить..."
    mc "...ладно."
    "Вот что это, если не очередная авантюра?!"
    "Хотя подождите-ка..."
    "А что, если она хочет получить от меня всё то внимание и заботу, которых ей не хватало на протяжении жизни, а не тупо любовь из-за гормонов?"
    "Не на того ты должна расчитывать, Юри..."
    "Я уже выбрал Монику."
    "{b}Окончательно{/b} выбрал."
    "Вот если бы найти «мне» альтернативу, которую ты полюбишь ещё сильнее..."
    window hide

    pause 7.0

    window auto
    "Я только сейчас осознал, что в комнате стоит какой-то сладковатый и приятный запах."
    mc "Юри..."
    hide y_cg3_exp1
    y "...м?"
    mc "Ты решила тотально подготовиться к стиху, воспользовавшись духами, да?"
    y "Ах..."
    y "Да."
    y "Это жасмин."
    y "Для релаксации."
    show y_cg3_exp1 at cgfade
    y "Один из моих любимых цветков..."
    mc "Вот как..."
    "Чай с ним на чаепитии был очень вкусный."
    window hide

    pause 7.0

    window auto
    "Я вроде бы где-то видел, что...{w}ну-у-у..."
    "Пары жасмина -- своего рода природный афродизиак."
    "Но в каких объёмах это надо вдыхать и как долго, чтобы он дал такой эффект?"
    "Короче, опять какая-то тупая шальная мысль."
    "Я же не думаю, что Юри...{w}специально такие духи выбрала..."
    window hide

    pause 8.0

    window auto
    "Кажется, уйдя в себя, она по-настоящему наслаждается моментом."
    "...но моя рука сейчас расплавится от тепла полотенца."
    "И ноги готовы отвалиться при одной мысле о кресле или кровати..."
    "Придётся нарушить эту идиллию."
    mc "Юри, ты прости, но..."
    hide y_cg3_exp1
    y "...м-м?"
    mc "Ноги..."
    y "Ох..."

    scene bg bedroom
    show yuri shy casual neut om oe n3 at s11
    with dissolve_cg
    show yuri om
    y "Извини."
    show yuri ce
    y "Что-то я сегодня не в себе..."
    show yuri n5
    y "Забылась в мыслях..."
    show yuri cm
    mc "Ой, не переживай."
    show yuri turned lsur om oe lup rup n1 at t11
    y "Но у тебя же ноги разболелись."
    show yuri cm
    mc "Такие боли всегда так протекают: организм устал, вот и усилилось."
    show yuri neut cm e1d ldown rdown at t11
    "А если серьёзно, даже Юри в более лучшем состоянии, чем я."
    "Позор какой-то..."
    "Возможно, она периодически занимается спортом?"
    show yuri om
    y "Ты бы лучше прилёг на кровать..."
    show yuri cm
    mc "А стих писать как?"
    show yuri curi om e1b
    y "Э-э..."
    show yuri me
    mc "Давай, кстати, уже думать над содержанием, потому что время у нас не бесконечное."
    show yuri neut cm e1d
    mc "Какую тему ты хотела бы выбрать?"
    y "М-м-м..."
    show yuri e1b
    y "..."
    show yuri e1c
    y "..."
    show yuri om
    y "Не знаю..."
    show yuri cm
    mc "Я тоже в ступоре, но надо что-то всё-таки придумать."
    show yuri e1d
    mc "Есть вариант попробовать что-то простое."
    mc "Сложный стих как по строфам, так и по смыслу может выйти комом."
    mc "Из-за меня именно."
    show yuri om
    y "Думаешь, не сможешь подхватить ту же волну вдохновения, что и я?"
    show yuri cm
    mc "Да."
    mc "Вот простой стих у нас получится гарантированно."
    mc "Поэтому...{w}ну...{w}идей всё ещё нет."
    show yuri laug om ce
    y "Ха-ха-ха, мы обязательно что-нибудь придумаем!"
    show yuri cm
    "Придумаем..."
    "Как же я ненавижу создавать что-то с нуля."
    show yuri oe
    "Была бы основа -- пожалуйста, могу вокруг неё отплясывать куда угодно."
    "Но вот когда эту основу нужно создавать..."
    "Всегда ловлю в таком случае тупизм и блокировку идей."
    show yuri neut cm e1b
    "Будто влетел со всего размаха в стену, а теперь пытаюсь прийти в себя."
    show yuri lup
    "Или как программа, которая не знает, откуда брать данные, путь к которым вроде бы прописали в коде, а на месте их самих не оказалось."
    "Грх..."
    show yuri b1f
    "Впрочем...{w}есть одна мысль."
    show yuri ldown
    "В голове из последнего крутится только дождь."
    show yuri -b1f
    "И немного Моники вперемешку с Юри, но не на это акцент."
    mc "А что, если нам написать про дождь?"
    show yuri e1d
    y "Хм?"
    mc "И написать это так, будто бы создавалось ощущение падающих капель."
    mc "Как там это называется..."
    mc "Ну, когда специальные слова по звучанию подбирают, чтобы подчеркнуть описываемое окружение."
    show yuri om
    y "Звукопись?"
    show yuri cm
    mc "Точно!"
    mc "Вот, как раз можем это попробовать."
    show yuri anno md oe
    mc "Заодно посмотрим, насколько интересен данный приём."
    show yuri om
    y "Я такое ещё не практиковала..."
    show yuri md
    mc "О чём и говорю."
    show yuri happ om ce rup
    y "Любопытно стало попробовать, хах."
    show yuri cm
    mc "Тем более."
    show yuri oe rdown
    mc "Тогда пишем стих про дождь?"
    show yuri om
    y "Да."
    show yuri cm
    mc "Хорошо, садись сюда поближе..."

    call poem_act_1_day_11

    scene bg bedroom
    show yuri turned casual happ cm oe at t11
    with dissolve_scene_half
    call show_poem(poem_mcy)
    mc "Да, на удивление мои куски стиха читаются очень даже..."
    show yuri om
    y "Что я как раз и говорила."
    show yuri cm
    mc "Твои тоже."
    mc "Всё очень хорошо получилось."
    show yuri om e1b
    y "Хе..."
    show yuri cm oe
    mc "Единственное, что...{w}ну прямо чувствуется, как кульминация стиха просто взяла и оборвалась."
    show yuri om lup
    y "Но лучше уж так, чем скомканное и натянутое продолжение."
    show yuri cm
    mc "Тоже верно..."
    show yuri ldown
    mc "Ладно, дело сделано."
    show yuri ce
    mc "Фух..."
    "..."
    "......"
    "...и?"
    mc "Ну..."
    show yuri oe
    y "М-м?"
    show yuri neut cm e1d
    mc "Юри, ты сегодня мне невзначай обещала рассказать про свою проблему поподробнее..."
    show yuri om
    y "А-а..."
    show yuri anno om oe
    y "Точно."
    show yuri cm
    mc "Ну, э-э-э..."
    show yuri neut cm e1d
    mc "Тьфу!"
    show yuri happ cm oe
    mc "Надо избавляться уже от таких «звуков-паразитов»."
    show yuri om
    y "Согласна."
    show yuri e1b
    y "Они портят речь и ограничивают мышление."
    show yuri neut cm e1d
    mc "Нет, не в этом плане, а в том, что они с мысли сбивают."
    mc "Так, это...{w}о чём мы там, а-а-а..."
    mc "Аргх!" with vpunch
    mc "Короче!"
    mc "..."
    y "..."
    show yuri laug om ce
    y "Ха-ха-ха!"
    show yuri cm
    mc "О-о-о..."
    "Почему я не могу спокойно сформулировать мысль?"
    show yuri oe
    "Боюсь ударить Юри в лоб и спугнуть её от этой злосчастной темы, покрытой мраком?"
    show yuri happ cm oe
    mc "Юри."
    mc "Если ты не против..."
    show yuri neut cm e1d
    mc "Ты можешь сейчас исполнить своё обещание."
    show yuri e2a
    mc "У нас ещё осталось время, да и ты пока одна живёшь, ведь так?"
    mc "Плюс, наверное, всё сделала -- срочных дел нет..."
    show yuri lsur om oe lup rup at h11
    y "Д-да-да-да, я всё сделала!"
    show yuri cm
    mc "Вот, тем более."
    show yuri dist om ce
    y "Очень неожиданное предложение с твоей стороны..."
    show yuri neut om e1d ldown rdown
    y "Потому что я не планировала у тебя задерживаться."
    show yuri lsur cm oe
    mc "Если нет, то нет, всё в порядке!"
    show yuri om
    y "Н-нет!"
    show yuri nerv om oe
    y "То есть да!"
    show yuri cm
    y "Э-э-э..."
    show yuri flus cm oe
    y "Ой."
    show yuri laug cm oe
    mc "Пха, я тебя заразил."
    show yuri mb ce
    y "Ха-ха!"
    show yuri happ cm ce
    y "Кхм..."
    show yuri om oe
    y "Я не против остаться и рассказать о том, о чём обещала."
    show yuri neut om e1d
    y "Только давай куда-нибудь переместимся..."
    show yuri e1c
    y "Например..."
    show yuri happ om oe
    y "Можно сесть на твою кровать?"
    show yuri cm
    mc "Даже нужно, особенно полусидя-полулёжа."
    mc "Потому что она мягкая, а тело у меня уже ноет в некоторых местах."
    show yuri om ce
    y "Ох, хорошо!"
    show yuri cm
    mc "Тогда после Вас."

    scene black with dissolve
    pause 0.25
    y "Ух-х-х..."
    mc "Пф-ф-ф..."
    mc "Как хорошо расслабляться после долгого напряжения..."
    y "И не говори..."
    "..."
    "Мда, в итоге мы вдвоём сидим на кровати, упёршись спинами в подушки."
    "Да как у меня так получается?"
    "Я же хочу как можно меньше {b}подтекстов{/b} с Юри, но выходит ровно наоборот."
    "Пф, она как...{w}нет, не суккуб...{w}некое любовное божество, которое «дурманит» тебя своей аурой."
    "А может, надо тупо перестать зацикливаться на своих действиях?"
    "Но тогда я точно потеряю контроль над ситуацией."
    "Опять противоречие!"
    mc "Кх-х-х..."
    y "Макс."
    y "Это всего лишь мысли..."
    y "Не напрягайся."
    mc "...знаю."
    "Положила свою ладонь на мою..."
    "Какая она у неё мягкая, однако."
    "..."
    "......"
    y "Ты точно хочешь, чтобы я тебе это рассказала?"
    mc "Шутишь?"
    mc "Мы только на кровати пристроились."
    mc "А если серьёзно, то ещё с момента, когда ты мне свои руки в первый раз показала."
    y "А, да..."
    y "..."
    mc "..."
    "Её весь энтузиазм мгновенно испарился..."
    mc "Это очень больная для тебя тема, да?"
    y "...угу..."
    mc "Но вечно молчать не получится."
    mc "И чем раньше ты поведуешь об этом, тем проще будет, в первую очередь, тебе."
    mc "Да, с ходу ничего так не решится, но шаг к этому будет уже сделан."
    y "..."
    y "...помнишь наш разговор на прошлой неделе, когда ты меня проводил до дома?"
    mc "Э-э..."
    mc "Разговор..."
    mc "А-а, про книги и музыку?"
    y "Угу."
    mc "Смутно, но помню."
    y "Отец привозил новые из-за границы..."
    mc "Точно-точно."
    "Попахивает семейными проблемами..."
    "Юри вообще скисла."
    "О, знаю, как её отвлечь, не съехав с темы!"
    mc "Кстати, вопрос."
    mc "Такие книги же не на японском языке были?"
    mc "Твой отец, наверное, в разные страны летал, вряд ли там кто-то любезно переводил хоть что-нибудь на наш язык."
    y "Да, верно."
    y "Приходилось мучиться с английским, используя англо-японский словарь."
    "Отлично, наживка зашла без проблем."
    "Стоп, что?!" with vpunch
    mc "Ты знаешь английский?"
    y "У-у..."
    y "Не совсем, но более-менее читать без помощи переводчика могу."
    y "С быстрым понимаем смысла написанного."
    y "Хотя мне в этом отчасти поспособствовала мама, она работает переводчиком в туристической компании нашего города и хорошо знает русский и английский..."
    mc "Ничего себе..."
    mc "У вашей семьи явно есть предрасположенность к языкам."
    mc "Потому что я, может, и могу правильно читать предложения, но у меня при переводе много слов западает."
    mc "Банально их не знаю, а они, как назло, являются ключевыми в понимании смысла."
    y "Это можно исправить лишь постоянной практикой над языком."
    y "Чтение, просмотры видео -- что угодно, но с использованием английского."
    y "Поэтому это нормально, тебе нужно просто над этим работать."
    mc "Были бы время, возможность и желание..."
    y "Но по-другому никак."
    y "Ой, а ещё важно думать на этом языке."
    y "То есть не вспоминать, как какое-то слово переводится на японский, и анализировать после этого его смысл, а сразу пытаться устанавливать связь."
    y "Например: \"{color=#fc7e23}I'm really glad to spend time with you on this bed{/color}\", -- я сказала напрямую, так как знаю, что предмет с подушками, матрасом и одеялом -- {color=#fc7e23}bed{/color}."
    mc "У тебя даже практически акцента нет."
    mc "Я даже думать на английском не успеваю."
    mc "Особенно использовать в нём времена."
    mc "Настоящее время, прошедшее продолжительное время, время, где действия происходили фиг пойми когда, а результат нужен сейчас..."
    mc "Никогда не мог найти ту грань, когда нужно использовать одно, а когда второе, или вообще третье, если по смыслу не четвёртое..."
    y "Понимаю тебя, я тоже до сих пор в них полностью не разбираюсь."
    y "Но оно и не сильно нужно."
    y "Как выучишь главные и начнёшь находить закономерности, так сразу станет понятно."
    mc "В общем, фу, проехали."

    scene bg bedroom at mc_bed_deep
    show yuri turned casual neut cm e1d at e11
    with dissolve
    pause 0.25
    mc "Что-то мы отклонились от темы..."
    "Ну не рассчитал я, да!"
    show yuri dist md oe
    "Зато Юри стала расслабленее."
    show yuri om
    y "Значит, книги..."
    show yuri md
    mc "Да, из-за рубежа."
    show yuri sad cm oe
    mc "Их привозил твой отец."
    show yuri om lup rup
    y "Вот...{w}всё."
    show yuri cm
    mc "В смысле, всё?"
    show yuri lsur om oe
    y "Макс."

    $ nightmare_active = True

    y "{b}Его нет.{/b}"
    show yuri cm
    mc "..."
    mc "......"
    show yuri ldown rdown
    mc "...да?"
    show yuri sad cm oe
    y "..."
    mc "..."
    "ТВОЮ МАТЬ!" with vpunch
    "Самая ХУДШАЯ мысль из всех возможных, как оказалось, самая ВЕРНАЯ!"
    show yuri ce
    "Добавьте сюда бедность и комплексы, которая Юри не смогла побороть в одиночку, потому что ей не хватило помощи и внимания со стороны..."
    "...и на выходе вы получите потрясающий коктейль для разрушения психики мозга."
    mc "...а как...{w}это вышло?"
    show yuri worr cm oe
    mc "Сразу извиняюсь за то, что лезу тебе в больное место."
    show yuri mg
    y "Н-ничего..."
    show yuri e1a
    y "А вышло..."
    show yuri om ce
    y "Ф-ф-ф..."
    show yuri mg e1a
    y "Ты первый человек извне, которому я это рассказываю."
    show yuri oe
    y "Поэтому...{w}постараюсь сделать это ёмко и без эмоций...{w}на одном дыхании..."
    show yuri cm
    mc "Хорошо."
    show yuri e1a
    mc "Но если будет тяжело -- сразу останавливайся."
    show yuri mg
    y "Конечно..."
    show yuri cm ce
    y "Кхм..."
    show yuri dist om ce
    show black at custom_fade(0.1)
    window hide
    y_nvl "Мой отец по профессии был фотожурналистом: снимал фотографии для новостных агенств..." with Dissolve(1.0)
    hide black
    show black at custom_fade(0.2)
    show yuri oe
    y_nvl "На момент его жизни я была ещё не совсем взрослой, поэтому совершенно не разбиралась во всех подробностях его работы."
    hide black
    show black at custom_fade(0.3)
    show yuri ce
    y_nvl "Но я точно могу сказать, что он был профессионалом своего дела."
    hide black
    show black at custom_fade(0.4)
    show yuri neut om e1b
    y_nvl "В общем, на его фотографии был хороший спрос, однако ему самому часто приходилось летать в другие страны."
    hide black
    show black at custom_fade(0.5)
    show yuri dist om oe
    y_nvl "Он был в Европе, в Индокитае, в Южной и Северной Америке, в России..."
    hide black
    show black at custom_fade(0.6)
    show yuri ce
    y_nvl "Если разделить этот список на страны (кроме России, естественно), то он будет очень большой."
    hide black
    show black at custom_fade(0.7)
    show yuri oe
    y_nvl "И вот, где-то примерно 5 лет назад во второй половине апреля, когда я начала учиться в средней школе, он отправился по одному заданию в Филиппины."
    hide black
    show black at custom_fade(0.8)
    show yuri anno om oe
    y_nvl "Там что-то было связано с политикой: вроде бы какие-то всеобщие выборы..."
    hide black
    show black at custom_fade(0.9)
    show yuri neut om e1b
    y_nvl "Но это не столь важно: мой папа сделал фотографии, о которых просили."
    hide black
    show black at custom_fade(1.0)
    show yuri dist om ce
    y_nvl "26 апреля он написал нам, то есть мне и маме, что купил билет обратно, по которому самолёт вылетит в тот же день, где-то ближе к вечеру."
    y_nvl "Ночью папа должен был прибыть в Нагою, откуда на ночном автобусе приехал бы к нам к утру."
    y_nvl "Я тогда, как обычно, с нетерпением ждала, когда он вернётся, несмотря на короткий срок его отсутствия."
    y_nvl "Моя мама полностью разделяла моё состояние."
    y_nvl "В общем, всё было в порядке вещей за исключением того, что я была очень уставшей, из-за чего решила лечь спать раньше обычного: в 8 часов после полудня."
    y_nvl "Перед тем, как уснуть, я всегда проверяю телефон."
    y_nvl "И в тот момент я увидела сообщение от папы, которое отпечаталось в моей голове:"
    y_nvl "\"Спокойной ночи, дорогая Юри.\""
    y_nvl "\"Я горжусь тобой и люблю тебя больше всего на свете.\""
    y_nvl "\"Будь смелой и верь в себя.\""
    y_nvl "\"Папа всегда рядом.\""
    y_nvl "Я...{w}сначала не поняла всей ситуации..."
    y_nvl "Подумала, что он мне просто написал на ночь парочку добрых слов."
    y_nvl "Уже не помню, как ему ответила, но точно взаимностью."
    y_nvl "И вот, наступил следующий день."
    y_nvl "Перед тем, как собраться и пойти в школу, я завтракаю с мамой, смотря всякие новости по телевизору."
    y_nvl "Тогда было то же самое."
    y_nvl "Я ей попутно рассказала о сообщении папы, отчего она явно забеспокоилась, хотя не подала виду."
    y_nvl "Мама предположила, что он мог внезапно задержаться по работе или в самом аэропорту."
    y_nvl "Но ведь папа бы тогда написал об этом..."
    y_nvl "Пока мы думали и гадали, что же произошло, в наши разбирательства влез телевизор."
    y_nvl "В нём была...{w}экстренная и короткая новость...{w}несколько фраз из которой у меня тоже отпечатались в памяти...{w}они звучали так:"
    y_nvl "\"Рейс из Тайбэя в Нагою...{w}при заходе на посадку...{w}потерпел крушение...\""
    y_nvl "\"...по предворительным данным...{w}пилоты\nпотеряли управление...\""
    y_nvl "\"...самолёт вертикально влетел в землю\nрядом со взлётно-посадочной полосой...\""
    y_nvl "\"...количество жертв...{w}оценивается...{w}\nв 200 человек...\""
    y_nvl "{sc=0.5}\"...ведутся спасательные работы...{w}не все\nлюди найдены...\"{/sc}"
    y_nvl "{sc=1.0}......{/sc}"
    y_nvl "{sc=1.0}Мы до конца надеялись...{w}что папа был\nжив...{w}с тяжёлыми травмами...{w}но жив...{/sc}"
    y_nvl "{sc=1.0}............{/sc}"
    nvl hide Dissolve(1.0)
    nvl clear
    window auto
    mc "Всё-всё, Юри, тихо..."
    y "{sc=1.0}............{/sc}"
    "Теперь всё встало на свои места..."
    mc "Тс-с-с..."
    "Сейчас нужно дать ей восстановиться."
    "...подумал я после того, как расковырял её душевную травму."
    "Хоть бы моего объятия с поглаживаниями спины хватило..."
    "......"
    "..."
    "Кажется, она потихоньку успокаивается..."
    "..."
    y "{sc=1.0}Сегодня...{w}26 апреля...{/sc}"
    mc "..."
    "...совпадение, блин..."
    y "{sc=1.0}Надо будет...{w}навестить его...{/sc}"
    "..."
    "Не сегодня же?"
    "Уже вечер, так ещё и дождь этот дурацкий..."
    "..."
    "Так."
    "Вот что я ещё не выяснил, так это внезапную тягу к ножам."
    "Нет, я уже догадался, что Юри пыталась так перебить свои переживания, но почему...{w}как она до ножей дошла?"
    "Как бы тебя аккуратно спросить, пока есть шанс..."
    mc "Юри..."
    mc "Прости, но я задам ещё один вопрос...{w}последний, обещаю."
    mc "Можешь на него не отвечать, если тебе тяжело."
    mc "Так вот..."
    mc "Почему ты решила заглушить боль именно порезами?"
    "Лишь бы тебя сейчас не переклинило!"
    y "{sc=1.0}...{w}папа...{/sc}"
    y "{sc=1.2}...{/sc}"
    y "{sc=1.4}......{/sc}"
    mc "Тс-с-с..."
    "Ой, ну не-е-ет, нет-нет-нет, не надо!"
    y "{sc=1.4}...{/sc}"
    y "{sc=1.2}...{/sc}"
    "Фу-у-ух, подуспокоилась..."
    "Не получилось выяснить...{w}отвратительно, конечно, но ковыряться в душевной ране -- ещё более отвратительно."
    "Я не психолог, нормально ничего не могу тут сделать."
    "Это всё равно, что в хирургию поставить человека, который за всю жизнь резал только колбасу для бутерброда."
    y "{sc=1.0}...{/sc}"
    "Юри уже получше, отлично..."
    "У самого камень с души начинает спадать."
    "Хотя из-за нерешённости проблемы снова становится плохо..."
    "Чёртовы американские горки эмоций."
    "Мало мне приливов негативных мыслей, так тут ещё такие ситуации..."
    "Вообще надо бы сменить тему разговора, а то уже плохо со всего этого негатива."
    mc "Ха..."
    y "{sc=0.5}...{/sc}"
    mc "Я сейчас вспомнил ту книгу, которую мы пытались вместе читать."
    mc "Знатно я тебя тогда засмущал."
    y "{sc=0.25}...{/sc}"
    "...ну...{w}надеюсь, она чуть-чуть улыбнулась..."
    "Чёрт, да на что я рассчитываю?"
    "Пару минут назад ты рассказывал про гибель своего отца, а сейчас тебе говорят, как ты забавно книжку в паре читал."
    "Хи-хи, ха-ха, блин."
    "Идиот я."
    y "...{color=#407fff}Мар{/color}..."
    mc "{color=#407fff}Мар{/color}?..."
    y "...Портрет...{w}{color=#407fff}Маркова{/color}...{w}эта книжка..."
    mc "...а-а-а, точно."
    mc "Из головы вылетело."
    y "Ты её...{w}не читал...{w}хе..."
    mc "Ну...{w}извини, ха-ха-ха, я тогда не мог сосредоточиться и тебя боялся отвлечь."
    mc "Кстати, мне показалось, или она тоже была на английском языке, как и твои книги?"
    y "...нет...{w}японский..."
    mc "...но книга всё-таки иностранная?"
    y "...м-м..."
    y "...зацепила обложкой...{w}в книжном магазине...{w}и потом сюжетом..."
    mc "Наверное, он довольно необычный."
    y "...просто интересный..."
    mc "Ну, ты там говорила про...{w}э-э-э, вроде какую-то школьницу, которая переехала к своей сестре, а потом там что-то с тюрьмой было связано..."
    y "...я тогда скомканно и кратко рассказала сюжет..."
    mc "Да ладно уж, хах."
    mc "Главное, что тебя увлекает эта книга, верно?"
    y "...м-м."
    "Отлично, её состояние кое-как стабилизировалось."
    "..."
    "А сколько времени?"
    mc "Ладненько, давай я встану, разомнусь..."
    mc "Затёк слишком."
    y "...м-м..."
    "..."
    mc "Ой, у-у-ух-х-х..."

    scene bg bedroom with dissolve
    pause 0.25
    mc "Хм, а ноги уже получше чувствуются."
    mc "Так, что там по времени..."
    window hide

    $ phone.calendar.current_day = (26, _("ЧТ"))

    python in phone.system:
        battery_level = 58
        clock = (18, 22)

    show screen phone() with Dissolve(0.5)
    $ plot_pause()

    window auto
    mc "6 часов вечера..."
    window hide

    hide screen phone with Dissolve(0.5)

    window auto
    mc "Ладно, я думаю, нам пора закругляться."
    show yuri turned casual lsur cm oe lup rup at t11
    pause 0.2
    show yuri om
    y "...правда?"
    show yuri cm
    mc "Стих готов, да и так поговорили..."
    show yuri anno cm oe ldown rdown
    mc "Можно было бы ещё посидеть, но завтра пятница -- рабочий день, надо рано вставать."
    show yuri om
    y "Точно..."
    show yuri cm
    mc "Вот только дождь всё никак не кончится..."
    show yuri neut cm e1d b1c
    mc "Льёт, как из ведра."
    show yuri om
    y "У меня есть зонт...{w}всё в порядке."
    show yuri cm
    mc "Ты хочешь, чтобы я тебя одну отпустил в такую погоду?"
    show yuri e1b
    y "..."
    show yuri om
    y "У тебя ноги..."
    show yuri neut cm e1d
    mc "Ну уж нет, Юри."
    show yuri laug cm oe
    mc "Пойдём, провожу до дома."
    show yuri mb
    y "Ох..."
    show yuri lsur om oe
    y "Т-ты уверен?"
    show yuri neut cm e1d
    mc "Абсолютно."
    show yuri om
    y "Тогда..."
    show yuri happ om ce
    y "Спасибо..."
    show yuri cm

    scene black with wipeleft_scene
    "Давайте серьёзно: если бы я её кинул в такой ситуации, то это было бы полнейшим свинством."
    "А я не мудила, чтобы такое устраивать."
    "Надо составить ей компанию, чтобы ей стало ещё легче."
    stop noise_1 fadeout 2.0
    call window_close

    $ nightmare_active = False

    call plot_transition

    call window_open
    play noise_1 rainfall fadein 3.0
    play noise_2 rainfall_umbrella_mc fadein 3.0
    scene bg residential_day rain
    show rain zorder 3
    show umbrella_mc zorder 4
    show yuri turned casual neut cm e1d lup_item umbrella at t11
    with wipeleft_scene
    "..."
    "......"
    mc "...жесть."
    show yuri anno om oe
    y "Всё небо затянуло..."
    show yuri cm
    "Это уже какая-то аномалия."
    "Сезон дождей ещё не начался, а облака уже раскрутились на полную катушку."
    "..."
    mc "Хм, у тебя такой маленький зонт?"
    show yuri neut cm e1d
    y "М-м?"
    show yuri om
    y "А, он у меня давно..."
    show yuri cm
    mc "И тебе с ним удобно?"
    show yuri om
    y "Да."
    show yuri curi om oe
    y "А что?"
    show yuri md
    mc "Мне кажется, ты немного из него выросла..."
    show yuri happ om ce
    y "Есть такое..."
    show yuri oe
    y "Но менее удобным он от этого не стал."
    show yuri cm
    mc "Ладно..."
    "По-моему, она просто к нему привыкла."
    show yuri e1b
    "И это не значит, что ей с ним комфортно."
    "Почему бы просто не купить зонт побольше?"
    "..."
    show yuri neut cm e1b
    "...а с чего я решил, что у Юри всё прекрасно с финансами?"
    "Дом классический, бедноватый."
    "Отца нет."
    "Мать явно в командировках или в чём-то подобном, из-за чего её нет дома."
    show yuri e1c
    "Хотя я даже не знаю, как часто она отсутствует..."
    "Но, блин, зонтик-то не настолько дорогой."
    "..."
    show yuri e1b
    "Юри уже такая умиротворённая..."
    "Хотя, точно, она же ещё днём мне говорила, что дожди её успокаивают."
    "Хоть какой-то плюс от этого ливня."
    "..."
    mc "Что-то мы застряли на месте..."
    mc "Пойдём потихоньку в сторону твоего дома?"
    show yuri e1d
    y "М?"
    show yuri flus cm oe rup
    y "Ой, прости."
    show yuri laug mb oe
    y "Капли заворожили..."
    show yuri neut cm e1d
    s "{size=19}Хэ-э-э-э-эй!!!{/size}"
    show sayori turned windbreaker flus cm ce lup umbrella at l21
    show yuri rdown at t22
    pause 0.5
    show sayori nerv om oe
    s "Фу-у-ух, успела!"
    show sayori neut om oe b1d
    s "А то вы уже уходите!"
    show sayori cm
    mc "Сайори?"
    show sayori happ om oe -b1d
    show yuri happ cm oe
    s "Да я из окна увидела, как вы здесь стояли, захотела с вами прогуляться."
    show sayori neut cm oe
    mc "В такую погоду?"
    show sayori om b1d
    s "Ты что-то имеешь против тучек?"
    show sayori curi cm oe -b1d
    show yuri neut cm e1d
    mc "Да."
    show sayori om
    s "И что же?!"
    show sayori neut cm oe
    mc "Они иногда слишком затягиваются."
    show sayori b1e
    mc "И приходят не к месту."
    show sayori om
    show yuri happ cm e1b
    s "Даже в таких деталях надо находить крупицы счастья!"
    show sayori happ om ce -b1e rup at h21 zorder 2
    s "Посмотри, как капли падают!"
    show sayori rdown
    s "А ещё как пахнет освежающей сыростью!"
    show sayori cm
    show yuri om ce
    y "Сайори права..."
    show yuri cm
    mc "М-м-м..."
    "И этот человек мне ещё что-то рассказывал про свои «тучки»."
    show sayori e1b
    "..."
    show yuri e1c
    "Блин, меня всегда забавляла куртка Сайори с камуфляжем цвета хаки."
    "Не знаю почему..."
    show sayori oe
    show yuri oe
    mc "Ладно, пойдёмте уже, по пути поговорим."
    show sayori ce

    scene bg niigata street suburban 11 day rain
    show rain zorder 3
    show umbrella_mc zorder 4
    show sayori turned windbreaker happ cm oe lup umbrella at t21 zorder 2
    show yuri turned casual happ cm oe lup_item umbrella at t22
    with wipeleft_scene
    show sayori om
    s "Как стихотворные успехи?"
    show sayori cm
    mc "Вполне...{w}наверное..."
    show yuri om
    y "Лаконично..."
    show sayori om ce rup at h21
    show yuri cm
    s "Рада, что у вас всё получилось!"
    show sayori oe rdown
    s "А о чём стих?"
    show sayori neut cm oe
    mc "Вот завтра и узнаешь."
    show sayori anno om e1b
    s "Так неинтересно!"
    show sayori cm
    show yuri om
    y "Наоборот, интерес повышается..."
    show sayori dist om ce
    show yuri cm
    s "Э-эх, как хотите..."
    show sayori md
    show yuri oe
    mc "А у тебя-то с Нацуки что-нибудь получилось?"
    show sayori happ om oe
    s "Ты бы видел!"
    show sayori ce
    s "Нацуки хорошо постаралась!"
    show sayori cm
    mc "Ого, какое заявление..."
    show sayori om oe
    s "Честно-честно."
    s "И стих немаленький!"
    show sayori cm
    show yuri om e1b
    y "Надеюсь, она приняла свою ошибку...{w}и научилась слушать других людей..."
    show sayori om ce
    show yuri cm
    s "Так и есть!"
    show sayori oe
    show yuri oe
    s "Стихотворение тому подтверждение."
    show sayori cm
    "Сайори прямо сверкает радостью..."
    "Неужто стих настолько хорош?"
    show sayori neut cm oe
    show yuri neut cm e1d
    mc "Кстати, а Нацуки уже ушла?"
    show sayori om
    s "Убежала ещё как только небо стало затягиваться."
    s "У неё же зонта не было."
    show sayori cm
    mc "Ха, ясно."
    show sayori om e1b
    s "Это хорошо, что мы стих вовремя успели сделать."
    show sayori oe
    s "Иначе бы она промокла, даже если бы я её провела до дома."
    show sayori cm
    "Ну да, учитывая одежду и комплекцию Нацуки, могу сказать, что она не то, что бы промокла..."
    show yuri e1c
    "Её бы смыло."
    "А перед этим сдуло."
    "..."
    show sayori worr om oe
    show yuri e1d
    s "Эх, жалко, конечно, что завтра будет последнее собрание по парным стихам..."
    show sayori cm
    mc "Ну это как посмотреть."
    show sayori neut cm oe
    mc "Писать их в разы сложнее, потому что надо всё согласовывать с партнёром."
    mc "К тому же неизвестно, что выйдет в результате."
    show yuri worr cm oe
    mc "Так ещё и не можешь сделать упор на собственный стиль."
    show sayori b1e
    show yuri om
    y "Тяжело..."
    show sayori om
    show yuri neut cm e1d
    s "Но если получалось, то зато как получалось!"
    show sayori cm
    mc "Ну это \"если\"."
    show sayori om -b1e
    s "Ну..."
    show sayori anno cm e1b
    s "Мф..."

    scene bg yuri house outside day rain
    show rain zorder 3
    show umbrella_mc zorder 4
    show sayori turned windbreaker happ cm ce lup umbrella at t21 zorder 2
    show yuri turned casual happ cm oe lup_item umbrella at t22
    with wipeleft_scene
    "Мда, остаток пути мы провели в молчании."
    show sayori oe
    show yuri om e1b
    y "Что ж..."
    show yuri ce
    y "Большое спасибо...{w}за компанию..."
    show sayori om
    show yuri cm
    s "Не за что!"
    show sayori cm
    mc "Да, обычное дело."
    show yuri om oe
    y "Встретимся завтра..."
    y "Надеюсь, это будет самое интересное собрание из всех."
    show sayori ce
    show yuri cm
    s "Угусь!"
    show sayori oe
    show yuri om
    y "До завтра."
    show yuri cm
    mc "До завтра."
    show sayori om
    s "Пока-пока!"
    show sayori cm
    show yuri ce at thide
    hide yuri
    pause 0.5
    show sayori at t11
    "..."
    "...чёрт."
    show sayori e1b
    "Нужно ли потом рассказать Сайори о том, что я узнал о Юри?..."
    show sayori oe
    "..."
    show sayori om
    "Ладно, нет, подождите, не всё сразу!"
    show sayori neut cm oe
    "Мне надо переварить всё, что произошло, а уже потом думать."
    show sayori angr cm oe
    "Сейчас уже голова никакая."
    show sayori om
    s "Макс!" with vpunch
    show sayori cm
    mc "А?!"
    show sayori happ om ce
    s "Ура!"
    show sayori cm
    mc "Ты что-то говорила, да?"
    show sayori om oe b1e
    s "Ага!"
    show sayori -b1e
    s "Я спросила, не хочешь прогуляться?"
    show sayori neut cm oe
    mc "В такой дождь..."
    show sayori om b1c
    s "Он же несильный!"
    show sayori cm
    mc "Ну хорошо, пошли."
    show sayori happ cm oe -b1c
    mc "Только недолго."
    show sayori om ce rup at h11
    s "Ок-ке!"
    show sayori cm rdown

    scene bg niigata street suburban 11 day rain
    show rain zorder 3
    show umbrella_mc zorder 4
    show sayori turned windbreaker neut cm e1b lup umbrella at t11
    with wipeleft_scene
    "Ни конца, ни края у этих туч..."
    play music sayori_my_confession_rain
    show sayori om
    s "Знаешь, я тут после своего стиха с Нацуки подумала..."
    show sayori worr om oe
    s "Неужели людям так тяжело меняться в лучшую сторону?"
    show sayori cm
    mc "Пф-ф-ф, вот это тебя занесло..."
    show sayori neut om oe b1e
    s "Нет, я серьёзно!"
    show sayori cm
    mc "Понял-понял."
    show sayori -b1e
    mc "Просто так внезапно подняла такую тему..."
    show sayori happ om oe
    s "Такой стих получился."
    show sayori cm
    mc "Блин, что же вы там такое написали?"
    show sayori laug cm oe
    mc "Интрига растёт как на дрожжах."
    show sayori om ce
    s "Ха-ха-ха!"
    show sayori happ om ce
    s "Так вот, возвращаясь к вопросу..."
    show sayori neut om oe
    s "Нет, я понимаю, что люди много чего творят плохого и нехорошего, но..."
    show sayori b1c
    s "...просто взять и поменять свою жизнь к лучшему, хотя бы на чуть-чуть...{w}разве это так трудно?"
    show sayori cm
    mc "Будто я знаю, почему они это не делают..."
    show sayori -b1c
    mc "Хотя у меня есть одно предположение."
    show sayori om
    s "И какое?"
    show sayori cm
    mc "Ну..."
    show sayori curi cm oe
    mc "Их это банально устраивает."
    show sayori om
    s "Как кому-то может нравится быть плохим?"
    show sayori cm
    mc "Сайори, это очень сложный вопрос, в котором играет большое количество причин и факторов."
    show sayori neut cm oe
    mc "Но для некоторых такое состояние реально как образ жизни."
    mc "Возможно, из-за психической травмы или совершенно неправильного мировоззрения."
    mc "Или желания выделиться на фоне, потешить своё эго."
    mc "Или ненависть к тем, у кого жизнь более «успешная»."
    mc "Короче, как я сказал, тут куча причин."
    mc "Но вместо того, чтобы бороться с этим и становиться лучше, они просто опустили руки и приняли это как должное."
    mc "А если будешь указывать им на этот изъян, то они найдут 3000 отговорок и оправданий, почему так якобы должно быть."
    show sayori om b1f
    s "Ты хочешь сказать, что такие люди пришли к этому из-за слабости?"
    show sayori cm
    mc "Да."
    show sayori -b1f
    mc "Прости за грубость, но ведь мудаком быть проще, чем человеком, который может выслушать, поддержать и бескорыстно помочь, не правда ли?"
    show sayori worr cm oe
    s "..."
    mc "Поэтому если встретишь такого «нелюдя», то помни, что ты сильнее его, потому что ты умеешь бороться с изъянами."
    show sayori neut cm oe
    mc "Нужно всего лишь научиться игнорировать таких индивидов или давать им грамотный и быстрый отпор, если столкновение неизбежно."
    mc "Потому что без внимания их потуги быстро гаснут вне зависимости от целей."
    show sayori worr cm oe
    mc "А если «сковырнуть» оболочку и посмотреть во внутрь этих «нелюдей», то можно увидеть, как там всё сгнило."
    show sayori om
    s "Сложно всё это..."
    show sayori cm
    mc "Вот, видишь?"
    show sayori neut cm oe
    mc "Значит, ты начинаешь это всё понимать и анализировать со своей точки зрения."
    mc "А зная, какая ты у нас добрая в хорошем смысле, я могу сказать, что ты на правильном пути."
    mc "Да, он трудный."
    show sayori laug ma oe
    mc "Но поверь, ты получишь в разы больше от жизни, чем все эти уроды вместе взятые, не говоря уже о том, что ты сможешь преумножить свои блага."
    show sayori om ce
    s "Это очень громкие слова, Макс, ха-ха-ха..."
    show sayori ma
    mc "Зато верные."
    show sayori happ cm oe
    mc "А пафос здесь ничего не значит."
    show sayori om
    s "Ладненько, теперь стало понятнее."
    show sayori ce
    stop music fadeout 6.0
    s "Спасибо за ответ!"
    show sayori cm
    mc "...пожалуйста."
    "Отлично, один кирпичик вложен в Сайори."
    show sayori e1b
    "Честно, я как-то сам от себя такого ответа не ожидал..."
    "Погрузился в мысль с головой."

    scene bg residential_day rain
    show rain zorder 3
    show umbrella_mc zorder 4
    show sayori turned windbreaker happ cm e1c lup umbrella at t11
    with wipeleft_scene
    "В итоге наша прогулка ограничилась походом обратно..."
    "Ну и правильно, время жмёт."
    show sayori e1b
    "Надо поесть и разобраться с мелкими бытовыми делами..."
    show sayori neut cm oe
    mc "Ну что, по домам?"
    show sayori flus om oe
    s "Мы уже вернулись?"
    show sayori cm
    mc "Ну да."
    show sayori worr om oe
    s "А так хотелось ещё походить..."
    show sayori happ om oe
    s "Но кушать хочется больше."
    show sayori cm
    mc "Пха, тогда беги ужинать."
    show sayori ce
    s "Угусь!"
    show sayori om oe
    s "Завтра утром встретимся!"
    show sayori cm
    mc "Обязательно."
    show sayori e1b
    call window_close

    hide sayori with easeoutleft
    pause 1.0
    stop noise_1 fadeout 2.0
    stop noise_2 fadeout 2.0

    call plot_transition

    $ nightmare_active = True

    call window_open
    scene bg bedroom with wipeleft_scene
    "Мда, стоило только вернуться и покончить со всеми делами, как дождь закончился."
    "..."
    "......"
    mc "Значит, разбился..."
    "Поиск в Интернете ничего нового не дал -- Юри и так всё рассказала."
    "Ну разве что более точные цифры, а также фотографии..."
    mc "И ведь я, по-моему, тоже видел эту новость..."
    "Но, ясно дело, не придал этому значение в силу своего возраста."
    mc "И вот летай потом на этих самолётах..."
    "Хотя эта авиакомпания ужесточила качества авиаперевозок пассажиров, судя по статьям."
    "А хотя..."
    mc "Ой, да ну вас нахрен!"
    "Постоянно все на чём-то экономят, пытаясь поиметь систему, а потом эта система с такой силой бьёт в морду, что потом в себя не приходишь."
    "И каждый раз, как в первый раз."
    "Сколько ни читал чисто из любопытства статьи про различные катастрофы и инциденты, в большинстве случаев видел, как они происходили из-за ошибок в элементарных мелочах."
    "И, как правило, из-за человеческого фактора."
    "А потом эти ошибки стоят большого количества жизней..."
    mc "Около 250 человек...{w}одна четвёртая от тысячи..."
    mc "...за пару мгновений превратилась в лепёшку из кровавого месива, смятого металла и горящего топлива."
    mc "Мать твою..."
    "И это только одна катастрофа."
    "А я мельком увидел большой список других катастроф с различными цифрами пострадавших и погибших."
    "И они охренеть какие немаленькие."
    mc "Фу..."
    "Мне аж плохо стало."
    "Даже не знаю, как это описать."
    "Смесь «подсознательного» адреналина и напряжения с более отчётливыми ударами сердца."
    mc "Так, ладно, хватит."
    mc "Состояние мерзкое, теперь до конца этого дня точно."
    mc "Но не надо тратить время на всю эту эмоциональную дрянь, она всё равно ничего мне не даст."
    mc "Однако она очень выбивает из колеи и избавиться от неё тяжело..."
    mc "Хоть слова в слух помогают кое-как акцентировать внимание на голосе, а не на чернушных мыслях."
    mc "Так, что теперь..."
    mc "В будущем мне надо будет рассказать эту ценную по Юри информацию психологу."
    mc "Опять его, блин, искать..."
    mc "А-а, ещё Монике надо отписаться."
    mc "Вот ей об этом точно нужно сообщить."
    mc "А Сайори?"
    "..."
    mc "Но это ТАКАЯ для Юри личная информация, что её утечка приведёт к крайне негативным последствиям."
    mc "Может быть, позже Сайори просвещу, но точно не сейчас."
    mc "Всё, сейчас напишем Монике..."
    call skip_block_on

    python in phone.system:
        cellular_data = False
        wifi = True
        battery_level = 57
        clock = (19, 7)

    phone discussion "mc_m_chat"
    $ plot_pause()
    phone discussion "mc_m_chat":
        time year 2018 day 26 month 4 hour 19 minute 7
        "mc" "Мони, очень важная новость"
        "mc" "Я наконец-то узнал причину, точнее, событие, после которого Юри сломалась"
    mc "Надеюсь, она не сильно потревожится..."
    mc "...пф, сказал человек, который написал \"Очень важная новость\"."
    phone discussion "mc_m_chat":
        "m" "УХ ТЫ!!!"
    $ phone.system.clock = (19, 8)
    phone discussion "mc_m_chat":
        "m" "Не томи, рассказывай!"
        "mc" "Только там всё очень серьёзно"
        "mc" "Ты уверена, что хочешь это знать?"
        "m" "И ты ещё спрашиваешь?"
        "m" "Юри же моя подруга и часть клуба"
        "m" "Я же ведь не успокоюсь, пока не узнаю причину её проблемы"
        "mc" "Хорошо, твой выбор"
        "mc" "Событие связано с её отцом"
        "mc" "Кстати, ты про него что-нибудь знаешь?"
    $ phone.system.clock = (19, 9)
    phone discussion "mc_m_chat":
        "m" "Хммм"
        "m" "Нет, мне Юри ничего про него не говорила"
        "mc" "Значит, я напишу"
        "mc" "Её отец был хорошим фотожурналистом, часто получал контракты, по которым делал фотографии за рубежом"
        "mc" "Попутно привозил с собой сувениры"
        "mc" "И в один прекрасный момент ему дали контракт на фотографии выступлений каких-то политиков в Филиппинах"
        "mc" "Съездил, выполнил задание, полетел обратно"
    $ phone.system.clock = (19, 10)
    phone discussion "mc_m_chat":
        "mc" "И вот этот рейс обратно завершился плачевно"
        "mc" "При подлёте к Нагое то ли из-за неисправности, то ли из-за ошибки пилотов (забыл уже, неважно) управление самолётом было потеряно"
        "mc" "Скорость резко снизилась, и он вошёл в штопор"
        "mc" "В результате он вертикально влетел во взлётно-посадочную полосу"
        "mc" "Результат, думаю, ты и сама знаешь какой..."
        "mc" "Причём произошло это всё 5 лет назад в этот же день"
        "mc" "Возможно, ты могла видеть где-то эту новость"
    $ phone.system.clock = (19, 11)
    phone discussion "mc_m_chat":
        "mc" "В общем, на этом всё"
        "mc" "А порезы..."
        "mc" "Юри, вероятно, не придумала лучше способа заглушить свои переживания по этому поводу"
        "mc" "Короче, полный аут"
    mc "Фу-у-ух, написал..."
    mc "Вроде бы вся информация."
    phone discussion "mc_m_chat":
        "mc" "Мони?"
    $ phone.system.clock = (19, 12)
    phone discussion "mc_m_chat":
        "mc" "Ты прости, если шокировал"
        "mc" "Если тебе плохо, то напиши"
        "m" "Нетнетнет всё в порядке Макс"
        "m" "Мне просто надо... Подумать"
        "mc" "Хорошо"
    mc "...ну мягче подать эту информацию я не мог."
    mc "Сама по себе ситуация ужасная..."
    "..."
    mc "Я, кстати, что-то на заметки в календаре забил."
    mc "А есть ли смысл туда писать негатив?"
    $ phone.system.clock = (19, 13)
    mc "Но прошедший конфликт в клубе я-то вписал."
    mc "Однако это было неделю назад..."
    phone discussion "mc_m_chat":
        "m" "Я всё быстро обдумала и..."
        "m" "Ничего не придумала"
        "mc" "Ну это понятно, устала за день"
        "mc" "Всё равно дело остаётся за мной, буду продолжать искать психолога"
        "m" "Да, безусловно"
        "m" "Мы же не будем никому про это рассказывать, верно?"
        "mc" "Верно"
        "m" "Тогда по этой ситуации всё?"
        "mc" "Ну а что тут ещё?"
    $ phone.system.clock = (19, 13)
    phone discussion "mc_m_chat":
        "mc" "Пока я свою задачу не выполню, ничто не сдвинется"
        "mc" "А вам пока надо присматривать за Юри"
        "mc" "Блин, пока-пока, пока-пока..."
        "mc" "Некоторые слова иногда приедаются"
        "m" "Ты большой молодец, Макс"
        "mc" "Спасибо, но пока рано об этом говорить"
        "mc" "НУ ВОТ ОПЯТЬ"
        "m" "Хахаха)"
        "m" "Давай немного разбавим тему"
        "mc" "?"
        "m" "Как у вас там со стихом дела?"
        "m" "Надеюсь, он лучше, чем то, что я сегодня видела?"
    python in phone.system:
        battery_level = 56
        clock = (19, 14)
    phone discussion "mc_m_chat":
        "mc" "Не сомневайся"
        "mc" "Но не настолько лучше, чем хотелось бы..."
        "m" "Но это уже хорошо"
        "mc" "Вот у Сайори с Нацуки там что-то реально интересное"
        "mc" "Встретился с ней, когда Юри до дома провожал"
        "m" "Прямо до дома?"
        "mc" "Ой, Моника, не надо тут псевдоревности"
        "mc" "Ты же видела, какой ливень был"
        "mc" "А Юри умудрился прийти в одном свитере с небольшим зонтиком, из которого она точно выросла"
        "m" "Ладно-ладно)"
    $ phone.system.clock = (19, 15)
    phone discussion "mc_m_chat":
        "mc" "Ну а у тебя как там дела?"
        "m" "Мы с Котонохой очень увлеклись и исписали целых два листа"
        "m" "Это будет самый большой стих за всю историю Литературного клуба!"
        "mc" "Ничего себе..."
        "m" "Мы сами не ожидали, что так всё выйдет"
        "m" "Могу с уверенностью сказать, что завтра нас ждёт интересный обмен и хороший финал для парных стихов"
        "mc" "Да уж"
    mc "Сплошные громкие заявления..."
    mc "Как бы ни хотелось на них купиться, но лучше не делать ставку на что-то грандиозное."
    mc "Так и разочарования не будет, и ожидания приятно удивят, если эти слова окажутся правдой."
    $ phone.system.clock = (19, 16)
    phone discussion "mc_m_chat":
        "m" "Хорошо, я тогда ещё раз всё обдумаю и пойду спать"
        "mc" "Угу"
        "mc" "До встречи в клубе"
        "m" "Бай~"

    phone end discussion transition

    call skip_block_off
    mc "О-о-ох..."
    mc "Теперь я могу точно откиснуть."
    mc "Уже начинает проступать пульсирующее ощущение в висках."
    mc "Возможно, из-за непогоды."
    mc "Но в любом случае пофиг: я свободен."
    mc "На сегодня."
    mc "До сна..."
    mc "И только после поиска..."
    call window_close

    call nightmare_act_1_day_11
    $ _history_list.clear()

    return
