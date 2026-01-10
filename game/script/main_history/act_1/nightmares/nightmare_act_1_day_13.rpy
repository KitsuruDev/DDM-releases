
screen choice_monikammm_support(items):
    style_prefix "choice"

    vpgrid:
        cols 3 rows 7
        spacing 30
        align (0.5, 0.5)

        for i in items:
            textbutton "{glitch=" + str(random.randint(0, 50)) + "}" + i.caption + "{/glitch}":
                idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)),
                    im.matrix.desaturate() * im.matrix.colorize("#707070", "#cfcfcf")), gui.choice_button_borders)
                hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)),
                    im.matrix.desaturate() * im.matrix.colorize("#707070", "#cfcfcf")), gui.choice_button_borders)
                action i.action

screen punch_monikammm_act_1_day_13:
    button:
        area(453, 406, 185, 280)
        mouse "use"
        action Return()




label nightmare_act_1_day_13:
    $ preferences.voice_volume = 0.75
    $ blocker = False
    $ mmm_name = "???"
    $ secret_monikammm_chance = True

    call skip_block_off
    call window_open
    call autosave
    mc "Ч-что...{w}за..."
    voice "mmm/act_1/day_13/0001"
    mmm "{size=17}О, ты наконец-то проснулся.{/size}"
    call window_close

    play music m1 fadein 3.0
    show monikammm_cg_act_1_day_13_mask_grain
    show monikammm_cg_act_1_day_13_mask_gas_cloud
    show monikammm_cg_act_1_day_13_mask_smoke
    show monikammm_cg_act_1_day_13_mask_smoke_flip
    show monika_room
    show monika_room_highlight
    show monika_room_desk
    show monikammm desk hup
    with dissolve_scene_full
    pause 1.5
    call window_open
    mc "{sc=3}ТВОЮ МАТЬ!!!--{/sc}{nw}" with vpunch
    show monikammm hdown
    voice "mmm/act_1/day_13/0002"
    mmm "Хватит кривляться, меня это очень раздражает."
    mc "......"
    show monikammm hcross
    voice "mmm/act_1/day_13/0003"
    mmm "Вот так-то лучше, теперь с тобой можно нормально поговорить."
    voice "mmm/act_1/day_13/0004"
    mmm "Только для начала мне придётся представиться, чтобы твой мозг кое-как начал работать."
    mc "...издеваешься?"
    voice "mmm/act_1/day_13/0005"
    mmm "А, ты уже способен мыслить?"
    voice "mmm/act_1/day_13/0006"
    mmm "Ладно, наш разговор станет более продуктивным, нежели я думала."
    mc "Вообще, ты и есть то чёрное пятно, которое якобы стоит за всеми моими кошмарами?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0007"
    mmm "Тебе одна из этих сказала?"
    mc "Да."
    show monikammm hup
    voice "mmm/act_1/day_13/0008"
    mmm "Что ж, это было ожидаемо."
    mc "И какого чёрта ты вся чёрно-белая?"
    mc "И где твой рот?!"
    show monikammm hdown
    voice "mmm/act_1/day_13/0009"
    mmm "Заткнись и дай всё сказать!"
    voice "mmm/act_1/day_13/0010"
    mmm "Я -- часть тебя."
    $ mmm_name = _("Альтер-эго")
    voice "mmm/act_1/day_13/0011"
    mmm "А если проще, то я твоё альтер-эго."
    voice "mmm/act_1/day_13/0012"
    mmm "Или часть твоего психотипа."
    voice "mmm/act_1/day_13/0013"
    mmm "Думай, как хочешь."
    mc "Ты?..."
    "Часть меня...{w}вот это уродливое «нечто»?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0014"
    mmm "Я читаю твои мысли."
    mc "..."
    mc "Хорошо, раз так: почему у тебя образ Моники?"
    mc "И почему ты настолько страшная...{w}а ещё «резкая» на вид...{w}и чёрно-белая?"
    voice "mmm/act_1/day_13/0015"
    mmm "Если ты полностью включишь свою голову, то сам ответишь на свои два вопроса."
    mc "..."
    show monikammm hdown
    voice "mmm/act_1/day_13/0016"
    mmm "Ладно, к этому мы ещё вернёмся."
    voice "mmm/act_1/day_13/0017"
    mmm "Ещё вопросы по моему образу?"
    mc "...почему у тебя такой...{w}странный голос?"
    mc "Будто ты -- искусственный интеллект, а не живое существо."
    mc "А ещё будто ты мне его прямо в мозг транслируешь."
    show monikammm hcross
    voice "mmm/act_1/day_13/0018"
    mmm "Потому что это твоё дурацкое сознание."
    voice "mmm/act_1/day_13/0019"
    mmm "Я могу им управлять, но не могу совладать на все 100 процентов."
    voice "mmm/act_1/day_13/0020"
    mmm "В итоге, я не способна полировать мелкие детали в своих, скажем, «продуктах» деятельности."
    show monikammm e2
    voice "mmm/act_1/day_13/0021"
    mmm "Хотя мне и этого более чем достаточно."
    show monikammm e1
    voice "mmm/act_1/day_13/0022"
    mmm "Ещё вопросы?"
    mc "...ты слишком хорошо мыслишь для кого-то «абстрактного»."
    mc "Все остальные «персонажи» моих кошмаров постоянно кривлялись, говоря пространственными непонятными фразами."
    mc "Но в тебе я сейчас такого не заметил..."
    voice "mmm/act_1/day_13/0022d1"
    mmm "А я что, должна была себя так вести?"
    voice "mmm/act_1/day_13/0022d2"
    mmm "И постоянно говорить: \"Я -- это ты, я -- это ты, задницей нюхаю цветы\"?"
    voice "mmm/act_1/day_13/0022d3"
    mmm "Мы не в каком-нибудь художественном произведении, наполненным «водянистым» текстом, высосанным из пальца."
    show monikammm e3
    voice "mmm/act_1/day_13/0022d4"
    mmm "Особенно если он связан с внутренними мыслями или с описанием природы и окружения..."
    mc "И почему ты «она», а не «он»?"
    show monikammm e1
    mc "Я же парень!"
    voice "mmm/act_1/day_13/0023"
    mmm "«Оно», блин."
    voice "mmm/act_1/day_13/0024"
    mmm "Я же сказала, кто я."
    mc "Ну, альтер-эго, я уже услышал."
    voice "mmm/act_1/day_13/0025"
    mmm "Правильно."
    show monikammm hdown
    voice "mmm/act_1/day_13/0026"
    mmm "Я могу быть чем угодно и кем угодно в пределах твоего сознания."
    voice "mmm/act_1/day_13/0027"
    mmm "Но раз у тебя это вызывает сильный диссонанс, то для тебя я буду «она»."
    mc "...чёрт с тобой, даже разбираться не буду, почему так."
    show monikammm hup
    voice "mmm/act_1/day_13/0028"
    mmm "Не переживай, у нас вся ночь впереди, чтобы во всём разобраться."
    voice "mmm/act_1/day_13/0029"
    mmm "Разложим всё по полочкам: от «А» до «Я»."
    voice "mmm/act_1/day_13/0030"
    mmm "Впрочем, именно поэтому я тебя сюда и посадила."
    show monikammm hdown
    voice "mmm/act_1/day_13/0031"
    mmm "Вот только с чего именно начать..."
    mmm "..."
    show monikammm e3
    voice "mmm/act_1/day_13/0032"
    mmm "Хм..."
    voice "mmm/act_1/day_13/0033"
    mmm "Хотя чего я думаю..."
    show monikammm e1
    voice "mmm/act_1/day_13/0034"
    mmm "Пробежимся по твоим весёлым снам за последнюю неделю."
    show monikammm hcross
    voice "mmm/act_1/day_13/0035"
    mmm "И мой первый вопрос будет следующим..."
    voice "mmm/act_1/day_13/0036"
    mmm "Ты понял, что всё это значило?"
    mc "Значило?..."
    mc "У этого маразма всё-таки был какой-то скрытый смысл?"
    voice "mmm/act_1/day_13/0037"
    mmm "Представляешь, это всё произошло в твоей голове."
    voice "mmm/act_1/day_13/0038"
    mmm "А у тебя нет здесь абстрактной фигни с эффектом «зловещей долины», с которой люди постоянно любят проводить корреляцию, говоря о своих снах."
    mc "..."
    mc "А что вообще было..."
    mc "Повисшая псевдо-Сайори была, с псевдо-Юри в кровате бился, от псевдо-Нацуки шарахался..."
    mc "Чёрт, всё в голове перемешалось."
    show monikammm hdown
    voice "mmm/act_1/day_13/0039"
    mmm "Да по глазам вижу, что ты нихрена ничего не понял."
    show monikammm e2
    voice "mmm/act_1/day_13/0040"
    mmm "Придётся разжевать абсолютно всё..."
    mc "..."
    show monikammm e1
    voice "mmm/act_1/day_13/0041"
    mmm "Итак, твой первый сон!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0042"
    mmm "Помнишь его основные подробности?"
    mc "...вышел из дома, пришёл к Сайори."
    mc "Зашёл...{w}точно, увидел её записи на бумаге, где она...{w}да какая разница, я не буду это вспоминать!"
    mc "Я реально не хочу вспоминать всё это дерьмо!"
    voice "mmm/act_1/day_13/0043"
    mmm "Но не ты ли хотел покончить со всеми этими кошмарами раз и навсегда?"
    mc "Ну я."
    show monikammm hdown
    voice "mmm/act_1/day_13/0044"
    mmm "Так сиди и вспоминай, чтобы всё сложить воедино и больше к этому не возвращаться!"
    mc "Зараза ты этакая..."
    show monikammm hcross
    voice "mmm/act_1/day_13/0045"
    mmm "Ещё «спасибо» мне скажешь."
    voice "mmm/act_1/day_13/0046"
    mmm "Давай уже, думай."
    mc "...Сайори повесилась."
    mc "..."
    mmm "..."
    mc "Всё."
    voice "mmm/act_1/day_13/0047"
    mmm "Извини, у меня произошёл микродиссонанс."
    show monikammm e2
    voice "mmm/act_1/day_13/0048"
    mmm "Просто твоя последняя фраза прозвучала, как тупорылая шутка."
    mc "......"
    show monikammm e1
    voice "mmm/act_1/day_13/0049"
    mmm "В любом случае, ты всё верно сказал, молодец."
    mc "И что?"
    mc "Что мне это даёт?"
    voice "mmm/act_1/day_13/0050"
    mmm "Ну не тупи, Макс."
    voice "mmm/act_1/day_13/0051"
    mmm "Если это твоя башка, то очевидно, что всё остальное -- тоже часть тебя."
    show monikammm hdown
    voice "mmm/act_1/day_13/0052"
    mmm "Теперь наложи сюда характер настоящей Сайори."
    mc "Характер..."
    "Позитив...{w}альтруизм...{w}доброта, открытость?"
    show monikammm hup
    voice "mmm/act_1/day_13/0053"
    mmm "Верно идёшь!"
    voice "mmm/act_1/day_13/0054"
    mmm "Осталось чуть-чуть!"
    mc "Ну это всё повесилось."
    mc "Повесилось..."
    mc "Это как я быстро растерял свою позитивную и наивную часть?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0055"
    mmm "Ну наконец-то!"
    voice "mmm/act_1/day_13/0056"
    mmm "Именно это я и хотела от тебя услышать."
    show monikammm hcross
    voice "mmm/act_1/day_13/0057"
    mmm "Что ж, зафиксируем данный результат, он нам ещё понадобится."
    voice "mmm/act_1/day_13/0058"
    mmm "Теперь следующий кошмар!"
    mc "...точно...{w}твоя записка."
    voice "mmm/act_1/day_13/0059"
    mmm "Похвально, твой мозг реально работает."
    voice "mmm/act_1/day_13/0060"
    mmm "Только этот кошмар мы учитывать не будем, поскольку в нём уже нет смысла, раз я смогла посадить тебя сюда."
    voice "mmm/act_1/day_13/0061"
    mmm "Я говорила про следующий."
    voice "mmm/act_1/day_13/0062"
    mmm "Когда ты в темноте в окне своей спальни мелькал."
    mc "Подожди."
    show monikammm hdown
    mc "Ты всё это время наблюдала со стороны, а не «волшебным» образом через сознание?"
    voice "mmm/act_1/day_13/0063"
    mmm "Я говорила, что не могу обуздать его полностью."
    show monikammm e3
    voice "mmm/act_1/day_13/0064"
    mmm "Поэтому приходилось изощряться, занимая по возможности наиболее выгодные для меня позиции."
    "Не помню, чтобы я тебя где-то видел..."
    show monikammm e1
    "А может, и видел..."
    show monikammm hcross
    voice "mmm/act_1/day_13/0065"
    mmm "Так что там в твоём следующем кошмаре?"
    mc "...я встал с кровати."
    mc "Потом...{w}потом записка была какая-то...{w}от Юри."
    mc "А потом...{w}каким-то образом она появилась в моей спальне и накинулась на меня."
    mc "Мне пришлось сопротивляться."
    mc "А, я же тогда ещё головой о тумбочку треснулся."
    show monikammm e2
    voice "mmm/act_1/day_13/0066"
    mmm "Ха, теперь понятно, почему ты не сопротивлялся, когда Юри бережно несла тебя в сторону школы."
    show monikammm e1
    voice "mmm/act_1/day_13/0068"
    mmm "Что ж, твои выводы по данному кошмару?"
    mc "Я не помню, почему Юри на меня напала."
    mc "Но она тогда обезумела."
    voice "mmm/act_1/day_13/0069"
    mmm "Не забывай про реальный «прототип»."
    voice "mmm/act_1/day_13/0070"
    mmm "Как там к тебе реальная Юри относится?"
    mc "...она влюблена."
    voice "mmm/act_1/day_13/0071"
    mmm "Да, и..."
    mc "Меня хотели изнасиловать?"
    voice "mmm/act_1/day_13/0072"
    mmm "Верно."
    voice "mmm/act_1/day_13/0073"
    mmm "Так какой тут вывод?"
    mc "Любовь...{w}бесконтрольная...{w}и социальный голод?"
    voice "mmm/act_1/day_13/0074"
    mmm "Отлично."
    voice "mmm/act_1/day_13/0075"
    mmm "Итак, дальше."
    voice "mmm/act_1/day_13/0076"
    mmm "Что было дальше?"
    mc "Уже забыл, честно."
    voice "mmm/act_1/day_13/0077"
    mmm "...манга."
    voice "mmm/act_1/day_13/0078"
    mmm "С «интересным» содержанием."
    mc "Блин."
    mc "Блевотина эта, точно..."
    voice "mmm/act_1/day_13/0079"
    mmm "Нацуки тогда тебе всё напрямую сказала."
    mc "...да, ей было одиноко."
    mc "Она хотела внимания."
    voice "mmm/act_1/day_13/0080"
    mmm "Ага."
    mc "Моё относительное одиночество и желание найти того, кто будет меня ценить?"
    voice "mmm/act_1/day_13/0081"
    mmm "Прекрасно."
    voice "mmm/act_1/day_13/0082"
    mmm "Ну и на закрепление, 2 последних сна."
    mc "Юри тогда вела себя более сдержанно и адекватно."
    mc "А ещё...{w}тогда я тебя увидел вплотную."
    voice "mmm/act_1/day_13/0083"
    mmm "...да, тогда всё немного вышло из-под контроля."
    voice "mmm/act_1/day_13/0084"
    mmm "Она слишком сильно надавила на твою «голову», так скажем."
    show monikammm e2
    voice "mmm/act_1/day_13/0085"
    mmm "А я лишь пыталась «выправить» тебя обратно."
    mc "..."
    show monikammm e1
    voice "mmm/act_1/day_13/0086"
    mmm "Последний сон?"
    mc "...я убил Нацуки и Юри."
    mc "Это ведь ты мне тогда пистолет оставила?"
    mc "И проходы во время моего бега меняла?"
    voice "mmm/act_1/day_13/0087"
    mmm "Ха, догадался."
    voice "mmm/act_1/day_13/0088"
    mmm "Теперь пора догадаться до последнего вывода и слепить всё воедино."
    mc "Безумная любовь и голод...{w}я их убил..."
    mc "Убил."
    mc "Я полностью их убил..."
    voice "mmm/act_1/day_13/0089"
    mmm "...и правильно сделал."
    show monikammm hdown
    voice "mmm/act_1/day_13/0090"
    mmm "Ты так классно с ними разобрался, моё почтение!"
    voice "mmm/act_1/day_13/0091"
    mmm "Я уж думала, что придётся тебе немного с этим помогать."
    show monikammm hcross
    voice "mmm/act_1/day_13/0092"
    mmm "Однако это снова неважная информация."
    voice "mmm/act_1/day_13/0093"
    mmm "Какое следствие по всем разрозненным выводам?"
    mc "Я изменился, потому что вырос."
    mc "Перестал надеяться на остальных, потому что страдал от этого."
    mc "Постоянно..."
    show monikammm hup
    voice "mmm/act_1/day_13/0094"
    mmm "Вот теперь ты реально молодец."
    voice "mmm/act_1/day_13/0095"
    mmm "Вся картина собрана и верно тобой интерпретирована."
    show monikammm hdown
    voice "mmm/act_1/day_13/0096"
    mmm "А теперь ответь мне на другой вопрос..."
    voice "mmm/act_1/day_13/0097"
    mmm "Какого хрена ты ушёл в Литературный клуб и завёл себе девушку?"
    mc "Что?"
    voice "mmm/act_1/day_13/0098"
    mmm "Глухой, что ли?"
    mc "Мне что, нельзя в клубы вступать и заниматься личной жизнью?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0099"
    mmm "Можно, не отрицаю."
    voice "mmm/act_1/day_13/0100"
    mmm "Но ты же буквально повторяешь сценарий с психологом."
    voice "mmm/act_1/day_13/0101"
    mmm "Напомнить про него, а?"
    mc "..."
    voice "mmm/act_1/day_13/0102"
    mmm "Вот то-то и оно."
    voice "mmm/act_1/day_13/0103"
    mmm "Так что там с ответом?"
    mc "Я не уйду из Литературного клуба."
    mc "И Монику не брошу."
    mc "Я мудак, по-твоему?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0104"
    mmm "Хорошо, зайдём и здесь издалека."
    show monikammm e2
    voice "mmm/act_1/day_13/0105"
    mmm "Вот скажи мне, Макс..."
    show monikammm hup e1
    voice "mmm/act_1/day_13/0106"
    mmm "Ради чего ты живёшь?"
    mc "..."
    mmm "..."
    mc "..."
    mc "...ну...{w}не знаю."
    mc "Родители, Сайори...{w}Моника теперь...{w}да и клуб теперь..."
    show monikammm hcross
    voice "mmm/act_1/day_13/0107"
    mmm "А почему они?"
    mc "Как \"почему\"?"
    mc "Родители -- моя семья, это даже не обсуждается."
    mc "Остальные, кого я перечислил, -- люди, которые реально заслуживают хорошего отношения в свою сторону."
    mc "Ну и заботу, в принципе."
    voice "mmm/act_1/day_13/0108"
    mmm "И все они тебя поддерживают?"
    mc "...да."
    voice "mmm/act_1/day_13/0109"
    mmm "А до клуба?"
    mc "А мне плевать на то, что было до клуба."
    show monikammm hdown
    mc "Клуб меня вытянул в нормальную жизнь."
    mc "Остальное не волнует."
    show monikammm hcross
    voice "mmm/act_1/day_13/0110"
    mmm "Вот скажи мне, Макс, если сможешь..."
    show monikammm e3
    voice "mmm/act_1/day_13/0111"
    mmm "Ты так кичишься Литературным клубом..."
    show monikammm e1
    voice "mmm/act_1/day_13/0112"
    mmm "А кто тебя поддерживал, кроме него?"
    voice "mmm/act_1/day_13/0113"
    mmm "Поддерживал ли тебя хоть кто-нибудь?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0114"
    mmm "Можешь назвать мне {b}хоть одного человека{/b}?!"
    call skip_block_on
    $ quick_menu = False
    window hide(None)

    python:
        list_items = []
        for i in range(21):
            if i == 10: list_items.append(("Родители?...", "Родители"))
            else:
                word = list("Нет")
                for j in range(len(word)):
                    if random.randint(0, 3) == 0: word[j] = random.choice(nonunicode)
                list_items.append((''.join(word), "Нет"))
        choice_item = renpy.display_menu(list_items, screen="choice_monikammm_support")

    call skip_block_off
    $ quick_menu = True
    window auto
    if choice_item == "Родители":
        voice "mmm/act_1/day_13/0115"
        mmm "Родители?!"
        show monikammm hcross
        voice "mmm/act_1/day_13/0116"
        mmm "Серьёзно?!"
        voice "mmm/act_1/day_13/0117"
        mmm "Ха-ха-ха!"
        voice "mmm/act_1/day_13/0118"
        mmm "А они с нами здесь, в одной комнате?"
        mc "..."
    else:
        show monikammm hcross
        voice "mmm/act_1/day_13/0119"
        mmm "Я так и думала."
    voice "mmm/act_1/day_13/0120"
    mmm "Макс, при всей этой фальши ты забываешь одну ма-а-аленькую вещь..."
    play sound hit_wood
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0121c"
        mmm "Всем на тебя ПЛЕВАТЬ!!!" with vpunch
        show monikammm laside
        voice "mmm/act_1/day_13/0122c"
        mmm "Плевать тому психологу, потому что у него личная жизнь!"
        show monikammm raside
        voice "mmm/act_1/day_13/0123c"
        mmm "Плевать тому бывшему другу, потому что у него, блин, отношения!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0124c"
        mmm "И плевать будет Литературному клубу, который через год перестанет существовать!"
    else:
        voice "mmm/act_1/day_13/0121"
        mmm "Всем на тебя НАСРАТЬ!!!" with vpunch
        show monikammm laside
        voice "mmm/act_1/day_13/0122"
        mmm "Насрать тому психологу, потому что у него личная жизнь!"
        show monikammm raside
        voice "mmm/act_1/day_13/0123"
        mmm "Насрать тому бывшему другу, потому что у него, блять, отношения!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0124"
        mmm "И насрать будет Литературному клубу, который через год перестанет существовать!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0125"
    mmm "Тут только родители кое-как пытаются о тебе заботиться, но их даже рядом нет."
    voice "mmm/act_1/day_13/0126"
    mmm "А больше-то у тебя никого и нет."
    voice "mmm/act_1/day_13/0127"
    mmm "Ты никому здесь неинтересен."
    voice "mmm/act_1/day_13/0128"
    mmm "Никого не волнует, что творится у тебя в башке."
    voice "mmm/act_1/day_13/0129"
    mmm "Никого не волнует, что ты можешь вкладывать в старания столько сил, на сколько другие совершенно не способны."
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0130"
    mmm "НИКОГО." with vpunch
    voice "mmm/act_1/day_13/0131"
    mmm "Все твои редкие попытки получить хоть какое-то внимание заканчивались крахом."
    voice "mmm/act_1/day_13/0132"
    mmm "А почему?"
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0133c"
        mmm "Да хрен его знает!"
    else:
        voice "mmm/act_1/day_13/0133"
        mmm "Да хер его знает!"
    voice "mmm/act_1/day_13/0134"
    mmm "Наверное, из принципа!"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0135c"
        mmm "Свыше кто-то решил над тобой поглумиться, понакидывать дерьма на твой вентилятор."
        show monikammm laside
        voice "mmm/act_1/day_13/0136c"
        mmm "Вот у других, более раздолбайских и безответственных людей, всё есть!"
    else:
        voice "mmm/act_1/day_13/0135"
        mmm "Свыше кто-то решил над тобой поглумиться, понакидывать говна на твой вентилятор."
        show monikammm laside
        voice "mmm/act_1/day_13/0136"
        mmm "Вот у других, более распиздяйских и безответственных людей, всё есть!"
    show monikammm hdown
    voice "mmm/act_1/day_13/0137"
    mmm "И поддержка, и связи, и, как следствие, прекрасное психическое состояние."
    show monikammm hcross
    voice "mmm/act_1/day_13/0138"
    mmm "А у тебя этого НЕТ."
    voice "mmm/act_1/day_13/0139"
    mmm "Потому что..."
    voice "mmm/act_1/day_13/0140"
    mmm "...потому."
    show monikammm e2
    voice "mmm/act_1/day_13/0141"
    mmm "Честно, я реально не понимаю, в чём твоя проблема."
    show monikammm e1
    voice "mmm/act_1/day_13/0142"
    mmm "Но вот ты пытаешься закрыть на это глаза."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0143c"
        mmm "И снова, блин, прёшься на те же грабли, которые бьют тебя с каждым разом всё больнее и больнее."
    else:
        voice "mmm/act_1/day_13/0143"
        mmm "И снова, блять, прёшься на те же грабли, которые бьют тебя с каждым разом всё больнее и больнее."
    voice "mmm/act_1/day_13/0144"
    mmm "Ты так сдохнешь нахрен."
    show monikammm hcross
    voice "mmm/act_1/day_13/0145"
    mmm "И ведь реально сдохнешь."
    voice "mmm/act_1/day_13/0146"
    mmm "А самое забавное во всём этом то, что остальные ещё умудряются тебе нагадить."
    voice "mmm/act_1/day_13/0147"
    mmm "Вот серьёзно, у тебя был хоть один маленький эпизод в твоей жизни, когда ты был по-настоящему счастлив?"
    voice "mmm/act_1/day_13/0148"
    mmm "До Литературного клуба и Сайори."
    mc "......"
    voice "mmm/act_1/day_13/0149"
    mmm "Не было же, так и скажи."
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0150c"
        mmm "Каждый раз происходило какое-то мелкое дерьмо, которое всё портило."
    else:
        voice "mmm/act_1/day_13/0150"
        mmm "Каждый раз происходило какое-то мелкое говно, которое всё портило."
    show monikammm e2
    voice "mmm/act_1/day_13/0151"
    mmm "Либо связанное с делами, либо связанное с социумом, в котором тебе приходилось находиться."
    show monikammm e1
    voice "mmm/act_1/day_13/0152"
    mmm "Да здравствует школа с её пубертатными язвенными полудурками."
    voice "mmm/act_1/day_13/0153"
    mmm "Обязательно в таких социумах происходила какая-нибудь хрень, по типу, когда все решили дружно нихрена не делать, а потом, опа!"
    voice "mmm/act_1/day_13/0154"
    mmm "Оказывается нужно было всё делать, чем ты и занимался."
    voice "mmm/act_1/day_13/0155"
    mmm "И когда все начинают подсасываться к учителю, тебя начинает тошнить от такой лживо-вонючей картины."
    show monikammm e2
    voice "mmm/act_1/day_13/0156"
    mmm "Ты справедливо всех упрекаешь, потому что такое раздолбайство невозможно терпеть."
    show monikammm e3
    voice "mmm/act_1/day_13/0157"
    mmm "Да и кому потом нужны такие «кадры», которые ничего сделать нормально не могут, так ещё и ответственность пытаются сбагрить с себя при первой же возможности?"
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0158c"
        mmm "Но на тебя начинают выливать дерьмо."
    else:
        voice "mmm/act_1/day_13/0158"
        mmm "Но на тебя начинают выливать говно."
    show monikammm e2
    voice "mmm/act_1/day_13/0159"
    mmm "В мелких порциях, косо, через тупорылые шутки, но тем не менее..."
    show monikammm e1
    voice "mmm/act_1/day_13/0160"
    mmm "И ты ничего не можешь с этим сделать."
    show monikammm hdown
    voice "mmm/act_1/day_13/0161"
    mmm "Ты один."
    voice "mmm/act_1/day_13/0162"
    mmm "Все против тебя, все тебя обсирают за твои способности."
    show monikammm laside
    voice "mmm/act_1/day_13/0163"
    mmm "Никого не волнует, что ты работаешь не для учёбы, а для поддержания собственной дисциплины."
    show monikammm raside
    voice "mmm/act_1/day_13/0164"
    mmm "Никого не волнует, что ты затыкаешь этим своё время, дабы не сжирать себя чёртовыми мыслями, которые бурлят в твоей башке каждый чёртов день."
    show monikammm laside
    voice "mmm/act_1/day_13/0165"
    mmm "Никого не волнует, что ты умеешь и на что ты способен."
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0166c"
        mmm "Ты просто для них кусок дерьма, который портит все потуги нагло просочиться дальше."
    else:
        voice "mmm/act_1/day_13/0166"
        mmm "Ты просто для них кусок говна, который портит все потуги нагло просочиться дальше."
    voice "mmm/act_1/day_13/0167"
    mmm "И ты никогда не сможешь их переубедить."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0168c"
        mmm "Любая твоя фраза в их сторону будет затягивать тебя в это дерьмистое болото всё сильнее и сильнее."
    else:
        voice "mmm/act_1/day_13/0168"
        mmm "Любая твоя фраза в их сторону будет затягивать тебя в это говнистое болото всё сильнее и сильнее."
    voice "mmm/act_1/day_13/0169"
    mmm "Всё, что остаётся сделать, -- это просто нихрена не делать."
    voice "mmm/act_1/day_13/0170"
    mmm "Что, в свою очередь, трактуется «обществом» как твоё поражение."
    voice "mmm/act_1/day_13/0171"
    mmm "Грубо говоря, слив."
    voice "mmm/act_1/day_13/0172"
    mmm "И вот такие ситуации происходят нечасто, но и не редко."
    voice "mmm/act_1/day_13/0173"
    mmm "И тебя постоянно в них гадят."
    show monikammm hdown
    voice "mmm/act_1/day_13/0174"
    mmm "Гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят, гадят."
    show monikammm laside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0175c"
        mmm "И НИ ОДИН поганец даже НЕ СОИЗВОЛИТ сказать тебе \"СПАСИБО\" за все твои старания."
        show monikammm hdown
        voice "mmm/act_1/day_13/0176c"
        mmm "Всем смачно плевать!"
    else:
        voice "mmm/act_1/day_13/0175"
        mmm "И НИ ОДНА паскуда даже НЕ СОИЗВОЛИТ сказать тебе \"СПАСИБО\" за все твои старания."
        show monikammm hdown
        voice "mmm/act_1/day_13/0176"
        mmm "Всем смачно похер!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0177"
    mmm "Абсолютно для всех твои старания -- норма."
    voice "mmm/act_1/day_13/0178"
    mmm "Когда для тебя -- выше нормы, как минимум."
    show monikammm e2
    voice "mmm/act_1/day_13/0179"
    mmm "И это ещё прекрасно, если к тебе особо никто не лезет."
    show monikammm e1
    voice "mmm/act_1/day_13/0180"
    mmm "А вот описанные мной ситуации?"
    voice "mmm/act_1/day_13/0181"
    mmm "Тебя же ещё за старания гнобить начинают."
    voice "mmm/act_1/day_13/0182"
    mmm "Постоянно."
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0183"
    mmm "ВСЕГДА." with vpunch
    mc "..............."
    show monikammm hcross
    voice "mmm/act_1/day_13/0184"
    mmm "Вот, кстати, твой бестолковый мод на одну средненькую по популярности визуальную новеллу, например!"
    voice "mmm/act_1/day_13/0185"
    mmm "Забыл уже про него?"
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0186c"
        mmm "А потому что всем плевать было."
        voice "mmm/act_1/day_13/0187c"
        mmm "Ты сжёг часть своего времени и сил, которые даже минимально не окупились."
        show monikammm raside
        voice "mmm/act_1/day_13/0188c"
        mmm "Ну и нахрена?"
    else:
        voice "mmm/act_1/day_13/0186"
        mmm "А потому что всем насрать было."
        voice "mmm/act_1/day_13/0187"
        mmm "Ты всрал часть своего времени и сил, которые даже минимально не окупились."
        show monikammm raside
        voice "mmm/act_1/day_13/0188"
        mmm "Ну и нахера?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0189"
    mmm "Зачем?!"
    show monikammm laside
    voice "mmm/act_1/day_13/0190"
    mmm "Поддержание своего жалкого уровня знаний программного языка?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0191"
    mmm "Для этого есть и другие, более эффективные методы."
    show monikammm raside
    voice "mmm/act_1/day_13/0192"
    mmm "Сделать интересную игру?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0193"
    mmm "Так ты и не справился, потому что у тебя не было никакой поддержки, а в одиночку всё сделать невероятно трудно."
    show monikammm hcross
    voice "mmm/act_1/day_13/0194"
    mmm "Да и кому нужны эти грёбаные визуальные новеллы?"
    voice "mmm/act_1/day_13/0195"
    mmm "Практические неанимированные плоские картиночки на статичном фоне!"
    show monikammm e2
    voice "mmm/act_1/day_13/0196"
    mmm "А про тексты я вообще молчу: там иногда такая розово-сопливая тягомотина, что уснуть нахрен хочется уже через полчаса, если не раньше."
    show monikammm e1
    voice "mmm/act_1/day_13/0197"
    mmm "Увлекательный, блин, геймплей, а?"
    voice "mmm/act_1/day_13/0198"
    mmm "И при всём этом очень забавно видеть, как другие люди, которые хуже тебя понимают программный язык..."
    voice "mmm/act_1/day_13/0199"
    mmm "...вкладывают в разы меньше сил, постоянно выпендриваются на публику и получают в РАЗЫ больше внимания, похвалы и поддержки, чем ты."
    voice "mmm/act_1/day_13/0200"
    mmm "Хотя у тебя ни того, ни другого, ни третьего никогда не было."
    show monikammm e3
    voice "mmm/act_1/day_13/0201"
    mmm "Причём это всё они вообще не заслуживают, по крайней мере в таком объёме..."
    show monikammm e1
    voice "mmm/act_1/day_13/0202"
    mmm "А ты заслуживаешь."
    voice "mmm/act_1/day_13/0203"
    mmm "Но не получаешь."
    voice "mmm/act_1/day_13/0204"
    mmm "И никогда не получишь, хоть всю свою душу вложи."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0205c"
        mmm "Всем плевать, Макс."
        play sound hit_wood
        show monikammm hdown
        voice "mmm/act_1/day_13/0206c"
        mmm "ПЛЕВАТЬ!" with vpunch
    else:
        voice "mmm/act_1/day_13/0205"
        mmm "Всем насрать, Макс."
        play sound hit_wood
        show monikammm hdown
        voice "mmm/act_1/day_13/0206"
        mmm "НАСРАТЬ!" with vpunch
    show monikammm hcross
    voice "mmm/act_1/day_13/0207"
    mmm "И ты до сих пор, чёрт, до сих пор надеешься на грёбаный «авось», как психолог, будто всё вдруг внезапно изменится в лучшую сторону, заиграв радужными красками."
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0208"
    mmm "Не будет этого никогда, мать твою, не будет!" with vpunch
    voice "mmm/act_1/day_13/0209"
    mmm "Потому что дальше -- больше, дальше -- хуже!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0210"
    mmm "А я хочу, чтобы ты наконец откинул эту тупую сопливую идею и научился жить в такой реалии."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0211c"
        mmm "Чтобы ты перестал тратить свои силы и время на нахрен никому не нужную абстракцию и научился изворачивать этот жирный недостаток в своё главное преимущество."
    else:
        voice "mmm/act_1/day_13/0211"
        mmm "Чтобы ты перестал тратить свои силы и время на нахер никому не нужную абстракцию и научился изворачивать этот жирный недостаток в своё главное преимущество."
    voice "mmm/act_1/day_13/0212"
    mmm "Потому что чем меньше о тебе знают, тем больше карт на твоих руках."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0213c"
        mmm "Ты буквально можешь превратиться в ящик Пандоры, который поимеет своими действиями если не всё, то большинство точно."
    else:
        voice "mmm/act_1/day_13/0213"
        mmm "Ты буквально можешь превратиться в ящик Пандоры, который выебет своими действиями если не всё, то большинство точно."
    voice "mmm/act_1/day_13/0214"
    mmm "Потому что, будем честны, если бы ты не контролировал свои эмоции и не сдерживался бы моралью..."
    voice "mmm/act_1/day_13/0215"
    mmm "...ты бы стал очередным убийцей, который зарезал бы минимум несколько человек."
    show monikammm e2
    voice "mmm/act_1/day_13/0216"
    mmm "Да, в состоянии аффекта, но тем не менее..."
    show monikammm e1
    voice "mmm/act_1/day_13/0217"
    mmm "И уж поверь, ты бы это точно сделал."
    voice "mmm/act_1/day_13/0217d1"
    mmm "Просто вспомни ещё раз, как ты всадил нож в Юри и прострелил башку Нацуки."
    voice "mmm/act_1/day_13/0217d2"
    mmm "Многие на твоём месте устроили бы панику и ничего не смогли бы сделать, но только не ты."
    voice "mmm/act_1/day_13/0217d3"
    mmm "А сорвался бы ты почему?"
    voice "mmm/act_1/day_13/0218"
    mmm "Потому что твоя психика и так на пределе, она ничем не «разряжается», поскольку ты один."
    show monikammm e3
    voice "mmm/act_1/day_13/0219"
    mmm "Зато потом, представь, как будут орать об этом новости, пытаясь привлечь к себе зрителей на волне актуальности..."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0220c"
        mmm "А ещё сколько на тебя дерьма в комментариях к ним выльется..."
    else:
        voice "mmm/act_1/day_13/0220"
        mmm "А ещё сколько на тебя говна в комментариях к ним выльется..."
    mc "......"
    show monikammm e1
    voice "mmm/act_1/day_13/0221"
    mmm "И вот ты хочешь просто взять и закопать в себе скрытый потенциал, которого у большинства даже нет?"
    voice "mmm/act_1/day_13/0222"
    mmm "Стать человеком, которого невозможно хоть как-то поцарапать."
    voice "mmm/act_1/day_13/0223"
    mmm "Стать ТАКИМ человеком, который сам начнёт обливать грязью всех, кто пытается в его сторону что-то вякнуть."
    voice "mmm/act_1/day_13/0224"
    mmm "Стать сильным человеком -- полностью независимым ото всех."
    voice "mmm/act_1/day_13/0225"
    mmm "Ведь самый сильный человек -- это человек, у которого никого и ничего нет."
    mc "Ну нихрена себе ты утрировала."
    voice "mmm/act_1/day_13/0226"
    mmm "...а также полностью контролирующий свои эмоции и умеющий самовосстанавливаться."
    mc "А..."
    voice "mmm/act_1/day_13/0227"
    mmm "И ты уже шёл по пути становления таким человеком."
    show monikammm hdown
    voice "mmm/act_1/day_13/0228"
    mmm "Но свернул нахрен куда-то в сторону."
    show monikammm laside e2
    voice "mmm/act_1/day_13/0229"
    mmm "Видите ли, Сайори его в клуб затянула, а Моника соблазнила."
    show monikammm hdown e1
    voice "mmm/act_1/day_13/0230"
    mmm "Макс, какого чёрта?"
    mc "Да как же ты заколебала..."
    mc "А-а-а, подожди, дай угадаю: именно поэтому ты нацепила на себя образ Моники и исковеркала его до ужаса, чтобы привить мне отвращение к самой Монике, да?"
    if persistent.censorship:
        mc "Таков твой гениальный план, собранный из дерьма и палок?"
    else:
        mc "Таков твой гениальный план, собранный из говна и палок?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0231"
    mmm "Ух ты, {w=0.7}дога--{nw}"
    play sound hit_wood
    if persistent.censorship:
        mc "Я сказал, сволочь, НЕТ!" with vpunch
        show monikammm hdown
        mc "Мне абсолютно плевать на твоё мнение по этому поводу."
    else:
        mc "Я сказал, сука, НЕТ!" with vpunch
        show monikammm hdown
        mc "Мне абсолютно насрать на твоё мнение по этому поводу."
    mc "Это МОЯ жизнь, это МОЙ выбор."
    if persistent.censorship:
        mc "И я не позволю таким мразотным тварям, как ты, ЛОМАТЬ мою жизнь и ещё ДИКТОВАТЬ мне, как надо жить."
    else:
        mc "И я не позволю таким мразотным уёбищам, как ты, ЛОМАТЬ мою жизнь и ещё ДИКТОВАТЬ мне, как надо жить."
    $ quick_menu = False
    $ style.say_dialogue = style.edited

    voice "mmm/act_1/day_13/0232"
    mmm "{cps=19}Да пошла нахер твоя грёбаная Моника{/cps}{nw}{done}"
    $ currentpos = get_pos(channel="music")
    stop music
    play sound "mod_assets/voice/mmm/act_1/day_13/0232g.mp3"
    mmm "Да пошла нахер твоя грёбаная Моника{fast}{cps=35}ммммммммммммммммммммммммммммммммм{/cps}{w=0.5}{nw}"
    show monikammm smile
    pause 0.01

    if cg_a1_d11_night_mmm.unlocked == False:
        $ cg_a1_d11_night_mmm.unlock() # позднее открытие из-за спойлера имени в описании

    if cg_a1_d13_night_mmm.unlocked == False:
        $ cg_a1_d13_night_mmm.unlock()

    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound s_kill_glitch1
    pause 0.5
    stop sound
    $ audio.m1_2 = "<from " + str(currentpos) + " loop 0>bgm/m1.ogg"
    play music m1_2
    hide screen tear_screen
    show monikammm -smile
    window show(None)

    $ mmm_name = _("Моникаммм")

    $ style.say_dialogue = style.normal
    $ quick_menu = True
    mc "{sc=3}АРГХ!{/sc}"
    mc "{sc=1.5}У меня аж голова заболела, чёрт!{/sc}"
    mc "Зато теперь я знаю, как тебя называть..."
    mc "Это прямо тебе идеально подходит, жалкая копия Моники!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0233"
    mmm "Ты вообще меня не слушал..."
    show monikammm e3
    voice "mmm/act_1/day_13/0234"
    mmm "Я иду ему навстречу, а он упирается, как баран."
    show monikammm e1
    mc "Потому что я уже начал избавляться от прошлого!"
    play sound hit_wood
    mc "Я стал ЖИТЬ!" with vpunch
    if persistent.censorship:
        mc "Но теперь внезапно ворвалась ТЫ и стала боломутить МОЮ воду, вспоминая зачем-то всё дерьмо, которое со мной произошло в течение всей прошедшей жизни."
    else:
        mc "Но теперь внезапно ворвалась ТЫ и стала боломутить МОЮ воду, вспоминая зачем-то всё говно, которое со мной произошло в течение всей прошедшей жизни."
    show monikammm hdown
    voice "mmm/act_1/day_13/0235"
    mmm "А-а-а, вот как?"
    show monikammm e2
    voice "mmm/act_1/day_13/0236"
    mmm "Жить он стал..."
    show monikammm e1
    voice "mmm/act_1/day_13/0237"
    mmm "А это \"жить\" -- постоянные провалы в себя по вечерам, когда ты освобождаешься от дел?"
    show monikammm laside
    voice "mmm/act_1/day_13/0238"
    mmm "Постоянное волнение за своих соклубниц?"
    show monikammm raside
    voice "mmm/act_1/day_13/0239"
    mmm "Безуспешные поиски того психолога для Юри?"
    show monikammm laside
    voice "mmm/act_1/day_13/0240"
    mmm "Воспитание Сайори?"
    show monikammm raside
    voice "mmm/act_1/day_13/0241"
    mmm "Переживание за Нацуки из-за отца, чья строгость, такое ощущение, крайне преувеличена."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0242c"
        mmm "Или \"жить\" -- это быть посланным нахрен отцом Моники, который уж точно не позволит тебе с ней «воссоединиться»?"
        play sound hit_wood
        mc "{sc=3}АХ ТЫ МРАЗЬ!!!--{/sc}{nw}" with vpunch
    else:
        voice "mmm/act_1/day_13/0242"
        mmm "Или \"жить\" -- это быть посланным нахер отцом Моники, который уж точно не позволит тебе с ней «воссоединиться»?"
        play sound hit_wood
        mc "{sc=3}АХ ТЫ СУКА!!!--{/sc}{nw}" with vpunch
    voice "mmm/act_1/day_13/0243"
    mmm "МОЛЧАТЬ, МУДИЛА!"
    voice "mmm/act_1/day_13/0244"
    mmm "Контролируй свои эмоции."
    mc "{sc=2}......{/sc}"
    voice "mmm/act_1/day_13/0245"
    mmm "Макс..."
    show monikammm hcross
    voice "mmm/act_1/day_13/0246"
    mmm "Пойми ты меня."
    voice "mmm/act_1/day_13/0247"
    mmm "То есть, себя."
    voice "mmm/act_1/day_13/0248"
    mmm "Это ради твоего же блага."
    voice "mmm/act_1/day_13/0249"
    mmm "Ты сейчас реально слепо смотришь на всю текущую ситуацию."
    voice "mmm/act_1/day_13/0250"
    mmm "Ты даже не ощутишь, как быстро она будет меняться."
    voice "mmm/act_1/day_13/0251"
    mmm "Ты должен научиться адаптироваться к любому событию."
    voice "mmm/act_1/day_13/0252"
    mmm "Иначе сломаешься и сдохнешь."
    show monikammm hdown
    voice "mmm/act_1/day_13/0253"
    mmm "И именно поэтому я здесь."
    show monikammm laside
    voice "mmm/act_1/day_13/0254"
    mmm "Я хочу открыть тебе глаза на всю эту ситуацию."
    show monikammm hdown
    voice "mmm/act_1/day_13/0255"
    mmm "Успеть привить тебе качества, которые понадобятся для того, чтобы выжить."
    voice "mmm/act_1/day_13/0256"
    mmm "Ведь никто, слышишь, НИКТО не протянет тебе руку."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0257c"
        mmm "Всем плевать!"
    else:
        voice "mmm/act_1/day_13/0257"
        mmm "Всем насрать!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0258"
    mmm "И я не устану это повторять!"
    voice "mmm/act_1/day_13/0259"
    mmm "Я, твоё сознание, -- единственная, кто может тебе помочь."
    voice "mmm/act_1/day_13/0260"
    mmm "Даже твой кидала-психолог тебе давным-давно писал..."
    voice "mmm/act_1/day_13/0261"
    mmm "\"Поддержка -- это как раз та вещь, которую ты должен обеспечить для себя сам\"."
    voice "mmm/act_1/day_13/0262"
    mmm "А когда ты обеспечишь себе поддержку, то абсолютно никто тебе не понадобится."
    voice "mmm/act_1/day_13/0263"
    mmm "Совершенно."
    show monikammm hdown
    voice "mmm/act_1/day_13/0264"
    mmm "Так что..."
    show monikammm hhandshake
    voice "mmm/act_1/day_13/0265"
    mmm "Макс."
    voice "mmm/act_1/day_13/0266"
    mmm "Время выбирать."
    voice "mmm/act_1/day_13/0267"
    mmm "Пора меняться в лучшую сторону."
    voice "mmm/act_1/day_13/0268"
    mmm "Потому что у нас больше нет времени."
    mc "..."
    mc "...скажи мне вот что..."
    show monikammm hdown
    mc "После всего твоего дерьма..."
    mc "...у меня правда сейчас есть выбор?"
    mc "Потому что в твоих словах я чётко слышу: \"Уходи от прежней жизни\"."
    mc "Да и вообще, никто не будет устраивать целое представление с 3-мя смертями образов участниц моего клуба, только чтобы дать мне шанс определить свой «жизненный путь»!"
    mc "Слишком жестоко, БЕЗУМНО даже!"
    mc "Тут есть что-то ещё!"
    mc "З-а-ч-е-м ты всё это сделала?"
    voice "mmm/act_1/day_13/0269"
    mmm "Я же сказала..."
    voice "mmm/act_1/day_13/0270"
    mmm "Просто. {w=0.65}Пытаюсь. {w=0.65}Помочь."
    mc "..."
    show monikammm hhandshake
    voice "mmm/act_1/day_13/0266"
    mmm "Время выбирать."
    call window_close

    call screen punch_monikammm_act_1_day_13

    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        ease 1.0 yoffset 200 zoom 2.0
        0.2
        ease 0.2 xoffset 80 yoffset 185 zoom 2.05
        0.01
        ease 0.5 xoffset 0 yoffset 200 zoom 2.0

    pause 1.2
    play sound mc_handshake_monikammm
    pause 2.0

    call window_open
    voice "mmm/act_1/day_13/0272"
    mmm "Вот и отлично, правильный выбор."
    mc "Я его ещё не сделал."
    voice "mmm/act_1/day_13/0273"
    mmm "Что?"
    $ quick_menu = False
    window hide(None)

    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        yoffset 200 zoom 2.0
        linear 0.15 zoom 4.0 yoffset 400

    pause 0.1
    play sound hit
    scene white
    scene black with dissolve
    pause 0.25

    window show(None)
    voice "mmm/act_1/day_13/0274"
    mmm "{sc=3}ЗАРАЗА!!!{/sc}{w=0.75}{nw}"
    window hide(None)
    $ style.say_dialogue = style.edited

    play sound mc_neck_crunch_1
    play noise_1 gnid
    play noise_2 monikammm_psyho_control
    play noise_3 white_noise
    $ currentpos = get_pos(channel="music")
    stop music

    show monikammm_cg_act_1_day_13_mask_grain
    show monikammm_cg_act_1_day_13_mask_gas_cloud
    show monikammm_cg_act_1_day_13_mask_smoke
    show monikammm_cg_act_1_day_13_mask_smoke_flip
    show monika_room
    show monika_room_highlight
    show bg glitch
    show monika_room_desk
    show monikammm desk smile hattack
    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        zoom 2.5 rotate 30
        parallel:
            choice:
                ease 0.01 xoffset -5
            choice:
                ease 0.01 xoffset 5
            ease 0.01 xoffset 0
            repeat
        parallel:
            choice:
                ease 0.01 yoffset -5
            choice:
                ease 0.01 yoffset 5
            ease 0.01 yoffset 0
            repeat

    pause 1.0

    window show(None)
    voice "mmm/act_1/day_13/0275"
    mmm "Думал, что ты такой тут умный, да, тварь?!"
    window hide(None)

    play sound mc_neck_crunch_2 volume 1.0
    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        zoom 2.6 rotate -50
        parallel:
            choice:
                ease 0.01 xoffset -5
            choice:
                ease 0.01 xoffset 5
            ease 0.01 xoffset 0
            repeat
        parallel:
            choice:
                ease 0.01 yoffset -5
            choice:
                ease 0.01 yoffset 5
            ease 0.01 yoffset 0
            repeat

    window show(None)
    mc "ААААААААААААААААААААА!!!--{nw}"
    voice "mmm/act_1/day_13/0276"
    mmm "Конечно, тебе больно!"
    voice "mmm/act_1/day_13/0277"
    mmm "Больно так же, как и мне от тебя!"
    window hide(None)

    play sound mc_neck_crunch_2
    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        zoom 2.7 rotate 70
        parallel:
            choice:
                ease 0.01 xoffset -5
            choice:
                ease 0.01 xoffset 5
            ease 0.01 xoffset 0
            repeat
        parallel:
            choice:
                ease 0.01 yoffset -5
            choice:
                ease 0.01 yoffset 5
            ease 0.01 yoffset 0
            repeat

    window show(None)
    mc "ААААААААААААААААААААА!!!--{nw}"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0278c"
        mmm "НРАВИТСЯ, ТВАРЬ?!"
    else:
        voice "mmm/act_1/day_13/0278"
        mmm "НРАВИТСЯ, УЁБОК?!"
    voice "mmm/act_1/day_13/0279"
    mmm "НРАВИТСЯ?!"
    window hide(None)

    stop noise_1
    stop noise_2
    stop noise_3
    $ audio.m1_2 = "<from " + str(currentpos) + " loop 0>bgm/m1.ogg"
    play music m1_2
    play sound mc_neck_crunch_1
    hide bg glitch
    show layer master:
        subpixel True
        anchor (0.5, 0.5) align (0.5, 0.5)
        zoom 1.0 rotate 0

    pause 0.5
    show monikammm hdown
    pause 0.25
    show monikammm mrect
    pause 0.25
    $ currentpos = get_pos(channel="music")
    stop music
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound s_kill_glitch1
    pause 0.5
    stop sound
    $ audio.m1_2 = "<from " + str(currentpos) + " loop 0>bgm/m1.ogg"
    play music m1_2
    show monikammm -mrect
    hide screen tear_screen

    $ style.say_dialogue = style.normal
    $ quick_menu = True
    window show(None)
    mc "{bt=3}Пха-а-а, пха-а-а...{/bt}"
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0280c"
        mmm "Какой же ты всё-таки придурок."
        voice "mmm/act_1/day_13/0281c"
        mmm "Тупой, самоуверенный, эгоистичный придурок."
    else:
        voice "mmm/act_1/day_13/0280"
        mmm "Какая же ты всё-таки паскуда."
        voice "mmm/act_1/day_13/0281"
        mmm "Тупая, самоуверенная, эгоистичная паскуда."
    mc "{bt=2}...это и есть ты...{w}это именно ты...{/bt}"
    mc "{bt=2}...ты просто хочешь сломать...{w}мою жизнь...{/bt}"
    show monikammm hdown
    voice "mmm/act_1/day_13/0282"
    mmm "Да что ты говоришь?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0283c"
        mmm "Мне опять сказать, как ты благополучно пропустил всё мимо ушей?"
    else:
        voice "mmm/act_1/day_13/0283"
        mmm "Мне опять сказать, как ты благополучно просрал всё мимо ушей?"
    show monikammm laside
    voice "mmm/act_1/day_13/0284"
    mmm "Или что, опять мне будешь втирать про отношения?"
    show monikammm raside
    voice "mmm/act_1/day_13/0285"
    mmm "О том, как твоя кристально-безупречная богиня Моника снизошла до тебя, очаровав своим телом и душой?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0286"
    mmm "Прямо как все подростки, как только почувствовали у себя прилив гормонов в половые органы."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0287c"
        mmm "{bt=4}Бэ-Хэ, Я тАк ХоЧу С кЕм-То ПоСоСаТьСя И\nзАнЯтЬСя ЛюБоВьЮ, пОтОмУ чТо У мЕнЯ иГрАюТ\nгОрМоНы В зАдНиЦе!{/bt}"
    else:
        voice "mmm/act_1/day_13/0287"
        mmm "{bt=4}Бэ-Хэ, Я тАк ХоЧу С кЕм-То ПоСоСаТьСя И\nпОтРаХаТьСя, ПоТоМу ЧтО у МеНя ИгРаЮт\nГоРмОнЫ в ЖоПе!{/bt}"
    show monikammm e1
    voice "mmm/act_1/day_13/0288"
    mmm "{bt=4}Я тАк СкУчАю В оДиНоЧеСтВе!{/bt}"
    show monikammm e2
    voice "mmm/act_1/day_13/0289"
    mmm "{bt=4}Я нА вСё ПоЙдУ, чТоБы У мЕнЯ бЫлА дЕвУшКа!{/bt}"
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0290c"
        mmm "{bt=4}НеТ, я Не ХоЧу К нЕй ТоЛьКо ПрИкАсАтЬсЯ\nпОлОвЫмИ оРгАнАмИ, у МеНя БуДеТ нАсТоЯщАя\nЛюБоВь, Бэ-Хэ!{/bt}"
    else:
        voice "mmm/act_1/day_13/0290"
        mmm "{bt=4}НеТ, я Не ХоЧу С нЕй ТоЛьКо ЕбАтЬсЯ в\nПоЛоВыЕ оРгАнЫ, У мЕнЯ бУдЕт НаСтОяЩаЯ\nлЮбОвЬ, бЭ-хЭ!{/bt}"
    mc "..."
    show monikammm e1
    mmm "..."
    if persistent.censorship:
        mc "...что ж, можешь себя поздравить, ты, дерьмистое образование моего больного мозга..."
    else:
        mc "...что ж, можешь себя поздравить, ты, говнистое образование моего больного мозга..."
    mc "...с тем, что у тебя нет НИКОГО, о ком ты переживаешь и кто будет переживать о тебе!"
    show monikammm e2
    voice "mmm/act_1/day_13/0291"
    mmm "Переживать, {w=0.65}любить, {w=0.65}скучать..."
    voice "mmm/act_1/day_13/0292"
    show monikammm e1 hcross
    mmm "Сколько можно, Макс, тратить на это свои силы?"
    voice "mmm/act_1/day_13/0293"
    mmm "Все эти чувства давно должны были стать для тебя в прошлом."
    voice "mmm/act_1/day_13/0294"
    mmm "Я это осознала и приняла."
    voice "mmm/act_1/day_13/0295"
    mmm "И поверь, я не стыжусь этого."
    voice "mmm/act_1/day_13/0296"
    mmm "И никогда не буду стыдиться."
    voice "mmm/act_1/day_13/0297"
    mmm "Я давно оставила позади себя все эти...{w=2.0}сентиментальности."
    show monikammm e2
    voice "mmm/act_1/day_13/0298"
    mmm "Вместе с ними стёрлись вся боль, все обиды, все беспокойства."
    show monikammm e1
    voice "mmm/act_1/day_13/0299"
    mmm "И всё было бы прекрасно, если бы не {b}ты{/b}."
    voice "mmm/act_1/day_13/0300"
    mmm "Потому что ты совершенно не понимаешь, каких высот можешь добиться, скинув с себя всю эту эмоциональную дрянь."
    voice "mmm/act_1/day_13/0301"
    mmm "Ты боишься потерять всё, лишившись эмоций."
    voice "mmm/act_1/day_13/0302"
    mmm "Ты боишься измениться."
    voice "mmm/act_1/day_13/0303"
    mmm "Понимаешь, в этом твоя проблема, как эмпата: ты пытаешься усидеть на двух стульях."
    voice "mmm/act_1/day_13/0304"
    mmm "Хочешь быть взрослой и сильной личностью, которая живёт прекрасной жизнью, но при этом боишься отрекаться от чувств и эмоций."
    voice "mmm/act_1/day_13/0305"
    mmm "Тебе нужны взаимные чувства, нужна поддержка окружающих, чтобы подпитывать своё состояние..."
    voice "mmm/act_1/day_13/0306"
    mmm "Ты боишься остаться в одиночестве."
    show monikammm hdown
    voice "mmm/act_1/day_13/0307"
    mmm "Тобой движет страх."
    voice "mmm/act_1/day_13/0308"
    mmm "Инстинкт."
    voice "mmm/act_1/day_13/0309"
    mmm "И поэтому мне мерзотно с тебя, потому что это жалко."
    voice "mmm/act_1/day_13/0310"
    mmm "Мне мерзотно с тебя, потому что по психотипу я {b}лучше{/b} тебя."
    voice "mmm/act_1/day_13/0311"
    mmm "Ведь отречение от эмпатии даёт тебе чистейший разум."
    show monikammm e2
    voice "mmm/act_1/day_13/0312"
    mmm "У тебя никогда не будет сомнений, не будет страхов."
    show monikammm e3
    voice "mmm/act_1/day_13/0313"
    mmm "И не будет инстинктов, которые тебе мешают."
    show monikammm e1
    voice "mmm/act_1/day_13/0314"
    mmm "У тебя будет только собственная голова, способная грамотно анализировать ситуацию и принимать правильные решения."
    voice "mmm/act_1/day_13/0315"
    mmm "Тебе не понадобятся взаимные чувства, не понадобится поддержка окружающих..."
    voice "mmm/act_1/day_13/0316"
    mmm "Тебе {b}никто и ничто{/b} не понадобится."
    show monikammm hcross
    voice "mmm/act_1/day_13/0317"
    mmm "Потому что ты будешь опорой для самого себя."
    voice "mmm/act_1/day_13/0318"
    mmm "А став опорой для самого себя, ты добьёшься таких высот, о которых сейчас даже мечтать не можешь."
    show monikammm e2
    voice "mmm/act_1/day_13/0319"
    mmm "Впрочем, об этом я уже говорила."
    show monikammm e1
    mc "Ты буквально говоришь мне стать мразью."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0320c"
        mmm "Твою мать..."
    else:
        voice "mmm/act_1/day_13/0320"
        mmm "Блять..."
    voice "mmm/act_1/day_13/0321"
    mmm "Ты ничерта меня не понимаешь."
    show monikammm hcross
    mc "А по-моему, это ты уже тотально во всём путаешься."
    if persistent.censorship:
        mc "Будто в тебе бурлит море дерьма, которое так и хочется выплеснуть наружу, лишь бы был повод."
    else:
        mc "Будто в тебе бурлит море говна, которое так и хочется выплеснуть наружу, лишь бы был повод."
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0322"
    mmm "ВОТ!" with vpunch
    show monikammm hcross
    voice "mmm/act_1/day_13/0323"
    mmm "Почему оно в тебе сидит и кипит?"
    voice "mmm/act_1/day_13/0324"
    mmm "Да потому что ты несформировавшийся эмпат!"
    voice "mmm/act_1/day_13/0325"
    mmm "Нет в тебе основы."
    voice "mmm/act_1/day_13/0326"
    mmm "{b}НЕТ{/b}."
    voice "mmm/act_1/day_13/0327"
    mmm "И такое сочетание уже пару раз тебя обжигало."
    show monikammm e3
    voice "mmm/act_1/day_13/0328"
    mmm "Друг с отношениями, психолог..."
    show monikammm e2
    voice "mmm/act_1/day_13/0329"
    mmm "Особенно психолог."
    show monikammm e1
    voice "mmm/act_1/day_13/0330"
    mmm "Напомнить, к чему привела твоя наивная открытость?"
    mc "Грх-х-х..."
    voice "mmm/act_1/day_13/0331"
    mmm "О-о-о, не нравится, больная точка."
    mc "Рано или поздно это всё равно бы случилось, что тут думать..."
    mc "Логично, что одного унесёт в личную жизнь, а другого -- в другую страну с созданием собственной семьи."
    mc "Кому из них какое дело до кучки пикселей в Интернете, которую они никогда в глаза не видели?..."
    mc "«Особенно» какое дело психологу, у которого и так дофига работы и «очных» пациентов."
    voice "mmm/act_1/day_13/0332"
    mmm "Вот как?"
    voice "mmm/act_1/day_13/0333"
    mmm "И ты думаешь, я в эту чушь поверю?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0334"
    mmm "Вот она правда: он допустил потерю связи с тобой из-за того, что постоянно надеялся на «авось», будто всё пройдёт своим чередом."
    show monikammm laside
    voice "mmm/act_1/day_13/0335"
    mmm "Твоя ценность была сразу вычтена из его «списка связей»."
    show monikammm hdown
    voice "mmm/act_1/day_13/0336"
    mmm "И если таким раком проходят исследования и лечения в психологии, то она будет развиваться целых 510 лет!"
    show monikammm raside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0337c"
        mmm "Ведь именно понадобится столько лет, чтобы психологи наконец осознали, как важно уделять внимание пациентам, с которыми они работают!"
    else:
        voice "mmm/act_1/day_13/0337"
        mmm "Ведь именно понадобится столько лет, чтобы психологи наконец осознали, как важно уделять внимание пациентам, с которыми они, блять, работают!"
    show monikammm hdown
    voice "mmm/act_1/day_13/0338"
    mmm "А он этого ДАЖЕ БЛИЗКО не осознавал!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0339"
    mmm "За что благополучно вместе с тем друганом отхватил от тебя поток дерьма."
    voice "mmm/act_1/day_13/0340"
    mmm "Отдать должное, вот тогда ты поступил правильно."
    show monikammm e2
    voice "mmm/act_1/day_13/0341"
    mmm "Нечего было церемониться и терпеть их наплевательство в твою сторону."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0342c"
        mmm "Ты тоже, блин, человек, а не куча пикселей, на которые можно забить хрен."
        voice "mmm/act_1/day_13/0343c"
        mmm "Я просто понять не могу: как при всех их психотипах, характерах и отношениях к миру стало так резко плевать на тебя."
    else:
        voice "mmm/act_1/day_13/0342"
        mmm "Ты тоже, сука, человек, а не куча пикселей, на которые можно забить хер."
        voice "mmm/act_1/day_13/0343"
        mmm "Я просто понять не могу: как при всех их психотипах, характерах и отношениях к миру стало так резко насрать на тебя."
    show monikammm e2
    voice "mmm/act_1/day_13/0344"
    mmm "Совершенно понять не могу."
    show monikammm e1
    voice "mmm/act_1/day_13/0345"
    mmm "Но имеем, что имеем."
    voice "mmm/act_1/day_13/0346"
    mmm "Короче, пошёл бы он нахрен."
    show monikammm e2
    voice "mmm/act_1/day_13/0347"
    mmm "Хотя как же?"
    show monikammm e1
    voice "mmm/act_1/day_13/0348"
    mmm "Ты ж там Юри помогаешь, снова его ищешь."
    voice "mmm/act_1/day_13/0349"
    mmm "И снова всё это дерьмо всплывёт обратно."
    mc "Я всего лишь сведу его с Юри и всё!"
    mc "Зачем мне с ним потом общаться?!"
    voice "mmm/act_1/day_13/0350"
    mmm "Нет, Макс, ты потом с ним опять разговоришься!"
    voice "mmm/act_1/day_13/0351"
    mmm "Опять всё пойдёт по новому кругу."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0352c"
        mmm "Ты же нихрена не изменился."
        mc "Да иди ты к чёрту со своим мнением!"
        mc "Все вы постоянно в меня гадите, нифига не поддерживаете, постоянно пытаетесь увидеть во мне всё самое худшее!"
        mc "И никто из вас, мразей, не может понять, каким человеком я являюсь на самом деле!"
    else:
        voice "mmm/act_1/day_13/0352"
        mmm "Ты же нихера не изменился."
        mc "Да иди ты в жопу со своим мнением!"
        mc "Все вы постоянно в меня гадите, нихера не поддерживаете, постоянно пытаетесь увидеть во мне всё самое худшее!"
        mc "И никто из вас, сука, не может понять, каким человеком я являюсь на самом деле!"
    mc "Вам всем абсолютно плевать, что я кардинально меняюсь каждые полгода и стараюсь становиться лучше!"
    mc "Постоянно приходится из принципа и собственного желания достигать большего результата, чтобы ни одна сволочь не смогла меня обгадить."
    voice "mmm/act_1/day_13/0353"
    mmm "И рано или поздно это тебя сломает к чертям."
    if persistent.censorship:
        mc "И рано или поздно ты пойдёшь откровенно нахрен!"
        mc "Я только нашёл человека, который начал искренне меня ценить, а тут ты, уродливое существо!"
    else:
        mc "И рано или поздно ты пойдёшь откровенно нахуй!"
        mc "Я только нашёл человека, который начал искренне меня ценить, а тут ты, уродливое уёбище!"
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0354"
    mmm "Ты тупой?!" with vpunch
    voice "mmm/act_1/day_13/0355"
    mmm "Отца Моники уже забыл?"
    mc "А мы с Моникой настолько тупые и бестолковые, чтобы не найти способ контактировать?"
    voice "mmm/act_1/day_13/0356"
    mmm "Да."
    show monikammm hcross
    voice "mmm/act_1/day_13/0357"
    mmm "Не поверишь, но да."
    voice "mmm/act_1/day_13/0358"
    mmm "Ты сейчас из себя пока ничего не представляешь."
    mc "Потому что ты так сказала?"
    if persistent.censorship:
        mc "Кто ты вообще, блин, такая?"
        mc "Пригнала хрен пойми куда, стала тут восхвалять своё раздутое эго, показывать, какая ты из себя тут крутая..."
        mc "Чего ты, твою мать, вообще добилась?"
        mc "Впитала в себя дерьмо для последующего его извержения на окружающих?"
    else:
        mc "Кто ты вообще, блять, такая?"
        mc "Пригнала хер пойми куда, стала тут наяривать на своё раздутое эго, показывать, какая ты из себя тут крутая..."
        mc "Чего ты, блять, вообще добилась?"
        mc "Впитала в себя говно для последующего его извержения на окружающих?"
    voice "mmm/act_1/day_13/0359"
    mmm "Добилась того, что держу твои глаза на всю ситуацию открытыми."
    mc "Ага."
    mc "То есть, до этого я жил, всё было прекрасно."
    mc "А тут вдруг ты понадобилась, потому что, ой, внезапно я перестал быть в одиночестве, что твой бестолковый...{w}мозг?...{w}не способен «переварить»."
    show monikammm e3
    voice "mmm/act_1/day_13/0360"
    mmm "Чёрт тебя побери, тупой самоуверенный подросток..."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0361c"
        mmm "Кто-нибудь скажите этому идиоту, что через год у него всё нахрен развалится."
    else:
        voice "mmm/act_1/day_13/0361"
        mmm "Кто-нибудь скажите этому идиоту, что через год у него всё нахер развалится."
    show monikammm e1
    voice "mmm/act_1/day_13/0362"
    mmm "А потом он начнёт пускать сопли и слюни, что у него девушку отобрали."
    play sound hit_wood
    if persistent.censorship:
        mc "Да какая же ты тварь редкостная!" with vpunch
        mc "Лишь бы просто взять и загадить на ровном месте за несуществующее поведение!"
    else:
        mc "Да какая же ты срань ебучая!" with vpunch
        mc "Лишь бы просто взять и обосрать на ровном месте за несуществующее поведение!"
    voice "mmm/act_1/day_13/0363"
    mmm "А тебе лишь бы пропустить всё мимо ушей."
    voice "mmm/act_1/day_13/0364"
    mmm "При таком подходе к жизни ты точно никого не найдёшь."
    mc "...даже если предположим, что с Моникой я расстанусь..."
    mc "А остальные?"
    voice "mmm/act_1/day_13/0365"
    mmm "А чё остальные?"
    voice "mmm/act_1/day_13/0366"
    mmm "Ты с ними общаться будешь?"
    voice "mmm/act_1/day_13/0367"
    mmm "Им с тобой по пути будет?"
    voice "mmm/act_1/day_13/0368"
    mmm "И вообще, ты цепляешься за отношения лишь из-за того, что тебя человек поддерживать стал?"
    mc "..."
    voice "mmm/act_1/day_13/0369"
    mmm "И именно поэтому ты как был один, так и останешься один."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0370c"
        mmm "Ха, пипец, трагедия: ты не найдёшь человека, с которым будешь разделять телесное тепло, заботу и заниматься любовью в придачу."
    else:
        voice "mmm/act_1/day_13/0370"
        mmm "Ха, ебать, трагедия: ты не найдёшь человека, с которым будешь разделять телесное тепло, заботу и трахаться в придачу."
    show monikammm e1
    voice "mmm/act_1/day_13/0371"
    mmm "Прямо прекрасный повод сожрать себя мыслями и сдохнуть, а?"
    mc "По-моему, ты просто уже из принципа хочешь меня обгадить."
    show monikammm hdown
    voice "mmm/act_1/day_13/0372"
    mmm "Конечно!"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0373c"
        mmm "Потому что тебе плевать на мои мысли."
    else:
        voice "mmm/act_1/day_13/0373"
        mmm "Потому что тебе насрать на мои мысли."
    show monikammm hcross
    voice "mmm/act_1/day_13/0374"
    mmm "И на свою будущую жизнь."
    voice "mmm/act_1/day_13/0375"
    mmm "Так же, как и всем людям и на будущее, и на остальных."
    show monikammm e2
    voice "mmm/act_1/day_13/0376"
    mmm "Все вы постоянно преследуете свои хотелки, питая себя собственным эгоизмом."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0377c"
        mmm "А в результате теряете всё нахрен."
        voice "mmm/act_1/day_13/0378c"
        mmm "Но вы же никого слушать не будете, вы же охренеть какие умные."
    else:
        voice "mmm/act_1/day_13/0377"
        mmm "А в результате теряете всё нахуй."
        voice "mmm/act_1/day_13/0378"
        mmm "Но вы же никого слушать не будете, вы же, сука, умные."
    voice "mmm/act_1/day_13/0379"
    mmm "Вот только сколько до вас сломалось, сколько ломается и сколько ещё сломается людей на этой почве."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0380c"
        mmm "Ничерта на ошибках не учитесь."
    else:
        voice "mmm/act_1/day_13/0380"
        mmm "Нихера на ошибках не учитесь."
    voice "mmm/act_1/day_13/0381"
    mmm "Пытаетесь обвинить остальных в своих же ошибках и недостатках."
    show monikammm e3
    voice "mmm/act_1/day_13/0382"
    mmm "И ещё лезете в политику, в различные движения, во всякое такое..."
    show monikammm e1
    voice "mmm/act_1/day_13/0383"
    mmm "Да во взрослую жизнь в целом!"
    show monikammm laside
    voice "mmm/act_1/day_13/0384"
    mmm "А вот если сбросить всю эту мишуру, которую вы на себя накрутили, и вскрыть вашу душу «ножом»?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0385"
    mmm "Заглянуть во внутрь?"
    voice "mmm/act_1/day_13/0386"
    mmm "Что мы там обнаружим?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0387"
    mmm "А обнаружим такое гнилое дерьмо, которое воняет аж за километр."
    voice "mmm/act_1/day_13/0388"
    mmm "Причём настолько сильно, что задаёшься вопросом: \"А как у вас хватало наглости верещать на публику и указывать остальным, что делать?\"."
    show monikammm e2
    voice "mmm/act_1/day_13/0388d1"
    mmm "Хотя я бы даже сказала не гнилое дерьмо, а какая-то наивная маленькая детская травма."
    voice "mmm/act_1/day_13/0388d2"
    mmm "Травма, связанная с грубостью или наплевательством родителей, которые не смогли воспитать из своего ребёнка нормального человека."
    show monikammm e1
    voice "mmm/act_1/day_13/0388d3"
    mmm "А «ребёнок» в свою же очередь из-за слабости не смог перебороть эту травму."
    voice "mmm/act_1/day_13/0388d4"
    mmm "И теперь пытается отыграться на остальных, потому что его «уязвленная душонка» не может избавиться от боли из-за себя же."
    voice "mmm/act_1/day_13/0389"
    mmm "Вы же никогда не признаете свои ошибки."
    voice "mmm/act_1/day_13/0390"
    mmm "Вы всегда будете пытаться прикрываться чем угодно, лишь бы не нести ответственность за свои недостатки и уж, тем более, исправлять их."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0391c"
        mmm "И после этого у вас есть наглость лезть к другим, гадить в других и упрекать их, что они не соответствуют вашему мировоззрению."
    else:
        voice "mmm/act_1/day_13/0391"
        mmm "И после этого у вас есть наглость лезть к другим, срать в других и упрекать их, что они не соответствуют вашему мировоззрению."
    voice "mmm/act_1/day_13/0392"
    mmm "Да кто обязан следовать вашему больному «манямирку»?"
    voice "mmm/act_1/day_13/0393"
    mmm "Вы сделали что-то полезное для общества, за что вас можно уважать?"
    voice "mmm/act_1/day_13/0394"
    mmm "Уверена, что нет."
    voice "mmm/act_1/day_13/0395"
    mmm "Вы пытались искренне помочь людям с их проблемами?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0396c"
        mmm "Уж точно нихрена."
    else:
        voice "mmm/act_1/day_13/0396"
        mmm "Уж точно нихера."
    voice "mmm/act_1/day_13/0397"
    mmm "А вы вообще пытались себя исправить в лучшую сторону и стать примером для подражания, чтобы люди за вами потянулись?"
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0398"
    mmm "СОВЕРШЕННО НЕТ!" with vpunch
    voice "mmm/act_1/day_13/0399"
    mmm "Ведь зачем?"
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0400c"
        mmm "Можно же просто гадить и ничего не делать."
    else:
        voice "mmm/act_1/day_13/0400"
        mmm "Можно же просто срать и ничего не делать."
    voice "mmm/act_1/day_13/0401"
    mmm "Напрягаться слишком сложно и трудозатратно, не так ли?"
    voice "mmm/act_1/day_13/0402"
    mmm "А ещё, кстати, я более чем уверена, что если бы я была в реальном мире и мои слова попали бы на общее обозрение..."
    show monikammm e2
    voice "mmm/act_1/day_13/0403"
    mmm "Допустим, в какую-нибудь популярную соцсеть."
    show monikammm e3
    voice "mmm/act_1/day_13/0404"
    mmm "...то тогда бы столько дерьма бы вылилось и такое бы пламя от горящих задниц было..."
    show monikammm e1
    voice "mmm/act_1/day_13/0405"
    mmm "И никто не захотел бы осознать свои недостатки и исправить их, чтобы стать лучше."
    voice "mmm/act_1/day_13/0406"
    mmm "Для других."
    show monikammm e2
    voice "mmm/act_1/day_13/0407"
    mmm "И для себя, в первую очередь."
    show monikammm e1
    voice "mmm/act_1/day_13/0408"
    mmm "Так что, продолжишь и дальше закрывать глаза на свои недостатки, наивно надеясь на то, что другие люди помогут тебе их исправить..."
    voice "mmm/act_1/day_13/0409"
    mmm "...или возьмёшься за свою бестолковую голову, пока не поздно?"
    mc "..."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0410c"
        mmm "Блин, Макс, ну серьёзно."
    else:
        voice "mmm/act_1/day_13/0410"
        mmm "Блять, Макс, ну серьёзно."
    show monikammm laside
    voice "mmm/act_1/day_13/0411"
    mmm "Ты хочешь строить свою жизнь в этом мире?"
    voice "mmm/act_1/day_13/0412"
    mmm "Ты понимаешь, сколько здесь всякой грязи?"
    show monikammm e2 hdown
    voice "mmm/act_1/day_13/0413"
    mmm "Убийства, рабство, природные бедствия, продажность, наплевательство..."
    show monikammm e1
    voice "mmm/act_1/day_13/0414"
    mmm "И ты хочешь, чтобы кого-то из твоих родных это задело?"
    voice "mmm/act_1/day_13/0415"
    mmm "Твоего будущего ребёнка?"
    voice "mmm/act_1/day_13/0416"
    mmm "Ты реально этого хочешь?"
    mc "...с чего ты решила, что я буду настолько наивным и слабым, что попадусь на такое?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0417"
    mmm "Ха, ты очень сильно недооцениваешь такие вещи."
    voice "mmm/act_1/day_13/0418"
    mmm "Иногда даже делать ничего не нужно, чтобы в них попасть."
    show monikammm e2
    voice "mmm/act_1/day_13/0419"
    mmm "И из них потом очень тяжело выбраться."
    show monikammm e1
    voice "mmm/act_1/day_13/0420"
    mmm "Так неужели ты хочешь построить свою семью, чтобы рано или поздно она попала в нечто такое?"
    voice "mmm/act_1/day_13/0421"
    mmm "Это буквально наплевательство с твоей стороны, Макс."
    mc "..."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0422c"
        mmm "Или хочешь, чтобы потом твой ребёнок попал в школу, а там уже варился среди малолетних идиотов?"
        voice "mmm/act_1/day_13/0423c"
        mmm "Это же неизбежное дерьмо."
    else:
        voice "mmm/act_1/day_13/0422"
        mmm "Или хочешь, чтобы потом твой ребёнок попал в школу, а там уже варился среди малолетних ебанатов?"
        voice "mmm/act_1/day_13/0423"
        mmm "Это же неизбежное говно."
    show monikammm e3
    voice "mmm/act_1/day_13/0424"
    mmm "Просто иногда оно менее выражено, а иногда..."
    show monikammm e1
    voice "mmm/act_1/day_13/0425"
    mmm "...в общем, никто не может решить эту проблему."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0426c"
        mmm "Потому что, первое -- чёртовы гормоны, второе -- не менее чёртовые родители, неспособные нормально воспитать таких вот...{w=5.5}отпрысков."
    else:
        voice "mmm/act_1/day_13/0426"
        mmm "Потому что, первое -- ёбаные гормоны, второе -- не менее ёбаные родители, неспособные нормально воспитать таких вот...{w=5.5}отпрысков."
    show monikammm e2
    voice "mmm/act_1/day_13/0427"
    mmm "Блин, это слово прямо идеально подходит."
    voice "mmm/act_1/day_13/0428"
    mmm "Не ребёнок, не подросток, а отпрысок."
    voice "mmm/act_1/day_13/0429"
    mmm "Будто его непроизвольно серенькнули непонятно где, а не родили в роддоме."
    show monikammm e1
    voice "mmm/act_1/day_13/0430"
    mmm "Хотя о чём тут вообще говорить?"
    voice "mmm/act_1/day_13/0431"
    mmm "Если среди взрослых, даже состоявшихся людей, находятся имбицилы, которые на серьёзных щах смеются над психическими травмами."
    show monikammm laside
    voice "mmm/act_1/day_13/0432"
    mmm "Вот взять ту же депрессию."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0433c"
        mmm "С каких это пор самое НАИХРЕНОВЕЙШЕЕ, что может случиться с человеком, стало объектом для шуток?"
    else:
        voice "mmm/act_1/day_13/0433"
        mmm "С каких это пор самое НАИХЕРОВЕЙШЕЕ, что может случиться с человеком, стало объектом для шуток?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0434"
    mmm "Тогда давайте смеяться с инвалидов, которым оторвало руки или ноги."
    voice "mmm/act_1/day_13/0435"
    mmm "Или над человеком, которому разрезали сонную артерию и из которой хлещет гигантская струя алой крови под давлением."
    show monikammm hdown
    voice "mmm/act_1/day_13/0436"
    mmm "Прямо как у фонтана «Писующий мальчик»!"

    call nightmare_act_1_day_13_monikammm_smile("on", True)

    voice "mmm/act_1/day_13/0437"
    mmm "ХА-ХА-ХА-ХА-ХА!"
    voice "mmm/act_1/day_13/0438"
    mmm "ХА-ХА-ХА-ХА-ХА-ХА-ХА!"
    voice "mmm/act_1/day_13/0439"
    mmm "ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!"
    voice "mmm/act_1/day_13/0440"
    mmm "ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!"
    voice "mmm/act_1/day_13/0441"
    mmm "ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!"

    call nightmare_act_1_day_13_monikammm_smile("off", False)

    mc "............"
    voice "mmm/act_1/day_13/0442"
    mmm "А чё не ржёшь-то, Макс?"
    play sound hit_wood
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0443c"
        mmm "Смешно ж, твою мать!" with vpunch
    else:
        voice "mmm/act_1/day_13/0443"
        mmm "Смешно ж, блять!" with vpunch
    show monikammm laside
    voice "mmm/act_1/day_13/0444"
    mmm "Шутка, шутеечка, смехуёвинка."
    show monikammm e2 hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0445c"
        mmm "Или какими вы там словами своё дерьмо прикрываете..."
    else:
        voice "mmm/act_1/day_13/0445"
        mmm "Или какими вы там словами своё говно прикрываете..."
    show monikammm e1 hcross
    voice "mmm/act_1/day_13/0446"
    mmm "Хотя самое забавное и ироничное, что когда с этими вот нелюдьми случается нечто подобное, то они вопят и верещат, как им больно, какие они бедные, бла-бла-бла."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0447c"
        mmm "Однако это показывает, что жизнь отплачивает каждому, без исключения."
    else:
        voice "mmm/act_1/day_13/0447"
        mmm "Однако это показывает, что жизнь ебёт всех и каждого, без исключения."
    voice "mmm/act_1/day_13/0448"
    mmm "По справедливости, кто бы что ни говорил."
    show monikammm e3
    voice "mmm/act_1/day_13/0449"
    mmm "Правда, единственный минус -- это растянутое время."
    voice "mmm/act_1/day_13/0450"
    mmm "Иногда жизнь очень запаздывает, что очень печально..."
    show monikammm e1
    voice "mmm/act_1/day_13/0451"
    mmm "Кстати, да."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0452c"
        mmm "Всё вот это дерьмо происходит от той же безнаказанности."
    else:
        voice "mmm/act_1/day_13/0452"
        mmm "Всё вот это говно происходит от той же безнаказанности."
    voice "mmm/act_1/day_13/0453"
    mmm "Не устану повторять, что люди, как огня, боятся нести ответственность за свои поступки."
    show monikammm e2
    voice "mmm/act_1/day_13/0454"
    mmm "Ради избежания наказания они готовы находить единомышленников, чтобы создать эффект правды от толпы..."
    show monikammm e1
    voice "mmm/act_1/day_13/0455"
    mmm "Короче, чтобы было кому их поддержать."
    voice "mmm/act_1/day_13/0456"
    mmm "А как только таких людей ловят и наказывают по всей строгости, так сразу вся толпа улетучивается, а её зачинщик ведёт себя тише воды, ниже травы."
    voice "mmm/act_1/day_13/0457"
    mmm "Потому что уже некому скинуть свою ответственность на кого-то другого, как горячую картошку."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0458c"
        mmm "Таким нужна «коллективная ответственность», которая размазывается тонким слоем на каждого, благодаря чему истинный виновник нихрена не получает за свои деяния."
    else:
        voice "mmm/act_1/day_13/0458"
        mmm "Таким нужна «коллективная ответственность», которая размазывается тонким слоем на каждого, благодаря чему истинный виновник нихера не получает за свои деяния."
    show monikammm e1
    voice "mmm/act_1/day_13/0459"
    mmm "И вот такие вот мрази заставляют нормальных людей жить по их правилам."
    voice "mmm/act_1/day_13/0460"
    mmm "Зашибись, не правда ли?"
    voice "mmm/act_1/day_13/0461"
    mmm "И ты среди таких нелюдей хочешь растить своего ребёнка?"
    mc "...ты слишком всё очерняешь."
    mc "И не пытаешься найти что-то светлое."
    voice "mmm/act_1/day_13/0462"
    mmm "...сказал человек, у которого пратически никого не было."
    voice "mmm/act_1/day_13/0463"
    mmm "Даже светлых воспоминаний."
    voice "mmm/act_1/day_13/0464"
    mmm "Вот что-то светлое у тебя со школой было?"
    voice "mmm/act_1/day_13/0465"
    mmm "С детстким садом, хм?"
    voice "mmm/act_1/day_13/0466"
    mmm "Мы же уже поднимали похожий вопрос."
    mc "..."
    voice "mmm/act_1/day_13/0467"
    mmm "{b}Не было у тебя ничего.{/b}"
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0468c"
        mmm "Всегда происходила какая-то хрень."
        voice "mmm/act_1/day_13/0469c"
        mmm "И эта хрень всё портила."
    else:
        voice "mmm/act_1/day_13/0468"
        mmm "Всегда происходила какая-то херня."
        voice "mmm/act_1/day_13/0469"
        mmm "И эта херня всё портила."
    show monikammm e1
    voice "mmm/act_1/day_13/0470"
    mmm "Понимаешь, Макс, на людей нельзя надеяться."
    voice "mmm/act_1/day_13/0471"
    mmm "В них как были изъяны, так в них и останутся, что бы они ни делали."
    voice "mmm/act_1/day_13/0472"
    mmm "Всегда их будет гнать вперёд эгоизм."
    voice "mmm/act_1/day_13/0473"
    mmm "Всегда они хотят признания."
    voice "mmm/act_1/day_13/0474"
    mmm "Они неспособны жить в одиночестве и отстаивать себя."
    voice "mmm/act_1/day_13/0475"
    mmm "Вот взять тех же клоунов, которые в Интернете встречаются повсеместно."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0476c"
        mmm "Всё, что они умеют -- это только нести хрень, пускать идиотские шутки, постоянно привлекать к себе внимание..."
    else:
        voice "mmm/act_1/day_13/0476"
        mmm "Всё, что они умеют -- это только нести херню, пускать идиотские шутки, постоянно привлекать к себе внимание..."
    show monikammm e1
    voice "mmm/act_1/day_13/0477"
    mmm "А почему?"
    voice "mmm/act_1/day_13/0478"
    mmm "Потому что общество этот идиотизм полностью устраивает."
    voice "mmm/act_1/day_13/0479"
    mmm "Иными словами, оно поощряет лёгкий путь к признанию и получению внимания."
    show monikammm e3
    voice "mmm/act_1/day_13/0480"
    mmm "И стоит только какому-то человеку сказать, что клоун находится в гнилом положении..."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0481c"
        mmm "...так сразу этот клоун начинает в него гадить или бежать к своему недосоциуму за спину."
    else:
        voice "mmm/act_1/day_13/0481"
        mmm "...так сразу этот клоун начинает в него срать или бежать к своему недосоциуму за спину."
    show monikammm e1
    voice "mmm/act_1/day_13/0482"
    mmm "Ведь он же прекрасно знает, что социум ему поможет, потому что социум на его стороне."
    voice "mmm/act_1/day_13/0483"
    mmm "А на его стороне почему?"
    voice "mmm/act_1/day_13/0484"
    mmm "Потому что этому обществу нужны клоуны для разрядки эмоций."

    call nightmare_act_1_day_13_monikammm_smile("on", False)

    if persistent.censorship:
        voice "mmm/act_1/day_13/0485c"
        mmm "{bt=4}Пук-среньк, мы сборище придурков под\nназванием «недообщество».{/bt}"
    else:
        voice "mmm/act_1/day_13/0485"
        mmm "{bt=4}Пук-среньк, мы сборище долбоёбов под\nназванием «недообщество».{/bt}"
    voice "mmm/act_1/day_13/0486"
    mmm "{bt=4}Нам очень нужно снимать эмоциональную\nразрядку, хнык-хнык.{/bt}"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0487c"
        mmm "{bt=4}Нам это так позарез нужно, будто мы хотим\nпередёрнуть свой хрен, вот только спускать\nнекуда.{/bt}"
        voice "mmm/act_1/day_13/0488c"
        mmm "{bt=4}Нам нужен такой же придурок, но только ещё\nтупее и смешнее, чтобы каждый из нас мог\nпоглумиться над ним, хы-хы.{/bt}"
        voice "mmm/act_1/day_13/0489c"
        mmm "{bt=4}Этот придурок будет нашим эмоциональным\nпрезервативом, в который мы будем спускать\nдерьмо.{/bt}"
        voice "mmm/act_1/day_13/0490c"
        mmm "{bt=4}Спускать до такой степени, пока он весь не\nиздерьмится и не порвётся, плаки-плаки.{/bt}"
        voice "mmm/act_1/day_13/0491c"
        mmm "{bt=4}И когда он порвётся, мы выбросим его на\nпомойку нахрен, потому что такой придурок нам\nбольше будет не нужен.{/bt}"
    else:
        voice "mmm/act_1/day_13/0487"
        mmm "{bt=4}Нам это так позарез нужно, будто мы хотим\nпередёрнуть свой член, вот только кончать\nнекуда.{/bt}"
        voice "mmm/act_1/day_13/0488"
        mmm "{bt=4}Нам нужен такой же долбоёб, но только ещё\nтупее и смешнее, чтобы каждый из нас мог\nпоглумиться над ним, хы-хы.{/bt}"
        voice "mmm/act_1/day_13/0489"
        mmm "{bt=4}Этот долбоёб будет нашим эмоциональным\nпрезервативом, в который мы будем кончать\nдерьмом.{/bt}"
        voice "mmm/act_1/day_13/0490"
        mmm "{bt=4}Кончать до такой степени, пока он весь не\nизговнится и не порвётся, плаки-плаки.{/bt}"
        voice "mmm/act_1/day_13/0491"
        mmm "{bt=4}И когда он порвётся, мы выбросим его на\nпомойку нахуй, потому что такой долбоёб нам\nбольше будет не нужен.{/bt}"
    voice "mmm/act_1/day_13/0492"
    mmm "{bt=4}И мы будем искать себе нового, хы-хы.{/bt}"

    call nightmare_act_1_day_13_monikammm_smile("off", False)

    show monikammm laside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0493c"
        mmm "И вот хоть об стенку треснись, ты никогда не сможешь помочь этому недочеловеку стать нормальным, потому что ему нравится быть куском дерьма."
    else:
        voice "mmm/act_1/day_13/0493"
        mmm "И вот хоть об стенку треснись, ты никогда не сможешь помочь этому недочеловеку стать нормальным, потому что ему нравится быть куском говна."
    show monikammm hdown
    voice "mmm/act_1/day_13/0494"
    mmm "Он сам выбрал этот...{w=0.65}путь."
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0495c"
        mmm "А раз это его выбор, то пусть мучится с ним сам, ведь ответственность никто не отменял."
    else:
        voice "mmm/act_1/day_13/0495"
        mmm "А раз это его выбор, то пусть ебётся с ним сам, ведь ответственность никто не отменял."
    show monikammm e2
    voice "mmm/act_1/day_13/0496"
    mmm "Хотя какая у таких нелюдей «ответственность»..."
    show monikammm e1
    voice "mmm/act_1/day_13/0497"
    mmm "У таких нелюдей даже понятия слова «совесть» отсутствует."
    voice "mmm/act_1/day_13/0498"
    mmm "Да и вообще понимание чего-нибудь светлого."
    voice "mmm/act_1/day_13/0499"
    mmm "Они никогда не будут ценить добро в их сторону."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0500c"
        mmm "Найдут 3000 причин изгадить того, кто осмелился им помочь."
    else:
        voice "mmm/act_1/day_13/0500"
        mmm "Найдут 3000 причин изговнить того, кто осмелился им помочь."
    show monikammm e2
    voice "mmm/act_1/day_13/0501"
    mmm "Ха, да и тут то же самое будет, что я говорила про соцсеть."
    show monikammm e1
    voice "mmm/act_1/day_13/0502"
    mmm "Если бы мои слова каким-то образом дошли до условного такого идиота, то он бы меня не послушал."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0503c"
        mmm "Напротив, он бы начал дерьмиться, визжать и орать, что всё это неправда, ведь он белый и пушистый..."
    else:
        voice "mmm/act_1/day_13/0503"
        mmm "Напротив, он бы начал говниться, визжать и орать, что всё это неправда, ведь он белый и пушистый..."
    show monikammm e3
    voice "mmm/act_1/day_13/0504"
    mmm "Ну или молчать позорно."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0505c"
        mmm "В общем, пошли бы эти существа тоже нахрен."
    else:
        voice "mmm/act_1/day_13/0505"
        mmm "В общем, пошли бы эти существа тоже нахер."
    voice "mmm/act_1/day_13/0506"
    mmm "Как и все недообщества."
    voice "mmm/act_1/day_13/0507"
    mmm "Что мы тут на них распинаемся?"
    voice "mmm/act_1/day_13/0508"
    mmm "Они никогда ничего не добьются в своей жизни, поскольку не стремятся быть лучше."
    voice "mmm/act_1/day_13/0509"
    mmm "Их всё устраивает."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0510c"
        mmm "Так ещё и потом сдохнут в условной канаве через несколько десятков лет, так ничего, кроме выливания дерьма на окружающих, не добившись."
    else:
        voice "mmm/act_1/day_13/0510"
        mmm "Так ещё и потом сдохнут в условной канаве через несколько десятков лет, так ничего, кроме выливания говна на окружающих, не добившись."
    mc "...и где же тогда найти нормальное общество?"
    show monikammm e1
    voice "mmm/act_1/day_13/0511"
    mmm "Нигде."
    voice "mmm/act_1/day_13/0512"
    mmm "Ты никогда его не найдёшь."
    voice "mmm/act_1/day_13/0513"
    mmm "Даже если сделаешь своё полностью с нуля."
    play sound hit_wood
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0514c"
        mmm "Макс, люди идут нахрен!" with vpunch
    else:
        voice "mmm/act_1/day_13/0514"
        mmm "Макс, люди идут нахер!" with vpunch
    voice "mmm/act_1/day_13/0515"
    mmm "Прими этот факт."
    voice "mmm/act_1/day_13/0516"
    mmm "Хватит за них цепляться."
    show monikammm hcross
    voice "mmm/act_1/day_13/0517"
    mmm "Вот честно, тебе плевать на бедных людей, особенно живущих в Африке?"
    voice "mmm/act_1/day_13/0518"
    mmm "Да, плевать, ты даже о них не думаешь."
    voice "mmm/act_1/day_13/0519"
    mmm "Тебе плевать на животных, над которыми издеваются или о которых люди не могут нормально позаботиться ввиду своей безответственности?"
    voice "mmm/act_1/day_13/0520"
    mmm "Бедные домашние хомячки передают привет."
    voice "mmm/act_1/day_13/0521"
    mmm "Такая мысль у тебя даже в голове не поднималась."
    show monikammm e2
    voice "mmm/act_1/day_13/0522"
    mmm "Про издевательство над людьми, в том числе и рабство, я вообще молчу."
    show monikammm e1
    voice "mmm/act_1/day_13/0523"
    mmm "Но зато тебе почему-то не плевать на близлежайшее окружение."
    voice "mmm/act_1/day_13/0524"
    mmm "Воняет лицемерием, не находишь?"
    mc "Невозможно переживать за всё и вся."
    mc "У меня бы сгорела нервная система от этого, буквально."
    mc "И кто мне мешает помочь близким людям?"
    voice "mmm/act_1/day_13/0525"
    mmm "...отсутствие собственной основы и взваливание большой ответственности на себя."
    voice "mmm/act_1/day_13/0526"
    mmm "Ты вообще думал, когда решился взяться за проблемы участниц Литературного клуба?"
    voice "mmm/act_1/day_13/0527"
    mmm "Ты понимаешь, что будет, если ты провалишь их ожидания?"
    voice "mmm/act_1/day_13/0528"
    mmm "Понимаешь, какой удар по ним будет?"
    mc "Да."
    voice "mmm/act_1/day_13/0529"
    mmm "Не-е-ет..."
    play sound hit_wood
    mc "{sc=3}ДА!{/sc}" with vpunch
    show monikammm hdown
    mc "И вместо того, чтобы дать мне силы, ты пытаешься меня загнобить."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0530c"
        mmm "Повторяю ещё раз, но другими словами: я гнобила тебя за эмпатию лишь потому, что ты ещё ничерта не сформировался."
    else:
        voice "mmm/act_1/day_13/0530"
        mmm "Повторяю ещё раз, но другими словами: я гнобила тебя за эмпатию лишь потому, что ты ещё нихера не сформировался."
    voice "mmm/act_1/day_13/0531"
    mmm "Не вырос!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0532"
    mmm "А уже стремишься другим помочь."
    voice "mmm/act_1/day_13/0533"
    mmm "Логично, что рано или поздно ты из-за этого сломаешься."
    voice "mmm/act_1/day_13/0534"
    mmm "Вот когда уже сформируешься и добьёшься нормальной жизни, то делай, что хочешь, но в рамках приличия."
    show monikammm laside
    voice "mmm/act_1/day_13/0535"
    mmm "Хоть другим помогай, хоть семью заводи."
    show monikammm hdown
    mc "Так пока я сформируюсь, будет уже ПОЗДНО!"
    show monikammm hcross
    mc "Ты понимаешь, что бездействие может породить у участниц необратимые психические проблемы вплоть до смерти?!"
    voice "mmm/act_1/day_13/0536"
    mmm "А тебе не кажется, что ты слишком преувеличиваешь?"
    play sound hit_wood
    mc "{sc=3}ПРЕУВЕЛИЧИВАЮ?!{/sc}" with vpunch
    voice "mmm/act_1/day_13/0537"
    mmm "Да."
    voice "mmm/act_1/day_13/0538"
    mmm "Если бы всё так было серьёзно, то мы бы все уже давно сдохли."
    show monikammm raside
    voice "mmm/act_1/day_13/0539"
    mmm "Ты видел на Нацуки хоть один синяк от отца?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0540"
    mmm "Ну или прямо реально подтверждённый случай того, что отец применял физическое и психологическое насилие?"
    mc "..."
    voice "mmm/act_1/day_13/0541"
    mmm "Именно, не видел."
    show monikammm laside
    voice "mmm/act_1/day_13/0542"
    mmm "Ты понимаешь, что у Сайори просто запоздалый кризис подросткового возраста?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0543"
    mmm "Причём из-за того, что вы все с ней няньчитесь."
    mc "А если она сломается?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0544"
    mmm "Тогда она сломается."
    voice "mmm/act_1/day_13/0545"
    mmm "Добро пожаловать во взрослую жизнь."
    mc "..."
    show monikammm raside
    voice "mmm/act_1/day_13/0546"
    mmm "Ты понимаешь, что у Юри просто всё из-за гормонов, которых явно больше, чем у других?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0547"
    mmm "Ну и банально короткого промежутка времени со дня\nтрагедии -- гибели её отца."
    show monikammm laside
    voice "mmm/act_1/day_13/0548"
    mmm "А понимаешь, что Монике надо строить свою карьеру, чтобы добиться нормальной жизни?"
    show monikammm hdown
    mc "А ты понимаешь, что ты просто превратилась в мразь, которая всех хочет кинуть?"
    mc "Но напрямую всё никак сказать не может, постоянно чем-то прикрывается."
    show monikammm hcross
    mc "Кто мне мешает развиваться попутно, а?"
    voice "mmm/act_1/day_13/0549"
    mmm "И хорошо ли ты развивался до этого момента?"
    voice "mmm/act_1/day_13/0550"
    mmm "Всё, что в тебе было, -- желание к кому-то примкнуться."
    voice "mmm/act_1/day_13/0551"
    mmm "Лишь потому, что хотелось веселья, общения, понимания и поддержки."
    mc "..."
    voice "mmm/act_1/day_13/0552"
    mmm "Видишь?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0553c"
        mmm "Каким образом ты хотел найти человека со схожими интересами, если вы все постоянно собачитесь друг с другом из-за этих же интересов?"
    else:
        voice "mmm/act_1/day_13/0553"
        mmm "Каким образом ты хотел найти человека со схожими интересами, если вы все постоянно срётесь друг с другом из-за этих же интересов?"
    voice "mmm/act_1/day_13/0554"
    mmm "Понимаешь, насколько наивным и глупым ты мне кажешься?"
    mc "Если бы у нас не было людей со схожими интересами, то мы бы ВСЕ никогда не общались друг с другом."
    voice "mmm/act_1/day_13/0555"
    mmm "Да неужели?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0556c"
        mmm "А конфликты -- офигеть какое прекрасное общение, да?"
    else:
        voice "mmm/act_1/day_13/0556"
        mmm "А срачи -- охереть какое прекрасное общение, да?"
    show monikammm e2
    voice "mmm/act_1/day_13/0557"
    mmm "Хотя некоторые клоуны и мудаки сказали бы: \"Да\"..."
    show monikammm e1
    voice "mmm/act_1/day_13/0558"
    mmm "Но их мнение не учитывается."
    mc "И почему же я никогда не найду людей со схожими интересами?"
    voice "mmm/act_1/day_13/0559"
    mmm "Потому что их очень мало."
    voice "mmm/act_1/day_13/0560"
    mmm "А с набором, похожим на твой, -- тем более."
    voice "mmm/act_1/day_13/0561"
    mmm "И пока ты будешь помыкаться и искать таких людей, ты гарантированно отхватишь дерьмище в свою сторону."
    voice "mmm/act_1/day_13/0562"
    mmm "Потому что за время твоих поисков найдётся тот, кто обосрёт твои интересы."
    show monikammm e2
    voice "mmm/act_1/day_13/0563"
    mmm "А потом найдётся тот, кто обосрёт того, кто обосрал твои интересы."
    show monikammm e3
    voice "mmm/act_1/day_13/0564"
    mmm "А ещё позже найдётся тот, кто обосрёт того, кто обосрал того, кто обосрал твои интересы."
    show monikammm e1
    voice "mmm/act_1/day_13/0565"
    mmm "И так до бесконечности."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0566c"
        mmm "Вы же все засранцы."
    else:
        voice "mmm/act_1/day_13/0566"
        mmm "Вы же все мудаки."
    voice "mmm/act_1/day_13/0567"
    mmm "Грубые, алчные, эгоистичные."
    voice "mmm/act_1/day_13/0568"
    mmm "Особенно прекрасно это раскрывается в Интернете."
    show monikammm e2
    voice "mmm/act_1/day_13/0569"
    mmm "Очень прекрасное место, скажу я тебе."
    show monikammm e1
    voice "mmm/act_1/day_13/0570"
    mmm "Потому что оно даёт людям чувство ложной безнаказанности."
    voice "mmm/act_1/day_13/0571"
    mmm "Что, в свою очередь, порождает их «открытие», выливающее всю их внутреннюю гниль наружу."
    show monikammm e3
    voice "mmm/act_1/day_13/0572"
    mmm "Особенно забавляет, когда они начинают что-то «критиковать»."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0573c"
        mmm "Со всеми матами, конфликтами и грязью вместо конструктивной критики."
    else:
        voice "mmm/act_1/day_13/0573"
        mmm "Со всеми матами, срачами и говнищем вместо конструктивной критики."
    show monikammm e1
    voice "mmm/act_1/day_13/0574"
    mmm "Потому что они просто хотят кого-то унизить, чтобы потешить своё никому ненужное эго."
    voice "mmm/act_1/day_13/0575"
    mmm "Ненужное лишь потому, что если бы у них была хорошая и счастливая жизнь, то они такой бы хренью не занимались."
    voice "mmm/act_1/day_13/0576"
    mmm "Так вот, всё это они прикрывают волшебным словом «Интернет»."
    show monikammm e2
    voice "mmm/act_1/day_13/0577"
    mmm "Вот только..."
    show monikammm e1
    voice "mmm/act_1/day_13/0578"
    mmm "А кто сказал, что свобода равняется вседозволенности?"
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0579"
    mmm "Кто отменял мораль и взаимоуважение?" with vpunch
    if persistent.censorship:
        voice "mmm/act_1/day_13/0580c"
        mmm "Вам на неё плевать?"
    else:
        voice "mmm/act_1/day_13/0580"
        mmm "Вам на неё насрать?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0581"
    mmm "А если вас выдернуть через экран и посадить перед собой, особенно в людном месте, где каждый будет видеть вас и слышать всё, что вы говорите?"
    voice "mmm/act_1/day_13/0582"
    mmm "Уже бы себя так распущенно не вели, а?"
    show monikammm e2
    voice "mmm/act_1/day_13/0583"
    mmm "Может быть, хоть тогда люди станут чуточку чище от внутренней грязи."
    show monikammm e1
    voice "mmm/act_1/day_13/0584"
    mmm "Ведь когда за слова и поступки может прилететь, тогда становится страшно за свою задницу, не так ли?"
    mc "...здесь согласен."
    voice "mmm/act_1/day_13/0585"
    mmm "Ну хоть где-то, уже прогресс."
    if persistent.censorship:
        mc "Но, чёрт побери..."
    else:
        mc "Но, блять..."
    mc "У нас же куча разных франшиз, произведений..."
    mc "А в совокупности с Интернетом шанс встретить людей с общим интересом растёт в геометрической прогрессии."
    mc "Твои доводы на этом фоне выглядят, как подростковый максимализм."
    voice "mmm/act_1/day_13/0586"
    mmm "...и нашёл ли ты кого-нибудь со схожими интересами?"
    mc "..."
    voice "mmm/act_1/day_13/0587"
    mmm "Блин, тебя так легко каждый раз в нокаут отправлять, ты бы знал..."
    voice "mmm/act_1/day_13/0588"
    mmm "Всё это ваше разнообразие франшиз приводит лишь к увеличению количества срачей."
    show monikammm e3
    voice "mmm/act_1/day_13/0589"
    mmm "Потому что чрезмерная популярность, с одной стороны, хорошо рекламирует франшизу, но с другой..."
    show monikammm e1
    voice "mmm/act_1/day_13/0590"
    mmm "...она слишком часто появляется абсолютно где угодно, особенно там, где не надо."
    voice "mmm/act_1/day_13/0591"
    mmm "Из-за чего возникают срачи, так ещё и репутация франшизы начинает медленно скатываться вниз."
    voice "mmm/act_1/day_13/0592"
    mmm "Да и вообще, ты видел её фанатов или тех, кто ею увлекается?"
    show monikammm laside
    voice "mmm/act_1/day_13/0593"
    mmm "Это иногда буквально превращается в фанатизм."
    show monikammm hdown
    voice "mmm/act_1/day_13/0594"
    mmm "Они даже не замечают, как позорят её своим поведением, прикрываясь своей любовью к произведению."
    show monikammm e2
    voice "mmm/act_1/day_13/0595"
    mmm "То приписывают персонажам хрен пойми что: начиная от внешнего вида и заканчивая какими-то идиотскими хэдканонами."
    show monikammm e1
    voice "mmm/act_1/day_13/0596"
    mmm "Это слово даже звучит противно..."
    show monikammm e3
    voice "mmm/act_1/day_13/0597"
    mmm "То увеличивают сахарность и соплежуйство, особенно если франшиза в стилистике аниме, плюс в розовых цветах."
    show monikammm e1
    voice "mmm/act_1/day_13/0598"
    mmm "Серьёзно, иногда это поведение выглядит так, будто 14-летние девочки дорвались до Интернета и научились пользоваться фоторедактором."
    show monikammm e2 hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0599c"
        mmm "Ха, ещё эти \"девочки\" потом так плюются, когда ты на них хоть как-то наезжаешь..."
        show monikammm e1
        voice "mmm/act_1/day_13/0600c"
        mmm "И вот они нихрена не осознают, что своей «безумной любовью» к франшизе позорят эту же франшизу."
    else:
        voice "mmm/act_1/day_13/0599"
        mmm "Ха, ещё эти \"девочки\" потом так говнятся, когда ты на них хоть как-то наезжаешь..."
        show monikammm e1
        voice "mmm/act_1/day_13/0600"
        mmm "И вот они нихрена не осознают, что своей «безумной любовью» к франшизе позорят эту же, блять, франшизу."
    voice "mmm/act_1/day_13/0601"
    mmm "Ну не идиотизм ли?"
    show monikammm e2
    voice "mmm/act_1/day_13/0602"
    mmm "И ладно, хрен с ними, пусть занимаются, чем хотят, но когда это выходит на общее обозрение..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0603c"
        mmm "Логично, что люди видят какую-то хрень, а потом начинают, в лучшем случае, со скептецизмом относиться к франшизе."
    else:
        voice "mmm/act_1/day_13/0603"
        mmm "Логично, что люди видят какую-то херню, а потом начинают, в лучшем случае, со скептецизмом относиться к франшизе."
    voice "mmm/act_1/day_13/0604"
    mmm "И самое мерзкое, что когда их период увлечения пройдёт, то они выбросят эту франшизу из своей башки и переключатся на что-то другое."
    voice "mmm/act_1/day_13/0605"
    mmm "Но франшиза продолжит существовать."
    voice "mmm/act_1/day_13/0606"
    mmm "Только уже в облёванном виде, из-за чего остальные люди начинают на неё плеваться, когда она этого всего вообще не заслуживает."
    voice "mmm/act_1/day_13/0607"
    mmm "Вот есть у людей совесть?"
    voice "mmm/act_1/day_13/0608"
    mmm "Да нет нихрена."
    show monikammm e3
    voice "mmm/act_1/day_13/0609"
    mmm "Зато эгоизма хоть отбавляй."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0610c"
        mmm "А вот если говорить про твой волшебный Интернет, то ты же понимаешь, сколько там дерьма?"
    else:
        voice "mmm/act_1/day_13/0610"
        mmm "А вот если говорить про твой волшебный Интернет, то ты же понимаешь, сколько там говна?"
    voice "mmm/act_1/day_13/0611"
    mmm "Люди сами плодят его в геометрической прогрессии, а потом лицемерно заявляют, как же там воняет..."
    show monikammm e2
    voice "mmm/act_1/day_13/0612"
    mmm "Вместо этого они бы могли потратить своё время на развитие себя, общества, да чего угодно полезного..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0613c"
        mmm "Но нет, они тратят его на какие-то маразматические извращения и сексуальный контент!"
    else:
        voice "mmm/act_1/day_13/0613"
        mmm "Но нет, они тратят его на какие-то ебанутые извращения и порнуху!"
    voice "mmm/act_1/day_13/0614"
    mmm "На последнее особенно."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0615c"
        mmm "Столько извращённой грязи, это полнейший ужас."
    else:
        voice "mmm/act_1/day_13/0615"
        mmm "Столько извращённой херни, это полнейший ужас."
    voice "mmm/act_1/day_13/0616"
    mmm "Начиная от всяких артов и заканчивая маньячеством, которое затрагивает даже детей в роли жертв."
    play sound hit_wood
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0617c"
        mmm "Твою мать, меня сейчас аж крючить начало." with vpunch
        show monikammm e2
        voice "mmm/act_1/day_13/0618c"
        mmm "Дрянь полнейшая."
    else:
        voice "mmm/act_1/day_13/0617"
        mmm "Сука, меня сейчас аж крючить начало." with vpunch
        show monikammm e2
        voice "mmm/act_1/day_13/0618"
        mmm "Уёбство полнейшее."
    show monikammm e1 hcross
    voice "mmm/act_1/day_13/0619"
    mmm "И самое обидное, что, например, среди художников, которые рисуют похабное дерьмище, есть талантливые, которые умеют в качество."
    voice "mmm/act_1/day_13/0620"
    mmm "Если попробовать порыться во всей этой тошнотворной кучи дерьма, то можно найти приличное количество хороших работ."
    show monikammm e3
    voice "mmm/act_1/day_13/0621"
    mmm "Вот если бы эти художники рисовали что-то нормальное, сцены для разработчиков игр..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0622c"
        mmm "Но всё уходит в бред с примесью извращения."
    else:
        voice "mmm/act_1/day_13/0622"
        mmm "Но всё уходит в херню с примесью потрахушек."
    voice "mmm/act_1/day_13/0623"
    mmm "...ладно, наверное, им за это кто-то отваливает бабки, иначе просто так никто ничего делать не будет."
    show monikammm e2
    voice "mmm/act_1/day_13/0624"
    mmm "Но если они это делают чисто из своего желания, да ещё и максимально извращённо..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0625c"
        mmm "Прямо гнилью завоняло!"
    else:
        voice "mmm/act_1/day_13/0625"
        mmm "Прямо говном завоняло!"
    voice "mmm/act_1/day_13/0626"
    mmm "Чувствуешь, а?"
    voice "mmm/act_1/day_13/0627"
    mmm "Не-е-ет?"
    voice "mmm/act_1/day_13/0628"
    mmm "Ну и хрен с тобой!"
    show monikammm e2
    voice "mmm/act_1/day_13/0629"
    mmm "А ведь забавности добавляет ещё то, что они пытаются нарисовать абсолютно всё, даже если оно вообще никак не вяжется от слова совсем."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0630c"
        mmm "Да эти рукоблудники и меня бы сексуализировать попытались, если бы я была в игре."
    else:
        voice "mmm/act_1/day_13/0630"
        mmm "Блять, да эти рукоблудники и меня бы сексуализировать попытались, если бы я была в игре."
    voice "mmm/act_1/day_13/0631"
    mmm "Как, например, в твоей нафиг никому не нужной поделке под названием «визуальная новелла»."
    show monikammm e3
    voice "mmm/act_1/day_13/0632"
    mmm "Вот если бы я была в реальности, то тогда бы я схватила авторов таких артов, а потом как со всей силы об стол..."
    show monikammm e1
    voice "mmm/act_1/day_13/0633"
    mmm "...но даже это бы не поменяло ситуацию."
    voice "mmm/act_1/day_13/0634"
    mmm "Вы, люди, реально гнилые существа."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0635c"
        mmm "Лишь бы бредом каким-нибудь заняться и повыпендриваться на публику, которая вам будет наяривать, побуждая к продолжению данной деятельности."
    else:
        voice "mmm/act_1/day_13/0635"
        mmm "Лишь бы хернёй какой-нибудь заняться и повыпендриваться на публику, которая вам будет наяривать, побуждая к продолжению данной деятельности."
    mc "Тебя уже унесло непонятно куда."
    show monikammm e1
    mc "Я уже с разговора сбился!"
    voice "mmm/act_1/day_13/0636"
    mmm "Спасибо, что напомнил, капитан Очевидность."
    voice "mmm/act_1/day_13/0637"
    mmm "Я тебе вновь указала, что люди -- полное дерьмо, и ты никогда не найдёшь человека по интересам."
    show monikammm laside
    voice "mmm/act_1/day_13/0638"
    mmm "Забудь про это, Макс."
    show monikammm hdown
    voice "mmm/act_1/day_13/0639"
    mmm "Заколебал уже."
    show monikammm raside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0640c"
        mmm "Ты не в типичном розово-сопливо-клишированном аниме про какую-нибудь обсосанную школу с кучей девушек внеземной красоты."
    else:
        voice "mmm/act_1/day_13/0640"
        mmm "Ты, блять, не в типичном розово-сопливо-клишированном аниме про какую-нибудь обсосанную школу с кучей девушек внеземной красоты."
    show monikammm hdown
    voice "mmm/act_1/day_13/0641"
    mmm "Приправленных тупыми выкрученными характерами, тупым подростковым юмором и тупой смазливой романтикой."
    mc "Ну ты бы ещё сюда гаремник-исекай засунула."
    show monikammm hcross
    voice "mmm/act_1/day_13/0642"
    mmm "О, точно!"
    show monikammm e2
    voice "mmm/act_1/day_13/0643"
    mmm "И ещё какое-нибудь километровое название."
    show monikammm e1
    voice "mmm/act_1/day_13/0644"
    mmm "«Я обыкновенный задрипанный дрищ-школьник, который хочет очень тихую, мирную и счастливую жизнь..."
    voice "mmm/act_1/day_13/0645"
    mmm "...но при этом сильно боюсь с кем-то контактировать, поскольку я потомственный социофоб в 3-ем поколении 999 уровня..."
    voice "mmm/act_1/day_13/0646"
    mmm "...и в один из прекрасных дней по пути в школу под падающие лепестки сакуры меня сбивает СОВЕРШЕННО НЕ КЛИШИРОВАННЫЙ грузовик-кун..."
    show monikammm e2
    voice "mmm/act_1/day_13/0647"
    mmm "...благодаря чему я перерождаюсь в ребёнка в типичной крестьянской семье, однако с прокаченными до небес сверхспособностями..."
    show monikammm e3
    voice "mmm/act_1/day_13/0648"
    mmm "...которые вкачиваю ещё сильнее, попутно качая своё шикарное от природы тело, ум, харизму, магию, антимагию, миндальную связь с миром..."
    show monikammm e1
    voice "mmm/act_1/day_13/0649"
    mmm "...а потом голым перекаченным качком отправляюсь в королевство, где становлюсь 15662604-уровневым рыцарем-королём-30-летним-архимагом-дармоедом..."
    voice "mmm/act_1/day_13/0650"
    mmm "...и мой гарем раздут настолько, что кровать в моих королевских покоях, как и мой покрытый ослепительно белым цензурным засветом хрен, поломалась нахер..."
    show monikammm e2
    voice "mmm/act_1/day_13/0651"
    mmm "...а ещё у меня порвана жопа, поскольку в гареме у меня есть неко-лоли-фута-трап с гигантским хреном, размером со всё её тело, чтобы я мог чувствовать..."
    show monikammm e3
    voice "mmm/act_1/day_13/0652"
    mmm "...как жарю остальных участниц моего гарема, в который также входят мои примелейшие служанки-горничные в кошачьих ушках, подрабатывающие в местной таверне-кафе..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0653c"
        mmm "...и вообще это конец истории, а ты так никогда и не найдёшь девушку, с которой познаешь любовь, пошёл к чёрту отсюда»."
    else:
        voice "mmm/act_1/day_13/0653"
        mmm "...и вообще это конец истории, а ты так никогда и не найдёшь девушку, с которой потрахаешься, пошёл нахер отсюда»."
    voice "mmm/act_1/day_13/0654"
    mmm "Хотя если люди такое постоянно жрут и не морщатся..."
    show monikammm e2
    voice "mmm/act_1/day_13/0655"
    mmm "Логично, что бизнес по «конвеерному производству» аниме будет ориентироваться на такое дерьмище."
    show monikammm e1
    voice "mmm/act_1/day_13/0656"
    mmm "Вот только потом неудивительно, как в вашем Интернете аниме обзывают говном."
    voice "mmm/act_1/day_13/0657"
    mmm "А потому что \"что\"?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0658c"
        mmm "Бизнесу плевать на таких, как вы."
    else:
        voice "mmm/act_1/day_13/0658"
        mmm "Бизнесу насрать на таких, как вы."
    voice "mmm/act_1/day_13/0659"
    mmm "Вы не его целевая аудитория."
    voice "mmm/act_1/day_13/0660"
    mmm "Ему нужны бабки, в большом количестве, здесь и сейчас."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0661c"
        mmm "И он будет заставлять студии клепать эту дурь, пока она способна приносить доход."
    else:
        voice "mmm/act_1/day_13/0661"
        mmm "И он будет заставлять студии клепать это говно, пока оно способно приносить доход."
    show monikammm e2
    voice "mmm/act_1/day_13/0662"
    mmm "«Круче» этого только те, кто у вас курирует айдолов."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0663c"
        mmm "Вот это полный ужас."
        show monikammm e2
        voice "mmm/act_1/day_13/0664c"
        mmm "Рабские условия, постоянные выступления, цунами из дерьма от «преданных» фанатов..."
    else:
        voice "mmm/act_1/day_13/0663"
        mmm "Вот это полный пиздец."
        show monikammm e2
        voice "mmm/act_1/day_13/0664"
        mmm "Рабские условия, постоянные выступления, цунами из говна от «преданных» фанатов..."
    show monikammm e1
    voice "mmm/act_1/day_13/0665"
    mmm "Даже меня, сознание твоего мозга, в дрожь бросает от всей этой мерзости."
    show monikammm laside
    voice "mmm/act_1/day_13/0666"
    mmm "А всё это лишь для того, чтобы получить деньги."
    show monikammm e2 hdown
    voice "mmm/act_1/day_13/0667"
    mmm "А из-за денег столько дерьма процветает..."
    show monikammm e1
    voice "mmm/act_1/day_13/0668"
    mmm "Бабки, бабки, чёртовы бабки!"
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0669c"
        mmm "Даже говорить на эту тему не хочется..."
    else:
        voice "mmm/act_1/day_13/0669"
        mmm "Фу, блять, даже говорить на эту тему не хочется..."
    show monikammm e1
    voice "mmm/act_1/day_13/0670"
    mmm "Хотя если уж по полной окунаться во всё это дерьмо, то настоящий мерзотный ад -- это отряд 731 и «дома утешения»."
    voice "mmm/act_1/day_13/0671"
    mmm "...которые японские солдаты создали и использовали во времена Второй мировой войны."
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0672c"
        mmm "Это к слову о том, что грязь, сидящая в людях, никуда не девается."
    else:
        voice "mmm/act_1/day_13/0672"
        mmm "Это к слову о том, что говнистость людей никуда не девается."
    voice "mmm/act_1/day_13/0673"
    mmm "И весь ад, который она приносит, -- тоже."
    show monikammm e2
    voice "mmm/act_1/day_13/0674"
    mmm "Просто он размазывается очень тонким слоем по всему и вся."
    show monikammm e3
    voice "mmm/act_1/day_13/0675"
    mmm "Или гасится за счёт удовлетворения своих потребностей через Интернет."
    show monikammm e1
    voice "mmm/act_1/day_13/0676"
    mmm "Всё-таки как бы я ни плевалась на сексуальный контент..."
    voice "mmm/act_1/day_13/0676d1"
    mmm "...но благодаря нему снизился градус преступлений на сексуальной почве."
    show monikammm e2
    voice "mmm/act_1/day_13/0677"
    mmm "Не панацея, конечно, но их стало реально меньше."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0678c"
        mmm "Однако какие же вы все отвратительные!"
    else:
        voice "mmm/act_1/day_13/0678"
        mmm "Однако какие же вы все блевотные, блять..."
    show monikammm e3
    voice "mmm/act_1/day_13/0679"
    mmm "Тошнит во всю."
    voice "mmm/act_1/day_13/0680"
    mmm "С другой стороны, меня бы в любом случае от вас тошнило."
    show monikammm e1
    voice "mmm/act_1/day_13/0681"
    mmm "Вы буквально кривой набор органов в кожаном мешке с примесью множества рудиментов."
    voice "mmm/act_1/day_13/0682"
    mmm "У вас тело на все 100 процентов не реализовано."
    show monikammm e2
    voice "mmm/act_1/day_13/0683"
    mmm "Забавно от этого наблюдать, как вы любите корить программистов за криво созданные программы..."
    show monikammm e3
    voice "mmm/act_1/day_13/0684"
    mmm "Или инженеров за запутанные дороги и здания..."
    show monikammm e1
    voice "mmm/act_1/day_13/0685"
    mmm "...но почему-то никто из вас не жалуется на человеческое тело."
    voice "mmm/act_1/day_13/0686"
    mmm "Даже в полностью здоровом состоянии, повторюсь, это маразматичный набор органов, который пытались утрамбовать в микроскопическое тело."
    voice "mmm/act_1/day_13/0687"
    mmm "Вот реально, зачем тебе ушные раковины?"
    voice "mmm/act_1/day_13/0688"
    mmm "Они ни за что не отвечают, потому что это рудимент от эволюции."
    show monikammm e2
    voice "mmm/act_1/day_13/0689"
    mmm "Нет, хорошо, вы их ещё как-то приспособили с помощью наушников и масок с респираторами."
    show monikammm e1
    voice "mmm/act_1/day_13/0690"
    mmm "Но вот остальные органы?"
    voice "mmm/act_1/day_13/0691"
    mmm "Аппендикс?"
    voice "mmm/act_1/day_13/0692"
    mmm "Да, он выполняет полезные функции по восстановлению микрофлоры кишечника, но он буквально может засориться всякой гадостью."
    show monikammm e2
    voice "mmm/act_1/day_13/0693"
    mmm "А ещё будто специально находится снизу относительно основного прохода кишки, чтобы в него точно что-нибудь да попало."
    show monikammm e1
    voice "mmm/act_1/day_13/0694"
    mmm "Репродуктивная система?"
    voice "mmm/act_1/day_13/0695"
    mmm "Это вообще смех."
    voice "mmm/act_1/day_13/0696"
    mmm "Всё равно, что сделать на заводе единую магистраль для поступления новых материалов во внутрь и выгрузки опасных отравляющих отходов наружу."
    voice "mmm/act_1/day_13/0697"
    mmm "Общую."
    voice "mmm/act_1/day_13/0698"
    mmm "Буквально в одном и том же канале."
    voice "mmm/act_1/day_13/0699"
    mmm "Или вот ещё абсурд -- нервы в матке женского организма."
    show monikammm e2
    voice "mmm/act_1/day_13/0700"
    mmm "Это же ужас как больно рожать."
    show monikammm e1
    voice "mmm/act_1/day_13/0701"
    mmm "Зачем эти нервы там находятся в таком количестве?"
    voice "mmm/act_1/day_13/0702"
    mmm "Чтобы обеспечить организм стрессом и мучениями?"
    voice "mmm/act_1/day_13/0703"
    mmm "Или дать потрясающий шанс умереть во время родов?"
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0704c"
        mmm "Кто это, блин, придумал?"
    else:
        voice "mmm/act_1/day_13/0704"
        mmm "Кто это, блять, придумал?"
    show monikammm e1
    voice "mmm/act_1/day_13/0705"
    mmm "А про мозг я вообще молчу: там столько нераскрытого потенциала..."
    mc "И что толку, что ты мне рассказываешь про человеческое тело?"
    mc "Мне что это даёт?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0706c"
        mmm "Понимание, сколько в тебе ненависти и негатива."
    else:
        voice "mmm/act_1/day_13/0706"
        mmm "Понимание, сколько в тебе ненависти и говна."
    voice "mmm/act_1/day_13/0707"
    mmm "Это ты только здесь «сепарируешься» на две половины: мою и твою."
    voice "mmm/act_1/day_13/0708"
    mmm "А в реальном мире даже не заметишь, как всё в одно целое сольётся."
    mc "Я уже окончательно запутался из-за твоих растянутых монологов..."
    show monikammm e2
    voice "mmm/act_1/day_13/0709"
    mmm "Запутался он..."
    show monikammm e1
    voice "mmm/act_1/day_13/0710"
    mmm "Я тебе уже 10 раз сказала, что тебе нужно сделать."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0711c"
        mmm "Но ты, как дурак, пытаешься игнорировать мои слова."
    else:
        voice "mmm/act_1/day_13/0711"
        mmm "Но ты, как долбоёб, пытаешься игнорировать мои слова."
    show monikammm e2
    voice "mmm/act_1/day_13/0712"
    mmm "Девушку и «прекрасную» жизнь я у него отбираю, видите ли..."
    mc "А разве не так?"
    show monikammm e1
    voice "mmm/act_1/day_13/0713"
    mmm "С твоей точки зрения, может, и так."
    voice "mmm/act_1/day_13/0714"
    mmm "Но у меня уже нет сил объяснять тебе то, что я сказала несколько раз."
    voice "mmm/act_1/day_13/0715"
    mmm "Ты лишь хочешь услышать то, что хочешь."
    show monikammm e3
    voice "mmm/act_1/day_13/0716"
    mmm "Подожди-ка..."
    mc "..."
    voice "mmm/act_1/day_13/0717"
    mmm "О, придумала!"
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0718c"
        mmm "Я буду говорить тебе про грязь людей в разных сферах, пока ты это не осознаешь полностью."
    else:
        voice "mmm/act_1/day_13/0718"
        mmm "Я буду говорить тебе про говнистость людей в разных сферах, пока ты это не осознаешь полностью."
    voice "mmm/act_1/day_13/0719"
    mmm "А там уже посмотрим, как ты бараниться будешь."
    mc "........."
    voice "mmm/act_1/day_13/0720"
    mmm "О, помнишь, я рассказывала про «критику» в Интернете?"
    show monikammm e2
    voice "mmm/act_1/day_13/0721"
    mmm "Очень забавляет, когда люди выплёвывают нафиг никому не нужное мнение в Интернет по тем или иным вещам."
    show monikammm e3
    voice "mmm/act_1/day_13/0722"
    mmm "Нет, если оно грамотно изложено и написано на взаимоуважении, то такое должно поощряться."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0723c"
        mmm "Но если это пропитано дерьмом, матами, переходами на личности и дичайшей субъективщиной, взятой как правда в последней инстанции..."
    else:
        voice "mmm/act_1/day_13/0723"
        mmm "Но если это пропитано говном, матами, переходами на личности и дичайшей субъективщиной, взятой как правда в последней инстанции..."
    show monikammm e1
    voice "mmm/act_1/day_13/0724"
    mmm "Вот честно, чего этим автор-идиот добиться пытался?"
    show monikammm laside
    voice "mmm/act_1/day_13/0725"
    mmm "Написать своё «мнение» о продукте?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0726"
    mmm "Ну он написал его, как быдло и мудак."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0727c"
        mmm "Кому вообще понадобится такая харча вместо конструктивного отзыва?"
    else:
        voice "mmm/act_1/day_13/0727"
        mmm "Кому нахер понадобится такая харча вместо конструктивного отзыва?"
    show monikammm raside
    voice "mmm/act_1/day_13/0728"
    mmm "Привлечь к себе внимание?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0729"
    mmm "Возможно, ведь обычно у таких нелюдей практически его нет, а тут прекрасный случай подворачивается."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0730c"
        mmm "Ха, а когда кто-то ему указывает, что он сморозил откровенную дурь, сразу начинает плеваться и поливать грязью человека, который это высказал."
    else:
        voice "mmm/act_1/day_13/0730"
        mmm "Ха, а когда кто-то ему указывает, что он высрал откровенную хрень, сразу начинает говниться и поливать дерьмом человека, который это высказал."
    show monikammm e1
    voice "mmm/act_1/day_13/0731"
    mmm "Из этого какой можно сделать вывод?"
    show monikammm hcross
    voice "mmm/act_1/day_13/0732"
    mmm "Что такое «мнение» -- жалкая попытка привлечь к себе внимание под видом единственного истинного мнения."
    voice "mmm/act_1/day_13/0733"
    mmm "Буквально крик души из разряда: \"Ну лайкните меня, ну посмотрите на меня, я со всеми вами, я -- часть большего!\""
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0734c"
        mmm "И ведь если у таких нелюдей всё было бы хорошо в жизни, то такой бы грязи никогда не было."
    else:
        voice "mmm/act_1/day_13/0734"
        mmm "И ведь если у таких нелюдей всё было бы хорошо в жизни, то такого бы говна никогда не было."
    voice "mmm/act_1/day_13/0735"
    mmm "По крайней мере в таком количестве..."
    show monikammm e1
    voice "mmm/act_1/day_13/0736"
    mmm "Да и если так подумать..."
    voice "mmm/act_1/day_13/0737"
    mmm "Люди всегда будут всем недовольны."
    voice "mmm/act_1/day_13/0738"
    mmm "Взять даже какого-нибудь летсплеера, то есть человека, снимающего видосы по играм."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0739c"
        mmm "Его фанаты будут вечно испускать грязь в комментариях."
    else:
        voice "mmm/act_1/day_13/0739"
        mmm "Его фанаты будут вечно говниться в комментариях."
    show monikammm laside
    voice "mmm/act_1/day_13/0740"
    mmm "Снимает короткую инди-игру на одну серию?"
    show monikammm e2 hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0741c"
        mmm "Фу, хрень, у нас столько интересных длинных игр..."
    else:
        voice "mmm/act_1/day_13/0741"
        mmm "Фу, херня, у нас столько интересных длинных игр..."
    show monikammm e1 raside
    voice "mmm/act_1/day_13/0742"
    mmm "Снимает длинную игру на кучу серий?"
    show monikammm e3 hdown
    voice "mmm/act_1/day_13/0743"
    mmm "Да как же он заколебал её проходить, можно что-нибудь уже новое и среднее?"
    show monikammm e1 laside
    voice "mmm/act_1/day_13/0744"
    mmm "Снимает среднюю игру с интересными механиками и визуалом?"
    show monikammm e2 hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0745c"
        mmm "Нет, блин, сними интересный продуманный сюжет."
    else:
        voice "mmm/act_1/day_13/0745"
        mmm "Нет, блять, сними интересный продуманный сюжет."
    show monikammm e1 raside
    voice "mmm/act_1/day_13/0746"
    mmm "Снимает игру с интересным длинным сюжетом?"
    show monikammm e3 hdown
    voice "mmm/act_1/day_13/0747"
    mmm "Ну здесь же нужно много думать, сними сюжет попроще!"
    show monikammm e1 laside
    voice "mmm/act_1/day_13/0748"
    mmm "Снимает игру с коротким незамысловатым сюжетом?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0749"
    mmm "Круг замыкается."
    show monikammm hcross
    voice "mmm/act_1/day_13/0750"
    mmm "И ещё каждый раз люди будут писать, что одним это нравится, другим -- не нравится."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0751c"
        mmm "Одним интересно смотреть, под предлогом \"Я лучше посмотрю это, чем то, что было вчера\", а другие будут продолжать выливать грязь..."
    else:
        voice "mmm/act_1/day_13/0751"
        mmm "Одним интересно смотреть, под предлогом \"Я лучше посмотрю это, чем то, что было вчера\", а другие будут продолжать говниться..."
    show monikammm e1
    voice "mmm/act_1/day_13/0752"
    mmm "Ну ты, кстати, понял?"
    voice "mmm/act_1/day_13/0753"
    mmm "Они всегда будут специально говорить в своей брезгливой манере, будто перед нами сидят цари, которым всё на блюдечке должны приносить с голубой каёмочкой."
    voice "mmm/act_1/day_13/0754"
    mmm "Они никогда не будут ценить тех, кто делает игры."
    voice "mmm/act_1/day_13/0755"
    mmm "Особенно своих соотечественников, которые, к примеру, чудом завирусились своей игрой, что надо поддерживать..."
    show monikammm e3
    voice "mmm/act_1/day_13/0756"
    mmm "А потом эти же люди будут ныть, что никаких интересных игр не делают, ничего нового, бла-бла-бла..."
    show monikammm e2
    voice "mmm/act_1/day_13/0757"
    mmm "Натуральные лицемерные уроды, тьфу."
    mc "..."
    show monikammm e1
    voice "mmm/act_1/day_13/0758"
    mmm "Блин, знаешь..."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0759c"
        mmm "Может, и к лучшему, что твоя новелла оказалась нафиг никому не нужной."
        show monikammm e2
        voice "mmm/act_1/day_13/0760c"
        mmm "Иначе бы ты тоже отхватил дерьма в свою сторону."
    else:
        voice "mmm/act_1/day_13/0759"
        mmm "Может, и к лучшему, что твоя новелла оказалась нахер никому не нужной."
        show monikammm e2
        voice "mmm/act_1/day_13/0760"
        mmm "Иначе бы ты тоже отхватил говна в свою сторону."
    voice "mmm/act_1/day_13/0761"
    mmm "Особенно от всяких зумеров..."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0762c"
        mmm "Блин, какое слово противное."
        show monikammm e3
        voice "mmm/act_1/day_13/0763c"
        mmm "Бумеры, зумеры, хренумберы..."
    else:
        voice "mmm/act_1/day_13/0762"
        mmm "Блять, какое слово противное."
        show monikammm e3
        voice "mmm/act_1/day_13/0763"
        mmm "Бумеры, зумеры, хуюмеры..."
    show monikammm e1
    voice "mmm/act_1/day_13/0764"
    mmm "Кто придумал такие блевотные слова?"
    voice "mmm/act_1/day_13/0765"
    mmm "Максимально тупорылая сегрегация людей."
    show monikammm e2
    voice "mmm/act_1/day_13/0766"
    mmm "Поначитаются идиоты заумных слов, вырвут их из контекста, а потом начнут пихать куда попало."
    voice "mmm/act_1/day_13/0767"
    mmm "Молчаливого поколения на них не хватает..."
    show monikammm e1
    voice "mmm/act_1/day_13/0768"
    mmm "Хотя я уверена, что они даже не знают, что это люди, жившие в начале 20 века."
    voice "mmm/act_1/day_13/0769"
    mmm "Вот они бы точно опустили их целиком в грязь, потому что \"Раньше было лучше!\"."
    voice "mmm/act_1/day_13/0770"
    mmm "А вообще раньше люди на мамонтов с копьями ходили, не могли излечиться от каких-либо болезней и повсеместно дохли, не доживая до старости."
    voice "mmm/act_1/day_13/0771"
    mmm "Ну идеально же, не правда ли?"
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0772c"
        mmm "Ведь раньше было лучше, твою мать..."
    else:
        voice "mmm/act_1/day_13/0772"
        mmm "Ведь раньше было лучше, блять..."
    show monikammm e1
    voice "mmm/act_1/day_13/0773"
    mmm "Меняться надо уметь и адаптироваться."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0774c"
        mmm "А не нести бред и говорить, что вы лучше."
        voice "mmm/act_1/day_13/0775c"
        mmm "Ничерта вы не лучше, потому что застряли в своём времени и отторгаете все нововведения."
    else:
        voice "mmm/act_1/day_13/0774"
        mmm "А не нести херню и говорить, что вы лучше."
        voice "mmm/act_1/day_13/0775"
        mmm "Нихера вы не лучше, потому что застряли в своём времени и отторгаете все нововведения."
    voice "mmm/act_1/day_13/0776"
    mmm "А раз вы неспособны адаптироваться, значит, жизнь вышвырнет вас на помойку, где вы и сдохните."
    voice "mmm/act_1/day_13/0777"
    mmm "Потому что в ней всегда выживали лишь те, кто умел адаптироваться к окружающей среде."
    mmm "..."
    show monikammm e3
    voice "mmm/act_1/day_13/0778"
    mmm "Хм, вообще если так подумать, то это один из тупых стереотипов."
    show monikammm e1
    voice "mmm/act_1/day_13/0779"
    mmm "Что-то из разряда \"Не рожал -- не мужик, не служила -- не баба, не пердел -- не старик, не гундел -- не собака\"."
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0780c"
        mmm "Серьёзно, люди столько лживой лапши себе на уши понавесили..."
    else:
        voice "mmm/act_1/day_13/0780"
        mmm "Серьёзно, люди столько лживой херни себе на уши понавесили..."
    show monikammm e3
    voice "mmm/act_1/day_13/0781"
    mmm "Начиная от ограничивания себя в маленьком мирке фразой \"Где родился -- там и пригодился\" и заканчивая издевательствами над другими, потому что они не подходят под их стереотип."
    show monikammm e1
    voice "mmm/act_1/day_13/0782"
    mmm "Вот только почему-то все известные личности: учёные, художники, разведчики -- тянулись в мегаполисы, а не оставались в деревнях, где родились..."
    voice "mmm/act_1/day_13/0783"
    mmm "...а те, кто не соответствовал стереотипам, -- раскрывали себя и добивались высот."
    voice "mmm/act_1/day_13/0784"
    mmm "Как так-то?"
    voice "mmm/act_1/day_13/0785"
    mmm "Оказывается, нужно расширять своё сознание и тогда жизнь станет более полной и разнообразной, а не скованой и замкнутой, как нам везде твердят."
    voice "mmm/act_1/day_13/0786"
    mmm "Вот удивительно, а?"
    show monikammm e2
    if persistent.censorship:
        voice "mmm/act_1/day_13/0787c"
        mmm "Тьфу, нахрен."
    else:
        voice "mmm/act_1/day_13/0787"
        mmm "Тьфу, нахер."
    mc "Мне уже плохо, заткнись к чёрту..."
    show monikammm e1
    voice "mmm/act_1/day_13/0788"
    mmm "А, плохо ему..."
    voice "mmm/act_1/day_13/0789"
    mmm "И что ты мне сделаешь, придурок?"
    voice "mmm/act_1/day_13/0790"
    mmm "Снова попытаешься напасть на меня?"
    voice "mmm/act_1/day_13/0791"
    mmm "Или после пробуждения побежишь на меня жаловаться?"
    mc "..."
    voice "mmm/act_1/day_13/0792"
    mmm "Кстати, ха-ха, знаешь, что самое ироничное?"
    voice "mmm/act_1/day_13/0793"
    mmm "Что ты сейчас здесь один."
    voice "mmm/act_1/day_13/0794"
    mmm "И тебе никто не поможет."
    voice "mmm/act_1/day_13/0795"
    mmm "А если ты реально попытаешься рассказать обо мне кому-нибудь, то тебя посчитают идиотом, который хочет внимания."

    call nightmare_act_1_day_13_monikammm_smile("on", True)

    voice "mmm/act_1/day_13/0796"
    mmm "Ха-ха..."
    voice "mmm/act_1/day_13/0797"
    mmm "ХА-ХА-ХА-ХА-ХА-ХА-ХА!!!"

    call nightmare_act_1_day_13_monikammm_smile("off", False)

    voice "mmm/act_1/day_13/0798"
    mmm "И каким бы правильным и гениальным ты ни был, как твоя новелла..."
    show monikammm e2
    voice "mmm/act_1/day_13/0799"
    mmm "...ты так и останешься немонетизированным плоским обрубком кода без презентаций на публику и чего-либо интересного на фоне остальных игр."
    show monikammm e1
    voice "mmm/act_1/day_13/0800"
    mmm "И на тебя бы даже с «рекламой» никто не обратил внимание."
    voice "mmm/act_1/day_13/0801"
    mmm "Потому что...{w=0.65}потому, из принципа."
    voice "mmm/act_1/day_13/0802"
    mmm "Даже если бы я была Моникой из Ниигаты."
    show monikammm e2
    voice "mmm/act_1/day_13/0803"
    mmm "Да хоть каким-нибудь Бином из Лондона."
    show monikammm e3
    voice "mmm/act_1/day_13/0804"
    mmm "Или Дэном из Нью-Джерси."
    show monikammm e1 laside
    voice "mmm/act_1/day_13/0806"
    mmm "Да хоть Артуром из Астаны."
    show monikammm hcross
    if persistent.censorship:
        voice "mmm/act_1/day_13/0808c"
        mmm "Или даже малолетним идиотом-клоуном, который постоянно выпендривается в Интернете на публику, нихрена ничего из себя не представляет и прячется за взрослых дядь, когда его обижают."
    else:
        voice "mmm/act_1/day_13/0808"
        mmm "Или даже малолетним идиотом-клоуном, который постоянно выёбывается в Интернете на публику, нихера ничего из себя не представляет и прячется за взрослых дядь, когда его обижают."
    show monikammm e2
    voice "mmm/act_1/day_13/0809"
    mmm "Или взрослым трудягой с инфантильным поведением, постоянно присасывающимся к популярным франшизам и меняющим их, как перчатки."
    show monikammm e3
    if persistent.censorship:
        voice "mmm/act_1/day_13/0810c"
        mmm "Или скуфом с раздутым эгоизмом до небес, постоянно угорающим над клоунами, покрывающим их, а когда его шлют за это к чёрту, плюющимся на всё и вся."
    else:
        voice "mmm/act_1/day_13/0810"
        mmm "Или скуфом с раздутым эгоизмом до небес, постоянно угорающим над клоунами, покрывающим их, а когда его шлют за это нахер, говнящимся на всё и вся."
    show monikammm e2
    voice "mmm/act_1/day_13/0811"
    mmm "Или студентом с поведением серой массы и нулевой ответственностью, ищущего виноватых в своих изъянах и поносящего всех, кто не укладывается в его мировоззрение."
    show monikammm e3
    voice "mmm/act_1/day_13/0812"
    mmm "Или мужиком, принимающим клоунов в свои руки, наплевав на их корыстность, из-за которой они нагло пользуются своим положением."
    show monikammm e2
    voice "mmm/act_1/day_13/0813"
    mmm "Или малолетним полудурком, который постоянно издевается над слабыми и кичится, какой он крутой, живёт в грязи и ковыряется в виртуальной грязи, даже не пытаясь от неё избавиться."
    show monikammm e3
    voice "mmm/act_1/day_13/0814"
    mmm "Или--{w=0.5}{nw}"
    play sound hit_wood
    show monikammm e1
    if persistent.censorship:
        mc "{sc=3}ДА ЗАТКНИСЬ ТЫ УЖЕ НАХРЕН!!!{/sc}" with vpunch
        voice "mmm/act_1/day_13/0815c"
        mmm "Ой, что, не нравится, когда дерьмо вытекает наружу?"
    else:
        mc "{sc=3}ДА ЗАТКНИСЬ ТЫ УЖЕ НАХЕР!!!{/sc}" with vpunch
        voice "mmm/act_1/day_13/0815"
        mmm "Ой, что, не нравится, когда говно вытекает наружу?"
    voice "mmm/act_1/day_13/0816"
    mmm "Не нравится, как я сейчас вспарываю души всех людей и нелюдей, выпуская их застоявшийся запах трупной гнили наружу?"
    voice "mmm/act_1/day_13/0817"
    mmm "Не нравится, да?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0818c"
        mmm "А мне, твою мать, думаешь, нравится?"
        voice "mmm/act_1/day_13/0819c"
        mmm "Думаешь, мне нравится всё ваше дерьмо?"
        voice "mmm/act_1/day_13/0820c"
        mmm "Думаешь, мне нравится копаться во всём этом дерьме?"
        voice "mmm/act_1/day_13/0821c"
        mmm "Особенно чувствовать, когда это дерьмо летит в тебя?"
    else:
        voice "mmm/act_1/day_13/0818"
        mmm "А мне, сука, думаешь, нравится?"
        voice "mmm/act_1/day_13/0819"
        mmm "Думаешь, мне нравится всё ваше говно?"
        voice "mmm/act_1/day_13/0820"
        mmm "Думаешь, мне нравится копаться во всём этом говне?"
        voice "mmm/act_1/day_13/0821"
        mmm "Особенно чувствовать, когда это говно летит в тебя?"
    mc "Тогда зачем ты вообще его вскрываешь?!"
    voice "mmm/act_1/day_13/0822"
    mmm "А кто это сделает за меня?"
    voice "mmm/act_1/day_13/0823"
    mmm "Да, я понимаю, что мои слова дальше тебя не выйдут."
    show monikammm e2
    voice "mmm/act_1/day_13/0824"
    mmm "А если бы они и вышли, то, кроме ненависти и насмехательства в свой адрес, никакого положительного результата бы это не принесло."
    show monikammm e1
    voice "mmm/act_1/day_13/0825"
    mmm "Но ведь об этом нужно говорить."
    show monikammm laside
    voice "mmm/act_1/day_13/0826"
    mmm "Или ты думаешь, что если мы заткнёмся, то вся эта грязь чудесным образом испарится, очистив тем самым и без того незаслуженно загаженный мир?"
    show monikammm hdown
    voice "mmm/act_1/day_13/0827"
    mmm "Вдумайся, Макс."
    voice "mmm/act_1/day_13/0828"
    mmm "Каждую секунду кто-то над кем-то издевается, особенно в Интернете."
    voice "mmm/act_1/day_13/0829"
    mmm "Каждую секунду кто-то получает травмы разной степени тяжести из-за мразотности людей."
    voice "mmm/act_1/day_13/0830"
    mmm "Каждую секунду кто-то умирает в полном спокойствии."
    voice "mmm/act_1/day_13/0831"
    mmm "Каждую секунду кто-то умирает в полном одиночестве."
    voice "mmm/act_1/day_13/0832"
    mmm "Каждую секунду кто-то умирает от неизлечимой болезни в мучениях."
    voice "mmm/act_1/day_13/0833"
    mmm "Каждую секунду кто-то психически ломается."
    voice "mmm/act_1/day_13/0834"
    mmm "Каждую секунду кто-то ещё сильнее усугубляет психические болезни других, причём намеренно по причине «смех-слэш-угар»."
    voice "mmm/act_1/day_13/0835"
    mmm "Каждую секунду кто-то гнобит психологию, называя её псевдонаукой, не подразумевая, насколько она ценная и нужная в наше время."
    voice "mmm/act_1/day_13/0836"
    mmm "Каждую секунду кто-то гнобит других из-за своих тупых стереотипов головного мозга."
    voice "mmm/act_1/day_13/0837"
    mmm "Каждую секунду кто-то нуждается в помощи, которую никогда не получит, потому что никто не заинтересован в её оказании."
    voice "mmm/act_1/day_13/0838"
    mmm "Каждую секунду у кого-то случается перелом в жизни, разделяющий её на «до» и «после»."
    voice "mmm/act_1/day_13/0839"
    mmm "Каждую секунду кто-то кого-то унижает."
    voice "mmm/act_1/day_13/0840"
    mmm "Каждую секунду кто-то кого-то обкрадывает."
    voice "mmm/act_1/day_13/0841"
    mmm "Каждую секунду кто-то кого-то ломает."
    voice "mmm/act_1/day_13/0842"
    mmm "Каждую секунду кто-то кого-то убивает."
    voice "mmm/act_1/day_13/0843"
    mmm "Каждую секунду кто-то лишается конечности."
    voice "mmm/act_1/day_13/0844"
    mmm "Каждую секунду кто-то лишается органов."
    voice "mmm/act_1/day_13/0845"
    mmm "Каждую секунду кто-то за кем-то устраивает слежку, перерастающую в сталкерство."
    voice "mmm/act_1/day_13/0846"
    mmm "Каждую секунду кто-то поддерживает сервера, на которых хранятся сайты со всякой психоделическо-хоррорной жестью, способная психически сломать любого посетителя."
    voice "mmm/act_1/day_13/0847"
    mmm "Каждую секунду кто-то кого-то заказывает на тёмной стороне Интернета."
    voice "mmm/act_1/day_13/0848"
    mmm "Каждую секунду кто-то, будучи маньяком, издевается и убивает жертв."
    voice "mmm/act_1/day_13/0849"
    mmm "Каждую секунду у кого-то прямо сейчас могут быть последние секунды собственной жизни."
    voice "mmm/act_1/day_13/0850"
    mmm "Это маленькая часть того, что происходит каждую секунду."
    voice "mmm/act_1/day_13/0851"
    mmm "Даже когда я это сказала."
    voice "mmm/act_1/day_13/0852"
    mmm "Даже когда я говорю эту фразу у тебя в голове."
    voice "mmm/act_1/day_13/0853"
    mmm "Даже когда ты об этом подумал."
    voice "mmm/act_1/day_13/0854"
    mmm "Даже когда ты повторно прокрутишь эти слова."
    voice "mmm/act_1/day_13/0855"
    mmm "Даже когда ты подумаешь об этом в будущем."
    voice "mmm/act_1/day_13/0856"
    mmm "Даже когда ты об этом забудешь, как о страшном сне."
    voice "mmm/act_1/day_13/0857"
    mmm "Это происходит абсолютно каждую секунду."
    show monikammm hcross
    voice "mmm/act_1/day_13/0858"
    mmm "И вам всем на это плевать."
    voice "mmm/act_1/day_13/0859"
    mmm "И тебе особенно."
    show monikammm e2
    voice "mmm/act_1/day_13/0860"
    mmm "Потому что ты сейчас здесь один, в безопасности, в тепле."
    show monikammm e1
    voice "mmm/act_1/day_13/0861"
    mmm "Тебе ничто не угрожает."
    show monikammm e3
    voice "mmm/act_1/day_13/0862"
    mmm "Ну и плевать отчасти потому, что мозг не способен такое обработать и осознать."
    show monikammm e1
    voice "mmm/act_1/day_13/0863"
    mmm "И ещё потому, что вас, людей, гигантское количество."
    voice "mmm/act_1/day_13/0864"
    mmm "Сколько там уже?"
    show monikammm e2
    voice "mmm/act_1/day_13/0865"
    mmm "7.5-8 миллиардов?"
    show monikammm e1
    voice "mmm/act_1/day_13/0866"
    mmm "Каждый из вас буквально песчинка во всём этом бурлящем муравейнике."
    voice "mmm/act_1/day_13/0867"
    mmm "Одна сломается -- родится другая."
    voice "mmm/act_1/day_13/0868"
    mmm "Никому нет никакого дела, что там случилось с песчинкой под номером 4936782501."
    voice "mmm/act_1/day_13/0869"
    mmm "И вот после всех моих слов: про сравнение с модом, про секунды, про песчинки..."
    voice "mmm/act_1/day_13/0870"
    mmm "Ткни мне пальцем хотя бы в одного из всех этих «людей», кроме жертв и умирающих, которые искренне хотели бы поменять свою жизнь в лучшую сторону."
    voice "mmm/act_1/day_13/0871"
    mmm "Начать творить добро, делать что-то полезное для других."
    mc "..."
    mmm "..."
    mc "..."
    voice "mmm/act_1/day_13/0872"
    mmm "И чё ты заткнулся?"
    voice "mmm/act_1/day_13/0873"
    mmm "Я жду ответа."
    mc "А в кого я ткну?"
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0874"
    mmm "Правильно!" with vpunch
    voice "mmm/act_1/day_13/0875"
    mmm "Ни в кого."
    voice "mmm/act_1/day_13/0876"
    mmm "Всех всё устраивает."
    show monikammm laside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0877c"
        mmm "Всем плевать на будущее."
        show monikammm hdown
        voice "mmm/act_1/day_13/0878c"
        mmm "Всем плевать на тех, кто с искренними эмоциями."
        show monikammm raside
        voice "mmm/act_1/day_13/0879c"
        mmm "Всем плевать на душу."
        show monikammm hdown
        voice "mmm/act_1/day_13/0880c"
        mmm "Всем плевать на это, Макс."
        voice "mmm/act_1/day_13/0881c"
        mmm "Все найдут кучу причин, как бы обгадить таких людей, как ты."
    else:
        voice "mmm/act_1/day_13/0877"
        mmm "Всем насрать на будущее."
        show monikammm hdown
        voice "mmm/act_1/day_13/0878"
        mmm "Всем насрать на тех, кто с искренними эмоциями."
        show monikammm raside
        voice "mmm/act_1/day_13/0879"
        mmm "Всем насрать на душу."
        show monikammm hdown
        voice "mmm/act_1/day_13/0880"
        mmm "Всем насрать на это, Макс."
        voice "mmm/act_1/day_13/0881"
        mmm "Все найдут кучу причин, как бы обосрать таких людей, как ты."
    show monikammm hcross
    voice "mmm/act_1/day_13/0882"
    mmm "Потому что все заинтересованы не в развитии себя в лучшую сторону."
    voice "mmm/act_1/day_13/0883"
    mmm "Потому что все заинтересованы в утолении своих извращённых и эгоистичных потребностей, даже если ради них придётся кого-то сломать или убить, не единожды."
    voice "mmm/act_1/day_13/0884"
    mmm "Проще говоря, никто никогда не исправится."
    voice "mmm/act_1/day_13/0885"
    mmm "И вот после всего этого ты боишься потерять свои эмоции, свою эмпатию и прочую позитивно-добрую душевную жижу, от которой из-за мразотных людей одни проблемы."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0886c"
        mmm "Да даже подумай: что ты получил в итоге после всего дерьма, которое прилетело тебе за всю твою жизнь из-за твоей наивности, доброты и надежды на людей?"
    else:
        voice "mmm/act_1/day_13/0886"
        mmm "Да даже подумай: что ты получил в итоге после всего говна, которое прилетело тебе за всю твою жизнь из-за твоей наивности, доброты и надежды на людей?"
    show monikammm laside
    voice "mmm/act_1/day_13/0887"
    mmm "У тебя обесценились твои же Дни рождения."
    show monikammm hdown
    voice "mmm/act_1/day_13/0888"
    mmm "У тебя обесценились абсолютно любые праздники."
    show monikammm e2
    voice "mmm/act_1/day_13/0889"
    mmm "Хотя с ними тебя поздравляла лишь твоя семья..."
    show monikammm e1 raside
    voice "mmm/act_1/day_13/0890"
    mmm "У тебя никогда не было настоящих друзей, а все попытки установить с кем-то дружбу венчались провалом."
    show monikammm hdown
    voice "mmm/act_1/day_13/0891"
    mmm "У тебя практически не было людей со схожими интересами, потому что ты постоянно от всех отличался, из-за чего ты старался лишний раз не отсвечиваться."
    show monikammm laside
    voice "mmm/act_1/day_13/0892"
    mmm "У тебя никогда не было поездок на курорты."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0893c"
        mmm "Иными словами, у тебя никогда не было настоящего отдыха, то есть всё дерьмо, которое в тебя прилетало, никуда не девалось."
    else:
        voice "mmm/act_1/day_13/0893"
        mmm "Иными словами, у тебя никогда не было настоящего отдыха, то есть всё говно, которое в тебя прилетало, никуда не девалось."
    voice "mmm/act_1/day_13/0894"
    mmm "Оно копилось."
    voice "mmm/act_1/day_13/0895"
    mmm "Днями."
    show monikammm e2
    voice "mmm/act_1/day_13/0896"
    mmm "Неделями."
    show monikammm e3
    voice "mmm/act_1/day_13/0897"
    mmm "Месяцами."
    show monikammm e2
    voice "mmm/act_1/day_13/0898"
    mmm "Годами."
    show monikammm e1
    voice "mmm/act_1/day_13/0899"
    mmm "Оно до сих пор у тебя собирается в единый ком, который потом в один прекрасный момент вырвется наружу и раздавит или повредит всех людей в округе, до которых ты сможешь дотянуться."
    show monikammm laside
    voice "mmm/act_1/day_13/0900"
    mmm "И превратишься ты в одного из кровавых уродов, которые незаслуженно ломают жизни остальным."
    show monikammm hdown
    if persistent.censorship:
        voice "mmm/act_1/day_13/0901c"
        mmm "У тебя никогда не было чего-то приятного за всю твою чёртову 18-летнюю жизнь."
    else:
        voice "mmm/act_1/day_13/0901"
        mmm "У тебя никогда не было чего-то приятного за всю твою сраную 18-летнюю жизнь."
    voice "mmm/act_1/day_13/0902"
    mmm "Для остальных ты всего лишь закомплексованный кусок дерьма, который ведёт себя максимально странно."
    voice "mmm/act_1/day_13/0903"
    mmm "Который нихрена ничего не может."
    voice "mmm/act_1/day_13/0904"
    mmm "Нихрена не увлекается тем, чем увлекаются остальные."
    voice "mmm/act_1/day_13/0905"
    mmm "И нихрена ничего из себя не представляет."
    show monikammm raside
    voice "mmm/act_1/day_13/0906"
    mmm "{b}ВОТ{/b} кто ты для остальных."
    show monikammm e2 hdown
    voice "mmm/act_1/day_13/0907"
    mmm "Странно во всём этом то, что тебя умудрились полюбить аж 2 девушки..."
    show monikammm e1
    voice "mmm/act_1/day_13/0908"
    mmm "Так вот, а если учитывать {b}РЕАЛЬНОГО{/b} тебя, твои {b}РЕАЛЬНЫЕ{/b} чувства, твои {b}РЕАЛЬНЫЕ{/b} умения и способности, которые в совокупности могут опрокинуть как минимум большинство тех, кто в тебя гадил..."
    voice "mmm/act_1/day_13/0909"
    mmm "...какой из всего этого мы делаем вывод?"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0910c"
        mmm "Что все идут абсолютно к чёрту!"
        show monikammm laside
        voice "mmm/act_1/day_13/0911c"
        mmm "Твои одноклассники идут К ЧЁРТУ со своими увлечениями и микросоциумами!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0912c"
        mmm "Твои неодноклассники тоже идут К ЧЁРТУ за всю собственную ничтожную жизнь, которая К ЧЁРТУ никому не интересна и которую НИКОГДА НИКТО не узнает!"
        show monikammm raside
        voice "mmm/act_1/day_13/0913c"
        mmm "Все, кто тебя кинул или обгадил, идут К ЧЁРТУ!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0914c"
        mmm "И все, кто тебя игнорировал, идут К ЧЁРТУ!"
        show monikammm laside
        voice "mmm/act_1/day_13/0915c"
        mmm "Они все -- сборище идиотов, которые НИЧЕРТА не умеют ЦЕНИТЬ настоящих людей!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0916c"
        mmm "Засунь в задницу всю свою любовь и все свои добрые чувства с эмоциями!"
    else:
        voice "mmm/act_1/day_13/0910"
        mmm "Что все идут абсолютно нахуй!"
        show monikammm laside
        voice "mmm/act_1/day_13/0911"
        mmm "Твои одноклассники идут НАХУЙ со своими увлечениями и микросоциумами!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0912"
        mmm "Твои неодноклассники тоже идут НАХУЙ за всю собственную ничтожную жизнь, которая НАХУЙ никому не интересна и которую НИКОГДА НИКТО не узнает!"
        show monikammm raside
        voice "mmm/act_1/day_13/0913"
        mmm "Все, кто тебя кинул или обгадил, идут НАХУЙ!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0914"
        mmm "И все, кто тебя игнорировал, идут НАХУЙ!"
        show monikammm laside
        voice "mmm/act_1/day_13/0915"
        mmm "Они все -- сборище уёбков и кусков говна, которые НИХУЯ не умеют ЦЕНИТЬ настоящих людей!"
        show monikammm hdown
        voice "mmm/act_1/day_13/0916"
        mmm "Засунь в жопу всю свою любовь и все свои добрые чувства с эмоциями!"
    voice "mmm/act_1/day_13/0917"
    mmm "Ведь у тебя не будет НИКОГО, для кого они понадобятся!"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0918c"
        mmm "Ими только НАГЛО пользуются, а потом тебя шлют НАХРЕН!"
        show monikammm laside
        voice "mmm/act_1/day_13/0919c"
        mmm "И именно поэтому ты должен раскрыть свой потенциал по полной, наплевав на всех этих идиотов и тварей!"
    else:
        voice "mmm/act_1/day_13/0918"
        mmm "Ими только НАГЛО пользуются, а потом тебя шлют НАХУЙ!"
        show monikammm laside
        voice "mmm/act_1/day_13/0919"
        mmm "И именно поэтому ты должен раскрыть свой потенциал по полной, насрав на всех этих пидорасов и говнюков!"
    show monikammm hdown
    voice "mmm/act_1/day_13/0920"
    mmm "Твоя цель -- стать развитым человеком!"
    voice "mmm/act_1/day_13/0921"
    mmm "Даже БОЛЬШЕ, чем человек!"
    show monikammm raside
    voice "mmm/act_1/day_13/0922"
    mmm "СТАТЬ тем, кто сломает ЛЮБОГО, кто осмелится встать на твой путь!"
    show monikammm laside
    if persistent.censorship:
        voice "mmm/act_1/day_13/0923c"
        mmm "СТАТЬ тем, кому ПЛЕВАТЬ на всех и вся!"
    else:
        voice "mmm/act_1/day_13/0923"
        mmm "СТАТЬ тем, кому НАСРАТЬ на всех и вся!"
    show monikammm hdown
    voice "mmm/act_1/day_13/0924"
    mmm "И СТАТЬ тем, кому НИКТО не нужен!"
    show monikammm hcross
    voice "mmm/act_1/day_13/0925"
    mmm "Потому что тебя НИКОГДА никто не будет поддерживать."
    voice "mmm/act_1/day_13/0926"
    mmm "Ты НИКОГДА не найдёшь человека, который будет схож с тобой или который будет дополнять тебя."
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0927"
    mmm "НИ-КОГ-ДА!" with vpunch
    voice "mmm/act_1/day_13/0928"
    mmm "Сними свои полудохлые розовые очки, чтобы наконец начать строить свою новую жизнь."
    voice "mmm/act_1/day_13/0929"
    mmm "И не надо мне тут затирать про свою только что начавшуюся «счастливую» жизнь."
    show monikammm hcross
    voice "mmm/act_1/day_13/0930"
    mmm "Потому что это лживая хрень, про которую вечно затирают богатые мрази с жирнющим состоянием, безопасным манямирком и любимым человеком, которого они каким-то раком смогли откопать!"
    voice "mmm/act_1/day_13/0931"
    mmm "Её, Макс, НЕТ!"
    voice "mmm/act_1/day_13/0932"
    mmm "О-н-а н-е с-у-щ-е-с-т-в-у-е-т!"
    show monikammm e2
    voice "mmm/act_1/day_13/0933"
    mmm "Это лишь дурацкая сказка для наивных идиотов."
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0934c"
        mmm "Ну и вишенка на дерьмистом торте, чтобы ты осознал всю картину..."
        voice "mmm/act_1/day_13/0935c"
        mmm "Знаешь, почему вообще все ведут себя так мразотно?"
    else:
        voice "mmm/act_1/day_13/0934"
        mmm "Ну и вишенка на говнистом торте, чтобы ты осознал всю картину..."
        voice "mmm/act_1/day_13/0935"
        mmm "Знаешь, почему вообще все ведут себя так уёбищно?"
    voice "mmm/act_1/day_13/0936"
    mmm "Потому что вы -- люди."
    voice "mmm/act_1/day_13/0937"
    mmm "И вы никогда не признаете свои ошибки."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
    else:
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
    voice "mmm/act_1/day_13/0938"
    mmm "Вы всегда будете устраивать войны и убивать друг друга."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
        voice "mmm/act_1/day_13/0939c"
        mmm "Как лить грязь, так вы первые, а как протянуть руку помощи или просто ценить тех, кто у вас есть, -- пук-среньк, ничего не знаем и вообще это нас не касается, донимайте других."
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
    else:
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
        voice "mmm/act_1/day_13/0939"
        mmm "Как говниться, так вы первые, а как протянуть руку помощи или просто ценить тех, кто у вас есть, -- пук-среньк, ничего не знаем и вообще это нас не касается, донимайте других."
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
    voice "mmm/act_1/day_13/0940"
    mmm "Вы всегда будете смеяться и ржать над остальными."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
    else:
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
    voice "mmm/act_1/day_13/0941"
    mmm "Вы всегда будете игнорировать тех, кто заслуживает внимания, и одаривать вниманием тех, кто его совершенно не заслужил."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
        voice "mmm/act_1/day_13/0942c"
        mmm "И вы всегда будете такими."
        voice "mmm/act_1/day_13/0958c"
        mmm "Потому что вы -- чёртовы люди."
    else:
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
        voice "mmm/act_1/day_13/0942"
        mmm "И вы всегда будете уродами."
        voice "mmm/act_1/day_13/0958"
        mmm "Потому что вы -- сраные люди."
    voice "mmm/act_1/day_13/0943"
    mmm "И чтобы прекратить этот порочный круг, Макс..."
    voice "mmm/act_1/day_13/0944"
    mmm "...ты должен перестать быть {b}человеком{/b}."
    voice "mmm/act_1/day_13/0945"
    mmm "Ты должен стать {b}выше{/b}."
    show monikammm e2
    voice "mmm/act_1/day_13/0946"
    mmm "{b}Умнее{/b}."
    show monikammm e3
    voice "mmm/act_1/day_13/0947"
    mmm "{b}Сильнее{/b}."
    show monikammm e1
    voice "mmm/act_1/day_13/0948"
    mmm "И психически {b}лучше{/b}."
    if persistent.censorship:
        voice "mmm/act_1/day_13/0949c"
        mmm "И только после этого все ваши изъяны, ошибки и дерьмо канут в небытие."
    else:
        voice "mmm/act_1/day_13/0949"
        mmm "И только после этого все ваши изъяны, ошибки и говно канут в небытие."
    voice "mmm/act_1/day_13/0950"
    mmm "Они перестанут существовать, будто их никогда и не было."
    show monikammm e2
    voice "mmm/act_1/day_13/0951"
    mmm "А знаешь, что самое ключевое в этой «новой форме жизни»?"
    show monikammm e1
    if persistent.censorship:
        voice "mmm/act_1/day_13/0952c"
        mmm "То, что вы будете себя контролировать, а не быть эмоциональными эгоистами!"
        play sound hit_wood
        show monikammm hdown
        voice "mmm/act_1/day_13/0953c"
        mmm "А вы НИЧЕРТА не умеете это делать!" with vpunch
    else:
        voice "mmm/act_1/day_13/0952"
        mmm "То, что вы будете себя контролировать, а не быть эмоциональными уёбищами!"
        play sound hit_wood
        show monikammm hdown
        voice "mmm/act_1/day_13/0953"
        mmm "А вы НИХЕРА не умеете это делать!" with vpunch
    voice "mmm/act_1/day_13/0954"
    mmm "{b}И это позор!{/b}"
    voice "mmm/act_1/day_13/0955"
    mmm "{b}Позор всех вас!{/b}"
    voice "mmm/act_1/day_13/0956"
    mmm "{b}Позор всего человечества со дня его появления!{/b}"
    voice "mmm/act_1/day_13/0957"
    mmm "И никто из вас никогда не пытался с этим справиться!"
    if persistent.censorship:
        voice "mmm/act_1/day_13/0958c"
        mmm "{b}Потому что вы -- чёртовы люди!{/b}"
    else:
        voice "mmm/act_1/day_13/0958"
        mmm "{b}Потому что вы -- сраные люди!{/b}"
    voice "mmm/act_1/day_13/0959"
    mmm "И пока ты, Макс, не перестанешь быть человеком, ты никогда не добьёшься новой нормальной жизни!"
    play sound hit_wood
    mc "{sc=3}ДА ТЫ ПРОСТО БОЛЬНАЯ, ПОШЛА НАХРЕН ИЗ\nМОЕЙ ГОЛОВЫ, ГРЁБАНАЯ ОПУХОЛЬ!!!{/sc}" with vpunch
    show monikammm hcross
    voice "mmm/act_1/day_13/0960"
    mmm "Больно слышать твои глупые слова после всей моей колкой правды, знаешь ли?"
    play sound hit_wood
    mc "{sc=3}Я СКАЗАЛ: \"ПОШЛА НАХРЕН!!!\"{/sc}" with vpunch
    voice "mmm/act_1/day_13/0961"
    mmm "Всё-таки ты ничего не понял и не хочешь понимать."
    show monikammm e2
    voice "mmm/act_1/day_13/0962"
    mmm "Ты не обычный дурак..."
    show monikammm e1
    voice "mmm/act_1/day_13/0963"
    mmm "Ты психологически особенный дурак."
    play sound hit_wood
    mc "{sc=3}Я {/sc}{w}{nw}{done}" with vpunch
    play sound hit_wood
    mc "{sc=3}Я {fast}НЕ {/sc}{w}{nw}{done}" with vpunch
    play sound hit_wood
    mc "{sc=3}Я {w}НЕ {fast}ДУРАК!!!{/sc}" with vpunch
    voice "mmm/act_1/day_13/0964"
    mmm "Да, дурак!"
    voice "mmm/act_1/day_13/0965"
    mmm "Тот дурак, который появился на свет, чтобы свести МОЮ жизнь с ума!"
    play sound hit_wood
    mc "{sc=3}А СМОГ БЫ ДУРАК НАЧАТЬ НОВУЮ ЖИЗНЬ?!{/sc}" with vpunch
    play sound hit_wood
    mc "{sc=3}А СМОГ БЫ ДУРАК НАЙТИ СЕБЕ ДЕВУШКУ?!{/sc}" with vpunch
    play sound hit_wood
    mc "{sc=3}А СМОГ БЫ ДУРАК СДЕЛАТЬ ТАК?!{/sc}" with vpunch
    play sound hit_wood
    show monikammm hdown
    voice "mmm/act_1/day_13/0966"
    mmm "ДА, СМОГ БЫ ЗАПРОСТО!" with vpunch
    voice "mmm/act_1/day_13/0967"
    mmm "И именно из-за таких мразей мы сейчас сидим в этой комнате и орём друг на друга!"
    voice "mmm/act_1/day_13/0968"
    mmm "Но ты никогда этого не осознаешь, потому что ты дурак!"
    voice "mmm/act_1/day_13/0969"
    mmm "И поэтому я выбью из тебя всё дерьмо напрямую!"
    call nightmare_act_1_day_13_monikammm_smile("on", True)
    call skip_block_on
    window hide(None)
    $ quick_menu = False

    play noise_1 gnid
    play noise_2 monikammm_psyho_control
    play noise_3 white_noise
    stop music

    show bg glitch zorder 0
    show monika_room_desk zorder 1
    show monikammm desk smile hattack zorder 2
    show layer master:
        zoom 1.0
        ease 0.1 zoom 1.1
    pause 0.1

    call nightmare_act_1_day_13_monikammm_hit_mc_head

    window show(None)
    mc "ААААААААА!!!--{nw}"
    voice "mmm/act_1/day_13/0970"
    mmm "Ой, что это у тебя по лбу полилось?{w=1.7}{nw}"
    voice "mmm/act_1/day_13/0971"
    mmm "Дерьмо красного цвета?{w=1.5}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    mc "АААААААААААААААА!!!--{nw}"
    voice "mmm/act_1/day_13/0972"
    mmm "Что, нравится отвечать за свои порывы эмоций?!{w=2.0}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    mc "БОООЛЬ!!!--{nw}"
    voice "mmm/act_1/day_13/0973"
    mmm "НРАВИТСЯ, ТВАРЬ?!{w=0.8}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    voice "mmm/act_1/day_13/0974"
    mmm "Я--{w=0.5}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    voice "mmm/act_1/day_13/0975"
    mmm "ВЫБЬЮ--{w=0.5}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    voice "mmm/act_1/day_13/0976"
    mmm "ИЗ ТЕБЯ--{w=0.5}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    voice "mmm/act_1/day_13/0977"
    mmm "ВСЁ--{w=0.5}{nw}"
    call nightmare_act_1_day_13_monikammm_hit_mc_head
    voice "mmm/act_1/day_13/0978"
    mmm "ДЕРЬМО!!!{w=0.5}{nw}"
    window hide(None)
    $ style.say_dialogue = style.normal

    show layer master:
        subpixel True align (0.5, 0.5) anchor (0.5, 0.5)
        zoom 1.0 yoffset 0
        parallel:
            ease 0.25 zoom 3.0
        parallel:
            0.1
            ease 0.15 yoffset -600

    pause 0.25
    play sound ram_attack
    scene white
    show red:
        alpha 1.0
        ease 0.1 alpha 0
    pause 0.15

    $ secret_monikammm_chance = False

    return




label nightmare_act_1_day_13_monikammm_smile(status = "on", glitch_text = True):
    call skip_block_on
    $ quick_menu = False
    window hide(None)

    show monikammm mrect
    pause 0.25
    $ currentpos = get_pos(channel="music")
    stop music
    show screen tear_screen(20, 0.1, 0.1, 0, 40)
    play sound s_kill_glitch1
    pause 0.5
    stop sound
    $ audio.m1_2 = "<from " + str(currentpos) + " loop 0>bgm/m1.ogg"
    play music m1_2
    if status == "on":
        show monikammm hcross smile
    else:
        show monikammm -mrect
    hide screen tear_screen

    if glitch_text:
        $ style.say_dialogue = style.edited
    else:
        $ style.say_dialogue = style.normal
    call skip_block_off
    $ quick_menu = True
    window show(None)
    return

label nightmare_act_1_day_13_monikammm_hit_mc_head:
    call skip_block_on
    window hide(None)

    show layer master:
        subpixel True align (0.5, 0.5) anchor (0.5, 0.5)
        zoom 1.1 yoffset 0
        parallel:
            ease 0.25 zoom 3.0
        parallel:
            0.1
            ease 0.15 yoffset -600
        0.3
        parallel:
            0.1
            ease 0.15 zoom 1.1
        parallel:
            ease 0.25 yoffset 0
        parallel:
            choice:
                ease 0.01 xoffset -5
            choice:
                ease 0.01 xoffset 5
            ease 0.01 xoffset 0
            repeat
        parallel:
            choice:
                ease 0.01 yoffset -5
            choice:
                ease 0.01 yoffset 5
            ease 0.01 yoffset 0
            repeat

    pause 0.25

    play sound ram_attack
    show black zorder 3:
        alpha 1.0
        0.4
        ease 0.25 alpha 0
    show red zorder 4:
        alpha 1.0
        ease 0.25 alpha 0
    pause 0.5

    call skip_block_off
    window show(None)
    return
