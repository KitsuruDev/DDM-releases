## characters.rpy

init -1 python in Characters:
    from store import Transform

    dict, current = {}, None

    class CharactersImage:
        def __init__(self, name, age, gender, color, name_color, nationality, hobby, status, description, sprites={}, cut=36, zoom_profile=0.5):
            self.name = name
            self.profile = _(
                    "Имя: %(name)s.\nВозраст: %(age)s.\nПол: %(gender)s.\nЦвет: {color=%(color)s}%(name_color)s{/color}.\nНациональность: %(nationality)s.\nУвлечения: %(hobby)s.\nСтатус: %(status)s."
                ) % {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "color": color,
                    "name_color": name_color,
                    "nationality": nationality,
                    "hobby": hobby,
                    "status": status,
                }
            self.description = description
            self.sprites = sprites
            self.count = len(sprites)
            self.current_key = 1
            self.image = Transform(sprites[1][0], zoom = sprites[1][1])

            if isinstance(cut, int):
                cut = (282, cut, 400, 453)

            self.image_profile = Transform(sprites[1][0], crop = cut, zoom = zoom_profile)

            dict[self.name] = self

        def next_sprite(self, back=False):
            next_key = self.current_key - 1 if back else self.current_key + 1

            try: self.image = Transform(self.sprites[next_key][0], zoom = self.sprites[next_key][1])
            except KeyError:
                next_key = self.count if next_key == 0 else 1
                self.image = Transform(self.sprites[next_key][0], zoom = self.sprites[next_key][1])

            self.current_key = next_key


init python:
    character_gender_age_l = _("лет")
    character_gender_age_g = _("года")

    character_gender_male = _("мужской")
    character_gender_female = _("женский")

    character_nationality_japan_male = _("японец")
    character_nationality_japan_female = _("японка")
    character_nationality_russia_female = _("русская")
    character_nationality_usa_male = _("американец")
    character_nationality_usa_female = _("американка")
    character_nationality_uk_female = _("англичанка")


    ########## Объекты в каждой группе в алфавитном порядке ##########

    ##################### Главные персонажи #####################

    char_mc = CharactersImage(
    name = _("Макс"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#aaa9ad",
    name_color = _("металлический"),
    nationality = character_nationality_japan_male,
    hobby = _("изучение программных языков на досуге, прослушивание музыки, «спокойный» отдых"),
    status = _("ученик, участник Литературного клуба"),
    description = _("""\
В жизни Макса нетипично всё: начиная от имени, данного родителями в честь музыкальной группы, на концерте которой они встретились в середине \
90-ых годов, и заканчивая чрезмерно рациональным мышлением. С одной стороны, Макс рано психически вырос, из-за чего быстро потерял интерес к \
сверстникам и стал одиноким, что дало ему больше времени на себя, но с другой -- у него нет опыта в таких вещах, как дружба, любовь и другие \
виды взаимоотношения с людьми. Однако это не значит, что он этого сторонится -- напротив, Макс не нашёл нужных людей, которым мог бы доверять и \
которые увидели бы его «изнутри». Поэтому вступление в Литературный клуб можно считать его подарком судьбы: быстро найти общий язык и \
подружиться с четырьмя девушками с совершенно отличающимися друг от друга характерами, мягко говоря, невероятно, не говоря уже о сложном \
состоянии и психотипе самого Макса. Решив воспользоваться шансом по полной, он, спустя неделю пребывания в клубе, признался в любви к Монике, \
тщательного проанализировав всю сложившуюся ситуцию. И, кажется, у него началась новая жизнь. Станет ли она счастливее прошлой? Это уже зависит \
от него самого. Но одно можно сказать точно: держаться за неё Макс будет до последнего.
    """),
    sprites = {
    # Школьная форма
    1: ("mc turned neut", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- StormBlazed76 (Reddit)\nНабросок спрайта -- Satchely из Team Salvato\nПак спрайтов -- SomeDudeNamedAyat (Reddit)")),
    2: ("mc cross neut", 0.68, _("Школьная форма (поза со скрещенными руками)"), _("Художник -- StormBlazed76 (Reddit)\nНабросок спрайта -- Satchely из Team Salvato")),
    # Чёрная футболка с длинными рукавами форма
    3: ("mc turned casual neut", 0.68, _("Чёрная футболка с длинными рукавами (обычная поза)"), _("Художник -- StormBlazed76 (Reddit)")),
    4: ("mc cross casual neut", 0.68, _("Чёрная футболка с длинными рукавами (поза со скрещенными руками)"), _("Художник -- StormBlazed76 (Reddit)")),
    # Меню
    5: ("mod_assets/sprites/characters/mc/menu/art_mc_0.png", 0.47, _("Основное главное меню"), _("Художник -- Robert Fearnz#1547 (Discord, старый ник)")),
    # Меню
    6: ("mc_chibi turned", 1.0, _("Чиби"), _("Художник -- Hadrosaur838 (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Аватарка в мессенджере
    7: ("phone/assets/icons/mc.png", 0.6, _("Аватарка в мессенджере"), _("{vspace=440}Изображение от Natthaphon Sirisombatyuenyong на сайте {a=https://www.vecteezy.com/photo/68253485-cool-dog-in-samurai-armor-and-sunglasses-looking-stylish-and-fierce}www.vecteezy.com{/a} (Vecteezy)"))
    }
    )


    char_m = CharactersImage(
    name = _("Моника"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#4ED42D",
    name_color = _("изумрудный"),
    nationality = character_nationality_japan_female + "/" + character_nationality_usa_female,
    hobby = _("клавишные инструменты, стихотворения, клубная деятельность"),
    status = _("ученица, президент Литературного клуба"),
    description = _("""\
\"Умница, музыкант, лидер и просто красавица\", -- как один раз подумал про Монику Макс. С первого взгляда эта девушка может показаться \
напыщенной особой с богатыми родителями, однако такие стереотипы рушатся о её характер. Скрестив в себе любовь, доброту и лидерские качества, \
Моника с головой погрузилась в клубную деятельность, которая оказалось не такой уж и радужной, как она её себе представляла. Пробыв в \
Дискуссионном клубе некоторое время и сильно в нём разочаровавшись, она решила создать собственный клуб -- Литературный. Несмотря на все \
трудности, из-за которых он балансировал на грани развала, она нашла несколько человек на постоянной основе, с которыми крепко подружились. После
вступления в клуб Макса быстро в него влюбилась, и уже через неделю он ответил ей взаимностью, подойдя к любовному выбору со всей серьёзностью. \
Казалось бы, жизнь Моники «удалась», но в ней есть единственная, но важная проблема -- это отношения со строгими родителями, которые хотят \
вырастить дочь такой, какой они её видят. Однако если Моника справилась с опекой Литературного клуба, то и здесь справится на «максимальный \
балл». Правда же?
    """),
    sprites = {
    # Школьная форма
    1: ("monika forward happ", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    2: ("monika forward happ lpoint rhip", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    3: ("monika lean happ", 0.68, _("Школьная форма (наклонённая поза)"), _("Художник -- Satchely из Team Salvato")),
    4: ("monika lean_hear_down happ_cm_oe", 0.68, _("Школьная форма (наклонённая поза с опущенными волосами)"), _("Художник -- ButtermilkPaincakes (Reddit)")),
    5: ("monika lean_hear_down happ_cm_oe lpoint", 0.68, _("Школьная форма (наклонённая поза с опущенными волосами)"), _("Художник -- ButtermilkPaincakes (Reddit)")),
    6: ("monika cross", 0.68, _("Школьная форма (поза со скрещенными руками)"), _("Художник -- Phathom (Reddit)")),
    # Зелёная толстовка
    7: ("monika forward green_hoodie happ", 0.68, _("Зелёная толстовка (обычная поза)"), _("Художник -- StormBlazed76 (Reddit)\nДизайнер -- GHm")),
    8: ("monika forward green_hoodie happ lpoint rhip", 0.68, _("Зелёная толстовка (обычная поза)"), _("Художник -- StormBlazed76 (Reddit)\nДизайнер -- GHm")),
    9: ("monika lean green_hoodie happ", 0.68, _("Зелёная толстовка (наклонённая поза)"), _("Художник -- StormBlazed76 (Reddit)\nДизайнер -- GHm")),
    # Зелёная толстовка с джинсами
    10: ("monika forward green_hoodie_long happ", 0.68, _("Зелёная толстовка с джинсами"), _("Художник -- Rocky#1118 (Discord, старый ник)\nРедактирование -- Morbiusgreen (Reddit), SYwaves (Reddit)\n{vspace=310}Первоначально спрайт был сделан для мода World of Dreams")),
    11: ("monika forward green_hoodie_long happ lpoint rhip", 0.68, _("Зелёная толстовка с джинсами"), _("Художник -- Rocky#1118 (Discord, старый ник)\nРедактирование -- Morbiusgreen (Reddit), SYwaves (Reddit)\n{vspace=310}Первоначально спрайт был сделан для мода World of Dreams")),
    # Спортивная одежда (свободная)
    12: ("monika forward sport_casual happ", 0.68, _("Свободная спортивная одежда (обычная поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nДизайнер -- TakodaChr\n{vspace=390}Спрайт представлен командой Team Hope")),
    13: ("monika forward sport_casual happ lpoint rhip", 0.68, _("Свободная спортивная одежда (обычная поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nДизайнер -- TakodaChr\n{vspace=390}Спрайт представлен командой Team Hope")),
    14: ("monika lean sport_casual happ", 0.68, _("Свободная спортивная одежда (наклонённая поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nДизайнер -- TakodaChr\n{vspace=390}Спрайт представлен командой Team Hope")),
    # Белое платье
    15: ("monika forward white_dress happ", 0.68, _("Белое платье (обычная поза)"), _("Художник -- Cyrke (Reddit)")),
    16: ("monika forward white_dress happ lpoint rhip", 0.68, _("Белое платье (обычная поза)"), _("Художник -- Cyrke (Reddit)")),
    17: ("monika lean white_dress happ", 0.68, _("Белое платье (наклонённая поза)"), _("Художник -- Cyrke (Reddit)")),
    # Тело
    18: ("monika forward body happ pants", 0.68, _("Тело"), _("Художник -- Ezfi (Reddit)")),
    19: ("monika forward body happ lpoint pants", 0.68, _("Тело"), _("Художник -- Ezfi (Reddit)")),
    # Меню
    20: ("mod_assets/sprites/characters/monika/menu/art_monika_0.png", 0.55, _("Основное главное меню"), _("Художники -- RockMedved, FuckingMoniker_mmmmm")),
    21: ("gui/menu_art_m.png", 0.55, _("Второстепенное главное меню"), _("Художник -- Satchely из Team Salvato")),
    # Чиби
    22: ("m_chibi turned", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    23: ("m_chibi hop", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Эмоции
    24: ("monika forward eyes_shock", 0.68, _("Сильный шок"), _("Художник (глаза) -- Lunatic Rabbit (Reddit)")),
    25: ("monika forward eyes_tsur_1", 0.68, _("Сильное удивление"), _("Художник (глаза) -- Lunatic Rabbit (Reddit)")),
    26: ("monika forward happ eyes_tsed_1", 0.68, _("Пьяное состояние/соблазнение"), _("Художник (глаза) -- Lunatic Rabbit (Reddit)")),
    # Предметы
    27: ("monika forward happ lup poem_paper", 0.68, _("Предмет в руке -- стих"), _("{vspace=465}Сделано на основе свободного изображения")),
    28: ("monika forward happ lup planchette", 0.68, _("Предмет в руке -- планшет"), _("{vspace=465}Сделано на основе свободного изображения")),
    # Аватарка в мессенджере
    29: ("phone/assets/icons/m.png", 0.6, _("Аватарка в мессенджере"), _("Автор (не художник) -- Elckarow#8399 (Discord, старый ник)"))
    },
    cut = 60
    )


    char_n = CharactersImage(
    name = _("Нацуки"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#ff367c",
    name_color = _("огненно-розовый"),
    nationality = character_nationality_japan_female,
    hobby = _("коллекционирование манги, готовка кексов, простая кухня"),
    status = _("ученица, участница Литературного клуба"),
    description = _("""\
Забавный факт: чем меньше живое разумное существо, тем больше в нём проявляется своенравный характер. Нацуки очень бойкая девушка, часто \
встревающая из-за этого в неприятности (Рэйко не даст соврать). Но если углубиться в её жизнь, можно понять, что это бессознательная защита \
своей психики, которая иногда выходит за рамки «дозволенного». Переезд из Токио в Ниигату, постоянные ссоры родителей, автокатастрофа, в \
которую попала её мать, отец с расстройством, бедность и Хироши, превратившийся из друга в сталкера, -- такие факторы изменили Нацуки в корне. \
Однако в её жизни не всё так плохо: сначала была долгая дружба с Юри, полной её противоположностью, что подчёркивает удивительность данного \
факта, после -- вступление в Клуб выпечки, где она практиковалась в готовке кексов, а потом -- переход в Литературный клуб, позволивший \
коллекционировать мангу. Конечно, даже в нём не обходится без конфликтов, где контраст характеров с Юри даёт о себе знать, но всё быстро \
нивелируется, после чего клубная жизнь возвращается в прежнее русло. Нацуки нуждается в заботе, которой очень ей не хватает, особенно для \
раскрытия внутреннего потенциала. Ведь если маленькое пламя попадёт в правильные руки, оно будет способно обогреть всех вокруг себя.
    """),
    sprites = {
    # Школьная форма
    1: ("natsuki turned neut", 0.71, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    2: ("natsuki turned neut lhip rhip", 0.71, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    3: ("natsuki cross neut", 0.71, _("Школьная форма (поза со скрещенными руками)"), _("Художник -- Satchely из Team Salvato")),
    4: ("natsuki laughter cm", 0.75, _("Школьная форма (смех)"), _("Художник -- TSS~Danny#2610 (Discord, старый ник)")),
    # Футболка с юбкой
    5: ("natsuki turned casual neut", 0.71, _("Футболка с юбкой (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    6: ("natsuki turned casual neut lhip rhip", 0.71, _("Футболка с юбкой (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    7: ("natsuki cross casual neut", 0.71, _("Футболка с юбкой (поза со скрещенными руками)"), _("Художник -- Satchely из Team Salvato")),
    # Чёрная футболка
    8: ("natsuki turned black_shirt neut", 0.71, _("Чёрная футболка (обычная поза)"), _("Художники -- команда Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    9: ("natsuki turned black_shirt neut lhip rhip", 0.71, _("Чёрная футболка (обычная поза)"), _("Художники -- команда Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    10: ("natsuki cross black_shirt neut", 0.71, _("Чёрная футболка (поза со скрещенными руками)"), _("Художники -- команда Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    # Меню
    11: ("mod_assets/sprites/characters/natsuki/menu/art_natsuki_0.png", 0.55, _("Основное главное меню"), _("Художники -- RockMedved, FuckingMoniker_mmmmm")),
    12: ("gui/menu_art_n.png", 0.55, _("Второстепенное главное меню"), _("Художник -- Satchely из Team Salvato")),
    # Чиби
    13: ("n_chibi turned", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    14: ("n_chibi hop", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Голова
    15: ("natsuki turned fc neut", 0.71, _("Голова (анфас)"), _("Художник -- ThoseDamnShinyPants (Reddit)\nПак спрайтов -- ZachmanAwesomenessII (Reddit)")),
    16: ("natsuki turned fs neut", 0.71, _("Голова (наклонённая)"), _("Художник -- Satchely из Team Salvato")),
    17: ("natsuki turned fta", 0.71, _("Школьная форма (профиль)"), _("Художник -- Satchely из Team Salvato")),
    # Предметы
    18: ("natsuki turned neut lup poem_paper", 0.68, _("Предмет в руке -- стих"), _("{vspace=465}Сделано на основе свободного изображения")),
    # Аватарка в мессенджере
    19: ("phone/assets/icons/n.png", 0.6, _("Аватарка в мессенджере"), _("{vspace=465}Сделано на основе свободного изображения"))
    },
    cut = 110
    )


    char_s = CharactersImage(
    name = _("Сайори"),
    age = f"17 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#34B1FF",
    name_color = _("небесный"),
    nationality = character_nationality_japan_female,
    hobby = _("активный образ жизни, клубная деятельность"),
    status = _("ученица, вице-президент Литературного клуба"),
    description = _("""\
Если вы видите красный бант в рыжих волосах, знайте -- это заводное гиперактивное чудо. Сайори -- натуральная альтруистка и «рассадник» \
позитивного настроения. Но иногда её особенность может выйти из-под контроля, обернушись для неё злой шуткой. Макс, как её близкий друг, очень \
этим обеспокоен, хоть и ценит, что она смогла сохранить в себе такие качества, несмотря на жестокий мир. Сайори, как и подобает стереотипу \
её характера, бывает рассеяной и гиперактивной, но по возможности старается держать себя в руках, а в важные моменты выкручивает всю свою \
ответственность и серьёзность на 100 процентов. Эти качества помогли ей найти общий язык с Моникой на школьном фестивале, а позже -- стать \
вице-президентом её клуба. В редких случаях Сайори настигают «тучки» -- состояние, похожее на депрессивное, во время которого весь накопленный \
негатив начинает выходить наружу. Это тоже является побочным эффектом её чрезмерной позитивности и ещё одной задачей Макса по исправлению, \
потому что такое нельзя игнорировать. Сайори нужно научиться выстраивать личные границы при помощи контроля своей неиссякаемой энергии и, как \
следствие, чувств и эмоций. Как минимум это станет ключом к её счастливой жизни.
    """),
    sprites = {
    # Школьная форма
    1: ("sayori turned happ", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato\nОбновлённые спрайты эмоций (LayeredRedux-Sayori) -- Blue Quacker (Reddit)")),
    2: ("sayori turned happ lup rup", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    3: ("sayori tap nerv om", 0.68, _("Школьная форма (наклонённая поза)"), _("Художник -- Satchely из Team Salvato")),
    4: ("sayori turned happ lclose rclose", 0.68, _("Школьная форма (прижатые руки)"), _("Художник -- Heli Pro Gamer")),
    5: ("sayori turned neut e1d lclosefist rclosefist", 0.68, _("Школьная форма (прижатые кулаки)"), _("Художник -- Heli Pro Gamer")),
    # Розовая футболка
    6: ("sayori turned casual happ", 0.68, _("Розовая футболка (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    7: ("sayori turned casual happ lup rup", 0.68, _("Розовая футболка (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    8: ("sayori tap casual nerv om oe", 0.68, _("Розовая футболка (наклонённая поза)"), _("Художник -- Satchely из Team Salvato")),
    9: ("sayori turned casual happ lclose rclose", 0.68, _("Розовая футболка (прижатые руки)"), _("Художник -- Heli Pro Gamer")),
    10: ("sayori turned casual neut e1d lclosefist rclosefist", 0.68, _("Розовая футболка (прижатые кулаки)"), _("Художник -- Heli Pro Gamer")),
    # Школьная форма без пиджака
    11: ("sayori turned shirt happ", 0.68, _("Школьная форма без пиджака (обычная поза)"), _("Художник -- Yagamirai10 (Reddit)")),
    12: ("sayori turned shirt happ lup rup", 0.68, _("Школьная форма без пиджака (обычная поза)"), _("Художник -- Yagamirai10 (Reddit)")),
    13: ("sayori tap shirt nerv om oe", 0.68, _("Школьная форма без пиджака (наклонённая поза)"), _("Художник -- NormallyAverage (Reddit)")),
    # Футболка с котом
    14: ("sayori turned cat_shirt happ", 0.68, _("Футболка с котом (обычная поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nОплата работы -- Retronika")),
    15: ("sayori turned cat_shirt happ lup rup", 0.68, _("Футболка с котом (обычная поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nОплата работы -- Retronika")),
    16: ("sayori tap cat_shirt nerv om oe", 0.68, _("Футболка с котом (наклонённая поза)"), _("Художник -- @Lecraftx9 (Discord/Twitter)\nОплата работы -- Retronika")),
    # Камуфляжная ветровка
    17: ("sayori turned windbreaker happ", 0.68, _("Камуфляжная ветровка"), _("Художники -- команда Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    18: ("sayori turned windbreaker happ lup rup", 0.68, _("Камуфляжная ветровка"), _("Художники -- команда Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    # Пижама
    19: ("sayori turned pajamas happ", 0.68, _("Пижама"), _("Художник -- Malukah из Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    20: ("sayori turned pajamas happ lup rup", 0.68, _("Пижама"), _("Художник -- Malukah из Wretched Team (авторы Doki Doki Exit Music: Redux (Full Release))")),
    # Тело
    21: ("sayori turned body happ shorts", 0.68, _("Тело"), _("Художник -- Ezfi (Reddit)")),
    22: ("sayori turned body happ lup rup shorts", 0.68, _("Тело"), _("Художник -- Ezfi (Reddit)")),
    # Меню
    23: ("gui/menu_art_s.png", 0.55, _("Основное главное меню"), _("Художник -- Satchely из Team Salvato")),
    24: ("mod_assets/sprites/characters/sayori/menu/art_sayori_2.png", 0.6, _("Второстепенное главное меню"), _("Художники -- RockMedved, FuckingMoniker_mmmmm")),
    # Чиби
    25: ("s_chibi turned", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    26: ("s_chibi hop", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Предметы
    27: ("sayori turned happ lup poem_paper", 0.68, _("Предмет в руке -- стих"), _("{vspace=465}Сделано на основе свободного изображения")),
    28: ("sayori turned windbreaker happ lup umbrella", 0.68, _("Зонт"), _("{vspace=465}Сделано на основе изображения от tohamina на сайте {a=https://ru.freepik.com/free-psd/umbrella-isolated-on-transparent-background_82627223.htm#query=transparent%20umbrella&position=16&from_view=keyword&track=ais&uuid=3aaff5a6-9f9a-4a61-954a-e4ca83ed7042}ru.freepik.com{/a} (Freepik)")),
    # Аватарка в мессенджере
    29: ("phone/assets/icons/s.png", 0.6, _("Аватарка в мессенджере"), _("Автор (не художник) -- Elckarow#8399 (Discord, старый ник)"))
    },
    cut = 80
    )


    char_y = CharactersImage(
    name = _("Юри"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#B957FF",
    name_color = _("лавандовый"),
    nationality = character_nationality_japan_female,
    hobby = _("книги, стихотворения, прослушивание музыки, «спокойный» отдых"),
    status = _("ученица, участница Литературного клуба"),
    description = _("""\
Элегантность могла бы стать вторым именем Юри, если бы не её скрытость и скованность. Сперва эту девушку вообще можно не заметить, но если \
Вы попытаетесь познать её внутренний мир, то готовьтесь погрузиться в него с головой: Юри за всю свою жизнь впитала в себя много книг, смешав \
всё с богатым воображением. Но погружение будет очень вялым и инертным, ведь Юри тяжело раскрываться и рассказывать про свои увлечения даже \ \
близким людям. Так же, как и в случае с Нацуки, на неё повлияли негативные факторы: смерть отца в авиакатострофе, отсутствие друзей и множество \
мелких проблем. Её каждый день терзают переживания по поводу отца в той или иной степени, накапливающиеся в один большой пузырь, из-за чего \
провоцируется прозванное Нацуки «демоническое» состояние, выраженное невероятным безумием, которое крайне трудно контролировать. Один раз, \
чтобы задавить переживания, Юри прибегла даже к порезам рук, правда, они ей помогли только в краткосрочной перспективе. Её проблема стала ещё \
одной головной болью Макса, в которого она, как и Моника, влюбилась по уши, что усугубило всё ещё сильнее. Главное для Юри -- найти человека, \
который примет её чувства и избавит от всех переживаний. Но найдётся ли такой человек?
    """),
    sprites = {
    # Школьная форма
    1: ("yuri turned happ", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    2: ("yuri turned happ lup rup", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    3: ("yuri shy happ", 0.68, _("Школьная форма (застенчивая поза)"), _("Художник -- Satchely из Team Salvato")),
    4: ("yuri turned neut e1d rcutdown", 0.68, _("Школьная форма (порезанная рука, опущенная вниз)"), _("Художник -- Phathom#9806 (Discord, старый ник)")),
    5: ("yuri turned neut e1d rcut", 0.68, _("Школьная форма (порезанная рука, поднятая вверх)"), _("Обновлённая версия -- Blue Quacker (Reddit)")),
    6: ("yuri turned happ rbandages", 0.68, _("Школьная форма (забинтованная рука, поднятая вверх)"), _("Художник -- Yagamirai10 (Reddit)")),
    # Свитер
    7: ("yuri turned casual happ", 0.68, _("Свитер (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    8: ("yuri turned casual happ lup rup", 0.68, _("Свитер (обычная поза)"), _("Художник -- Satchely из Team Salvato")),
    9: ("yuri shy casual happ", 0.68, _("Свитер (застенчивая поза)"), _("Художник -- Satchely из Team Salvato")),
    # Сарафан
    10: ("yuri turned sundress happ", 0.68, _("Сарафан (обычная поза)"), _("Художники -- BlackRabbitArtworks (Reddit), Zachman Awesomeness")),
    11: ("yuri turned sundress happ lup rup", 0.68, _("Сарафан (обычная поза)"), _("Художники -- BlackRabbitArtworks (Reddit), Zachman Awesomeness")),
    12: ("yuri shy sundress happ", 0.68, _("Сарафан (застенчивая поза)"), _("Художники -- BlackRabbitArtworks (Reddit), Zachman Awesomeness")),
    # Ветровка
    13: ("yuri turned windbreaker happ", 0.68, _("Ветровка"), _("Художник -- gurogurl (Reddit)")),
    14: ("yuri turned windbreaker happ lup rup", 0.68, _("Ветровка"), _("Художник -- gurogurl (Reddit)")),
    # Свобоная спортивная одежда
    15: ("yuri turned sport_casual happ", 0.68, _("Свобоная спортивная одежда (обычная поза)"), _("Художник -- IanSuller_Blogger")),
    16: ("yuri turned sport_casual happ lup rup", 0.68, _("Свобоная спортивная одежда (обычная поза)"), _("Художник -- IanSuller_Blogger")),
    17: ("yuri shy sport_casual happ", 0.68, _("Свобоная спортивная одежда (застенчивая поза)"), _("Художник -- IanSuller_Blogger")),
    # Тело
    18: ("yuri turned body happ", 0.68, _("Тело"), _("Художник -- Ari#5636 (Discord, старый ник)\nРедактирование -- KitsuruDev")), # перетащить в проекцию ГГ в будущем (более сексуализировано, т.к. проекция)
    19: ("yuri turned body happ hup", 0.68, _("Тело"), _("Художник -- Ari#5636 (Discord, старый ник)\nРедактирование -- KitsuruDev")), # перетащить в проекцию ГГ в будущем
    # Меню
    20: ("mod_assets/sprites/characters/yuri/menu/art_yuri_0.png", 0.55, _("Основное главное меню"), _("Художники -- RockMedved, FuckingMoniker_mmmmm")),
    21: ("gui/menu_art_y.png", 0.55, _("Второстепенное главное меню"), _("Художник -- Satchely из Team Salvato")),
    # Чиби
    22: ("y_chibi turned", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    23: ("y_chibi hop", 1.0, _("Чиби"), _("Художник -- Satchely из Team Salvato\nУлучшенная версия -- Mouhantain (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Предметы
    24: ("yuri turned happ lup_item poem_paper", 0.68, _("Предмет в руке -- стих"), _("{vspace=465}Сделано на основе свободного изображения")),
    25: ("yuri turned happ lup_item knife", 0.68, _("Нож"), _("Художник -- Satchely из Team Salvato, Phathom#9806 (Discord, старый ник)")), # перетащить в проекцию ГГ в будущем
    26: ("yuri turned casual happ lup_item umbrella", 0.68, _("Зонт"), _("{vspace=465}Сделано на основе изображения от\ntohamina на сайте {a=https://ru.freepik.com/free-psd/umbrella-isolated-on-transparent-background_82627233.htm#query=transparent%20umbrella&position=8&from_view=keyword&track=ais&uuid=3aaff5a6-9f9a-4a61-954a-e4ca83ed7042}ru.freepik.com{/a} (Freepik)")),
    # Аватарка в мессенджере
    27: ("phone/assets/icons/y.png", 0.6, _("Аватарка в мессенджере"), _("Автор (не художник) -- Elckarow#8399 (Discord, старый ник)"))
    }
    )


    ##################### Второстепенные персонажи #####################

    char_kam = CharactersImage(
    name = _("Камуко"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#856655",
    name_color = _("кофейный"),
    nationality = character_nationality_japan_female,
    hobby = _("общение с людьми, аниме, видеоигры, представители кошачьих"),
    status = _("ученица, участница Клуба выпечки"),
    description = _("""\
Что выйдет, если скрестить увлечение аниме, компьютерные игры и кучу энергии? Правильно -- гиперактивное чудовище. Камуко нереально болтливая \
девушка, но в одиночестве, вопреки своему характеру, её состояние более чем спокойное, хоть и сопряжено позитивными «выпадами». Камуко неглупа, \
как может показаться: она способна делать верные шаги по достижению своих целей. Изюминкой в её внешности является ободок на голове с брошью в \
форме мордочки кота. Почему кот? Потому что она помешана на кошачьих, причём настолько, что, по её рассказам, у неё дома есть ободок и игровые \
наушники с кошачьими ушами, но только ничто из этого никто ещё не видел. Не исключено, что это одна из занимательных историй, которые Камуко \
любит травить в кругу друзей, особенно в Клубе выпечки, куда она вступила из небогатого выбора. Основной её задачей было нахождение друзей для \
весёлого времяпрепровождения, а остальное ей было не так уж важно. Разношёрстный состав Выпечки, за исключением президента, ей очень \
приглянулся, потому она там и осела. Но на горизонте замаячил Литературный клуб, который может справиться с её потребностью лучше Выпечки. И \
Камуко уже морально приготовилась вступить туда. Только сначала надо приноровиться писать стихи.
    """),
    sprites = {
    ### НЕ ВСЕ ОБОДКИ -- ДОБАВИТЬ В БУДУШЕМ
    # Школьная форма
    1: ("kamuko turned happ headband_cat", 0.68, _("Школьная форма"), _("Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)\nПак спрайтов -- silver")),
    2: ("kamuko turned happ headband_cat lup rup", 0.68, _("Школьная форма"), _("Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)")),
    3: ("kamuko turned happ headband_cat lhid rhid", 0.68, _("Школьная форма"), _("Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)")),
    4: ("kamuko turned happ headband_cat lhiphid rface", 0.68, _("Школьная форма"), _("Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)")),
    ## Домашняя одежда
    # 5: ("kamuko turned casual happ", 0.68, "Школьная форма", "Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)"),
    # 6: ("kamuko turned casual happ lup rup", 0.68, "Школьная форма", "Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)"),
    # 7: ("kamuko turned casual happ lhid rhid", 0.68, "Школьная форма", "Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)"),
    # 8: ("kamuko turned casual happ lhiphid rface", 0.68, "Школьная форма", "Художник -- ChyChy\nРедактирование (доп. элементы) -- Blue Quacker (Reddit)"),
    # Меню
    5: ("mod_assets/sprites/characters/kamuko/menu/art_kamuko_10.png", 0.33, _("Второстепенное главное меню"), _("Художник -- ChyChy")),
    # Аватарка в мессенджере
    6: ("phone/assets/icons/kam.png", 0.6, _("Аватарка в мессенджере"), _("Художник -- ChyChy"))
    },
    cut = 100
    )


    char_k = CharactersImage(
    name = _("Котоноха"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#DDA0DD",
    name_color = _("сиреневый"),
    nationality = character_nationality_japan_female,
    hobby = _("природа, «спокойный» отдых, общение с друзьями"),
    status = _("ученица, участница Литературного клуба"),
    description = _("""\
Про Котоноху и сказать особо нечего: её жизнь довольно спокойная, как и её характер. Она старается не досаждать людям и всегда старается \
обеспечить им комфорт в разговоре, при этом Котоноха может выслушать проблемы и дать ободряющий совет. В средней школе она подружилась с Юри, \
Нацуки и Либитиной, с которыми проводит много времени. Первые две хотели затянуть её в Литературный клуб, но из-за стеснения каждый раз она \
мягко отказывалась от их предложений. Когда же клуб стал набирать обороты, а в траектории учебного плана остался последний год, Котоноха решила \
откинуть свои колебания в сторону и стать его частью, чтобы познать клубную деятельность в полной мере. Что он ей даст в будущем? Время покажет.
    """),
    sprites = {
    # Школьная форма
    1: ("kotonoha happ", 0.68, _("Школьная форма"), _("Художник -- Cyrke (Reddit)\nРелиз персонажа -- Danko\nПост на Реддите со спрайтами -- NathanL3 (Reddit)")),
    2: ("kotonoha happ lup rhid", 0.68, _("Школьная форма"), _("Художник -- Cyrke (Reddit)")),
    3: ("kotonoha happ lself rhip", 0.68, _("Школьная форма"), _("Художник -- Cyrke (Reddit)")),
    # Сарафан
    4: ("kotonoha casual happ", 0.68, _("Сарафан"), _("Художник -- Laure15")),
    5: ("kotonoha casual happ lup rhid", 0.68, _("Сарафан"), _("Художник -- Laure15")),
    6: ("kotonoha casual happ lself rhip", 0.68, _("Сарафан"), _("Художник -- Laure15")),
    ## Свободный купальник
    # 1: ("kotonoha swimsuit happ", 0.68, "Свободный купальник", "Художник -- Laure15"),
    # 1: ("kotonoha swimsuit happ lup rhid", 0.68, "Свободный купальник", "Художник -- Laure15"),
    # 1: ("kotonoha swimsuit happ lself rhip", 0.68, "Свободный купальник", "Художник -- Laure15"),
    # Чиби
    7: ("k_chibi turned", 1.0, _("Чиби"), _("Художник -- SlightlySimple (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    8: ("k_chibi hop", 1.0, _("Чиби"), _("Художник -- SlightlySimple (Reddit)\nРедактирование (контур) -- KitsuruDev")),
    # Аватарка в мессенджере
    9: ("phone/assets/icons/k.png", 0.6, _("Аватарка в мессенджере"), _("{vspace=465}Сделано на основе изображения от\nИИ на сайте {a=https://ru.freepik.com/free-photo/beautiful-flowers-with-water-drops_60047110.htm#query=purple%20blossoms&position=0&from_view=keyword&track=ais_hybrid&uuid=4386b4ae-b298-4ff6-8498-4b04257c3823}ru.freepik.com{/a} (Freepik)"))
    }
    )


    char_koh = CharactersImage(
    name = _("Кохаку"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#ffbf00",
    name_color = _("янтарный"),
    nationality = character_nationality_japan_female,
    hobby = _("кухня"),
    status = _("ученица, президент Клуба выпечки"),
    description = _("""\
\"Я злой злюка с планеты Зло, и сегодня меня ударили по яйцам\", -- такой девиз мог быть у Кохаку, если бы она была парнем и проявляла \
агрессию каждую секунду. Злость, циничность, эгоистичность -- лишь основные черты её характера. Каким образом она встала у руля целого клуба? \
До президентства Кохаку была добрее, и катализатором её негатива послужила средняя школа с бунтарским поведением и гормонами, а также родители. \
И нет, с ними она общается, но они её не ценят, как это выяснилось во время разбирательства Рэйко в конфликте между Литературным клубом и \
Клубом выпечки. В качестве решения своей проблемы Кохаку выбрала кондитерство. Тем не менее, она стала президентом Клуба выпечки, где начала \
отыгрываться на всех, кто шёл против неё. Как итог, из десятка человек остались буквально единицы, приход всего лишь парочки новых участников и \
статус «плохого» клуба. Приоритетной целью Кохаку являются кексы Нацуки, которые могут дать ей и Выпечке новое дыхание, немного обелив \
репутацию. И, вероятнее всего, в погоне за ними она просто свалится в яму, из которой не выберется без посторонней помощи, на которую уже давно \
не верит из-за больного опыта доверия к окружающим.
    """),
    sprites = {
    # Школьная форма
    1: ("kohaku turned angr m1e", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)\nПак спрайтов -- iitzwolfyy_ (Discord)\n{vspace=240}Изначальное \"имя\" персонажа -- Fem. MC Switcheroo\n\nПерсонаж взят из мода Doki Doki Switcheroo")),
    2: ("kohaku turned angr m1e lup rup", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)")),
    3: ("kohaku cross angr m1e", 0.68, _("Школьная форма (поза со скрещенными руками)"), _("Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)")),
    ## Майка
    # 4: ("kohaku turned casual angr m1e", 0.68, "Майка (обычная поза)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)"),
    # 5: ("kohaku turned casual angr m1e lup", 0.68, "Майка (обычная поза)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)"),
    # 6: ("kohaku cross casual angr m1e", 0.68, "Майка (поза со скрещенными руками)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)")
    ## Сарафан
    # 7: ("kohaku turned sundress angr m1e", 0.68, "Сарафан (обычная поза)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)"),
    # 8: ("kohaku turned sundress angr m1e lup", 0.68, "Сарафан (обычная поза)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)"),
    # 9: ("kohaku cross sundress angr m1e", 0.68, "Сарафан (поза со скрещенными руками)", "Художник -- MWRoach (Reddit)\nОплата работы -- BlackRabbitArtworks (Reddit)")
    },
    cut = 60
    )


    char_l = CharactersImage(
    name = _("Либитина"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#ffedff",
    name_color = _("снежный"),
    nationality = character_nationality_japan_female + "/" + character_nationality_uk_female,
    hobby = _("«спокойный» отдых, мифология"),
    status = _("ученица"),
    description = _("""\
Либитина одна из тех самых чрезмерно умных людей, набирающих практически высший балл по всем предметам. \"Как у неё так получается?\", \"У неё \
есть личная жизнь?\", \"Она вообще человек?\" -- эти вопросы так и останутся без ответа, хотя даже если бы они и были, то что бы они дали? \
Либитина наполовину является англичанкой, вот только в Англии она провела лишь раннее детство, так что японская сторона в ней сильно доминирует. \
По характеру она тихая, любит пошутить, чтобы разбавить обстановку (а ещё для этого постоянно улыбается, что вызывает, скорее, паническое \
напряжение, чем расслабление), и умеет подстраиваться под собеседника. Так вышло, что в средней школе она подружилась с Котонохой, часто проводя \
с ней время («виной» тому схожие характеры, внешность и интересы), а уже через неё позже стала общаться с Юри и Нацуки. Но в Либитине есть \
«изюминка», которая не по душе Котонохи, -- это увлечение мифологией разных народов. Что уж говорить, если её имя есть также у древнеримской \
богини, заведующей погребальными обрядами? В любом случае с Либитиной никогда не заскучаешь.
    """),
    sprites = {
    # Школьная форма
    1: ("libitina forward happ", 0.68, _("Школьная форма (обычная поза)"), _("Художники и оплата работы -- bronya_rand (GanstaKingofSA (Reddit)), отец bronya_rand, Cyrke (Reddit)\n{vspace=180}Первоначально персонаж был сделан для мода \"Doki Doki Literature Club: The True Reality\" за авторством bronya_rand (GanstaKingofSA (Reddit))\n\n{a=https://drive.google.com/drive/folders/1tA2ssy3Tn8w2JdvVbZPjxee4_e-bWKl6}Ссылка на гугл-диск{/a} со спрайтами и лецензией на использование")),
    2: ("libitina shy happ", 0.68, _("Школьная форма (поза c наклонённой головой)"), _("Художники и оплата работы -- bronya_rand (GanstaKingofSA (Reddit)), отец bronya_rand, Cyrke (Reddit)"))
    ## Регалия
    # 1: ("libitina forward regalia happ", 0.68, "Регалия (поза c наклонённой головой)", "Художник -- Storm Blaze (Reddit)\nОплата работы -- Retronika\nИдея одежды -- bronya_rand (GanstaKingofSA (Reddit))"),
    # 1: ("libitina shy regalia happ", 0.68, "Регалия (поза c наклонённой головой)", "Художник -- Storm Blaze (Reddit)\nОплата работы -- Retronika\nИдея одежды -- bronya_rand (GanstaKingofSA (Reddit))"),
    ## Предметы
    # 1: ("libitina shy happ knife", 0.68, "Нож", "Художники и оплата работы -- bronya_rand (GanstaKingofSA (Reddit)), отец bronya_rand, Cyrke (Reddit)")
    },
    cut = 100
    )


    char_r = CharactersImage(
    name = _("Рэйко"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#745eff",
    name_color = _("светло-сапфирный"),
    nationality = character_nationality_japan_female,
    hobby = _("лидерство"),
    status = _("ученица, глава Школьного совета, старшая сестра Соры"),
    description = _("""\
Гроза всех учеников, меч правосудия, заноза в заднице нарушителей -- называйте Рэйко, как хотите, но вы абсолютно точно будете уважать её \
лидерские качества и способности. Она настолько сильно вжилась в роль руководителя, что иногда получает лёгкие насмешки со стороны учителей. \
Казалось бы, строгость -- её второе имя, но Рэйко всегда руководствуется логикой и анализом, поэтому, когда ей попадается нетривиальный случай, \
она старается принять адекватное и справедливое решение, которое если и выходит за рамки правил, то немного (ловля Нацуки за беготню -- \
показательный пример). Во время существования Дискуссионного клуба она узнала от его президента про Монику и позже с ней подружилась. Когда клуб \
распался, Рэйко взяла себе президента и вице-президента в качестве помощников с их согласия. Она также хотела взять и Монику, но та отказалась, \
поскольку хотела создать собственный клуб. Рэйко является старшей сестрой Соры (разница в возрасте составляет всего лишь 1 год), хотя наедине с \
ним ведёт себя как младшая (но без капризов), поэтому всеми домашними делами преимущественно заправляет её брат. Больше про Рэйко нечего сказать: \
своё место она нашла -- в мире точно не пропадёт.
    """),
    sprites = {
    # Форма Школьного совета
    1: ("reiko turned uniform_council", 0.68, _("Форма Школьного совета (обычная поза)"), _("Художники и пак спрайтов -- Retronika, Storm Blaze (Reddit)")),
    2: ("reiko turned uniform_council lpoint rup", 0.68, _("Форма Школьного совета (обычная поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    3: ("reiko turned uniform_council lhip rthink", 0.68, _("Форма Школьного совета (обычная поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    # 1: ("reiko turned uniform_council shy", 0.68, "Форма Школьного совета (застенчивая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    4: ("reiko tough uniform_council neut_cm_oe", 0.68, _("Форма Школьного совета (наклонённая поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    ## Школьная форма
    # 1: ("reiko turned", 0.68, "Школьная форма (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned lpoint rup", 0.68, "Школьная форма (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned lhip rthink", 0.68, "Школьная форма (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned shy", 0.68, "Школьная форма (застенчивая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned tough", 0.68, "Школьная форма (наклонённая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    ## Кофта
    # 1: ("reiko turned casual", 0.68, "Кофта (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned casual lpoint rup", 0.68, "Кофта (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned casual lhip rthink", 0.68, "Кофта (обычная поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned casual shy", 0.68, "Кофта (застенчивая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # 1: ("reiko turned casual tough", 0.68, "Кофта (наклонённая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    # Майка
    5: ("reiko turned vest", 0.68, _("Майка (обычная поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    6: ("reiko turned vest lpoint rup", 0.68, _("Майка (обычная поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    7: ("reiko turned vest lhip rthink", 0.68, _("Майка (обычная поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)")),
    # 1: ("reiko turned vest shy", 0.68, "Майка (застенчивая поза)", "Художники -- Retronika, Storm Blaze (Reddit)"),
    8: ("reiko tough vest neut_cm_oe", 0.68, _("Майка (наклонённая поза)"), _("Художники -- Retronika, Storm Blaze (Reddit)"))
    },
    cut = 100
    )


    char_sor = CharactersImage(
    name = _("Сора"),
    age = f"17 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#1e43fc",
    name_color = _("сапфирный"),
    nationality = character_nationality_japan_male,
    hobby = _("«спокойный» отдых"),
    status = _("ученик, участник Клуба выпечки, младший брат Рэйко"),
    description = _("""\
Что вы хотите узнать об обычном ученике старшей школы? У Соры нет ничего сверхособенного за исключением родственной связи с Рэйко -- главы \
Школьного совета, что, на самом деле, особо ничего не меняет. Спокойный характер, хорошие оценки в учёбе, успешное ведение дел по дому и забота \
о старшей сестре, когда она наедине с ним -- вот и все мазки образа Соры без лишних примесей. Поскольку он эктоморф (худой человек, плохо \
набирающий вес), он часто замерзает в прохладную погоду, особенно в помещениях со сквозняками, поэтому Соре разрешается носить кофту под \
школьной формой, чтобы сохранять тепло. Почему его занесло в Клуб выпечки? А это часть плана Рэйко по образумеванию президента Кохаку. Сора \
должен был аккуратно на неё повлиять, чтобы она сбавила свои негативные обороты и взялась за голову, но это пока не дало какие-либо плоды, да и \
вряд ли даст, поскольку Кохаку крепко впряглась за свою идею фикс. А раз это занятие безрезультатное, то и нет смысла находится в данном клубе. \
Поэтому после ухода, который является лишь вопросом времени, Сора вернётся в прежнюю колею своей спокойной жизни. Или же вкус клубной жизни \
поменяет его взгляд на внеучебную деятельность?
    """),
    sprites = {
    # Школьная форма
    1: ("sora turned", 0.68, _("Школьная форма (обычная поза)"), _("Художники -- Hayashi_Takahashi (Reddit), ThoseDamnShinyPants (Reddit)\nРедактирование (глаза) -- Endlessneagi (Reddit)\nПак спрайтов -- Elckarow#8399 (Discord, старый ник){vspace=235}Персонаж сделан на основе спрайтов главного героя от Childish-N (Deviant Art)")),
    2: ("sora turned lup rpock", 0.68, _("Школьная форма (обычная поза)"), _("Художники -- Hayashi_Takahashi (Reddit), ThoseDamnShinyPants (Reddit)")),
    3: ("sora turned lface rpock", 0.68, _("Школьная форма (обычная поза)"), _("Художники -- Hayashi_Takahashi (Reddit), ThoseDamnShinyPants (Reddit)")),
    4: ("sora cross", 0.68, _("Школьная форма (поза со скрещенными руками)"), _("Художники -- Hayashi_Takahashi (Reddit), ThoseDamnShinyPants (Reddit)")),
    # Чёрная толстовка
    5: ("sora turned casual", 0.68, _("Чёрная толстовка (обычная поза)"), _("Художники -- ThoMysteriousY (Reddit)")),
    6: ("sora turned casual lup rpock", 0.68, _("Чёрная толстовка (обычная поза)"), _("Художники -- ThoMysteriousY (Reddit)")),
    7: ("sora turned casual lface rpock", 0.68, _("Чёрная толстовка (обычная поза)"), _("Художники -- ThoMysteriousY (Reddit)")),
    8: ("sora cross casual", 0.68, _("Чёрная толстовка (поза со скрещенными руками)"), _("Художники -- ThoMysteriousY (Reddit)")),
    # Меню
    9: ("mod_assets/sprites/characters/sora/menu/art_sora_10.png", 0.40, _("Второстепенное главное меню"), _("Художники -- Hayashi_Takahashi (Reddit)"))
    }
    )


    char_f = CharactersImage(
    name = _("Фуккацуми"),
    age = f"17 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#14fa70",
    name_color = _("салатовый"),
    nationality = character_nationality_japan_female + "/" + character_nationality_russia_female,
    hobby = _("струнные щипковые инструменты (гитары)"),
    status = _("ученица, участница Клуба выпечки"),
    description = _("""\
Если уж кто и может переплюнуть Макса в «нетипичности», то это только Фуккацуми. Будучи дочерью русского отца и японской матери она провела \
часть своего детства в сердце России -- в Москве (где жил её отец до полного переезда) и её области (где живут бабушка и дедушка по отцовской \
линии). Поездки туда совершались в периоды лета, а когда началась учёба, то и вовсе прекратились. Впрочем Фукка за пределами родного дома \
чувствует себя не в своей тарелке. Но, несмотря на это, к ней мягко относятся: даже за всё обучение в школе её досаждали лишь пару раз, да и то \
в мягкой и шутливой форме. Здесь важно отметить две вещи. Первая: Фуккацуми -- застенчивая социопатка с высокой тревожностью при социальном \
контакте. Вторая: одноклассница Кохаку, которая что-то в ней нашла, но что -- никто не может сказать. Она всегда защищает Фукку, а также \
заботится о ней, если есть такая возможность. И именно из-за неё Фуккацуми оказалась в Клубе выпечки после развала Музыкального, в котором \
раньше практиковалась на гитаре, поскольку в этом деле у неё лежит душа. Главный парадокс Фукки в том, что любовь к гитарам может помочь ей с \
«застенчивой скорлупой», но всё время уходит на Клуб выпечки. Сможет ли кто-то разорвать этот порочный круг?
    """),
    sprites = {
    # Школьная форма
    1: ("fukkacumi turned", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)\nПак спрайтов -- Cleb#4559 (Discord, старый ник){vspace=190}Изначальное имя персонажа -- Настя, которое сохранено и адаптировано в данном моде")),
    2: ("fukkacumi turned lfist rfist", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)")),
    # 3: ("fukkacumi turned lhip rhip", 0.68, "Школьная форма (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 4: ("fukkacumi cross", 0.68, "Школьная форма (поза со скрещенными руками)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    3: ("fukkacumi cross grab", 0.68, _("Школьная форма (поза с удерживаемой рукой)"), _("Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)")),
    ## Свитер
    # 6: ("fukkacumi turned casual", 0.68, "Свитер (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 7: ("fukkacumi turned casual lfist rfist", 0.68, "Свитер (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 8: ("fukkacumi turned casual lhip rhip", 0.68, "Свитер (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 9: ("fukkacumi cross casual", 0.68, "Свитер (поза со скрещенными руками)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 10: ("fukkacumi cross casual grab", 0.68, "Свитер (поза с удерживаемой рукой)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    ## Пальто
    # 11: ("fukkacumi turned coat", 0.68, "Пальто (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 12: ("fukkacumi turned coat lfist rfist", 0.68, "Пальто (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 13: ("fukkacumi turned coat lhip rhip", 0.68, "Пальто (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 14: ("fukkacumi cross coat", 0.68, "Пальто (поза со скрещенными руками)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 15: ("fukkacumi cross coat grab", 0.68, "Пальто (поза с удерживаемой рукой)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    ## Пижама
    # 16: ("fukkacumi turned pajamas", 0.68, "Пижама (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 17: ("fukkacumi turned pajamas lfist rfist", 0.68, "Пижама (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 18: ("fukkacumi turned pajamas lhip rhip", 0.68, "Пижама (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 19: ("fukkacumi cross pajamas", 0.68, "Пижама (поза со скрещенными руками)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 20: ("fukkacumi cross pajamas grab", 0.68, "Пижама (поза с удерживаемой рукой)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    ## Свободный купальник
    # 21: ("fukkacumi turned swimsuit", 0.68, "Свободный купальник (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 22: ("fukkacumi turned swimsuit lfist rfist", 0.68, "Свободный купальник (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 23: ("fukkacumi turned swimsuit lhip rhip", 0.68, "Свободный купальник (обычная поза)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 24: ("fukkacumi cross swimsuit", 0.68, "Свободный купальник (поза со скрещенными руками)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # 25: ("fukkacumi cross swimsuit grab", 0.68, "Свободный купальник (поза с удерживаемой рукой)", "Художник -- Spirtowochka\nРедактирование (волосы) -- Blue Quacker (Reddit)\nАвтор -- NekoLaiS#8541 (Discord, старый ник)"),
    # Эмоции
    4: ("fukkacumi turned bcm boe", 0.68, _("Тревожность"), _("Редактирование (глаза) -- KitsuruDev")),
    5: ("fukkacumi turned bom boe", 0.68, _("Тревожность"), _("Редактирование (глаза) -- KitsuruDev"))
    },
    cut = 70
    )


    char_h = CharactersImage(
    name = _("Хироши"),
    age = f"17 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#966F33",
    name_color = _("древесный"),
    nationality = character_nationality_japan_male,
    hobby = _("манга, математические науки"),
    status = _("ученик, президент Математического клуба"),
    description = _("""\
Хироши очень двойственный человек: на людях он старается быть спокойным, рассудительным и готовым выслушать собеседника, но, когда дело доходит \
до более близкого взаимодействия, он становится более напористым и грубым, хотя и старается в себе это контролировать. В средней школе Хироши \
подружился с Нацуки, однако из-за известной только им причины она его сильно возненавидела, однако Хироши из-за своей влюблённости не собирался \
разрывать с ней контакт. По сей день он предпринимает попытки наладить дружбу, в том числе и приглашением в собственный Математический клуб, но \
Нацуки всячески их отвергает. Один раз Хироши доканал Нацуки и она пожаловалась на него Рэйко, что помогло сбавить градус его напористости, но \
не закрыло ситуацию. К чему это приведёт в будущем? Никому неизвестно. Однако сталкерство Хироши явно не прекратится без постороннего \
вмешательства, которое «обеспечит» ему серьёзные последствия.
    """),
    sprites = {
    # Школьная форма
    1: ("hiroshi neut", 0.68, _("Школьная форма"), _("Художник -- Blue Quacker (Reddit) (Discord: bluequacker)\nПак спрайтов -- iiTzWolfyy (Discord: iitzwolfyytherenewal){vspace=130}Изначальное \"имя\" персонажа -- Wallace\n\nПак спрайтов \"Wallace Reborn Spritepack\" является переделкой старых спрайтов персонажа, которые были сделаны на основе спрайтов {a=https://childish-n.deviantart.com/art/DDLC-Protagonist-Sprite-715239172}MC v1{/a} за авторством Childish-N (Deviant Art)")),
    2: ("hiroshi neut lhip rhip", 0.68, _("Школьная форма"), _("Художник -- Blue Quacker (Reddit) (Discord: bluequacker)")),
    # Форма Школьного совета
    # 1: ("hiroshi uniform_council neut", 0.68, _("Форма Школьного совета"), _("Художник -- Blue Quacker (Reddit) (Discord: bluequacker)")),
    # 1: ("hiroshi uniform_council neut lhip rhip", 0.68, _("Форма Школьного совета"), _("Художник -- Blue Quacker (Reddit) (Discord: bluequacker)")),
    # Голова
    3: ("hiroshi fc neut", 0.68, _("Голова (анфас)"), _("Художник -- Blue Quacker (Reddit) (Discord: bluequacker)"))
    },
    cut = 70
    )


    char_e = CharactersImage(
    name = _("Эми"),
    age = f"18 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#ede61a",
    name_color = _("солнечный"),
    nationality = character_nationality_japan_female,
    hobby = _("кухня"),
    status = _("ученица, участница Клуба выпечки"),
    description = _("""\
Эми -- образцовая участница Клуба выпечки, поскольку умеет хорошо готовить и постоянно практикуется в этом деле. Вот только лишь на ней \
держится вся деятельность клуба: остальные участники практически не смыслят в готовке. Что касается самой Эми, то она уравновешенная девушка, \
которая может пускать ситуативные шутки. В прошлом часто общалась с Нацуки, когда она состояла в Клубе выпечки, но после её ухода Эми стала \
редко с ней пересекаться, из-за чего всё общение сошло на нет. В некоторой степени ей обидно за такой расклад событий, но её общий настрой \
остался прежним. И всё в жизни Эми было бы хорошо, но Клуб выпечки во главе с Кохаку вошёл в кризис. Он начал планомерно «скатываться вниз»: \
потеря старых участников, минимальное желание готовить у новых, а также отсутствие совместной работы со всеми членами клуба. Эми была бы не \
прочь сместить Кохаку, но остальным как-то на это побоку, а в одиночку она ничего не сможет сделать. Иными словами, она может лишиться \
«кулинарного полигона», ведь, когда клуб развалится, его финансовое поддержание прекратится. Эми прекрасно это осознаёт, но старается жить \
сегодняшним днём. Не лучший вариант решения проблемы, но других пока что нет. Хотя кто знает, что будет завтра?
    """),
    sprites = {
    # Школьная форма
    1: ("emi turned happ", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)\nПост на Реддите со спрайтами -- Blue Quacker (BlueGodXD (Reddit)\n{vspace=230}Изначальное \"имя\" персонажа -- Blonde FeMC")),
    2: ("emi turned happ lhip rhip", 0.68, _("Школьная форма (обычная поза)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)")),
    # 3: ("emi turned happ lup rhip", 0.68, "Школьная форма (обычная поза)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    3: ("emi cross happ", 0.68, _("Школьная форма (поза со скрещенными руками)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)")),
    # Школьная форма c завязанным пиджаком
    4: ("emi turned uniform_waist_jacket happ", 0.68, _("Школьная форма c завязанным пиджаком (обычная поза)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)")),
    5: ("emi turned uniform_waist_jacket happ lhip rhip", 0.68, _("Школьная форма c завязанным пиджаком (обычная поза)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)")),
    # 7: ("emi turned uniform_waist_jacket happ lup rhip", 0.68, "Школьная форма c завязанным пиджаком (обычная поза)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    6: ("emi cross uniform_waist_jacket happ", 0.68, _("Школьная форма c завязанным пиджаком (поза со скрещенными руками)"), _("Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)")),
    ## Свободная рубашка
    # 9: ("emi turned casual happ", 0.68, "Свободная рубашка (обычная поза)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    # 10: ("emi turned casual happ lhip rhip", 0.68, "Свободная рубашка (обычная поза)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    # 11: ("emi turned casual happ lup rhip", 0.68, "Свободная рубашка (обычная поза)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    # 12: ("emi cross casual happ", 0.68, "Свободная рубашка (поза со скрещенными руками)", "Художник -- Meddy-Sin (Reddit)\nРедактирование (волосы, коррекция размера, обрезка спрайта) -- SlightlySimple (Reddit)"),
    ## Предметы
    # 13: ("emi turned happ lup_pen rhip", 0.68, "Шариковая ручка", "Художник -- Meddy-Sin (Reddit)")
    },
    cut = 70
    )


    ##################### Взрослый контингент #####################

    char_mcm = CharactersImage(
    name = _("Идзуми"),
    age = f"43 {character_gender_age_g}",
    gender = character_gender_female,
    color = "#787878",
    name_color = _("темновато-металлический"),
    nationality = character_nationality_japan_female,
    hobby = _("различные журналы, телепередачи"),
    status = _("офисный работник, домохозяйка, мать Макса"),
    description = _("""\
Идзуми является трудолюбивой женщиной, которой под силу и офисная работа, и ведение дел по дому, и воспитание собственного сына, но, конечно, \
не без помощи отца, с которым она встретилась в середине 90-ых годов на концерте группы MAX. Несмотря на высокую рабочую нагрузку, она очень \
волнительна, когда дело доходит до сына: например, его переезд из Мориоки, где проживает вся семья, в Ниигату заставил Идзуми очень переживать, \
из-за чего она сильно контролировала Макса, чтобы всё прошло так, как было запланировано. Сам Макс рад, что его родители хорошо о нём \
заботятся, но чрезмерная опека матери иногда нарушает его личные границы, что всегда приводит его в раздражение и даёт порцию переживаний за \
нервное состояние матери. Но переезд должен исправить эту ситуацию: Макс станет взрослым и самостоятельным человеком, а Идзуми не будет столь \
волнительной. По крайней мере, этот процесс неизбежен.
    """),
    sprites = {
    # Рабочий стиль
    1: ("mc_mom happ", 0.68, _("Рабочий стиль"), _("Художник -- sutemo (Itch.io)"))
    },
    cut = (200, 180, 572, 648),
    zoom_profile = 0.35
    )

    char_md = CharactersImage(
    name = _("Дэн (Дайсуке)"),
    age = f"47 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#289e0b",
    name_color = _("тёмно-изумрудный"),
    nationality = character_nationality_usa_male,
    hobby = _("работа в компании"),
    status = _("руководитель японского филиала компании Multi Orange Group, отец Моники"),
    description = _("""\
Дайсуке-сан или, если быть точным, мистер Дэн -- пример сильного и уверенного в себе человека, который смог добиться высот в карьере и \
личной жизни благодаря своей целеустремлённости и высокой силе духа. Несмотря на некоторые азиатские черты своего лица, он является коренным \
американцем: своё детство и подростковый период Дэн провёл в штате Нью-Джерси, а юношество уже в Чикаго, где обучался в Чикагском университете, \
получив оттуда море знаний в сфере бизнес-администрирования. После окончания обучения он поступил на работу в компанию Multi Orange Group, \
которая занимается разработкой IT-продуктов в сфере услуг во многих странах. Поднявшись по социальной лестнице, Дэн перевёлся по предложению \
своего начальства в японский отдел компании, где через чуть более 5 лет работы смог занять пост руководителя. В самой Японии Дэн познакомился со \
своей будущей женой Харуми, и уже через несколько лет совместной жизни у них родилась Моника, к воспитанию которой Дэн относится достаточно \
строго, потому что он хочет взрастить в ней сильные качества, которые помогут добиться ей значительных успехов в этой тяжёлой жизни. Но \
учитывает ли он желания самой Моники?
    """),
    sprites = {
    # Рабочий стиль
    1: ("monika_dad", 0.68, _("Рабочий стиль"), _("Художник -- StormBlaze76 (Reddit)\nРелиз в открытый доступ -- BassPon3 (Reddit)\n{vspace=390}Персонаж взят из мода Doki Doki Within")),
    2: ("monika_dad lup", 0.68, _("Рабочий стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    # Свободный стиль
    3: ("monika_dad casual", 0.68, _("Свободный стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    4: ("monika_dad casual lup", 0.68, _("Свободный стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    },
    cut = 50
    )


    char_mm = CharactersImage(
    name = _("Харуми"),
    age = f"44 {character_gender_age_g}",
    gender = character_gender_female,
    color = "#42ba23",
    name_color = _("темновато-изумрудный"),
    nationality = character_nationality_japan_female,
    hobby = _("природа, проведение времени со своей семьёй"),
    status = _("ландшафтный дизайнер в крупной студии, мать Моники"),
    description = _("""\
Несмотря на свой возраст, Харуми выглядит на все 25, так как всегда хорошо о себе заботится. Вероятно, именно из-за этого выбор Дайсуке пал на \
неё, хотя, конечно, уже нельзя сказать точно, но это теперь не имеет никакого значения, поскольку его брачный союз с Харуми закрепился ещё со \
времён первых свиданий, когда она ещё очно работала в ландшафтной студии, прежде чем перевестись на удалённую работу из-за нехватки времени на \
себя и свою семью. Спустя несколько лет совместной жизни у Харуми с Дайсуке родилась Моника, которая больше унаследовала черт от матери, нежели \
от отца, причём не только физических, но и психологических: добрый и мягкий характер, забота и сострадание и другие. В отличие от Дайсуке Харуми \
старается нежно воспитывать свою дочь, однако это не значит, что она позволяет ей творить что угодно -- напротив, если того требует ситуация, \
Харуми может запросто превратиться из доброго родителя в злого и строгого воспитателя, а в очень редких ситуациях её гнев способен достичь \
уровня гнева Дайсуке, что крайне пугает Монику. Но ведь это случается только в редких случаях, верно? Правда, данная «редкость» зависит либо от \
поведения самой Моники, либо от оправдания возложенных на неё ожиданий.
    """),
    sprites = {
    # Рабочий стиль
    1: ("monika_mom happ", 0.68, _("Рабочий стиль"), _("Художник -- StormBlaze76 (Reddit)\nРелиз в открытый доступ -- BassPon3 (Reddit)\n{vspace=390}Персонаж взят из мода Doki Doki Within")),
    2: ("monika_mom happ rhip", 0.68, _("Рабочий стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    3: ("monika_mom happ cross", 0.68, _("Рабочий стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    # Свободный стиль
    4: ("monika_mom happ casual", 0.68, _("Свободный стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    5: ("monika_mom happ casual rhip", 0.68, _("Свободный стиль"), _("Художник -- StormBlaze76 (Reddit)")),
    6: ("monika_mom happ casual cross", 0.68, _("Свободный стиль"), _("Художник -- StormBlaze76 (Reddit)"))
    },
    cut = 60
    )


    char_nd = CharactersImage(
    name = _("Тамоцу"),
    age = f"45 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#d91e60",
    name_color = _("тёмно-огненно-розовый"),
    nationality = character_nationality_japan_male,
    hobby = _("спиртное при большом количестве стресса"),
    status = _("отставной полицейский, корректор в небольшой юридической компании, отец Нацуки"),
    description = _("""\
В прошлом Тамоцу был сотрудником полиции Токио в районе Чиёда. В конце 90-ых он познакомился со своей женой, и в 2000 году у них уже \
родилась Нацуки. Всё было прекрасно, но в 2008 году произошёл инцидент: в квартале Акихабара было зафиксировано нападение мужчины с ножом на \
толпу гражданских. Пока преступника задерживал местный патруль, отец оказывал помощь пострадавшим. Несмотря на приезд 17 машин скорой помощи, \
часть людей скончалась на месте. Это оставило в нём глубокий отпечаток вплоть до появления ПТСР. Под страхом за жизнь своей семьи Тамоцу решил \
переселить её из мегаполиса в средний город. Жена была против, но после уговоров согласилась. Дождавшись окончания Нацуки начальной школы, он \
подал в отставку и вывез семью в Ниигату, но там доход резко упал. Попытка поступить на службу в местную полицию провалилась из-за психической \
травмы. Денег на её лечение не хватало: всё уходило на семью. Устроившись удалённо корреткором в небольшой компании, Тамоцу с трудом смог \
стабилизировать себя и ситуацию. Жена тоже нашла работу, но после очередного скандала попала в автокатастрофу, из-за чего он стал корить себя и \
налегать на спиртное. И это начинает набирать плохие обороты.
    """),
    sprites = {
    # Рабочий стиль
    1: ("natsuki_dad turned", 0.68, _("Рабочий стиль (обычная поза)"), _("Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))\nПак спрайтов -- RedLeader{vspace=310}Первоначально персонаж был сделан для мода \"Doki Doki Rewind/Replay\" за авторством Chronos (Reddit)")),
    # 1: ("natsuki_dad turned lup rup", 0.68, "Рабочий стиль (обычная поза)", "Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"))
    2: ("natsuki_dad cross", 0.68, _("Рабочий стиль (поза со скрещенными руками)"), _("Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"))
    ## Предметы
    # 1: ("natsuki_dad turned lbottle", 0.68, "Бутылка со спиртным", "Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))")
    },
    cut = 50
    )


    char_sd = CharactersImage(
    name = _("Мамору"),
    age = f"40 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#007cc9",
    name_color = _("тёмно-небесный"),
    nationality = character_nationality_japan_male,
    hobby = _("проведение времени со своей семьёй"),
    status = _("консультант в консалтинговой компании, отец Сайори"),
    description = _("""\
Мамору -- консультант в консалтинговой компании, занимающийся производственными вопросами. Клиенты (т.е. другие компании) практически всегда \
находятся за пределами Ниигаты, из-за чего Мамору постоянно приходится уезжать в командировки на пару недель. Но как только он возвращается \
домой, то с удовольствием проводит время со своей семьёй. Ведь что может быть лучше, чем уделение времени любимым людям? Мамору знает про \
проблему Сайори, как и его жена Юко. Пока они стараются уделять время своей дочери и думать, как можно её «вылечить». По крайней мере, \
знание -- уже половина победы. Осталось только достичь вторую.
    """),
    sprites = {
    # Рабочий стиль
    1: ("sayori_dad happ", 0.68, _("Рабочий стиль"), _("Художник -- StormBlazed76 (Reddit)\nРедактирование -- KitsuruDev"))
    }
    )


    char_sm = CharactersImage(
    name = _("Юко"),
    age = f"40 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#008ae0",
    name_color = _("темновато-небесный"),
    nationality = character_nationality_japan_female,
    hobby = _("книги, различные журналы"),
    status = _("домохозяйка, мать Сайори"),
    description = _("""\
Юко -- счастливый человек в счастливой семье. Внешне от своей дочери она отличается только ростом и телосложением. Постоянно пребывая \
дома, она заботится о Сайори, а также ведёт домашние дела. Когда муж Мамору приезжает домой, она старается организовывать семейные прогулки в \
разные места Ниигаты. Она с мужем в курсе проблемы Сайори, поэтому старается уделять ей время и думать, как можно её «вылечить». По крайней \
мере, знание -- уже половина победы. Осталось только достичь вторую.
    """),
    sprites = {
    # Домашняя одежда
    1: ("sayori_mom happ", 0.68, _("Домашняя одежда"), _("Художники -- latteaddicted (Reddit), SovietSpartan (Reddit) (TsukiZuramaru (Twitter))\nИдея создания персонажа -- crybaby_natsuki (Reddit)\n{vspace=170}Релиз пака спрайтов на Реддите -- latteaddicted (Reddit)\nДоп. эмоции -- Lunatic_Rabbit (Reddit), Mattyd (Reddit), LeoDeCraprio (Reddit), FuckingMoniker_mmmmm (Reddit)")),
    2: ("sayori_mom happ lpoint rhip", 0.68, _("Домашняя одежда"), _("Художник -- latteaddicted (Reddit), SovietSpartan (Reddit) (TsukiZuramaru (Twitter))")),
    3: ("sayori_mom happ lvpoint rhip", 0.68, _("Домашняя одежда"), _("Художник -- latteaddicted (Reddit), SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"))
    ## Летняя рубашка
    # 1: ("sayori_mom casual happ", 0.68, "Летняя рубашка", "Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"),
    # 1: ("sayori_mom casual happ lpoint rhip", 0.68, "Летняя рубашка", "Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"),
    # 1: ("sayori_mom casual happ lvpoint rhip", 0.68, "Летняя рубашка", "Художник -- SovietSpartan (Reddit) (TsukiZuramaru (Twitter))"),
    ## Белое платье
    # 1: ("sayori_mom sundress happ", 0.68, "Белое платье", "Художники -- leemuel01 (Reddit), EntonyEscX (Reddit)"),
    # 1: ("sayori_mom sundress happ lpoint rhip", 0.68, "Белое платье", "Художники -- leemuel01 (Reddit), EntonyEscX (Reddit)"),
    # 1: ("sayori_mom sundress happ lvpoint rhip", 0.68, "Белое платье", "Художники -- leemuel01 (Reddit), EntonyEscX (Reddit)"),
    ## Траурная одежда
    # 1: ("sayori_mom funeral happ", 0.68, "Траурная одежда", "Художник -- Lucy#4433 (Discord, старый ник)"),
    # 1: ("sayori_mom funeral happ lpoint rhip", 0.68, "Траурная одежда", "Художник -- Lucy#4433 (Discord, старый ник)")
    },
    cut = 80
    )


    char_ym = CharactersImage(
    name = _("Ари"),
    age = f"42 {character_gender_age_g}",
    gender = character_gender_female,
    color = "#8d2ed1",
    name_color = _("темновато-лавандовый"),
    nationality = character_nationality_japan_female,
    hobby = _("книги"),
    status = _("переводчик в туристической компании, мать Юри"),
    description = _("""\
Ари -- профессиональный переводчик, знающий английский и русский языки. Она является сотрудницей в туристической компании в Ниигате и в \
основном занимается переводом документов, но иногда её направляют в командировку, где необходима работа с людьми, поскольку Ари хорошо владеет \
изученными языками и сама не против лишний раз заменить бумаги на живое общение. В конце 90-ых Ари встретилась со своим мужем, фотожурналистом, \
и в начале 2000-ых годов у них родилась Юри. Однако счастье долго не продлилось: в 2015 году, возвращаясь из Филиппин, в авиакатострофе погибает \
муж. Пережив утрату, Ари не отступила от своей работы и продолжила зарабатывать деньги на жизнь Юри, но оставаясь в Ниигате, поскольку Юри \
требуется поддержка, которую никто, кроме самой Ари, дать не в состоянии. Через пару лет отношения между Россией и Японией ухудшились, спрос на \
туристические услуги в Ниигате упал, сбавив выплаты работникам в этой сфере, что и без того усугубило положение семьи Ари. Однако она не \
собирается сдаваться, потому что в её руках будущее Юри.
    """),
    sprites = {
    # Рабочий стиль
    1: ("yuri_mom happ", 0.68, _("Рабочий стиль"), _("Художник -- Iansuller_blogger\nПак спрайтов -- Retronika")),
    2: ("yuri_mom happ lup rup", 0.68, _("Рабочий стиль"), _("Художник -- Iansuller_blogger"))
    },
    cut = 80
    )


    char_um = CharactersImage(
    name = _("Мартин"),
    age = f"50 {character_gender_age_l}",
    gender = character_gender_male,
    color = "#054fa3",
    name_color = _("тёмно-синий"),
    nationality = character_nationality_usa_male,
    hobby = _("вождение, спокойный отдых"),
    status = _("личный водитель Дайсуке (отец Моники)"),
    description = _("""\
\"Дядя Мартин\" -- так окрестила его Моника в детстве, впоследствии чего такое обращение закрепилось за ним на постоянной основе. Несмотря на \
свой добрый и открытый характер, Мартин мало рассказывал про своё прошлое даже самой Монике. Будучи коренным американцем, он вырос в США, где \
познакомился и сдружился с Дайсуке ещё задолго до его брака и рождения дочери. Когда Дайсуке поднялся по карьерной лестнице, он не забыл про \
своего друга: Мартин стал его личным водителем, потому что вождение -- это его призвание, ведь когда-то в молодости он даже участвовал в местом \
автогоночном соревновании, в котором смог получить первое место, но, осознав, что такая деятельность слишком динамична для его образа жизни, \
отказался от дальнейшего участия в подобных мероприятиях. За всю свою жизнь Мартин так и не решился завести собственную семью. Да и есть ли \
теперь в этом смысл? Ведь он является неформальным членом семьи Дайсуке, часто проводя время с его дочерью, словно «родной» дядя. А если \
учесть, что у него ещё хороший заработок и приятная работая, то можно с уверенностью сказать, что жизнь Мартина точно удалась.
    """),
    sprites = {
    # Рабочий стиль
    1: ("uncle_martin happ", 0.68, _("Рабочий стиль"), _("Художник -- StormBlazed76 (Reddit)\nОплата работы -- Elenathebullimom (Reddit)\nРедактирование -- KitsuruDev"))
    },
    cut = -5
    )


    char_mi = CharactersImage(
    name = _("Ида"),
    age = f"35 {character_gender_age_l}",
    gender = character_gender_female,
    color = "#f0e0bb",
    name_color = _("ванильный"),
    nationality = character_nationality_japan_female,
    hobby = _("социология, всё связанное с романтикой"),
    status = _("учитель"),
    description = _("""\
Если у вас проблемы с мотивацией в сфере любви, то смело обращайтесь к Иде -- она быстро закапает вам все мозги, из-за чего вы из принципа \
будете достигать любовные высоты, лишь бы больше она не досаждала этой темой. Ну а если быть серьёзным, то Ида -- образцовый классный \
руководитель. Она может найти общий язык со многими учениками, а также помочь в трудную минуту. Можно сказать, что и здесь Максу повезло: хоть \
кто-то из взрослых, кроме родителей, серьёзно относится к его состоянию. Если говорить про личную жизнь, то тут можно сказать кратко: хороший \
муж, работа по душе в хорошем коллективе (что всё-таки редкость среди учебных заведений), да и в целом прекрасная жизнь. Придраться не к чему.
    """),
    sprites = {
    # Рабочий стиль
    1: ("mrs_ida happ", 0.68, _("Рабочий стиль"), _("Художники -- bruuuh#2858 (Discord, старый ник), sayuuki._ (Instagram)\nПак спрайтов -- Elckarow#8399 (Discord, старый ник){vspace=280}Первоначально персонаж был сделан для мода Club Meetings за авторством KrazyCaley#0948 (Discord, старый ник)")),
    2: ("mrs_ida happ lup rhold", 0.68, _("Рабочий стиль"), _("Художники -- bruuuh#2858 (Discord, старый ник), sayuuki._ (Instagram)"))
    ## Юката
    # 3: ("mrs_ida happ yutaka", 0.68, "Юката", "Художник -- SYwaves#7903 (Discord, старый ник)"),
    # 4: ("mrs_ida happ yutaka lup rhold", 0.68, "Юката", "Художник -- SYwaves#7903 (Discord, старый ник)")
    }
    )


    char_v = CharactersImage(
    name = _("Voires"),
    age = _("Н/Д"),
    gender = character_gender_male,
    color = "#e3e3e3",
    name_color = _("Белый"),
    nationality = character_nationality_japan_male,
    hobby = _("общение с людьми, путешествия"),
    status = _("профессиональный психолог международной компании «Щит Милосердия»"),
    description = _("""\
Voires -- психолог компании «Щит Милосердия». В первое время работы ему приходилось отправляться в международные командировки, подарившие ему \
любовь к путешествиям и общению с людьми. Однако, несмотря на свою социальность, Макс за всё время контакта с ним ничего о нём не узнал: ни \
имени, ни возраста, ни лица. Но ему точно известно, что Voires успел познакомиться в Японии со своей женой, с которой переехал в Австралию и \
обустроил там совместную счастливую жизнь, но в ущерб Максу: во время личностного кризиса он познакомился с ним на просторах Интернета, \
разговорился и тот пообещал помочь проработать его проблемы. Сначала так и было, но постепенно Voires стал обделять Макса вниманием. Масла в \
огонь подливала его работа с тогдашним другом Макса, который тоже перестал уделять внимание из-за появившихся отношений благодаря этой работе. \
Окончательно надежды Макса сгорели после долгих отсутствий Voires-а. После одного из них он разорвал связь с психологом и другом. На этом всё \
могло закончится, но внезапное ухудшение состояния Юри побудило Макса найти Voires-а из-за его бесплатной помощи и богатого опыта работы. К \
чему приведёт повторный контакт Макса с психологом, никому неизвестно. Но явно ни к чему позитивному.
    """),
    sprites = {
    # Аватарка в мессенджере
    1: ("phone/assets/icons/v.png", 0.6, _("Аватарка в мессенджере"), _("{vspace=465}Изображение на сайте {a=https://ru.freepik.com/free-ai-image/illustration-anime-character-rain_170845437.htm#fromView=search&page=5&position=25&uuid=1a31fc87-7538-4e32-8e94-1d16940f12c9&query=%D0%90%D0%BD%D0%B8%D0%BC%D0%B5+%D0%B0%D1%80%D1%82+1920x1080}ru.freepik.com{/a} (Freepik)"))
    },
    cut = (-20, -37, 400, 400)
    )




## Characters Description Screen #############################################################

screen characters():
    tag menu

    style_prefix "characters"

    use game_menu(_("Персонажи")):

        fixed:

            vpgrid id "bar_char_list":
                rows len(Characters.dict)
                cols 1

                mousewheel True
                arrowkeys True

                pos (55, -70)
                ysize 600
                spacing 5

                for name, char in Characters.dict.items():
                    vbox:
                        textbutton "[name]":
                            text_style "characters_textbutton_text"
                            xsize (179)
                            activate_sound gui.activate_sound
                            action SetVariable("Characters.current", char)

            vbar value YScrollValue("bar_char_list") pos (16, -70) ysize 600

            if Characters.current == None:
                text _("Нажмите на имя персонажа,\nчтобы увидеть его описание и спрайты"):
                    style "characters_label_text_none_characters"
            else:
                frame:
                    pos (245, -80)
                    xsize 670

                    background "character_description_background"

                    hbox:
                        ypos -32
                        spacing 313

                        label _("Описание персонажа")

                        textbutton _("Спрайты"):
                            ypos -10
                            text_style "characters_button_preview_text"
                            activate_sound gui.activate_sound
                            action [ShowMenu("preview_character", Characters.current), With(Dissolve(0.5))]

                    hbox:
                        xpos -6
                        spacing 15

                        add Characters.current.image_profile

                        text _("{b}Краткая характеристика:{/b}\n%(profile)s") % {"profile": Characters.current.profile}:
                            ypos -2
                            line_leading -5

                    vbox:
                        pos (-2, 250)
                        spacing 2

                        text _("{b}Описание:{/b}")
                        text Characters.current.description


        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
                "extra_screen_help",
                _("Помощь\nЧтобы посмотреть спрайты персонажа, нажмите на\nодноимённую кнопку в правом верхнем углу окна.\nВсе спрайты были взяты из {a=https://www.reddit.com/r/DDLCMods}группы DDLCmods на Реддит{/a}, a также\nиз двух гугл-таблиц же группы: {a=https://docs.google.com/spreadsheets/u/0/d/15wYfDrWLHLtBbijRnwER4wpEavKuYBkwlFGZARE6F4M/edit}спрайты главных героинь{/a}, {a=https://docs.google.com/spreadsheets/d/1ZDswf0CjWgxyq3m3LOxnwXXSdY5LFhqMxZwyxTFk4t8/edit?usp=sharing}список новых персонажей{/a} (в таблицах также указано авторство)."),
                ok_action = Hide("extra_screen_help"),
                chibi = "y_chibi turned magnifier",
                chibi_pos = 30
            )


image character_description_background:
    "mod_assets/elements/mod_gui/menu/character_description_background.png"
    zoom 0.825 xsize 825
    pos (-5, -40)


style characters_text is gui_text
style characters_label_text is characters_text
style characters_label_text_none_characters is characters_label_text
style characters_textbutton_text is navigation_button_text
style characters_button_preview_text is gui_text

style characters_text:
    font "mod_assets/font/menu/NAMU-Pro.ttf"
    color "#000"
    outlines []
    size 16
    line_leading -6

style characters_label_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    size 18

style characters_label_text_none_characters:
    size 25
    line_leading 0
    text_align 0.5
    align (0.87, 0.4)

style characters_textbutton_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    size 24

style characters_button_preview_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/font/menu/Vivl-rail.ttf"
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(3, "#fac", 0, 0), (2, "#fac", 2, 2)]
    size 18



## Preview Character Screen #############################################################

screen preview_character(char):
    tag menu

    style_prefix "preview_character"

    frame:
        add "menu_extra_bg"

        hbox:
            xalign 0.999 ypos 0.01

            textbutton "X":
                text_style "preview_character_textbutton_text"
                activate_sound gui.activate_sound
                action ShowMenu("characters")


        label _(char.sprites[char.current_key][2]):
            xalign 0.5 ypos 30

        vbox:
            pos (10, 150)
            xsize 430

            text char.sprites[char.current_key][3]


        hbox:
            xalign 0.5 ypos 35
            xsize 630 yfill True

            add char.image:
                align (0.5, 0.5)

        if char.count > 1:
            textbutton "<":
                text_style "preview_character_textbutton_text"
                align (0.25, 0.56)
                action Function(char.next_sprite, True)

            textbutton ">":
                text_style "preview_character_textbutton_text"
                align (0.75, 0.56)
                action Function(char.next_sprite)

    on "replaced" action With(Dissolve(0.5))


style preview_character_text is gui_text
style preview_character_label_text is navigation_button_text
style preview_character_textbutton_text is navigation_button_text

style preview_character_text:
    font "mod_assets/font/menu/BitterPro-Bold.ttf"
    color "#000"
    outlines []
    size 18

style preview_character_label_text:
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]
    size 25

style preview_character_textbutton_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    size 40
