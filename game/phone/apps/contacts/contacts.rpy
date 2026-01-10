screen phone_contacts():
    default group_chats = phone.data[pov_key_mobile]["group_chats"]
    default contacts = contact_list[pov_key_mobile]

    use _phone():
        style_prefix "phone_contacts"

        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Чаты") xalign 0.5 text_align 0.5

            if not group_chats:
                text _("Список пуст") style "phone_contacts_no_friends" align (0.5, 0.05)

            else:
                viewport:
                    draggable True
                    mousewheel True
                    yfill True

                    frame:
                        vbox:
                            for i, gc in enumerate(group_chats):
                                $ group_chat = phone.group_chat.group_chat(gc)

                                if group_chat.key in contacts:
                                    if i != 0:
                                        add Solid("#000"):
                                            xysize (1.0, 1) nearest True

                                    button:
                                        action (
                                            SetField(phone.discussion, "_group_chat", group_chat),
                                            SetField(group_chat, "unread", False),
                                            PhoneMenu("phone_discussion")
                                        )

                                        hbox:
                                            add group_chat.icon at _fits(46) yalign 0.5

                                            fixed:
                                                text group_chat.name yalign 0.2

                                                text _("[group_chat._date_text] в [group_chat._hour_text]"):
                                                    style "phone_contacts_date_text" yalign 1.0
                                                    font phone.config.basedir + "fonts/tahoma.ttf"

style phone_contacts_side is empty:
    xfill True
    yfill True

style phone_contacts_frame is empty:
    padding (10, 0, 10, 0)

style phone_contacts_vbox is empty:
    xfill True
    spacing 0

style phone_contacts_button is empty:
    xfill True
    hover_background Solid("#e4e4e4")
    ysize 60
    padding (10, 7)

style phone_contacts_hbox is empty:
    spacing 6

style phone_contacts_text is empty:
    outlines [ ]
    color "#525252"
    size 18
    font phone.config.basedir + "fonts/hack.ttf"

style phone_contacts_no_friends is phone_contacts_text:
    color "#000"
    size 20

style phone_contacts_date_text is phone_contacts_text:
    color "#9d9d9d"
    size 14
