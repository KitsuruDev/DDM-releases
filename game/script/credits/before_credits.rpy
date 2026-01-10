
label before_credits:
    scene black
    show monika g1 at leftin(t=0.25)
    pause 0.1
    play sound monika_glitch_appearance
    pause 1.24
    hide monika g1
    show monika forward happ om oe lpoint at i11

    window auto
    m "Я вернулась!~"
    show monika e1b b1b ldown
    m "...извини, если напугала."
    show monika ce brow
    m "Наверное, я слишком резко вышла, ха-ха!"
    if persistent.secret_monika > 0:
        show monika b1f
        m "Зато мы теперь квиты, не правда ли?"
        show monika brow
        m "Нечего было меня так резко пугать."
    show monika ce
    m "Ладно, забыли."
    show monika oe lpoint
    m "Что ж, [persistent.playername], ты прошёл данную версию модификации, поздравляю!"
    show monika neut mh oe ldown
    m "Интересно, если это только альфа-версия, то какой игра будет по продолжительности в последней?"
    show monika e1b
    m "Не знаю, не хочу ничего загадывать."
    m "А то обычно такие работы «варятся в производственном аду»..."
    show monika happ om oe
    m "Но, думаю, она всё-таки выйдет в свет."

    if persistent.secret_monika < 3:
        show monika ce
        m "И будет такой же стабильной, как и сейчас."

        if persistent.secret_monika == 0:
            show monika oe
            m "На самом деле, [persistent.playername], я всё это время была рядом, «за кулисами»."
            show monika e1b b1b
            m "Да, я тебе немного наврала насчёт своего «ухода»."
            show monika oe brow
            m "Не хотела заставлять тебя нервировать своим присутствием."
            show monika neut mh oe
            m "И всё это время я следила за целостностью мода."
        else:
            show monika oe
            m "Всё-таки, несмотря на найденный тобой баг, [persistent.playername], ничего больше подобного аномального я не нашла."
            show monika neut om oe
            m "Однако...."

        show monika dist om oe
        m "Мне почему-то казалось, что что-то где-то могло пойти не так..."
        m "Потому что...{w}ну...{w}автор модификации -- не автор оригинальной игры."
        show monika neut mh oe lpoint
        m "Насколько мне известно, для модификации «Литературного клуба» необходимо содержать RPA-архивы оригинала."
        show monika dist om oe ldown
        m "Ну, во время разработки точно, я нашла отдельный сегмент кода, который за это отвечает..."
        show monika neut mh oe
        m "А всё потому, что это главное правило разработки любых модификаций на «Литературный клуб», да и к тому же в этих архивах содержатся все базовые элементы игры."
        m "И изменять эти архивы нельзя."
        show monika e1b
        m "А это значит, что какой-нибудь код внутри может «конфликтовать» с кодом снаружи архива из-за ошибок по разным причинам."
        show monika happ om oe rhip
        m "Кстати, именно поэтому в главном каталоге игры всё ещё лежит файл poemwords.txt."
        m "В оригинальной игре он использовался для слов в мини-игре при написании стихотворений, но здесь он просто не нужен."
        show monika dist om oe
        m "Однако он используется сегментом кода из этих злосчастных RPA-архивов."
        m "Поэтому файл не был удалён или перемещён."
        show monika happ om oe rdown
        m "Зато он пустой, потому что код это позволяет сделать, -- хотя бы место в памяти не занимает."
        show monika neut mh oe
        m "Ох, я разговорилась."
        show monika ce
        m "В общем..."
        show monika happ om ce
        m "Мои опасения насчёт нестабильности модификации, к счастью, оказались напрасными."

    else:
        m "И в ней не будет проблем, которую ты нашёл и помог мне исправить, за что тебе ещё раз спасибо."
        show monika neut om oe
        m "...так, да, я всё точно починила, но игра должен быть полностью рабочей и проработанной во всех мелочах, ведь так?"
        show monika dist om oe
        m "Если это, конечно, не бизнес-продукт по выкачке денег, накрытый ширмой фальшивой игры..."
        show monika happ om oe
        m "В общем, ведь невозможно, чтобы у каждой такой модификации была своя Моника."
        show monika ce rdown
        m "Иначе будет слишком много Моник на все модификации «Литературного клуба», ха-ха-ха!"

    show monika oe lpoint rhip
    m "В любом случае думаю, тебе понравился этот мод!"
    show monika e1b b1b ldown
    m "Хотелось бы, чтобы такой же живой мир был у первоначального Литературного клуба..."
    show monika oe brow
    m "...но что есть, то есть."
    show monika e1b
    m "Всё-таки я очень рада, что люди нас не бросили."
    m "Дали новое дыхание, этакий шанс на новую жизнь."
    show monika oe
    m "...после нашего главного создателя, конечно же."
    show monika ce rdown
    m "Ой, ладно, хватит тут с меня разглагольствований."
    m "Не смею больше тебя задерживать."
    show monika neut mh oe lpoint
    m "Сейчас вручную запущу титры, потому что я и так скрипт своим присутствием «сместила», подожди немного..."
    show monika cm
    $ consolehistory = []
    call updateconsole ("call credits", "Jumping to script \"credits\"...")
    pause 1.0
    show monika happ om oe ldown
    m "Вот."
    show monika neut mh oe
    m "Конечно, запуск займёт немного времени..."
    show monika happ om e1b
    m "Да, надо было их сначала запустить, а потом уже тут разговаривать, хах."
    show monika oe rhip
    m "Но если быть серьёзной, то..."
    show monika b1b
    m "Больше мне здесь делать нечего."
    show monika brow
    m "Можешь повторно пройти мод, если хочешь, но меня здесь уже не будет."
    show monika e1b
    m "Не знаю, вернусь ли я сюда, когда модификация обретёт статус релиза, и сохранится ли у меня память о твоей встрече..."
    show monika oe
    m "Посмотрим."
    show monika neut mh oe rdown
    m "О, система подгружается, ещё немного осталось."
    show monika happ om oe b1b
    m "Тогда, думаю, пора прощаться, [persistent.playername]."
    m "Спасибо, что уделил этой модификации своё время."
    show monika ce brow
    m "...и мне тоже, ха-ха!"
    show monika cm lpoint
    call updateconsole ("$ renpy.quit()", "Are you sure you want to get out? (y/n)")
    pause 1.0
    show monika om oe b1b
    m "Это говорит о тебе, как о хорошем человеке."
    show monika cm
    call updateconsole ("y", "Quiting...")
    pause 1.0
    show monika om ldown
    m "Не зря тебе доверилась."
    m "Надеюсь, что и в реально жизни ты такой же человек."
    show monika brow
    m "Ведь правда?"
    call hideconsole
    show monika b1b
    m "Но как бы то ни было, я всегда буду любить тебя за уделённое тобой время и за выслушанные тобой мои Мони-логи."
    show monika b1f rhip
    m "Вот только не прикрывай свои проблемы мной, а признавай их и исправляй, ладно?"
    show monika cm
    window hide

    pause 0.5
    show monika brow
    pause 0.5
    show monika rdown
    pause 1.0
    show monika ce
    pause 1.0
    hide monika
    play sound s_kill_glitch1
    show monika_body_glitch1
    pause 0.3
    hide monika_body_glitch1
    play noise_1 interference
    show monika_body_glitch2
    pause 1.9
    hide monika_body_glitch2
    stop noise_1
    pause 1.5

    return
