init -100 python in phone.calendar:
    from renpy import store
    from store import _, At, _fits, phone
    from store.phone import system, config
    import calendar

    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY = calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY
    SATURDAY, SUNDAY = calendar.SATURDAY, calendar.SUNDAY

    days = ( _("Понедельник"), _("Вторник"), _("Среда"), _("Четверг"), _("Пятница"), _("Суббота"), _("Воскресенье") )

    months = (_("январь"), _("февраль"), _("март"), _("апрель"), _("май"), _("июнь"), _("июль"), _("август"), _("сентябрь"), _("октябрь"), _("ноябрь"), _("декабрь"))

    renpy.const("phone.calendar.MONDAY")
    renpy.const("phone.calendar.TUESDAY")
    renpy.const("phone.calendar.WEDNESDAY")
    renpy.const("phone.calendar.THURSDAY")
    renpy.const("phone.calendar.FRIDAY")
    renpy.const("phone.calendar.SATURDAY")
    renpy.const("phone.calendar.SUNDAY")
    renpy.const("phone.calendar.days")
    renpy.const("phone.calendar.months")

    class _Day(object): # object просто указан явно (наследуется автоматически)
        def __init__(self, index):
            self.index = index
            self.description = None

    class Calendar(calendar.Calendar):
        def __init__(self, first_day, month, year):
            super(Calendar, self).__init__(first_day)

            self.month = month
            self.month_name = months[month - 1]
            self.year = year

            self.__days = [ ]
            self.start_offset = self.end_offset = 0

            end = False
            for index_day in self.itermonthdays(year, month): # из модуля calendar
                if index_day == 0: # день-заполнитель для выравнивания календаря (пример: месяц со вторника -> понедельник - заполнитель)
                    self.__days.append(None)
                    if end:
                        self.end_offset += 1
                    else:
                        self.start_offset += 1
                else:
                    self.__days.append(_Day(index_day))
                    if not end:
                        end = True # начальные пустые дни пройдены, остались только в конце

        def lenght(self, offsets=False):
            if offsets:
                return len(self.__days)
            return self.lenght(True) - self.end_offset - self.start_offset

        def get_week_days(self):
            return get_week_days(self.firstweekday)

        @property
        def rows(self):
            return self.lenght(True) // 7

        def clear(self):
            for day in self.__days:
                if day:
                    if desc := day.description:
                        desc = None

        def __getitem__(self, i):
            return self.__days[self.start_offset:self.lenght(True) - self.end_offset][i - 1]

        def __iter__(self):
            return iter(self.__days)

    def get_week_days(first_day=SUNDAY):
        for i in range(first_day, 7):
            yield days[i]
        for i in range(0, first_day):
            yield days[i]

    def day_name(year, month, day):
        return days[calendar.weekday(year, month, day)]

    def add_calendar(calendar, key=None):
        if renpy.is_init_phase():
            phone._run_on_start(renpy.partial(add_calendar, calendar, key), ("_phone_add_calendar", calendar.month, calendar.year, key))
        else:
            key = character.character(key).key

            if get_calendar(year=calendar.year, month=calendar.month, key=key) is not None:
                raise Exception(f"a calendar for the year {calendar.year} and month {calendar.month} already exists for the *character* {key}")

            calendars = store.phone.data[key]["calendars"]
            calendars.append(calendar)
            calendars.sort(key=lambda c: (c.year, c.month))

    def add_calendar_to_all_characters(calendar):
        if renpy.is_init_phase():
            phone._run_on_start(renpy.partial(add_calendar_to_all_characters, calendar), ("_phone_add_calendar", calendar.month, calendar.year))
        else:
            l = calendar.lenght(False)

            for key in character._characters:
                _calendar = Calendar(calendar.firstweekday, calendar.month, calendar.year)
                for i in range(l):
                    _calendar[i].description = calendar[i].description

                add_calendar(_calendar, key)

    def add_description(char_key, index_calendar, index_day, description):
        phone.data[char_key]["calendars"][index_calendar][index_day].description = description

    _calendar_button_background = At(config.basedir + "circle.png", store._fits(None))

    def get_calendar(year, month, key=None):
        key = character.character(key).key
        for calendar in data[key]["calendars"]:
            if calendar.year == year and calendar.month == month:
                return calendar
        return None


screen phone_calendars():
    default calendars = phone.data[pov_key_mobile]["calendars"]
    default calendars_lenght = len(calendars) - 1
    default calendars_current = 0 # номер календаря в списке персонажа (0 - апрель у ГГ) (изменить в будущем вместе с phone.calendar.current_day)
    default selected_day = None

    $ calendar = calendars[calendars_current]

    use _phone():
        style_prefix "phone_calendar"

        side "t c":
            use app_base():
                style_prefix "app_base"
                text _("Календарь") xalign 0.5 text_align 0.5

            grid 7 calendar.rows + 1 xalign 0.5:
                for day in calendar.get_week_days():
                    if day in phone.calendar.days[1:3]:
                        text day[:2] style "phone_calendar_days_text"
                    else:
                        text day[0:3:2] style "phone_calendar_days_text"

                for day in calendar:
                    if day is None:
                        null width gui.phone_calendar_button_size
                    else:
                        button:
                            if day.index == phone.calendar.current_day[0]:
                                background Transform("phone/assets/circle_calendar_day_now.png", subpixel=True, fit="contain")
                            hover_background Transform(phone.calendar._calendar_button_background, matrixcolor=TintMatrix("#d4d4d4"))
                            selected_background Transform(phone.calendar._calendar_button_background, matrixcolor=TintMatrix("#5cadff"))
                            action (
                                If(selected_day is not day,
                                       SetScreenVariable("selected_day", day),
                                       SetScreenVariable("selected_day", None)
                                ),
                                SelectedIf(selected_day is day)
                            )

                            text str(day.index) style "phone_calendar_button_text"

                            if day.description is not None:
                                frame style "empty" align (1.0, 0.0) xysize (16, 16):
                                    background Transform(phone.calendar._calendar_button_background, matrixcolor=TintMatrix("#8f8f8fff"))
                                    text "i" style "phone_calendar_button_text_special":
                                        at transform:
                                            subpixel True

        vbox style_prefix "phone_calendar_notes" yalign 1.0:
            spacing 5

            side "l c r" xalign 0.5:
                textbutton "<":
                    action (
                        If(calendars_current != 0,
                            (
                                SetScreenVariable("calendars_current", calendars_current - 1),
                                SetScreenVariable("selected_day", None)
                            )
                        )
                    )

                text _("[calendar.year] год, [calendar.month_name]"):
                    size 25 xalign 0.5 text_align 0.5

                textbutton ">":
                    action (
                        If(calendars_current != calendars_lenght,
                            (
                                SetScreenVariable("calendars_current", calendars_current + 1),
                                SetScreenVariable("selected_day", None)
                            )
                        )
                    )

            frame:
                vbox at Flatten:
                    spacing 3

                    text _("Заметка:") size 22

                    null height 3

                    viewport:
                        draggable True mousewheel True

                        if selected_day is not None:
                            if selected_day.description is None:
                                text _("Нет заметки.")
                            else:
                                text selected_day.description

style phone_calendar_side is empty:
    yfill True xfill True

style phone_calendar_grid is empty:
    spacing 10

style phone_calendar_button is empty:
    xysize (gui.phone_calendar_button_size, gui.phone_calendar_button_size)

style phone_calendar_button_text is empty:
    color "#000"
    outlines []
    size 16
    align (0.5, 0.5) text_align 0.5
    font phone.config.basedir + "fonts/tahoma.ttf"

style phone_calendar_button_text_special is phone_calendar_button_text:
    size 12

style phone_calendar_days_text is phone_calendar_button_text:
    size 17

style phone_calendar_notes_side is empty:
    xsize 0.9 xfill True

style phone_calendar_notes_text is empty:
    font phone.config.basedir + "fonts/tahoma.ttf"
    color "#000" outlines []
    size 17

style phone_calendar_notes_button is empty:
    yalign 0.5
style phone_calendar_notes_button_text is phone_calendar_notes_text:
    size 21

style phone_calendar_notes_frame is empty:
    background "#e0e0e0"
    padding (13, 7, 13, 0)
    xfill True ysize 180

style phone_calendar_notes_vbox is empty:
    xfill True

init -50 python in phone.calendar:
    from store.phone import character

init python in phone:
    renpy_config.start_callbacks.append(lambda: setattr(calendar, "data", data))
