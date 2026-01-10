define audio.t3a = "<from 13.347 loop 4.618>bgm/3.ogg"


screen punch_hiroshi_a1_d1:
    button:
        area(440, 0, 340, 340)
        mouse "punch"
        action [Play("sound", "mod_assets/sound/body/hit.mp3"), Return()]




label act_1_day_1:

    stop music fadeout 6.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 6.0

    hide black onlayer front
    scene black

    show loading_sign_mc at loading_sign_position with dissolve
    pause 0.25

    if ach_pr_d2.unlocked == False:
        $ ach_pr_d2.unlock()

    pause 7.0
    hide loading_sign_mc with dissolve
    pause 1.0

    play sound mc_alarm_clock
    show screen new_day(episode) with dissolve_scene_full
    pause 5.0
    hide screen new_day
    scene black
    with dissolve_scene_full
    play sound mc_wake_up
    pause 5.34

    call window_open
    scene bg bedroom at mc_bed
    with dissolve_scene_full
    call autosave
    mc "{cps=20}М-м-м...{/cps}"
    "{cps=20}Где мобильник?...{/cps}"
    "{cps=20}Надо посмотреть время...{/cps}"
    "{cps=20}И проверить всё остальное на всякий случай...{/cps}"
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 2,
            description = "С переездом и с началом самостоятельной жизни меня. Единственный человек не из семьи, который был рад этому событию -- это Сайори. И я могу её понять: не каждому удаётся жить рядом с надёжными друзьями."
        )

        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 3,
            description = "В этот день я впервые встретился с Моникой. Она красивая девушка, но очень странная. Почему-то решила со мной общаться после того, как я её чуть не сбил во время пробежки в парке."
        )

        current_day = (16, _("ПН"))

    python in phone.system:
        battery_level = 86
        clock = (6, 40)

    show screen phone() with Dissolve(0.5)

    if not persistent.first_phone_menu_apps:
        show hint_phone_app at hint_position onlayer front

    $ plot_pause()

    hide screen phone with Dissolve(0.5)

    if not persistent.first_phone_menu_apps:
        $ persistent.first_phone_menu_apps = True
        $ renpy.save_persistent()
        hide hint_phone_app onlayer front

    window auto
    "Ладно, всё в порядке..."
    "Кстати, не знаю зачем, но я почему-то решил оставлять памятные заметки в календаре."
    "Просто...{w}не могу объяснить."
    "Всё равно я ими никогда не пользовался, так что почему бы и нет?"

    scene bg bedroom with dissolve
    pause 0.25
    mc "{cps=25}У-у-у-ум-м-м-мф-ф-ф-ф...{/cps}"
    mc "{cps=40}Ха-а-а...{/cps}"
    "А вообще забавно, что ты просыпаешься каждый день и при этом не знаешь, изменит ли он твою жизнь навсегда."
    "Но как бы то там ни было..."
    mc "...вот оно, начало школьной рутины."
    "...да, я это заявляю спустя неделю после начала учёбы."
    "Просто я только сейчас это осознал."
    "Хм, если так подумать, то в этой школе не так уж и плохо."
    "Торжественное вступление и втягивание в учебный процесс прошли как обычно: нормально, без всяких маразматичных проблем."
    "Новое школьное общество по своей «начинке» ничем не отличается от предыдущего -- люди практически везде одинаковы, это я давно понял."
    "Снова все уважительно ко мне относятся, чему я рад."
    "По крайней мере, идиотов и выпендрёжников я не видел -- буллингом в обществе не пахнет."
    "...однако при всём этом меня практически тотально игнорируют, будто я пустое место."
    "Хотя и этому я тоже рад: никто не лезет, всем фиолетово."
    "Просто приходишь, быстренько отучиваешься, уходишь домой, делаешь домашние задания -- свободен."
    "Никаких различных обязаловок и прочих «игрищ»..."
    "..."
    "......"
    mc "Да бли-и-ин..."
    "Я же обещал подумать со вступлением в Литературный клуб..."
    "А ещё в мобильник лез, смотрел переписки с заметками, ага."
    "Вспомнить не мог..."
    "Ха, к слову, мне миссис И{image=accent_high_register}{space=-15}да, классный руководитель, уже всю плешь проела, как важно стать частью какого-нибудь клуба."
    "Однако само вступление должно совершаться исключительно по желанию самого ученика, а его у меня как раз таки нет."
    "Так что извините, миссис Ида, не в этот раз."
    "..."
    "...но не по-свински ли это прозвучало?"
    "Я не хочу обидеть ни Монику, ни Сайори."
    "В общем, молодец я, вляпался по самое не балуй."
    "..."
    "Странно, что после начала учебного года мы с Сайори прекратили бегать по утрам, -- успели сделать всего 3 вылазки."
    "Хотя она раньше и в школьное время бегала...{w}короче, не знаю, как так вышло."
    "Сайори ничего не говорила."
    "А раз так, то и не надо, я чуть не умер на той первой пробежке -- за глаза хватило."
    "..."
    "Ладно, надо уже шевелиться, а то так всё время потеряю."
    call window_close

    scene black with dissolve
    pause 0.25
    play noise_1 mc_steps_house
    pause 8.005
    stop noise_1
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    "Классический поход в туалет."
    "Ничего нового."
    "И хорошо, а то не хотелось бы принимать какие-нибудь нововведения в подобном...{w}деле."
    "..."
    "Что у меня за мысли?..."
    "Фу."
    call window_close

    pause 1.0
    play noise_1 toilet
    pause 5.4
    play sound closet_open
    pause 1.75
    play sound closet_close
    stop noise_1
    pause 2.0
    play noise_1 mc_steps_house
    pause 2.0
    stop noise_1
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0

    call window_open
    scene bg mc house bathroom day with dissolve
    "А сегодня я даже не разбитый."
    play noise_1 sink_open
    "Обычно встаёшь через силу, тащишься по всему дому..."
    "Потом начинаешь завтракать, а желудок отказывается работать из-за сонливости."
    "Позже он, естественно, очухивается, но всё равно неприятно."
    stop noise_1
    play sound sink_close
    "А сейчас совершенно наоборот: легко поднялся, тяжести никакой, мысли свежие..."
    "Мне аж с себя страшно."
    call window_close

    scene black with dissolve
    pause 0.25
    play sound closet_open
    pause 1.75
    play sound closet_close
    pause 2.0
    play noise_1 mc_steps_house
    pause 4.0
    stop noise_1

    call window_open
    scene bg kitchen with dissolve
    "А сегодня у нас что?"
    "Правильно, купленные с того похода в магазин хлопья."
    "Взял тогда себе пару пачек."
    "..."
    "Стойте, уже больше недели с того момента прошло?"
    "А ведь словно это вчера было..."
    "Мда."
    call window_close

    play sound cereals
    pause 15.762

    call window_open
    scene bg kitchen at mc_kitchen_table_alone
    with dissolve
    mc "Что ж, жрать подано."
    "..."
    "Честно, всё равно к школе идёт какое-то отвращение..."
    "Ничего привлекательного и что-то стоящего, кроме знаний, там нет."
    "Да и с ними тоже мало приятного, если уж быть честным."
    "Хотя я вроде как это уже говорил..."
    "Вообще вот была бы возможность, учился бы в одиночку."
    "Причём гораздо эффективнее, чем очно."
    "Заодно мог бы сразу передохнуть, послушав музыку, перекусив или глянув что-нибудь интересное."
    "А так..."
    "Ждать эти перемены...{w}торчать в постоянном шуме среди наивных, а иногда и дерзких одноклассников, ну и, конечно же, невероятных «вундеркиндов» в учёбе..."
    "И это ещё радоваться надо, что идти до школы недалеко, а сама программа обучения более-менее понятная и простая."
    "О, я всё слямзал."
    "Значит, пора одеваться."
    call window_close

    scene bg kitchen with dissolve
    pause 1.0
    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "Школьная форма..."
    "Отдать должное, дресс-код у этой школы реально хороший."
    "Лично мне он понравился за это короткое время."

    scene bg bedroom zorder 1:
        xzoom -1
        blur 15.0
    show mc_house_mirror zorder 3
    show mc cross happ cm oe zorder 2 at i11:
        xzoom -1
        offset(-30, 50)
    with wiperight
    show mc om
    mc "Отлично смотрится."
    mc "Костюм сидит так, будто на меня сшит."
    show mc neut om oe
    mc "Ох, он же ведь действительно на меня сшит."
    show mc cm
    mc "..."
    mc "......"
    show mc turned neut om oe
    mc "Да блин, всё равно выглядишь, как придурок."
    show mc angr om oe
    mc "Другие успели вырасти и приобрести лицо в харизме, а ты всё такой же...{w}всратый."
    mc "Ну серьёзно..."
    show mc cross neut om oe
    mc "А впрочем...{w}какая разница, если честно?"
    show mc curi om oe
    mc "Перед кем мне красоваться?"
    mc "Перед собой родимым?"
    show mc neut om oe
    mc "Всем глубоко на меня плевать."
    mc "Как и мне на остальных."
    show mc cm

    scene bg bedroom with wiperight
    "Ладно, сумка собрана уже вчера -- всё на месте."
    "Мобильник с собой, ключи тоже."
    "Пора выходить."
    "Может, сразу Сайори подхвачу..."
    "Не опоздает ли она в этот раз?"
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg residential_day with wipeleft_scene
    "Снова солнце..."
    "Снова голубое небо..."
    "Снова..."
    play music sayori_happy fadein 3.0
    s "{size=19}Х-э-э-э-э-э-й!!!{/size}"
    "...ко мне бежит жизнерадостное семнадцатитилетнее чудо, которому абсолютно фиолетово на то, что оно только что сильно привлекло внимание окружающих."
    show sayori turned nerv cm ce school_bag at l11
    pause 0.7
    show sayori om
    s "Фух, успела!"
    show sayori cm
    mc "Ха, я думал уже за тобой идти."
    show sayori laug om oe
    s "Размечтался!"
    show sayori happ om ce
    s "Я всегда успеваю выйти вовремя!"
    show sayori cm
    "Как она, несмотря на свой спортивный образ жизни, умудряется опаздывать на несколько минут?"
    show sayori neut cm oe
    mc "Сайори, ты слишком много суетишься..."
    show sayori tap pout cm oe school_bag at s11
    s "Уф-ф-ф..."
    mc "...из-за чего теряешь много времени."
    mc "Тебе стоит получше распланировать своё утро."
    show sayori neut cm oe
    mc "Постарайся это сделать в ближайшее время, хорошо?"
    show sayori turned happ cm ce rup lup school_bag at h11
    s "Угу!"
    show sayori rdown ldown
    "Надеюсь, мои слова не были для неё пустым звуком..."
    show sayori oe
    mc "Раз с этим разобрались, то нам пора уже идти."
    show sayori om ce rup lup at h11
    s "Ок-ке!"
    show sayori cm ldown rdown
    hide sayori with easeoutright
    mc "Ё-моё, носится, как угорелая..."
    "..."
    "У Сайори такая маленькая сумка, что за спиной её вообще не видно: только ремень спереди торчит."
    "И как только туда всё помещается?"

    scene bg niigata street suburban 10 day
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om
    s "Кстати, Макс..."
    show sayori cm
    mc "М-м-м?"
    show sayori om
    s "Ты же ведь помнишь, что нам всем надо выбрать себе клуб?"
    show sayori cm
    mc "Да, добровольно-принудительно, каждый день классный руководитель говорит мне об этом."
    show sayori om
    s "Ты ведь что-то уже надумал?"
    show sayori cm
    mc "Ха..."
    stop music fadeout 3.0
    show sayori neut cm oe
    mc "Нет."
    show sayori om b1b
    s "Почему?"
    show sayori cm
    mc "Я не люблю подобные вещи, Сайори."
    show sayori vsur cm oe -b1b
    mc "Да и ничто не приглянулось, если уж на то пошло."
    show sayori om
    s "Тебе всё равно надо что-то выбрать!"
    show sayori happ om oe lup
    s "Ведь клубы -- это не только совместные занятия по интересам..."
    "...но и высасывание твоего личного времени."
    show sayori curi om e2b ldown rup
    s "...но и новые связи: знакомые, друзья, подруги..."
    show sayori neut cm oe rdown
    mc "Я это прекрасно понимаю..."
    show sayori sad om oe
    s "Я же беспокоюсь за тебя!"
    s "У тебя слишком мало общения, а тут такой шанс его получить, так ещё и развить социальные навыки, которые пригодятся в дальнейшей жизни!"
    show sayori cm
    mc "Сайори, ты же ведь сама знаешь, что я не люблю контактировать с людьми, хоть и умею это делать."
    show sayori pout cm oe
    mc "Мне тебя за глаза хватает."
    show sayori om
    s "...и компьютера."
    show sayori cm
    mc "Эй, я там хотя бы занимаюсь, а не в игры играю."
    show sayori om
    s "Всё равно!"
    show sayori cm
    "Мда, это может продолжаться бесконечно."
    "Вот вечно всем надо усложнить мне жизнь."
    show sayori anno cm ce
    "У меня будто так много желания и времени, чтобы вступить в какой-то бестолковый клуб?"
    "Ещё же сверху будут нагружать какими-то обязательными заданиями."
    show sayori curi cm ce
    "Вот был бы клуб по обсуждению различных сюжетов игр или книг..."
    "Пришёл, пообщался на приятную тебе и окружению тему, попрощался, ушёл."
    show sayori dist cm ce
    "Всё, все довольны и все счастливы."
    "И никаких лишних и бесмысленных занятий."
    show sayori happ om oe
    s "Давай так: сегодня после уроков мы вместе пойдём и выберем тебе клуб."
    show sayori cm
    "Ага, и я за ручку с Сайори буду прыгать по кабинетам и светиться у всех на виду?"
    "Да это же посмещище!"
    show sayori neut cm oe
    mc "Нет, так не пойдёт."
    show sayori tap pout cm oe school_bag at s11
    s "Мф-ф-ф..."
    show sayori cm ce
    s "Хм-м-м..."
    "...или она так завуалированно хотела втянуть меня в Литературный клуб?"
    "Я же ей, кстати, про Монику ничего не рассказывал."
    show sayori neut cm oe
    mc "...ладно, была у меня одна идея..."
    show sayori turned neut cm oe school_bag at t11
    s "М-м?"
    mc "Я как-то недавно встретился в соцсетях с одной ученицей этой школы, которая является президентом Литературного клуба."
    show sayori happ cm oe
    mc "Вот она и предложила членство."
    show sayori om
    s "А, так это тот клуб, в котором я состою."
    show sayori neut cm oe
    mc "Состоишь?"
    "Всё, начинается игра на публику с моей стороны..."
    show sayori om e1b
    s "Да, я не рассказывала, потому что тебе всё равно такое неинтересно..."
    show sayori cm
    mc "Э-э-э..."
    show sayori oe
    mc "С чего вдруг?"
    show sayori om
    s "Ну ты же не увлекаешься стихами или нечто подобным."
    show sayori dist om oe
    s "Да и в целом у нас вяленько..."
    show sayori cm
    "...если это так, то нагрузки будет мало, верно?"
    show sayori neut cm oe
    mc "Это не повод умалчивать ситуацию."
    mc "Тем более раз ты там, то почему бы и не зайти, посмотреть..."
    show sayori om
    s "Да?"
    show sayori cm
    mc "А почему нет?"
    show sayori happ cm oe
    mc "Но так не хочется время тратить, когда много домашних заданий сверху навалят..."
    show sayori om
    s "Да ладно тебе, Макс, просто зайдём и глянем, приключение на 20 минут."
    show sayori cm
    mc "...ну хорошо, посмотрим."
    show sayori om e4c lup rup at h11
    s "Ура!"
    show sayori cm ldown rdown
    "Хоть один туда не попрусь, уже хорошо."

    scene bg school gate 1
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    mc "Кажется, пришли."
    show sayori om ce
    s "Ага!"
    show sayori cm
    "Вроде самое время, но учеников практически нет."
    "Только несколько человек на горизонте еле прутся."
    show sayori oe
    mc "Вообще никого."
    show sayori om ce rup lup at h11
    s "Это потому что у нас отлично распланирован график!"
    show sayori cm ldown rdown
    "...сказала Сайори, которая опаздывает по утрам, прибегая в попыхах."
    mc "...точно."
    "Но в её словах есть правда."
    show sayori e1b
    "Может, график у меня «совсем отнюдь не очень», но вполне приемлемый."
    show sayori neut cm oe
    mc "Что ж, пора расходиться?"
    show sayori dist om oe
    s "Да..."
    show sayori happ om ce lup rup at h11
    s "Увидимся после уроков!"
    show sayori cm ldown rdown
    mc "Хорошо."
    show sayori at thide
    hide sayori
    pause 1.0
    "Пора тащиться в свой класс..."
    stop noise_1 fadeout 3.0
    call window_close

    call window_dialog_long_transition("n")

    call window_open
    play noise_1 school_corridor_light_noise fadein 3.0 volume 0.5
    scene bg school new_class_natsuki day with dissolve_scene_full
    n "Фе-е-е..."
    "Наконец-то дошла..."
    "Как же хорошо, когда приходишь очень рано: никого нет..."
    "А то вечно все шумят и мешают."
    "Дома в это время сидеть нет смысла: папа ещё спит, не хочу его беспокоить и лишний раз попадаться ему на глаза."
    "А-а-а, вообще нигде нельзя спокойно мангу почитать!" with vpunch
    "Отец вечно отнимает её у меня под предлогом: \"Это всё детская ерунда!\""
    "Приходится хранить в кладовке клуба, потому что больше негде."
    "Если бы школа запрещала и это..."
    "...я бы тогда в своей жизни никогда не расслабилась..."
    "Но странно, что ранобэ папа не трогает."
    "Море текста для него, значит, не «детская ерунда», даже если там откровенный бред..."
    "Зато её можно спокойно оставлять в спальне на полках."
    "Конечно, я пробовала читать подобные произведения, но быстро уставала от большого количества «воды»."
    "Хотя ведь что-то смогла осилить..."
    "Но нет, больше покупать ранобэ не буду!"
    "...только если сам сюжет не захватит."
    "Угх, а за мангу на людях всегда стыдно!"
    "Всё равно, что если меня увидят в нижнем белье..."
    "Короче, засмеять могут из-за «несерьёзности»."
    "Все же у нас знатоки в произведениях, да?"
    "Пока что в открытую одноклассники не презирали, вероятно, понимают, что могут за такое от меня получить, как тот идиот зимой, который пытался надо мной поиздеваться..."
    "Но я прямо чувствую, как они косятся своими глазами на мои томики и как они хотят к ним придраться!"
    "Кх-х-х, это издевательство надо мной!"
    "Хорошо тихое место есть в старом корпусе у перекрытой лестницы."
    "Спасибо, Юри..."
    "И Монике спасибо за то, что всегда открывает ключом кладовку, когда я хочу почитать."
    "Ни разу не получила отказ в такой просьбе."
    "И спасибо за хранение манги у себя дома летом."
    "Ой, ладно, не будем терять драгоценное время."
    "Пора почитать мою любимую «Ванильную симфонию»!"
    "Люблю эту мангу ещё с детства."
    "Никогда бы не подумала, что она сможет укрепить мой интерес к готовке кексов..."
    "Изначательно меня мама научила их готовить, но я хотела с ними экспериментировать, а не просто печь по одному и тому же рецепту."
    "Ну хоть это отец не запрещает, спасибо!"
    "Так, всё!"
    "Приступим!"
    window hide

    pause 8.5

    if persistent.add_random_menu == 4:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()

    window auto
    show hiroshi neut cm e1c at r11
    pause 0.5
    show hiroshi oe
    pause 0.3
    show hiroshi happ om ce rhip
    play music school_of_quirks fadein 3.0
    h "О, На{image=accent_low_register}{space=-15}цуки, привет!"
    show hiroshi cm
    "{sc=3}А-А-А-А-А-А, ПРЯТАТЬ-ПРЯТАТЬ-ПРЯТАТЬ!!!--{/sc}{nw}"
    n "Опять ты?"
    show hiroshi oe
    "Чёртов Хиро{image=accent_low_register}{space=-15}ши!"
    show hiroshi fc happ om oe
    h "Время идёт, а ты всё такая же грубая."
    show hiroshi cm
    n "Что ты сюда так рано припёрся?"
    show hiroshi doub om oe
    h "А что, нельзя?"
    show hiroshi cm
    n "Да, я запрещаю."
    show hiroshi happ om oe lhip
    h "Я вообще раньше тебя сюда пришёл, имею право."
    h "Сейчас просто в туалет отходил."
    show hiroshi cm
    "А ведь точно..."
    "Его сумка в другом конце класса сбоку парты висит."
    show hiroshi neut om e1d ldown
    h "Хотел, кстати, у тебя спросить..."
    show hiroshi cm
    n "Что тебе опять нужно?"
    show hiroshi happ om oe
    h "Я слышал, что у тебя есть свежий томик «Ванильной симфонии»..."
    show hiroshi cm
    "ЧЕГО?!" with vpunch
    "Откуда он узнал?!"
    "Только на днях его купила!"
    show hiroshi neut cm oe
    n "Я тебе его не дам!"
    show hiroshi curi om oe
    h "Эй, я тоже фанат этой франшизы, забыла уже?"
    show hiroshi cm
    n "Ты?!"
    n "Ха-ха-ха!"
    show hiroshi anno cm oe
    n "Не смеши меня."
    show hiroshi om rdown
    h "Что за натянутый смех?"
    show hiroshi cm
    n "Потому что ты как не знал, так никогда и не узнаешь скрытый смысл данного произведения!"
    n "А значит, ты не можешь быть истинным фанатом «Ванильной симфонии»!"
    "Наполовину блефую, но, может, он хоть так отстанет..."
    show hiroshi neut cm oe
    "А то достал уже, честное слово!"
    "Сколько не огрызаюсь, он всё лезет и лезет!"
    show hiroshi om
    h "Ты могла бы меня просветить."
    show hiroshi cm
    n "Нафиг надо?"
    show hiroshi angr om oe lhip rhip
    h "А вообще я тебя не понимаю: у меня довольно маленький, уютный Клуб математики."
    h "Почему бы тебе не вступить в него?"
    show hiroshi neut om oe
    h "Никто тебя там донимать не будет, обещаю."
    show hiroshi happ om oe
    h "У тебя будет место, где хранить твою мангу, а заодно подтянешь свои знание по математике."
    show hiroshi neut cm oe
    n "Я же сказала, отстань от меня."
    show hiroshi rdown
    n "Мне литературного клуба за глаза хватает, меня там всё устраивает!"
    show hiroshi anno cm oe
    n "И менять его на другие я не собираюсь!"
    show hiroshi om
    h "Глупо отказываться от этого, Нацуки."
    show hiroshi cm
    n "Глупо быть бараном после стольких отказов!"
    show hiroshi happ om oe
    h "Давай снова подружимся, и ты узнаешь, что я далеко не баран."
    show hiroshi cm
    n "Ещё чего!"
    show hiroshi neut cm oe
    n "У меня нет желания дружить с занудами-ботаниками-баранами вроде тебя."
    show hiroshi angr om oe
    h "Грх, когда успокоишься, тогда и поговорим!"
    show hiroshi ff angr cm e1d at thide
    hide hiroshi
    pause 1.0
    "Наконец-то..."
    "Хватило мне дружбы с этим дураком в средней школе!"
    "Сначала был такой весь из себя добрый, а потом начал подкалывать и лезть ко мне без остановки."
    "Это хорошо, что он до откровенных издевательств не дошёл!"
    "Нельзя никому доверять, совершенно!"
    "Никогда!"
    "Иначе опять попадётся такой же засранец, который испоганит мою и без того проблемную жизнь."
    $ currentpos = get_pos(channel="music") + 2
    stop music fadeout 2.0
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition(different_scene = False)
    pause 1.0
    play sound school_bell
    pause 4.5

    call window_open
    "Да что ж такое!"
    "Я только втянулась в чтение!"
    "Ладно, на перемене продолжу."
    "А сейчас надо слушать скучный монолог учителя по геометрии, который заставит всех решать свои нудные задачки..."
    call window_close

    call plot_transition

    call window_open
    $ audio.school_of_quirks_2 = "<from " + str(currentpos) + " loop 7.058 to 146.077>mod_assets/music/school_of_quirks.ogg"
    play music school_of_quirks_2 fadein 0.5
    play noise_1 wind fadein 3.0
    scene bg school new_rooftop 1 day with wipeleft_scene
    "Да ладно, неужели тут пусто?"
    "Очень хорошо, мне это только на руку."
    "Итак, снова приступим к манге."
    window hide

    pause 6.0

    window auto

    show hiroshi happ cm e1c at l11
    pause 0.7
    show hiroshi fc neut cm oe
    n "Опять ты припёрся?!"
    show hiroshi doub om oe rhip
    h "Нацуки, хватит уже грубить, я даже ничего не сделал."
    show hiroshi cm
    n "Не дам!"
    show hiroshi curi om oe
    h "Ну можно я хотя бы рядом присяду и послушаю, что в этом томе по сюжету?"
    show hiroshi cm
    n "Уйди НАХРЕН!"
    hide hiroshi
    show hiroshi fc curi cm oe at el11
    with dissolve
    pause 0.25
    show hiroshi om
    h "Да почему, я же просто присяду--{nw}"
    show hiroshi cm
    n "{sc=3}САМ НАПРОСИЛСЯ!!!{/sc}{w=1.0}{nw}"
    call skip_block_on

    call screen punch_hiroshi_a1_d1

    call skip_block_off
    scene white
    stop music
    pause 0.1

    scene bg school new_rooftop 1 day
    show hiroshi fc shoc cm oe at el11
    show hiroshi at tfast
    pause 1.5
    play music natsuki_run_panic
    show hiroshi om
    h "Ч-ч-чего?..."
    show hiroshi cm

    scene black with wipeleft_scene
    play noise_2 natsuki_steps_run
    "{sc=3}А-А-А-А-А!!!{/sc}"
    "{sc=3}Почему мне везёт на таких идиотов?!{/sc}"
    h "{sc=3}А НУ СТОЙ!!!{/sc}"
    call window_close

    $ n_name = "???"
    $ h_name = "???"
    $ renpy.music.set_volume(0.2, 0, "music")

    call window_dialog_fast_transition("mc")

    stop noise_1
    stop noise_2

    call window_open
    scene bg school f3 new_corridor
    show crowd_background zorder 0
    show crowd_foreground zorder 2
    play noise_1 school_corridor_hard_noise
    "..."
    "Ребят, вас что-то слишком много..."
    "Фиг протиснешься."
    window hide

    pause 5.0

    window auto
    "Там кто-то впереди бежит или мне показалось?"
    window hide

    pause 4.0

    window auto
    "О, дыра в толпе."
    "Сейчас выберемся из этого--{nw}"
    call window_close

    $ renpy.music.set_volume(1.0, 0.5, "music")
    show natsuki turned fc pani cm oe school_bag zorder 3 at movein_hugs
    pause 0.15
    show natsuki s_scream
    pause 0.15
    play sound ram_attack
    scene white
    pause 0.1
    scene black
    show particle_star
    with dissolve

    call window_open
    mc "{sc=3}А-А-А!{/sc}"
    n "{sc=2}АЙ!{/sc}"
    "Какого чёрта?!"

    scene bg school f3 new_corridor
    show crowd_foreground zorder 2
    show crowd_background zorder 0
    show natsuki turned fc pani cm ce school_bag zorder 3 at t11
    with dissolve_scene_full
    mc "Ты в порядке?!"
    show natsuki om ce
    n "Да!"
    show natsuki cm ce
    mc "Зачем ты так носишься в толпе?!"
    show natsuki om oe
    n "Не до тебя сейчас!"
    show natsuki cm e2b at lhide
    hide natsuki
    pause 0.5
    "Что?"
    h "{sc=3}СТОЙ, КОМУ ГОВОРЮ!!!{/sc}"
    call window_close

    show hiroshi fc vang cm oe zorder 3 at t11
    pause 0.4
    show hiroshi ff vang cm oe at lhide
    hide hiroshi
    pause 0.5

    call window_open
    "Что здесь происходит?!"
    call window_close

    $ n_name = _("Нацуки")
    $ h_name = _("Хироши")

    call window_dialog_fast_transition("n")

    stop noise_1

    call window_open
    scene black
    play noise_1 natsuki_steps_run
    h "{sc=3}СТОЙ, ЗАРАЗА!!!{/sc}"
    n "{sc=3}САМ СТОЙ, ЗАРАЗА!!!{/sc}"
    window hide

    pause 3.0

    window auto
    "{sc=3}ДА ЛАДНО?!{/sc}"

    play noise_2 school_corridor_empty_noise fadein 1.0
    scene bg school f3 old_corridor
    show yuri turned neut mf e1b lup school_bag at t41
    with wipeleft_scene
    stop noise_1
    n "ЮРИ{image=accent_high_register}{space=-15}-И-И!"
    n "Хорош глазеть на автомат!"
    n "Куплю я тебе этот зелёный чай!"
    n "Лучше меня спаси!"
    show yuri pani om oe rup at h41
    y "Н-Нацуки?!"
    show yuri cm at t11
    n "{sc=3}УГОМОНИ ЭТОГО ПОЛОУМНОГО!!!{/sc}"
    show yuri ldown rdown at t22
    show hiroshi fc yand om oe at t21
    h "Опять за свою Юри прячешься?!"
    show hiroshi cm
    n "Могу себе позволить!"
    show yuri vsur om oe
    y "Р-ребят...{nw}"
    show yuri cm
    show hiroshi angr om oe
    h "Устроила проблему на ровном месте!"
    show hiroshi cm
    n "{sc=3}ИЗДЕВАЕШЬСЯ?!{/sc}"
    show yuri sad om oe
    y "Подождите...{nw}"
    show yuri cm
    show hiroshi om lhip rhip
    h "А сама что делаешь?!"
    show yuri shoc cm ce
    show hiroshi cm
    n "Спасаюсь от такого придурка, как ты!"
    show yuri pani cm ce
    show hiroshi om
    h "Ах ты--{nw}"
    play music_none_loop music_stop
    stop music
    show yuri vang om oe
    show hiroshi cm
    y "{sc=3}МОЛЧА-А-АТЬ!!!{/sc}" with vpunch
    show yuri cm
    h "..."
    show yuri angr cm oe
    n "..."
    show yuri om ce
    y "Вдох..."
    show yuri anno om ce
    y "...выдох."
    show yuri pout om oe
    y "А теперь спокойно расскажите, что у вас происходит--{nw}"
    show yuri neut cm e1d
    show hiroshi om
    h "Да идите вы обе нафиг со своими разбирательствами..."
    show yuri lsur cm oe
    show hiroshi cm at thide
    hide hiroshi
    n "Пошёл отсюда, дебил!"
    y "..."
    "..."
    show yuri om
    y "Но я по-настоящему хотела разобраться..."
    show yuri cm
    n "Юри..."
    show yuri shy sad om ce n5 school_bag at s22
    y "А он снова нагрубил..."
    show yuri cm
    n "Ты просто МОНСТР!"
    n "Укокошила его пыл на раз-два одной фразой!"
    n "А вот меня он, как обычно, ничерта не слушал!"
    y "..."
    n "Ой, да забей на его поведение, в гробу я видала его грубость!"
    n "Он по жизни такой, его ничто не исправит."
    n "Я бы ему втащила несколько раз со всей силы, а не легонько, но только после этого куча проблем начнётся..."
    n "Короче, ты молодец!"
    n "Защитила меня в очередной раз!"
    y "..."
    n "А, точно, теперь с меня причитается."
    call window_close

    scene black with wiperight
    pause 3.0
    play sound vending_machine_drinks
    pause 20.323

    call window_open
    n "Держи свой чай."
    y "Спасибо..."
    n "Это я тебя должна благодарить, ха!"
    y "..."
    "Всё бестолку, надо чем-то её расслабить..."
    n "Хм-м..."
    "Точно, перекрытая лестница!"
    n "Ладно, у нас ещё полно времени до следующего урока..."
    n "Может, посидим на нашей любимой лестнице?"
    n "У меня с собой несколько шоколадок имеется, купила их вчера."
    n "Поэтому их надо съесть, пока они не растаяли окончательно."
    y "М-м...{w}давай..."
    "Её слабости -- чтение и шоколад."
    "После такого перерыва Юри точно забудет обо всём происходящем."
    call window_close

    call plot_transition

    call window_open
    scene bg school f1 old_stairwell right
    show yuri turned worr cm oe school_bag at t22
    with wipeleft_scene
    "Как прекрасно, что в старом корпусе, кроме клубов, практически никого нет."
    "Никаких идиотов, как тот дурень Хироши."
    "Только тишина...{w}первую половину дня точно."
    show yuri neut cm e1d
    n "Давай опять к окну между пролётами, там нас точно никто не увидит."
    show yuri me
    y "Угу."
    show yuri cm
    "Я уже вижу, как у Юри слегка загорелись глаза."
    "Это место всегда её оживляет."

    if cg_a1_d1_y.unlocked == False:
        $ cg_a1_d1_y.unlock()

    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc at cgfade
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    play music t6
    n "Ух, хорошо..."
    y "Угу..."
    "Не прошло и десяти секунд, как она погрузилась в свою книгу."
    "«Портрет что-то там...»."
    "Никогда не понимала такие массивные произведения."
    "Умрёшь читать первые страницы, а их там сотни, если не тысячи!"
    "А если там ещё описание природы и прочей ерунды, так вообще повеситься можно."
    "В манге хотя бы разнообразие есть."
    "И сюжет динамичный."
    n "Ладно, пора поедать шоколадку, а то растает."
    y "..."
    "Она вообще слышала?"
    "Или мы потеряли связь с Юри?"
    window hide

    pause 3.0

    window auto
    n "Так, вот и первая долька!"
    n "Открой рот."
    "..."
    "Она точно меня не слушает."
    "Значит, так впихну."
    "Её проблема, раз не услышала."
    window hide

    pause 2.0
    hide y_cg2_nochoc
    pause 2.0
    show y_cg2_exp2 at cgfade

    window auto
    y "Мфмпфм?"
    n "Шоколадка."
    n "Ам-м."
    call window_close

    pause 2.0
    show y_cg2_nochoc at cgfade
    pause 1.0
    show y_cg2_exp3 at cgfade
    hide y_cg2_exp2

    call window_open
    n "Ну как?"
    y "...вкусно."
    y "Спасибо..."
    n "У меня ещё есть."
    hide y_cg2_exp3
    window hide

    pause 3.0

    window auto
    "Второй кусок плитки на подходе."
    "Сначала Юри..."
    window hide

    pause 2.0
    hide y_cg2_nochoc
    pause 2.0

    window auto
    "...потом себе."
    window hide

    pause 6.0

    window auto
    "Обожаю молочный шоколад."
    "Горький всегда вызывает отвращение, если его есть без всего."
    "Такой шоколад только в готовке и использовать."
    "А молочный мягко тает во рту и оставляет приятное послевкусие."
    show y_cg2_nochoc at cgfade
    "Но переедать нельзя, иначе пить жутко захочется..."
    n "Э-э, так быстро?"
    n "Там одна долька осталась..."
    y "М-м-м..."
    "Неужто шоколада так было мало?"
    window hide

    pause 3.0

    window auto
    n "Так, хватай шоколад--{nw}"
    hide y_cg2_nochoc
    show y_cg2_exp2 at cgfade
    play music_none_loop music_stop
    stop music
    m "О, вот вы где!" with vpunch
    n "МОНИКА?!"


    play music t5 fadein 3.0
    scene bg school f1 old_stairwell right
    show monika forward happ cm oe school_bag at t21
    show yuri shy school_bag sad cm oe n5 at s22
    with dissolve_cg
    show monika om ce lpoint
    m "Ха-ха, извините, что прервала ваш отдых!"
    show monika cm ldown
    n "У меня чуть сердце не ёкнуло, предупреждать надо!"
    show monika oe
    y "Умф..."
    show monika om
    show yuri neut cm oe n1
    m "Не стыдись, Юри."
    show monika lean happ om oe n3 school_bag at h21
    show yuri m1 e1 b2
    m "Честно говоря, я бы не отказалась, чтобы меня так же покормили!"
    show monika forward laug cm oe n1 school_bag at t21
    show yuri m3
    n "Шоколадок на вас не напасёшься!"
    show monika ce
    show yuri ce
    y "Хе-хе..."
    show monika om
    m "Ха-ха-ха!"
    show monika happ om oe
    show yuri m1 e1
    m "Ладно, ближе к делу."
    show monika lpoint rhip
    show yuri turned curi cm oe school_bag at t22
    m "У нашего клуба сегодня может быть знаменательное событие!"
    show monika cm ldown rdown
    show yuri om oe
    y "По какому поводу?"
    show monika laug cm ce
    show yuri doub cm oe
    n "Манга теперь официально литература?"
    show yuri om ce
    y "Манга никогда не была литературой."
    show yuri cm ce
    n "Манга -- ли--{nw}"
    show monika happ om oe lpoint
    show yuri curi cm oe
    m "Нет-нет, лучше!"
    show monika cm ldown
    show yuri om oe
    y "Лучше?..."
    show monika ce
    show yuri cm oe
    n "Ай, Моника, не томи, говори уже!"
    show monika om oe
    show yuri vsur cm oe
    m "Наш состав может увеличиться до 5-и человек уже на постоянной основе!"
    show monika lpoint rhip
    m "А это будет означать, что мы станем полностью официальным клубом!"
    show monika neut cm oe ldown rdown
    n "Воу-воу-воу, полегче!"
    n "С чего вдруг этот 5-ый человек будет у нас постоянным участником?"
    show yuri lsur om ce
    y "Д-да, не будем забегать вперёд и рано радоваться."
    show monika happ cm oe
    show yuri dist om ce
    y "Надо сначала убедиться, что этот некто точно захочет стать членом нашего клуба."
    show yuri cm ce
    n "Именно."
    show yuri curi cm oe
    n "Кстати, кто это вообще?"
    show monika lean happ om ce school_bag at h21
    m "Сюрприз~"
    show monika om oe at t21
    m "Но, думаю, он вам понравится."
    show monika cm oe
    show yuri om oe
    y "Понравится?..."
    show monika forward happ cm oe school_bag
    show yuri cm oe
    n "Если это кто-то будет откровенным придурком или идиотом--{nw}"
    show monika om oe
    show yuri shoc cm oe
    m "Нет, я с ним уже разговаривала, он хороший парень."
    show monika cm ce
    show yuri shoc om oe lup rup at h22
    y "П-парень?!"
    show monika neut cm oe
    show yuri nerv cm oe at t22
    n "Да он же всю атмосферу клуба убьёт!"
    show monika happ om oe lpoint rhip
    show yuri lsur cm oe
    m "Не думаю, потому что он достаточно аккуратный и понимающий человек."
    show monika cm oe ldown rdown
    show yuri worr cm oe ldown rdown
    n "Аккуратный и понимающий..."
    show yuri happ om oe lup
    y "Как бы то ни было, мы его «торжественно» примем."
    show monika laug cm oe
    show yuri flus cm e1a ldown
    n "Одарим лавровым венком и постелим красную ковровую дорожку?"
    show monika laug cm ce
    show yuri om
    y "Не в этом смысле!"
    show yuri cm
    n "А ещё будем преклоняться и говорить: \"Добро пожаловать, господин!\""
    show yuri oe
    n "Ха-ха-ха-ха!"
    show monika lean happ om oe school_bag at h21
    show yuri laug cm oe
    m "Но ты правильно мыслишь, Юри!"
    show monika cm oe
    show yuri happ cm ce
    n "ПХ-Х-ХП--{nw}" with vpunch
    n "Вы чё?!"
    show monika forward happ om oe lpoint rhip school_bag at t21
    show yuri cm oe
    m "Я предлагаю вам после уроков сразу пойти в клуб и прибраться."
    show monika ldown rdown
    m "Буквально пыль немного смахнуть, парты поправить и так далее."
    m "А в это время мы с Сайори немного задержим нашего гостя и позже приведём его в класс."
    show monika happ cm ce
    show yuri angr cm oe
    n "Ага, значит, нам с Юри поручаешь грязную работу, а себе -- церемонию посвящения?"
    show monika cm oe
    show yuri angr om oe
    y "Уборка клуба -- тоже важная ответственность!"
    show yuri dist om ce lup rup
    y "Мы сделаем всё в лучшем виде."
    show yuri cm ce
    n "А-а-а--{nw}"
    show monika om ce
    show yuri happ cm ce rdown ldown
    m "Спасибо, я знала, что на вас можно рассчитывать!"
    show monika neut om oe
    show yuri pout cm oe
    m "Только всего будет где-то полчаса, а может, и меньше, успеете?"
    show monika happ cm oe
    show yuri om oe
    y "Абсолютно."
    show yuri cm oe
    n "....."
    show monika lean happ om oe school_bag at h21
    show yuri happ cm ce
    m "Отлично, до встречи сегодня всем составом!"
    show monika cm oe at t21
    show yuri om ce
    y "Удачи!"
    show yuri cm ce
    show monika forward happ cm oe school_bag
    hide monika with easeoutleft
    n "....."
    show yuri om oe
    y "Пошли, Нацуки, скоро будет звонок."
    show yuri cm oe
    hide yuri with easeoutleft
    n "....."
    stop noise_2 fadeout 5.0
    stop music fadeout 5.0
    call window_close

    call window_dialog_long_transition("mc")

    call window_open
    play noise_1 school_corridor_empty_noise fadein 3.0
    scene bg school new_class_mc day with dissolve_scene_full
    mc "У-у-угх-х-х..."
    "Как же я затёк..."
    "Весь класс уже смылся либо на выход, либо в клубы."
    "Пора бы и мне двинуть."
    if persistent.add_random_menu == 5:
        $ persistent.add_random_menu += 1
        $ renpy.save_persistent()
    show mrs_ida happ cm oe at t11
    pause 0.2
    show mrs_ida om
    mi "Ну что, Макс, всё ещё не хочешь вступить в какой-нибудь клуб?"
    show mrs_ida neut cm oe
    mc "Нет, Ида-сэнсэй, нет ни желания, ни вариантов."
    show mrs_ida om ce
    mi "Что ж ты так их боишься..."
    show mrs_ida cm oe
    mc "Да не боюсь я!"
    show mrs_ida happ cm oe
    mc "У меня и так куча дел, не всегда успеваю справляться."
    show mrs_ida om ce lup
    mi "Оправдываешься~"
    show mrs_ida oe ldown
    mi "Я же знаю, что ты один живёшь."
    mi "У тебя времени априори достаточно."
    show mrs_ida cm
    mc "Гхм, это немного не так работает..."
    show mrs_ida neut om oe
    mi "Слушай, я понимаю, что ты приходишь сюда учиться, но школа -- это не просто получение знаний."
    show mrs_ida ce
    mi "Школа -- это первичный социальный институт, помогающий человеку влиться в общество."
    show mrs_ida oe
    mi "У нас в Японии этому уделено большое внимание: создаются клубы с разнонаправленными тематиками, организуются различные фестивали, интересные мероприятия..."
    show mrs_ida happ om oe
    mi "Поэтому ты должен быть рад, что тебе выпадает такая хорошая возможность социализироваться, которая есть не у всех учеников в мире."
    show mrs_ida neut cm oe
    mc "Если бы меня ещё это общество привлекало..."
    show mrs_ida neut om oe
    mi "Разве ты так и не нашёл себе друзей, кроме Сайори?"
    show mrs_ida cm
    mc "Я тут всего чуть больше недели."
    show mrs_ida happ cm oe
    mc "Откуда?"
    show mrs_ida om ce
    mi "Вот как раз тебе и дополнительный стимул для вступления в клуб~"
    show mrs_ida cm
    mc "Пф-ф-ф..."
    show mrs_ida neut om oe
    mi "Я знаю, что по поведению ты отличаешься от большинства: более спокойный, работоспособный и ответственный...{w}но при этом крайне закрытый и отстранённый."
    show mrs_ida sad om oe
    mi "Мне это очень не нравится."
    show mrs_ida ce
    mi "В дальнейшем это может перерасти в серьёзную проблему или даже в комплекс личности."
    show mrs_ida cm oe
    mc "Просто я чувствую себя на совершенно другом уровне, нежели на котором находятся мои сверстники."
    show mrs_ida neut cm oe
    mc "Не выше, не ниже, а где-то сбоку..."
    mc "Мне не нравятся ни их увлечения, ни их характеры, ни их микросоциумы, которые они организуют."
    show mrs_ida om
    mi "Прямо всех-всех сверстников не любишь?"
    show mrs_ida cm
    mc "...с кем приходилось пересекаться, или кого видел, слышал..."
    show mrs_ida ce
    mi "Хм..."
    show mrs_ida om oe
    mi "Но тогда почему Сайори является для тебя исключением?"
    show mrs_ida cm
    mc "Если б я сам знал..."
    show mrs_ida happ om oe
    mi "Кстати, она же у нас вице-президент Литературного клуба."
    mi "Почему бы тебе не вступить туда?"
    show mrs_ida cm
    mc "Я поэт, по-вашему?"
    show mrs_ida omb ce
    mi "Ну может, и поэт, ха-ха-ха!"
    show mrs_ida om oe
    mi "К тому же там всего 4 участника, и все они девушки."
    show mrs_ida lup
    mi "Им как раз не хватает одного человека для официального статуса."
    show mrs_ida neut cm oe ldown
    mc "Ограничение?"
    show mrs_ida om
    mi "Угу."
    show mrs_ida happ om oe
    mi "Литературный клуб уже давно должен был лишиться привилегий официального статуса, в том числе и своего класса в старом корпусе."
    mi "Однако все участницы крепко держатся друг за друга, а Моника является ответственным лицом на уровне всех президентов школы."
    mi "Всё это помогает сохранить привилегии."
    show mrs_ida neut cm oe
    mc "И даже так, у них всё равно нет людей."
    show mrs_ida sad om oe
    mi "Всему виной стихи."
    show mrs_ida ce
    mi "Не каждому это приходится по душе, не у каждого есть способности..."
    show mrs_ida happ cm oe
    mc "А у меня будто это есть?"
    show mrs_ida om ce
    mi "Уверена, что с твоими навыками и умениями всё получится."
    show mrs_ida oe
    mi "Вступи в Литературный клуб."
    show mrs_ida omb lup rhold
    mi "Подумай только, это же так романтично: писать для четырёх девушек стихотворения собственного сочинения!~"
    show mrs_ida ce
    mi "А может быть, ты там найдёшь вторую половинку, с которой свяжешь свою дальнейшую жизнь?~"
    show mrs_ida cm
    mc "Ох-х-х..."
    "Убейте меня от испанского стыда..."
    "Надо срочно сменить курс разговора, пока миссис Иду не унесло в любовные дебри."
    show mrs_ida neut cm oe ldown rdown
    mc "А, точно!"
    show mrs_ida curi cm oe
    mi "М-м?"
    show mrs_ida neut cm oe
    mc "Мы же с Сайори сегодня договорились зайти в этот клуб."
    show mrs_ida happ om oe
    mi "Ох, неужели?"
    show mrs_ida neut cm oe
    mc "Вот только мы не обсудили место встречи..."
    "Серьёзно, как мы упустили этот момент?"
    show mrs_ida om
    mi "Что ж вы так..."
    show mrs_ida cm
    mc "Без понятия."
    "И что делать?"
    "Пойти к Сайори?"
    show mrs_ida curi cm ce
    "А где находится её класс?"
    "Аргх!"
    "Начинаются проблемы..."
    show mrs_ida oe
    "Вечно что-то идёт не так!"
    show mrs_ida om
    mi "Может, тебе стоит сейчас--{nw}"
    show mrs_ida vsur cm oe
    s "{size=19}Он здесь!{/size}"
    mc "Э?"
    "Сайори меня нашла?"
    "И в каком смысле «здесь»?"
    "Она же ведь одна--{nw}"
    play sound closet_open
    pause 1.0
    play music according_to_the_plan fadein 3.0
    show mrs_ida happ cm oe at t33
    show monika forward happ cm oe school_bag at l32
    show sayori turned happ cm oe school_bag at l31
    pause 0.7
    show sayori om ce
    s "Приве-е-ет~"
    show monika om e1b
    show sayori cm
    m "Да, привет..."
    show monika nerv cm oe
    show sayori nerv cm oe
    mc "Моника?!" with vpunch
    show monika om ce
    m "Сегодня я прямо для всех сама неожиданность, ха-ха!"
    show monika cm
    show sayori flus om oe
    s "Ой, Ида-сэнсэй?!"
    show mrs_ida ce
    show monika happ cm oe
    show sayori happ om ce lup rup at h31
    s "Здравствуйте!"
    show monika om
    show sayori cm ldown rdown
    m "Здравствуйте, Ида-сэнсэй."
    show mrs_ida om
    show monika cm
    mi "Привет, ребятки~"
    show mrs_ida oe
    show sayori neut cm oe
    mi "Я так понимаю, что цель вашего визита -- забрать с собой Макса?"
    show mrs_ida cm
    show sayori curi om oe
    s "Как вы угадали?!"
    show mrs_ida om
    show sayori neut cm oe
    mi "Мы сейчас немного поговорили о клубах, заодно я ему про вас рассказала~"
    show mrs_ida cm
    show sayori happ om oe
    s "Ясненько..."
    show mrs_ida om
    show sayori cm
    mi "Ну что, Макс?"
    show mrs_ida ce
    show monika laug cm oe
    show sayori laug cm oe
    mi "Теперь тебе не отвертеться от вступления в Литературный клуб, когда за тобой пришли такие милые девушки~"
    show mrs_ida cm
    mc "Тх-х..."
    show monika ce
    show sayori tap nerv om oe school_bag at s31
    s "Э-хе-хе~"
    show sayori om ce
    "Нет, я бы сходил с Сайори в любом случае, но сейчас чувствую себя в кандалах."
    show mrs_ida oe
    show monika happ cm oe
    show sayori turned happ cm oe school_bag at t31
    mc "Ладно, пойдёмте, не будем тянуть время."
    mc "До свидания, Ида-сэнсэй."
    show monika om
    show sayori om ce
    ms "До свидания, Ида-сэнсэй!"
    show mrs_ida om ce
    show monika cm
    show sayori cm
    mi "До свидания, ребятки!"
    show mrs_ida cm
    show monika ce

    $ r_name = "???"

    scene black with wipeleft_scene
    mi "{size=19}Эх, повезло же парню~{/size}"
    mc "..."
    m "Хах, она так часто над тобой прикалывается?"
    mc "При каждом разговоре."
    m "Да-а, весело тебе..."
    s "Главное, что не скучно!"
    r "{size=19}Моника!{/size}"
    m "Ум-м?"
    r "{size=19}Привет!{/size}"
    r "{size=19}Подойди на минутку!{/size}"
    m "Ах, сейчас!"
    m "Вы пока идите в промежуточный коридор, я вас догоню."
    mc "...хорошо."
    s "Мы тебя подождём!"
    m "Да, конечно."
    call window_close

    $ r_name = _("Рэйко")

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg corridor
    n "Практически на месте..."
    "Юри написала, что уже орудует в кабинете."
    "Не понимаю, там же и так чисто, что там вообще делать?"
    call window_close

    scene black with wipeleft_scene
    play sound closet_open
    pause 0.25

    call window_open
    scene bg school literature_club board day with wipeleft_scene
    n "Йо, Юри!"
    n "Я пришла."
    "..."
    n "Юри?..."
    "..."
    "Где она?..."
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg school f3 new_corridor
    show sayori turned neut cm oe school_bag at i11
    mc "Кто это был?"
    show sayori curi om oe
    s "Глава школьного совета, если не ошибаюсь..."
    show sayori cm
    mc "Ничего себе..."
    show sayori neut cm oe
    mc "Моника с ней часто контактирует?"
    show sayori om b1d lup
    s "Она же глава клуба!"
    show sayori ldown
    s "Все главы клуба состоят в школьном совете."
    show sayori cm
    mc "А, ну да, точно."
    show sayori -b1d
    "Разбор вопросов финансирования, различных мероприятий, прочего..."
    show sayori e1b
    "Логично."
    show monika forward happ cm oe school_bag at t21
    show sayori happ cm oe at t22
    pause 0.2
    show monika om ce rhip
    m "Я снова с вами!"
    show monika cm
    show sayori om ce lup rup at h22
    s "Ура!"
    show monika oe rdown
    show sayori neut cm oe ldown rdown
    mc "Что-то важное сказали?"
    show monika om
    m "Нет, ничего такого."
    show monika nerv mb oe n2 at s21
    show sayori b1c
    m "Просто опять одна из наших участниц немножко нарушила школьный устав..."
    show monika cm e1a
    show sayori om
    s "Нацуки?"
    show monika mb
    show sayori cm
    m "...да."
    show monika neut cm oe n1 at t21
    show sayori -b1c
    mc "Подожди, это не та девушка, что сегодня по школе бегала от какого-то паренька во время большой перемены?"
    show monika happ om oe
    m "Ха, так ты её видел?"
    show monika cm
    mc "Я с ней прямо здесь столкнулся...{w}буквально."
    show monika neut om e2a
    show sayori flus cm oe
    m "Ох..."
    show monika cm
    show sayori om lup rup at h22
    s "Она тебя не ушибла?!"
    show monika oe
    show sayori neut cm oe
    mc "При её-то размерах?"
    show sayori ldown rdown
    mc "Меня больше волнует, что там между ней и тем учеником случилось."
    show monika om
    m "Надеюсь, ничего серьёзного."
    show monika happ om oe lpoint
    show sayori dist cm oe
    m "Но я с ней обязательно поговорю."
    show monika neut cm oe ldown
    show sayori om
    s "Вечно с Нацуки что-то происходит..."
    show sayori cm
    mc "Часто нарывается на неприятности?"
    show monika om e1b
    m "У неё немного своеобразный характер..."
    show monika oe
    show sayori neut cm oe
    m "Ой, это долго объяснять, как-нибудь потом."
    show monika lean happ om ce school_bag at h21
    show sayori happ cm oe
    m "...когда вступишь в наш клуб, естественно!"
    show monika cm
    show sayori ce
    mc "Пха-ха, я так и думал!"
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg club_day
    "Все парты выставлены идельно в ряд..."
    "Вот Юри делать нечего."
    pause 0.5
    play sound natsuki_sneeze
    pause 0.388
    with vpunch
    pause 0.8
    n "Фу!"
    "Откуда столько пыли?!"
    "Тут, кроме парт и кладовки, ничего больше не..."
    "Так."
    "СТОП!"
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg school f2 new_corridor
    show monika forward happ cm oe school_bag at i21
    show sayori turned happ cm ce school_bag at i22
    mc "Ребят, по-моему, мы делаем лишний зигзаг."
    show monika om oe
    m "Разве?"
    show monika neut cm oe
    mc "Возможно, я ошибаюсь, но в старый корпус можно попасть и через третий этаж."
    show monika happ cm oe
    show sayori om oe
    s "Мы привыкли ходить в клуб через второй, потому что...{w}он на втором этаже."
    show sayori cm
    mc "Ясненько..."
    show monika cm ce
    show sayori om ce
    s "Так что привыкай!"
    show monika cm oe
    show sayori cm ce
    mc "Звучит как приговор."
    show monika om ce lpoint rhip
    m "Учитывая наш весёлый коллектив, совершенно нет."
    show monika cm ce ldown

    scene black with wipeleft_scene
    s "А, ой..."
    m "Точно, здесь же проход в корпус перекрыт из-за ремонта, который устроили на днях..."
    m "Придётся всё-таки пойти через третий этаж, ха-ха!"
    mc "Мда-а..."
    "Будто они умышленно тянут время."
    "Лучше бы уже домой пришёл и домашнее задание стал разгребать, пока силы есть, честное слово."
    call window_close

    call window_dialog_fast_transition("n")

    $ renpy.music.set_volume(0.2, 0, "music")

    call window_open
    scene bg closet
    y "{size=19}И вот здесь...{/size}"
    y "{size=19}Фу-у-ух...{/size}"
    y "{size=19}Если бы полки не были забиты этой бестолковой мангой, то было бы в разы проще...{/size}"
    n "{sc=3}ЮРИ-И-И!!!{/sc}" with vpunch
    y "{size=19}А-А-А-А-А-А!{/size}"
    n "А ну-ка, выйди на свет, горничная с {s}оч{/s}умелыми ручками!"
    call window_close

    pause 1.0
    show yuri turned lsur cm oe at t11
    pause 1.0
    show yuri pout cm oe
    pause 0.5

    call window_open
    n "Что ты там творишь?!"
    show yuri om oe
    y "Протираю полки от пыли."
    show yuri cm oe
    n "ДА ТЫ ВСЮ МАНГУ ПЕРЕВОРОТИЛА!"
    n "Я замучаюсь её обратно в правильном порядке ставить!"
    show yuri om oe
    y "Она мне мешала."
    show yuri angr cm oe
    n "Зачем ты вообще залезла в кладовку?!"
    show yuri om oe
    y "Потому что кое-кому лень там убираться!"
    show yuri cm oe
    n "Зато ты у нас чистюля, сразу полезла без разрешения!"
    show yuri doub om ce
    y "С каких пор эта кладовка стала твоей собственностью?"
    show yuri pout cm oe
    n "С тех самых, когда там появилась моя манга!"
    show yuri om oe
    y "Кладовка всегда была общей, Нацуки."
    show yuri angr om oe
    y "А твоя глупая манга своим фактом существования никак не влияет на право собственности."
    show yuri cm oe
    n "Глупая?!"
    show yuri om oe
    y "Да, глупая."
    show yuri vang cm oe
    n "МАНГА -- ЛИТЕРАТУРА!!!"
    show yuri om oe
    y "Манга никогда не была литературой и не может ей стать априори!"
    show yuri cm oe
    n "ЛИТЕРАТУРА!!!"
    show yuri om oe
    y "Это целый кластер бездарных произведений на фоне НАСТОЯЩЕЙ литературы!"
    show yuri anno cm ce
    n "Бездарность -- это твоя уборка в кладовке!"
    show yuri om ce
    y "Как же..."
    show yuri angr om ce
    y "...ты..."
    show yuri vang om ce
    y "...меня..."
    show yuri yand om oe
    y "{sc=3}ДОСТАЛА!{/sc}"
    show yuri cm oe

    scene black with wipeleft_scene
    y "{sc=3}А НУ ИДИ СЮДА, ЗАСРАНКА МЕЛКАЯ!{/sc}"
    n "{sc=3}А-А-А-А-А-А!!!{/sc}"
    call window_close

    call window_dialog_fast_transition("mc")

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg school f3 old_corridor
    show monika forward happ cm oe school_bag at i22
    show sayori turned happ cm oe school_bag at i21
    pause 0.2
    show monika b1b n2
    show sayori lsur om oe at h21
    s "О, апельсиновый сок!"
    show monika om ce
    show sayori worr cm oe
    m "Сайори, давай попозже..."
    show monika om oe
    m "А то времени не останется."
    show sayori shoc cm oe
    show monika lean m2 e2 b1 n1 school_bag at t11
    m "{size=15}Я куплю его тебе в качестве награды, когда Макс станет частью нашего клуба!{/size}"
    show monika happ cm oe
    mc "Я всё слышал."
    show monika forward laug om ce school_bag at h11
    m "Ха-ха-ха!"
    show monika cm ce at t11
    show sayori om oe
    s "{size=15}Договорились.{/size}"
    show monika happ cm oe at t22
    show sayori nerv cm oe
    mc "{size=15}А мне купите?{/size}"
    show monika laug om ce rhip
    m "Сначала приведи нового участника в клуб, тогда и купим!"
    show monika cm ce
    show sayori laug cm ce
    mc "Ну, блин, я так не играю..."
    call window_close

    call window_dialog_fast_transition

    $ renpy.music.set_volume(0.2, 0, "music")

    play noise_2 natsuki_steps_run
    scene bg school literature_club board day:
        align (0.5, 0.5) anchor (0.5, 0.5) zoom 1.15
        parallel:
            easein 0.1 yoffset 20
            easeout 0.1 yoffset 0
            easein 0.1 yoffset -20
            easeout 0.1 yoffset 0
            repeat
        parallel:
            linear 0.5 zoom 1.65
            linear 1.0 zoom 2.95 xanchor 0.40
            linear 1.0 zoom 3.95 xanchor 0.43
            linear 1.0 zoom 5
    pause 2.5

    scene black with wipeleft_scene
    stop noise_2
    scene bg club_day with dissolve
    show yuri turned yand cm oe lup rup at movein_hugs
    pause 0.5
    play sound ram_attack
    scene white
    pause 0.1
    scene black
    show particle_star
    with dissolve
    pause 0.5

    call window_dialog_fast_transition

    $ renpy.music.set_volume(1.0, 0, "music")

    call window_open
    scene bg corridor
    show monika forward happ cm oe school_bag at i21
    show sayori turned happ cm ce school_bag at i22
    pause 0.2
    show monika om oe lpoint rhip
    show sayori cm oe
    m "Итак, друзья!"
    show monika ldown rdown
    show sayori cm ce
    m "Мы, наконец-то, пришли!"
    show monika cm ce
    show sayori om ce lup rup at h22
    s "Е-е-е!"
    show sayori cm ce ldown rdown
    mc "Да уж, пришли..."
    show monika om oe
    m "Что ж, Макс..."
    show monika lpoint
    show sayori cm oe
    m "Готов познакомиться с остальными членами Литературного клуба?"
    show monika cm oe
    show monika cm oe ldown
    mc "А у меня будто выбор есть?"
    mc "Конечно готов."
    stop music fadeout 1.5
    show monika om oe
    m "Тогда входим на счёт «три»..."
    play music t1 fadein 3.0
    $ quick_menu = False
    $ y_name = "???"
    $ n_name = "???"
    show monika vsur om ce
    show sayori nerv cm ce
    m "{cps=40}Раз...{/cps}{w=0.7}{nw}"
    m "{cps=40}Два...{/cps}{w=0.7}{nw}"
    show monika happ om ce
    show sayori laug cm ce
    m "{cps=40}Три!{/cps}{w=0.7}{nw}"
    show monika cm
    window hide

    scene black with wipeleft_scene
    play sound closet_open
    pause 0.1

    window auto
    scene bg school literature_club board day
    show monika forward happ cm oe school_bag at t43 zorder 2
    show sayori turned happ cm oe school_bag at t33
    with wipeleft_scene
    show monika om oe
    m "{cps=45}Ребята, мы--{/cps}{nw}"
    show monika pani om oe
    show sayori pani om oe
    y "{cps=75}МАНГА -- НЕ ЛИТЕРАТУРА!!!{/cps}{w=0.5}{nw}"
    window hide

    play sound hit
    show monika e4c at h43
    show sayori om ce at h33
    with vpunch
    pause 0.15
    play sound hit
    show monika at h43
    show sayori at h33
    with vpunch
    pause 0.15
    show monika om oe at lhide
    hide monika
    show sayori vsur om oe at lhide
    hide sayori

    $ quick_menu = True
    window auto
    queue music t3a
    m "{sc=3}ВЫ ЧТО ТВОРИТЕ?!{/sc}"
    s "{sc=3}РЕБЯТА, НЕ ССОРЬТЕСЬ!!!{/sc}"
    n "{sc=3}БОЛЬНО!!!{/sc}"
    y "{sc=3}ТАК ТЕБЕ И НАДО!!!{/sc}"
    n "{sc=3}ЗАТКНИ-И-ИСЬ!!!{/sc}"
    m "{sc=3}ЮРИ, НАЦУКИ, ХВАТИТ!!!{/sc}"
    $ y_name = _("Юри?")
    $ n_name = _("Нацуки?")
    y "{sc=3}ИЗДЕВАЕТЕСЬ?!{/sc}"
    s "{sc=3}Я ЗА ХОЛОДНЫМ, СЕЙЧАС!{/sc}"
    show sayori turned pani cm oe at t11 with easeinleft
    show sayori om
    s "МАКС, ТОТ СОК!"
    show sayori cm
    mc "Деньги?"
    show sayori om
    s "ДА!"
    show sayori cm
    mc "На."
    "Ей должно хватить этих несколько монет."
    show sayori om
    s "СПАСИБО!"
    show sayori cm at rhide
    hide sayori

    scene bg club_day with wipeleft_scene
    "Чёрт побери..."
    m "{size=19}Что произошло?!{/size}"
    "Этот клуб только что оправдал своё название."
    y "{size=19}ОНА МЕНЯ...{w}вывела из себя...{/size}"
    "Литературный?"
    n "{size=19}И чуть не убила!{/size}"
    "Вроде да, есть манга и стихи."
    m "{size=19}Это всё из-за этой кладовки, да?!{/size}"
    "«Доки-Доки?»"
    n "{size=19}Догадайся с трёх раз!{/size}"
    "Ровно два раза."
    m "{size=19}Перестаньте провоцировать друг друга!{/size}"
    m "{size=19}Посмотрите, во что это выливается!{/size}"
    y "{size=19}П-простите...{/size}"
    n "{size=19}Аргх!{/size}"
    s "{size=19}Я пришла!{/size}"
    s "{size=19}Нацуки, давай--{nw}{/size}"
    $ y_name = _("Юри")
    $ n_name = _("Нацуки")
    n "{size=19}Не надо...{/size}"
    s "{size=19}А?{/size}"
    s "{size=19}Почему?!{/size}"
    n "{size=19}Пусть это будет мне наказанием, всё равно лоб уже не болит...{/size}"
    m "{size=19}Ладно, всё, хватит вам, успокойтесь.{/size}"
    m "{size=19}Давайте лучше примем новенького!{/size}"
    y "{size=19}Он уже тут?!{/size}"
    s "{size=19}Мы же вместе с ним пришли.{/size}"
    n "{size=19}Классно, отличное начало...{/size}"
    m "{size=19}Не надо пессимизма, давайте уже действовать!{/size}"
    show yuri shy neut cm oe at t41
    show natsuki cross fs neut cm oe at t42
    show monika forward happ cm oe at t43
    show sayori turned happ cm ce at t44
    pause 0.2
    show monika om oe lpoint rhip
    m "Макс, добро пожаловать в Литературный клуб «Доки-Доки»!"
    show yuri om e1
    show natsuki ff curi om oe
    ny "{size=19}Макс?{/size}"
    show yuri cm
    show natsuki cm
    show monika om ce
    m "Меня и Сайори ты уже знаешь, так что познакомлю тебя с остальными участницами."
    show monika cm ce ldown rdown
    "Кажется, она сказала эту фразу больше для этих «остальных», чем для меня."
    show yuri oe
    show natsuki turned neut cm oe
    show monika om oe
    show sayori cm oe
    m "Итак, девушка с розовыми волосами -- Нацуки."
    show natsuki sedu cm ce lhip rhip
    show monika lpoint
    m "Она у нас энергичная и бойкая, а также творческая: в её стихах хорошо описываются простые вещи, при этом сохраняется серьёзный смысл!"
    show natsuki nerv cm oe ldown rdown at h42
    show monika cm ce ldown
    show sayori om ce lup rup at h44
    s "А ещё она любит печь вкусные кексы и кормить нас ими по особым случаям!"
    show natsuki om oe
    show sayori cm ce
    n "Сайори!"
    show sayori ldown rdown
    n "{size=19}Он же ещё не участник клуба...{/size}"
    show natsuki cm oe
    show monika cm oe
    mc "Ух ты..."
    "Бесплатная домашняя еда?"
    show natsuki curi cm oe
    "Я мало ел кексы в своей жизни, так что, если будет возможность, не откажусь попробовать."
    show natsuki anno om oe
    show sayori cm oe
    n "Не пялься так на меня."
    show natsuki cm oe
    "Так, да, я опять в себя ушёл."
    show natsuki neut cm oe
    show monika neut cm oe
    show sayori neut cm oe
    mc "Выходит, ты сегодня налетела на меня в коридоре, когда от кого-то убегала?"
    show natsuki om oe
    n "Пф, теперь ясно, в кого я врезалась..."
    n "А то я думаю, что лицо твоё слишком знакомое."
    show natsuki doub cm oe
    mc "У тебя всё уладилось?"
    show natsuki om oe lhip rhip
    show monika happ cm oe
    show sayori happ cm oe
    n "Сомневаешься?"
    show natsuki cm oe
    show monika cm ce
    mc "Нет."
    show natsuki ldown rdown
    show sayori cm ce
    "..."
    show natsuki dist cm oe
    "Сказать-то больше нечего."
    "Остаётся только классическое рукопожатие."
    show natsuki neut cm oe
    show monika cm oe
    show sayori cm oe
    mc "Макс."
    show natsuki happ om oe
    n "Рада приветствовать тебя в этом клубе, но..."
    show natsuki curi om oe lhip rhip
    n "...имя у тебя какое-то...{w}неяпонское..."
    show natsuki cm
    mc "Да родители назвали меня в честь одноимённой музыкальной группы."
    mc "Во второй половине 90-ых встретились на одном её концерте."
    show natsuki om e1b
    n "А-а..."
    show natsuki cm
    mc "Ладно, давайте не будем задерживаться."
    show natsuki neut cm oe ldown rdown
    show monika lean happ om oe at h43
    show sayori cm ce
    m "Хорошо!"
    show yuri n3
    show natsuki ma e1b
    show monika forward happ om oe rhip
    m "Последний участник -- девушка с лавандовыми волосами -- Юри!"
    show monika lpoint
    m "Она же, в свою очередь, довольно застенчивая и тихая -- не любит большое внимание."
    show yuri cm ce
    show monika om ce
    m "Но стоит ей приняться за любимое дело, как сразу становится страстной и решительной."
    show natsuki dist cm oe
    m "Любит читать книги и использовать различные приёмы в стихотворениях."
    show yuri e1 m1 b2
    show monika cm ce ldown rdown
    show sayori om ce
    s "Юри -- прирождённый поэт!"
    show yuri m4
    show sayori cm ce
    y "Л-ладно, хватит..."
    show yuri e3 m1
    show sayori om ce lup rup at h44
    s "И эксперт в области чая!"
    show yuri n5 at s41
    show sayori cm ce ldown rdown
    y "Угх..."
    show natsuki neut cm oe
    "Явно она неспроста такая скованная."
    "Ей пришлось пережить что-то очень негативное?"
    "Или увидеть этот негатив со стороны..."
    "В общем, без понятия, но что-то такое, вероятно, случилось в её жизни."
    "А ещё у неё проблемы со сдерживанием себя."
    show natsuki e1c
    "Ладно, хватит анализа, надо взять инициативу в свои руки, а то Юри явно дискомфортно."
    show yuri e1 b2 n3
    show monika cm oe
    show sayori cm oe
    mc "Макс."
    show yuri turned happ om oe lup rup at t41
    y "Добро пожаловать в Литературный клуб."
    show yuri cm ce
    mc "Благодарю."
    show yuri ldown rdown
    show natsuki e1a
    show monika om ce
    show sayori cm ce
    m "Прекрасно!"
    show yuri n1 cm oe
    show monika dist om ce
    show sayori neut cm oe
    m "Теперь, когда ты познакомился со всеми, мы зададим тебе один важный вопрос..."
    m "Поскольку ты и так от меня в курсе, чем мы здесь занимаемся..."
    show yuri lsur cm oe
    show natsuki lsur cm oe
    show monika neut om oe
    m "Ты вступишь к нам?"
    show monika cm oe
    "Скажите честно: как я могу воспринимать этот вопрос как реальный выбор после разговора с миссис Идой, переписки с Моникой и, судя по всему, её новостью про мой приход?"
    "Нет, ну если абстрагироваться от этого всего и взглянуть на вопрос со свободной позиции...{w}может, не всё так и плохо, как я думал."
    "Состав я уже знаю, людей мало, что хорошо."
    "Место тоже знаю."
    "Написание стихов?"
    "Не самое муторное, что может быть, в принципе."
    "Да и беря в расчёт, что абсолютно всё кричит мне вступить в этот клуб..."
    "Отказать этим девушкам после всех их приложенных усилий было бы откровенно свинством."
    show yuri laug cm oe
    show natsuki happ cm oe
    show monika laug cm oe
    show sayori laug cm oe
    mc "Хм, иначе говоря, каков мой положительный ответ?"
    show monika om ce
    m "Ха-ха-ха!"
    show yuri happ cm ce
    show natsuki cm ce
    show monika happ cm ce
    show sayori cm ce
    mc "Да, я вступаю в Литературный клуб."
    show natsuki pani cm ce at h42
    show monika laug cm ce
    show sayori yand om ce lup rup at h44
    s "УРА-А-А-А-А-А!!!" with vpunch
    show natsuki om oe
    show sayori laug cm ce ldown rdown
    n "Сайори, не ори!"
    show yuri om ce
    show natsuki nerv cm oe
    y "Хе-хе..."
    show yuri cm ce
    show natsuki happ cm oe
    show monika happ om oe
    show sayori happ cm oe
    m "Восхитительно!"
    show natsuki cm ce
    show monika lean happ om ce at h43
    show sayori cm ce
    m "Теперь в ближайшие дни мы получим статус официального школьного клуба!"
    show monika cm
    "Блин, я ещё толком ничего не сделал, а они уже все радостные."
    "Много ли надо людям для счастья?"
    show monika forward happ om oe lpoint
    m "Итак, друзья!"
    show yuri curi cm oe
    show natsuki curi cm oe
    show monika cm oe ldown
    show sayori curi cm oe
    nsy "???"
    show yuri happ cm oe
    show natsuki doub cm oe
    show monika lean happ om oe at h43
    show sayori happ cm oe
    m "Посколько мы в этом учебном году ещё не писали стихи, то предлагаю возобновить данное мероприятие!"
    show monika forward happ om oe lpoint rhip
    m "Как и в прошлые разы: придумываем от себя одно небольшое стихотворение, делимся друг с другом."
    show yuri laug cm oe
    show monika ldown
    m "Это поможет нам улучшить писательские навыки и интересно провести время как минимум."
    show natsuki om oe
    show monika curi cm oe rdown
    show sayori neut cm oe
    n "Мы и так в курсе."
    show natsuki neut cm oe
    show monika om oe
    m "Но Макс-то нет."
    show natsuki dist cm oe
    show monika happ cm oe
    show sayori happ cm oe
    mc "Я догадывался."
    show yuri om oe lup
    y "Можно снова попробовать, у меня есть несколько идей..."
    show yuri cm oe ldown
    show sayori om ce rup lup at h44
    s "Да, давайте!"
    show natsuki om ce
    show monika cm ce
    show sayori cm ce ldown rdown
    n "Окей, пару раз что-то написать да можно."
    show yuri happ cm oe
    show natsuki neut cm oe
    show monika om oe lpoint
    show sayori cm oe
    m "А что насчёт тебя, Макс?"
    show monika cm oe ldown
    mc "В принципе, я был к этому морально готов."
    show natsuki sedu cm oe
    mc "Поэт из меня никакущий, но посмотрим, что получится."
    show yuri cm ce
    show natsuki happ cm oe
    show monika om ce
    show sayori cm ce
    m "Договорились!"
    show natsuki neut cm oe
    show monika om oe
    m "Сегодня мы ничего проводить не будем, так что можете прямо сейчас идти по домам."
    show yuri cm oe
    show monika lean happ om oe at h43
    m "Жду вас завтра после уроков с плодами вашего творческого самовыражения!"
    show yuri curi cm oe
    show natsuki om oe
    show monika forward curi cm oe
    show sayori neut cm oe
    n "Можно нам с Юри немного здесь задержаться?"
    show natsuki cm oe
    show monika om oe
    m "Кстати, да, ты мне нужна, Нацуки, по одному вопросу..."
    m "...но зачем ты хочешь остаться с Юри?"
    show yuri sad cm oe
    show natsuki dist om oe
    show monika neut cm oe
    n "Хочу прибраться в кладовке и вернуть всё в изначальный вид..."
    show yuri lsur cm oe
    n "А Юри мне в этом поможет."
    show natsuki curi om oe
    n "Да, Юри?"
    show yuri flus cm oe
    show natsuki cm oe
    y "Умф...{w}угу."
    show monika om ce
    m "Хорошо."
    show yuri laug cm oe
    show natsuki happ cm oe
    show monika happ om oe
    m "Тогда сначала я помогу вам, а потом разберёмся с вопросом."
    show natsuki om oe
    show monika cm oe
    n "Идёт."
    show yuri at thide
    hide yuri
    show natsuki cm oe at thide
    hide natsuki
    show monika om oe lpoint
    show sayori happ cm oe
    m "Сайори, Макс, вы можете идти."
    show monika cm oe ldown
    show sayori om ce lup rup at h44
    s "Ок-ке!"
    show sayori cm ce ldown rdown
    mc "До завтра."
    stop music fadeout 3.0
    call window_close

    scene black with wipeleft_scene
    pause 0.5
    play sound closet_open
    pause 1.0

    call window_open
    scene bg corridor
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    mc "Ух-х-х..."
    "Что-то я утомился."
    mc "Кстати, Сайори..."
    show sayori cm oe
    s "М-м-м?"
    mc "Выходит, ты всё-таки получила свой заслуженный сок?"
    show sayori tap nerv om oe school_bag at s11
    s "Э-хе-хе~"
    show sayori ce
    stop noise_1 fadeout 2.0
    call window_close

    call plot_transition

    call window_open
    play noise_1 street_suburban_noise fadein 3.0
    scene bg niigata street suburban 10 afternoon
    show sayori turned happ cm ce school_bag at t11
    with wipeleft_scene
    show sayori neut cm oe
    mc "А часто у вас Юри и Нацуки грызутся между собой?"
    show sayori worr om oe
    s "Нет, нечасто."
    s "При этом они в основном мирятся."
    s "Хотя, чтобы этого добиться, приходится вмешиваться, особенно Монике."
    show sayori neut cm oe
    mc "Ну, смею предположить, что Юри много терпит, из-за чего потом срывается, а Нацуки сама иногда провоцирует."
    show sayori sad om oe
    s "Да, Юри робкая и закрытая, редко делится переживаниями."
    show sayori lup
    s "Даже несмотря на нашу уютную атмосферу и поддержку, она всё равно полностью не раскрывается."
    show sayori ldown rup
    s "А Нацуки стала «острой» из-за своего отца."
    show sayori worr om oe rdown
    s "Часто перегибает палку, хотя старается так не делать."
    show sayori neut cm oe
    mc "Да уж, тут бы психолог помог..."
    show sayori happ om ce lup rup at h11
    s "Мы и сами своего рода психологи!"
    show sayori cm ce ldown rdown
    "Есть в её словах доля правды..."
    "Вот только доля."
    "..."
    "Короче, весёлый состав, ничего не скажешь."

    scene bg house
    show sayori turned happ cm oe school_bag at t11
    with wipeleft_scene
    show sayori om oe
    s "Спасибо, что проводил в очередной раз!"
    show sayori cm ce
    mc "Пожалуйста."
    show sayori laug om oe
    s "Только не забудь сегодня написать стих!"
    show sayori cm oe
    mc "Само собой."
    show sayori happ om ce
    s "Всё, до завтра!"
    show sayori cm ce
    mc "Удачи."
    call window_close
    show sayori at thide
    hide sayori
    pause 1.0
    stop noise_1 fadeout 2.0

    call plot_transition

    call window_open
    scene bg bedroom with wipeleft_scene
    "Домашнее задание сделал, на завтра всё собрал..."
    "И даже добавил заметку на этот день в календарь."
    window hide

    python in phone.calendar:
        add_description(
            char_key = "mc",
            index_calendar = 0,
            index_day = 16,
            description = "Сегодня я вступил в Литературный клуб. Не знаю, во что это выльется и как долго я в нём продержусь, но пока он мне нравится. На полном серьёзе. Правда, придётся теперь писать стихи на пару с домашней работой..."
        )

    python in phone.system:
        battery_level = 74
        clock = (18, 38)

    show screen phone_calendars() with Dissolve(0.5)
    $ plot_pause()
    hide screen phone_calendars with Dissolve(0.5)

    window auto
    "«Знаменательное» событие всё-таки."
    mc "Уф-ф-ф..."
    "Какие же у Литературного клуба своеобразные участники..."
    "Батарейка с энергией термоядерного синтеза Солнца, розоволосовое миниатюрное нечто с характером, лавандовая хрупкая статуя с бюстом и «идеальный» образ девушки..."
    mc "Куда я, блин, попал?..."
    "Нет, я в заметке написал, что мне нравится клуб."
    "Пока что нравится."
    "Надеюсь, что и впредь..."
    "На что тут вообще возмущаться?"
    "Даже такому отстранённому, как мне?"
    "4 красивые девушки, спокойный корпус, все меня знают, я всех знаю."
    "Мне откровенно повезло с клубом."
    "Однако никакие любовные отношения с кем-то из участниц я строить не намерен."
    "Не из разряда понтов, а-ля, какой я сильный и независимый..."
    "А потому что не готов к такой ответственности."
    "Ха, кто-то бы сказал: \"Ты что, дурак?\""
    "А я бы ответил: \"Да. Вопросы?\""
    "Не, ну честно: какие, к чёрту, серьёзные отношения в таком возрасте?"
    "У меня нет собственного жилья на постоянке."
    "У меня нет работы и должного самостоятельного материального обеспечения."
    "У меня нет ещё даже среднего образования."
    "У меня нет ни желания, ни мотивации, ни сил этим заниматься, в конце концов."
    "Отношения для меня будут лишь ещё одной проблемой в жизни, которая в любом случае породит множество других."
    "Блин, да никто мной даже не интересовался, кроме Сайори и Моники, за всю короткую и бестолковую жизнь."
    "Да и те только в плане общения..."
    "Как другие умудряются крутить романы и вечно с кем-то засасываться на людях?"
    "Фу, нахрен, аж противно."
    "Вероятно, все делают это на пофиг, не задумываясь ни о каких последствиях."
    "А потом измены, алименты, прочее дерьмо, а как так, а почему, а я его любил/любила, сопли, слюни..."
    "Идиотизм."
    "Ой, всё, проехали, хватит тратить время на эту хрень, у меня его и так мало."
    "Мне же теперь надо стихи клепать."
    "Так что ручку в руки и...{w}о чём писать?"
    "..."
    "У меня вообще нет идей."
    "Нужно что-то такое, чтобы это звучало лаконично."
    "А ещё чтобы не опозорится при демонстрации..."
    "..."
    mc "Блин, не знаю."
    "..."
    mc "А может..."
    "Если попробовать цепляться за ключевые слова?"
    "К примеру, появится в мыслях первое, попытаюсь из него что-то сделать, потом второе, которое я скомпоную с первым, потом третье и так далее..."
    "В теории звучит интересно."
    "А вот на практике?"
    "Эх, не попробуешь -- не узнаешь."
    "Приступим..."

    call poem_act_1_day_1

    scene bg bedroom with dissolve_scene_half
    call show_poem(poem_mc1, music=False)
    "Ну и фуфло."
    "Нет, к чёрту, я не буду это переписывать."
    "У меня так времени не останется."
    "Да и мозги во всю плывут..."
    "Надо отдохнуть..."
    call window_close

    return
