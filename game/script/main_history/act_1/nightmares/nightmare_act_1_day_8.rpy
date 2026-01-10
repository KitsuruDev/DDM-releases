
label nightmare_act_1_day_8:

    pause 3.0
    show loading_sign_mc at loading_sign_position with dissolve
    pause 4.0
    hide loading_sign_mc with dissolve
    pause 1.0

    call window_open
    call autosave
    "М-м-м, блин..."
    "Снова проснулся из-за Моники."
    "То неподвижно спит, то ворочается."
    "То опять не двигается."
    "Почему нельзя лежать спокойно?"
    "Неужто это всё из-за алкоголя?"
    "Ай, ну конечно, ещё в туалет захотелось..."
    "Прям флэш-рояль."
    "Придётся аккуратно встать, чтобы не разбудить Монику, и быстренько утолить свои потребности."
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    "Пусть либо глаза мои быстро к черноте привыкнут, либо пусть свет на улице усилится."
    "Тьма-тьмущая везде -- нихрена не видно."
    "Либо я слишком резко вылетел из освещённой ванны."
    "Ладно, передвигаемся по памяти и ощущениям."
    "Лишь бы так не втемяшиться во что-нибудь..."

    scene bg monika house bedroom night 2 with wipeleft_scene
    "Ну вот, тут хоть посветлее."
    "..."
    "...этот листок с пьяными каракулями Моники теперь не даёт моему любопытству покоя."
    "Когда ещё в жизни увидишь старания человека, даже когда он был пьяным в зю-зю?"
    call show_poem(note_mmm_1, music=False)
    if persistent.censorship:
        "Что это за хрень?!"
    else:
        "Что это за херня?!"
    "Тут ещё с обратной стороны что-то измазано..."
    call window_close

    play sound page_turn
    show drawing_monika_nightmare with Dissolve(1.0)
    $ plot_pause()
    hide drawing_monika_nightmare with Dissolve(0.5)
    pause 0.5

    $ nightmare_active = True

    call window_open
    "КРОВЬ И РАЗМАЗАННЫЙ РИСУНОК МОНИКИ?!"
    "Эй, а где она сама?!"
    "Она только что тут лежала!"
    "Куда она делась?!"
    "Она не могла в таком убитом состоянии тихо слезть и уйти из комнаты!"
    "......"
    "Так, стоп-стоп-стоп..."
    "Я что, опять в кошмаре?"
    "Да нет же: окружение, ощущения, мысли, чувства -- всё реалистично..."
    "Тогда откуда на листе...{w}{b}это{/b}?"
    "Это совершенно не поддаётся логике--{nw}"
    play sound toilet volume 0.05
    pause 2.5
    "Звук бачка туалета?"
    "..."
    "...может, я слишком накручиваюсь...{w}но эта бумага всё ещё существует!"
    play sound giggle
    pause 1.5

    scene black with wipeleft_scene
    mc "Моника?"
    "..."
    mc "Эй!"
    mc "Хорош надо мной прикалываться."
    mc "Мне сейчас совсем не до смеха."
    mc "И хватит торчать в коридоре в одних трусах."
    mc "У нас ещё апрель, простудишься же ведь...{nw}"

    call skip_block_on
    $ quick_menu = False
    play sound nun_massacre_scream
    show monika forward body pants yand mr eyes_white at movein_hugs:
        linear 0.5 yoffset 150
    pause 0.1

    if persistent.censorship:
        mc "{sc=3}ТВОЮ МАТЬ!--{/sc}{nw}"
    else:
        mc "{sc=3}БЛЯТЬ!--{/sc}{nw}"
    window hide(None)

    play sound ram_attack
    scene white
    pause 0.3

    call skip_block_off

    return
