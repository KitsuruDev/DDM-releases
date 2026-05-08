## gallery_cg.rpy

default persistent.gallery_lock_imgs = {}

init -1 python in GalleryCG:
    from store import persistent, config, Transform, Hide
    from io import BytesIO
    import os, pygame

    dict, current = {}, None

    def unlock_all():
        for name in persistent.gallery_lock_imgs:
            persistent.gallery_lock_imgs[name]["unlocked"] = True
            dict[name].unlocked = True

    def next(back=False):
        global current, dict
        keys_unlocked = [k for k, v in dict.items() if v.unlocked] # всегда, иначе: заполнение -> фиксация -> открытие новой CG -> она не в списке
        index_current = keys_unlocked.index(current)
        index_next = index_current - 1 if back else index_current + 1
        try:               current = keys_unlocked[index_next]
        except IndexError: current = keys_unlocked[0]

    class GalleryCGImage:
        def __init__(self, name, timeline, place, description, artist, image_show, image_export):
            self.name = name
            self.place = place
            self.description = description
            self.artist = artist
            self.timeline = timeline
            self.image_show = Transform(image_show, size=(config.screen_width, config.screen_height))
            self.small_size = Transform(image_show, size=(400, 225), crop=(0, 0, 1280, 720))
            self.image_export = image_export

            if self.name not in persistent.gallery_lock_imgs:
                persistent.gallery_lock_imgs[self.name] = { "unlocked": False }

            self.unlocked = persistent.gallery_lock_imgs[self.name]["unlocked"]
            dict[self.name] = self

        def unlock(self):
            self.unlocked = True
            persistent.gallery_lock_imgs[self.name]["unlocked"] = True

        def export(self):
            if self.image_export:
                if not os.path.exists(config.basedir + "/export_gallery_cg"):
                    try: os.mkdir(config.basedir + "/export_gallery_cg")
                    except: pass

                try:
                    output_surface = pygame.Surface((1280, 720), pygame.SRCALPHA) # SRCALPHA включает поддержку прозрачности

                    if isinstance(self.image_export, tuple):
                        for img_path in self.image_export:
                            f = renpy.file(img_path)
                            image_data = f.read()
                            f.close()
                            output_surface.blit(pygame.image.load(BytesIO(image_data)), (0, 0))
                    else:
                        f = renpy.file(self.image_export)
                        image_data = f.read()
                        f.close()
                        output_surface.blit(pygame.image.load(BytesIO(image_data)), (0, 0))

                    pygame.image.save(
                        output_surface, os.path.join(config.basedir, "export_gallery_cg", self.name + ".png"
                    ).replace("\\", "/"))

                    message_var = _("Сцена (CG) успешно экспортирована в папку \"export_gallery_cg\".")
                    chibi_var = ("s_chibi hop", 117)

                except Exception as e:
                    message_var = _(f"Не удалось экспортировать сцену (CG) из-за ошибки: {e}")
                    chibi_var = ("s_chibi turned mt ce", 117)

            else:
                message_var = _(f"Не удалось экспортировать сцену (CG) из-за сложных эффектов и\nпозиционных параметров спрайтов.")
                chibi_var = ("s_chibi turned mt ce", 100)

            renpy.show_screen(
                "extra_screen_help",
                message = message_var,
                ok_action = Hide("extra_screen_help"),
                chibi = chibi_var[0],
                chibi_pos = chibi_var[1]
            )


init python:
    cg_timeline_act_1 = _("Акт 1 \"Новая жизнь\". День")

    cg_a1_d1_y = GalleryCGImage(
        name = "cg_a1_d1_y",
        timeline = f"{cg_timeline_act_1} 1",
        place = _("Лестница старого корпуса школы"),
        description = _("Юри читает «Портрет Маркова» в любимом месте в компании Нацуки."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "y_cg2_bg", (0, 0), "y_cg2_base", (0, 0), "y_cg2_nochoc", (0, 0), "y_cg2_details", (0, 0), "y_cg2_dust1", (0, 0), "y_cg2_dust2", (0, 0), "y_cg2_dust3", (0, 0), "y_cg2_dust4"),
        image_export = ("images/cg/y_cg2_bg1.png", "images/cg/y_cg2_base.png", "images/cg/y_cg2_nochoc.png", "images/cg/y_cg2_details.png", "images/cg/y_cg2_dust1.png", "images/cg/y_cg2_dust2.png", "images/cg/y_cg2_dust3.png", "images/cg/y_cg2_dust4.png")
    )

    cg_a1_d2_y = GalleryCGImage(
        name = "cg_a1_d2_y",
        timeline = f"{cg_timeline_act_1} 2",
        place = _("Литературный клуб"),
        description = _("Юри читает «Портрет Маркова» вместе с Максом во время ожидания обмена стихами."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = "y_cg1_base",
        image_export = "images/cg/y_cg1_base.png"
    )

    cg_a1_d4_n_1 = GalleryCGImage(
        name = "cg_a1_d4_n_1",
        timeline = f"{cg_timeline_act_1} 4",
        place = _("Кладовка Литературного клуба"),
        description = _("Нацуки ставит лимитированную коробку с мангой на полку под присмотром Макса."),
        artist = _("Художник -- Satchely из Team Salvato\nУсталое выражение лица -- Sundeer🍨#6114 (Discord, старый ник)"),
        image_show = Composite((1280, 720), (0, 0), "n_cg2_bg", (0, 0), "n_cg2_base"),
        image_export = ("images/cg/n_cg2_bg.png", "images/cg/n_cg2_base.png")
    )

    cg_a1_d4_n_2 = GalleryCGImage(
        name = "cg_a1_d4_n_2",
        timeline = f"{cg_timeline_act_1} 4",
        place = _("Литературный клуб"),
        description = _("Нацуки увлечённо рассказывает Максу сюжет манги."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "n_cg1_bg", (0, 0), "n_cg1_base"),
        image_export = ("images/cg/n_cg1_bg.png", "images/cg/n_cg1_base.png")
    )

    cg_a1_d5_night_s = GalleryCGImage(
        name = "cg_a1_d5_night_s",
        timeline = f"{cg_timeline_act_1} 5",
        place = _("Спальня Сайори"),
        description = _("Давно погибший от собственных рук образ Сайори в кошмаре Макса."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "s_kill_bg_zoom", (0, 0), "s_kill_zoom", (0, 0), "s_kill_zoom_trans", (0, 0), Transform("noise", alpha=0.25), (0, 0), Transform("vignette", alpha=0.75)),
        image_export = None
    )

    cg_a1_d6_s_1 = GalleryCGImage(
        name = "cg_a1_d6_s_1",
        timeline = f"{cg_timeline_act_1} 6",
        place = _("Спальня в доме Сайори"),
        description = _("Сайори лежит в кровати спустя день после конфликта в Литературном клубе."),
        artist = _("Художник -- staticquit#8020 (Discord, старый ник)"),
        image_show = "sayori_cg_act_1_day_6",
        image_export = "mod_assets/cg/main_history/act_1/day_6/s.png"
    )

    cg_a1_d6_s_2 = GalleryCGImage(
        name = "cg_a1_d6_s_2",
        timeline = f"{cg_timeline_act_1} 6",
        place = _("Перед домом Сайори"),
        description = _("Макс выслушивает Сайори и успокаивает её после конфликта в Литературном клубе."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = "s_cg3",
        image_export = "images/cg/s_cg3.png" # развернуть при этом коде невозможно
    )

    cg_a1_d7_n = GalleryCGImage(
        name = "cg_a1_d7_n",
        timeline = f"{cg_timeline_act_1} 7",
        place = _("Кухня в доме Макса"),
        description = _("Макс схватил Нацуки во время проверки глазури на кислость."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "n_cg3_base", (0, 0), "n_cg3_cake", (0, 0), "n_cg3_exp1"),
        image_export = ("images/cg/n_cg3_base.png", "images/cg/n_cg3_cake.png", "images/cg/n_cg3_exp1.png")
    )

    cg_a1_d7_cup = GalleryCGImage(
        name = "cg_a1_d7_n",
        timeline = f"{cg_timeline_act_1} 7",
        place = _("Кухня в доме Макса"),
        description = _("Испечённые кексы для празднования воссоединения Литературного клуба."),
        artist = _("Редактирование -- KitsuruDev (использованы свободные изображения)"),
        image_show = "cupcakes_cg_act_1_day_7",
        image_export = "mod_assets/cg/main_history/act_1/day_7/cup.png"
    )

    cg_a1_d8_s = GalleryCGImage(
        name = "cg_a1_d8_s",
        timeline = f"{cg_timeline_act_1} 8",
        place = _("Литературный клуб"),
        description = _("Макс поправляет одежду Сайори во время ожидания чаепития."),
        artist = _("Художник -- Satchely из Team Salvato\nРадостное выражение лица и закрытые глаза -- Reitanna"),
        image_show = Composite((1280, 720), (0, 0), "s_cg1_base", (0, 0), "s_cg1_exp1"),
        image_export = ("images/cg/n_cg3_base.png", "images/cg/n_cg3_cake.png", "images/cg/n_cg3_exp1.png")
    )

    cg_a1_d10_night_n_1 = GalleryCGImage(
        name = "cg_a1_d10_night_n_1",
        timeline = f"{cg_timeline_act_1} 10",
        place = _("Кладовка Литературного клуба"),
        description = _("Образ Нацуки ставит коробку с мангой на полку в кошмаре Макса."),
        artist = _("Художник -- Satchely из Team Salvato\nРедактирование спрайта персонажа -- SpringingTraps#5243 (Discord, старый ник)"),
        image_show = Composite((1280, 720), (0, 0), "n_cg2_bg", (0, 0), "n_cg2_base_horror_gallery_cg"),
        image_export = None
    )

    cg_a1_d10_night_n_2 = GalleryCGImage(
        name = "cg_a1_d10_night_n_2",
        timeline = f"{cg_timeline_act_1} 10",
        place = _("Литературный клуб"),
        description = _("Образ Нацуки рассказывает Максу о недостатке внимания в его кошмаре."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "n_cg1_bg", (0, 0), "n_cg1_base", (0, 0), "n_cg1b"),
        image_export = None
    )

    cg_a1_d11_y = GalleryCGImage(
        name = "cg_a1_d11_y",
        timeline = f"{cg_timeline_act_1} 11",
        place = _("Спальня в доме Макса"),
        description = _("Юри наслаждается мягким полотенцем, придерживая руку Макса."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = "y_cg3_base",
        image_export = "images/cg/y_cg3_base.png"
    )

    cg_a1_d11_night_mmm = GalleryCGImage(
        name = "cg_a1_d11_night_mmm",
        timeline = f"{cg_timeline_act_1} 11",
        place = _("Коридор школы"),
        description = _("Моникаммм осматривает Макса вблизи в его кошмаре."),
        artist = _("Художник образа -- Satchely из Team Salvato\nРедактирование спрайта -- KitsuruDev"),
        image_show = Composite((1280, 720), (0, -550), "bg glitch", (-300, -500), "monikammm_cg_act_1_day_11_gallery_cg"),
        image_export = None
    )

    cg_a1_d12_s = GalleryCGImage(
        name = "cg_a1_d12_s",
        timeline = f"{cg_timeline_act_1} 12",
        place = _("Кладовка Литературного клуба"),
        description = _("Сайори охлаждает свой лоб бутылкой с яблочным соком после удара о косяк."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = "s_cg2_base2",
        image_export = "images/cg/s_cg2_base2.png"
    )

    cg_a1_d12_night_y = GalleryCGImage(
        name = "cg_a1_d12_night_y",
        timeline = f"{cg_timeline_act_1} 12",
        place = _("Литературный клуб"),
        description = _("Погибший от рук Макса образ Юри в его кошмаре."),
        artist = _("Художник образа -- Satchely из Team Salvato"),
        image_show = "images/cg/y_kill/1a.png",
        image_export = None
    )

    cg_a1_d13_night_mmm = GalleryCGImage(
        name = "cg_a1_d13_night_mmm",
        timeline = f"{cg_timeline_act_1} 13",
        place = _("Класс школы"),
        description = _("Моникаммм разговаривает с Максом в его кошмаре."),
        artist = _("Художник -- Satchely из Team Salvato\nРедактирование спрайта -- KitsuruDev"),
        image_show = Composite((1280, 720), (0, 0), "black", (0, 0), "monikammm_cg_act_1_day_13_mask_smoke", (0, 0), "monikammm_cg_act_1_day_13_mask_smoke_flip", (0, 0), "monikammm_cg_act_1_day_13_mask_grain", (0, 0), "monikammm_cg_act_1_day_13_mask_gas_cloud", (0, 0), "monika_room", (0, 0), "monika_room_highlight", (0, 0), "monika_room_desk", (0, 0), "monikammm desk hcross"),
        image_export = None
    )

    cg_a1_d14_m = GalleryCGImage(
        name = "cg_a1_d14_m",
        timeline = f"{cg_timeline_act_1} 14",
        place = _("Гостиная дома Моники"),
        description = _("Моника в ожидании поцелуя на свидании с Максом."),
        artist = _("Художники -- Itchylychi, Cyrke (Reddit), Chiff The Oblivious"),
        image_show = Composite((1280, 720), (0, 0), "monika_cg_act_1_day_14_base", (0, 0), "monika_cg_act_1_day_14_exp3"),
        image_export = ("mod_assets/cg/main_history/act_1/day_14/m_base.png", "mod_assets/cg/main_history/act_1/day_14/m_exp3.png")
    )

    cg_menu_m = GalleryCGImage(
        name = "cg_menu_m",
        timeline = _("Всё время"),
        place = _("Главное меню"),
        description = _("На страже целостности и работоспособности модификации."),
        artist = _("Художник -- Satchely из Team Salvato"),
        image_show = Composite((1280, 720), (0, 0), "menu_bg", (0, 0), "images/cg/monika/monika_bg.png"),
        image_export = None
    )


## Gallery Screen #############################################################


screen gallery_cg():
    tag menu

    style_prefix "gallery_cg"

    use game_menu(_("Галерея")):

        fixed:

            vpgrid id "gcgvp":
                rows math.ceil(len(GalleryCG.dict) / 2.0)
                cols 2

                mousewheel True
                arrowkeys True
                allow_underfull True

                spacing 50

                align (0.35, 1.0)
                ysize 600

                for name, gl in GalleryCG.dict.items():
                    vbox:
                        xsize 400 ysize 370

                        if gl.unlocked:
                            label "[gl.timeline]"

                            null height 5

                            imagebutton:
                                idle gl.small_size
                                action [SetVariable("GalleryCG.current", name), ShowMenu("preview_cg"), With(Dissolve(0.5))]

                            null height 10

                            text "[gl.place]" style "gallery_cg_place_text"

                            null height 5

                            text "[gl.description]"

                        else:
                            label "???"

                            null height 5

                            imagebutton:
                                idle "mod_assets/mod_extra_images/gallery_cg/lock.png"
                                action [
                                    Play("sound", gui.activate_sound),
                                    Show(
                                        "extra_screen_help",
                                        message = _("Продолжайте проходить сюжет,\nчтобы открыть эту CG-сцену."),
                                        ok_action = Hide("extra_screen_help"),
                                        chibi = "s_chibi turned mt ce",
                                        chibi_pos = 95
                                    )
                                ]

                            null height 10

                            text _("CG-сцена заблокирована") style "gallery_cg_place_text"

                            null height 5

                            text "???"

            vbar value YScrollValue("gcgvp") xalign 1.012 ypos -0.08 ysize 570


        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
                "extra_screen_help",
                _("Помощь\nДля просмотра сцены (CG) во весь экран нажмите на его разблокированную миниатюру.\nЧтобы переключать CG при просмотре, нажмите на боковые стрелки.\nЧтобы выйти из режима просмотра, нажмите \"X\".\nЧтобы экспортировать CG к себе на компьютер, нажмите \"E\".\nПапка эскпорта будет указана во всплывающем окне."),
                ok_action = Hide("extra_screen_help"),
                chibi = "y_chibi turned magnifier",
                chibi_pos = 30
            )

        if config.developer:
            textbutton "UN":
                text_size 30
                pos (0.89, 0.98)
                action Function(GalleryCG.unlock_all)


style gallery_cg_text is gui_text
style gallery_cg_place_text is gallery_cg_text
style gallery_cg_label_text is gallery_cg_place_text

style gallery_cg_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    color "#000"
    outlines []
    size 18
    text_align 0.5
    xalign 0.5

style gallery_cg_place_text:
    color "#fff"
    outlines [(2, "#505050", 0, 0)]
    size 20

style gallery_cg_label:
    xalign 0.5

style gallery_cg_label_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]



## Gallery Screen #################################################################
##
## This screen shows the currently selected screen to the player in-game.
screen preview_cg():

    tag menu

    hbox:
        add GalleryCG.dict[GalleryCG.current].image_show

    hbox:
        xalign 0.999 ypos 0.01
        spacing 7

        textbutton "i":
            text_style "preview_cg_textbutton_text"
            text_size 30
            activate_sound gui.activate_sound
            action Show("dialog", message=GalleryCG.dict[GalleryCG.current].artist, ok_action=Hide("dialog"))

        textbutton "E":
            text_style "preview_cg_textbutton_text"
            text_size 30
            activate_sound gui.activate_sound
            action Function(GalleryCG.dict[GalleryCG.current].export)

        textbutton "X":
            text_style "preview_cg_textbutton_text"
            text_size 30
            activate_sound gui.activate_sound
            action ShowMenu("gallery_cg")

    textbutton "<":
        text_style "preview_cg_textbutton_text"
        xalign 0.0 yalign 0.5
        action Function(GalleryCG.next, True)

    textbutton ">":
        text_style "preview_cg_textbutton_text"
        xalign 1.0 yalign 0.5
        action Function(GalleryCG.next)

    on "replaced" action With(Dissolve(0.5))


style preview_cg_textbutton_text is navigation_button_text
style preview_cg_textbutton_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    size 40
