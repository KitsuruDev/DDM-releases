
# Нарисованная голова Сайори на плёнке
image bg eyes:
    "images/bg/eyes.png"
    align (0.5, 0.5) anchor (0.5, 0.5) zoom 2.3

image bg eyes_move:
    "images/bg/eyes.png"
    align (0.5, 0.5) anchor (0.5, 0.5) zoom 2.3
    parallel:
        yoffset 1480 ytile 2
        linear 1.0 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat

# Анимированные фоны во время чаепития
image bg_literature_club_tea_party_mc:
    recolorize("gui/menu_bg.png", "#aaa9ad", "#fff", 1)
    subpixel True pos (1100, 430) zoom 0.25 rotate 60
    bg_literature_club_tea_party_animation(5.0, -25, -43)

image bg_literature_club_tea_party_s:
    recolorize("gui/menu_bg.png", "#34B1FF", "#fff", 1)
    subpixel True pos (870, 620) zoom 0.25 rotate 60
    bg_literature_club_tea_party_animation(5.0, -25, -43)

image bg_literature_club_tea_party_n:
    recolorize("gui/menu_bg.png", "#ff367c", "#fff", 1)
    subpixel True pos (410, 620) zoom 0.25 rotate 30
    bg_literature_club_tea_party_animation(5.0, 25, -43)

image bg_literature_club_tea_party_y:
    recolorize("gui/menu_bg.png", "#B957FF", "#fff", 1)
    subpixel True pos (190, 430) zoom 0.25 rotate 30
    bg_literature_club_tea_party_animation(5.0, 25, -43)

image bg_literature_club_tea_party_m:
    recolorize("gui/menu_bg.png", "#4ED42D", "#fff", 1)
    subpixel True pos (635, 388) zoom 0.25 rotate 45
    bg_literature_club_tea_party_animation(4.0, 0, -35)

transform bg_literature_club_tea_party_animation(t, x, y):
    xoffset 0 yoffset 0
    linear t xoffset x yoffset y
    repeat




label act_1_day_8:

    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_a1_d7.unlocked == False:
        $ ach_a1_d7.unlock()

    pause 7.0
    hide loading_sign_mc with dissolve
    pause 1.0

    play sound eyes
    stop music
    show bg eyes_move
    pause 1.2
    hide bg eyes_move
    show bg eyes
    pause 0.5
    hide bg eyes
    show bg eyes_move
    pause 1.2
    show bg eyes
    pause 0.5
    show bg eyes_move
    pause 0.5
    play sound screamer

    scene bg bedroom at mc_bed
    show monika lean happ cm ce at e21:
        xzoom -1
    pause 0.1
    show monika at lhide
    hide monika
    with shake(time=0.2, dist=40)
    pause 1.0

    call window_open
    scene bg bedroom
    show monika forward happ cm ce at t11
    with dissolve
    pause 0.25
    call autosave
    mc "{sc=3}МОНИКА?!{/sc}"
    "{sc=2}Она мне в ухо дула?!{/sc}"
    mc "{sc=1}Какого чёрта?!{/sc}"
    show monika oe
    n "Вопрос неправильный!"
    show sayori turned angr cm oe at l31
    show natsuki turned angr cm oe lhip rhip at l32
    show monika at t33
    pause 0.5
    show natsuki om
    show monika e1d
    n "Макс, какого чёрта?!"
    show natsuki ce
    n "Уже полвосьмого!"
    show natsuki cm
    mc "Ч-что...{w}как?..."
    "Какой я пожёванный..."
    show natsuki cross angr om oe
    n "А вот так!"
    show natsuki cm
    show monika om
    m "Ты проспал."
    show monika cm
    "Не кричите, блин, голова ходуном..."
    show sayori om
    s "Ага!"
    show sayori cm
    "{cps=25}СайоринеговориСайоринеговори--{/cps}{nw}"
    show sayori om ce
    s "А ведь обещал же мне вчера, что...{nw}"
    show monika ce
    "{cps=20}Даёбдаёбтвоюмать......{/cps}{nw}"
    call window_close

    play sound none_transition
    scene black
    show screen new_day(episode)
    pause 4.0
    hide screen new_day

    call window_open
    scene bg kitchen
    show sayori turned happ cm oe school_bag at t41 zorder 2
    show natsuki turned neut cm e1b school_bag at t42
    show monika forward happ cm oe school_bag at t43 zorder 2
    show yuri turned neut cm e1b school_bag at t44
    with dissolve_scene_full
    "А Юри всё-таки пришла."
    show natsuki oe
    show monika om lpoint rhip
    show yuri e1d
    m "Итак, раз все контейнеры заполнены и распределены по сумкам, то сейчас план такой."
    show monika ldown
    m "Как придём в школу, я сразу зайду в учительскую и заберу ключ от клуба, а вы подождёте меня у его входа."
    show monika rdown
    m "Спрячем кексы в кладовке от солнца и посторонних глаз."
    show sayori om ce
    show monika cm
    s "Понятно!"
    show sayori cm oe
    show natsuki om lhip rhip
    show monika neut cm oe
    n "Только надо поглубже их всунуть, а ещё мангой закрыть."
    show sayori neut cm oe
    show natsuki cm
    mc "Да куда ж такой схрон делать?"
    show natsuki ldown rdown b1b
    mc "О кексах, кроме нас, вообще никто не знает."
    show natsuki om
    n "Не в этом дело!"
    show natsuki lhip rhip -b1b
    show yuri dist cm oe
    n "Помнишь, я рассказывала про главу клуба выпечки?"
    show natsuki cm
    show yuri b2b
    mc "Ну?"
    show sayori e1c
    show natsuki anno cm oe
    show monika happ cm oe
    show yuri om
    y "Ребят, нам уже пора выходить..."
    show sayori oe
    show natsuki om ce
    show yuri cm
    n "...мгх, по пути расскажу."
    show sayori happ cm oe
    show natsuki cm
    show monika lean happ om oe school_bag at h43
    show yuri neut cm e1d -b2b
    m "Всё, в путь!"
    show natsuki ldown rdown
    show monika forward happ cm oe school_bag
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 10 day
    show sayori turned happ cm oe school_bag at t41
    show natsuki turned neut cm oe school_bag at t42 zorder 2
    show monika forward happ cm ce school_bag at t43
    show yuri turned neut cm e1b school_bag at t44 zorder 2
    with wipeleft_scene
    show sayori neut cm oe
    show monika oe
    show yuri e1d
    mc "Ну и что там с ней?"
    show natsuki om lhip rhip
    show monika neut cm oe
    n "Так вот."
    n "Ещё когда я была частью того клуба, а она не была президентом, мы уже плохо ладили из-за её самовлюблённого характера."
    show natsuki anno om ce
    n "Она меня вечно донимала."
    show natsuki neut om oe
    n "Неспроста, естественно."
    show sayori e1b
    show natsuki curi cm oe ldown rdown
    mc "Издевалась по приколу, что ли?"
    show sayori oe
    show natsuki om
    n "Нет."
    show natsuki dist om oe
    show monika e1c
    n "В готовке этот «президент» был не особо силён, хотя не знаю, как у неё с этим сейчас..."
    show natsuki neut om oe
    n "В общем, я была лучше в этом деле."
    show natsuki anno om ce
    n "И мне это вышло боком, потому что ей очень понравились мои кексы."
    show natsuki oe
    show yuri e1c
    n "Фифа хотела с их помощью завлекать новых участников."
    show natsuki neut om oe
    show monika oe
    n "Сначала пробовала сделать кексы самостоятельно, но каждый раз у неё не получалось достичь моего уровня."
    n "Тогда она решила выклянчить у меня рецепт или «оригинал», ну а я не хотела с ней этим делиться, потому что знала, что её выберут в качестве главы клуба."
    show natsuki angr om oe
    show yuri e1d
    n "Нельзя было давать ей шанс на новых подчинённых!"
    show natsuki curi cm oe ldown rdown
    mc "Хорошо, и что?"
    show natsuki neut cm oe
    mc "Клуб будет закрыт, кладовка тоже."
    mc "Даже если она узнает про кексы, то сделать ничего не сможет."
    show natsuki om
    n "Надо всегда быть начеку, от неё можно ожидать что угодно."
    show natsuki anno cm oe
    show yuri e1c
    mc "Мне почему-то кажется, что ты слишком сильно паришься на этот счёт..."
    show natsuki om
    n "Это ты просто с ней не знаком."
    show sayori happ cm oe
    show natsuki doub om oe lhip rhip
    show monika e1c
    n "Да и сам подумай: уж слишком подозрительно, что весь Литературный клуб столпился утром в своём классе."
    show natsuki cm
    show yuri e1d
    mc "Хм..."
    show natsuki dist cm oe
    "Нет у меня сейчас желания спорить с её параноей."
    show sayori e1b
    show natsuki ldown rdown
    "Мало ли что там у Литературного клуба с утра?"
    "Почему сразу кексы?"
    show natsuki e1b
    "Хотя...{w}может, и я на её месте таким бы стал?"
    "Ладно, неважно."
    "Странно, что остальные отмалчиваются."
    "Вероятно, они уже и так всё знают."
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    m "Всё, заходим!"
    call window_close

    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club morning with wipeleft_scene
    "Ох..."
    "Клубный класс ранним утром выглядит...{w}довольно непривычно."
    m "{size=19}Доставайте контейнеры.{/size}"
    "Всё такое «мягкое», глаза не режет..."
    s "{size=19}Вот!{/size}"
    n "{size=19}Так, сюда пихайте.{/size}"
    y "{size=19}Разве они здесь вместятся?...{/size}"
    n "{size=19}Ещё как!{/size}"
    "А у меня, кстати, один вопрос."
    "Я тут зачем?"
    "Контейнер я донёс, Нацуки сама у меня его забрала."
    n "{size=19}Бака!{/size}"
    n "{size=19}Не так, дай сюда...{/size}"
    "А ещё 5 человек в кладовке не поместятся."
    mc "Мда..."
    m "{size=19}Всё, все контейнеры?{/size}"
    n "{size=19}Кажется...{/size}"
    s "{size=19}Ура!{/size}"
    show yuri turned happ cm e1d school_bag at t41
    show natsuki turned happ cm oe school_bag at t42
    show monika forward happ cm oe school_bag at t43 zorder 2
    show sayori turned happ cm oe school_bag at t44
    pause 0.2
    show monika om lpoint
    m "Тогда, друзья, расходимся по своим занятиям."
    show monika lean happ om oe school_bag at h43
    m "Жду сегодня всех здесь после уроков для обсуждения организации чаепития."
    show monika cm
    mc "Угу."
    show yuri ce
    show monika forward happ cm ce school_bag
    show sayori om ce lup rup at h44
    s "Я хочу уже сейча-а-ас!"
    show natsuki ce
    show monika om
    show sayori cm ldown rdown
    m "Всему своё время, Сайори!"
    show yuri neut cm e1d
    show natsuki oe
    show monika oe lpoint
    show sayori oe
    m "И кстати, Юри, ты же взяла заварку для чая?"
    show yuri om
    show monika cm ldown
    y "Да, она с собой."
    show yuri happ cm oe
    show monika om ce
    m "Отлично."
    show yuri neut om e1d
    show natsuki pout cm oe
    show monika cm oe
    y "Надо будет ещё наведаться в Клуб выпечки и забрать у них на время сервиз."
    show yuri cm
    show monika neut mh oe lpoint
    show sayori neut cm oe
    m "Я сегодня снова немного задержусь, поэтому сходите за ним без меня."
    show natsuki om e1b
    show monika cm ldown
    n "Аргх, такими темпами фифа точно поймёт, что у нас сегодня кексы!"
    show natsuki cm
    show monika mh
    m "Но нигде больше сервиза нет, Нацуки."
    show natsuki curi om oe
    show monika cm
    show sayori curi cm e1a
    n "Не в этом плане."
    show natsuki pout om oe lhip rhip
    show sayori neut cm oe
    n "Нельзя пускать вас всех вместе за сервизом!"
    show yuri e1b
    n "Это будет выглядеть слишком подозрительно."
    show yuri e1d
    show natsuki neut om oe ldown
    n "Лучше с Юри пойдёт либо один человек, либо никто."
    show natsuki e1b
    n "Пусть думают, что...{w}она новый сорт чая купила и хочет нас им угостить."
    show natsuki cm
    "Если абстрагироваться от её нервозности, то это очень даже недурная идея..."
    show yuri n2
    show natsuki oe rdown
    show monika happ cm oe
    show sayori happ cm oe
    mc "Ну, я могу составить компанию."
    mc "Увижу в глаза этот Клуб выпечки, так сказать."
    show natsuki dist om ce
    n "...во, всё, только вы вдвоём."
    show yuri happ cm oe n1
    show natsuki cm
    show monika lean happ om oe school_bag at h43
    m "Вот и отлично!"
    show natsuki neut cm oe
    show monika forward happ om oe school_bag
    show sayori ce
    m "Всё, всем спасибо, все свободны!"
    show yuri ce
    show natsuki e1b
    show monika cm
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("n")

    call window_open
    play noise_2 school_corridor_light_noise fadein 3.0 volume 0.5
    scene bg school new_class_natsuki day with dissolve_scene_full
    n "Наконец-то большая перемена..."
    "Где там моя...{w}где..."
    "Где «Ванильная симфония»?!"
    "Нет-нет, я что, забыла её взять с собой?"
    "..."
    "Пусто."
    "..."
    "Пусто!"
    "Её нет!"
    "Грх-х-х, теперь надо искать Монику с ключами и снова тащиться в клуб!"
    "И где она может сейчас ошиваться?"
    "Я даже не знаю."
    n "М-м-м, издевательство..."
    "Ладно, похожу по коридорам."
    "Если не найду так, то напишу ей."
    stop noise_2 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 school_corridor_hard_noise fadein 3.0
    play music t6
    scene bg school f3 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    with wipeleft_scene
    "Кх-х, её тут нет!"
    "А может, она вообще не на третьем этаже?"
    "У-у-у, время уходит!"
    "Не надо думать -- надо действовать!"

    scene bg school f2 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 1
    with wipeleft_scene
    "Откуда тут такая толпа на втором этаже?..."
    "..."
    "А-а, ясно."
    "На стыке со старым корпусом ремонт закончили, проход стал открыт."
    "Но это сейчас вообще не к месту!"
    "Так Монику проще пропустить!"
    "..."
    "Ну же..."
    "Где..."
    window hide

    pause 4.0
    show monika forward neut cm e1b school_bag:
        xcenter 700 yanchor 1.0 ypos 0.65
        on show:
            zoom 0.65*0.63 alpha 0.00
            easein .25 zoom 0.65*0.65 alpha 1.00
        on hide:
            easein .25 zoom 0.65*0.63 alpha 0.00
    pause 1.5

    window auto
    "Ага, вот!"
    n "Моника!"
    call window_close
    call skip_block_on

    call screen swing_hand
    pause 1.0
    show monika oe
    pause 1.0
    show monika happ cm oe
    pause 0.5
    hide monika
    pause 3.0
    show monika forward happ cm oe school_bag at t11 zorder 2
    pause 0.2

    call skip_block_off
    call window_open
    show monika om
    m "Привет, Нацуки."
    show monika cm
    n "Да, привет."
    show monika om
    m "Ты что-то хотела?"
    show monika cm
    n "Ага."
    show monika neut cm oe
    n "Мне нужен ключ от клуба, буквально на чуть-чуть, хочу взять себе почитать одну мангу..."
    show monika om e1b
    m "Ум-м..."
    show monika mh oe
    m "Ты его не потеряешь?"
    show monika lpoint rhip
    m "Я хотела сейчас на крыше старого корпуса перекусить, пока перемена позволяет."
    show monika happ om oe ldown
    m "Заодно подышать свежим воздухом."
    show monika cm
    n "Клянусь."
    show monika e1c
    m "Хм..."
    "Я не настолько рассеянная, чтобы его где-то потерять."
    show monika om oe lpoint
    m "Хорошо, держи."
    show monika cm ldown
    n "Спасибо."
    show monika rdown
    n "Верну сразу, как только заберу томик."
    show monika om ce
    m "Договорились."
    show monika cm
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_2 school_corridor_empty_noise fadein 3.0
    scene bg corridor with wipeleft_scene
    "А вот и клуб."
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day with wipeleft_scene
    "Фу, как тут душно..."
    "Эх, запрещено оставлять окна на проветривание, если в классе никого нет."

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    scene bg closet with wipeleft_scene
    "Так, «Ванильная симфония»..."
    "Она стояла где-то тут..."
    call window_close

    call plot_transition

    call window_open
    scene bg corridor with wipeleft_scene
    "Ну вот и всё!"
    "Теперь надо отнести ключ Монике и..."
    "Нет, я сейчас помру от этого спёртого воздуха!"
    "И это ещё когда снаружи +15 градусов."
    "Надо купить что-нибудь прохладное попить, а потом тоже проветриться на крыше."
    call window_close

    call plot_transition

    call window_open
    scene bg school f3 old_corridor
    show mc turned neut cm oe at t41
    with wipeleft_scene
    show mc curi om oe at t11
    mc "О, Нацуки?"
    mc "Тоже жажда мучает?"
    show mc neut cm oe
    n "Ещё как..."
    show mc om
    mc "Ясно."
    show mc cm
    n "Ну-ка, дай-ка выбрать..."
    show mc cross anno om oe
    mc "Эй, не слишком ли нагло вклиниваешься?"
    show mc cm
    n "Ты же ещё не определился с напитком?"
    show mc neut om oe
    mc "Нет."
    show mc anno cm oe
    n "Вот поэтому дай я быстро куплю, а потом можешь выбирать сколько душе угодно."
    show mc turned dist om ce
    mc "Какая же ты сегодня злая..."
    show mc neut cm oe
    n "Не я такая -- жизнь такая!"
    show mc om
    mc "Мда."
    show mc cm

    scene black with dissolve
    pause 0.25
    "Сейчас достанем пару монет..."
    "Та-а-ак..."
    "Вот одна."
    "Та-а-а-ак..."
    "Вот вторая--{nw}"
    play sound coin_fall
    pause 1.0
    n "Ай!"
    n "Зараза, укатилась прямо под него!"
    mc "Что ж ты..."
    n "Да соскользнула!"
    mc "Ладно, дай достану."
    n "Нет!"
    mc "У меня руки длиннее, чем у тебя."
    n "Ты габаритный, а там очень узко."
    n "Я и так дотянусь."
    mc "Пф, окей, дело твоё."
    n "Но всё равно спасибо..."
    call window_close

    call plot_transition

    call window_dialog("mc")

    call window_open
    scene bg school f3 old_corridor
    show natsuki turned nerv cm ce school_bag at t41
    with wipeleft_scene
    show natsuki om
    n "Фух, получилось..."
    show natsuki neut cm oe
    mc "Кстати, не видела сегодня каких-нибудь скрытых шпионов Клуба выпечки?"
    show natsuki om b1d lhip rhip at t11
    n "Какие, нафиг, шпионы?"
    show natsuki cm
    mc "По приколу спросил."
    show natsuki om -b1d ldown rdown
    n "Не было никого."
    show natsuki cm
    mc "Понятно."
    show natsuki curi cm oe
    mc "А то я пока шёл сюда по второму этажу, увидел краем глаза одного паренька у стены в коридоре, что постоянно посматривал в сторону нашего клубного класса."
    show natsuki om
    n "Как он выглядел?"
    show natsuki cm
    mc "Худоват, вытянут, глаза...{w}голубые вроде."
    show natsuki pani cm oe
    mc "А ещё у него почему-то кофта под пиджаком."
    show natsuki om
    n "Угх, это же один из них!"
    show natsuki cm
    mc "Да?"
    show natsuki pout om oe lhip rhip
    n "Да, это брат Рэйко -- главы школьного совета!"
    show natsuki e1b
    n "Вот только по статусу он и близко с ней не стоит."
    show natsuki curi cm oe
    mc "И что его в этот клуб потянуло?"
    show natsuki om ldown
    n "Откуда я знаю?"
    show natsuki e1b
    n "Мне незачем следить за Клубом выпечки."
    show natsuki cm
    mc "Короче, класс закрыт, правильно?"
    show natsuki neut cm oe
    mc "Он ничего не сможет сделать."
    show natsuki rdown
    mc "И воспользоваться положением своей сестры тоже: вряд ли ему кто-то даст запасной ключ."
    show natsuki curi om e1b
    n "Ну я ходила только что в клуб за мангой, одолжив у Моники ключ..."
    show natsuki pout cm oe
    mc "Ты же ведь реально не забыла закрыть дверь обратно на замок, чтобы уберечь свои бедные кексы?"
    show natsuki om
    n "Шутишь?"
    show natsuki cm
    call window_close

    stop music fadeout 7.0
    pause 1.0
    show natsuki e1b
    pause 3.0
    show natsuki neut cm e2b
    pause 3.0
    show natsuki shoc om ce rdown
    pause 2.0

    call window_open
    "«Шутка», я как вижу, удалась."
    show natsuki oe
    n "Дверь..."
    show natsuki cm
    n "Я её закрыла."
    show natsuki e2b
    n "Или нет..."
    show natsuki oe
    mc "Проверь-ка на всякий случай, а то это будет фиаско для всего Литературного клуба."
    show natsuki om
    n "Д-да!"
    show natsuki ce
    n "Сейчас!"
    show natsuki at thide
    hide natsuki
    pause 2.0
    "Будет очень иронично, если глава Клуба выпечки реально решила устроить ограбление руками своих участников."
    call window_close

    call window_dialog_fast_transition("n")

    call window_open
    play noise_2 natsuki_steps_run
    scene black
    "{sc=3}Нет-нет-нет, я точно закрыла эту дверь!{/sc}"
    "{sc=3}С кексами всё в порядке!{/sc}"
    "{sc=3}Я сейчас прибегу и увижу закрытую дверь!{/sc}"
    "{sc=3}Она закрыта, она закрыта, она закрыта!{/sc}"
    call window_close

    pause 3.0
    stop noise_2

    call window_open
    scene bg corridor with wipeleft_scene
    "Вот она!"
    call window_close

    scene black with wipeleft_scene
    play sound closet_open
    pause 0.5

    call window_open
    "{sc=3}НЕТ, Я ЕЁ НЕ ЗАКРЫВАЛА!!!{/sc}"

    scene bg closet with wipeleft_scene
    n "{sc=3}КЕКСЫ!{/sc}"
    "{sc=3}..........{/sc}"
    n "{sc=2}Всё на месте...{/sc}"
    "{sc=1}И никого нет...{/sc}"
    n "Фу-у-у-у-ух..."
    "Пронесло..."
    call window_close

    $ sor_name = "???"
    play sound sora_sneeze
    pause 0.25
    with vpunch
    pause 1.0

    scene bg school literature_club board day with wipeleft_scene
    show sora turned neut cm oe s_scream at t44
    pause 0.2
    hide sora with easeoutright

    window show(Dissolve(0.25))
    "Я видела у него был {b}КЕКС ЗА СПИНОЙ{/b}!{w=0.5}{nw}"
    n "{sc=3}СТО-О-О-О-ОЙ, СКОТИНА!!!{/sc}{w=0.5}{nw}"
    window hide(Dissolve(0.25))
    call skip_block_on

    stop noise_2 fadeout 3.0

    play music natsuki_chasing fadein 3.0

    call qte_act_1_day_8

    call skip_block_off
    stop music fadeout 3.0
    play noise_3 school_corridor_empty_noise fadein 3.0
    pause 1.0
    window show(Dissolve(0.25))
    "...стоп..."
    n "Пха-а-а...."
    "Что?..."
    n "...ха..."
    n "...ха-ха..."
    n "...ха-ха-ха!"
    window hide(Dissolve(0.25))

    call window_dialog_fast_transition("mc")

    call window_open
    scene bg school f3 old_corridor
    show natsuki turned vang cm oe school_bag at i21
    show sora turned sad cm oe at i22
    pause 0.2
    show natsuki om lhip rhip
    n "Ну что, допрыгался, сайгак недоделанный?!"
    show natsuki cm
    show sora neut cm oe
    mc "И всё-таки ты дверь не закрыла..."
    show natsuki om ce
    n "Аргх, Макс, сейчас не это важно!"
    show natsuki oe
    show sora sad cm oe
    n "Важно то, что ОН попытался выкрасть наш кекс!"
    show natsuki cm
    mc "Да?"
    show natsuki shoc cm oe
    mc "Кабинет-то небось всё ещё открыт, ведь так?"
    show natsuki om ce ldown rdown at h21
    n "КХ!"
    show natsuki cm
    show sora neut cm oe
    mc "Так, у нас ещё полперемены есть, давайте в наш клуб перебазируемся."
    show natsuki angr cm oe lhip rhip
    mc "Только не пытайся сбежать, я за тобой слежу."
    show natsuki om
    n "Сначала кекс верни!"
    show natsuki cm
    show sora om ce
    sor "Ох, ладно, это всё равно бы плохо кончилось..."
    show natsuki anno cm oe ldown rdown
    show sora oe
    sor "Держи."
    show sora cm
    call window_close

    call plot_transition

    call window_open
    scene bg club_day
    show natsuki turned doub cm oe lhip rhip at t21
    show sora turned neut cm oe at t22
    with wipeleft_scene
    mc "Ну что ж, колись: кем звать, откуда узнал про выпечку, зачем стырил..."
    $ sor_name = _("Сора")
    show sora om
    sor "Со{image=accent_low_register}{space=-15}ра я."
    show natsuki curi cm oe ldown rdown
    show sora lup bc
    sor "А это Нацуки, я так понимаю?"
    show natsuki om
    show sora cm ldown
    n "Откуда ты меня знаешь?"
    show natsuki cm
    show sora -bc
    mc "Угу."
    show sora om
    sor "И ты тоже в Литературном клубе состоишь?"
    show sora bc
    sor "Я тебя раньше вообще не видел..."
    show sora cm -bc
    mc "Да, недавно переехал, в клубе уже как неделю числюсь."
    show natsuki angr cm oe
    show sora om
    sor "Ясно."
    show sora cm
    mc "Моё имя Макс."
    show sora om
    sor "Хм, хорошо, буду знать."
    show natsuki om lhip rhip
    show sora cm
    n "Алло!"
    show natsuki curi om oe
    n "Тебе Рэйко про меня рассказывала?"
    show natsuki cm
    show sora om rpock
    sor "Ну да, ты же часто в мелкие проблемы попадаешь."
    show natsuki anno cm ce
    show sora cm
    n "Пф-ф..."
    mc "Так, не тяните время."
    show natsuki neut cm oe
    mc "Зачем ты пытался выкрасть наш кекс?"
    show natsuki e2a ldown rdown
    show sora om
    sor "Думаю, Нацуки и сама догадаться может."
    show natsuki om
    show sora cm
    n "Президент..."
    show natsuki cm
    show sora om
    sor "Бинго."
    show natsuki oe b1d
    show sora cm
    mc "И зачем ты ей потакаешь?"
    show sora cross anno om oe
    sor "А что мне остаётся делать?"
    show natsuki -b1d
    sor "Готовить, кроме простых блюд на завтрак, не умею, а никаких занятий больше нет."
    show sora neut om oe
    sor "Если спросите: \"Зачем я тогда вступил в этот клуб?\" -- то отвечу, что из принципа."
    show sora turned anno om oe lface rpock
    sor "Знаете, как мне сестра на пару с преподавателями капала на мозги по этому поводу?"
    show natsuki anno cm oe
    show sora neut om oe ldown
    sor "В итоге примкнулся в конце прошлого учебного года туда...{w}ну куда можно было."
    show natsuki om ce
    show sora cm
    n "Будто других клубов тебе было недостаточно..."
    show natsuki cm
    show sora sad om oe
    sor "Ну а что тут?"
    show natsuki oe
    sor "Дискуссионный клуб развалился, музыкальный тоже, в ваш не захотел, в Клуб изобретателей не захотел, да и--{nw}"
    show natsuki angr om oe lhip rhip
    show sora cm
    n "Поняли, блин, поняли!"
    show natsuki neut om oe b1d rdown
    show sora neut cm oe
    n "Ближе к сути: почему ты согласился помочь Коха{image=accent_low_register}{space=-15}ку?"
    show natsuki cm
    show sora om
    sor "Да она переняла эстафету по капанью на мозги."
    show natsuki -b1d ldown
    show sora anno om oe lface
    sor "Ребят, реально, простите меня за этот маразм, но знали б вы, как она мне все уши этими кексами прожужжала."
    show natsuki pout cm oe
    show sora angr om ce
    sor "\"Сора, от них зависит будущее нашего клуба\", \"Я хочу уметь их готовить лучше, чем Нацуки, Сора!\", \"Мне нужно знать, из чего они состоят, Сора!\", \"Помоги мне с этим, Сора!\""
    show sora omt ldown
    sor "Тьфу!"
    show sora cm
    mc "Она прям помешанная."
    show sora anno om oe
    sor "Скорее, эгоистичная и капризная."
    show natsuki e1b
    show sora sad cm oe
    mc "Мда, не повезло тебе со всей ситуацией в целом..."
    show sora om
    sor "Судьбу не выбирают, так что приходится терпеть."
    show natsuki oe
    show sora neut om oe lup
    sor "В общем, не выдержал я и решил испытать удачу, лишь бы она отвяла с этой темой."
    show sora ldown
    sor "И как видите...{w}я здесь...{w}вместе с вами."
    show natsuki curi cm oe
    show sora cm
    mc "Хм, ясно..."
    show natsuki om
    n "Нет, подожди."
    show natsuki neut om oe b1d lhip rhip
    n "Откуда вы узнали, что у нас тут кексы?"
    show natsuki angr cm oe -b1d
    show sora anno om ce
    sor "Нездоровое желание Кохаку + твоя известность, как хорошего пекаря, в нашем клубе + её наблюдения = ..."
    show natsuki vang cm ce
    show sora cm oe
    n "...г-гх!"
    show sora om
    sor "Страйк."
    show sora neut om oe
    sor "Честно, я пытался отговорить её от этой идеи, но всё бестолку."
    show natsuki om
    show sora cm
    n "Почему мне везёт на таких...{w}ненормальных личностей..."
    show natsuki pout cm oe
    show sora anno cm oe
    mc "Ты бы к учителям обратился."
    show sora cross anno om oe
    sor "Так уже."
    sor "Они ничего не могут с ней сделать без должных оснований и улик -- всё это бесполезно."
    sor "А одному их наскрёбывать очень долго."
    sor "Так ещё и в сталкинге обвинят."
    show sora ce
    sor "Я уже не знаю, что делать с Кохаку..."
    show natsuki e1b
    show sora cm
    n "М-м-м..."
    show natsuki oe
    show sora sad om oe
    sor "И возвращаться обратно с пустыми руками не могу: начнёт капать на мозги ещё сильнее."
    show sora cm
    mc "Патовая ситуация..."
    show natsuki anno om oe
    n "Нет, я не буду отдавать кекс."
    show natsuki cm
    show sora turned sad cm oe rpock
    sor "..."
    show natsuki curi cm oe
    show sora neut cm oe
    mc "А что именно она хочет изучить в этих кексах?"
    show sora om lup
    sor "Да всё подряд: состав теста, начинки, глазури."
    show natsuki lsur cm oe ldown rdown
    show sora bc
    sor "Однако последние два пункта её волнуют больше всего."
    show sora cm ldown -bc
    n "Кхф-кхф..."
    mc "Что ты смеёшься?"
    show natsuki sedu om ce lhip rhip
    show sora curi cm oe
    n "Мы ей сейчас троянского коня организуем..."
    show natsuki cm
    mc "Чего?"
    show natsuki laug om oe
    show sora lsur cm oe
    n "А ты представь её выражение лица, когда перед ней будет стоять кекс, от которого будет только оболочка из теста!"
    show natsuki cm
    mc "Ну нифига себе препарации..."
    show natsuki happ cm oe
    show sora neut cm oe bc
    mc "И чем же ты всё выедать и соскабливать будешь?"
    show natsuki om
    n "Вилка и ложка!"
    n "С собой же поесть беру."
    show natsuki neut cm oe
    mc "Я думал, у тебя палочки."
    show natsuki om
    n "Нет, к ним я так и не привыкла."
    show natsuki cross sedu om oe
    n "Тем более я пекарь!"
    show natsuki ce
    n "Одна из главных черт пекарей -- тонкость и акккуратность."
    show natsuki cm
    "В жизни не слышал столь сложного оправдания ради того, чтобы пожрать."
    show natsuki turned neut cm oe
    show sora om lup
    sor "А мне что сказать?"
    show natsuki curi om oe rhip
    show sora cm ldown
    n "А чего тебе вообще говорить?"
    show natsuki neut om oe
    show sora -bc
    n "Сделаешь вид, будто не знал нашего умысла, случайно попал на «обманку» в одном из лотков."
    show natsuki rdown
    n "Твоё дело доставить экземпляр, так?"
    n "Остальное не волнует."
    show natsuki cm
    show sora sad om ce
    sor "Боюсь, что это только ещё больше её раззадорит..."
    show natsuki doub om ce lhip
    show sora neut cm oe
    n "Ну и пусть, будет знать своё место!"
    show natsuki neut om oe
    n "И чем больше она будет злиться, тем больше она будет косячить."
    show natsuki sedu om ce
    show sora anno cm oe
    n "Что в конечном итоге сыграет с ней злую шутку."
    show natsuki neut cm oe
    mc "Не думаю, что это хорошая идея."
    show natsuki pout cm oe ldown
    show sora om
    sor "Вот-вот."
    show sora ce
    sor "Она не такая импульсивная."
    show natsuki om
    show sora neut cm oe
    n "И что тогда с ней, предлагаете, делать?"
    show natsuki cm
    mc "..."
    show sora om ce bc lup
    sor "Если бы я знал..."
    show natsuki neut cm oe
    show sora cm oe -bc ldown
    mc "Мгх, мы тут уже заговорились."
    mc "Времени осталось немного, и выбора у нас нет."
    mc "Нацуки, делай свои «препарации», а ты, Сора, сделаешь вид, что взял случайный кекс."
    show natsuki om
    n "Ок."
    show natsuki cm at thide
    hide natsuki
    pause 0.2
    show sora om
    sor "...о-ох, хорошо."
    show sora cm
    mc "И да, я ещё сегодня вас навещу вместе с другой участницей нашего клуба, нам понадобится сервиз."
    show sora om bc lup
    sor "А это не та, которая с длинными фиолетовыми волосами?"
    show sora cm -bc ldown
    mc "Да, она."
    show sora om
    sor "Соклубницы мне рассказывали про эту девушку, вроде бы она в прошлом учебном году иногда захаживала по такой же просьбе."
    show sora cm
    mc "Хм."
    show sora bc
    show natsuki turned neut cm oe b1d at t21
    pause 0.2
    show natsuki om lhip rhip
    n "Знаете что?"
    show sora lsur cm oe -bc
    n "Макс, возьми и меня тоже!"
    show natsuki cm ldown rdown
    mc "Ага, конфликта перед нашей посиделкой ещё не хватало."
    show natsuki om
    show sora sad cm oe
    n "А когда будет такой же повод поквитаться с этой самодуркой?"
    show natsuki angr om ce -b1d lhip rhip
    n "Надо закрыть данный вопрос раз и навсегда!"
    show natsuki cm
    mc "Плохо это всё кончится..."
    show natsuki neut cm oe
    show sora happ om oe be
    sor "Я был бы только рад, если вам удастся до неё достучаться."
    show natsuki happ cm oe ldown rdown
    show sora -be
    sor "Так что поддержу вас в разговоре, если понадобится."
    show sora cm
    mc "Ладно, хорошо."
    "Надеюсь, долго и болезненно это длиться не будет."
    call window_close

    call plot_transition

    call window_dialog("n")

    call window_open
    scene bg school literature_club board day
    show sora turned neut cm oe rpock at t21
    show mc turned neut cm oe at t22
    with wipeleft_scene
    n "Так, начинка съедена..."
    n "Дырка сбоку небольшая, сразу не заметит..."
    show mc cross neut om oe
    mc "Ага, небольшая."
    mc "С этой дыркой он, как бракованный: слишком в глаза бросается при определённом ракурсе."
    show sora om lup
    show mc cm
    sor "Ну я могу сказать, что взял второпях наиболее близкий кекс..."
    show sora happ cm oe ldown
    n "Да, отлично!"
    show mc turned neut cm oe
    n "Мы якобы специально поставили его ближе к краю в контейнере, пусть так и подумает!"
    show mc doub om ce
    mc "Натянуто всё это выглядит, но раз уж начали, то надо довести до конца."
    show mc neut om oe
    mc "Я так понимаю, на этом пока всё?"
    show mc cm
    n "Да."
    show sora om rdown
    sor "Давайте тогда этот кекс, и я пойду."
    show sora cm
    n "Вот, на."
    show sora om
    sor "Увидимся после уроков."
    show sora cm
    show mc om
    mc "Да, увидимся."
    show mc cm
    n "Ага."

    scene black with wipeleft_scene
    mc "Нацуки..."
    n "Что?"
    mc "Не нравится мне его «история»..."
    mc "Как-то наигранно она звучит."
    n "Без понятия, что ты там услышал, но я ничего такого не заметила."
    mc "Не верю я, чтобы такой парень с головой на плечах так безответственно подошёл ко вступлению в клуб."
    n "Да кто его знает?"
    n "И откуда у тебя взялось такое подозрение?"
    n "Я тебя что, скепсисом заразила?"
    mc "Кхм..."
    "Сам же с утра мне особо не доверял, а теперь пуще меня так думает."
    mc "Ладно, пойду уже."
    mc "Только не забудь запереть дверь, а?"
    n "Закрою-закрою!"
    call window_close

    call plot_transition

    call window_open
    scene bg school f2 old_stairwell center with wipeleft_scene
    n "Всё...{w}ура..."
    "Манга у меня...{w}кексы в порядке...{w}дверь закрыта..."
    "Осталось только отнести Монике ключ, и после этого можно будет тупо выдохнуть..."
    "Не так я хотела провести всю перемену..."
    stop noise_3 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 wind fadein 2.0
    scene bg school old_rooftop day with wipeleft_scene
    n "Фе-е-е..."
    "Воздух!"
    "Как же я...{w}вскипела...{w}после чёртовых ступенек!"
    show monika forward happ cm oe school_bag at r11
    pause 0.5
    show monika om
    m "О, Нацуки, принесла ключ?"
    show monika neut cm oe
    n "Д-да...{w}забирай, спас-сибо..."
    show monika mh lpoint
    m "Ты довольно долго пробыла в клубе."
    show monika ldown
    m "И ещё выглядишь запыхавшейся..."
    show monika b1f
    m "Что-то случилось?"
    show monika cm -b1f
    n "Ха, я в ф-форме!"
    n "Всё отлично!"
    n "Просто решила чуть-чуть перебрать м-мангу в кладовке."
    n "А вспотела я из-за с-ступенек!..."
    show monika om
    m "Ты только поаккуратнее, не торопись."
    show monika cm
    n "К-конечно!"
    n "Я пойду-у..."

    scene black with wipeleft_scene
    "...и помру на ступеньках, а-а-а..."
    stop noise_1 fadeout 4.0
    call window_close

    call window_dialog_long_transition("mc")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    "..."
    "...всё?"
    "Это же был последний урок?"
    "Странно, в этот раз время пролетело довольно быстро..."
    "Хотя и немудрено: праздник с кексами на носу."
    "А это вам не рутинная стихотворная писанина."
    "..."
    "А, конечно, обрадовался..."
    "Ещё разговор с президентом Клуба выпечки."
    "Что ж у вас вечно какие-то проблемы..."
    "У меня такое ощущение, будто их натягивают из принципа."
    "Практически всё можно было бы решить банальным обсуждением друг с другом по душам."
    "Именно без всякой предвзятости, дерьма и попыток морального давления."
    "Как психически зрелые люди: спокойно сесть, всё обсудить и прийти к логичному заключению."
    "Но нет, на кого в своей короткой жизни не натыкался, вечно стараются морально задавить, наорать, наистерить, прочее-прочее-прочее..."
    "Самих не достало?"
    "Так тяжело исправить в себе эту черту и зажить более лучшей, спокойной жизнью?"
    "Почему надо быть такими упёртыми и агрессивными?"
    "Как же это, блин, бесит и раздражает..."
    "Всё, хватит думать, пора топать в клуб."
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Итак, спустя неделю из угрюмого ученика ты превратился в живого человека с искрами в глазах."
    show mrs_ida cm
    "Ой, нет, сейчас опять начнётся эта избитая тема..."
    mc "Я тоже это заметил."
    show mrs_ida om ce
    mi "Рада, что ты смог социализироваться за столь короткий срок."
    show mrs_ida cm
    "А может...{w}контратаковать?"
    "Просто надоело отверчиваться и что-то мямлить."
    show mrs_ida om oe
    mi "К слову сказать, сегодня я встретила Монику и немного с ней разговорилась."
    mi "Она была очень счастлива, что ты вступил в её клуб."
    show mrs_ida cm
    mc "Ну, есть такое."
    show mrs_ida om bc
    mi "Кстати, как она тебе?"
    show mrs_ida cm
    mc "А?"
    show mrs_ida om -bc
    mi "Я понимаю, что у нас в школе «открытые» любовные отношения под запретом, но ты бы к ней присмотрелся."
    mi "Она тоже успешна в учёбе, как и ты."
    show mrs_ida lup ce
    mi "У неё хорошая фигура и интересный характер, что делает её обаятельной девушкой~"
    mi "Некоторые смельчаки пытались сразить её сердце, но она оказалась более неприступной, несмотря на свою общительность."
    show mrs_ida vsur cm oe
    mc "Ида-сэнсэй, так я с ней уже в отношениях."
    show mrs_ida ldown
    mi "..."
    "Есть пробитие!"
    show mrs_ida me
    mi "...правда?"
    show mrs_ida cm
    mc "Абсолютно."
    show mrs_ida me ce
    mi "Ух ты..."
    show mrs_ida cm oe
    m "{size=19}У-у, Макс, так ты ещё тут?!{/size}"
    show mrs_ida at t22
    show monika forward happ cm oe school_bag at l21
    pause 0.7
    show monika om lpoint rhip
    m "Давай скорее в клуб, нам надо всё успеть!"
    show monika ce ldown rdown
    m "О, Ида-сэнсэй, здравствуйте!"
    show monika neut cm oe
    show mrs_ida me
    mi "Здравствуй, Моника..."
    show monika curi om oe
    show mrs_ida cm
    m "Что-то случилось?..."
    show monika neut cm e2a
    show mrs_ida curi om oe
    mi "Вы правда теперь пара?"
    show monika shoc om oe
    show mrs_ida cm
    m "Что?!"
    show monika cm
    show mrs_ida neut cm oe
    mc "Да!"
    mc "Видите?"
    call window_close

    hide monika with dissolve
    show monika forward shoc cm oe school_bag at e21
    pause 1.0
    show mrs_ida happ cm oe
    show monika om e4c n4 with dissolve

    call window_open
    m "И-и-их!"
    show monika oe
    m "Макс, что происходит?!"
    show monika md
    show mrs_ida om ce
    mi "Ха-ха-ха!"
    show mrs_ida oe
    mi "Как говорится, совет вам да любовь!"
    show mrs_ida cm
    mc "Ладно, простите, Ида-сэнсэй, но у нас реально много дел, которые надо сегодня закрыть."
    show mrs_ida om
    mi "Да-да, не задерживаю."
    show mrs_ida cm
    mc "До свидания."
    show monika cm
    m "Д-д-д..."
    show monika md
    show mrs_ida om ce
    mi "Удачи, ребятки!"
    show mrs_ida cm

    scene black with wipeleft_scene
    mc "{size=19}Чтоб я ещё раз устроил подобное представление...{/size}"
    m "{size=19}Макс, что это было?!{/size}"
    mc "{size=19}Раскрытие наших взаимоотношений.{/size}"
    m "{size=19}Слишком резко и неожиданно!{/size}"
    mc "{size=19}Поверь мне, Моника, если бы ты практически каждый день разговаривала с миссис Идой, то сама бы не выдержала и сделала то же самое.{/size}"
    m "{size=19}М-м-м, не знаю...{/size}"
    call window_close

    call plot_transition

    call window_open
    scene bg corridor
    show monika forward neut cm oe school_bag at t11
    with wipeleft_scene
    mc "Мы первые или нет?"
    show monika om lpoint
    m "До тебя я встретила Сайори и передала ей ключи."
    show monika ldown
    m "Сейчас она должна пересчитывать кексы."
    m "Ей почему-то показался один контейнер пустоватым."
    show monika cm
    mc "Хм."
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg school literature_club board day
    show monika forward happ cm oe school_bag at t44
    with wipeleft_scene
    show monika neut cm oe
    s "Тут всего 27 кексов!"
    s "Я уже несколько раз пересчитала!"
    s "Один исчез!"
    n "Д-да знаю я!"

    scene black with wipeleft_scene
    y "Что случилось, Нацуки?"
    s "Его кто-то украл?!"
    n "Да тихо-тихо-ТИХО!"
    n "Сейчас всё скажу."

    scene bg closet
    show monika forward neut cm oe at t41 zorder 2
    show sayori turned neut cm oe at t42
    show natsuki cross neut cm oe at t43 zorder 2
    show yuri turned neut cm e1d at t44
    with wipeleft_scene
    show natsuki om
    n "О, вы тоже пришли."
    n "Вовремя."
    show monika om
    show natsuki angr cm oe
    m "Так значит, что-то произошло, Нацуки?"
    show monika cm
    show natsuki turned pani om ce at h43
    show yuri angr cm oe
    n "А-а-а, да-да-да-да-да!!!"
    show natsuki angr om oe
    n "Дайте начать!"
    show natsuki anno cm oe
    show yuri om
    y "Нацуки, давай, говори уже."
    show natsuki om ce
    show yuri cm
    n "Пф-ф-ф-ф-ф..."
    show natsuki neut om oe lhip rhip
    show yuri neut cm e1d
    n "Так вот."
    show monika e2a
    show sayori e2a
    show natsuki dist om ce
    show yuri e2a
    n "Да, у нас его как бы...{w}«украли»."
    show monika om at s41
    show sayori om at s42
    show natsuki cm e2d
    show yuri me lup rup at s44
    msy "Ха-а-а..."
    show monika cm
    show sayori cm
    show natsuki pani om oe ldown rdown at h43
    show yuri cm
    n "СПОКОЙСТВИЕ, только спокойствие!"
    show monika oe at t41
    show sayori oe at t42
    show natsuki pout om oe lhip rhip
    show yuri e1d at t44
    n "Начнём с начала."
    show natsuki cm e1b
    show yuri ldown rdown
    n "...м-м..."
    show natsuki nerv om oe ldown rdown
    n "Макс, помоги, ты же всё знаешь!"
    show natsuki cm
    mc "Ну нифига себе!"
    show natsuki md
    mc "Это всё произошло из-за того, что кое-кто забыл закрыть дверь."
    show natsuki me e2b
    n "...грх..."
    mc "Ай..."
    show natsuki neut cm oe
    mc "В общем..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg closet
    show monika forward dist cm oe at i41 zorder 2
    show sayori turned worr cm oe at i42
    show natsuki turned curi cm oe at i43 zorder 2
    show yuri turned anno cm oe at i44
    with wiperight
    show sayori om
    s "Пожалуй, нам стоит устроить чаепитие вне школы..."
    show monika neut cm oe
    show sayori neut cm oe
    show natsuki sedu om oe lhip rhip
    show yuri neut cm e1d
    n "Не-не-не, это прекрасный повод наведаться к этой заразе!"
    show natsuki neut cm oe
    show yuri curi om oe
    y "А сможем ли мы тогда забрать сервиз?"
    show natsuki pout cm oe
    show yuri anno om oe
    y "Ведь конфликт неизбежен..."
    show natsuki om
    show yuri neut cm e1d
    n "Не сразу же он начнётся!"
    n "Сначала вы свой сервиз вытащите, потом я с Кохаку начну спорить."
    show natsuki cm
    mc "Вообще-то не ты одна: я, а ещё Сора."
    mc "Да и то мне кажется, что маловато будет людей с нашей стороны для подобного..."
    show natsuki neut om oe
    n "Она же одна в своей позиции, её никто не поддержит."
    show natsuki cm
    mc "А с чего ты так уверена?"
    show natsuki curi cm oe ldown rdown
    mc "Ты с ней встречалась в последний раз в прошлом учебному году, верно?"
    show natsuki om
    n "...пару раз после ухода пересекалась, но в целом да..."
    show natsuki cm
    mc "Кто вообще знает, кого она могла на свою сторону завлечь за это время?"
    show monika curi om oe lpoint
    show natsuki neut cm oe
    m "Может, тогда стоит наведаться всем вместе?"
    show monika neut mh oe ldown
    m "Это уже не просто конфронтация между двумя людьми, здесь всё выходит на уровень клубов."
    m "Тем более Нацуки -- наша участница, мы не можем просто взять и остаться в стороне."
    show monika cm
    show sayori e2b
    show natsuki pout cm oe
    mc "Это уже какие-то междоусобицы..."
    show sayori oe
    mc "Слушайте, надо вообще к учителям обратиться."
    mc "Сора говорил, что ему это не помогло, но он делал это один."
    mc "Вся эта ситуация -- полный бардак за рамками адекватного понимания."
    mc "Да, вряд ли это изменит поведение Кохаку, однако за нарушение школьных правил она по-любому ответит."
    show monika dist om oe
    show natsuki dist cm oe
    m "Но тогда лучше стоит предъявить весомые доказательства в виде аудио-записи или видео..."
    show monika neut cm oe
    show natsuki om
    n "Да все и так знают, что она ненормальная."
    show monika om lpoint
    show natsuki curi cm oe
    m "А вдруг она натворит что-то такое, за что смогут наказать?"
    show monika cm ldown
    show natsuki om e1b
    n "Ну-у-у..."
    show natsuki neut cm oe
    mc "Ха, записать на диктофон весь разговор, а вместе с ним все прелестные словечки?"
    show yuri pout cm oe
    mc "...а это реально стоит сделать."
    show monika happ cm oe
    mc "Моника, ты гений."
    show monika neut cm oe
    show yuri om
    y "Только тогда нам стоит вести себя сдержанно и прилично..."
    show yuri cm
    mc "Да."
    show natsuki anno cm oe
    mc "Нацуки, услышала?"
    mc "Не надо на неё срываться, иначе и тебе прилетит."
    show natsuki om lhip rhip
    n "Да-да, понятно."
    show sayori om
    show natsuki neut cm oe
    show yuri neut cm e1d
    s "Стойте..."
    show sayori curi om oe
    show natsuki curi cm oe ldown rdown
    s "Мы кексы снова оставим?"
    show monika om e1c
    show sayori cm
    show natsuki ce
    show yuri e2b
    m "У-у..."
    "Хм-м-м, брать Сайори с собой в будущее «месиво» совершенно не хочется..."
    show monika neut cm oe
    show sayori neut cm oe
    show natsuki neut cm oe
    show yuri e1d
    mc "А что если тебе остаться здесь, чтобы приготовить столы и расставить кексы?"
    show monika om
    m "Ты уверен, что это хорошая идея перед конфликтом?"
    show monika cm
    mc "Пф, тоже мне..."
    show sayori curi cm e1a
    mc "Сайори просто запрётся в классе."
    mc "А когда с цирком будет покончено, то она нам откроет дверь."
    show monika e1b
    show sayori doub cm ce
    s "Хм-хм-хм..."
    show monika oe
    show natsuki curi cm oe
    show yuri om
    y "Знаете, может, мне стоит тоже запереться здесь вместе с сервизом?"
    show yuri anno om oe
    y "От меня никакого толка не будет..."
    show monika happ cm oe
    show sayori happ om oe
    show natsuki neut cm oe
    show yuri neut cm e1d
    s "Хорошо, я согласна!"
    show sayori cm
    show yuri happ om oe
    y "Заодно помогу Сайори..."
    show monika om
    show yuri cm
    m "Ладно, договорились!"
    show monika lpoint rhip
    m "Юри, Макс, сходите за сервизом в Клуб выпечки, мы с Нацуки спрячемся у лестницы."
    show monika ldown
    m "Потом ты, Юри, вернёшься обратно и поможешь Сайори."
    show monika rdown
    m "А мы в этом время включим диктофоны на мобильниках и займёмся проблемой."
    show monika neut cm oe
    show sayori neut cm oe
    show yuri neut cm e1d
    mc "Снимать на камеру не будем?"
    show monika mh
    m "Только в крайнем случае."
    m "Не будем выдавать свои намерения."
    show monika cm
    mc "Понял."
    show monika happ om oe lpoint rhip
    show sayori happ cm oe
    show natsuki happ cm oe
    show yuri happ cm oe
    m "Итак, друзья!"
    show monika rdown
    m "Начинаем нашу «внезапную, но необходимую операцию» перед праздником!"
    show monika ce ldown
    show sayori ce
    show natsuki ce
    show yuri ce
    m "Вперёд!"
    show monika cm
    call window_close

    call plot_transition

    call window_open
    scene bg school f1 old_stairwell center
    show monika forward neut cm oe at t31 zorder 2
    show natsuki turned neut cm oe at t32
    show yuri turned neut cm e1d at t33 zorder 2
    with wipeleft_scene
    mc "И где находится этот Клуб выпечки?"
    show monika mh lpoint
    m "Налево по коридору, а дальше сами поймёте."
    show monika cm ldown
    mc "Угу."
    show monika mh e1b
    show natsuki e1b
    show yuri happ cm oe
    m "И если что, помоги Юри сервиз донести, а то мало ли..."
    show monika happ cm oe
    show yuri om lup
    y "Ничего, я справлюсь сама, уже не раз в руках его держала."
    show yuri cm
    mc "Посмотрим."
    show natsuki oe
    show yuri ldown
    mc "Ну, мы выдвигаемся?"
    show monika om
    m "Да."
    show monika lpoint
    m "Как Юри мимо нас проходить будет, то сразу подойдём."
    show monika cm ldown
    mc "Понял, договорились."
    mc "Пошли."
    show yuri ce

    scene black with wipeleft_scene
    mc "Кстати, а состав там какой?"
    y "Довольно дружелюбный."
    mc "Дружелюбный?"
    y "Да, это может показаться немного странным, учитывая их президента..."
    y "...но он в действительности таким и является."
    mc "Звучит как-то подозрительно..."
    "А может, Юри права?"
    "А может, нет?"
    "А может...{w}Нацуки реально заразила меня своей паранойей."
    "Ладно, всё, успокойся."
    "Всё спланировано."
    "На нашей стороне целых 4 человека, включая меня."
    "Но вот сердце прямо выпрыгнуть и убежать хочет..."
    mc "Эй, Юри..."
    y "Да?"
    mc "А тебе самой не волнительно на душе?"
    y "Есть такое чувство, однако...{w}мы так уже подготовились, что волнение здесь неуместно."
    y "К тому же после этого будет чаепитие!"
    mc "Даже так..."
    y "Но ведь ты не один, верно?"
    y "Мы Литературный клуб: держимся друг за друга горой."
    y "...в чём ты и сам уже убедился по недавним событиям..."
    mc "Хм..."

    scene bg corridor:
        xzoom -1
    show yuri turned happ cm oe at t11
    with wipeleft_scene
    mc "{size=19}Ладно, давай покончим с этим.{/size}"

    $ koh_name = "???"
    $ e_name = "???"
    $ kam_name = "???"
    $ f_name = "???"

    scene black with wipeleft_scene
    y "{size=19}Нужно постучаться...{/size}"
    mc "{size=19}Ты или я?{/size}"
    y "{size=19}...давай я.{/size}"
    y "{size=19}Я здесь уже была, меня тут в лицо знают.{/size}"
    mc "{size=19}Хорошо.{/size}"
    pause 0.5
    play sound door_knock
    pause 1.8
    f "{size=16}А?!{/size}"
    kam "{size=16}Кья!{/size}"
    koh "{size=16}ТИХО!{/size}"
    koh "{size=16}Что случилось?{/size}"
    kam "{size=16}Она дёрнулась и испугала меня!{/size}"
    koh "{size=16}Она тебя?!{/size}"
    koh "{size=16}Ха-ха-ха, не верю!{/size}"
    koh "{size=16}Ты сама дёргаешься так, что мы тут все на нервах сидим!{/size}"
    mc "{size=19}Они собираются дверь открывать?{/size}"
    y "{size=19}Без понятия...{/size}"
    kam "{size=16}Ш-ш-ш-ш-ш!!!{/size}"
    "Это что ещё за кошачье шипение?..."
    sor "{size=16}Бу-у-у...{/size}"
    e "{size=16}Ну всё, хватит!{/size}"
    e "{size=16}Из-за чего ты вскрикнула?{/size}"
    f "{size=16}Там кто-то постучался...{/size}"
    f "{size=16}Или мне показалось...{/size}"
    e "{size=16}Тогда надо проверить.{/size}"
    koh "{size=16}Правильное решение!{/size}"
    $ e_name = _("Эми")
    koh "{size=16}Эми, иди и проверь.{/size}"
    e "{size=16}Почему сразу я?{/size}"
    koh "{size=16}Потому что!{/size}"
    koh "{size=16}Давай, время не ждёт!{/size}"
    e "{size=16}У-у-у!{/size}"
    mc "{size=19}Что-то здесь вообще не пахнет дружелюбием...{/size}"
    y "{size=19}...м-м-м...{/size}"
    call window_close

    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    e "О-о...{w}хо...{w}ого!"

    scene bg corridor:
        xzoom -1
    show emi turned uniform_waist_jacket laug cm ce lhip rhip at t21
    show yuri turned happ cm oe at t22
    with dissolve_scene_full
    play music baking_club fadein 3.0
    show emi om
    e "Юри-чан, привет!"
    show emi cm
    show yuri om
    y "Привет, Эми."
    show yuri cm
    "Это и есть та самая Эми?..."
    show emi happ om oe rdown
    e "А это кто с тобой?"
    show emi cm
    show yuri om e1c lup
    y "Это Макс, он недавно вступил в Литературный клуб, решил составить мне компанию..."
    show emi om ce rhip
    show yuri vsur cm oe ldown
    e "Да ладно, у тебя парень появился?"
    show emi cm
    show yuri mi lup rup at s22
    y "Н-нет!"
    show emi neut cm oe
    show yuri lsur cm oe
    mc "Нет-нет, я просто помочь ей решил."
    show emi anno cm eb
    show yuri neut cm e1d
    e "Мф-ф-ф..."
    show emi pout om eb
    e "Я уж обрадовалась..."
    show emi cm
    show yuri neut cm e1d ldown rdown at t22
    "......"
    show emi neut om oe
    e "Хм, имя у тебя звучит...{w}по-русски."
    show emi ec
    show yuri curi md oe
    e "Ты не из России?"
    show emi cm
    mc "...чего?"
    show emi oe
    mc "Я в Японии родился."
    show emi om ldown
    show yuri neut cm e1d
    e "А-а, просто Фукка много чего успела про Россию рассказать, вот и подумала..."
    show emi happ om oe
    e "Но почему тебя так назвали?"
    show emi cm
    mc "...почему тебе так интересно?"
    show emi om ce
    e "Обычное любопытство."
    show emi neut cm oe
    mc "Про музыкальную группу {color=#fc7e23}MAX{/color} слышала?"
    show emi curi om oe
    e "Э-э-э-э-э..."
    show emi cm
    mc "Ну вот в честь неё меня и назвали."
    show emi om
    e "Звучит как-то сомнительно, но...{w}о-о-оке-е-ей?"
    show emi neut cm oe
    show yuri e1b
    mc "А кто такая Фукка?"
    show emi happ om oe lhip
    e "А, да одна из наших."
    show emi ce
    e "Хочешь, познакомлю?"
    show emi oe
    show yuri e1d
    e "Правда, она очень пугливая, но так прикольная."
    show emi neut cm oe
    show yuri om
    y "Эми, можно...{w}нам сервиз взять для чая?"
    show emi happ om ce
    show yuri cm
    e "О, так вы за этим!"
    show emi oe
    show yuri happ cm oe
    e "Лады, за мной!"
    show emi neut om oe ldown rdown
    e "Макс, ща, подожди минутку."
    show emi happ cm oe
    mc "Угу."
    show emi at thide
    hide emi
    show yuri ce at thide
    hide yuri
    pause 0.5
    "Эта ваша Эми -- какая-то смесь Сайори и Нацуки..."
    "Мда, чувствуется, что в этом клубе БОЛЕЕ экстравагантные личности."
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down neut_cm_oe at i21
    pause 0.2
    show monika neut_cm_oe
    n "А, Эми..."
    show monika forward neut om oe at t11
    m "Что-то ты со вздохом это сказала."
    show monika cm
    n "Да так, вспомнила, как раньше с ней общалась..."
    show monika om b1f
    m "А сейчас?"
    show monika cm
    n "Поверхностные разговоры, которые быстро заканчиваются."
    show monika om
    m "А что так?"
    show monika cm -b1f
    n "Да не знаю, как-то вот так вышло."
    n "Возможно, потому что из клуба ушла, стали реже встречаться."
    show monika e1b
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    $ f_name = _("Фукка")
    e "{size=16}Фукка, давай, иди, знакомься!{/size}"
    f "{size=16}Не-не-не-не-не-не--{/size}{nw}"
    e "{size=16}Мы пока сервиз подготовим!{/size}"
    e "{size=19}Макс, принимай!{/size}"
    show fukkacumi turned shoc om e4c at t33
    f "АП!"
    show fukkacumi cm
    f "..."
    show fukkacumi oe
    mc "Привет?"
    show fukkacumi vsur cm oe lfist rfist at t22
    f "{cps=20}П-п-п-п-п--{/cps}{nw}"
    show fukkacumi mj
    mc "Всё нормально, я не кусаюсь!"
    show fukkacumi neut cm oe ldown rdown at t11
    mc "Расслабься."
    show fukkacumi om
    f "...ривет..."
    show fukkacumi cm
    mc "Ну..."
    mc "Как тебя зовут?"
    show fukkacumi om e1b
    f "Фу...{w}фу..."
    show fukkacumi cm oe
    mc "Фукка, верно?"
    $ f_name = _("Фуккацуми")
    show fukkacumi om
    f "Фуккацу{image=accent_low_register}{space=-15}ми..."
    show fukkacumi cm
    mc "А моё -- Макс."
    mc "Приятно познакомиться."
    f "..."
    "Да что ж так кисло..."
    mc "Мне Эми сказала, что ты из России."
    show fukkacumi om
    f "Да."
    show fukkacumi e1b
    f "Папа оттуда."
    show fukkacumi bom boe
    f "{cps=40}Вообще моё истинное имя -- {color=#407fff}Анастаси{image=accent_low_register}{space=-15}я{/color}.{/cps}{w=1.0}{nw}"
    f "{cps=50}Или сокращённо -- {color=#407fff}На{image=accent_low_register}{space=-15}стя{/color}.{/cps}{w=1.0}{nw}"
    f "{cps=60}Часть своего детства я провела в России: в городе Москва и в Московской области, где живут дедушка и бабушка моего папы.{/cps}{w=1.0}{nw}"
    f "{cps=70}Но когда я подросла, то перестала туда приезжать, потому что поступила в эту школу, а из-за того, что я любила играть на гитаре, я вступила в музыкальный клуб--{/cps}{nw}"
    show fukkacumi bcm
    mc "А-а-а, слишком много информации, СТОЙ!" with vpunch
    f "..."
    mc "Куда ж ты так несёшься..."
    show fukkacumi at t21 zorder 2
    show kohaku cross happ cm oe at t22
    pause 0.3
    show fukkacumi neut cm oe
    show kohaku om
    koh "Ха, давненько к нам новые люди не захаживали!"
    show kohaku oe
    koh "Как тебя звать, паренёк?"
    show kohaku cm
    mc "Макс."
    mc "А ты кто будешь?"
    show fukkacumi e1b
    show kohaku om ce
    koh "От тебя зависит, хе-хе-хе."
    $ koh_name = _("Кохаку")
    show kohaku oe
    koh "А если серьёзно, то Кохаку, глава Клуба выпечки."
    show kohaku cm
    "А вот и главный враг..."
    mc "Ясно."
    show fukkacumi e2a lfist rfist at h21
    show kohaku angr om oe
    koh "Эй, Фукка, не прохлаждайся в коридоре!"
    show kohaku neut om oe
    koh "Лучше помоги им там с поиском чашек."
    show kohaku ce
    koh "Каким образом они оказались в разных местах, ума не приложу..."
    show fukkacumi om
    show kohaku cm
    f "П-поняла!"
    show fukkacumi cm at thide
    hide fukkacumi
    show kohaku oe
    pause 0.2
    show kohaku happ cm oe at t11
    mc "А мне-то можно зайти?"
    show kohaku turned happ om ce lup
    koh "Тю-тю-тю, не так быстро, М-а-к-с..."
    show kohaku oe ldown
    koh "Я хочу поговорить с тобой здесь без лишних глаз, так сказать."
    show kohaku ce
    koh "Заодно познакомиться поближе, ага?"
    show kohaku cm
    mc "В каком смысле \"познакомиться\"?"
    show kohaku om oe lup
    koh "Начнём с азов!"
    show kohaku ldown
    koh "Ты давно здесь учишься или только в этом году с нами?"
    show kohaku cm
    mc "Причём тут это..."
    show kohaku cross laug om oe
    koh "Ну не будь душным!"
    koh "Будь душкой."
    show kohaku happ cm oe
    mc "...мне и говорить толком нечего."
    show kohaku om ce
    koh "Всё равно, я вся во внимании!"
    show kohaku cm
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down angr_cm_oe lpoint at i21
    pause 0.2
    show monika angr_om_oe
    m "Нет, ну ты посмотри на неё!"
    show monika hdown
    m "{bt=7}\"Познакомимся поближе, ага?\"{/bt}"
    m "{bt=7}\"Я вся во внимании!\"{/bt}"
    show monika anno_om_oe
    m "Бу-э-эх."
    show monika anno_cm_oe
    n "Пх, она что, к Максу подкатывает?"
    show monika lean angr om oe n4 at h21
    m "Она серьёзно к нему подкатывает?!"
    show monika cm
    n "ТИШЕ!"
    show monika om ce
    m "Нет, я сейчас возьму и--{nw}"

    scene black with dissolve
    pause 0.25
    n "Стой на месте!"
    n "Моника, успокойся!"
    n "Что на тебя нашло?!"
    m "Мне неприятно смотреть на всё это..."
    n "Ты что, к Максу ревнуешь?"
    m "..."
    "Что с ней такое?"
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    show kohaku turned curi cm oe at i11
    "Где там Юри со своим избитым сервизом?"
    show kohaku om
    koh "Значит, ты уже состоишь в Литературном клубе?"
    show kohaku cm
    mc "Да."
    show kohaku sad om ce
    koh "Жаль..."
    show kohaku e1b
    koh "Мы могли бы предоставить тебе место."
    show kohaku cm
    mc "С чего вдруг?"
    show kohaku happ om oe lup
    koh "С виду ты парень хороший, а ещё серьёзный."
    show kohaku ldown
    koh "Мне как раз не хватает таких людей."
    show kohaku cross angr om ce
    koh "А то одна гиперактивная, другая болтливая, третья словно на иголках сидит, бедняжка..."
    show kohaku e1b
    koh "...а четвёртый совершенно не смыслит в готовке."
    show kohaku ce
    koh "Толку от него..."
    show kohaku cm
    mc "Хм..."
    "Жёстко она, конечно, о других думает."
    show kohaku neut cm oe
    "Но доля правды ощущается."
    "Хотя от Кохаку слегка веет эгоизмом..."
    show kohaku turned happ om oe lup
    koh "А всё-таки не хочешь перейти к нам?"
    show kohaku ldown
    koh "Ну сам подумай: готовка -- полезный навык, который обязательно пригодится в жизни, нежели написание стихов."
    show kohaku angr cm oe
    mc "Но вы же Клуб выпечки, а не разнонаправленной кухни."
    show kohaku cross angr om oe
    koh "А вы -- Литературный клуб, но при этом, как мне известно, никакие книжки не читаете."
    koh "И что дальше?"
    show kohaku angr cm oe
    mc "Гхм..."
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down yand_cm_oe_n3 at i21
    pause 0.2
    show monika yand_om_oe_n3
    m "Мы её схватим, привяжем к стулу, а потом я найду «толстую» книгу, являющейся всемирным произведением, и тресну ей Кохаку по голове!"
    show monika yand_cm_oe_n3
    n "Моника, остуди свой пыл!"
    n "Мы же всё записывать будем!"
    "Такими темпами сорвусь не я, а она!"
    "И когда там Юри, наконец, вернётся?!"
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    show kohaku turned happ cm oe at i11
    pause 0.2
    show kohaku om ce lup
    koh "Подумай хорошенько над мои предложением, ага?"
    show kohaku neut cm oe ldown
    mc "Ты уж меня извини, но нет."
    show kohaku happ cm oe
    mc "Я стал частью Литературного клуба по собственному желанию, и я не собираюсь из него уходить."
    show kohaku laug om ce lup rup at h11
    koh "Какой ты у нас «правильный», ха-ха-ха!"
    show kohaku happ om oe ldown rhip
    koh "А ты мне начинаешь нравиться всё больше и больше!"
    show kohaku ce
    koh "Может, всё-таки не будешь торопиться с решением?"
    show kohaku lsur cm oe ldown
    mc "Я же сказал: \"{b}НЕТ{/b}\"."
    koh "..."
    mc "..."
    show kohaku e1b
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down happ_cm_oe at i21
    pause 0.2
    show monika happ_om_oe
    m "Да, да, Макс!"
    m "Ты молодец!"
    show monika sedu_om_oe_n3
    m "{size=10}Не зря тебя полюбила~{/size}"
    show monika sedu_cm_oe_n3
    n "Моника, даже я так не переживаю!"
    n "Побереги свои силы!"
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    show kohaku turned neut cm e1b at i11
    pause 0.2
    show kohaku at t21
    show kamuko turned happ cm oe lhid rhid headband_cat at t22
    pause 0.2
    show kohaku neut cm oe
    show kamuko happ om e2a lup rup at h22
    kam "Ух ты, новенький?!"
    show kohaku angr cm oe
    show kamuko om ce ldown rdown
    kam "Приве-е-е-е--{nw}"
    show kohaku cross angr om oe
    show kamuko neut cm oe
    koh "Ты что тут делаешь?"
    show kamuko angr om oe
    kam "Передать тебе пару новостей!"
    show kohaku cm
    show kamuko lup rhid
    kam "Твой сервиз был закопан в этой кладовке -- это раз!"
    show kamuko ce lhiphid rup
    kam "А два -- остальные помогают Юри-чан найти последнюю чашку!"
    show kohaku om
    show kamuko cm oe rhid
    koh "Ну и что?"
    koh "Найти её не можете?"
    show kohaku cm
    show kamuko om
    kam "Да!"
    kam "Мы её выкладывали из набора, потому что Юри пятая чашка раньше была без надобности."
    show kohaku om
    show kamuko doub cm oe
    koh "Значит, вы же её и посеяли где-то в клубе."
    show kohaku cm
    show kamuko om rface
    kam "Но в последний раз именно ты притрагивалась к сервизу!"
    show kohaku om ce
    show kamuko ma rhid
    koh "Да как же вы меня все заколебали..."
    show kohaku at thide
    hide kohaku
    pause 0.2
    koh "{size=19}Ну где, где она, блин, может валяться, что вы её вчетвером откопать не можете?!{/size}"
    show kamuko at t11
    "Фух, передышка на пару минут..."
    show kamuko happ om ce
    kam "Хи-хи-хи-хи-хи!"
    show kamuko oe ldown rdown
    kam "Пока её нет, мы можем поговорить!"
    show kamuko cm
    mc "..."
    show kamuko nerv om oe at s11
    kam "Ой, я не представилась..."
    $ kam_name = _("Камуко")
    show kamuko happ om oe at t11
    kam "Меня зовут Каму{image=accent_low_register}{space=-15}ко!"
    show kamuko rup
    kam "Люблю игры, аниме и котиков!"
    show kamuko ce lup rdown
    kam "У меня даже дома есть ободок с ушками и наушники в таком же стиле!"
    show kamuko cm ldown
    mc "А...{w}ага..."
    show kamuko nerv om oe
    kam "Готовить у меня не очень получается..."
    show kamuko neut om oe b1d
    kam "\"Но я же ведь состою в клубе выпечки\", -- ты мог подумать."
    show kamuko happ om ce rface -b1d
    kam "\"В нашей школе нет клуба любителей аниме и игр!\" -- отвечу я."
    show kamuko oe rdown
    kam "Поэтому...{w}я тут."
    show kamuko cm
    mc "Понятно..."
    show kamuko nerv om ce
    kam "Ой, извини, что я о себе да о себе..."
    show kamuko happ om oe lup
    kam "Как тебя зовут?"
    show kamuko ldown rup
    kam "Что любишь?"
    show kamuko ldown rdown
    kam "Чем занимаешься?"
    show kamuko cm lhid rhid
    "Твою ж ты мать..."
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down neut_cm_oe at i21
    pause 0.2
    show monika neut_om_oe lpoint
    m "А это ещё кто?"
    show monika neut_cm_oe hdown
    n "Камуко -- заядлая любительница аниме, но только она больше по сериалам и фильмам, а не по манге и ранобэ."
    n "Ещё любит игры всякие."
    n "А по характеру как Сайори, только помноженная на 2."
    m "Хм..."
    n "Разве ты раньше с ней не сталкивалась?"
    show monika forward neut om oe lpoint rhip at t11
    m "В нашей школе слишком много учеников и учениц, чтобы я точно знала всех в лицо."
    show monika cm ldown
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    show kamuko turned vsur cm oe headband_cat at i11
    pause 0.2
    show kamuko om oe lup rup at h11
    kam "Всего неделю?!" with vpunch
    show kamuko curi om oe ldown rdown
    kam "А как же ты раньше учился без клубов?!"
    show kamuko neut cm oe
    mc "Меня здесь и не было."
    show kamuko happ cm oe
    mc "Я недавно сюда жить переехал."
    show kamuko om ce
    kam "А, понятно-понятно-понятно."
    show kamuko cm
    mc "..."
    show kamuko neut cm oe lhid rhid
    kam "..."
    show kamuko pout om oe
    kam "Ню-ю-ю, какой ты молчаливый..."
    show kamuko happ om oe ldown rdown
    kam "Прямо как типичный герой любого аниме про школу!"
    show kamuko ce lup
    kam "Который потом добивается успехов в жизни и обретает любовь--{nw}"
    show kamuko lsur cm oe
    mc "Не-не-не, вот с такими персонажами меня сравнивать не надо."
    show kamuko om ldown
    kam "Э-э-э?!"
    show kamuko curi om oe lhiphid rhid
    kam "Это почему?"
    show kamuko neut cm oe
    mc "Да они же все избиты различными клише!"
    show kamuko pout cm e1a
    mc "У одного мозг от стресса взрывается при виде девушек, другой творит всякую дичь по тупости."
    mc "А третьи так вообще мнят себя недогероями и несут ахинею, от которой воротит за километр."
    show kamuko oe
    kam "Хмпф..."
    show kamuko om e1a
    kam "Они не все такие!"
    show kamuko cm
    mc "Но в большинстве случаев это именно так."
    show kamuko doub mb oe ldown rdown
    kam "А может, ты им завидуешь?!"
    show kamuko happ om ce lup rup at h11
    kam "Ведь у них счастливая жизнь и счастливая любовь!"
    show kamuko cm ldown rdown
    "У всех это больная тема или что?!"
    show kamuko lsur cm oe
    mc "Да мне как-то фиолетово, что там у них творится, если честно."
    show kamuko happ om oe
    kam "У тебя просто нет второй половинки!"
    show kamuko cm
    mc "...и?"
    show kamuko om ce
    kam "Вот поэтому ты их не понимаешь и они тебе не нравятся!"
    show kamuko cm
    mc "...не понимаю их поведение?"
    show kamuko oe
    mc "Я состою в Литературном клубе, где нет ни одного участника мужского пола."
    mc "И я ни разу не вёл себя, как они."
    show kamuko om lup at h11
    kam "Кстати, может, мне тоже стоит попробовать писать стихи?"
    show kamuko ce ldown
    kam "У меня иногда мысли таким образом выстраиваются, что прямо так и хочется перенести их на бумагу!"
    show kamuko nerv om oe rface
    kam "Только нужен красивый стиль, красивая тетрадка, ручка с красивыми чернилами..."
    show kamuko cm
    "{sc=1.5}Кто-нибудь, уймите её!{/sc}"
    show kamuko neut om oe rdown
    kam "Ой, а ещё нужно будет оценивать, что и другие насочиняли, ведь да?"
    show kamuko cm
    "{sc=2}Помогите!{/sc}"
    show kamuko sad om ce at s11
    kam "У-у-у, оценщик из меня никакой!"
    show kamuko happ om ce at t11
    kam "Хотя если постараться...{nw}"
    "{sc=3}А-А-А-А-А-А-А-А!!!{/sc}{nw}"
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg school f1 old_stairwell center
    show monika lean_hear_down sad_cm_oe_n4 at i21
    pause 0.2
    show monika sad_om_oe_n4
    m "Ты посмотри, Макс там весь измучился!"
    show monika sad_cm_oe_n4
    n "Что там они вообще делают с этим сервизом?"
    show monika neut_cm_oe
    n "Я думала, на это уйдёт всего лишь пара минут."
    show monika neut_om_oe
    m "Без понятия..."
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor:
        xzoom -1
    show kamuko turned happ cm oe headband_cat lhiphid rhid at i11
    pause 0.2
    show kamuko neut cm oe
    koh "{size=16}СЮДА, ХА-ХА!{/size}"
    e "{size=16}Да ну?!{/size}"
    sor "{size=16}Пипец какой-то...{/size}"
    show kamuko happ cm oe
    mc "...нашли, что ли?"
    show kamuko om ce
    kam "Кажется, да!"
    show kamuko cm
    stop music fadeout 2.0
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg corridor:
        xzoom -1
    show kohaku turned angr cm oe at t11 zorder 2
    show kamuko turned happ cm oe headband_cat lhid rhid at t22
    show emi turned uniform_waist_jacket happ cm oe lhip rhip at t55 zorder 2
    with wiperight
    "Наконец-то..."
    "Наконец-то мы всей гурьбой провожаем Юри, которая несёт объёмную коробку в сторону центральной лестницы."
    show kohaku om
    show kamuko neut cm oe
    show emi neut cm oe
    koh "Я не поняла..."
    show kohaku cross angr om oe
    show emi curi cm oe
    koh "А ты чего не уходишь?"
    show kohaku cm
    mc "Я?"
    show kohaku om
    koh "А кто ещё с ней пришёл, а?"
    show kohaku cm
    "Неужто она так недовольно фактом моего отказа?"
    show emi neut cm oe
    mc "Ну..."
    call window_close

    call window_dialog_fast_transition("n")

    call window_open
    scene bg school f1 old_stairwell center
    show monika forward neut cm oe rphone at i11
    pause 0.2
    show monika mh
    m "Юри, ты там не упадёшь?"
    show monika happ cm oe
    y "Нет-нет, всё хорошо!"
    n "Ура, эта эпопея закончилась!"
    show monika om lpoint
    m "Ты включила диктофон?"
    show monika cm ldown
    n "Да."
    show monika om
    m "Значит, прячем телефоны в карманы вверх тормашками, чтобы микрофон лучше улавливал звуки."
    show monika cm
    call window_close

    call window_dialog_fast_transition("mc")

    call window_open
    scene bg corridor:
        xzoom -1
    show kamuko turned neut cm oe headband_cat lhid rhid at i43
    show emi turned uniform_waist_jacket neut cm oe lhip rhip at i55 zorder 2
    show kohaku turned angr cm oe at i11 zorder 3
    pause 0.2
    show kohaku om
    koh "Всё уже закончилось, ты свободен."
    show kohaku cm
    mc "Закончилось?"
    show kamuko curi cm oe
    mc "Не, ошибаешься."
    show emi curi cm oe
    mc "Думаешь, я сюда просто за компанию пришёл?"
    show kamuko neut cm oe
    show kohaku cross angr om ce
    koh "Да ты издеваешься..."
    show kohaku cm oe
    show emi neut cm oe ldown
    mc "Кстати, стыдно сегодня не было?"
    show kohaku om
    koh "Нет, с чего это должно быть?"
    show kohaku cm
    show emi happ_neko lhip
    mc "Ну, если бы ты была честной, то ответила бы по-другому на мой вопрос."
    show kamuko happ cm e2a
    show emi laug om ce -happ_neko
    e "Ух ты, Моника-чан, Нацуки-чан, привет!"
    show emi cm
    show kamuko om lup rup at h43
    kam "Нацуки?!"
    show kamuko cm ldown rdown
    show emi happ cm oe
    show kohaku cross angr om oe
    koh "Ч-что?"
    show kamuko lhid rhid
    show monika forward happ cm oe at t51 zorder 3
    show natsuki turned happ cm oe at t52 zorder 4
    show kohaku angr cm oe
    show sora turned happ cm oe at t54 zorder 3
    show fukkacumi turned neut cm oe at t44
    pause 0.2
    if persistent.add_random_menu == 9:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()
    play music dont_play_with_me fadein 3.0
    show natsuki om lhip rhip
    n "Ну здрасьте!"
    show natsuki cm
    "Так, надеюсь, они включили диктофоны на мобильниках?"
    show emi cross uniform_waist_jacket neut cm oe
    show kamuko neut cm oe
    show monika neut cm oe
    show natsuki anno cm oe
    show kohaku om
    koh "Что ты тут делаешь вместе с Моникой?"
    show natsuki om
    show kohaku cm
    n "Перейдём сразу к делу!"
    show kamuko curi cm oe
    show monika angr cm oe
    show natsuki angr om oe ldown rdown
    show kohaku m1e
    show sora anno cm oe rpock
    show emi curi cm oe
    n "Мы все знаем, что ты сегодня хотела!"
    show natsuki cm
    show kohaku m2a
    koh "Ха, я так и думала..."
    show kamuko vsur cm oe
    show monika neut cm oe
    show kohaku turned angr om oe
    show sora angr cm oe
    show emi lsur cm oe n2
    koh "Сора, ты идиот!"
    show kohaku cm
    show sora om
    sor "Что?!"
    show kamuko neut cm oe
    show sora cm
    mc "Вообще-то он всё сделал правильно."
    show kohaku cross angr om oe
    koh "Это ты мне говоришь?!"
    show kamuko lsur cm oe
    show natsuki om lhip rhip
    show kohaku cm
    show sora anno cm oe
    show emi angr md oe
    show fukkacumi sad md e2a
    n "Кохаку, ты нас всех достала своим желанием своровать НАШИ кексы!"
    show kamuko vsur cm oe
    show natsuki anno om ce
    show kohaku om
    n "Ладно это было ещё во времена, когда я была частью Клуба выпечки, но сейчас..."
    show kamuko om ldown rdown at h43
    show natsuki cm
    kam "Кья?!"
    show kamuko cm
    show natsuki neut cm oe b1d
    show emi om
    e "Вы когда кекс украсть успели?"
    show emi md
    "Судя по всему, она его ещё и спрятала."
    show natsuki angr om oe -b1d
    n "Сегодня!"
    show emi s_scream at h55
    e "Чё?!"
    show natsuki cm
    show monika angr cm oe
    show kohaku ce
    koh "Кх-х-х-х-х..."
    show natsuki om
    n "Может, пора прекратить, а?"
    show natsuki cm
    show emi -s_scream
    koh "Всё через задницу..."
    show kohaku cross angr om oe
    koh "Хорошо, да, я признаюсь, что хотела взять ваш кекс."
    koh "Довольны?"
    show natsuki om
    show kohaku cm
    n "Нет!"
    show natsuki cm
    koh "..."
    show kamuko lsur cm oe lhid rhid
    show sora angr cm oe
    "..."
    show monika neut cm oe
    show natsuki neut cm oe b1d ldown rdown
    show kohaku turned angr cm oe
    show sora om lface
    show fukkacumi oe
    sor "Ну чёрт тебя дери, Кохаку!"
    sor "Так тяжело бросить эту затею?"
    show kamuko neut cm oe
    show fukkacumi neut cm oe ldown rdown
    show kohaku cross angr om oe
    show sora cm ldown
    show emi neut cm oe n1
    koh "Ты понимаешь, как сильно наш клуб выйдет в плюс после этого?"
    koh "Я добьюсь новых высот, мы получим новых людей!"
    koh "Новые рецепты -- новые возможности!"
    show emi curi cm oe
    koh "Мы станем серьёзным конкурентом для остальных клубов!"
    show monika curi om oe lpoint
    show kohaku cm
    m "Это с каких пор клубы стали конкурентами друг для друга?"
    show monika angr cm oe ldown
    show kohaku m2a
    show emi neut cm oe
    koh "Ха-ха-ха, и это мне говорит президент Литературного клуба?"
    show monika om
    show kohaku cm
    m "Да, именно Я, потому что Я участвую в совещаниях школьного совета, где ты нечасто появляешься!"
    show monika anno cm oe
    show kohaku om
    koh "И какой толк от них, кроме организации праздников?"
    koh "Обсуждение финансирования, которое можно обсудить с Рэйко лично?"
    show monika om ce
    show kohaku cm
    m "Помощь начинающим клубам, а также тем, у которых есть проблемы..."
    show monika cm oe
    show kohaku m2a
    koh "Ага, так я и поверила."
    show kohaku om
    koh "Помощь клубам?"
    show kamuko curi cm oe
    show monika neut cm oe
    show natsuki brow
    show kohaku m2a
    show sora neut cm oe
    koh "Серьёзно?"
    show emi angr md oe
    koh "И как тебе «помогли» с Литературным клубом на первых порах, м-м?"
    show monika dist cm oe
    show kohaku m1e
    m "..."
    show kamuko neut cm oe
    show kohaku m2a
    koh "Именно!"
    show kamuko lsur cm oe
    show natsuki b1d
    show kohaku om
    show emi neut md oe
    koh "За всё моё время у руля Клуба выпечки ты смогла набрать лишь 3-ёх человек на постоянной основе, и то ближе к концу учебного года."
    show monika ce
    show kohaku ce
    koh "Когда у нас в школе обучается около 600-а человек!"
    show kamuko neut cm oe
    show monika neut cm oe
    show natsuki om lhip rhip
    show kohaku cm oe
    show emi cm
    n "Да ты чё, смеёшься, что ли?"
    show monika happ cm oe b1b
    show natsuki angr om oe -b1d
    show emi sedu cm oe
    show fukkacumi ma
    n "Моника своими руками с нуля зародила и поставила на ноги Литературный клуб."
    show monika neut cm oe -b1b
    show emi neut cm oe
    show fukkacumi md
    n "А ты просто захватила власть!"
    n "И потеряла при этом половину состава, позорище!"
    show natsuki anno om ce
    show emi anno md ee
    n "Лидер, блин..."
    show natsuki cm
    show kohaku om
    show sora anno cm oe
    show emi angr md oe
    koh "А мне такие люди и не нужны были."
    show natsuki neut cm oe b1d
    show kohaku cm
    show sora om lface
    sor "Оправдания..."
    show kohaku m2a
    show sora angr cm oe ldown
    koh "О, знаток голос проявил!"
    show natsuki ldown rdown
    show kohaku m1e
    show sora om
    sor "Да, я!"
    sor "Чем дольше я нахожусь в этом клубе под твоей властью, тем больше убеждаюсь, что из меня мог бы выйти очень хороший лидер!"
    show kohaku m2a
    show sora cm
    koh "Ха-ха-ха, ты?!"
    show kohaku m1e
    show sora om
    sor "Именно я!"
    show kohaku ce
    show sora cm
    koh "Да ты даже кекс нормальный стащить не смог!"
    show kohaku m2a oe
    show sora anno cm oe
    koh "О чём тут вообще говорить?"
    show kohaku m1e
    show sora om
    sor "А с чего это я должен уметь воровать?"
    show kamuko anno cm oe lhiphid
    show kohaku cm
    show sora lface
    sor "Каким образом это пересекается с лидерством, а?"
    show sora ldown
    sor "С таким же успехом можно упрекнуть тебя, что ты в термоядерной физике не разбираешься."
    show sora angr om oe
    sor "Да и вообще, {b}чужими{/b} руками хотела стащить кекс!"
    sor "Не своими!"
    show monika anno cm oe
    show kohaku om
    show sora cm
    koh "И очень теперь об этом жалею, ага."
    show kohaku ce
    show sora anno cm oe
    show emi n2
    koh "За что мне такой бездарный участник..."
    show sora om lface
    show fukkacumi ce
    sor "За что мне такой эгоистичный и мерзкий лидер?"
    show kohaku cm oe
    show sora ce ldown
    sor "Затравили небось в младших классах за плохую готовку, теперь всем палки в колёса вставляет..."
    show kohaku om
    show sora angr cm oe
    show emi lsur cm oe
    show fukkacumi oe
    koh "Заткнись нафиг, образцовый ученик!"
    show kohaku cm
    show sora om
    sor "Да, я прекрасно учусь, завидуешь?"
    show kohaku m2a
    show sora cm
    koh "Ха-ха-ха, да ты даже дресс-код не соблюдаешь!"
    show kohaku om
    koh "Как тебе вообще разрешают носить чёрную толстовку поверх жилетки и рубашки?"
    show kohaku ce
    koh "И как ты в ней не свариваешься?"
    show kohaku cm oe
    show sora om
    sor "В это время года в коридорах всегда прохладно!"
    show kohaku m1e
    sor "А сам я не обладаю нужным количеством жира для сохранения тепла, как ты!"
    show kohaku m2a
    show sora cm
    koh "Дистрофик!"
    show kohaku om
    show sora anno om oe
    sor "Зато могу спокойно жрать и не толстеть, в отличие от некоторых."
    show kohaku ce
    show sora cm
    koh "ГРХ!"
    show sora om lup
    sor "И кстати, раз уж мы заговорили об «образцовости»..."
    show kohaku cm oe
    show sora angr om oe ldown
    show emi s_scream at h55
    show fukkacumi neut cm oe
    sor "Где пиджак, «лидерша»?"
    show kohaku om
    show sora cm
    show emi at thide
    hide emi
    koh "В нём жарко, потому что у меня с телом всё нормально!"
    show kohaku cm
    show sora om
    sor "Как же тебе тогда разрешают не носить часть дресс-кода?"
    show kohaku om
    show sora anno cm oe
    koh "А вот так!"
    show kohaku cm
    show sora om
    sor "Ага, отмалчиваемся?"
    show kamuko neut cm oe lhid
    show monika neut cm oe
    show natsuki -b1d
    show kohaku turned curi cm oe
    show sora neut cm oe
    show emi turned neut cm oe lhip rhip at t55 zorder 2
    mc "Мне вот одно интересно, Кохаку: конкуренция с другими клубами тебе нахрена?"
    show kohaku om
    koh "Придурок?"
    koh "Я как людей должна набирать, когда другие к себе заманивают?"
    show kamuko happ cm oe
    show monika happ cm oe
    show kohaku angr cm oe
    mc "Клубы первоначально создаются с целью, чтобы найти, блин, единомышленников и заниматься с ними тем, чем ты хочешь!"
    show kamuko neut cm oe
    show monika b1e
    show natsuki b1d
    show emi anno md ee
    mc "А ты мало того, что тянешь свой клуб на дно из-за своих кривых устоев, так ещё и другим жить мешаешь!"
    show kamuko lsur cm oe
    show monika om rhip
    show sora lsur cm oe
    show emi lsur cm oe n2
    show fukkacumi e2a
    m "И ещё внаглую пытаешься переманить к себе людей!"
    show monika cm
    show kohaku cross angr om oe
    koh "Как ты?!..."
    show monika om angr om oe -b1e rdown
    m "Макс вступил к нам по своему желанию!"
    m "И мы тебе его ни за что не отдадим!"
    show kamuko angr cm oe
    show monika cm
    show kohaku ce
    show sora angr cm oe
    show emi neut cm oe -n2
    koh "Ну и пожалуйста!"
    koh "Ну и не нужно!"
    show natsuki anno cm oe -b1d
    show kohaku m2a oe
    koh "...забирать у вас единственного парня, ха-ха-ха."
    show monika om
    show kohaku m1e
    show fukkacumi oe
    m "Может, и единственный, зато хороший и заботливый!"
    show kamuko curi cm oe
    show monika vang cm oe
    show natsuki curi cm oe
    show kohaku m2a
    koh "Пф-пф-пф, ты в него втюрилась, что ли?"
    show kohaku ce
    show emi curi cm oe
    koh "Хотя признаться, поначалу он мне тоже понравился."
    show kohaku e1b
    koh "Интересно было бы подружиться с ним, не правда ли--{nw}"
    play music_none_loop music_stop
    stop music
    show kamuko vsur cm oe
    show monika om
    show natsuki shoc om oe at h52
    show kohaku neut m3a oe
    show sora lsur cm oe
    show emi s_scream at h55
    show fukkacumi bcm boe
    m "ЕСЛИ ТЫ ТАК ХОЧЕШЬ КОГО-ТО ТРАХНУТЬ, ТО ТРАХНИ СВОЮ ГОЛОВУ ОБ СТЕНУ, МОЖЕТ, ТАК МОЗГИ НА МЕСТО ВСТАНУТ!!!" with vpunch
    show monika cm
    show sora rdown
    "........."
    show natsuki cm
    show kohaku turned angr om oe
    show sora angr cm oe
    koh "АХ ТЫ--{nw}"
    show kohaku cm
    show emi pani cm oe n2 -s_scream
    show fukkacumi at thide
    hide fukkacumi
    mc "ТАК, ВСЁ, СТО-О-ОП!"
    show natsuki vang cm oe
    show sora om at t11 zorder 4
    sor "Кохаку, угомонись!"
    show kohaku at thide
    hide kohaku
    show sora cm at thide
    hide sora
    pause 0.2
    koh "ПФМ!"
    show monika om
    m "Эй, я только начала--{nw}"
    call window_close

    hide monika with dissolve
    show monika forward vang om oe at e21 zorder 4
    pause 1.0
    show mc_hand_closing_mouth_monika zorder 5
    show monika shoc cm oe
    with dissolve

    call window_open
    m "--мф-фмф-фм-м-м!!!"
    mc "Предлагаю на этом закончить наш бардак!"
    sor "{size=19}Солидарен!{/size}"
    koh "{size=19}КХГХ!{/size}"
    show monika e4c
    m "М-м-м-м-м!!!"
    show natsuki om lhip rhip at t11
    n "Мы же ничего не добились!"
    n "Какой \"закончить\"?!"
    show monika oe
    show natsuki cm
    mc "Нацуки, блин, мы сегодня уже ничего не добьёмся!"
    show natsuki om ce
    n "Аргх, ну и зачем мы тогда вообще начинали?!"
    show natsuki cm
    mc "Всё, ребят, извините, мы уходим."
    e "Э-э-э..."
    show kamuko om at s43
    kam "Мя-я..."
    show kamuko cm
    show monika e4c
    m "Макпф, отпуфти м-мн-н!"
    call window_close

    call plot_transition

    call window_open
    scene bg school f2 old_stairwell center
    show natsuki turned neut cm oe at t21
    show monika forward doub cm ce at t22
    with wipeleft_scene
    mc "Так, здесь нас точно не услышат..."
    show monika om
    m "Пфу, Макс, я чуть не задохнулась!"
    show monika cm
    mc "Ну извини!"
    show natsuki e1b
    show monika angr cm oe
    mc "Ты СЛИШКОМ резко отреагировала на провокацию Кохаку."
    show monika om
    m "Её слова уже ни в какие рамки не лезут!"
    show natsuki oe
    show monika cm
    mc "Меня сейчас другое волнует."
    show natsuki pout cm oe
    show monika neut cm oe
    mc "Мы будем показывать...{w}такую запись учителям?"
    show natsuki om lhip rhip
    show monika dist cm oe n2
    n "Ага, Монике сразу прилетит по шее."
    show natsuki cm ldown rdown
    mc "Ну что я сделать могу?"
    mc "Других доказательств у нас нет и, вероятно, не будет."
    show natsuki neut cm oe
    show monika neut cm oe n1
    mc "И если оценивать всю ситуацию, то здесь провокации Кохаку налицо."
    mc "Не Моника же первая начала, в конце концов."
    show natsuki e1c
    n "М-м-м..."
    show natsuki oe
    show monika om lpoint
    m "Если мы не покажем записи сейчас..."
    show monika ce ldown
    m "...то я уверена, что дальше будет хуже."
    show natsuki curi cm oe lhip rhip
    show monika cm oe
    mc "Тогда прямо сейчас это сделаем?"
    show monika mh
    m "Тянуть не имеет смысла."
    show natsuki om
    show monika cm
    n "У нас так праздник накроется вместе с кексами, время не резиновое."
    show natsuki neut cm oe ldown rdown
    show monika mh ce
    m "Давайте так."
    show monika oe lpoint
    m "Я пойду и предоставлю запись учителям, а вы пока идите в клуб и помогите Сайори с Юри, если понадобится."
    show monika cm ldown
    mc "Одна предоставишь?"
    show monika happ cm oe
    mc "Может, я хотя бы тебе компанию составлю?"
    show monika om
    m "Нет, Макс, спасибо."
    show monika lpoint
    m "Не думаю, что это займёт много времени."
    show monika neut om ce ldown
    m "Надеюсь, такой записи будет более чем достаточно..."
    show monika cm oe
    mc "Качество там хорошее?"
    show monika mh
    m "Микрофон ничем не заслонялся, всё должно быть нормально."
    show monika happ cm oe
    mc "Ну раз так, то ждём тебя в клубе всем...{w}клубом."
    show natsuki happ cm oe
    show monika om ce
    m "Чтобы к моему приходу все были готовы, ха-ха!"
    show natsuki om
    show monika cm ce
    n "Поняли, мы пошли."
    show natsuki cm
    show monika om oe
    m "Да, удачи!"
    show monika cm
    mc "Угу."
    show natsuki ce

    scene black with wipeleft_scene
    mc "Кстати, я так понимаю, что весь состав Клуба выпечки, за исключением Соры, совершенно не изменился?"
    n "Ага."
    n "Кохаку ничерта не умеет управлять."
    n "Всё строит из себя жёсткого лидера, но по факту её никто не слушает."
    n "Подчиняются ей лишь из-за того, что выбора особо нет."
    mc "Хм..."
    "Попахивает преувеличением, но только немного."
    mc "Моника, я так понимаю, тоже не раз встречалась со всем клубом?"
    n "Не знаю, но с Фуккой точно."
    mc "А почему с ней?"
    n "Потому что она раньше была в Музыкальном клубе, который базировался в музыкальном классе."
    n "Сам клуб, к слову, уже давно не существует."
    mc "Развалился?"
    n "Да, там какие-то свои мутки и проблемы были."
    n "Фукка даже после всего этого продолжала ходить в музыкальный класс."
    n "Правда, уже без особого энтузиазма, по словам Моники..."
    mc "Она прям музыкантка?"
    n "Что-то умеет на гитаре, ага."
    n "Так вот, Моника ещё во времена членства в Дискуссионном клубе захаживала в музыкальный класс поигрывать на рояле."
    n "Вот там-то она с Фуккой и познакомилась."
    mc "Ясно."
    mc "Но сейчас Фуккацуми в Клубе выпечки..."
    mc "Как так вышло?"
    n "Всё, что могу сказать -- так это то, что Кохаку ещё до президентской роли хотела завлечь её в клуб."
    n "Причём из заботливых намерений, и я сейчас серьёзно."
    mc "Вот как?"
    n "Сама не понимаю."
    n "Вроде бы такая вся из себя эгоистка, а тут это."
    n "Причём Кохаку и Фукка учатся в том же классе, где и Юри, но ситуацию это не меняет."
    mc "Мда, странно..."
    "Это сильно идёт вразрез с её нынешним поведением."
    "Блин, какие ж вы все запутанные-перепутанные..."
    "И никак вас не распутаешь."
    "Хотя надо ли?..."

    scene bg school old_corridor door with wipeleft_scene
    "Фу, такие засветы в окнах, что приходится только в пол смотреть, чтобы не ослепнуть."
    mc "Ребзя!"
    mc "Мы пришли!"
    "..."
    n "Что они там возятся?"
    s "{size=16}Хм-м-м...{/size}"
    s "{size=19}Вы кто такие?{/size}"
    n "Это мы!"
    s "{size=19}Мы вас не звали.{/size}"
    mc "Чё?"
    s "{size=19}Идите--{/size}{nw}"
    n "ДА МЫ ЭТО, МЫ!" with vpunch
    s "{size=19}Нацуки?{/size}"
    n "Сайори, открывай, конфликт закончился!"
    s "{size=19}А-а-а!{/size}"
    call window_close

    scene black with wipeleft_scene
    pause 1.0
    play sound closet_open
    pause 0.5

    call window_open
    scene bg school literature_club board day
    show yuri turned neut cm e1d at t41
    show sayori turned happ cm oe at t43
    show natsuki turned curi cm oe at t44 zorder 2
    with wipeleft_scene
    mc "Эм..."
    show sayori nerv cm oe
    mc "Здесь ничего не изменилось."
    mc "И где контейнеры?"
    show yuri happ cm oe
    show sayori tap nerv om e2 at s43
    s "Э-хе-хе..."
    show yuri om
    show sayori turned happ cm oe at t43
    show natsuki neut cm oe
    y "Мы приняли решение, что понадобится сдвинуть всего 2-3 парты."
    show yuri e1b lup
    y "Ведь нас всего 5 человек."
    show yuri oe ldown
    y "А контейнеры мы поставили на стулья, чтобы их не было видно из коридора."
    show yuri cm
    "И это всё, что они сделали?..."
    show yuri neut cm e1d
    mc "Сервиз, я так понимаю, вы пока в кладовку убрали?"
    show yuri om
    y "Да, чай будем заваривать, когда соберёмся все вместе."
    show yuri cm
    show sayori e1b
    "..."
    show yuri anno cm oe
    show sayori oe
    show natsuki dist cm oe
    mc "Эх, опять сидеть и ждать..."
    show yuri neut cm e1d
    show sayori om ce lup rup at h43
    show natsuki neut cm oe
    s "Мы можем снова сыграть в слова!"
    show sayori neut cm oe
    mc "Не, извини Сайори, у меня голова мутная после всего этого маразма."
    show yuri lsur om oe lup rup
    show sayori ldown rdown
    show natsuki anno cm oe
    y "О-о, у вас там всё хорошо прошло?"
    show yuri neut cm e1d
    show natsuki om lhip rhip
    n "Догадайся с трёх раз."
    show yuri ldown rdown
    show natsuki neut cm oe ldown rdown
    mc "Ничего мы не смогли добиться, однако записи на руках теперь имеются."
    mc "Моника прямо сейчас их должна передать учителям."
    mc "Как только это дело решится, сразу к нам вернётся."
    show yuri dist om oe
    y "Понятно..."
    show yuri neut cm e1d
    show sayori curi cm oe
    mc "Кстати, целостность набора хотя бы проверили?"
    y "..."
    call window_close

    pause 1.0
    show yuri anno cm oe
    pause 2.0
    show yuri curi cm e2b
    pause 1.0
    show sayori neut cm oe
    hide yuri with easeoutleft
    show natsuki pani om oe at h44

    call window_open
    n "А, манга!"
    show sayori nerv cm oe
    show natsuki pout om oe lhip rhip
    n "Вы там ничего не наворотили?"
    show natsuki cm
    s "..."
    show natsuki anno om oe
    n "Сайори, скажи мне честно."
    show sayori happ om ce
    show natsuki cm
    s "Не-е-ет~"
    show sayori cm
    show natsuki pout om oe
    n "Твой голос не вселяет уверенности."
    show natsuki cm
    call window_close

    pause 0.2
    show natsuki e1b ldown rdown
    pause 0.2
    hide natsuki with easeoutleft
    show sayori at t11
    pause 2.0
    show sayori laug cm ce

    call window_open
    n "{size=19}А-а-а, ну конечно!{/size}"
    y "{size=19}Нацуки, отойди!{/size}"
    y "{size=19}Дай набор проверю!{/size}"
    n "{size=19}Это можно и в классе сделать, а не в кладовке!{/size}"
    y "{size=19}Снова твоя упрямость...{/size}"
    n "{size=19}Бла-бла-бла!{/size}"
    show sayori happ cm oe
    mc "Ох, блин, что-то я совсем размяк..."
    s "М-м?"
    show sayori neut cm oe
    mc "Да не знаю, состояние такое...{w}противное."
    show sayori pout cm oe
    mc "Хочется свалиться и вырубиться."
    show sayori om
    s "Это потому что ты вчера поздно лёг, правильно?"
    show sayori ce
    s "А потом утром не мог встать!"
    show sayori cm
    mc "Не сказал бы."
    show sayori neut cm oe
    mc "Уснул как обычно."
    show sayori om
    s "Тогда..."
    show sayori curi om oe
    s "...может, ты нанервничался за неделю?"
    show sayori cm
    mc "Не, как-то глупо."
    show sayori neut om oe
    s "Ну или устал за воскресенье."
    show sayori cm
    mc "...м-м-м..."
    "Ну да, были вчера свои приколы, но..."
    "Подождите-ка..."
    "Мне же что-то невнятное снилось..."
    "Нарисованная голова Сайори."
    "Возможно, я ночью периодически просыпался и засыпал, а сейчас этого не помню?"
    mc "Ну..."
    show sayori vsur cm oe
    mc "Не знаю, ворочился ночью, скорее всего..."
    show sayori om lup rup at h11
    s "Плохо!"
    show sayori e1a ldown rdown
    s "Тебе срочно требуется отдых!"
    play music t6
    show sayori happ om oe
    s "Садись на стул, я тебе сделаю массаж шеи и плеч."
    show sayori cm
    "ПФ-Ф-Ф-Ф-Ф!!!" with vpunch
    mc "Массаж?!"
    show sayori om
    s "Да, а что такого?"
    show sayori cm
    mc "...как минимум это неожиданно."
    show sayori sad om oe
    s "Ты же мой близкий друг!"
    s "Я должна о тебе заботиться!"
    show sayori cm
    mc "Ох, Сайори..."
    show sayori neut cm oe
    mc "Про себя ж не забывай."
    show sayori flus cm oe
    mc "Вон, смотри, какой у тебя колтун на голове."
    show sayori om at h11
    s "Ой!"
    show sayori cm
    mc "Дай-ка..."
    call window_close

    hide sayori
    show sayori turned flus cm oe at e11
    with dissolve
    pause 2.0

    call window_open
    mc "М-м-м, нет, тут без расчёски не обойтись..."
    show sayori curi cm oe
    mc "Ты вообще сегодня себя расчёсывала?"
    show sayori om e2b
    s "Э-э-э..."
    show sayori nerv cm oe
    mc "У тебя и бант ещё покосился..."
    show sayori mb
    s "...хе-хе..."
    show sayori cm
    mc "И ленточка на шее слегка распустилась..."
    show sayori mb
    s "...хе..."
    show sayori cm
    "Возможно, она так обрадовалась нашему празднику, что про всё остальное нафиг забыла."
    mc "Эх, Сайори..."

    if cg_a1_d8_s.unlocked == False:
        $ cg_a1_d8_s.unlock()
    scene s_cg1_base with dissolve_cg
    mc "Тебе надо лучше за собой смотреть, я же не всегда буду рядом."
    s "Я знаю..."
    "Снова твоя невнимательность в совокупности с торопливостью..."
    "И это ещё хорошо, что ты не попалась каким-нибудь мразям или мудакам."
    "На самом деле, меня это пугает ещё больше, чем просто какие-то...{w}«шоковые» ситуации."
    "Сайори легко открывается людям, чем они могут нагло воспользоваться."
    "Поэтому перво-наперво ей надо научиться регулировать свои границы."
    "Не принимать всё, скажем так, близко к сердцу."
    "И как же тебя этому научить?..."
    s "Хах, знаешь, это так забавно выглядит..."
    mc "Что именно?"
    s "Забота с твоей стороны."
    s "Обычно я проявляю её по отношению к другим, даже не задумываясь."
    s "А тут ты..."
    mc "А как же клуб и родители?"
    s "В основном только Моника, но...{w}это ощущается проще, она же подруга."
    s "А родители...{w}тоже нечто другое, более естественное..."
    s "Поэтому забота с твоей стороны...{w}приятная..."
    s "Сразу хочется расслабиться."
    mc "Хм..."
    show s_cg1_exp1 at cgfade
    s "Впрочем, всё в порядке!"
    s "Не бери особо в голову."
    mc "Хорошо..."
    "Как тут не брать..."
    mc "Так, лента готова."
    mc "Эм-м..."
    s "М-м-м?"
    mc "Тебе не кажется, что этот пиджак тебе маловат?"
    hide s_cg1_exp1
    s "О, правда?..."
    mc "Будто он расчитан максимум на ученика средней школы."
    s "Может, так и есть..."
    s "Я давно его не меняла и не застёгивала..."
    mc "Тогда можно это проверить?"
    show s_cg1_exp1 at cgfade
    s "Давай."
    show s_cg1_exp2 at cgfade
    hide s_cg1_exp1
    mc "..."
    mc "Как туго лезет..."
    s "Ум-м-м..."
    mc "Слушай, нет, я так пуговицу оторву."
    hide s_cg1_exp2
    s "Хочешь сказать, что..."
    mc "Что?"
    show s_cg1_exp1 at cgfade
    s "...моя грудь выросла!"
    mc "Было бы странно, если бы это не произошло."
    "Надеюсь, Нацуки это не услышала..."
    mc "А вот пиджак уже давно менять надо!"
    hide s_cg1_exp1
    s "Ню-ю-ю, последний год остался!"
    s "Уже поздно..."
    mc "Эх..."

    scene bg school literature_club board day
    show sayori turned nerv om ce at s11
    with dissolve_cg
    s "Фух, мне уже получше!"
    show sayori cm
    "Не знаю, как она это ощутила, если я только всякие мелкие детали поправил..."
    mc "Рад слышать."
    n "{size=19}Так, давай эту стопку сюда...{/size}"
    y "{size=19}Бе-е-ех...{/size}"
    "Ладно, они там мирно возятся, повезло..."
    show sayori happ cm oe at t11
    mc "Ой, ладно, надо уже присесть."
    show sayori oe
    mc "Всё время на ногах был."
    show sayori om
    s "Садись-садись, подошла моя очередь заботы!"
    show sayori sedu cm oe
    mc "Только не перестарайся..."
    show sayori om
    s "Всё будет хорошо, можешь быть уверен."
    show sayori cm
    "Я ни разу не получал массаж от Сайори."
    "Да и за всю свою жизнь, в принципе."

    scene black with dissolve
    pause 0.25
    mc "Так."
    s "Теперь сними пиджак, расстегни сверху рубашку и приспусти галстук."
    mc "По-моему, лучше это было сделать стоя, но да ладно."
    "..."
    s "Так, повесим сюда..."
    mc "М-м-м..."
    mc "Так пойдёт?"
    s "Угусь~"
    s "А теперь расслабь плечи и голову."
    mc "Да-да..."
    mc "Приступай."
    "..."
    "......"
    "Пока никакой боли, уже хорошо."
    "..."
    "Слушайте, а у неё получается довольно-таки неплохо..."
    "Очень приятно..."
    "..."
    "Мне очень нравится плавность и мягкость её пальцев, между прочим."
    mc "Сайори, где ты так виртуозно научилась?"
    s "Моя мама когда-то работала массажистом."
    s "Она меня научила простым приёмам."
    s "А практиковалась я на папе."
    mc "Да, чувствуется уверенность в этом деле."
    s "А ты переживал!"
    mc "Ха..."
    "..."
    "О-о-о..."
    "О-о-о-о-о..."
    "Прямо будто весь задеревенел, а сейчас размяк под руками Сайори..."
    mc "Фу-у-у..."
    s "Если бы я знала, что у тебя всё настолько неразмятое, то я бы раньше сделала тебе массаж."
    mc "Если б я сам знал..."
    "Чёрт, ещё немного и грохнусь на стол от расслабленности."
    mc "О, да-да-да, у основания плеч, здесь..."
    s "Ага!"
    "А-а-а-а-а..."
    "Даже как-то жалко, что моё тело ни разу не получало такие важные процедуры."
    "Это всё равно, что не ухаживать за техникой."
    "Если не пользоваться ей должным (нормальным) образом, то она быстро изнашивается, когда могла бы проработать намного дольше."
    "Эх, тело..."
    "Что-то мне кажется, что я помру где-то лет в 50."
    "...по-моему, у меня уже была такая мысль."
    "В общем, то перегруз нервной системы из-за эмоций и проблем, то перегруз сердца и всего остального из-за этого, то недосыпы из-за учёбы, то ещё что-то..."
    "Мда..."
    "Сразу ощущается слабость в руках и ногах."
    "Образуется какая-то беспомощность..."
    "А ещё стыд за ненадлежайший уход за телом."
    mc "Слушай, Сайори, в последнее время я не был таким расслабленным..."
    s "Конечно, потому что тебе нужно снимать напряжение!"
    mc "Было б чем..."
    "Я сейчас настолько размягчился, что в сидячем положении меня удерживают только её руки."
    "Поэтому если она сейчас меня отпустит, то--{nw}"
    stop music
    play music_none_loop music_stop
    m "{cps=30}Ребята, я вернулась!{/cps}{nw}" with vpunch
    play sound hit_wood
    show white:
        alpha 1
        ease 0.25 alpha 0
    pause 0.25
    mc "!!!" with vpunch
    s "А-а-а, Макс, ты в порядке?!"
    mc "А ты как думаешь?"
    m "Ох, извините..."
    "Где мой пиджак?..."
    n "{size=19}Что?{/size}"
    n "{size=19}Где?{/size}"
    n "Когда?"
    y "У-у?"

    scene bg school literature_club board day
    show yuri turned neut cm e1d at i41
    show natsuki turned neut cm oe at i42 zorder 2
    show sayori turned nerv cm oe at s43
    show monika forward nerv cm ce at i44 zorder 2
    with dissolve
    pause 0.25
    mc "Я думаю, это уже неважно..."
    show natsuki om oe lhip rhip
    show sayori neut cm oe at t43
    show monika neut cm oe
    n "Так."
    show natsuki curi om oe
    n "Моника, как там всё прошло?"
    show natsuki cm
    show monika dist om oe
    m "Ну..."
    show natsuki neut cm oe
    show monika neut mh oe lpoint
    m "Запись прослушали."
    show monika cm ldown
    mc "...и дальше?"
    show monika mh
    m "Сказали, что эту ситацию должна рассмотреть глава школьного совета."
    m "И только после этого уже будут принимать меры."
    show monika dist mh oe
    m "Правда, ещё сказали, что она пока занята, поэтому неизвестно, когда дело сдвинется..."
    show natsuki anno om ce ldown rdown
    show monika neut cm oe
    n "Ой, начинается..."
    show natsuki neut cm oe
    show monika mh lpoint
    m "Предварительно учителями была зафиксирована пара нарушений школьных правил со стороны Кохаку."
    show monika ldown
    m "И главное из них -- вмешательство в нашу клубную деятельность путём воровства нашего кекса."
    show monika curi om e1c
    m "Нет, оно, конечно, не так звучало..."
    show monika neut om ce
    m "Просто уже не помню, как это назвали «официальным» языком..."
    show monika cm oe
    mc "Значит, будем надеяться, что это хоть как-то поумерит её пыл."
    show yuri curi cm oe
    show natsuki curi om oe lhip rhip
    show sayori curi cm oe
    show monika e2a n2
    n "Тебе самой-то не прилетело?"
    show natsuki cm
    show monika nerv mb oe
    m "Чуть-чуть..."
    show natsuki ldown rdown
    show sayori neut cm oe
    show monika e1a
    m "Всё в порядке."
    show yuri om
    show monika cm
    y "Что-то ещё произошло?"
    show yuri cm
    show monika mb ce
    m "Н-нет, просто..."
    show yuri neut cm e1d
    show natsuki neut cm oe
    show sayori happ cm oe
    show monika neut cm oe n1
    mc "...просто хватит уже тянуть время -- давайте приступать к нашему чаепитию!"
    show yuri laug cm ce
    show natsuki happ cm oe
    show sayori om ce lup rup at h43
    show monika happ cm oe
    s "Да, ура!"
    show sayori cm
    show monika om ce
    m "Ха-ха..."
    show sayori oe ldown rdown
    show monika oe
    m "Ладно."
    show yuri happ cm oe
    show monika lpoint rhip
    m "Итак, друзья!"
    show yuri ce
    show natsuki ce
    show sayori ce
    show monika ce ldown rdown
    m "Пора начинать празднование нашего воссоединения!"
    show monika cm

    scene white
    show bg_literature_club_tea_party_mc zorder 0
    show mc turned neut cm e1e at t55 zorder 2:
        xoffset -30 ypos 505 zoom 0.64
    show bg_literature_club_tea_party_y zorder 0
    show bg_literature_club_tea_party_s zorder 3
    show sayori turned happ cm ce at t54 zorder 4:
        xoffset -30 ypos 665 zoom 0.64
    show bg_literature_club_tea_party_n zorder 3
    show bg_literature_club_tea_party_m zorder 5
    show school literature_club tea party zorder 7
    with dissolve_scene_full
    play music literature_club_tea_party fadein 3.0
    "После размятия стал чувствовать себя посвежее."
    "Спасибо Сайори за массаж."
    show mc oe
    show sayori om
    s "Кексы-кексы-кексы-кексы-кексы~"
    show mc om
    show sayori neut cm oe
    mc "Потерпи ещё немножко."
    show mc cm
    show sayori pout om ce
    s "У-у-у-у-у!"
    show sayori cm
    "Нацуки уже открывает контейнеры, ставя их на приставленные столы, а Юри принялась за заваривание чая."
    "Моника в свою очередь на подхвате у обеих."
    show mc om e1e
    show sayori neut cm oe
    mc "Всё-таки как-то это немного странно..."
    show mc cm
    show sayori om
    s "Что?"
    show mc neut om oe
    show sayori cm
    mc "Тогда в пятницу из-за недопониманий наши связи чуть не разорвались окончательно."
    show mc curi om oe
    mc "Однако если бы не они, то «праздника» сегодня бы не было."
    show mc cm
    show sayori happ om oe
    s "Не это важно!"
    show mc neut cm oe
    show sayori rup
    s "Важно то, что мы прошли это испытание, ведь да?"
    show sayori ce rdown
    s "И пора есть кексы!"
    show mc om
    show sayori cm
    mc "Возможно, ты права..."
    show mc cm
    show sayori e1b
    "Я бы сказал, что Сайори снова в своём духе беззаботности, но...{w}она реально права."
    show sayori oe
    show natsuki turned happ cm oe at t52 zorder 4:
        xoffset 15 ypos 650 zoom 0.64
    pause 0.2
    show natsuki om lhip rhip
    n "Так, вот."
    show mc happ cm oe
    n "Все равны как на подбор."
    n "С ними..."
    show mc neut cm oe
    show sayori neut cm oe
    show natsuki curi om oe ldown rdown
    n "Юри, где чай?"
    show natsuki cm
    y "Сейчас-сейчас..."
    show natsuki neut cm oe
    m "Давай возьму."
    y "Угу."
    m "Так..."
    show mc happ cm oe
    show sayori happ cm oe
    show natsuki happ cm oe
    show monika forward happ cm oe rteaparty at t53 zorder 6:
        xoffset 0 ypos 500 zoom 0.64
    pause 0.2
    show monika om ce lpoint
    m "Первая партия прибыла!"
    show sayori om ce
    show monika cm ldown
    s "Ох, какой аромат!"
    show sayori cm
    "Зелёный чай с жасмином?"
    "Чаепитие обещает быть вкусным."
    show mc neut cm oe
    "Но как бы нам тут не пропитать весь класс этими запахами..."
    show monika oe
    show yuri turned happ cm oe at t51 zorder 2:
        xoffset 50 ypos 500 zoom 0.64
    pause 0.2
    show yuri om
    y "А вот и вторая."
    show mc e1c
    show sayori pani om ce lup rup
    show natsuki pout cm oe
    show monika lsur cm oe
    show yuri neut cm e1d
    s "А!"
    show sayori cm
    show monika om
    m "Осторожно, горячий!"
    show mc oe
    show sayori pout mh oe ldown rdown
    show natsuki neut cm oe
    show monika cm
    show yuri happ cm oe
    s "Нэ..."
    show sayori cm
    show natsuki e1b
    show monika ce
    show yuri ce
    "Итак, попробуем эти хвалёные кексы..."
    show mc ce
    show sayori happ cm ce
    show natsuki oe
    show monika happ cm ce
    "..."
    "......"
    show mc oe
    "Ха..."
    show mc happ cm oe
    "Это очень вкусно!"
    show sayori om
    show natsuki happ cm oe
    show monika oe
    show yuri oe
    s "Объедение!"
    show sayori cm
    show monika om
    m "По-моему, они ещё вкуснее, чем раньше!"
    show monika cm
    show yuri om ce
    y "Да, начинка тает во рту."
    show mc ce
    show yuri cm
    mc "Угу."
    show natsuki om ce lhip rhip
    show yuri oe
    n "Значит, я ещё не потеряла хватку, спасибо!"
    show mc oe
    show natsuki cm ldown rdown
    show monika ce
    "..."
    show mc neut cm oe
    show yuri e1b
    "Все молча жуют кексы."
    "Да, это аппетитно, но...{w}скучно?"
    show yuri ce
    "Нет, скорее слишком спокойно."
    show mc e1e
    "Ой, нафиг, не хочу думать."
    "Надо наслаждаться такой стабильностью."
    show mc oe
    show sayori om
    show natsuki oe
    show monika oe
    show yuri oe
    s "Чай-чай-чай~"
    show mc om
    show sayori cm oe
    mc "Тихо, он не успел ещё остыть."
    show mc cm
    show sayori om
    s "Ничего, я по чуть-чуть."
    show sayori cm
    show natsuki ce
    show monika e1b
    "Хм..."
    show sayori ce
    "Ну-ка тоже попробую..."
    "..."
    show mc e1e
    "{cps=15}Глоток...{/cps}{nw}"
    show mc flus cm ce
    show sayori pani cm oe
    show natsuki pani cm oe
    show monika shoc cm oe
    show yuri vsur cm oe
    mc "{sc=3}МФ-Ф-Ф!!!{/sc}" with vpunch
    show mc oe
    show natsuki laug cm oe
    "{sc=3}СЛИШКОМ МНОГО!{/sc}"
    show monika om
    m "Макс?!"
    show monika cm
    show yuri om
    y "Аккуратно!"
    show mc angr ma oe
    show sayori angr cm oe
    show natsuki om ce lhip rhip
    show yuri pout cm oe
    n "Пха-ха, у тебя глаза из орбит практически вылетели!"
    show sayori om
    show natsuki cm
    s "Не смешно!"
    show mc om ce
    show sayori neut cm oe
    show natsuki happ cm oe ldown rdown
    show monika sad cm oe
    show yuri neut cm e1d
    mc "Тьфу, я слишком увлёкся из-за вкуса..."
    show mc ma
    show yuri om e1b
    y "Ох..."
    show mc neut cm oe
    show sayori happ om oe
    show natsuki neut cm oe
    show monika neut cm oe
    show yuri cm e1d
    s "Кстати, да!"
    show sayori cm
    "Я такой ещё не пробовал..."
    "Юри точно эксперт в области чая."
    "Или гурман..."
    show natsuki curi om oe
    show yuri happ cm oe
    n "Это какой-то новый сорт?"
    show sayori neut cm oe
    show natsuki neut cm oe
    show yuri om lup rup
    y "Да, я недавно решила купить жасминовую заварку, которая потом очень хорошо себя зарекомендовала."
    show yuri e1b
    y "Конечно, у меня были и другие варианты: с мятой, с шиповником и лавандой..."
    show mc curi cm oe
    show yuri flus om oe
    y "Для одних рецептов некоторые ингредиенты было невозможно найти, а другие были сложны в реализации..."
    show mc om
    show yuri neut cm e1d
    mc "Сложны в реализации?"
    show mc neut cm oe
    show sayori curi cm oe
    show yuri happ om oe ldown rdown
    y "К примеру, есть арбузный чай."
    show sayori neut cm oe
    show yuri neut om e1d
    y "Но у нас сейчас неарбузный сезон."
    show natsuki e1b
    show yuri anno om oe
    y "А даже если и арбузный, то мне бы пришлось принести сюда целый килограм арбузной мякоти, чтобы сделать из него сок..."
    show mc om
    show yuri cm
    mc "Ну и ну."
    show mc cm
    "Впервые слышу про существование арбузного чая."
    show sayori happ cm oe
    show natsuki happ cm oe
    show monika happ cm oe
    show yuri happ om oe
    y "Жасмин в этом случае выигрывает по всем параметрам."
    show sayori om
    show yuri cm
    s "Он очень хорошо идёт с кексами."
    show mc happ cm oe
    show sayori ce
    show yuri ce
    s "Ам~"
    show sayori cm
    show natsuki ce
    show monika om ce
    m "Ха-ха..."
    show monika cm
    "..."
    show mc neut cm oe
    "И снова тишина..."
    "Никогда ещё Литературный клуб в полном составе не был таким спокойным."
    show mc ce
    "Аж приятно."
    "..."
    show mc oe
    show sayori lsur cm oe lup rup
    show natsuki neut cm oe
    show monika oe
    show yuri oe
    s "Ой, точно."
    show sayori happ om oe ldown rdown
    show monika neut cm oe
    show yuri neut cm e1d
    s "Завтра вы должны познакомить меня с..."
    show sayori curi om e2b
    show natsuki anno cm oe
    show yuri happ cm oe
    s "Коко...{w}Котото..."
    show sayori cm
    show natsuki om
    n "Котонохой."
    show sayori happ om ce
    show natsuki neut cm oe
    s "Да, с ней!"
    show sayori cm
    show natsuki doub cm oe
    show yuri om e1b lup
    y "Надо не забыть кекс..."
    show sayori oe
    show natsuki om lhip rhip
    show monika happ cm oe
    show yuri cm ldown
    n "Да будет, будет всё, успокойтесь."
    show sayori e1b
    show natsuki cm ldown rdown
    show yuri ce
    "..."
    show mc happ cm e1e
    show natsuki neut cm e1b
    show monika e1c
    "Как же мне, однако, повезло с этим клубом..."
    show mc om oe
    show sayori neut cm oe
    show natsuki oe
    show monika oe
    show yuri neut cm e1d
    mc "Знаете что?"
    mc "Раз мы уж так собрались..."
    show sayori flus cm oe
    show natsuki curi cm oe
    show monika e2a
    show yuri happ cm oe
    mc "То подниму эту...{w}чашку чая, да...{w}за Литературный клуб."
    show mc neut om oe
    mc "Буду краток и лаконичен."
    show sayori happ cm oe
    show natsuki nerv cm oe
    show monika nerv cm e1a n3
    show yuri e1b
    mc "Коллектив хороший."
    show mc curi om e1f
    mc "Э-э-э..."
    show mc neut om oe
    mc "Стихи интересные."
    show mc curi om oe
    mc "Кексы, чай...{w}что ещё..."
    show mc happ om oe
    show yuri ce
    mc "Да всё прекрасно."
    show mc lsur om ce
    show sayori pani cm oe
    show natsuki lsur cm oe
    show monika pani cm oe n2
    show yuri vsur cm oe
    mc "Уп!"
    show mc ma
    "{cps=25}Это всего лишь--{/cps}{nw}"
    show mc pout cm ce
    "{sc=1.5}Большо-о-ой глото-о-ок...{/sc}"
    show sayori om
    s "Макс, ты себя вообще не щадишь!"
    show mc flus cm oe
    show sayori cm
    show natsuki nerv cm ce
    mc "Х-х-х..."
    show mc neut om oe
    show sayori vsur cm oe
    show monika sad cm oe n1
    show yuri lsur cm oe
    mc "Подостыл он, нормально всё."
    show mc shoc cm ce
    mc "Уф-ф-ф..."
    show sayori neut cm oe
    show natsuki om
    show monika neut cm oe
    show yuri neut cm e1d
    n "А вообще это дельная идея..."
    show mc neut cm oe
    show sayori happ cm oe
    show natsuki happ om oe lhip rhip
    show monika e2a
    show yuri happ cm oe
    n "Я выпиваю эту чашку чая за Монику."
    show monika n3
    n "Если бы не ты, то мы бы ни за что не познакомились."
    show mc happ cm oe
    show sayori om
    show natsuki cm
    show monika nerv cm e1a
    s "Да, я тоже!"
    show sayori laug om ce
    show natsuki ce
    s "Моника, ты молодец!"
    show sayori cm
    show yuri om e1b lup
    y "И я..."
    show sayori happ cm ce
    show yuri oe ldown
    y "За тебя и за Литературный клуб, который помогает не только раскрыть писательский талант, но и найти новых друзей."
    show sayori oe
    show natsuki oe
    show monika mb
    show yuri cm
    m "О-ох..."
    show sayori neut cm oe
    show monika cm e1g
    m "..."
    show mc b1b
    show sayori pani cm oe
    show natsuki nerv cm oe ldown rdown
    show monika e1h
    show yuri laug cm oe
    m "......"
    show sayori om
    s "Моника?!"
    show sayori ce
    show monika e4e
    s "Не надо плакать!"
    show sayori cm
    show monika mb
    m "С-спасибо, ребята..."
    show sayori oe
    show monika happ om e4e
    show yuri ce
    m "Я очень растрогана, хах!"
    show sayori sad cm oe
    show natsuki om
    show monika cm
    n "Ой, да ладно тебе, обычное дело."
    show natsuki cm
    show monika om e1g n1
    show yuri happ cm oe
    m "Я очень рада, что встретила вас всех..."
    show mc -b1b
    show sayori nerv cm e1a
    show natsuki happ cm oe
    show monika e4d
    m "Даже не представляла, что у меня получится сделать такой дружный клуб."
    show mc om
    show monika cm e1g
    mc "Как видишь, получилось."
    show mc cm
    show monika om
    m "Да..."
    stop music fadeout 4.0
    show sayori neut cm oe
    show monika cm
    show yuri om lup
    y "В таком случае, если мы затронули тосты, то..."
    show mc neut cm oe
    show natsuki neut cm oe
    show monika oe
    show yuri anno cm oe ldown
    y "М-м-м..."
    show natsuki curi om oe lhip rhip
    show monika neut cm oe
    n "Что?"
    show natsuki cm
    show yuri om
    y "Ну..."
    show mc lsur cm oe
    show sayori shoc cm oe
    show natsuki lsur cm oe ldown rdown
    show monika eyes_tsur_1
    show yuri cm
    show wine zorder 3 with dissolve:
        xpos 30 ypos 170 zoom 0.2 rotate -25
    pause 0.2
    show yuri happ om oe lup rup
    y "Кто-нибудь хочет попробовать немного вина?"
    show yuri cm
    "............"
    show mc om
    show yuri neut cm e1d
    mc "...что?"
    play music literature_club_wine_incident
    show mc cm
    show sayori vang mj oe
    show natsuki laug om ce lhip rhip
    show monika happ cm eyes_tsur_3
    n "ПХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!!!"
    show sayori om
    show natsuki cm
    show yuri lsur cm oe
    s "ЮРИ!"
    show sayori angr om oe
    show natsuki oe
    show monika neut cm oe
    s "В школу нельзя приносить спиртные напитки!"
    show sayori rup
    s "И пить тоже нельзя!"
    show sayori rdown
    s "Тебе станет плохо от них!"
    show sayori vang om ce
    s "Спрячь бутылку!"
    show sayori mj
    show yuri nerv cm oe
    y "{cps=25}Н-но...{/cps}{nw}"
    show sayori angr om oe
    show yuri lsur cm oe
    s "Никаких но!"
    show sayori cm
    "Как она умудрилась пронести бутылку вина у себя в сумке?..."
    show natsuki nerv cm oe ldown rdown
    show yuri nerv cm ce
    y "...праздник..."
    show mc neut cm oe
    show sayori anno cm oe
    show yuri e2b
    y "Я хотела всех обрадовать..."
    show sayori om
    show yuri mj
    s "Нет, Юри, так не надо делать!"
    show mc curi cm oe
    show sayori vsur cm oe
    show natsuki happ cm oe
    show monika happ om oe
    show yuri neut cm e1d ldown rdown
    m "А может, всё-таки попробуем немножко?"
    show mc om
    show natsuki neut cm oe
    show monika neut cm oe
    mc "Смеёшься?"
    show mc neut om oe
    show monika happ cm oe b1f
    mc "Это «немножко» превратится в полностью опустошённую бутылку, более чем уверен."
    show mc cm
    show natsuki happ cm oe
    show monika om
    show yuri happ cm oe
    m "Да ладно тебе, Макс, один раз в жизни попробовать!"
    show natsuki sedu om oe lhip rhip
    show monika cm -b1f
    n "Ага, я бы тоже не отказалась."
    show natsuki sad om oe
    n "Но только совсем капельку, иначе папа убьёт..."
    show mc ce
    show natsuki cm
    show monika ce
    "Чёрт побери, это плохо кончится..."
    show mc oe
    show sayori om e1a
    show natsuki neut cm oe
    show monika oe
    show yuri neut cm e1d
    s "Моника, ты же президент!"
    show sayori cm
    show natsuki happ cm oe
    show monika om
    show yuri happ cm oe
    m "Президенты -- тоже люди."
    show mc angr ma oe
    show natsuki ldown rdown
    show monika ce
    m "Юри, налей нам немного, чай и так уже выпит."
    show monika cm
    show yuri om ce
    y "О, хорошо!"
    show mc om
    show sayori oe
    show natsuki neut cm oe
    show monika oe
    show yuri cm
    mc "Моника, ты обратно до дома не дойдёшь!"
    show mc ma
    show monika om
    m "Ну у меня же есть клуб, на который можно положиться!"
    show mc om
    show sayori angr cm oe
    show natsuki anno cm oe
    show monika cm eyes_tsur_3
    mc "Это уже не смешно!"
    show mc ma
    show sayori om
    s "Полностью согласна с Максом!"
    show sayori cm
    show natsuki pani om ce b1e
    n "Бе-бе-бе!"
    show natsuki anno om oe -b1e lhip rhip
    show monika oe
    n "Хватит душнить."
    n "Попробуем чуть-чуть и выбросим."
    show sayori pout cm oe
    show natsuki cm
    show monika ce
    s "Хмф..."
    show mc curi om ce
    show natsuki neut cm oe ldown rdown
    show monika neut cm oe
    show yuri neut cm e1d
    mc "Какое вообще удовольствие травить свой организм?"
    show mc oe
    mc "Особенно когда это ничерта не вкусно."
    show mc neut cm oe
    show yuri om lup
    y "Вероятно, выпивают из-за эффекта опьянения, прилива эндорфинов и притупления чувств..."
    show mc curi om oe
    show sayori anno cm oe
    show natsuki doub cm oe
    show monika happ cm oe
    show yuri cm ldown
    mc "И оно вам надо?"
    show mc neut cm oe
    show natsuki happ cm oe
    show monika om
    show yuri happ cm oe
    m "Один раз можно!"
    show mc e1e
    show natsuki ce
    show monika cm
    show yuri ce
    "Нет, их нифига не переубедишь..."
    show mc om oe
    show sayori neut cm oe
    show monika e1b
    mc "Сайори, мы приплыли."
    show mc cm
    show sayori om
    s "Что будем делать?"
    show mc om
    show sayori cm
    show yuri e1b
    mc "Раз до них невозможно достучаться, то поступим другим образом."
    show mc curi om oe
    mc "У тебя ключи от клуба с собой?"
    show mc neut cm oe
    show sayori om
    show monika ce
    s "Да, в кармане."
    show mc om
    show sayori cm
    mc "Отлично."
    show natsuki oe
    mc "Закрой двери и приоткрой окна."
    show sayori happ cm oe
    show yuri ce
    mc "Так, во-первых, никто зайти не сможет, а во-вторых, запах вина выветрится."
    show mc cm
    show sayori om
    s "Хорошо, сейчас!"
    show mc om
    show sayori cm
    mc "Я пока буду контролировать их «питьё»."
    show mc cm
    hide sayori with dissolve
    pause 0.25
    show mc ce
    "Остаётся молиться, чтобы в коридоре никого не оказалось."
    show yuri oe
    "Стёкла на дверях ничем не прикроешь..."
    show mc oe
    show natsuki pout cm oe
    show monika curi om eyes_tsed_3 n2
    show yuri neut cm e1d
    m "Бе-э-эх!"
    show monika neut om oe n1
    m "Какое-то оно...{w}странное..."
    show monika cm
    show yuri om
    y "Это красное вино со вкусом вишни."
    show mc curi om oe
    show natsuki neut cm oe
    show yuri cm
    mc "Где ты его достала?"
    show mc neut om oe
    mc "У нас же запрещена продажа алкогольной продукции тем, кому меньше 20 лет."
    show mc cm
    show monika happ cm oe
    show yuri happ om oe
    y "Пусть это останется секретом, ведь это подарок на наш праздник."
    show yuri cm
    mc "Хм..."
    show natsuki e1b
    "Небось вино взято из дома."
    "Родители в будущем ей за это не настучат?"
    show natsuki om ce
    show monika neut cm oe
    show yuri neut cm e1d
    n "Ой, фу."
    show mc happ cm oe
    show natsuki nerv om oe
    n "Нет, с меня хватит, я больше это пробовать не буду."
    show natsuki pani om ce
    n "Гадость какая-то!"
    show mc om e1h
    show natsuki angr cm oe
    show monika happ cm oe
    mc "Не вижу в твоих глазах дух авантюризма, который был буквально минуту назад."
    show mc cm
    show sayori turned neut cm oe at t54 zorder 4:
        xoffset -30 ypos 665 zoom 0.64
    show natsuki om oe lhip rhip
    n "Сам попробуй, а потом уже говори!"
    show mc neut cm oe
    show sayori om
    show natsuki cm
    show monika neut cm oe
    show yuri e1b
    s "Макс, ты же ведь не будешь этого делать?..."
    show mc om
    show sayori cm
    show natsuki curi cm oe
    mc "Нафиг надо?"
    show sayori happ cm oe
    show natsuki ldown rdown
    show yuri ce
    mc "Я не собираюсь употреблять алкоголь ни при каких обстоятельствах."
    show mc cm
    show sayori neut cm oe
    show natsuki neut cm oe
    show monika curi md oe
    show yuri om
    y "...м-м-м, не такое, как я думала..."
    show monika om e1c
    show yuri cm e1d
    m "Хотя подожди, я слишком быстро проглотила."
    show monika neut om oe
    m "Мне надо прочувствовать вкус."
    show mc worr cm oe
    show sayori angr cm oe
    show natsuki pout cm oe
    show monika happ om oe
    show yuri happ cm oe
    m "Юри, налей ещё."
    show mc om
    show monika cm
    show yuri e1b
    mc "Моника..."
    show mc angr ma oe
    show monika om ce
    m "Всё под контролем, Макс!"
    show mc om
    show monika cm
    mc "Я вижу."
    show mc lsur cm oe
    show sayori flus cm oe
    show natsuki shoc cm oe
    show monika oe
    show yuri om ce
    y "Вот."
    show monika om
    show yuri cm
    m "Попробуем снова..."
    show monika cm
    "Полчашки у каждой?!"
    show sayori om
    show natsuki om
    show monika neut cm e4c
    m "..." with vpunch
    show monika n3
    "Залпом?!"
    show natsuki cm
    show monika e4b n4
    m "{cps=20}...м-м-м...{/cps}"
    show mc neut cm oe
    show sayori cm
    show natsuki pout cm oe
    show monika mh eyes_tsed_3
    show yuri n4
    m "{cps=20}Приторная вишня...{/cps}"
    show sayori pani cm oe
    show monika om e4c
    m "{cps=40}Ип!{/cps}"
    show natsuki om ce
    show monika cm ce
    show yuri neut cm oe
    n "Чересчур приторная!"
    show natsuki cm
    show monika happ cm eyes_tsed_2
    show yuri om
    y "{cps=20}Д-да нет, н-нормальная...{/cps}"
    show sayori mi
    show natsuki oe
    show monika ce
    show yuri cm
    s "О нет, они начинаются пьянеть..."
    show sayori cm
    show yuri happ cm e1b
    "Уже развезло?"
    "Хотя чему я удивляюсь?"
    show mc ce
    "Суммарно чуть больше половины чайной чашки для женского организма, который ни разу не употреблял алкоголь."
    "Кажется, это всё быстро сдуется."
    "И нам это, кстати, на руку."
    show mc oe
    show sayori sad cm oe
    show monika om eyes_tsed_1
    show yuri curi md oe
    m "{cps=20}З-знаешь, Юри-и-и?{/cps}"
    show monika cm
    show yuri cm
    y "{cps=20}Ч-ч-ч?...{/cps}"
    show mc angr ma oe
    show sayori vang mj oe
    show monika om eyes_tsed_2
    show yuri happ cm oe
    m "{cps=20}Это наст{/cps}{cps=30}о-о-о-о-о{/cps}{cps=20}лько странно, что х-хочется ещ-щё!{/cps}"
    show monika cm ce
    show yuri om ce
    y "{cps=25}Э-э-э{/cps}{cps=20}хе-хе-хе...{/cps}"
    show mc om
    show monika eyes_tsed_1
    show yuri cm
    mc "Стоп!"
    show mc ma
    show sayori om
    show monika sad md eyes_tsed_1
    show yuri neut cm oe
    s "Так, нет, хватит!"
    show sayori mj
    pause 0.1
    hide sayori with dissolve
    pause 0.25
    show natsuki om
    n "Да, это уже перебор..."
    show natsuki cm
    show monika om ce
    m "{cps=20}Ну-ну-ну!{/cps}"
    show monika eyes_tsed_2
    show yuri happ cm ce
    m "{cps=20}Ещё к{/cps}{cps=30}а-а-а-а{/cps}{cps=20}пельку!{/cps}"
    show mc om
    show monika md
    mc "Блин, Моника, на себя посмотри!"
    mc "Ты уже никакая!"
    show mc ma
    show monika angr om eyes_tsed_1
    m "{cps=20}Я?!{/cps}"
    show mc neut cm oe
    show monika happ om ce
    show yuri oe
    m "{cps=20}Я у-умная, кра{/cps}{cps=30}с-с-с{/cps}{cps=20}ивая, в мер-ру упит-{cps=15}тн-н-н...{/cps}{w}{cps=20}я девушка-а в п{/cps}{cps=30}о-о-о{/cps}{cps=20}лном расцве-ете сил!{/cps}"
    show monika neut cm e4c
    m "{cps=20}Уп!{/cps}"
    show mc om
    show monika eyes_tsed_1
    mc "Нет, Моника, ты просто в зюзю."
    show mc cm
    show monika lsur om ce
    m "{cps=25}Э-э-э-э-эх...{/cps}"
    show monika md
    show sayori turned angr cm oe at t51 zorder 1:
        xoffset -30 ypos 500 zoom 0.64
    pause 0.2
    show yuri shoc om oe lup rup
    y "{cps=20}С-С-Сайори-и?!{/cps}"
    hide wine
    hide sayori
    hide yuri
    with dissolve
    pause 0.25
    show monika neut cm eyes_tsed_2
    y "{cps=23}Отда-а-ай вино!{/cps}"
    s "Нет, даже не пытайся отобрать эту бяку!"
    y "{cps=20}Не бяка!{/cps}"
    show monika happ cm eyes_tsed_2
    y "{cps=20}Это вк{/cps}{cps=30}у-у-у{/cps}{cps=20}сно-о!{/cps}"
    show monika om eyes_tsed_1
    m "{cps=20}Н-не сказать, ч-что по сути вку-усно...{/cps}"
    show monika cm
    y "{cps=23}...н-но вкусно!{/cps}"
    show natsuki om ce
    show monika ce
    n "Да ничего там вкусного..."
    show sayori turned angr cm ce at t54 zorder 4:
        xoffset -30 ypos 665 zoom 0.64
    show wine zorder 5 with dissolve:
        xpos 730 ypos 370 zoom 0.2 rotate -25
    show natsuki cm
    show yuri turned worr cm oe n3 at t51 zorder 2:
        xoffset 50 ypos 500 zoom 0.64
    pause 0.2
    show mc curi om oe
    show sayori neut cm oe
    show natsuki neut cm oe
    show monika neut cm eyes_tsed_2
    mc "И куда его?"
    show mc neut cm oe
    show sayori om
    show monika lsur eyes_tsed_3
    show yuri vsur cm oe
    s "Можно выбросить в мусорку."
    show sayori cm
    show monika om
    show yuri shoc om oe lup rup
    my "{cps=23}Н-Н-НЕ!!!{/cps}"
    show mc om
    show monika cm eyes_tsed_1
    show yuri vsur cm oe
    mc "Не слишком ли радикально?"
    show sayori e1c
    show yuri lsur cm oe ldown rdown
    mc "Оно денег стоит."
    show mc cm
    show sayori oe
    show natsuki om e1b
    show monika happ cm eyes_tsed_1
    n "А ещё там осталось примерно половина."
    show natsuki cm
    show monika ce
    show yuri sedu cm ce
    y "{cps=40}Ик!{/cps}"
    show sayori anno om ce
    show natsuki oe
    show yuri worr om ce
    s "Ради здоровья клуба..."
    show sayori om
    show monika curi md eyes_tsed_1
    show yuri e1a
    s "Надо избавиться от этой бутылки любым способом."
    show mc curi cm oe
    show sayori neut cm oe
    show natsuki curi om oe lhip rhip
    show monika happ cm eyes_tsed_1
    show yuri neut cm oe
    n "Может, просто вернем обратно, откуда Юри взяла?"
    show natsuki cm
    show yuri happ om oe
    y "{cps=20}Д-да!{/cps}"
    show mc om
    show natsuki ldown rdown
    show monika neut cm eyes_tsed_1
    show yuri neut cm oe
    mc "Ага, чтобы она не устояла перед соблазном и «захлебнулась» в этом вине в одиночку?"
    show mc neut om e1e
    show natsuki pout cm oe
    show monika b1b
    show yuri vsur cm oe
    mc "Нет, этот вариант отпадает."
    show mc cm
    show yuri om
    y "{cps=20}Н-нет!{/cps}"
    show mc oe
    show sayori om
    show yuri cm
    s "Его только и выбрасывать."
    show mc om
    show sayori cm
    show natsuki curi cm oe
    show monika -b1b
    show yuri neut cm oe
    mc "Я бы мог взять на хранение, но смысл?"
    show mc cm
    show natsuki om
    n "Никакого."
    show mc om
    show natsuki cm
    mc "Именно."
    show mc cm
    show sayori happ om oe
    show natsuki neut cm oe
    show monika b1b
    show yuri lsur cm oe
    s "Тогда куда выбрасываем?"
    show sayori cm
    show monika om ce
    show yuri nerv cm oe
    my "{cps=20}Ви-и-и-и-и...{/cps}"
    show mc om
    show monika cm
    show yuri mj
    mc "В любую общественную мусорку, где принимается стекло."
    show sayori neut cm oe
    show yuri ce
    mc "Но сначала сольём вино и промоем бутылку."
    show mc cm
    show natsuki curi om oe lhip rhip
    n "Здесь, что ли?"
    show mc om
    show natsuki cm
    mc "Слишком рискованно."
    show mc cm
    show natsuki e1b
    show monika om eyes_tsed_2
    show yuri sad cm oe
    m "{cps=20}У-у-у...{/cps}"
    show mc om ce
    show natsuki neut cm oe ldown rdown
    show monika cm
    mc "О, вот как поступим."
    show mc oe
    show natsuki pout cm oe
    show monika eyes_tsed_1 -b1b
    show yuri neut cm oe
    mc "Вы вдвоём доведёте Юри до дома и поможете ей отлежаться."
    show mc cm
    y "{cps=20}М-м-м-м-м?{/cps}"
    show mc om
    mc "Я возьму на себя Монику и вино."
    mc "Сайори, давай его сюда."
    show mc cm
    show sayori om
    s "Угусь."
    show sayori cm
    call window_close

    hide wine
    hide sayori
    with dissolve
    pause 1.0
    show sayori turned happ cm ce at t55 zorder 1:
        xoffset -30 ypos 500 zoom 0.64
    show wine zorder 3 with dissolve:
        xpos 960 ypos 170 zoom 0.2 rotate -25
    pause 0.7
    hide sayori with dissolve
    pause 1.0
    show sayori turned happ cm ce at t54 zorder 4:
        xoffset -30 ypos 665 zoom 0.64
    pause 0.2
    show mc om
    show sayori neut cm oe

    call window_open
    show yuri e1b
    mc "И да, как закончишь, зайдёшь к нам забрать бутылку?"
    show mc b1b
    show monika ce
    mc "Оставить Монику одну в таком убитом состоянии, даже на короткое время, я не могу."
    show mc -b1b
    show sayori om
    s "Поняла."
    show sayori cm
    show natsuki doub om oe lhip rhip
    show yuri ce
    n "Ты серьёзно думаешь, что мы с Сайори донесём эти «буфера» до дома?"
    show mc om
    show natsuki neut cm oe
    mc "Вполне, два человека могут справиться."
    show mc curi om oe
    show natsuki sedu cm oe b1f ldown rdown
    show monika happ cm eyes_tsed_2
    mc "У меня не «легче», между прочим."
    show mc neut cm oe
    show monika om
    show yuri oe
    m "{cps=20}К-комплимент?{/cps}"
    show monika ce
    m "{cps=20}Это та-а-ак мило, М-Макс!...{/cps}"
    show mc om e1e
    show sayori happ cm oe
    show natsuki neut cm oe -b1f
    show monika cm
    mc "Короче, всё."
    show monika eyes_tsed_1
    mc "Собираемся."
    show mc oe
    show sayori neut cm oe
    mc "А, Сайори, дверь открыть не забудь!"
    show sayori happ cm oe
    mc "И ключи сдать, и окна закрыть, и сервиз убрать в кладовку (потом его почистим и отнесём обратно)..."
    show mc cm
    show sayori om
    s "Да-да-да, проще пареной репы!"
    show sayori cm
    pause 0.1
    hide sayori with dissolve
    show natsuki e1b
    show monika ce
    show yuri e1b

    scene black with dissolve
    pause 0.25
    "Так, вино..."
    "Потуже закрутим и уберём к себе в сумку..."
    y "{cps=30}Ви-и-ино-о-о...{/cps}"
    "..."
    "Ха, нормально так уместилось, практически вертикально."
    "Средняя бутылка, как-никак."
    "Теперь неудивительно, как Юри удалось его транспортировать."
    "...блин, от этой мысли только пугаешься."
    "Мало ли какую хрень могут вот так вот взять и пронести без чьего-либо ведома."

    scene bg club_day
    show monika forward neut cm eyes_tsed_1 n4 at t21
    with dissolve
    pause 0.25
    n "Всё, Юри, давай, вставай."
    y "{cps=25}Не-е-е-е...{/cps}"
    y "{cps=20}М-мы только н{/cps}{cps=30}а-а-а{/cps}{cps=20}чали...{/cps}"
    show monika om
    m "{cps=20}П-праздник не отменя--{/cps}{nw}"
    show monika mh e4c at h21
    m "{cps=40}Ик!{/cps}"
    show monika cm eyes_tsed_2
    show sayori turned happ cm oe at t22
    pause 0.2
    show sayori om
    s "Готово!"
    show sayori cm
    mc "Отлично."
    show monika flus om eyes_tsed_2 lpoint
    m "{cps=35}Я н-ниче-его-о не {/cps}{cps=20}объ-яв-л-я-л-а!{/cps}"
    show monika cm ldown
    show sayori neut cm oe
    mc "А теперь, раз сам президент у нас пребывает в недееспособном состоянии, то, как вице-президент, объяви, пожалуйста, об окончании нашего мероприятия."
    show monika neut cm eyes_tsed_1
    show sayori happ om ce lup rup at h22
    s "Итак, друзья!"
    show monika om rhip
    show sayori cm
    m "{cps=25}М-моя фраза-а-а!{/cps}"
    show monika cm rdown
    show sayori om oe ldown rdown
    s "Наш праздник окончен!"
    show sayori ce
    s "Всем по домам!"
    show monika sad om ce
    show sayori cm
    my "{cps=30}Не-е-е-е-е-е-ет!{/cps}"
    show monika cm
    show sayori neut cm oe
    n "Сайори, подхвати её с другой стороны."
    show sayori at thide
    hide sayori
    pause 0.2
    n "Её сумку я на себя надену."
    s "Угусь."
    y "{cps=40}Хип!{/cps}"
    y "{cps=20}К-куда?{/cps}"
    n "Туда!"
    n "Лучше ноги переставляй нормально, чтобы ни у кого вопросов не возникло!"
    y "{cps=30}Мэ-э-э-э-э...{/cps}"
    show monika eyes_tsed_2
    mc "Так, Моника, и ты давай тоже собирайся."
    show monika at t11
    pause 0.2
    show monika flus om ce
    m "{cps=20}Я не х-о-ч-у!{/cps}"
    show monika cm
    mc "А тебя никто не спрашивает."
    "Нести её сумку на пару с моей, конечно, неудобно, но обе хотя бы лёгкие."

    scene black with dissolve
    pause 0.25
    mc "Залезай ко мне на спину."
    m "{cps=20}К те-бе?...{/cps}"
    mc "А к кому ещё?"
    "А выдержу ли я?..."
    "Да чего я сомневаюсь?"
    "Это всё равно, что мешок цемента перетаскивать."
    "Килограммов ~45 где-то, да?"
    "В деревне приходилось этим заниматься, но давно это было..."
    m "{cps=20}О-о-ох...{/cps}"
    m "{cps=20}Х-х-х{/cps}{cps=30}вать~{/cps}"
    mc "Кх-х-х..."
    "55 минимум!"
    m "{cps=25}Хи-хи-хи-хи-хи!{/cps}"
    mc "Не надо тереться о мою шею, щекотно!"
    m "{cps=25}М-о-г-у с-е-б-е п-о-з-в-о-л-и-ть, св-вити-и!{/cps}"
    n "{size=19}Вы там долго?{/size}"
    mc "Уже идём!"
    "Чёрт побери..."
    "Надеюсь, по пути домой на глаза никто не попадётся..."
    stop noise_1 fadeout 2.0
    stop music fadeout 3.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 10 afternoon with wipeleft_scene
    mc "Пф-ф-фе-е-е..."
    mc "Хе-е-е..."
    mc "Пхе..."
    m "{cps=25}Я п-поняла-а!{/cps}"
    mc "А?"
    m "{cps=25}Как с-скучно мы-ы живём...{/cps}"
    m "{cps=25}В нас п-п-пропал...{w}этот...{w}н-ну как ты та-а-ам сказ-зал?...{/cps}"
    m "{cps=25}О-о, дух {/cps}{cps=15}а-в-а-н-т-ю-р-и-з-м-а!{/cps}{nw}"
    m "{cps=40}Уп!{/cps}" with vpunch
    mc "Моника, твоё сознание уже уплыло."
    m "{cps=20}Не-е-е, Макс...{/cps}"
    m "{cps=25}П-парни переста-али ба-ло-ваться с {/cps}{cps=15}л-ю-б-и-м-ы-м-и{/cps}{cps=25} девушками!{/cps}"
    m "{cps=25}Мы все пере...{w}ре...{w}стали де-е-елать больши-ие хоро-ошие глупости-и!{/cps}"
    mc "Ну не знаю..."
    mc "Лично у меня шила в заднице никогда не было."
    m "{cps=20}М-м-м...{/cps}"
    "А мысль-то актуальная..."
    "В нашей стране в последнее время серьёзная проблема с рождаемостью."
    "Но тут вопрос больше с ценами, обеспечением и ответственностью..."
    m "{cps=20}Макс...{/cps}"
    mc "Что?"
    m "{cps=25}М-мы уже...{/cps}{nw}"
    m "{cps=40}Ик!{/cps}" with vpunch
    m "{cps=25}...пришли?{/cps}"
    mc "Нет, Моника, не пришли."

    scene bg niigata street suburban 11 afternoon with wipeleft_scene
    m "{cps=25}Мы уже {/cps}{cps=15}п-р-и-ш-л-и?{/cps}"
    mc "Пока нет."
    "Сколько там ещё тащиться?"
    "И правильно ли мы идём?..."

    scene bg niigata street suburban 15 day with wipeleft_scene
    m "{cps=35}А с-с-с{/cps}{cps=25}ейчас-то пришли-и?{/cps}"
    mc "Нет!"
    "Ей невтерпёж?!"

    scene bg niigata street suburban 16 day with wipeleft_scene
    m "{cps=25}А теп{/cps}{cps=35}е-е-е{/cps}{cps=25}рь п-пришли?{/cps}"
    mc "ДА!"
    m "{cps=25}Ч-честно?...{/cps}"
    mc "{sc=3}НЕ-Е-ЕТ!!!{/sc}" with vpunch

    scene black with wipeleft_scene
    m "{cps=25}Мы-ы-ы уже пришли?~{/cps}"
    mc "Мы уже пришли?"
    m "{cps=25}Ч-что?{/cps}"
    mc "Что?"
    m "{cps=25}Ты-ы повтор-ряешь мои сло-ова?{/cps}"
    mc "Ты повторяешь мои слова?"
    m "{cps=25}Со{/cps}{cps=35}в-в-в{/cps}{cps=25}сем не смешно, М-Макс{/cps}{cps=40}--{/cps}{nw}"
    m "{cps=40}Ип!{/cps}"
    mc "Ты меня сбиваешь, Моника!"
    mc "Я и так еле плетусь с двумя сумками наперевес и с тобой на спине, пытаясь не отклониться от маршрута, а тут твои вопросы!"
    m "{cps=25}Ой, хорош{/cps}{cps=35}о-о-о{/cps}{cps=25}-хоро{/cps}{cps=35}ш-ш-ш{/cps}{cps=25}о, я {/cps}{cps=15}п-п-п...{w}{/cps}{cps=25}няла.{/cps}"
    m "{cps=25}Просто я {/cps}{cps=35}о-оф-фигела{/cps}{cps=25} от ск{/cps}{cps=35}у-у-у{/cps}{cps=25}ки!{/cps}"
    mc "А ты попробуй себя чем-нибудь развлечь!"
    m "{cps=30}Уф-ф-ф...{/cps}"
    "..."
    "Неужто тишина?"
    "Надо мной смиловались!"
    "Теперь надо сосредоточиться на ногах."
    "Они уже забиваются."
    "По идее, мы должны быть рядом с её домом, поэтому--{nw}"
    play sound monika_lips_popcorn
    pause 1.0
    "{sc=1}......{/sc}"
    "{sc=1}Она стала.{w} «Хлопать» губами.{w} Возле моего\nуха?{/sc}"
    play sound monika_lips_popcorn
    pause 0.5
    "{sc=2}......{/sc}"
    m "{cps=35}Хи-хи-хи...{/cps}"
    play sound monika_lips_popcorn
    pause 0.5
    mc "{sc=3}У-У-У-У-У-У-У-У!{/sc}" with vpunch
    mc "{cps=40}{sc=1}Ну 5 минут...{/sc}{/cps}"
    mc "{cps=40}{sc=1}Ты можешь прерваться...{/sc}{/cps}"
    mc "{cps=80}{sc=3}ХОТЬ НА 5 МИНУТ?!{/sc}{/cps}" with vpunch
    "{sc=3}......{/sc}"
    "{sc=2}......{/sc}"
    "{sc=1}......{/sc}"
    play sound monika_lips_popcorn
    pause 0.5
    mc "{sc=3}А-А-А-А-А-А-А-А-А!!!{/sc}" with vpunch
    mc "{sc=3}Мы пришли или нет?!{/sc}"
    m "{cps=35}Да-а-а!{/cps}"
    "{sc=3}В смысле?!{/sc}"

    scene bg monika house outside day with dissolve
    pause 0.25
    mc "{sc=3}УРА-А-А!{/sc}"
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day
    show monika forward flus cm ce n4 at t11
    with wipeleft_scene
    show monika om
    m "{cps=25}О-о-ох, голова кружится...{/cps}"
    show monika cm
    mc "Аккуратно, давай на диван."
    call window_close

    hide monika with dissolve
    pause 0.2
    scene bg monika house livingroom day at monika_sofa
    show monika forward nerv cm ce n4 at e11
    with dissolve
    pause 0.25
    show monika cm eyes_tsed_2

    call window_open
    show monika mb
    m "{cps=35}Э-хе-хе-хе-хе...{/cps}"
    show monika cm
    "Что-то она слишком сильно расклеилась."
    show monika ce
    "Так и до рвоты недалеко."
    show monika flus cm ce
    mc "Как ты себя чувствуешь?"
    show monika om
    m "{cps=25}О-о-о...{/cps}"
    show monika eyes_tsed_1
    m "{cps=25}Стра{/cps}{cps=15}н-н-н-{/cps}{cps=25}но...{/cps}"
    show monika neut cm eyes_tsed_1
    mc "Конкретнее: тяжело дышать, тошнит, ещё что-нибудь."
    show monika mh
    m "{cps=25}Душно...{/cps}"
    m "{cps=25}Жарко...{/cps}"
    show monika flus om ce
    m "{cps=25}Голова слегка к-крутится...{/cps}"
    show monika cm
    mc "Подожди, я сейчас окна открою."

    scene black with dissolve
    pause 0.25
    m "{cps=25}Н-но я ст-текла как трё-ёзвыш-шко!{/cps}"
    mc "Вот именно, что стекла на диван."
    mc "Ты вся размякла."
    m "{cps=25}Уф-ф...{/cps}"
    "Хорошо, что сейчас лёгкий ветер на улице задувает..."
    mc "Кстати, Моника."
    m "{cps=25}Д-да-а, Макс-с?{/cps}"
    mc "У тебя есть тут вентилятор или кондиционер?"
    m "{cps=25}Д-да, поищи пульт...{/cps}"
    "Ещё пульт искать..."
    "А, не, вот он."
    "..."
    "Так, чуть ниже поставлю..."
    "..."
    "Во, всё."
    "Какой-то он очень тихий, в отличие от моего..."
    "Так, надо вино вылить, Сайори должна же прийти!"

    scene bg monika house livingroom day at monika_sofa
    show monika forward flus cm ce n4 at e11
    with dissolve
    pause 0.5
    show monika neut cm eyes_tsed_1
    mc "Мони, я пока с вином разберусь."
    show monika happ cm eyes_tsed_1
    mc "Если что, сразу зови, хорошо?"
    show monika om
    m "{cps=25}К-конечно, с-свити...{/cps}"
    show monika ce
    m "{cps=25}Буд...{w}бу...{w}б{/cps}{cps=35}у-у-у{/cps}{cps=25}д...{w}жать!{/cps}"
    show monika cm
    mc "...чего?"
    show monika neut cm eyes_tsed_1
    mc "Моника, почётче."
    show monika om e4c
    m "{cps=25}Тьф-пф-пф!{/cps}"
    show monika happ om eyes_tsed_1
    m "{cps=15}Б-у-д-у ж-д-а-ть!{/cps}"
    show monika cm
    mc "А-а..."
    show monika ce

    scene black with wipeleft_scene
    mc "Хм..."
    "Всего 2 дня назад я был здесь гостем, а теперь веду себя, как хозяин."
    "Даже на кухне ни разу не был."
    "Как же это абсурдно!"
    "Но сейчас совершенно не до этого."

    scene bg monika house kitchen day
    show wine:
        align (0.5, 0.5) anchor (0.5, 0.5)
        xpos 250 ypos 520 rotate -25
    with wipeleft_scene
    "Уютненько тут, однако..."
    "А, вот раковина."
    show wine with dissolve:
        xpos 640 ypos 360 rotate 0
    pause 0.2
    "Ну что, вино?"
    "Пора прощаться."
    show wine with dissolve:
        xpos 250 ypos 520 rotate -25
    "Жалко, конечно, но ты больше никому не нужно."
    call window_close

    hide wine with dissolve
    pause 1.0
    play sound pouring_wine
    pause 21.5

    call window_open
    "Только что в раковину была спущена куча денег."
    "Лучше б они были потрачены на что-то более полезное."
    pause 0.2
    play sound doorbell_monika
    pause 1.5
    mc "Что, уже?!"

    scene black with wipeleft_scene
    "Надо спросить, как там с Юри дела обстоят."
    "Не хватало, чтобы и она ещё сильно скисла."
    "..."
    "А стоит ли бутылку промывать?"
    "Ай, без этого обойдёмся."
    call window_close

    pause 2.0
    play sound house_door_open
    play noise_3 street_suburban_noise fadein 1.0
    pause 4.0
    stop noise_3 fadeout 1.0
    play sound house_door_close

    call window_open
    scene bg monika house hallway day
    show sayori turned happ cm oe school_bag at t11
    with dissolve_scene_full
    mc "Что-то ты быстро."
    show sayori om
    s "А чего медлить?"
    show sayori neut cm oe
    mc "Полагаю, Юри более-менее в состоянии?"
    show sayori om rup
    s "Да, она хоть и пьяная, но в сознании."
    show sayori happ om oe rdown
    s "Никаких ухудшений не произошло, поэтому за неё можно не беспокоиться."
    s "Нацуки осталась с ней ненадолго, потом пойдёт домой."
    show sayori cm
    mc "Фух."
    show sayori neut om oe b1d
    s "Кстати, она сказала, что уже не раз пробовала алкоголь..."
    show sayori cm
    mc "Да?"
    show sayori pout cm oe -b1d
    s "Угу."
    show sayori happ om oe
    s "...но благодаря этому у неё есть опыт в борьбе с опьянением."
    show sayori neut om oe
    s "В общем, она просила передать Монике этот кусочек имбиря, он хорошо помогает организму бороться с токсинами."
    s "Она должна съесть его лишь тогда, когда у неё не будет раздражён желудок."
    show sayori cm
    mc "Ясно."
    show sayori om b1f
    s "Как она там?"
    show sayori cm -b1f
    mc "Да хреново ей."
    mc "Когда домой тащились, была ещё ничего, бодренькой."
    show sayori flus cm oe
    mc "А сейчас прямо свалилась, голова кружится, душно, да и вообще вяло и тяжело реагирует."
    show sayori om
    s "Её не тошнило?"
    show sayori neut cm oe
    mc "Нет, к счастью."
    mc "Хотя всё к этому идёт."
    show sayori sad om oe
    s "Плохо дело..."
    show sayori cm
    mc "Ничего, справится."
    show sayori neut cm e1b
    show wine with dissolve:
        align (0.5, 0.5) anchor (0.5, 0.5)
        xpos 250 ypos 520 rotate -25
    mc "Ладно, вот бутылка."
    mc "А имбирь я ей попозже дам."
    hide wine with dissolve
    pause 0.15
    show sayori om oe
    s "Хорошо..."
    show sayori cm
    mc "И да."
    mc "Может, придёшь к нам завтра утром?"
    show sayori happ cm oe
    mc "Поможем Монике втянуться в строй."
    show sayori laug ma oe
    mc "Мне одному это сделать будет проблематично."
    show sayori om ce
    s "Макс, я бы всё равно её проведала, так что да!"
    show sayori happ cm ce
    mc "Вот и хорошо."
    show sayori neut cm oe
    mc "Мне придётся тогда здесь переночевать, Монике слишком плохо."
    show sayori curi om oe
    s "А ничего...{w}не случится?"
    show sayori cm
    mc "А что случится?"
    show sayori neut cm oe
    mc "Разве что мы отрубимся раньше времени."
    mc "А если ты про мой дом, то там всё выключено и закрыто."
    show sayori om
    s "...ладно."
    show sayori cm
    mc "И извини, что на тебя всё взваливаю."
    show sayori sedu cm oe
    mc "То это, то то..."
    show sayori mb
    s "Ой, Макс..."
    s "Я бы и без тебя так поступила."
    show sayori cm
    mc "Ну окей."
    show sayori happ cm oe
    mc "Если что, на связи."
    show sayori om ce
    s "Поняла!"
    show sayori cm ce
    mc "До завтра, Сайори."
    show sayori om oe
    s "До завтра, Макс!"
    show sayori cm
    call window_close

    scene black with dissolve
    pause 2.0
    play sound house_door_open
    play noise_3 street_suburban_noise fadein 1.0
    pause 4.0
    stop noise_3 fadeout 1.0
    play sound house_door_close
    pause 2.0

    call window_open
    "Имбирь горький..."
    "Всухомятку жевать -- такое себе удовольствие."
    "Надо отнести его на кухню: пусть полежит на столе, пока Монике не станет лучше."
    "Но сначала проверим её состояние."

    scene bg monika house livingroom day
    show monika forward body neut om ce n4 pants at t11
    with wipeleft_scene
    mc "Моника, предлагаю нам--{nw}"
    show monika flus me eyes_tsed_2
    mc "{sc=3}ПЕРЕОДЕТЬСЯ?!{/sc}" with vpunch
    show monika eyes_tsed_1
    mc "Зачем до гола?!"
    show monika om lpoint
    m "{cps=25}Мне ж{/cps}{cps=35}а-а-а{/cps}{cps=25}рко, Макс!{/cps}"
    show monika ce ldown
    m "{cps=25}Мне-е-е очень жа-а-а...{/cps}{nw}"
    show monika curi om ce at panic
    m "{cps=35}{bt=7}...а-а-а-а-а...{/bt}{/cps}"
    show monika cm
    mc "Тихо-тихо-тихо!"
    mc "Не надо падать!"
    mc "Вернись на диван!"
    show monika om lpoint
    m "{cps=25}{bt=7}Н-нет, Макс, с-стой...{/bt}{/cps}"
    show monika cm ldown
    mc "...что?!"
    call window_close

    play sound hugs
    hide monika
    show monika forward body neut om eyes_tsed_1 n4 at e11
    with dissolve
    pause 0.5

    call window_open
    mc "Ап..."
    "..."
    "Блин, серьёзно?"
    "У неё гормоны сейчас заиграли?"
    play music your_eyes
    show monika flus om eyes_tsed_1
    m "{cps=25}Макс...{/cps}"
    show monika neut mh oe
    m "{cps=25}Посмотри мне в глаза.{/cps}"
    show monika om
    "Как она чётко и уверенно это сказала..."
    mc "Допустим..."
    show monika mh oe
    m "{cps=25}Что ты...{w}видишь?{/cps}"
    show monika om eyes_tsed_1 b1b
    mc "Глаза человека, у которого перегар."
    show monika mh eyes_tsed_2
    m "{cps=35}Да-а не-е-ет!{/cps}"
    show monika oe -b1b
    m "{cps=25}Что ты...{w}видишь в моих глазах?{/cps}"
    show monika anno me oe
    mc "...своё отражение?"
    mc "Белок, радужки, зрачки..."
    show monika om
    m "{cps=25}Макс...{/cps}"
    show monika me
    mc "Чёрт побери, Моника."
    show monika happ cm eyes_tsed_1
    mc "Нашла время для романтики..."
    show monika om ce
    m "{cps=25}З-значит, ты меня понимаешь, х-хе-хе...{/cps}"
    show monika neut mh eyes_tsed_1
    m "{cps=25}Ты ве-едь...{w}чувствуешь...{w}моё тепло?{/cps}"
    show monika om
    mc "...да?"
    mc "И даже слишком."
    mc "Мы сейчас сваримся заживо."
    mc "К слову, мне тоже стоит скинуть школьную форму..."
    mc "И надеть что-то лёгкое."
    mc "У тебя же тут есть...{w}э-э-э, футболки там...{w}шорты...{w}да?..."
    show monika curi mh eyes_tsed_1
    m "{cps=25}Разве это...{w}важно?{/cps}"
    show monika neut mh eyes_tsed_1
    m "{cps=25}Мы же ведь...{w}любим друг друга...{/cps}"
    show monika om
    mc "Моника, блин, ты меня начинаешь пугать."
    mc "Не слишком ли быстро ты {b}забегаешь вперёд{/b}?"
    mc "Да ещё в таком «неосознанном» состоянии..."
    show monika mh
    m "{cps=25}Макс...{/cps}"
    show monika om
    "Мне уже плохо от этого перегара."
    mc "Моника?"
    show monika mh ce
    m "{cps=25}Давай без...{w}лишних слов...{/cps}"
    show monika om
    "Она же сейчас не начнёт на полном серьёзе...{w}{b}это{/b}?"
    "Нет, я этого не позволю."
    "Что-то там у неё руками...{w}окей, но остальное...{w}эй, что за мысли, извращуга хренов?!"
    "ВЫ, БЛЯТЬ, ДВА УЧЕНИКА, У КОТОРЫХ НИЧЕГО НЕТ В ЭТОЙ ЖИЗНИ--{nw}"
    show monika mh oe
    m "{cps=25}Просто поцелуй меня.{/cps}"
    show monika om
    mc "Кхм..."
    show monika ce
    call window_close

    show layer master:
        pos (640, 360) anchor (0.5, 0.5)
        linear 8 zoom 4.0

    pause 4.0

    scene black with dissolve
    pause 1.0
    stop music
    play sound monika_nausea
    play music_none_loop music_stop
    pause 2.0

    call window_open
    mc "{cps=30}Твою ты мать, {/cps}{cps=50}к унитазу, СЕЙЧАС!{/cps}{w=0.75}{nw}"
    call window_close

    call plot_transition

    call window_open
    scene bg monika house livingroom day at monika_sofa
    show monika forward body worr cm ce n4 at e11
    with wipeleft_scene
    show monika om
    m "{cps=30}О-о-ох...{/cps}"
    show monika cm
    "Это было...{w}мерзко, но необходимо."
    "Но хотя бы успели..."
    show monika e1d
    mc "Полежи, тебе надо восстановиться."
    show monika om
    m "{cps=30}Н-нет, я...{w}лучше посижу...{/cps}"
    show monika ce
    m "{cps=30}Боюсь, что меня снова может стошни-и-ить...{/cps}"
    show monika mh
    m "{cps=30}Пха-а-а...{/cps}"
    show monika me
    mc "Как скажешь."
    "Кондей на всякий случай вырубил, чтобы Моника не простудилась."
    show monika om
    m "{cps=30}О-о-о...{/cps}"
    show monika me
    mc "Что случилось?"
    show monika om e1d
    m "{cps=30}Мне же...{w}ещё делать...{w}домашнее задание...{/cps}"
    show monika cm
    mc "И много?"
    show monika om oe
    m "{cps=30}Нет...{/cps}"
    show monika me
    mc "М-м-м..."
    show monika om ce
    m "{cps=30}Придётся...{w}что-то сказать учителям...{/cps}"
    show monika neut me e1d
    mc "Ох, Мони..."
    show monika oe
    mc "Я всё равно хотел сейчас закрыть свою работу, поэтому и тебе с этим помогу."
    show monika om
    m "{cps=30}П-правда?...{/cps}"
    show monika me
    mc "Да."
    show monika happ cm e1d b1b
    mc "Только переписать всё в тетради тебе придётся своим почерком, сама понимаешь..."
    mc "Но с твоим-то состоянием тебе придётся сделать это завтра утром."
    show monika om
    m "{cps=30}...спасибо, Макс...{/cps}"
    show monika cm
    mc "Пожалуйста."
    show monika -b1b
    mc "Всё-таки твоя «неформальная» рука, а?"
    show monika om ce
    m "{cps=30}Хе-хе-хе...{w}дам-дам я тебе...{w}э-э-э...{w}о-ф-и-ц-и-а-ль-н-у-ю роль.{/cps}"
    show monika cm
    mc "Да ладно, не надо."
    show monika eyes_tsed_1
    mc "Я и так у тебя в, кхм, «особом» статусе."
    show monika om
    m "{cps=30}Макс...{/cps}"
    show monika eyes_tsed_2
    m "{cps=30}Не разгоняй меня...{w}снова.{/cps}"
    show monika ce
    m "{cps=30}Я же ведь сорвусь и тебе мало не покажется~{/cps}"
    show monika cm
    "В таком состоянии Моника может сорваться разве что с дивана на пол..."
    show monika eyes_tsed_2
    mc "Если это поможет повторно прочистить твой желудок от всякой гадости, то почему нет?"
    show monika om ce
    m "{cps=30}Всё, ладно, хватит, ха-ха...{/cps}"
    show monika cm e1d
    mc "Кстати, пока не забыл."
    show monika neut cm e1d
    mc "Когда всё решу и напишу, то принесу тебе кусочек имбиря для облегчения."
    mc "Его Юри тебе через Сайори принесла."
    show monika om
    m "{cps=30}О-о...{/cps}"
    show monika e1b
    m "{cps=30}Понятно...{/cps}"
    show monika cm

    scene black with dissolve
    pause 0.25
    "Блин, нет, не могу..."
    "Сниму весь верх, иначе сдохну."
    mc "Мони, серьёзно, у тебя есть что-нибудь из одежды для меня?"
    mc "Если ты не против поделиться, конечно..."
    m "{cps=30}Это надо идти в мою спальню.{/cps}"
    m "{cps=30}Давай туда перейдём полностью.{/cps}"
    m "{cps=30}Там мягкая кровать и просторный стол...{/cps}"
    mc "Ну давай."
    mc "Она на втором этаже, да?"
    m "{cps=30}Да...{/cps}"
    mc "...эх."
    mc "Залезай на спину."
    m "{cps=30}Ха-ха, не понесёшь на руках?~{/cps}"
    mc "Так я навернусь по пути или тебя случайно ударю об какой-нибудь угол, или вообще укачаю."
    mc "Поэтому давай, аккуратно залезай мне на спину."
    mc "Постараюсь «понежнее» доставить тебя до кровати."
    m "{cps=30}Хе-хе-хе...{/cps}"
    "Какая же она...{w}чёрт, раскалённая..."
    call window_close

    call plot_transition
    pause 0.25

    call window_open
    "...ладно, зелёная кофта не такой уж и хреновый вариант..."
    "Вот правда всё равно какая-то лёгкая жара ощущается, хотя под кофтой больше ничего нет."
    mc "Фух..."
    "Как же хорошо, что сейчас меня, свободного от груза домашних заданий человека, идущего по лестнице с имбирём в руках и стаканом воды, никто, блин, не видит!"
    "Какой абсурд, чёрт побери!"
    "Хоть широкие штаны вместо чёрной юбки, и на том спасибо..."
    mc "Тьфу!"
    "А где-то там наверху сидит Моника в одних трусах, буквально."
    "Как вообще всё до этого дошло и как меня угораздило во всё это влипнуть?"
    "..."
    "Не хватало, чтобы она начала стих сочинять."
    "Я ж говорил, успокойся, отоспись."
    "Нет, всё равно: \"Стих...\", \"А как же стих?\""
    "Короче, пусть съест имбирь и уснёт."
    "Если понадобится, полежу вместе с ней."
    "Просто спать ещё не хочется: надо бы полазить в мобильнике, новости полистать и прочее..."
    "Так, вот и дверь."
    m "{cps=20}{size=16}...кровать, одеяло...{/size}{/cps}"
    m "{cps=20}{size=16}...атмо...{w}сфера!...{/size}{/cps}"
    mc "Не понял."
    m "{cps=20}{size=16}...очаро...{w}выва...{/size}{/cps}"
    mc "Ну, Моника!"
    "Откуда у тебя такой поэтический свербёж?!"
    call window_close

    play sound closet_open
    pause 0.5

    call window_open
    scene bg monika house bedroom night light with dissolve
    pause 0.25
    mc "Моника!"
    m "{cps=20}{size=19}О-ча-ро-вы-ва-ть и убега-а-ать...{/size}{/cps}"
    mc "Тебе отдых нужен!"
    m "{cps=20}{size=19}Ощу...{w}щ-щ-щ...{w}ще-е-е...{/size}{/cps}"
    mc "Ты всё равно в таком состоянии стих не составишь!"
    mc "Положи ручку!"
    m "{cps=20}{size=19}П-п-пейзаж!{/size}{/cps}"
    mc "Всё, хватит!"
    mc "Давай, на кровать, аккуратно!"
    m "{cps=20}Особенный папа!{/cps}"
    mc "Блин, уже накорябать что-то успела..."
    show monika forward body flus om ce n4 pants at t11
    m "{cps=20}Ё...{w}ё...{w}ё...{w}отхлё...{w}лё...{w}лё...{/cps}"
    mc "Мда, ты совсем скисла..."
    show monika neut om eyes_tsed_1 b1b
    mc "Моника, сядь на кровать, вот имбирь и стакан воды."
    show monika mh eyes_tsed_2
    m "{cps=20}Я уста-а-ала...{/cps}"
    show monika om
    mc "Я понимаю, но чуть-чуть ты должна откусить."
    show monika e4b
    m "{cps=20}Уф...{/cps}"
    show monika happ om ce brow
    m "{cps=20}А-а-ам~{/cps}"

    scene black with dissolve
    pause 0.25
    "..."
    mc "Вот так, молодец."
    mc "Запьёшь?"
    m "{cps=20}У, у.{/cps}"
    "Я до этого ей уже приносил попить, чтобы сгладить обезвоживание."
    "Возможно, поэтому не хочет."
    mc "Всё, а теперь можешь немного посидеть на кровати, чтобы переварить, так сказать, и лечь спать."
    mc "Сейчас 20 минут 9-ого вечера, времени отоспаться полно."
    mc "Я разбужу, если что."
    m "{cps=20}Умф...{/cps}"
    "И сразу легла..."
    mc "Я выключу свет."
    call window_close

    scene bg monika house bedroom night light with dissolve
    pause 1.0
    play sound light_turning_on
    scene bg monika house bedroom night 1
    pause 1.0

    call window_open
    "В общем, не похоже, что Монике стало значительно лучше, хотя большая часть токсинов и дерьма из неё точно вышли."
    mc "Бедная Моника..."
    "Вот именно поэтому и не надо пить алкоголь."
    "Одни проблемы от него..."
    "И ведь кто-то догадался выпить этот разбавленный яд и принять его за «праздничный» напиток, в то время как организм пытался вывести отраву всеми возможными способами."
    "Эх, никогда я людей не пойму."
    "Да и нет смысла."
    "Лучше заметочку в календарь накатаю..."
    call window_close

    call plot_transition(different_scene = False)

    call window_open
    scene bg monika house bedroom night 1 with wiperight
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 23,
            description = "Самый насыщенный день за последнее время: и весь клуб меня разбудил, и чуть кекс не украли, и с президентом Клуба выпечки конфликт устроили, и чаепитие с кексами провели, и даже разняли пьяных из-за вина Монику и Юри. Я взял заботу о похмелье первой на себя, а вторая осталась на обеспечении Сайори и Нацуки. Надеюсь, завтра им обеим станет лучше. Больше никакого алкоголя."
        )

        current_day = (23, _("ПН"))

    python in phone.system:
        battery_level = 81
        clock = (20, 26)

    show screen phone_calendars() with Dissolve(0.5)
    $ plot_pause()
    hide screen phone_calendars with Dissolve(0.5)

    window auto
    "Почему у меня заметки так криво формулируются?"
    "Это больше смахивает на набор бессвязных мыслей."
    m "{cps=30}{size=19}У-у-у...{w}м-м-м...{/size}{/cps}"
    "Блин, Моника постанывает во сне..."
    mc "Тихо-тихо-тихо-тихо..."

    scene black with dissolve
    pause 0.25
    "Поглаживание по голове, поглаживание по голове..."
    mc "Тс-с-с..."
    m "{cps=30}...ф-ф-ф...{/cps}"
    "Лучше лежать рядом с ней, мало ли..."
    m "{cps=30}......{/cps}"
    "Всё, успокоилась..."
    "Эх, Мони..."
    "Ты прямо вафелька."
    "И как же ты раньше жила одна?"
    "Тебя же ведь так не оставишь..."
    m "{cps=30}......{/cps}"
    "Ладно, попытаюсь ещё раз найти аккаунт психолога, а потом усну рядом в обнимку..."
    call window_close

    call nightmare_act_1_day_8
    $ _history_list.clear()

    call window_open
    scene bg monika house bedroom night 2 at monika_bed
    mc "{sc=3}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А--{/sc}{nw}" with shake(dist=40)
    mc "{sc=1.5}--а-а-а-а-а-а-а-а-а...{/sc}{nw}"
    mc "......"
    m "{cps=30}...м-м-м, Макс, что ты...{w}кричишь...{/cps}"
    m "{cps=30}...кругом люди спят...{/cps}"
    m "{cps=30}...подумаешь, спихнула тебя немного...{w}в сторону...{w}всем телом...{/cps}"
    mc "Так ты тут...{w}тут...{w}фу-у-у..."
    m "{cps=30}...умф-ф-ф, ч-что такое?...{/cps}"
    mc "Кошмар, Моника, кошмар!"
    mc "Опять дрянь какая-то приснилась."
    m "{cps=30}...у-у-у...{/cps}"
    m "{cps=30}...давай обниму...{/cps}"

    scene black with dissolve
    play sound hugs
    pause 1.0
    m "{cps=30}Вот...{w}так...{/cps}"
    m "{cps=30}У тебя...{w}сердце...{w}коло...{/cps}"
    mc "Меня ещё нервы не отпустили."
    m "{cps=30}...{/cps}"
    mc "Моника?"
    m "{cps=30}......{/cps}"
    "Уже уснула..."
    "Да что за издевательство надо мной происходит?!"
    "Откуда эти кошмары?!"
    "В честь чего?"
    "Зачем?!"
    "Никогда в своей жизни не было ничего подобного!"
    "..."
    mc "Пф-ф-ф..."
    "Ладно, медленное сердцебиение Моники начинает успокаивать."
    "..."
    "......"
    "Но сна ни в одном глазу."
    "И мобильника под рукой нет..."
    "И встать уже не могу, потому что Моника обвила меня рукой и ногой..."
    "Да ну ёб твою...{nw}"
    call window_close

    $ nightmare_active = False

    return
