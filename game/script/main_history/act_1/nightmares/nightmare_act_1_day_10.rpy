
screen punch_natsuki_ghost_a1_nd10_1:
    button:
        area(606, 134, 445, 400)
        mouse "punch"
        action [Play("sound", "mod_assets/sound/body/hit.mp3"), Return()]




label nightmare_act_1_day_10_1:

    scene black with dissolve_scene_full

    pause 1.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 3.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    call autosave
    "..."
    "Кто...{w}кто в меня тыкает?..."
    mc "Х-хватит..."
    n "О, так ты не спишь."

    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp5 at cgfade
    with dissolve_scene_full
    n "С добрым утром, соня."
    mc "Сколько...{w}я так просидел?"
    hide n_cg1_exp5
    show n_cg1_exp2 at cgfade
    n "Думаю, столько же, сколько и я проспала с тобой тогда в кладовке."
    mc "Недолго?"
    hide n_cg1_exp2
    n "Ага."
    show n_cg1_exp5 at cgfade
    n "Всё равно пока ещё никого нет."
    n "Прихожу, дверь открыта."
    n "Сначала удивилась, потому что никого не увидела в классе, а потом тебя заметила."
    n "От скуки сюда и села."
    mc "Понятно."
    "Хм, мне уже стало намного лучше."
    hide n_cg1_exp5
    show n_cg1_exp4 at cgfade
    "Ничего не кружится..."
    "Нормальное ощущение пространства..."
    "Ну хоть что-то хорошее за сегодня."
    hide n_cg1_exp4
    show n_cg1_exp2 at cgfade
    n "Слушай, нет, мы так целую вечность в тишине просидим, пока остальных ждать будем..."
    mc "М-м..."
    hide n_cg1_exp2
    show n_cg1_exp1 at cgfade
    n "Предлагаю нам что-нибудь почитать из моей коллекции!"
    "Какая-то Нацуки слишком...{w}весёлая?"
    mc "И что же?"
    hide n_cg1_exp1
    n "Что угодно, кроме «Ванильной симфонии»."
    show n_cg1_exp2 at cgfade
    n "Потому что вряд ли тебя такое заинтересует..."
    mc "Как знать, может, зацепит."
    hide n_cg1_exp2
    n "Ладно, пошли, выберем по ходу дела."
    mc "Ох..."
    show n_cg1_exp3 at cgfade
    n "Не раскисай."
    mc "С вами и не выйдет..."

    scene bg closet
    show natsuki turned neut cm oe at i11
    with dissolve_cg
    mc "Ух-х-х..."
    "Прям как новенький."
    "Я уж боялся, что развалюсь ещё сильнее."
    call window_close

    scene black with dissolve_cg
    pause 3.0

    call window_open
    play music t6
    mc "Да ну нафиг, Нацуки!"

    scene n_cg2_bg
    show n_cg2_base
    show n_cg2_exp1 at cgfade
    with dissolve_cg
    mc "Опять ты с этой коробкой?!"
    mc "Ещё и на том же крутящемся стуле..."
    mc "Прошлый опыт ничему не научил?"
    n "Помолчи!"
    hide n_cg2_exp1
    n "Именно в этой лимитированной коробке есть интересная манга!"
    mc "Я б сам всё спокойно достал..."
    show n_cg2_exp1 with Dissolve(0.5)
    n "Ты что, меня недооцениваешь?"
    mc "...что?"

    $ currentpos = get_pos(channel="music")
    $ audio.t6g_1 = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    stop music
    play music audio.t6g_1

    hide n_cg2_base
    hide n_cg2_exp1
    show n_cg2_base_horror

    pause 0.1

    $ currentpos = get_pos(channel="music")
    $ audio.t6_1 = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    stop music
    play music audio.t6_1

    show n_cg2_base
    show n_cg2_exp1
    hide n_cg2_base_horror
    n "..."
    mc "Нет-нет-нет, я не это имел в виду!"
    mc "Просто я не хочу снова ловить тебя всем телом под угрозой, что ты треснешься обо что-нибудь головой."
    show n_cg2_exp3 at cgfade
    hide n_cg2_exp1 with Dissolve(0.5)
    n "А-а-а..."
    n "Ладно, извини, на меня какая-то грусть накатила..."
    mc "Бывает."

    scene black with dissolve
    pause 0.25
    "Что-то здесь не так..."

    scene bg closet
    show natsuki turned happ cm oe at t11
    with dissolve_cg
    pause 0.5
    stop music fadeout 3.0
    show natsuki pout om oe lhip rhip
    n "Так, подожди..."
    show natsuki curi om oe
    n "Это хоть то, что я хотела показать?..."
    show natsuki cm
    mc "А?"
    show natsuki b1a
    mc "Манга как манга..."
    show natsuki e1f -b1a
    "Полностью чёрная-белая манга..."
    n "..."
    show natsuki neut om oe
    n "А, да, оно, отлично."
    show natsuki happ om oe ldown rdown
    n "Садись!"
    show natsuki cm

    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    "Какой странный и «жирный» томик..."
    "Обложка уже отторгает."
    "Но ведь книгу по обложке не судят?"
    "Точнее мангу..."
    "Похоже, это сборник различных сюжетов, судя по содержанию."
    "Посмотрим..."
    "..."
    "Вытянутая биомасса с окном?"
    "Что за хренотень?"
    "Человек с гвоздями вместо зубов?"
    "Чё?..."
    "Летающие человеческие головы-виселицы?"
    "Блин, Нацуки, что это за..."
    "Куча сшитых между собой людей...."
    "Ты надо мной смеёшься?"
    "Какие, нахрен, мутировавшие куклы?"
    "А это что за сборище людей-паразитов из туши какого-то морского гиганта?!"
    "Твою мать..."
    "Меня сейчас стошнит, если я не остановлюсь..."
    "Как ВОТ ЭТО ты вообще хранишь в своей коллекции?!"
    n "Как тебе?"
    mc "Отвал башки..."
    show n_cg1_exp1 at cgfade
    n "Ха-ха-ха, понравилось, да?"
    mc "Не то слово!"
    mc "Ты мне одно скажи: ты серьёзно ТАКОЕ читаешь?!"
    n "Да, а что?"
    mc "Это..."
    "...вот чёрт, снова раздражение в желудке..."
    "А ведь мне только-только полегчало..."
    hide n_cg1_exp1
    mc "...это очень тошнотворно выглядит..."
    mc "Нет, я не говорю, что всё сделано плохо."
    mc "Сюжет, может, хороший, качественный..."
    mc "Но...{w}мне кажется, что здесь СЛИШКОМ переборщили с рисовкой."
    mc "Тут что ни страница, то либо страхоёбина, либо насилие, либо ещё что-то мерзкое."
    mc "Я такое даже в Интернете не видел."
    "Или всё-таки что-то такое было?"
    n "Мерзко?..."
    "Да, чёрт возьми, мерзко!"
    show n_cg1_exp2 at cgfade
    n "М-м..."
    "...что с её реакцией?"
    mc "Эй, что с тобой?"
    show n_cg1_exp3 at cgfade
    hide n_cg1_exp2
    n "Подожди, дай мне подумать."
    "..."
    "Она что, теперь взглядом меня сверлить будет?"
    "Хорошо, в эту игру могут играть только двое."
    "Разрядим немного обстановку и отвлечёмся, пока мне снова не поплохело."
    "Смотри в глаза, смотри в глаза, не думай о манге, не думай о манге..."
    call window_close

    pause 6.0

    call window_open
    mc "И долго мы так сидеть будем?"
    n "Заткнись."
    n "Я ещё не закончила."
    mc "Как грубо..."
    n "Ну извини, ты меня сбил."
    mc "Хорошо, блин, молчу."
    n "..."
    hide n_cg1_exp3
    n "А..."
    n "Кажется..."
    n "Я начинаю понимать..."
    mc "Что именно?"
    n "То, что я..."
    call window_close

    play music t6
    pause 4.7

    call window_open
    show n_cg1_exp1 at cgfade
    n "...испугала тебя до чёртиков!"
    n "Ха-ха-ха!"
    stop music fadeout 3.0
    mc "...чего?"
    n "Ты реально думал, что я буду читать подобную крипотень?"
    mc "Ни разу."
    hide n_cg1_exp1
    n "Я просто на днях нашла это и купила по скидке, чтобы прикольнуться над тобой."
    show n_cg1_exp2 at cgfade
    n "Правда потом придётся кому-нибудь втюхать этот сборник за деньги..."
    hide n_cg1_exp2
    n "...но это мелочи."
    show n_cg1_exp1 at cgfade
    n "А ведь ты чуть не поверил!"
    n "Ха-ха-ха!"
    n "Видел бы ты свою скорчившуюся гримасу!"
    mc "Тьфу на тебя!"
    "Я реально параноик."
    "Думал, что опять во сне..."
    "У меня уже активно едет крыша..."
    n "Нет, ну классно вышло, а?!"
    mc "Пф..."
    "По крайней мере она искренне счастлива."
    "...хоть и ценой моего спокойствия и настроения."
    "Надо насладиться этим моментом, пока не поздно."
    "Всё равно он продлится буквально пару секунд."
    call window_close

    call skip_block_on
    $ blocker = True
    $ blocker_key = "natsuki_ghost"
    $ n_name = _("{glitch=15}{color=#000}Нацуки{/color}{/glitch}")

    $ nightmare_active = True

    play music t6g
    pause 4.7
    show n_cg1b
    hide n_cg1_base
    hide n_cg1_exp1
    pause 1.0

    if cg_a1_d10_night_n_1.unlocked == False:
        $ cg_a1_d10_night_n_1.unlock()

    if cg_a1_d10_night_n_2.unlocked == False:
        $ cg_a1_d10_night_n_2.unlock()

    call window_open
    mc "{sc=3}ЁПТ!!!--{/sc}{nw}" with vpunch
    $ style.say_dialogue = style.edited
    n "Я соврала."
    n "Я хотела разрядить обстановку."
    n "Но поняла, что уже не могу сдерживать свои эмоции."
    n "Значит, это манга мерзкая, да?"
    n "На самом деле я специально искала именно её."
    n "Я думала, что она тебе понравится."
    n "Потому что я старалась впечатлить тебя."
    n "А ты даже этого не ценишь."
    $ style.say_dialogue = style.normal
    "Какого хрена?!"
    mc "Значит, это сон!"
    $ style.say_dialogue = style.edited
    n "Нет, это твоя реальность."
    $ style.say_dialogue = style.normal
    mc "Даже думать не хочу!"
    mc "{sc=3}Пошла ты нахрен, фальшивка!!!{/sc}"
    call window_close
    call skip_block_on

    call screen punch_natsuki_ghost_a1_nd10_1

    call skip_block_off
    scene white
    stop music

    pause 0.3

    call skip_block_off
    $ blocker = False
    $ n_name = _("Нацуки")

    $ nightmare_active = False

    return




label nightmare_act_1_day_10_2:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    pause 1.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 3.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call skip_block_on
    $ blocker = True
    $ blocker_key = "natsuki_ghost"
    $ n_name = _("{glitch=15}{color=#000}Нацуки{/color}{/glitch}")

    call window_open
    scene bg club_day
    show monikamm_watch_a1_d10
    show darkred zorder 4:
        alpha 0.5
    with dissolve_scene_full
    call autosave
    "..."
    "......"
    mc "...что?"
    mc "Почему я..."
    mc "..."
    if persistent.censorship:
        mc "...зараза, снова."
    else:
        mc "...блять, снова."
    "Я отказываюсь это понимать."
    "Да даже если бы хотел!"
    mc "Что со мной происходит, а?!"
    mc "Кто-нибудь мне может объяснить?!"
    play music t6g
    $ style.say_dialogue = style.edited
    n "Зачем, если ты всё знаешь?"
    $ style.say_dialogue = style.normal
    "Знакомый голос..."
    show natsuki mouth zorder 2 at t11
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Ты абсолютно всё знаешь."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Опять ты?!"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Это моя фраза."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Нет, не твоя, а Нацуки."
    mc "А ты лишь фальшивый образ в моём мозге, вот и всё!"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Как удобно ты мыслишь."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "А что, неправда?"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Да."
    n "Я не фальшивый образ."
    n "У меня есть ЧУВСТВА."
    n "В отличие от тебя..."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Какие, нахрен, чувства?!"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Натуральные."
    n "Как и у тех, кто умеет ощущать."
    n "А ты этого не хочешь понять."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Окей, хорошо, давай попытаемся разобраться во всей этой абсурдной ситуации."
    "Не верю, что говорю это «кошмару» в кошмаре."
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "О, давай."
    n "А то здесь ОЧЕНЬ скучно."
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "..."
    mc "Пф-ф-ф..."
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Что, волнуешься?"
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Твою мать, да!"
    mc "Ты можешь скрыть своё ненормальное лицо?"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "НЕНОРМАЛЬНОЕ?!"
    n "ТЫ НЕ ПРИНИМАЕШЬ МЕНЯ?!"
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Да, пока ты действуешь мне на нервы!"
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "Я ПРОСТО ХОЧУ ПОИГРАТЬ!"
    n "ПОИГРАТЬ, МАКС!"
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Какие, нафиг, игры..."
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "МНЕ ОДИНОКО!"
    n "И ты этого совсем не понимаешь!"
    hide n_moving_mouth
    show n_rects_mouth zorder 3
    $ style.say_dialogue = style.normal
    mc "Так ты лицо своё скроешь?"
    $ style.say_dialogue = style.edited
    n "......"
    $ style.say_dialogue = style.normal
    mc "Если нет, то я не буду с тобой разговаривать."
    mc "И \"играть\"."
    hide n_rects_mouth
    show n_moving_mouth zorder 3
    $ style.say_dialogue = style.edited
    n "АРГХ, хорошо."
    n "Будь по-твоему."
    hide n_moving_mouth
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    show screen tear_screen(8, offtimeMult=1, ontimeMult=10)
    stop music
    play noise_1 g1

    pause 2.0
    hide darkred
    hide natsuki mouth
    show natsuki ghost_base at i11
    pause 1.0

    stop noise_1
    hide screen tear_screen
    play music contact fadein 1.0
    $ quick_menu = True
    mc "А-А-А, вот это меня сейчас пробило!" with vpunch
    mc "Фу-у-у..."
    mc "Что ты сделала?!"
    $ style.say_dialogue = style.edited
    n "Убрала лицо, как ты просил."
    $ style.say_dialogue = style.normal
    mc "Нет, не это!"
    mc "У меня картинка перед глазами «заглючила»!"
    $ style.say_dialogue = style.edited
    n "Я убрала лицо."
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    n "..."
    $ style.say_dialogue = style.normal
    mc "Ладно, начнём с самого-самого начала."
    mc "Кто ты такая?"
    $ style.say_dialogue = style.edited
    n "Догадайся с трёх раз."
    $ style.say_dialogue = style.normal
    mc "Издеваешься?"
    $ style.say_dialogue = style.edited
    n "Издеваешься здесь только ты."
    $ style.say_dialogue = style.normal
    mc "Нет уж, отвечай!"
    show natsuki ghost_base at h11
    $ style.say_dialogue = style.edited
    n "Это игра, Макс!"
    n "Угадай!"
    $ style.say_dialogue = style.normal
    mc "Да какая ж ты засранка..."
    mc "Больной образ моего воображения?"
    $ style.say_dialogue = style.edited
    n "Две попытки."
    $ style.say_dialogue = style.normal
    mc "..."
    mc "Да я чё, знаю, что ли?"
    $ style.say_dialogue = style.edited
    n "Знаешь."
    n "Серьёзно знаешь."
    $ style.say_dialogue = style.normal
    mc "Да нихрена я не знаю!"
    $ style.say_dialogue = style.edited
    n "Знаешь, Макс."
    n "Думай."
    $ style.say_dialogue = style.normal
    mc "Грх..."
    mc "Это связано с чувством?"
    $ style.say_dialogue = style.edited
    n "Верно."
    n ghost2 "Но за это я заберу одну попытку."
    $ style.say_dialogue = style.normal
    mc "ЧТО?!"
    mc "Мы так не договаривались!"
    $ style.say_dialogue = style.edited
    n "Но ведь так больше азарта!"
    n "Одна попытка, Макс."
    $ style.say_dialogue = style.normal
    "Она меня начинает бесить."
    "Но надо контролировать своё состояние..."
    "Когда мне ещё предоставится такая возможность разобраться в себе?"
    $ style.say_dialogue = style.edited
    n "Ну что, сдаёшься?"
    $ style.say_dialogue = style.normal
    mc "Нет, я думаю, что ты..."
    mc "...ну ты общения и ласки жаждешь, что я ещё могу сказать?"
    $ style.say_dialogue = style.edited
    n "Верно, но ты не назвал меня."
    $ style.say_dialogue = style.normal
    mc "Ты кривой образ Нацуки моего мозга."
    n ghost_base "..."
    mc "Всё!"
    mc "Как раз всё прекрасно сходится: она хотела поиграть, я с ней провёл много времени за...{w}уже вчера."
    mc "В итоге, у меня в голове отпечатался её образ, а в совокупности с произвольными кошмарами появилась ты."
    $ style.say_dialogue = style.edited
    n "Я была и раньше."
    $ style.say_dialogue = style.normal
    mc "...это {b}ты{/b} так считаешь."
    mc "Раньше тебя не было."
    $ style.say_dialogue = style.edited
    n "Была."
    $ style.say_dialogue = style.normal
    mc "Откуда такая уверенность?"
    $ style.say_dialogue = style.edited
    n "Я реально была."
    $ style.say_dialogue = style.normal
    mc "Не было тебя, блин, ты просто кусок воображения!"
    show natsuki ghost_base at h11
    $ style.say_dialogue = style.edited
    n "Была, я была!"
    $ style.say_dialogue = style.normal
    mc "Чёрт тебя побери..."
    "Это может продолжаться бесконечно..."
    mc "Ладно, другой вопрос."
    mc "Что ты хочешь?"
    mc "Ты же тут не просто так, да?"
    $ style.say_dialogue = style.edited
    n "Я хочу быть с тобой, Макс."
    $ style.say_dialogue = style.normal
    mc "В каком плане?"
    $ style.say_dialogue = style.edited
    n "Мне одиноко."
    n "Мне всё время было одиноко."
    n "Я устала это терпеть."
    n "Я хочу, чтобы ты поиграл."
    n "Поиграл со мной."
    $ style.say_dialogue = style.normal
    mc "Ты можешь говорить менее расплывчато?"
    mc "Или ты специально так делаешь?"
    $ style.say_dialogue = style.edited
    n "Поиграй...{w}со мной..."
    $ style.say_dialogue = style.normal
    mc "Скажи конкретно, что здесь происходит!"
    mc "Хватит меня держать за идиота!"
    mc "Так тяжело, что ли?!"
    $ style.say_dialogue = style.edited
    n "Ты...{w}меня ненавидишь?"
    $ style.say_dialogue = style.normal
    mc "Нет, но такими темпами да!"
    "Абсолютно ноль информации!"
    "Может, я что-то и мог бы у неё выклянчить, но мне уже плохо."
    $ style.say_dialogue = style.edited
    n "Значит, ты меня ненавидишь."
    $ style.say_dialogue = style.normal
    mc "Тьфу на тебя, пусть будет так, как ты считаешь."
    mc "У меня нет сил с тобой бодаться."
    mc "Вы все меня достали своими тупыми фразами и страхами."
    if persistent.censorship:
        mc "Каждый раз снится какая-то хрень вместо чего-то нормального и приятного."
    else:
        mc "Каждый раз снится какая-то херня вместо чего-то нормального и приятного."
    mc "И каждый раз во всём этом нет НИКАКОГО смысла, начиная от причин появления сна и заканчивая его подтекстом (которого нет)!"
    stop music fadeout 2.0
    $ style.say_dialogue = style.edited
    n "Ты меня ненавидишь..."
    $ style.say_dialogue = style.normal
    mc "О-о-о, за что мне это всё..."
    play music natsuki_hard_glitch fadein 6.0
    show darkred zorder 5:
        alpha 0.0
        easein 20.0 alpha 1.0
    show n_rects_left zorder 4:
        yoffset -20 alpha 0
        easeout 12 alpha 1.0
    show n_rects_right zorder 4:
        yoffset -20 alpha 0
        easeout 12 alpha 1.0
    show n_rects_mouth zorder 4:
        yoffset -20 alpha 0
        easeout 12 alpha 1.0
    $ style.say_dialogue = style.edited
    n "Зачем я на тебя надеялась?"
    n "Зачем я старалась ради тебя?"
    n "Зачем я искала ту блевотную мангу?"
    n "Зачем, Макс?"
    $ style.say_dialogue = style.normal
    mc "Это ты себя спрашивай."
    $ style.say_dialogue = style.edited
    n "Зря я тебе верила."
    n "Ты ужасен."
    $ style.say_dialogue = style.normal
    mc "...сказал кусок воображения."
    mc "Был бы я ужасен, не вступил бы в Литературный клуб."
    $ style.say_dialogue = style.edited
    n "Нет, ты ужасен, Макс, именно сейчас."
    $ style.say_dialogue = style.normal
    mc "Ой, да пошла ты в задницу!"
    show natsuki_ghost_blood zorder 3
    $ style.say_dialogue = style.edited
    n "ТЫ УРОД, МАКС!"
    n "ТЫ БРОСИЛ МЕНЯ!"
    n "КИНУЛ МЕНЯ!"
    n "У МЕНЯ БОЛЬШЕ НИКОГО НЕТ!"
    n "Я ВСЕГО ЛИШЬ ХОЧУ ПОИГРАТЬ!"
    n "ПОЧЕМУ ДРУГИЕ МОГУТ, А Я НЕТ?!"
    n "ПОЧЕМУ Я ВСЕГДА ОБДЕЛЕНА?!"
    n "ПОЧЕМУ У ДРУГИХ ВСЁ ЕСТЬ?!"
    n "ПОЧЕМУ У МЕНЯ НЕТ НИЧЕГО?!"
    n "ХОТЯ Я БОЛЬШЕ ВСЕХ НИХ ЗАСЛУЖИВАЮ ВНИМАНИЕ!"
    n "Я ИСКРЕННЕ ЭТО ЗАСЛУЖИВАЮ!"
    n "А ОНИ НЕТ!"
    n "ИМ НА ЭТО ПЛЕВАТЬ!"
    n "А МНЕ НЕ-Е-ЕТ!!!"
    n "НО ОНИ ПОСТОЯННО ЭТИМ ДОВОЛЬСТВУЮТСЯ!!!"
    n "А МЕНЯ РАЗЪЕДАЕТ ОДИНОЧЕСТВО!!!"
    n "ПОИГРАЙ СО МНОЙ, МАКС!!!"
    n "ПОИГРАЙ!!!"
    hide n_rects_mouth
    n ghost2 "ПОИГРАЙ СО МНОЙ!!!"
    $ style.say_dialogue = style.normal
    mc "Иди ты нахрен со своими играми!!!{w=0.25}{nw}"
    $ quick_menu = False
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_left
    hide n_rects_right
    show natsuki ghost3
    show n_rects_neck_right onlayer front zorder 4:
        pause 0.2
        easeout 0.25 zoom 4.5 xoffset 250 yoffset -250
    show n_rects_neck_left onlayer front zorder 4:
        pause 0.2
        easeout 0.25 zoom 4.5 xoffset 250 yoffset -100
    pause 0.2
    hide natsuki
    play sound natsuki_ghost_run
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    hide natsuki onlayer front
    hide n_rects_neck_right onlayer front
    hide n_rects_neck_left onlayer front
    show screen tear_screen(8, offtimeMult=1, ontimeMult=12)
    window hide(None)
    stop music
    play noise_1 g2
    pause 2.0
    stop noise_1
    hide screen tear_screen
    $ quick_menu = True

    show black

    call skip_block_off
    $ blocker = False
    $ n_name = _("Нацуки")

    return
