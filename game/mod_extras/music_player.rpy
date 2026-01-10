## music_player.rpy

init -1 python in MusicPlayer:
    from re import sub

    dict, values, current = {}, None, None
    current_time = 0
    paused = False

    def next(back=False):
        global dict, values, current, current_time, paused

        if not values:
            values = [v for k, v in dict.items()]
        index_current = values.index(current)
        index_next = index_current - 1 if back else index_current + 1
        try:               current = values[index_next]
        except IndexError: current = values[0]

        current_time, paused = 0, False
        renpy.music.stop("music_player_channel")
        renpy.music.play(current.music, "music_player_channel", fadeout=1.0)

    class Track:
        def __init__(self, music, length, title, author, description = None):
            self.music = sub(r"<[^>]+>", "", music)
            self.length = length # в секундах
            self.title = title
            self.author = author
            self.description = description
            dict[self.title] = self


init python:
    track_author_old_discord = _("Discord, старый ник")
    track_description_original = _("Трек из оригинальной игры")
    track_description_mod_site = _("Трек взят с сайта")
    track_description_mod_license = _("под лицензией")
    track_description_mod_DDMC = _("Трек взят из {a=https://drive.google.com/drive/folders/1yTohcOnGV6Kw6Lru1cITWt-zwRoGSCm_}DDMC Community Assets{/a}/{a=https://drive.google.com/drive/folders/175rY_jBUY1N7TLOIeSX4justUH63Nh4c}DDMC Music Archive{/a}")
    track_description_mod_EZ2 = _("Трек взят из {a=https://www.youtube.com/live/OgwzpCBKLrc}набора треков{/a} модификации игры «Half-Life 2» -- «Entropy zero 2»")

    track_description_mod_url_incompetech = "{a=https://incompetech.com/}incompetech.com{/a}"
    track_description_mod_url_ccmixter = "{a=https://dig.ccmixter.org/}dig.ccmixter.org{/a}"
    track_description_mod_url_opengameart = "{a=https://opengameart.org/}opengameart.org{/a}"
    track_description_mod_url_airyluvs = _("Он также есть в наборе треков на официальном сайте композитора {a=https://airyluvs.com/}AIRYLUVS{/a}")
    track_description_mod_url_freepd = "{a=https://www.freepd.com/}freepd.com{/a}"
    track_description_mod_url_silvermansound = "{a=https://www.silvermansound.com/}silvermansound.com{/a}"
    track_description_mod_url_youfulca = "Трек взят с одноимённого {a=https://youfulca.com/}сайта композитора{/a}"
    track_description_mod_url_wub_machine = "Трек создан при помощи сайта {a=https://the.wubmachine.com/}Wub Machine (the automagic dubstep remixer){/a}"

    track_description_mod_youtube_tad = "У композитора есть {a=https://www.youtube.com/c/Tadon}youtube-канал{/a}"
    track_description_mod_youtube_djmykah = "У композитора есть {a=https://www.youtube.com/@DJMykah/videos}youtube-канал{/a}"
    track_description_mod_youtube_sstardvst = "У композитора есть {a=https://www.youtube.com/@sstardvst/videos}youtube-канал{/a}"
    track_description_mod_youtube_benjamintyt = "У композитора есть {a=https://www.youtube.com/@BenjamintYT/videos}youtube-канал{/a}"

    track_description_mod_license_CC0_1 = "{a=https://creativecommons.org/publicdomain/zero/1.0/}Creative Commons Zero License{/a}."
    track_description_mod_license_CC_NC_SAMPLINGPLUS_1 = "{a=https://creativecommons.org/licenses/nc-sampling+/1.0/deed.en}Creative Commons Noncommercial Sampling Plus license{/a}."
    track_description_mod_license_CC_BY_3 = "{a=https://creativecommons.org/licenses/by/3.0/deed.en}Creative Commons Attribution 3.0 License{/a}."
    track_description_mod_license_CC_BY_4 = "{a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 License{/a}."
    track_description_mod_license_CC_BY_NC_3 = "{a=https://creativecommons.org/licenses/by-nc/3.0/legalcode.en}Creative Commons Attribution Noncommercial (3.0) License{/a}."
    track_description_mod_license_CC_BY_NC_4 = "{a=https://creativecommons.org/licenses/by-nc/4.0/legalcode.en}Creative Commons Attribution Noncommercial (4.0) License{/a}."
    track_description_mod_license_OGA_BY_3 = "{a=https://opengameart.org/content/oga-by-30-faq}Open Game Art Attribution 3.0 License{/a}."


    track_t1 = Track(
        music = audio.t1,
        length = 131,
        title = _("Doki Doki Literature Club! -- Главная тема"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t2 = Track(
        music = audio.t2,
        length = 80,
        title = "Ohayou Sayori!",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t3 = Track(
        music = audio.t3,
        length = 100,
        title = _("Doki Doki Literature Club! -- Тема в игре"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t4 = Track(
        music = audio.t4,
        length = 122,
        title = "Dreams of Love and Literature",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5 = Track(
        music = audio.t5,
        length = 91,
        title = "Okay Everyone!",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5m = Track(
        music = audio.tmonika,
        length = 91,
        title = _("Okay Everyone! -- Тема Моники"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5s = Track(
        music = audio.tsayori,
        length = 91,
        title = _("Okay Everyone! -- Тема Сайори"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5n = Track(
        music = audio.tnatsuki,
        length = 91,
        title = _("Okay Everyone! -- Тема Нацуки"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5y = Track(
        music = audio.tyuri,
        length = 91,
        title = _("Okay Everyone! -- Тема Юри"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5yg = Track(
        music = audio.t5yg,
        length = 91,
        title = _("Okay Everyone! -- «Испорченная» тема Юри"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t5ng = Track(
        music = audio.t5ng,
        length = 91,
        title = _("Okay Everyone! -- «Испорченная» тема Нацуки"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t6 = Track(
        music = audio.t6,
        length = 90,
        title = "Play With Me",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t6g = Track(
        music = audio.t6g,
        length = 90,
        title = _("Play With Me -- «Испорченная» версия"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t6s = Track(
        music = audio.t6s,
        length = 362,
        title = _("Play With Me -- «Растянутая» версия"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t7 = Track(
        music = audio.t7,
        length = 71,
        title = "Poem Panic",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t7g = Track(
        music = audio.t7g,
        length = 49,
        title = _("Poem Panic -- «Ускоренная» версия"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t8 = Track(
        music = audio.t8,
        length = 92,
        title = "Daijoubu!",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t9 = Track(
        music = audio.t9,
        length = 59,
        title = "My Feelings",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t9g = Track(
        music = audio.t9g,
        length = 28,
        title = _("My Feelings -- «Ускоренная» версия"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_t10y = Track(
        music = audio.t10y,
        length = 77,
        title = _("My Confession -- «Испорченная» тема Юри"),
        author = "Dan Salvato",
        description = track_description_original
    )

    track_td = Track(
        music = audio.td,
        length = 160,
        title = "Sayo-nara",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_m1 = Track(
        music = audio.m1,
        length = 231,
        title = "Just Monika",
        author = "Dan Salvato",
        description = track_description_original
    )

    track_sayori_flashback = Track(
        music = audio.sayori_flashback,
        length = 210,
        title = "Ohayou Sayori! 2010 ver.",
        author = "Dan Salvato",
        description = _("Старая версия трека «Ohayou Sayori!»")
    )

    track_baking_club = Track(
        music = audio.baking_club,
        length = 166,
        title = "Set myself on fire",
        author = "Wretched Team (Doki Doki Exit Music)",
        description = _("Трек взят из {a=https://drive.google.com/drive/folders/18i6pNRiThgHxF55oWpGpPCjZxACOKAzJ}архива{/a} группы разработчиков")
    )

    track_literature_club_hellevator_incident = Track(
        music = audio.literature_club_hellevator_incident,
        length = 186,
        title = "Enter the Party",
        author = "Kevin MacLeod",
        description = f"{track_description_mod_site} {track_description_mod_url_incompetech} {track_description_mod_license} {track_description_mod_license_CC_BY_4}"
    )

    track_shop_food_music = Track(
        music = audio.shop_food_music,
        length = 183,
        title = "Blow Your Horn",
        author = "Darkroom",
        description = f"{track_description_mod_site} {track_description_mod_url_ccmixter} {track_description_mod_license} {track_description_mod_license_CC_BY_NC_4}"
    )

    track_mc_house_lofi_bliss = Track(
        music = audio.mc_house_lofi_bliss,
        length = 168,
        title = "No mistakes",
        author = "Robbero",
        description = f"{track_description_mod_site} {track_description_mod_url_ccmixter} {track_description_mod_license} {track_description_mod_license_CC_BY_NC_3}"
    )

    track_according_to_the_plan = Track(
        music = audio.according_to_the_plan,
        length = 179,
        title = "Partners in crime (Instrumental)",
        author = "spinningmerkaba, platinum butterfly",
        description = f"{track_description_mod_site} {track_description_mod_url_ccmixter} {track_description_mod_license} {track_description_mod_license_CC_BY_NC_3}"
    )

    track_sayori_bliss = Track(
        music = audio.sayori_bliss,
        length = 255,
        title = "Square3",
        author = "Airtone, Kara Square",
        description = f"{track_description_mod_site} {track_description_mod_url_ccmixter} {track_description_mod_license} {track_description_mod_license_CC_BY_NC_3}"
    )

    track_literature_club_tea_party = Track(
        music = audio.literature_club_tea_party,
        length = 315,
        title = "Drops of H2O (The Filtered Water Treatment)",
        author = "J.Lang, Airtone",
        description = f"{track_description_mod_site} {track_description_mod_url_ccmixter} {track_description_mod_license} {track_description_mod_license_CC_BY_3}"
    )

    track_mod_game_menu = Track(
        music = audio.mod_game_menu,
        length = 54,
        title = "Hella bumps",
        author = "The Cynic Project (pixelsphere.org)",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_mod_game_menu_nightmare = Track(
        music = audio.mod_game_menu_nightmare,
        length = 96,
        title = "Tech Lab (Soft Hum) verb",
        author = "Circlerun",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC_BY_3}"
    )

    track_natsuki_run = Track(
        music = audio.natsuki_run,
        length = 26,
        title = "Fast Fight",
        author = "Ville Nousiainen",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_school_of_quirks = Track(
        music = audio.school_of_quirks,
        length = 148,
        title = "School of Quirks",
        author = "Zander Noriega",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC_BY_3}"
    )

    track_suspicion = Track(
        music = audio.suspicion,
        length = 92,
        title = "Deliciously Sour",
        author = "Matthew Pablo (matthewpablo.com)",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC_BY_3}"
    )

    track_natsuki_chasing = Track(
        music = audio.natsuki_chasing,
        length = 138,
        title = "Thrust Sequence",
        author = "Matthew Pablo (matthewpablo.com)",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC_BY_3}"
    )

    track_mc_with_monika = Track(
        music = audio.mc_with_monika,
        length = 186,
        title = "Funky Hip Hop Lofi Jam",
        author = "omfgdude",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_chill_lofi = Track(
        music = audio.chill_lofi,
        length = 123,
        title = "Chill lofi inspired",
        author = "omfgdude",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_cup_of_tea = Track(
        music = audio.cup_of_tea,
        length = 168,
        title = "A cup of tea",
        author = "TAD",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}. {track_description_mod_youtube_tad}"
    )

    track_amaterasu = Track(
        music = audio.amaterasu,
        length = 268,
        title = "Arukas Bloom",
        author = "TAD",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC_BY_4}. {track_description_mod_youtube_tad}"
    )

    track_literature_club_wine_incident = Track(
        music = audio.literature_club_wine_incident,
        length = 225,
        title = "Post-adventure tea party",
        author = "Zane Little Music",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_tetris_round = Track(
        music = audio.tetris_round,
        length = 90,
        title = "The Cool Factor",
        author = "Zane Little Music",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_tetris_loss = Track(
        music = audio.tetris_loss,
        length = 117,
        title = "Glitch Stairs",
        author = "Fupi",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_yuri_romanticism = Track(
        music = audio.yuri_romanticism,
        length = 156,
        title = "Funny and Cute Town Theme",
        author = "ISAo",
        description = f"{track_description_mod_site} {track_description_mod_url_opengameart} {track_description_mod_license} {track_description_mod_license_OGA_BY_3} {track_description_mod_url_airyluvs}"
    )

    track_martini_sunset = Track(
        music = audio.martini_sunset,
        length = 174,
        title = "Martini Sunset",
        author = "KevinMacLeod",
        description = f"{track_description_mod_site} {track_description_mod_url_freepd} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_monika_playful = Track(
        music = audio.monika_playful,
        length = 95,
        title = "Brooker's Blues",
        author = "Jason Shaw",
        description = f"{track_description_mod_site} {track_description_mod_url_freepd} {track_description_mod_license} {track_description_mod_license_CC0_1}"
    )

    track_libitina_playful = Track(
        music = audio.libitina_playful,
        length = 162,
        title = "Strollin' Cat",
        author = "Shane Ivers",
        description = f"{track_description_mod_site} {track_description_mod_url_silvermansound} {track_description_mod_license} {track_description_mod_license_CC_BY_4}"
    )

    track_reiko_music = Track(
        music = audio.reiko_music,
        length = 216,
        title = "HOLY MOLY",
        author = "Shane Ivers",
        description = f"{track_description_mod_site} {track_description_mod_url_silvermansound} {track_description_mod_license} {track_description_mod_license_CC_BY_4}"
    )

    track_set_ablaze = Track(
        music = audio.set_ablaze,
        length = 80,
        title = "Set Ablaze",
        author = "Youfulca",
        description = track_description_mod_url_youfulca
    )

    track_impalpable_force = Track(
        music = audio.impalpable_force,
        length = 84,
        title = "The Impalpable Force",
        author = "Youfulca",
        description = track_description_mod_url_youfulca
    )

    track_contact = Track(
        music = audio.contact,
        length = 130,
        title = "Youkai",
        author = "Youfulca",
        description = track_description_mod_url_youfulca
    )

    track_mc_after_nightmare = Track(
        music = audio.mc_after_nightmare,
        length = 90,
        title = "I'm innocent",
        author = "CW3D",
        description = track_description_mod_EZ2
    )

    track_confrontation = Track(
        music = "mod_assets/music/nightmares/confrontation.ogg",
        length = 183,
        title = "Confrontation",
        author = "Spencer Baggett",
        description = track_description_mod_EZ2
    )

    track_mc_daijoubu = Track(
        music = audio.mc_daijoubu,
        length = 175,
        title = "Daijoubu! (mc ver.)",
        author = "BlueGodXD (Reddit)",
        description = track_description_mod_DDMC
    )

    track_sayori_boring = Track(
        music = audio.sayori_boring,
        length = 124,
        title = "Random ukulele playing",
        author = f"SpeiBer#7316 ({track_author_old_discord})",
        description = track_description_mod_DDMC
    )

    track_sayori_my_confession_piano = Track(
        music = audio.sayori_my_confession_piano,
        length = 126,
        title = "Sad Sayori",
        author = f"JLucher#2410 ({track_author_old_discord}) (soundcloud.com/jlucher)",
        description = track_description_mod_DDMC
    )

    track_natsuki_cooking = Track(
        music = audio.natsuki_cooking,
        length = 63,
        title = "Wii (epic remix)",
        author = f"Empyre#4565 ({track_author_old_discord})",
        description = track_description_mod_DDMC
    )

    track_natsuki_hard_glitch = Track(
        music = audio.natsuki_hard_glitch,
        length = 51,
        title = "Play with me (remix hard glitch)",
        author = f"TsunKrAZy#2862 ({track_author_old_discord})",
        description = track_description_mod_DDMC
    )

    track_mc_house_tired = Track(
        music = audio.mc_house_tired,
        length = 128,
        title = "Matane",
        author = "soriinz",
        description = track_description_mod_DDMC
    )

    track_sayori_happy_thoughts = Track(
        music = audio.sayori_happy_thoughts,
        length = 124,
        title = "Happy Thoughts",
        author = "jadethevixen",
        description = track_description_mod_DDMC
    )

    track_mod_main_menu = Track(
        music = audio.mod_main_menu,
        length = 215,
        title = "Doki Doki Literature Club! (remix)",
        author = "DJMykah",
        description = track_description_mod_youtube_djmykah
    )

    track_yuri_poem = Track(
        music = audio.yuri_poem,
        length = 132,
        title = "My Confession Lofi Remix (Remake)",
        author = "sstardvst",
        description = track_description_mod_youtube_sstardvst
    )

    track_sayori_my_confession_rain = Track(
        music = audio.sayori_my_confession_rain,
        length = 207,
        title = "My confession, but Yuri got sleepy while confessing",
        author = "BenjaMint",
        description = track_description_mod_youtube_benjamintyt
    )

    track_dont_play_with_me = Track(
        music = audio.dont_play_with_me,
        length = 158,
        title = "Play with me (remix)",
        author = "Wub Machine",
        description = track_description_mod_url_wub_machine
    )

    track_dreams_of_hatred_and_literature = Track(
        music = audio.dreams_of_hatred_and_literature,
        length = 183,
        title = "Dreams of love and literature (remix)",
        author = "Wub Machine",
        description = track_description_mod_url_wub_machine
    )

    track_your_eyes = Track(
        music = audio.your_eyes,
        length = 97,
        title = "Your Eyes (remake)",
        author = "ASCOIRIS (Reddit)"
    )

    track_sayori_happy = Track(
        music = audio.sayori_happy,
        length = 97,
        title = "Ohayou Sayori! (remix)",
        author = "DanFourts",
        description = _("Трек взят из {a=https://drive.google.com/file/d/1y2LfJniuEf3dcfQonrZeOJ--nRfeaoUs/view}архива{/a} треков композитора")
    )



screen music_player():
    tag menu

    style_prefix "music_player"

    use game_menu(_("Музыка")):

        frame:
            background "extra_background_element"

            if not MusicPlayer.current:
                text _("Выберите музыкальный трек для воспроизведения\nи просмотра авторства"):
                    style "music_player_label_text_none_track"
            else:
                python:
                    track = MusicPlayer.current
                    track_length = track.length
                    current_time = MusicPlayer.current_time

                timer 1.0 repeat True:
                    action If(
                        not MusicPlayer.paused,
                            SetVariable("MusicPlayer.current_time", get_pos(channel="music_player_channel"))
                        )

                vbox:
                    pos (0.185, -0.197)
                    ysize 210

                    text f"{current_time // 60:.0f}:{current_time % 60:02.0f} -- {track_length // 60:.0f}:{track_length % 60:02.0f}":
                        style "music_player_text_time"
                        xalign 0.5

                    null height 1

                    vbox:
                        xsize 600 ysize 70

                        label _("Трек: [track.title]")
                        label _("Автор: [track.author]")

                    if track.description:
                        textbutton _("Информация об источнике"):
                            text_style "music_player_textbutton_description_text"
                            activate_sound gui.activate_sound
                            action ShowMenu(
                                "extra_screen_help",
                                track.description,
                                ok_action = Hide("extra_screen_help"),
                                chibi = "kam_chibi turned headphones",
                                chibi_pos = 110
                            )
                    else:
                        null height 37

                    hbox:
                        xalign 0.5
                        spacing 10

                        imagebutton:
                            idle "prev_idle"
                            hover "prev_hover"
                            action Function(MusicPlayer.next, True)

                        imagebutton:
                            if MusicPlayer.paused:
                                idle "play_idle"
                                hover "play_hover"
                            else:
                                idle "pause_idle"
                                hover "pause_hover"
                            action If(
                                MusicPlayer.paused,
                                [
                                    SetVariable("MusicPlayer.paused", False),
                                    PauseAudio("music_player_channel", False),
                                ],
                                [
                                    SetVariable("MusicPlayer.paused", True),
                                    PauseAudio("music_player_channel", True)
                                ]
                            )

                        imagebutton:
                            idle "replay_idle"
                            hover "replay_hover"
                            action [
                                SetVariable("MusicPlayer.current", track),
                                SetVariable("MusicPlayer.current_time", 0),
                                SetVariable("MusicPlayer.paused", False),
                                Play("music_player_channel", track.music)
                                ]

                        imagebutton:
                            idle "next_idle"
                            hover "next_hover"
                            action Function(MusicPlayer.next)

            vpgrid id "bar_music_list":
                rows len(MusicPlayer.dict)
                cols 1

                mousewheel True
                arrowkeys True

                pos (200, 170)
                ysize 400
                spacing 5

                for title, track in MusicPlayer.dict.items():
                    textbutton "[title]":
                        text_style "music_player_textbutton_text"
                        xsize 585
                        activate_sound gui.activate_sound
                        action [
                            SetVariable("MusicPlayer.current", track),
                            SetVariable("MusicPlayer.paused", False),
                            SetVariable("MusicPlayer.current_time", 0),
                            Stop("music_player_channel"), # для перекрытия fadeout
                            Play("music_player_channel", track.music, fadeout=1.0)
                        ]

            vbar value YScrollValue("bar_music_list") xalign 1.015 ypos 0.3 ysize 360

        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
                "extra_screen_help",
                _("Помощь\nЧтобы выбрать трек для прослушивания, нажмите на его название из списка.\nЭкспорт треков отсутствует во избежание нарушения лицензионных соглашений,\nоднако имеются гиперссылки на их источники. Чтобы увидеть их, нажмите на\nсоответствующую кнопку в окне вывода трека."),
                ok_action = Hide("extra_screen_help"),
                chibi = "y_chibi turned magnifier",
                chibi_pos = 50
            )


style music_player_text is gui_text
style music_player_text_time is gui_text
style music_player_label_text is music_player_text
style music_player_label_text_none_track is music_player_label_text
style music_player_textbutton_text is navigation_button_text
style music_player_textbutton_description_text is music_player_label_text

style music_player_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    size 20
    color "#000"
    outlines []

style music_player_text_time:
    font "mod_assets/font/menu/TickingTimebombBb.ttf"
    size 35
    color "#fff"
    outlines [(2, text_outline_color, 0, 0)]

style music_player_label_text:
    size 20
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (1, text_outline_color, 2, 2)]

style music_player_label_text_none_track:
    size 24
    text_align 0.5
    pos (0.1785, -0.085)

style music_player_textbutton_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    size 24

style music_player_textbutton_description_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/font/menu/Vivl-rail.ttf"
    size 17
    color "#fff"
    outlines [(2, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(3, "#fac", 0, 0), (1, "#fac", 2, 2)]


image play_idle:
    "mod_assets/mod_extra_images/music_player/play_idle.png"
    size (50, 50)
image play_hover:
    "mod_assets/mod_extra_images/music_player/play_hover.png"
    size (50, 50)

image pause_idle:
    "mod_assets/mod_extra_images/music_player/pause_idle.png"
    size (50, 50)
image pause_hover:
    "mod_assets/mod_extra_images/music_player/pause_hover.png"
    size (50, 50)

image replay_idle:
    "mod_assets/mod_extra_images/music_player/replay_idle.png"
    size (50, 50)
image replay_hover:
    "mod_assets/mod_extra_images/music_player/replay_hover.png"
    size (50, 50)

image next_idle:
    "mod_assets/mod_extra_images/music_player/next_idle.png"
    size (50, 50)
image next_hover:
    "mod_assets/mod_extra_images/music_player/next_hover.png"
    size (50, 50)

image prev_idle:
    "mod_assets/mod_extra_images/music_player/next_idle.png"
    size (50, 50) xzoom -1
image prev_hover:
    "mod_assets/mod_extra_images/music_player/next_hover.png"
    size (50, 50) xzoom -1
