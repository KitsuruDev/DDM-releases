## script.rpy

label start:
    
    $ renpy.save_persistent() # для окончательного сохранения режима цензуры и прочего

    if not persistent.seen_based_menu:
        $ persistent.seen_based_menu = True

    $ style.say_dialogue = style.normal

    $ config.allow_skipping = allow_skipping = True


    python:
        for char_key in contact_list:           # очистка списка всех контактов у каждого (для отображения в интерфейсе)
            if mass := contact_list[char_key]:
                mass.clear()

        for chat_key in phone.group_chat._group_chats:
            if obj := phone.group_chat._group_chats[chat_key]: # очистка историй ВСЕХ чатов
                obj.clear()

        for char_key in phone.data:
            if mass := phone.data[char_key]['call_history']:   # очистка всех звонков у каждого
                mass.clear()
            if calendars := phone.data[char_key]['calendars']: # очистка всех записей в календаре у каждого
                for days in calendars:
                    days.clear()


    if persistent.secret_monikammm_complite and not persistent.secret_monikammm_complite_rofl:
        call monika_after_secret_monikammm_script
        $ persistent.secret_monikammm_complite_rofl = True
        $ renpy.save_persistent()
    else:
        stop music fadeout 3.0

        if not config.developer:
            show white

            call screen fake_loading(
                (1, 4),
                "new_game",
                "Doki Doki Метанойя",
                0,
                ("mc", 0)
            )

            hide white with dissolve


    ############# ПРОЛОГ - 2018 год, 2-3 апреля #############

    $ episode = _("Пролог\nДень 1")
    $ save_name = episode.replace('\n', '. ')
    call prologue_day_1 # Второй день идёт сразу после первого


    ############# АКТ 1 - 2018 год, 16-29 апреля #############

    ## Неделя 1

    $ episode = _("Акт 1 «Новая жизнь»\nДень 1")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_1

    $ episode = _("Акт 1 «Новая жизнь»\nДень 2")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_2

    $ episode = _("Акт 1 «Новая жизнь»\nДень 3")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_3

    $ episode = _("Акт 1 «Новая жизнь»\nДень 4")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_4

    $ episode = _("Акт 1 «Новая жизнь»\nДень 5")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_5

    $ episode = _("Акт 1 «Новая жизнь»\nДень 6")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_6

    $ episode = _("Акт 1 «Новая жизнь»\nДень 7")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_7

    ## Неделя 2

    $ episode = _("Акт 1 «Новая жизнь»\nДень 8")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_8

    $ episode = _("Акт 1 «Новая жизнь»\nДень 9")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_9

    $ episode = _("Акт 1 «Новая жизнь»\nДень 10")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_10

    $ episode = _("Акт 1 «Новая жизнь»\nДень 11")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_11

    $ episode = _("Акт 1 «Новая жизнь»\nДень 12")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_12

    $ episode = _("Акт 1 «Новая жизнь»\nДень 13")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_13

    $ episode = _("Акт 1 «Новая жизнь»\nДень 14")
    $ save_name = episode.replace('\n', '. ')
    call act_1_day_14

    if persistent.secret_monika <= 3:
        call before_credits

    call mod_credits

    return


########## ТЕХНИЧЕСКИЕ СКРИПТЫ ##########

label autosave:
    python:
        autosave_number = autosave_number % 6 + 1
        renpy.save(f"auto-{autosave_number}", save_name)
    return


label skip_block_on:
    $ config.allow_skipping = False
    $ config.skipping = False
    return

label skip_block_off:
    $ config.allow_skipping = True
    return


label window_close:
    window hide
    $ quick_menu = False
    return

label window_open:
    $ quick_menu = True
    window auto
    return


label window_dialog(character_key, multiple = False):
    python:
        if not multiple:
            pov_key = pov_key_mobile = character_key
            default_mouse = "default" if character_key == "mc" else character_key
        else:
            pov_key = default_mouse = character_key
    return

label window_dialog_fast_transition(character_key = None):
    play sound narrative_changing
    if character_key:
        call window_dialog(character_key)
    pause 0.382
    scene white with dissolve
    return

label window_dialog_long_transition(character_key = None, transition = True):
    scene black
    if transition:
        with dissolve_scene_full
    pause 1.0
    show expression "mod_assets/elements/mod_gui/load/sign/[pov_key].png" as loading_sign at loading_sign_position with dissolve
    pause 5.0
    hide loading_sign with dissolve
    pause 0.25
    if character_key:
        call window_dialog(character_key)
    return


label plot_transition(different_scene = True):
    scene black
    if different_scene:
        with wipeleft_scene
    else:
        with wiperight
    pause 0.25
    show expression "mod_assets/elements/mod_gui/load/sign/[pov_key].png" as loading_sign at loading_sign_position with dissolve
    play sound seconds
    pause 2.792
    hide loading_sign with dissolve
    pause 0.25
    return


label phone_status_bar_button(name, disable = False):
    python:
        if name == 'cellular_data':
            phone.system.cellular_data_lock = False
            while phone.system.cellular_data == disable:
                plot_pause()
            phone.system.cellular_data_lock = True
        else:
            phone.system.wifi_lock = False
            while phone.system.wifi == disable:
                plot_pause()
            phone.system.wifi_lock = True
    return


########## ТЕСТОВЫЕ СКРИПТЫ ##########

label test_phone:
    window hide

    $ phone.system.cellular_data_lock = False

    show screen phone() with Dissolve(0.5)

    call phone_status_bar_button('cellular_data', disable = False)

    $ plot_pause()
    hide screen phone with Dissolve(0.5)

    $ phone.system.cellular_data_lock = True

    window auto
    return
