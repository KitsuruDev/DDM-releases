
init python:
    poem_words_a1_d11 = {
        1: (_("Тишина"), "mc", 0.65, 0.31),
        2: (_("Жара"), "mc", 0.3, 0.445),
        3: (_("Марево"), "mc", 0.6, 0.514),
        4: (_("Природа"), "mc", 0.25, 0.31),
        5: (_("Ветер"), "mc", 0.35, 0.107),
        6: (_("Капать"), "mc", 0.7, 0.514),
        7: (_("Крыша"), "mc", 0.35, 0.445),
        8: (_("Шум"), "mc", 0.7, 0.107),
        9: (_("Водопад"), "y", 0.6, 0.514),
        10: (_("Тягучесть"), "y", 0.2, 0.305),
        11: (_("Гром"), "y", 0.68, 0.305),
        12: (_("Вспышка"), "y", 0.4, 0.514),
        13: (_("Резонансный звук"), "y", 0.72, 0.1),
        14: (_("Сердце"), "y", 0.35, 0.1),
        15: (_("Темнота"), "y", 0.19, 0.305),
        16: (_("Шум"), "y", 0.70, 0.514),
        17: (_("Глаза"), "mc", 0.65, 0.31),
        18: (_("Стресс"), "mc", 0.44, 0.445),
        19: (_("Порыв"), "y", 0.37, 0.305),
        20: (_("Мир"), "y", 0.68, 0.305)
    }




label poem_act_1_day_11:
    call skip_block_on
    scene bg notebook_full_mc
    show mc_chibi turned at st_c21:
        xzoom -1
    show y_chibi turned at st_c22
    with dissolve_scene_full
    play music yuri_poem fadein 3.0
    "..."
    "...уже минуту сидим и ничего не говорим."
    show y_chibi e2
    mc "Да как начать-то..."
    y "Попробуй написать, что первое пришло в голову."
    y "А то, если будешь зацикливаться на чём-то одном, ничего не придумаешь."
    y "Нам так один раз Моника сказала."
    show y_chibi e1
    y "Точнее, дала такой совет, ещё когда мы только начали заниматься стихами..."
    mc "Хм."
    y "Жаль, что она отошла от такой помощи."
    y "Я бы обязательно подчерпнула от неё что-нибудь новое."
    show mc_chibi e2
    show y_chibi e2
    mc "Моника давала общие советы?"
    y "Да."
    y "\"Писательский совет дня от Моники\", -- так она их называла, если мне не изменяет память..."
    mc "О как, не знал."
    show mc_chibi e1
    mc "Но ладно, попробую сейчас строфы накинуть."
    "Может, пойти банальным путём?"
    "Тут довольно уютно и тихо."
    "Тихо..."
    call screen poem_game_duo(*poem_words_a1_d11[1])
    show mc_chibi at chibi_hop
    pause 0.72
    "Ну и чё?"
    "Ну и всё."
    show mc_chibi ce
    mc "Приехали..."
    y "Н-не опускай руки, Макс!"
    show y_chibi e1
    y "Попробуй полностью избавиться от мыслей и писать так, как выйдет."
    show mc_chibi e2
    mc "Тогда получится каша."
    show y_chibi e2
    mc "Как я могу избавиться от мыслей, если это нереально?"
    show mc_chibi e1
    mc "Мне же надо и созвучие контролировать, и количество слогов, и ударения..."
    y "Именно поэтому ты сейчас завяз."
    y "Стих должен быть полётом фантазии, а не клеткой."
    show mc_chibi e2
    mc "Удобно такое говорить, когда ты умеешь писать стихотворения."
    show y_chibi e1
    y "Нет, ты не так меня понимаешь..."
    show y_chibi e2
    y "Я имела в виду, что ты должен акцентироваться на мыслях и следовать за ними, а не запутываться в критериях стиля."
    show mc_chibi e1
    mc "Так в том и прикол, что я не знаю, как дальше писать."
    mc "Созвучные слова хоть иногда тебя наталкивают на продолжение сюжета."
    mc "А тут просто пустота."
    show y_chibi e1
    y "...не знаю, возможно, у меня другой тип мышления..."
    mc "В этом и кроется главный критерий, Юри."
    show mc_chibi e2
    show y_chibi e2
    y "Но ты себя принижаешь."
    mc "А где я не прав?"
    y "..."
    show mc_chibi e1
    "Блин, жарко стало..."
    call screen poem_game_duo(*poem_words_a1_d11[2])
    show mc_chibi at chibi_hop
    pause 0.72
    y "О-о, видишь?"
    y "У тебя уже вышло четверостишие!"
    mc "Обычное дело, ничего такого."
    show mc_chibi e2
    y "Но ведь тебе пришла мысль, а не одно слово, верно?"
    mc "...пришла."
    y "Поэтому продолжай в том же духе, и тогда всё получится!"
    show mc_chibi e1
    mc "Угу."
    "Не знаю, на меня что-то...{w}негатив накатил."
    show mc_chibi ce
    "Устал из-за состояния?"
    "Или Юри вывела из равновесия?"
    "В любом случае надо собраться и написать этот стих."
    "А ещё, точно, не забыть выслушать откровение Юри по поводу своей проблемы."
    y "Макс?"
    show mc_chibi e1
    mc "Ай..."
    y "Неужели тебя так сильно одолевают мысли?"
    show mc_chibi e2
    mc "Ну, как видишь."
    show mc_chibi e1
    mc "Это всё неконтролируемо..."
    y "Я начинаю за тебя переживать..."
    mc "Ой, нет, не надо, я привык."
    mc "Ты лучше прибереги свои нервы для других случаев."
    y "Но ведь тебе от них нехорошо..."
    show mc_chibi e2
    mc "Нет, всё в порядке."
    mc "Не волнуйся."
    "Не хватало тут ещё, чтобы Юри на себя начала накручивать..."
    show mc_chibi e1
    mc "Так, ладно, вернёмся к стиху..."
    "Жара..."
    "Жара на асфальте..."
    call screen poem_game_duo(*poem_words_a1_d11[3])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d11[4])
    show mc_chibi at chibi_hop
    pause 0.72
    y "Ещё одно четверостишие!"
    mc "...да, что-то стало получаться."
    "Окей, немножко нормализовался и втянулся."
    "Продолжаем..."
    call screen poem_game_duo(*poem_words_a1_d11[5])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d11[6])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d11[7])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d11[8])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "Так, стоп."
    mc "Чего я тут один пишу?"
    y "Ты поймал вдохновение..."
    show mc_chibi e2
    mc "Юри, у нас же парный стих."
    mc "Тебе тоже нужно приложить свою руку."
    show y_chibi e1
    y "А, конечно..."
    "Прекрасно понимаю, что она на меня сейчас смотрела."
    "Поэтому аккуратно переключил её на стихотворение."
    show mc_chibi e1
    window hide
    call window_dialog("y")
    call screen poem_game_duo(*poem_words_a1_d11[9])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[10])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[11])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[12])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[13])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    show mc_chibi e1
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[14])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[15])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[16])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    call window_dialog("mc")
    window auto
    mc "Ничего себе."
    mc "Ты целую стопку строф настрочила на одном дыхании."
    show mc_chibi e2
    mc "Как у тебя так выходит?"
    y "Наверное, я уже натренирована, хе-хе..."
    mc "Это заметно..."
    show y_chibi e2
    y "Я думаю, тебе стоит продолжить стих дальше."
    mc "А, уже?"
    show mc_chibi e1
    mc "Ну-ка..."
    "Надо же пробежаться глазами, что там Юри настрочила..."
    "..."
    mc "Ты тут так всё описала, что даже добавить в продолжение нечего."
    mc "Тогда надо как-то закончить...{w}или слишком маленький стих на двоих будет..."
    y "Не торопись, Макс, подожди..."
    show mc_chibi e2
    show y_chibi e1
    y "Как говорила, пиши так, как получится."
    y "Нам не нужен идеал с рамками."
    y "Нам нужен стих."
    show y_chibi e2
    y "Поэтому если ты считаешь, что здесь стоит закончить, то я поддержу твоё решение."
    mc "...окей."
    show mc_chibi e1
    mc "Дай подумать..."
    show mc_chibi ce
    "..."
    "М-м-м..."
    show mc_chibi e1
    "Смотрю я на часть Юри и...{w}ничего в голову не приходит."
    "Или...{w}ну разве что условный конец."
    call screen poem_game_duo(*poem_words_a1_d11[17])
    show mc_chibi at chibi_hop
    pause 1.44
    call screen poem_game_duo(*poem_words_a1_d11[18])
    show mc_chibi at chibi_hop
    pause 0.72
    mc "Нет, кажется, я всё."
    mc "Сегодня, как и вчера, вдохновение идёт плохо и отвратительно."
    y "Сегодня -- точно нет."
    show y_chibi e1
    y "Твои строфы очень легко и приятно читаются."
    show mc_chibi e2
    show y_chibi e2
    mc "Разве?"
    y "Сейчас доведу стихотворение до конца, и ты в этом убедишься."
    show mc_chibi e1
    show y_chibi e1
    window hide
    call window_dialog("y")
    call screen poem_game_duo(*poem_words_a1_d11[19])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    pause 0.72
    call screen poem_game_duo(*poem_words_a1_d11[20])
    show y_chibi hop at chibi_hop
    pause 0.72
    show y_chibi turned
    call window_dialog("mc")
    window auto
    y "Вот."
    show y_chibi e2
    y "Давай посмотрим на результат."
    call skip_block_off
    window hide

    stop music fadeout 3.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0

    return
