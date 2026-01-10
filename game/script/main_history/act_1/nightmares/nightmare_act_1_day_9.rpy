
screen punch_yuri_ghost_a1_nd9:
    button:
        area(435, 0, 425, 720)
        mouse "punch"
        action [Play("sound", "mod_assets/sound/body/hit.mp3"), Return()]




label nightmare_act_1_day_9:

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

    call window_open
    call autosave
    mc "Да чёрт!"

    scene bg bedroom at mc_bed
    show dark
    with dissolve_scene_full
    mc "Что ж тебе не спится?!"
    "Вот стоило только один раз глаза открыть во время полусна, и на тебе..."
    mc "У-у-у..."
    "И так, и этак некомфортно..."
    "А почему?"
    "Правильно, туалет!"
    "Поэтому никогда нельзя прогонять сон."
    "......"
    mc "Ну пошли-пошли..."
    "Как только мочевой пузырь не разъедается, если за ночь в нём много жидкости скапливается?..."
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    "Ура, теперь я могу уснуть с полным спокойствием..."
    play sound doorbell_mc volume 0.5
    pause 1.0
    "......"
    "Это ещё что?!"
    "Кого разобрало в разгар ночи?"

    scene bg mc house hallway night with wipeleft_scene
    "..."
    "Вроде тихо..."

    scene black with dissolve
    pause 0.25
    "В глазке сплошная мгла..."
    "Если бы тут рядом кто-то стоял, то сразу бы увидел."

    scene bg mc house hallway night with dissolve
    pause 0.25
    "Идите вы нафиг с такими приколами!"
    "..."
    "Что это под дверью торчит?"
    "..."
    "Бумажка...{w}попачканная...{w}кровью?!"
    call show_poem(note_yg, music=False, paper="mod_assets/elements/poems/note_yg.png")

    $ nightmare_active = True

    if persistent.censorship:
        mc "Твою мать!"
    else:
        mc "Блять!"
    mc "Опять!"
    "Мозг, зараза!"
    "Что с тобой не так?!"
    "Фу, я даже держать это не хочу!"
    play sound paper_torn_out
    pause 1.0
    "И думать, что там написано и измазано!"
    "..."
    mc "...значит, я в кошмаре."
    "И как мне очнуться?"
    "Нет, я ТОЧНО уверен, что это кошмар."
    "Плевать на всю реалистичность, уже напарывались на такое два раза."
    "Юри бы так не поступила."
    "Ни со стихом, ни с подкидыванием его таким...{w}неадекватным способом."
    mc "..."
    "Что делать-то?!"
    if persistent.censorship:
        "Ждать, когда на меня выпрыгнет какая-то хрень?"
    else:
        "Ждать, когда на меня выпрыгнет какая-то херня?"
    "Треснутся башкой, чтобы потерять сознание?"
    "Ага, чтоб голову разбить в реальном мире."
    "Или попытаться взять и уснуть..."
    "Ну тоже «уход в себя», верно?"
    "Только наиболее безопасный."
    "..."
    "Окей, попробуем запереться в спальне и уснуть."
    "Лишь бы на меня кто-нибудь не сиганул..."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1
    play sound closet_close
    pause 1.0

    call window_open
    scene bg bedroom
    show dark
    with dissolve
    mc "Так, никого..."
    "Пусто..."
    mc "Фух..."
    "Дверь запер, ложимся в постель..."

    scene black
    show dark zorder 2
    with dissolve
    pause 0.25
    "Примащиваемся поудобнее, полностью подмяв под себя одеяло, чтобы чувствовать себя безопаснее..."
    "..."
    "Вот."
    "И закрываем глаза..."
    window hide

    pause 6.0

    call skip_block_on
    $ quick_menu = False

    window auto
    "...кто дышит мне в лицо?..."
    $ y_name = _("Юри?")
    show yuri turned body neut cm e3a n4 hup at e11
    pause 0.5
    show yuri me
    y "...хах..."
    show yuri om b1b
    y "Зачем...{w}ты открыл глаза?"
    show yuri me
    mc "......"
    show yuri -b1b
    y "Закрой..."
    show yuri happ om ce
    y "Ты должен всё прочувствовать, темнота усилит наслаждение..."
    show yuri mn
    mc "Уйди к чёрту из моей головы."
    show yuri yand om oe hdown
    y "{sc=1.5}Я больше не могу себя сдерживать!{/sc}"
    show yuri ce
    y "{sc=1.5}Я перевозбуждена!{/sc}"
    show yuri oe
    y "{sc=1.5}Я хочу удовлетворить тебя!{/sc}"
    y "{sc=1.5}Я хочу слиться с тобой в экстазе!{/sc}"
    y "{sc=1.5}Я хочу, чтобы все наши жидкости вышли наружу\nи перемешались!{/sc}"
    y "{sc=3}ЛЮБИ МЕНЯ!!!{/sc}"
    $ y_name = _("{glitch=15}{color=#000}Юри{/color}{/glitch}")
    show yuri cm
    mc "{sc=3}ВАЛИ ОТСЮДА!!!{/sc}"
    call screen punch_yuri_ghost_a1_nd9
    scene white
    scene black with dissolve
    pause 0.25
    mc "{sc=3}ОТВАЛИ ОТ ОДЕЯЛА!{/sc}"
    y "{sc=3}ПОЧУВСТВУЙ МОЁ ГОРЯЧЕЕ ТЕЛО!!!{/sc}"
    mc "{sc=3}ИДИ НАХРЕН, ФАЛЬШИВАЯ ЖЕНЩИНА!!!{/sc}"
    y "{sc=3}Я НЕ МОГУ СЕБЯ КОНТРОЛИРОВАТЬ!!!{/sc}"
    "{sc=3}ДА ЧТО ТЫ ТАКАЯ БРЫКАЮЩАЯСЯ?!{/sc}"
    "{sc=3}НАДО РЕЗКО ОТПИХНУТЬ ЕЁ В СТОРОНУ--{/sc}{nw}"
    window hide

    play sound hit_wood
    show white zorder 3:
        alpha 1
        ease 0.25 alpha 0

    call skip_block_off
    $ y_name = _("Юри")

    return
