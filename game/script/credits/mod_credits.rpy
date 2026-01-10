## mod_credits.rpy

image credits_original_logo:
    "gui/logo.png"
    zoom 0.5

image credits_mod_logo:
    "mod_assets/elements/logo/act/act_1.png"
    zoom 0.25

image credits_team_salvato:
    "images/bg/splash-white.png"
    zoom 0.57

image credits_orange_team:
    "mod_assets/elements/logo/developers.png"
    zoom 0.37


style credits_text:
    font "mod_assets/font/Doki.ttf"
    color "#fff"
    size 30
    text_align 0.5
    outlines []

style credits_text_final is credits_text:
    color "#c2c2c2"

style credits_label_text is credits_text:
    color "#ffaae6"
    size 35

style credits_label_text_big is credits_label_text:
    size 45

image credits_text = ParameterizedText(style = "credits_text", ypos = 40)
image credits_text_final = ParameterizedText(style = "credits_text_final", ypos = 40)
image credits_label_text = ParameterizedText(style = "credits_label_text", ypos = -40)
image credits_label_text_big = ParameterizedText(style = "credits_label_text_big", ypos = -40)


transform credits_scroll(x = 0.5):
    subpixel True
    xalign x yoffset 740
    linear 25 yoffset -530

transform cs_left:
    credits_scroll(1.0)
transform cs_right:
    credits_scroll(0.9)


transform credits_text_scroll(x = 640):
    subpixel True
    anchor (0.5, 0.5) xpos x yoffset 920
    linear 25 yoffset -350

transform cts_center:
    credits_text_scroll
transform cts_left:
    credits_text_scroll(320)
transform cts_left_small:
    credits_text_scroll(420)
transform cts_right_small:
    credits_text_scroll(860)
transform cts_right:
    credits_text_scroll(960)


transform credits_sticker_scroll(x = 0.56):
    subpixel True
    xalign x yanchor 1.0 yoffset 940
    1.0
    linear 25 yoffset -330

transform cc_1:
    credits_sticker_scroll(0.2)
transform cc_2:
    credits_sticker_scroll(0.8)




label mod_credits:

    scene black

    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False

    play music mod_credits_1

    pause 6.0

    show credits_original_logo at credits_text_scroll(780)
    pause 0.1
    show credits_team_salvato at credits_text_scroll(1100)
    show credits_label_text "Концепция, дизайн и сценарий\nоригинальной игры" as clt0 at cts_left
    pause 0.1
    show credits_text "Dan Salvato из команды Team Salvato" as ct0 at cts_left

    pause 8.0

    show credits_mod_logo at credits_text_scroll(540)
    pause 0.05
    show credits_orange_team at credits_text_scroll(210)
    show credits_label_text "Концепция, дизайн и сценарий\nмодификации" as clt1 at cts_right
    show credits_text "KitsuruDev" as ct1 at cts_right

    pause 8.0

    show credits_label_text_big "Художники" as clt at cts_center

    pause 6.0

    show credits_label_text "Художники спрайтов персонажей" as clt2 at cts_left_small
    pause 0.1
    show credits_text "Все художники спрайтов указаны в\nразделе \"Персонажи\" экстра-меню" as ct2 at cts_left_small
    pause 0.5
    show m_chibi_poem at cc_2

    pause 8.0

    show credits_label_text "Художники спрайтов" as clt0 at cts_right_small
    pause 0.25
    show credits_text "Голова хоррорного чиби Сайори при прыжке:\n\"Doki Doki Takeover: Bad Ending\"\n(модификация игры \"Friday Night Funkin\")" as ct0 at cts_right_small
    pause 0.5
    show s_chibi_poem at cc_1

    pause 8.0

    show credits_label_text "Художники спрайтов" as clt1 at cts_left_small
    pause 0.1
    show credits_text "Глючная чиби-смесь Моники, Юри и Нацуки:\nAverage#3201 (Discord, старый ник)" as ct1 at cts_left_small
    pause 0.5
    show mix_chibi glitch at cc_2

    pause 8.0

    show credits_label_text "Художники спрайтов" as clt2 at cts_right_small
    pause 0.1
    show credits_text "Пистолет в кошмаре 1 акта 12 дня (Flame-Hybrid 9):\nzonked (opengameart.org)" as ct2 at cts_right_small
    pause 0.5
    show mc_chibi_poem at cc_1

    pause 8.0

    show credits_label_text "Художники СG-сцен" as clt0 at cts_left_small
    pause 0.1
    show credits_text "Все художинки CG-сцен указаны в\nразделе \"Галерея (CG)\" экстра-меню" as ct0 at cts_left_small
    pause 0.5
    show y_chibi_poem at cc_2

    pause 8.0

    show credits_label_text "Художники фонов" as clt1 at cts_right_small
    pause 0.1
    show credits_text "Все художники фонов указаны в\nразделе \"Галерея (фоны)\" экстра-меню" as ct1 at cts_right_small
    pause 0.5
    show n_chibi_poem at cc_1

    pause 8.0

    show credits_label_text_big "Музыка и звуки" as clt at cts_center

    pause 6.0

    show credits_label_text "Композиторы" as clt2 at cts_left_small
    pause 0.1
    show credits_text "Все композиторы указаны в\nразделе \"Музыка\" экстра-меню" as ct2 at cts_left_small
    pause 0.5
    show kam_chibi_poem at cc_2

    pause 8.0

    show credits_label_text "Звуки" as clt0 at cts_right_small
    pause 0.1
    show credits_text "Все звуки использованы из оригинальной игры\nи с сайтов zvukogram.com и zvukipro.com" as ct0 at cts_right_small
    pause 0.5
    show k_chibi_poem at cc_1

    pause 8.0

    show credits_label_text "Звуки" as clt1 at cts_center
    pause 0.1
    show credits_text "Рингтон Макса \"Ringtone -- Red Light\": fadirra (dig.ccmixter.org)\nРингтон Юри \"Ringtone\": Dimas#4872 (Discord, старый ник) (DDMC Community Assets)" as ct1 at cts_center

    pause 8.0

    show credits_label_text_big "Механики и код" as clt at cts_center

    pause 6.0

    show credits_label_text "Шаблон-основа модификации" as clt2 at cts_center
    pause 0.1
    show credits_text "Разработчик кода: Azariel Del Carmen (GanstaKingofSA)\n(подробное описание есть в разделе \"О моде\" экстра-меню)" as ct2 at cts_center

    pause 6.0

    show credits_label_text "Mood Posing Tool (MPT) -- система сочетаний спрайтов персонажей" as clt0 at cts_center
    pause 1.1
    show credits_text "Автор: Chronos (Reddit)\nПомощь автору: AgentGold\nХудожник эмоций: Yagamirai10 (Reddit)\nРазработчик кода: Terra\nТестирование: MrGraves" as ct0 at cts_center

    pause 8.0

    show credits_label_text "Смартфон (код и интерфейс)" as clt1 at cts_center
    pause 0.1
    show credits_text "Elckarow#8399 (Discord, старый ник)\n" as ct1 at cts_center

    pause 6.0

    show credits_label_text "Ползунки настроек и идея меняющегося меню" as clt2 at cts_center
    pause 0.1
    show credits_text "\"Doki Doki Takeover +\" (модификация \"Friday Night Funkin\")\n" as ct2 at cts_center

    pause 6.0

    show credits_label_text "Анимированные глитчи на объектах" as clt0 at cts_center
    pause 0.1
    show credits_text "Gouvernathor (GitHub, репозиторий:\nhttps://github.com/Gouvernathor/renpy-ChromaGlitch.git)" as ct0 at cts_center

    pause 6.0

    show credits_label_text "Мини-игра Tetromania (Тетрис)" as clt9 at cts_center
    pause 1.1
    show credits_text "Разработчик основы кода: Mikan-DS (GitHub)\nСписок мини-игр для RenPy: Andredron (lemmasoft.renai.us)\nЗвук получения нового уровня: Circlerun (opengameart.org)\nЗвуки блоков и музыка проигрыша: Fupi (opengameart.org)" as ct9 at cts_center

    pause 6.0

    show credits_label_text "Значки, курсоры и шрифты" as clt10 at cts_center
    pause 0.1
    show credits_text "Значки и курсоры использованы с сайта flaticons.net\nШрифты использованы с сайта fonts-online.ru" as ct10 at cts_center

    pause 6.0

    queue music mod_credits_2

    show credits_label_text "Отдельная благодарность (хотя вряд-ли это кто-то из них увидит)" as clt1 at cts_center
    pause 0.5
    show credits_text "Team Salvato и лично Дэну Сальвато за созданный Литературный клуб,\nкоторый изменил мою жизнь" as ct1 at cts_center
    pause 3.0
    show credits_text "Сообществу DDLC в Reddit за большое количество материала для модов и\nподдержание игры до сих пор (но не за вялую публикацию моего поста о моде и\nнаплевательство на него, тьфу на вас)" as ct2 at cts_center
    pause 3.0
    show credits_text "Космическому коту (Youtube) за видео по RenPy, которые помогли мне освоиться\nна первых парах разработки" as ct3 at cts_center
    pause 2.0
    show credits_text "Akane its mein Alter Ego за тестирование модификации и настоящую дружбу" as ct4 at cts_center
    pause 1.75
    show credits_text "Fugita за тестирование модификации и поддержку" as ct5 at cts_center
    pause 1.75
    show credits_text "Моему брату за помощь в формировании общей структуры сюжета\nмодификации по главам" as ct6 at cts_center
    pause 2.0
    show credits_text "Моей семье за всю поддержку (без них я бы не был тем, кем являюсь сейчас)" as ct7 at cts_center
    pause 2.0
    show credits_text "Моим одногруппникам (и -цам) в вузе за хорошее отношение ко мне, да и в целом\nтоже за \"ненаплевательство\" в мою сторону" as ct8 at cts_center
    pause 2.5
    show credits_text "А отдельным из них благодарность за общение и времяпрепровождение,\nблагодаря которым становится веселее и легче" as ct9 at cts_center
    pause 3.0
    show credits_text "Моим учителям и препродавателям (и в школе, и в вузе), которые\nвпихнули в меня кучу знаний (без них бы я тоже не был тем,\nкем являюсь сейчас)" as ct10 at cts_center
    pause 3.0
    show credits_text "Всем остальным, кому было интересно наблюдать за разработкой и\nкто ждал релиз (считаные единицы, ха-ха)" as ct11 at cts_center
    pause 4.0
    show credits_text "А ещё себе родимому, потому что смог довести модификацию до релиза\nв нормальном и рабочем виде, несмотря на практически нулевую поддержку и\nпонимание хоть кого-то, сколько я здесь наворотил (поразительно, на самом деле...\nХотя нет, эмоций у меня это не вызывает)" as ct12 at cts_center
    pause 4.0
    show credits_text "И, конечно же, тебе, [persistent.playername], за прохождение этого мода!\n(Даже если я тебя никогда не увижу)\n(И даже если я тебя ненавижу)" as ct13 at cts_center

    pause 22.0

    show credits_text "Однако это ещё не конец..." as cft1:
        align (0.5, 0.5) alpha 0
        ease 2.0 alpha 1
        4.5
        ease 2.0 alpha 0

    pause 8.0

    show credits_text "...потому что это только начало." as cft2:
        align (0.5, 0.5) alpha 0
        ease 2.0 alpha 1
        4.5
        ease 2.0 alpha 0

    pause 8.5

    stop music fadeout 11.0

    scene menu_bg
    show intro
    with Dissolve(9.0)

    pause 2.0

    show credits_text_final "Нажмите любую клавишу продвижения сюжета для выхода в главное меню...":
        align (0.5, 1.0) alpha 0
        ease 8.0 alpha 0.85

    $ plot_pause()

    python:
        if persistent.secret_monika <= 3:
            persistent.full_playthrough = True
            persistent.secret_monika = 11083688962175460853
            renpy.save_persistent()

    return
