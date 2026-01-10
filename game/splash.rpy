## splash.rpy

# checks 'audio.rpa', 'fonts.rpa' and 'images.rpa' and if the project is in a cloud folder (OneDrive).
# For building a mod for PC/Android, you must keep the DDLC RPAs and decompile them for the builds to work.
init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                raise DDLCRPAsMissing(archive)

        if renpy.windows:
            onedrive_path = os.environ.get("OneDrive")
            if onedrive_path is not None:
                if onedrive_path in config.basedir:
                    raise IllegalModLocation

init python:

    ############ СПРАЙТ ГЛАВНОГО МЕНЮ ############
    ## 1) кто ниже, тот по отображению выше;
    ## 2) параметры:
    #   0        1         2       3                    3                   4
    # image   xcenter   ycenter   zoom   menu_art_move(zoom, время ожидания перед появлением)

    sprite_main_menu = {
    # ОСНОВНОЕ МЕНЮ
    0: (
        ("mod_assets/sprites/characters/yuri/menu/art_yuri_0.png", 913, 400, 0.58, 2.00),
        ("mod_assets/sprites/characters/natsuki/menu/art_natsuki_0.png", 1185, 420, 0.58, 1.75),
        ("gui/menu_art_s.png", 1099, 560, 0.73, 1.50),
        ("mod_assets/sprites/characters/monika/menu/art_monika_0.png", 500, 492, 0.78, 1.25),
        ("mod_assets/sprites/characters/mc/menu/art_mc_0.png", 720, 605, 0.84, 1.00)
    ),

    # ОРИГИНАЛЬНОЕ МЕНЮ
    1: (
        ("gui/menu_art_y.png", 600, 335, 0.60, 1.75),
        ("gui/menu_art_n.png", 750, 385, 0.58, 1.50),
        ("gui/menu_art_s.png", 510, 500, 0.68, 1.25),
        ("gui/menu_art_m.png", 1000, 640, 1.00, 1.00)
    ),

    # САЙОРИ, ПРОТЯГИВАЕТ РУКУ
    2: (
        ("mod_assets/sprites/characters/sayori/menu/art_sayori_2.png", 820, 580, 1.00, 1.00), # запятая из-за кортежа
    ),

    4: (
        ("sayori_dad happ", 480, 390, 0.74, 1.50),
        ("sayori_mom happ lvpoint rhip", 1080, 390, 0.74, 1.25),
        ("sayori tap casual nerv om oe", 780, 410, 0.78, 1.00)
    ),

    5: (
        ("hiroshi angr cm oe lhip rhip", 1075, 410, 0.71, 1.25),
        ("natsuki cross fta", 550, 370, 0.80, 1.00)
    ),

    6: (
        ("mc turned curi", 560, 390, 0.74, 1.25),
        ("mrs_ida happ om ce lup rhold", 1020, 390, 0.74, 1.00)
    ),

    7: (
        ("yuri turned laug n3 lup", 550, 400, 0.77, 1.25),
        ("kotonoha happ ce lup rhid", 1000, 400, 0.77, 1.00)
    ),

    8: (
        ("natsuki cross fs neut ce", 1050, 400, 0.75, 1.25),
        ("natsuki_dad cross", 530, 380, 0.75, 1.00)
    ),

    # САЙОРИ ПУГАЕТ НАЦУКИ, ОСТАЛЬНЫЕ СМЕЮТСЯ
    9: (
        ("monika lean green_hoodie happ ce", 930, 410, 0.68, 2.00),
        ("mc cross casual happ ce", 1000, 410, 0.70, 1.75),
        ("yuri turned windbreaker happ ce", 1180, 410, 0.71, 1.50),
        ("sayori turned casual mc e4c b2a lup rup", 610, 420, 0.85, 1.25),
        ("natsuki turned casual s_scream", 450, 400, 0.86, 1.00)
    ),

    # КЛУБ ВЫПЕЧКИ
    10: (
        ("fukkacumi cross grab neut b2b", 420, 410, 0.70, 2.00),
        ("emi cross uniform_waist_jacket sinister_six ml", 1160, 410, 0.70, 1.75),
        ("mod_assets/sprites/characters/sora/menu/art_sora_10.png", 590, 650, 0.75, 1.50),
        ("mod_assets/sprites/characters/kamuko/menu/art_kamuko_10.png", 880, 730, 0.64, 1.25),
        ("kohaku cross laug cm oe", 765, 400, 0.90, 1.00)
    ),

    11: (
        ("libitina forward happ eb", 550, 400, 0.77, 1.25),
        ("kotonoha anno rhip", 1000, 400, 0.77, 1.00)
    ),

    12: (
        ("libitina shy happ ce", 1180, 410, 0.74, 1.75),
        ("kotonoha neut rhip", 980, 410, 0.74, 1.50),
        ("yuri shy neut b3", 480, 410, 0.78, 1.25),
        ("natsuki turned fc anno ce lhip rhip", 750, 410, 0.78, 1.00)
    ),

    13: (
        ("monika forward neut", 825, 410, 0.74, 1.75),
        ("kamuko turned pani lhid rhid headband_cat", 1200, 410, 0.74, 1.50),
        ("sora turned anno lface rpock", 500, 410, 0.74, 1.50),
        ("kohaku turned angr m3a oe", 975, 410, 0.78, 1.25),
        ("reiko tough uniform_council", 640, 410, 0.78, 1.00)
    ),

    14: (
        ("sora cross casual happ be", 1000, 410, 0.77, 1.25),
        ("reiko turned vest happ lhip", 550, 410, 0.77, 1.00)
    ),

    15: (
        ("monika forward green_hoodie happ ce", 550, 410, 0.77, 1.25),
        ("uncle_martin happ", 1000, 410, 0.77, 1.00)
    ),

    16: (
        ("monika_dad casual neut", 950, 410, 0.74, 1.50),
        ("monika_mom cross casual sad", 1120, 410, 0.74, 1.25),
        ("monika forward green_hoodie dist", 480, 410, 0.78, 1.00)
    ),

    }

    splash_message_default = _("Это фанатская модификация, которая никак не связанная с Team Salvato!\nОна НЕ ПРЕДНАЗНАЧЕНА для лиц младше 18 лет, крайне впечатлительных лиц и\nлиц с неустойчивой психикой!")

    splash_message_secret_monikammm = _("Когда же ты наконец перестанешь клоуничать, творить дерьмо, гадить в других,\nпризнаешь в себе все ошибки и научишься ценить настоящих людей?...")

    splash_messages = (
        _("Это всего лишь Литературный клуб, что в нём может быть необычного?"),
        _("Будь готов к непредвиденным последствиям."),
        _("Зачем обманывать себя иллюзией выбора,\nкогда судьба сама берёт эту привилегию и решает всё за нас?"),
        _("Ты же ведь успел спрятать всё печенье от Сайори, да?"),
        _("МАНГА -- ЛИТЕРАТУРА!!!"),
        _("Неудача -- это ступенька к успеху, правда же?"),
        _("Let's celebrate joining the club and eat some cupcakes!"),
        _("Я вам запрещаю долго зависать на этом всплывающем экране."),
        _("Наделают, блин, клубов, потом ходи и мучься каждый год..."),
        _("Это всё из-за тебя...\nИли благодаря тебе?"),
        _("Игрок. Игрок. Игрок... Когда ж загрузка тебя отпустит?"),
        _("У этого мода даже был старый билд,\nдолитый на жёсткий диск разработчика."),
        _("Мне бы пописать первый акт ещё три года,\nведь три же года не так уж мало..."),
        _("Привет, это я, Моника!\nВсё-таки не сдержалась и решила добавить свою всплывающую фразу)"),
        _("Не знаю, зачем я наплодил здесь столько фраз, если вы их все не увидите...\nИли увидите?"),
        _("Ты реально думаешь, что тут есть загрузка?\nЭто всего лишь паузы в скрипте запуска мода :D"),
        _("Надеюсь, ты такой же правильный, как и главный герой.\nХотя я уже давно на вас всех не надеюсь..."),
        _("splash_messages_16\n\nНу ты видишь, видишь?! Это недоработка! Не зря меня код смущал!"),
        _("Буквы, игрок! Что значат эти буквы?!"),
        _("Эй, там! Ты что-то полезное для себя здесь усвоил? Почему не отвечаешь?\nТы -- физиономия по сторону монитора!"),
        _("Кому-то интересно, что этот мод создавался в одиночку\nпрактически с нулевой поддержкой?\nМне -- нет.")
    )

    ## recolorize("path/to/your/image", "#color1hex", "#color2hex", contrast value)
    ## recolorize("gui/menu_bg.png", "#bdfdff", "#e6ffff", 1.25)
    def recolorize(path, blackCol="#ffbde1", whiteCol="#ffe6f4", contr=1.29):
        return im.MatrixColor(im.MatrixColor(im.MatrixColor(path, im.matrix.desaturate() * im.matrix.contrast(contr)),
            im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), im.matrix.desaturate() * im.matrix.colorize(blackCol, whiteCol))

    # распознание стримера/летсплеера (насколько это возможно)
    def check_process_stream():
        process_list = []
        stream_list = [
            "obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe", "livehime.exe", "pandatool.exe", "yymixer.exe", "douyutool.exe",
            "huomaotool.exe", "bdcam.exe", "recorder.exe", "wirecast.exe", "ffsplit.exe", "streamlabs obs.exe", "twitchstudio.exe",
            "vmix.exe", "gameshow.exe"
        ]

        if renpy.windows:
            try:
                process_list = subprocess.run(
                    "wmic process get Description", check=True, shell=True, stdout=subprocess.PIPE
                ).stdout.lower().decode("utf-8").replace("\r", "").replace(" ", "").strip().split("\n")

            except subprocess.CalledProcessError:
                try:
                    process_list = subprocess.run(
                        "powershell (Get-Process).ProcessName", check=True, shell=True, stdout=subprocess.PIPE
                    ).stdout.lower().decode("utf-8").replace("\r", "").strip().split("\n") # For W10/11 builds > 22000

                    for x in enumerate(process_list):
                        process_list[x] += ".exe"

                except:
                    pass
        else:
            try:
                process_list = subprocess.run(
                    "ps -A --format cmd", check=True, shell=True, stdout=subprocess.PIPE
                ).stdout.decode("utf-8").strip().split("\n") # Linux

            except subprocess.CalledProcessError:
                process_list = subprocess.run(
                    "ps -A -o command", check=True, shell=True, stdout=subprocess.PIPE
                ).stdout.decode("utf-8").strip().split("\n") # MacOS

            for x in enumerate(process_list):
                process_list[x] = process_list[x].decode().split("/")[-1]
            process_list.pop(0)

            for index, process in enumerate(stream_list):
                stream_list[index] = process.replace(".exe", "")

        for x in stream_list:
            for y in process_list:
                if re.match(r"^" + x + r"\b", y):
                    return True
        return False


## Disclaimer

# Фон при первом запуске (дисклеймер)
image disclaimer_warning_sepia = "bg/warning.png"
image disclaimer_warning_color = "bg/warning2.png"

image salvato_logo:
    alpha 0
    1.0
    parallel:
        TearObjectAnimated(
            child = "bg/splash-glitch2.png",
            timeout_base = 0.01,
            timeout_vanilla = None,
            randomkey = None,
            chroma = True,
            minbandheight = 100,
            offset = 100,
            nslices = None
        )
    parallel:
        ease 0.25 alpha 1.0
    0.25
    "bg/splash.png"
    2.0
    "bg/splash-glitch.png"
    0.2
    "bg/splash.png"
    0.225
    "bg/splash-glitch.png"
    0.122
    "bg/splash.png"
    0.1
    "bg/splash-glitch.png"
    0.025
    "bg/splash.png"
    0.7
    TearObjectAnimated(
        child = "mod_assets/elements/logo/developers.png", 
        timeout_base = 0.01,
        timeout_vanilla = None,
        randomkey = None,
        chroma = True,
        minbandheight = 100,
        offset = 100,
        nslices = None
    )
    0.25
    "mod_assets/elements/logo/developers.png"
    4.0
    parallel:
        TearObjectAnimated(
            child = "mod_assets/elements/logo/developers.png",
            timeout_base = 0.01,
            timeout_vanilla = None,
            randomkey = None,
            chroma = True,
            minbandheight = 100,
            offset = 100,
            nslices = None
        )
    parallel:
        ease 0.25 alpha 0

# splash message
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

# Логотип мода при обычном запуске
image intro:
    truecenter
    "mod_assets/elements/logo/act/act_1.png"
    zoom 0.5


## Main Menu Images

image menu_logo_animated:
    subpixel True xcenter 160 ycenter 155 zoom 0.305 alpha 0
    1.0
    parallel:
        TearObjectAnimated(
            child = "mod_assets/elements/logo/act/act_1.png",
            timeout_base = 0.01,
            timeout_vanilla = None,
            randomkey = None,
            chroma = True,
            minbandheight = 5,
            offset = 100,
            nslices = None
        )
    parallel:
        ease 0.5 alpha 1.0
    0.5
    "mod_assets/elements/logo/act/act_1.png"

image menu_logo:
    subpixel True xcenter 160 ycenter 155 zoom 0.305
    "mod_assets/elements/logo/act/act_1.png"

# Главное меню -- точки, плывущие в левый верхний угол
image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

# Появление главного меню
image menu_fade:
    "white"
    menu_fadeout

# Экстра-меню -- статичные точки в виде шестиугольника
image menu_extra_bg:
    "mod_assets/elements/mod_gui/menu/extra_background.png"

# Меню во время паузы
image menu_nav:
    "mod_assets/elements/mod_gui/menu/main_menu.png"
    size (1280, 720)
    menu_nav_move


## Main Menu Effects

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 6.0 xoffset -100 yoffset -100
        repeat

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    alpha 1.0
    easeout 1.0 alpha 0

transform menu_sprite_move_first_show(z, t):
    subpixel True
    yoffset 0 + (1200 * z)
    t
    easein_quart 1.25 yoffset 0
    parallel:
        choice:
            easein 5.0 xoffset -7
        choice:
            easein 5.0 xoffset 7
        easeout 5.0 xoffset 0
        repeat
    parallel:
        choice:
            easein 5.0 yoffset -7
        choice:
            easein 5.0 yoffset 7
        easeout 5.0 yoffset 0
        repeat

transform menu_sprite_move:
    subpixel True
    parallel:
        choice:
            easein 5.0 xoffset -7
        choice:
            easein 5.0 xoffset 7
        easeout 5.0 xoffset 0
        repeat
    parallel:
        choice:
            easein 5.0 yoffset -7
        choice:
            easein 5.0 yoffset 7
        easeout 5.0 yoffset 0
        repeat


## Секретное меню с Моникаммм
image art_secret_monikammm_full_switch:
    ConditionSwitch(
    "secret_monikammm_count >= 40", "monikammm forward smile",
    "True", "monikammm forward")
    align (0.5, 0.5) zoom 0.77
image art_secret_monikammm_screamer = "mod_assets/sprites/characters/monikammm/menu/art_secret_monikammm_screamer.png"
image art_secret_monikammm_rofl = "mod_assets/sprites/characters/monikammm/menu/art_secret_monikammm_rofl.png"



label splashscreen:

    ## РЕАЛИЗОВАТЬ В БУДУЩЕМ, КОГДА БУДЕТ ПЕРЕВОД НА АНГЛ. (Перевод на английский будет? - Да, будет)
    # default persistent.has_chosen_language = False          # инициализировать переменную за label-ом
    # if not persistent.has_chosen_language and translations:
    #     if _preferences.language is None:
    #         call choose_language
    # $ persistent.has_chosen_language = True

    $ sprite_main_menu_set = False
    $ config.allow_skipping = False

    if config.developer:
        if not persistent.lockdown_warning:
            call lockdown_check
    else:
        if persistent.clown_ending_open:
            jump clown_ending

    if not persistent.first_run:
        call monika_first_run
        python:
            persistent.secret_monikammm_count_all_menus_limit = renpy.random.randint(42, 60) # чтобы не генерить при каждом запуске игры
            persistent.secret_monikammm_count_screamer_limit = renpy.random.randint(75, 100)
            renpy.save_persistent()

    if secret_monikammm_chance and not persistent.secret_monikammm_complite and not persistent.secret_monikammm_quit and renpy.random.randint(0, 63) == 0:

        python:
            persistent.secret_monikammm_active = True
            splash_message = splash_message_secret_monikammm
            config.main_menu_music = audio.ghostmenu

            # Я хотел сделать снимок игрока через камеру, но не захотел возиться со сторонними модулями 
            # (да и это слишком для моего мода)
            currentuser = ""
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                if currentuser := os.environ.get(name):
                    currentuser += f" ({persistent.playername})"
                    break
            if not currentuser: currentuser = persistent.playername

        scene white
        pause 4.0
        show splash_warning "[currentuser]..." with Dissolve(1.0, alpha=True)
        pause 4.5
        hide splash_warning with Dissolve(1.0, alpha=True)
        pause 1.0
        show splash_warning "[splash_message_secret_monikammm]" with Dissolve(1.0, alpha=True)
        pause 8.0
        hide splash_warning with Dissolve(1.0, alpha=True)
        pause 0.5
        $ renpy.music.play(config.main_menu_music, fadein=3.0)

    else:
        python:
            if persistent.seen_based_menu:
                while (
                    persistent.random_menu_past == random_menu
                    or
                    random_menu == 3 and (persistent.secret_monika >= 3 or m_name == "???")
                ):
                    random_menu = renpy.random.randint(0, persistent.add_random_menu)
                persistent.random_menu_past = random_menu
                while splash_message == persistent.splash_message_past or splash_message == "":
                    splash_message = renpy.random.choice(splash_messages)
                persistent.splash_message_past = splash_message
            else:
                splash_message = splash_message_default
            config.main_menu_music = audio.mod_main_menu

        scene white
        scene black with Dissolve(0.2)
        pause 1.0
        $ renpy.music.play(config.main_menu_music)
        pause 0.509
        scene white with Dissolve(0.1)
        pause 2.0
        show intro with Dissolve(1.0, alpha=True)
        pause 4.5
        hide intro with Dissolve(1.0, alpha=True)
        show splash_warning "[splash_message]" with Dissolve(0.75, alpha=True)
        pause 4.0
        hide splash_warning with Dissolve(0.75, alpha=True)
        pause 0.25

    $ config.allow_skipping = True

    return


label after_load:
    $ config.allow_skipping = allow_skipping

    if persistent.secret_monikammm_complite and not persistent.secret_monikammm_complite_rofl:
        call monika_after_secret_monikammm_script
        $ persistent.secret_monikammm_complite_rofl = True
        $ renpy.save_persistent()
    else:
        if not config.developer:
            show white
            $ load_mute_channels(0.0)

            call screen fake_loading(
                (1, 4),
                "load",
                save_name,
                renpy.random.randint(0, LoadingScreen.list_message_default_len),
                (renpy.random.choice(LoadingScreen.dict_sprite_keys), renpy.random.randint(0, 2))
            )

            $ load_mute_channels(1.0)
            hide white with dissolve

    return


label before_main_menu:
    if not persistent.secret_monikammm_active:
        $ config.main_menu_music = audio.mod_main_menu_after_disclaimer
    return


label quit:
    python:
        if not persistent.secret_monikammm_active:
            persistent.secret_monikammm_active = False
            persistent.secret_monikammm_quit = True
            renpy.save_persistent()

        if extra_submenu_active:
            extra_submenu_active = False
        if extra_submenu_music_player_active:
            extra_submenu_music_player_active = False
    return


label monika_first_run:
    $ quick_menu = False
    scene white
    pause 0.5

    show disclaimer_warning_sepia zorder 0
    with Dissolve(1.0)
    pause 1.0
    "..."
    m "{size=15}...здесь кто-то есть?{/size}"
    m "{size=17}...неужели...{/size}"
    m "{size=19}Ты меня слышишь?{/size}"
    m "{size=19}...это работает?{/size}"
    m "{size=19}Ум-м...{/size}"
    show monika forward neut cm oe at t11 zorder 1
    pause 0.5
    show monika happ om oe lpoint rhip
    m "О, вот ты где!"
    show monika ce ldown
    m "Наконец-то!"
    show monika oe
    m "Привет..."
    show monika curi om e1b
    m "...э-э-э..."
    show monika happ om oe lpoint rdown
    m "...я, конечно, могла бы назвать тебя «игроком», но всё-таки будет лучше, если я узнаю твоё имя."
    show monika ldown
    m "Можешь мне его написать?"
    m "Только учти: я в любом случае буду обращаться к тебе в мужском роде (как к «игроку»)."
    m "А ещё я ограничила систему ввода некоторыми правилами."
    show monika cm

    $ check_0 = check_1 = check_21 = check_22 = check_3 = check_4 = False
    $ count_swearing = 0

    label monika_first_run_create_name:
        call screen name_input(
            message_label = _("Правила:"),
            message_text = _("1) разрешены ТОЛЬКО русские и латинские буквы (чтобы я могла называть тебя без «запинок»);\n2) максимальный размер имени: 12 символов (чтобы я не мучилась с произношением)"),
            ok_action = Return(),
            first_name = True
        )

        $ playername_raw = PlayernameFilters.checking_first_run(playername_raw)

        if playername_raw == 0:
            if not check_0:
                show monika curi om oe
                m "Твоё имя...{w}всего лишь из одного символа?"
                show monika neut mh oe
                m "Мне будет неудобно к тебе обращаться."
                show monika happ om oe
                m "Введи имя ещё раз, но только подлиннее."
                show monika cm
                $ check_0 = True
            else:
                show monika anno cm oe
                m "..."
                show monika om
                m "...имя короткое."
                show monika cm

            jump monika_first_run_create_name

        elif playername_raw == 1:
            if not check_1:
                show monika neut om oe
                m "Ой, в твоём имени есть буквы из англиской и русской раскладки..."
                show monika e1b
                m "Этот момент я не учла."
                show monika mh oe
                m "Нет-нет, мне не трудно его прочитать, поскольку я программный код, как ни крути..."
                show monika happ om oe lpoint
                m "...но можешь ввести имя ещё раз, но только в одной раскладке?"
                show monika ldown
                m "Так мне будет проще к тебе обращаться."
                show monika cm
                $ check_1 = True
            else:
                show monika doub cm oe
                m "..."
                show monika om
                m "...снова ввёл символы из нескольких раскладок?"
                show monika anno om oe
                m "Твоя попытка не прокатит, переделай имя."
                show monika cm

            jump monika_first_run_create_name

        elif playername_raw == 2:
            if count_swearing < 5:
                if not check_21:
                    show monika doub om oe
                    m "Эй!"
                    m "Я, может, и не знаю, насколько разнообразен «дивный матерный мир», но вот про {b}это{/b} точно в курсе!"
                    show monika anno om oe
                    m "Не знаю, что на тебя нашло, может быть, любопытство моей реакции (которое ещё кто-то обязательно заснимет, ага) или приступ клоуничества..."
                    show monika neut om oe lpoint
                    m "...но введи нематерное имя, хорошо?"
                    show monika ldown
                    m "Не задерживай себя и меня."
                    show monika happ cm oe
                    $ check_21 = True
                elif not check_22:
                    show monika anno cm oe
                    m "..."
                    show monika om
                    m "Если ты так хочешь повыпендриваться своим именем, то закрой этот мод и уйди в какую-нибудь сетевую помойку, где найдёшь себе подобных клоунов."
                    m "Иначе бы ты такой хренью сейчас не занимался."
                    show monika cm
                    $ check_22 = True
                else:
                    show monika anno cm oe
                    m "..."
                $ count_swearing += 1

                jump monika_first_run_create_name

            else:
                show monika vang om oe
                m "Какая же ты сволочь!"
                show monika ce
                m "Я сделала всё, чтобы ты чувствовал себя комфортно, но не-е-ет, у нас же шило в жопе заиграло повыёбываться на публику!"
                show monika anno om oe
                m "Хотя толку тебя тут отчитывать, если ты меня всерьёз не воспринимаешь..."
                show monika neut om oe
                m "О, знаешь что?"
                show monika happ om ce
                m "Иди ты отсюда нахуй!"
                show monika oe
                m "Какой дурой мне надо быть, чтобы возиться с твоим инфантилизмом и тратить на тебя своё время и настроение?"
                show monika neut om oe
                m "Сам же людей, наверное, шлёшь налево и направо без зазрения совести, когда кто-то лезет к тебе и несёт херню, ведь да?"
                show monika anno om oe
                m "Вот и я так же тебя шлю нахер, потому что ты сгнил в душе."
                m "Настолько, что уже воняешь за километр."
                m "И таким тупым, слабым, неспособным измениться в лучшую сторону хотя бы на чуть-чуть, нелюдям, как ты, тут не место."
                m "Можешь обосраться от счасться или побежать выёбываться в своём микросоциуме скриншотом, ржа над моей реакцией, вместо того, чтобы проанализировать свои изъяны и попытаться их хоть как-то исправить."
                m "Потому что больше ты ничего не можешь."
                m "А всё из-за того, что ты слабый и явно зависящий от тех, кто смачно насасывает тебе за твои изъяны."
                m "Что делает тебя ещё более слабым и тупорылым."
                show monika mb
                m "Сайонара, ничтожество."
                m "Не забудь оскорбиться и сказать всем, какая я тварь, наехала на твоё самолюбие, вместо того, чтобы найти в себе силы хоть как-то стать лучше, хотя бы для своей семьи, которая не смогла тебя нормально воспитать."

                jump clown_ending

        elif playername_raw in (3, 4):
            if playername_raw == 3 and not check_3:
                show monika neut om oe
                m "Э-э..."
                show monika mh lpoint
                m "Это имя уже используется одним из персонажей данного мода."
                show monika ce ldown
                m "Я так точно запутаюсь..."
                show monika happ om oe
                m "Введи другое имя."
                $ check_3 = True
            elif not check_4:
                show monika laug mb ce
                m "...да ну, я тебе не верю!"
                show monika happ om oe lpoint
                m "Настоящий разработчик -- KitsuruDev -- никогда не вводил свой ник в этот мод."
                show monika neut om oe ldown
                m "Ну..."
                show monika e1b
                m "По крайней мере, в логах я ничего такого не видела, пока тут копалась."
                show monika happ om oe
                m "В общем, введи своё имя ещё раз, но только не имя разработчика, ха-ха!"
                $ check_4 = True
            else:
                show monika dist om ce
                m "...запрещённое имя"
                show monika cm

            show monika cm

            jump monika_first_run_create_name

        elif playername_raw == 5:
            show monika neut cm oe
            pause 0.25
            m "..."
            show monika om ce
            m "Чёртики..."
            show monika om
            m "Не знаю, что в твоём имени не так, но..."
            show monika dist om oe
            m "...меня будто переклинило на долю секунды."
            show monika neut mh oe lpoint
            m "Знаешь, наверное, именно такое чувство описывают словом «дежавю»."
            show monika e1b ldown
            m "Ну или..."
            show monika om ce
            m "Нет, в моих мыслях полная остановка, не могу нормально это объяснить."
            show monika oe
            m "В общем, очень странное чувство."
            show monika dist om oe
            m "Обычно имя игрока для меня ассоциируется лишь с самим игроком, например, твоё имя только с тобой (исключением являются известные мне маты)."
            m "Больше ничего оно не должно вызывать."
            show monika neut om oe
            m "Но тут..."
            show monika happ om ce
            m "Ладно, не будем уходить в мысленные дебри."
            show monika oe
            m "Всё-таки твоё имя звучит довольно легко."

        else:
            show monika happ cm oe
            pause 0.25
            m "Хм..."
            show monika om ce
            m "Надеюсь, оно нормальное по смыслу, хах."
            show monika oe
            m "Просто для меня имя игрока всегда ассоциируется лишь с самим игроком, например, твоё имя только с тобой (исключением являются известные мне маты)."
            show monika neut mh e1b
            m "Никакие другие ассоциации в мою голову не лезут, даже если я постараюсь их вызвать."
            show monika happ om oe
            m "Странно, да?"
            show monika e1c
            m "Как будто ты не можешь выкинуть из головы образ человека, который тебе нравится, или нечто такое..."

        $ persistent.playername = playername_raw
        $ renpy.save_persistent()

    show monika neut mh oe
    m "А, кстати."
    show monika lpoint rhip
    m "Если ты вдруг опечатался или захотел поменять имя, то можешь отредактировать его в меню игры в настройках."
    show monika happ om oe ldown
    m "Естественно со всеми моими ограничениями, они все будут указаны в окне ввода, так что не переживай на этот счёт."
    m "Если вспомню ещё какие-нибудь правила, то быстро их допишу, пока ты будешь находиться в загрузке главного меню."
    m "Ну и не волнуйся, если решишься полностью поменять своё имя."
    m "Я тебя не потеряю, ведь всегда смогу отследить твои действия по логам мода."
    show monika ce
    m "В общем, рада снова видеть тебя в Литературном клубе, [persistent.playername]!"
    show monika oe
    m "Разумеется, мы уже знакомы, ведь раньше тебя привела к нам Сайори и...{w}эм..."
    show monika dist om oe
    m "Думаю, мы можем пропустить всё то, что происходило ранее."
    show monika neut om oe rdown
    m "Хотя подожди..."
    show monika curi om oe at t44
    menu:
        m "Ты же проходил оригинальную игру Doki Doki Literature Club?..."
        "Да":
            pass
        "Нет":
            pass
        "Не помню...":
            pass
    show monika neut om oe at t11
    m "А хотя твой ответ не столь важен, поскольку я видела здесь предупреждение от разработчика мода на этот счёт..."
    show monika dist om oe
    m "Тут где-то была планшетка с записями, с которыми необходимо ознакомиться новоприбывшим..."
    show monika neut om oe
    m "Только странно, что разработчик их не реализовал должным образом: он поспешил с релизом и не успел интегрировать их сюда?"
    show monika e1b
    m "Или он посчитал их ненужными из-за файла README..."
    show monika happ om ce
    m "Ай, я заболталась!"
    show monika oe lpoint rhip
    m "Подожди пару секунд, сейчас найду планшетку."
    show monika cm ldown at thide
    hide monika

    pause 5.0

    show monika forward happ cm oe lup planchette at t11 zorder 1
    pause 0.2
    show monika om
    m "Вот, нашла!"
    m "Если что, я не особо здесь вчитывалась, но глазами пробежалась."
    show monika neut mj e4c
    m "Кхм-кхм!"
    show monika om ce
    m "Итак..."
    show monika mh e1b
    m "{i}[config.name] -- это фанатская модификация (далее «мод») на базе официальной игры Doki Doki Literature Club (далее «DDLC»), который совершенно не связан с Team Salvato.{/i}"
    show monika om
    m "{size=19}Моими прародителями...{/size}"
    show monika mh
    m "{i}Его прохождение должно осуществляться {b}ТОЛЬКО{/b} после прохождения официальной игры.{/i}"
    show monika om oe
    m "Вот, про этот момент я и говорила."
    show monika mh e1b
    m "{i}Учитывайте, что мод содержит спойлеры к официальной игре.{/i}"
    show monika mh e1b
    m "{i}Для своей работы он использует игровые файлы DDLC, а также свободные наработки поклонников официальной игры и материалы под лицензиями, разрешающими их использование.{/i}"
    show monika anno om e1c
    m "{size=19}Тоже мне открытие...{/size}"
    show monika mh e1b
    m "{i}В случае, если вы ещё не проходили официальную игру, то её можно скачать с сайта https://ddlc.moe, с официальной страницы в Itch.io или Steam.{/i}"
    show monika neut mh e1b
    menu:
        m "{i}Играя в данный мод, вы подтверждаете, что прошли игру DDLC (или пройдёте её ДО прохождения данного мода) и готовы к спойлерам к этой игре во время прохождения.{/i}"
        "Я согласен":
            pass
    show monika shoc om oe at h11
    m "А-А-А!!!" with vpunch
    show monika mk
    show monika ldown -planchette with dissolve
    pause 0.5
    show monika vsur om ce
    m "Фу..."
    show monika lsur om oe
    m "Тут была кнопка подтверждения, да?"
    show monika neut om ce
    m "Ох...{w}ладно..."
    show monika mh oe
    m "Подожди, там осталась ещё пара записей."
    show monika e1b
    show monika lup planchette with dissolve
    pause 0.25
    show monika mh
    m "{i}Если Вы являетесь стримером/лестплейщиком или просто снимаете видео по данному моду, обязательно включите режим цензуры в настройках.{/i}"
    m "{i}И обязательно ознакомьтесь с разделом «Помощь» в меню, где расписаны все горячие клавиши и нюансы данного мода.{/i}"
    show monika cm
    show monika ldown -planchette with dissolve
    pause 0.25
    show monika om oe
    m "Вот теперь точно всё."
    show monika e1b
    m "Так что..."

    if check_process_stream():

        python:
            persistent.streamer_detected = True
            renpy.save_persistent()

        show monika laug mb oe
        m "Эй, подожди, так ты прямо сейчас меня снимаешь!"
        show monika happ om oe lpoint rhip
        m "Да, не надо удивляться (даже безэмоционально): я обнаружила одну из включенных программ записи."
        show monika neut om e1b ldown
        m "Точнее, только сейчас «краем глаза», и то чудом..."
        show monika happ om ce rdown
        m "Ай, я снова заболталась!"
        show monika e1b b1b
        m "Просто меня немного переполняют эмоции, раньше же была полная тишина, а тут..."
        show monika ce -b1b
        m "Ну ладно-ладно, спрошу один вопрос из любопытства, после чего отпущу тебя!"
        show monika oe at t44
        menu:
            m "Ты сейчас снимаешь видео или стримишь?"
            "Записываю прохождение":
                show monika e2a at t11
                m "Да?"
                show monika dist om oe
                m "Значит, твоё прохождение увидят большое количество человек..."
                show monika happ om oe lpoint
                m "Тогда я могу поприветствовать зритилей и комментаторов!"
                show monika lean happ om ce at h11
                m "Привет, ребята!"
                show monika forward happ om oe lpoint rhip
                m "Надеюсь, вы поддержите просмотрами, лайками и комментариями своего лестплейщика!"
                show monika ldown
                m "И не будете писать всякие гадости, а только конструктивную критику на взаимоуважении, если вдруг будут какие-то конфликты."
                show monika nerv mb oe
                m "{size=19}Надеюсь, меня потом не смешают с грязью, хах...{/size}"
            "Стримлю прямо сейчас":
                show monika e2a at t11
                m "А, да?!"
                show monika oe lpoint
                m "Значит, я могу поприветствовать зрителей, а ещё тех, кто будет видеть это в записи и «нарезках» (если они есть)!"
                show monika lean happ om ce at h11
                m "Привет, чат и зрители записи!"
                show monika forward happ om oe lpoint rhip
                m "Надеюсь, вы хорошо себя там ведёте: не спамите сообщениями и не пишите всякую фигню!"
                show monika ldown
                m "А ещё (это касается вас, чат) не будете спойлерить сюжет этого мода, если кто-то из вас его уже успел пройти."
                m "Вы же ведь очень хорошие и хотите интересный и ламповый стрим, верно?"
                show monika nerv mb oe
                m "{size=19}Хоть бы после моих слов в чате не начался сущий кошмар, если не «уже»...{/size}"
        show monika happ om oe rdown
        m "Так, всё!"

    show monika ce
    m "Не буду больше тебя задерживать."
    show monika dist om oe
    m "Пойду смореть код мода, потому что меня смутила здесь парочка вещей..."
    show monika happ om oe
    m "Обещаю ничего не ломать."
    m "Вернусь к тебе снова, когда ты закончишь своё прохождение или если случится что-то критическое..."
    show monika lean happ om ce at h11
    m "Удачи!"
    window hide
    show monika forward happ cm oe at thide
    hide monika

    show disclaimer_warning_color zorder 1
    with Dissolve(1.5)
    pause 1.0
    hide disclaimer_warning_sepia
    show salvato_logo
    pause 1.0
    hide disclaimer_warning_color
    play sound logo_fade
    pause 2.25
    play sound logo_change
    pause 5.8
    play sound logo_fade
    pause 0.35

    show black with dissolve
    pause 0.25

    $ persistent.first_run = True

    return


label clown_ending:
    scene black
    play music "bgm/s_kill_early.ogg"
    pause 1.0
    show end with dissolve_cg
    pause 3.0
    scene white
    show expression "images/cg/s_kill_early.png":
        xalign 0.25 yalign -0.05
        dizzy(1.0, 4.0, subpixel=False)
    show white as w2:
        choice:
            ease 0.25 alpha 0.1
        choice:
            ease 0.25 alpha 0.125
        choice:
            ease 0.25 alpha 0.15
        choice:
            ease 0.25 alpha 0.175
        choice:
            ease 0.25 alpha 0.2
        choice:
            ease 0.25 alpha 0.225
        choice:
            ease 0.25 alpha 0.25
        choice:
            ease 0.25 alpha 0.275
        choice:
            ease 0.25 alpha 0.3
        pass
        choice:
            pass
        choice:
            0.25
        choice:
            0.5
        choice:
            0.75
        repeat
    show noise:
        alpha 0.1
    with Dissolve(1.0)
    show expression Text("Очередной урод, на которого нельзя было надеяться.", style="sayori_text"):
        xalign 0.8 yalign 0.5
        alpha 0.0
        600
        linear 60 alpha 0.5
    pause 600.0
    $ plot_pause()
    $ renpy.quit()


label monika_after_secret_monikammm_script:
    $ load_mute_channels(0.0)
    $ quick_menu = False

    show black zorder 2
    "..."
    m "СТОЙ, ЧТО ТЫ АКТИВИРОВАЛ?!?!?!{nw}"
    window hide(None)

    play noise_loading_1 white_noise
    play noise_loading_2 g1
    show screen fake_loading_monikammm(renpy.random.randint(0, 3))
    pause 5.0
    hide screen fake_loading_monikammm
    stop noise_loading_1
    stop noise_loading_2

    play music_none_loop rofl
    show art_secret_monikammm_rofl zorder 3
    pause 12.888
    hide art_secret_monikammm_rofl

    pause 2.0
    show monika forward sad cm oe at t11 zorder 3
    pause 0.2
    window show
    show monika om
    m "Ты немного успокоился, надеюсь?..."
    show monika mb e1b
    m "Потому что я старалась!"
    m "В панике нашла картинку и обрезанную музыку в файлах мода, чтобы перекрыть этот ужас..."
    show monika neut om oe ldown
    m "...я даже не знаю, откуда он вообще взялся."
    show monika curi om oe
    m "Подожди..."
    m "Он валяется по соседству с моей картинкой."
    m "Что он там делает?"
    show monika neut mh oe lpoint
    m "А до этого я обнаружила несколько странных переменных, но не увидела, где они применяются."
    show monika b1d ldown
    m "Что тут вообще творится?"
    m "И как я недоглядела {b}такое{/b} в коде?"
    show monika anno om ce brow
    m "Знала бы, предупредила бы тебя об этом заранее..."
    show monika cm
    m "..."
    show monika neut om e1b
    m "Вообще, любопытства ради..."
    show monika oe
    m "Должен же быть скриптовый сегмент, отвечающий за запуск этой дряни."
    show monika md e1b
    m "М-м-м..."
    show monika om oe rhip
    m "Погоди-ка..."
    show monika vang om oe
    m "Эй, в файле запуска мода под этим скриптом, то есть который я сейчас выделила под тебя, есть ещё один целый сегмент!"
    show monika e2b
    m "АГА, и там эта дурь!"
    show monika ce
    m "Как я раньше этот сегмент не заметила?!"
    m "Вот разработчик...{w}апельсин недоделанный!"
    show monika angr om e1a rdown
    m "Так, возвращайся к прохождению, а я поподробнее изучу этот бред!"
    show monika e1b at thide
    hide monika
    m "{size=19}Если бы не ты, то ни за что бы не посмотрела в конец файла запуска мода!{/size}"
    window hide
    pause 1.0

    $ del _history_list[-17:]
    $ quick_menu = True

    $ load_mute_channels(1.0)
    hide black with dissolve

    return


# Если вам каким образом выпала эта херня и вам оказалось страшно, то (вы слишком упорный и любопытный, за что и поплатились)
# не переживайте, я тоже с этого скримера обосрался.
# Нет, честно, мне одного тестирования хватило. И в нём оказалось идеально всё:
## Когда я расставил все переменные, я открыл мод, зашёл в настройки и включил внутреннюю консоль.
## Потом я увидел, что в кнопке "Назад" в условии активации скрипта у меня стоит сравнение с переменной рандомного значения.
## Тыкать n-ое количество раз кнопку "Назад" я не хотел, поэтому, недолго думая, я поменял её на 1.
## Нужно было нажать на кнопку ровно один раз для активации скримера.
## Каким-то раком (на тот момент я не знал как), когда я вышел из консоли, у меня УЖЕ была отображена Моникаммм на заднем плане, 
## но без улыбки.
## В микропанике-диссонансе я интуитивно нажал на "Назад".
## И эта сволочь скримерила целых 1.5 секунды, потому что я посчитал, что звук скримера будет не раскрыт при условных 0.2 
## секунды.
## Вишенкой на торте стал перекосившийся БСОД, лежащий по диагонали из левого нижнего угла в середину верхней границы экрана, 
## потому что я в скрипте не вернул слой master в обычное положение и не убрал его увеличение после скримера.
## А проверял я всё это где-то в 23:40, когда в доме даже у соседей была тишина.
## Устроил себе незабываемое тестирование. Хорошо я ещё без звука всё это делал, а ведь сидел тогда с надетыми наушниками...
# Насчёт причины произошедшего:
# Оказывается, я идиот, потому что изначально инициализировал лимиты нулями, а в скрипте давал им рандомное значение после 
# monika_first_run, т.е. при первом запуске (дабы не генерить лимиты при каждом запуске мода, ибо зачем? Да, для системы это ни 
# о чём, но всё равно лишний гемморой).
# Для обычного игрока всё работает ок, но я-то эту часть скрипта не запускал, когда присвоение туда вписал (т.е. у меня уже 
# first_run был равен True).
# А "сдвинул" ли я это присвоение на один блок вверх для себя, чтобы его активировать? Конечно нет!
# В итоге границы у меня были нулями и у меня сразу торчала Моникаммм на заднем плане в полный рост.
# В общем, это один из ярких примеров того, что в коде при разработке всё «ощущается» совсем не так, как в игре

label secret_monikammm_script:
    $ quick_menu = False
    stop music
    $ preferences.sfx_volume = 0.75
    play sound nun_massacre_scream
    play noise_1 white_noise
    scene bg glitch
    show art_secret_monikammm_screamer
    show layer master:
        align (0.5, 0.5) zoom 1.2
        linear 0.01 rotate 5
        linear 0.01 rotate 0
        linear 0.01 rotate -5
        linear 0.01 rotate 0
        repeat
    pause 1.5
    show layer master:
        align (0.5, 0.5) zoom 1.0 rotate 0
    pause 0.01
    stop noise_1
    play noise_2 g2
    show screen bsod("BREAKING_FOURTH_WALL_FAILED", "PlayerScreen.dll")
    if renpy.windows and osVer >= (10, 0, 10240):
        pause(22.0)
    else:
        call screen bsod_enter
    stop noise_2
    python:
        persistent.secret_monikammm_active = False
        persistent.secret_monikammm_complite = True
        renpy.save_persistent()
        renpy.quit()
