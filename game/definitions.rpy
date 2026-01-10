## definitions.rpy

# Make sure only one copy of the mod is running
python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    # всё равно всегда пустые, поэтому нестрашно, что ссылаются на один массив
    config.keymap['self_voicing'] = config.keymap['clipboard_voicing'] = config.keymap['toggle_skip'] = []
    config.keymap['hide_windows'] = ['noshift_K_h'] if persistent.streamer_detected else []


    renpy.music.register_channel("music_player_channel", "music", False)
    renpy.music.register_channel("music_none_loop", "music", False)
    renpy.music.register_channel("music_poem", "music", True)

    renpy.music.register_channel("sound_2", "sfx", False)

    renpy.music.register_channel("noise_1", "sfx", True)
    renpy.music.register_channel("noise_2", "sfx", True)
    renpy.music.register_channel("noise_3", "sfx", True)
    renpy.music.register_channel("noise_4", "sfx", True)
    renpy.music.register_channel("noise_5", "sfx", True)

    renpy.music.register_channel("noise_loading_1", "sfx", True)
    renpy.music.register_channel("noise_loading_2", "sfx", True)

    renpy.music.register_channel("phone_sound", "sfx", False)

    def load_mute_channels(volume):
        for ch in ("music", "music_poem", "noise_1", "noise_2", "noise_3", "noise_4", "noise_5"):
            renpy.music.set_volume(volume, 0.5, ch) # для плавного перехода (в SetMute его нет, к сожалению)

    def get_pos(channel = "music"):
        if pos := renpy.music.get_pos(channel=channel):
            return pos
        return 0

    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    def plot_pause():
        renpy.ui.saybehavior(afm=" ")
        renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
        return


############################## КУРСОРЫ ##############################

define config.mouse = {}

define default_mouse = "default"

## Основные

define config.mouse['default'] = [("mod_assets/elements/dialog/cursors/main_cursors/mc.png", 4, 0)]
define config.mouse['m'] = [("mod_assets/elements/dialog/cursors/main_cursors/m.png", 4, 0)]
define config.mouse['s'] = [("mod_assets/elements/dialog/cursors/main_cursors/s.png", 4, 0)]
define config.mouse['n'] = [("mod_assets/elements/dialog/cursors/main_cursors/n.png", 4, 0)]
define config.mouse['y'] = [("mod_assets/elements/dialog/cursors/main_cursors/y.png", 4, 0)]
define config.mouse['k'] = [("mod_assets/elements/dialog/cursors/main_cursors/k.png", 4, 0)]
define config.mouse['sor'] = [("mod_assets/elements/dialog/cursors/main_cursors/sor.png", 4, 0)]

define config.mouse['ny'] = [("mod_assets/elements/dialog/cursors/main_cursors/ny.png", 4, 0)]

## Интерактивные

define config.mouse['use'] = [("mod_assets/elements/dialog/cursors/interactive/use.png", 16, 16)]
define config.mouse['touch'] = [("mod_assets/elements/dialog/cursors/interactive/touch.png", 12, 7)]
define config.mouse['swing'] = [("mod_assets/elements/dialog/cursors/interactive/swing.png", 24, 28)]

define config.mouse['punch'] = [("mod_assets/elements/dialog/cursors/interactive/punch.png", 24, 24)]
define config.mouse['aim'] = [("mod_assets/elements/dialog/cursors/interactive/aim.png", 23, 25)]


############################## ЭКРАНЫ КУРСОРОВ ##############################

# Подзывание к себе рукой в толпе
screen swing_hand:
    button:
        area(0, 0, 1280, 720)
        mouse "swing"
        action Return()

# Ручка двери в "bg school old_corridor door"
screen club_door_lock_screen:
    button:
        area(662, 76, 299, 568)
        mouse "use"
        action [Play("sound", "mod_assets/sound/school/club_door_lock.mp3"), Return()]


############################## ЭКРАНЫ ##############################

# Экран с номером дня акта
screen new_day(episode):
    text episode:
        font "mod_assets/font/menu/Vivl-rail.ttf"
        size 90
        text_align 0.5
        align (0.5, 0.5)
        line_spacing 40

# Накладываемый текст
screen impose_text(t, c, s=20, x=640, y=360):
    text t:
        font "mod_assets/font/menu/NAMU-Pro.ttf"
        size s
        outlines [(2, c, 0, 0)]
        text_align 0.5
        line_leading -10
        pos (x, y)



############################## Original - music ##############################

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg" # Ohayou Sayori! - сбитый темп, только начало
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg" # Ohayou Sayori! - продолжение сбитого темпа, но оно нормальное
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg" # Ohayou Sayori! - немного повышен тон и скорость
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game
define audio.t3g = "<to 15.255>bgm/3g.ogg" # Main Theme - In Game - сбитый темп, специальный момент для однократного (ломаного) зацикливания мелодии
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg" # Main Theme - In Game - после зацикливания, мелодия в норме
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg" # Main Theme - In Game - приглушенный вариант + мясо
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg" # Dreams of Love and Literature - писк ошибки при составлении стиха
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5yg = "<loop 4.444>bgm/5_yuri2.ogg" # Okay Everyone! - Yuri glitch
define audio.t5ng = "<loop 4.444>bgm/5_ghost.ogg" # Okay Everyone! - Natsuki glitch
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg" # Play With Me - до цикла в норме, после цикла глитчная флейта в мелодии
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg" # Play With Me - реверс
define audio.t6o = "<loop 10.893>bgm/6o.ogg" # Play With Me - Приглушённый вариант
define audio.t6s = "<loop 43.572>bgm/6s.ogg" # Play With Me - смерть Юри - растянутая версия
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg" # Poem Panic - цикл для перехода в ускорение
define audio.t7g = "<loop 31.880>bgm/7g.ogg" # Poem Panic - ускорение - "поезд сошёл с рельс"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings - 207% Speed - "Кто будет переживать по этой соплячке?"
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori
define audio.t10y = "<loop 0>bgm/10-yuri.ogg" # My Confession - Yuri glitch
define audio.td = "<loop 36.782>bgm/d.ogg" # Sayo-nara - смерть Сайори

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme


############################## Mod - music ##############################

############### Техническая музыка ###############

define audio.mod_main_menu = "<loop 31.899 to 211.893>mod_assets/music/main/mod_main_menu.ogg" # DJMykah - Doki Doki Literature Club! (main theme remix)
define audio.mod_main_menu_after_disclaimer = "<from 31.899 loop 31.899 to 211.893>mod_assets/music/main/mod_main_menu.ogg"
define audio.mod_game_menu = "<loop 7.753>mod_assets/music/main/mod_game_menu.ogg" # Cynic Project - Hella bumps
define audio.mod_game_menu_nightmare = "mod_assets/music/main/mod_game_menu_nightmare.ogg" # Circlerun - Tech Lab (Soft Hum) verb

define audio.mod_credits_1 = "<loop 56.972 to 116.970>mod_assets/music/main/mod_credits.ogg" #loop 55.200 to 115.084 # Simon L. - Lo-Fi DDLC
define audio.mod_credits_2 = "<from 116.970>mod_assets/music/main/mod_credits.ogg"

############### Музыкальные вставки (music_none_loop) ##############

define audio.music_stop = "mod_assets/music/insert/music_stop_scratch.mp3"
define audio.oops = "mod_assets/music/insert/oops.mp3"
define audio.joke = "mod_assets/music/insert/joke.mp3"
define audio.rofl = "mod_assets/music/insert/rofl.mp3" # после секретки в меню с Моникаммм


############### Музыка персонажей ###############

## MC
define audio.mc_house_tired = "<loop 0.028 to 127.957>mod_assets/music/characters/mc/house_lofi_tired.ogg" # soriinz - Matane
define audio.mc_house_lofi_bliss = "<loop 47.847 to 155.838>mod_assets/music/characters/mc/house_lofi_bliss.ogg" # Robbero - No mistakes
define audio.mc_daijoubu = "<loop 8.364 to 173.550>mod_assets/music/characters/mc/daijoubu.ogg" # u/BlueGodXD - Daijoubu! (mc ver.)
define audio.mc_with_monika = "<loop 4.168>mod_assets/music/characters/mc/with_monika.ogg" # omfgdude - Funky Hip Hop Lofi Jam
define audio.mc_after_nightmare = "mod_assets/music/characters/mc/after_nightmare.ogg" # CW3D (Entropy Zero 2) - I'm Innocent

## Моника
define audio.monika_playful = "<loop 8.215 to 94.766>mod_assets/music/characters/m/playful.ogg" # Jason Shaw - BrookersBlues

## Сайори
define audio.sayori_boring = "mod_assets/music/characters/s/boring.ogg" # Speißer#7316 - random ukulele playing
define audio.sayori_happy = "<loop 4.364 to 152.727>mod_assets/music/characters/s/happy.ogg" # DanFourts - Ohayou Sayori Remix
define audio.sayori_bliss = "<loop 6.328>mod_assets/music/characters/s/bliss.ogg" # Airtone, Kara Square - Square3
define audio.sayori_flashback = "<loop 16.688 to 199.604>mod_assets/music/characters/s/flashback.ogg" # Ohayou Sayori 2010 ver.
define audio.sayori_my_confession_rain = "<loop 80.041 to 175.985>mod_assets/music/characters/s/my_confession_rain.ogg" # BenjaMint - My confession, but Yuri got sleepy while confessing
define audio.sayori_my_confession_piano = "<loop 0 to 125.278>mod_assets/music/characters/s/my_confession_piano.ogg" # JLucher#2410 - Sad Sayori
define audio.sayori_happy_thoughts = "<loop 31.780 to 119.765>mod_assets/music/characters/s/happy_thoughts.ogg" # jadethevixen - Happy Thoughts

## Нацуки
define audio.natsuki_run = "<loop 1.541>mod_assets/music/characters/n/run.ogg" # Ville Nousiainen - Fast fight
define audio.natsuki_run_panic = "<loop 0 to 122.202>mod_assets/music/characters/n/run_panic.ogg" # Ville Nousiainen - Fast fight
define audio.natsuki_cooking = "<loop 0.046 to 61.760>mod_assets/music/characters/n/cooking.ogg" # Empyre#4565 - Wii but epic remix
define audio.natsuki_chasing = "<loop 22.744 to 133.466>mod_assets/music/characters/n/chasing.ogg" # Matthew Pablo - Thrust Sequence
define audio.natsuki_hard_glitch = "mod_assets/music/characters/n/hard_glitch.ogg" # TsunKrAZy#2862 - Play with me (remix hard glitch)

## Юри
define audio.yuri_romanticism = "mod_assets/music/characters/y/romanticism.ogg" # ISAo - Funny and Cute Town Theme
define audio.yuri_poem = "<loop 12.024>mod_assets/music/characters/y/poem.ogg" # Sstardvst - DDLC My Confession Lofi Remix (Remake)

## Либитина
define audio.libitina_playful = "<loop 0.055 to 158.954>mod_assets/music/characters/l/playful.ogg" # Shane Ivers - Strollin' Cat

## Рэйко
define audio.reiko_music = "<loop 0 to 213.348>mod_assets/music/characters/r/music.ogg" # Shane Ivers - HOLY MOLY


############### Музыка клубов ###############

## Литературный клуб
define audio.literature_club_tea_party = "<loop 24.145 to 312.261>mod_assets/music/club/literature_club/tea_party.ogg" # Djlang59, Airtone - Drops of H2O
define audio.literature_club_wine_incident = "<loop 17.440 to 218.144>mod_assets/music/club/literature_club/wine_incident.ogg" # Zane Little Music - Post-adventure tea party
define audio.literature_club_hellevator_incident = "<loop 24.024 to 184.006>mod_assets/music/club/literature_club/hellevator_incident.ogg" # Kevin MacLeod - Enter the Party

## Клуб выпечки
define audio.baking_club = "<loop 12.346 to 163.869>mod_assets/music/club/baking_club/club_music.ogg" # Wretched Team - Set myself on fire


############### Музыка пробежек ###############

define audio.set_ablaze = "<loop 8.626>mod_assets/music/jogging/set_ablaze.ogg" # youfulca.com - Set Ablaze
define audio.impalpable_force = "<loop 12.161>mod_assets/music/jogging/impalpable_force.ogg" # youfulca.com - The Impalpable Force


############### Музыка магазинов ###############

define audio.shop_food_music = "mod_assets/music/shops/shop_food_music.ogg" # Darkroom - Blow Your Horn


############### Музыка ресторанов и кафе ###############

define audio.martini_sunset = "<loop 0.885 to 170.006>mod_assets/music/restaurants/martini_sunset.ogg" # Anonymous - Martini Sunset


############### Музыка кошмаров ГГ ###############

define audio.confrontation_part_1 = "<loop 1.423 to 8.273>mod_assets/music/nightmares/confrontation.ogg" # Spencer Baggett (Entropy Zero 2) - Confrontation
define audio.confrontation_part_2 = "<from 8.273 loop 15.092 to 21.933>mod_assets/music/nightmares/confrontation.ogg"
define audio.confrontation_part_3 = "<from 21.933 loop 27.134 to 33.988>mod_assets/music/nightmares/confrontation.ogg"
define audio.confrontation_part_4 = "<from 33.988 loop 35.734 to 42.602>mod_assets/music/nightmares/confrontation.ogg"
define audio.confrontation_part_5 = "<from 42.602 loop 42.602 to 56.327>mod_assets/music/nightmares/confrontation.ogg"
define audio.confrontation_part_6 = "<from 56.327 loop 72.056 to 92.588>mod_assets/music/nightmares/confrontation.ogg" # loop 78.150 to 91.862
define audio.confrontation_part_7 = "<from 92.588 loop 97.892 to 125.319>mod_assets/music/nightmares/confrontation.ogg"
define audio.confrontation_part_8 = "<from 152.691>mod_assets/music/nightmares/confrontation.ogg"

define audio.contact = "mod_assets/music/nightmares/contact.ogg" # youfulca.com - Youkai


############### Музыка мини-игр ###############

define audio.tetris_round = "mod_assets/mini_games/tetris/audio/round.ogg" # Zane Little Music - The Cool Factor
define audio.tetris_loss = "mod_assets/mini_games/tetris/audio/loss.ogg" # Fupi - Glitch Stairs


############### Прочее ###############

# Ремиксы оригинальных треков
define audio.dont_play_with_me = "<loop 30.057 to 150.045>mod_assets/music/dont_play_with_me.ogg" # Wub Machine - Play with me (remix)
define audio.dreams_of_hatred_and_literature = "<loop 13.737 to 178.316>mod_assets/music/dreams_of_hatred_and_literature.ogg" # Wub Machine - Dreams of love and literature (remix)

# Позитивные
define audio.according_to_the_plan = "<loop 11.296>mod_assets/music/according_to_the_plan.ogg" # spinningmerkaba, platinum butterfly - Partners in crime (Instrumental)
define audio.school_of_quirks = "<loop 7.058 to 146.077>mod_assets/music/school_of_quirks.ogg" # Zander Noriega - School of Quirks

# Спокойные
define audio.chill_lofi = "<loop 27.419 to 100.324>mod_assets/music/chill_lofi.ogg" # omfgdude - Chill lofi inspired
define audio.cup_of_tea = "<loop 13.775 to 168.041>mod_assets/music/cup_of_tea.ogg" # Tad - A cup of tea
define audio.suspicion = "<loop 1.119 to 76.938>mod_assets/music/suspicion.ogg" # Matthew Pablo - Deliciously Sour

# Любовные
define audio.your_eyes = "mod_assets/music/your_eyes.ogg" # Ascoiris - Your Eyes Remake

# "Традиционные"
define audio.amaterasu = "<loop 16.205 to 258.787>mod_assets/music/amaterasu.ogg" # Tad - Arukas bloom


############################## Original - sounds #############################

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg" # Ghoust menu
define audio.g1 = "<loop 0>bgm/g1.ogg" # заевший звук критической ошибки
define audio.g2 = "<loop 0>bgm/g2.ogg" # пердящий заевший звук критической ошибки
define audio.hb = "<loop 0>bgm/heartbeat.ogg" # Heartbeat
define audio.stab = "sfx/stab.ogg" # Юри зарезалась без падения (без музыки)
define audio.yuri_kill = "sfx/yuri-kill.ogg" # Юри зарезалась без падения (с музыкой)
define audio.gnid = "sfx/gnid.ogg" # Шум при секретном рисунке с головами Сайори в 7 секунд
define audio.eyes = "sfx/eyes.ogg" # Шум при секретном рисунке с опалёнными краями и нарисованной головой Сайори
define audio.interference = "<to 1.5>sfx/interference.ogg" # Звук заедания изображения (движется снизу вверх)
define audio.giggle = "sfx/giggle.ogg" # Хохот Моники
define audio.baa = "gui/sfx/baa.ogg" # Па-а-а~ Юри
define audio.natsuki_ghost_run = "sfx/run.ogg" # Бег нацуки со сломанной шеей

## 3 удара и помехи в 3 секунды:
# play sound monikapound
# show layer master:
#     truecenter
#     parallel:
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#     parallel:
#         xpos 0
#         easein_elastic 0.35 xpos 640
#         xpos 1280
#         easein_elastic 0.35 xpos 640
#         xpos 0
#         easein_elastic 0.35 xpos 640
# show layer screens:
#     truecenter
#     parallel:
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#         zoom 1.5
#         easeout 0.35 zoom 1.0
#     parallel:
#         xpos 0
#         easein_elastic 0.35 xpos 640
#         xpos 1280
#         easein_elastic 0.35 xpos 640
#         xpos 0
#         easein_elastic 0.35 xpos 640
# show noise onlayer front:
#     alpha 0.3
#     easeout 0.35 alpha 0
#     alpha 0.3
#     easeout 0.35 alpha 0
#     alpha 0.3
#     1.35
#     linear 1.0 alpha 0.0
#     pause 3.0
define audio.monikapound = "sfx/monikapound.ogg"

## Помехи с глюками в 0.2 секунды:
# show screen tear_screen(20, 0.1, 0.1, 0, 40)
# window hide(None)
# play sound s_kill_glitch1
# pause 0.25
# stop sound
# hide screen tear_screen
# window show(None)
define audio.s_kill_glitch1 = "sfx/s_kill_glitch1.ogg"

define audio.closet_open = "sfx/closet-open.ogg" # Door open
define audio.closet_close = "sfx/closet-close.ogg" # Door close
define audio.page_turn = "sfx/pageflip.ogg" # Page turn
define audio.fall = "sfx/fall.ogg" # Drop
define audio.fall2 = "sfx/fall2.ogg" # Падение Нацуки со стула в кладовке
define audio.slap = "sfx/slap.ogg" # Упаковка печенья врезалось в лицо


############################## Mod - sounds ##############################


############### Технические звуки + переходы ###############

define audio.logo_fade = "mod_assets/sound/modding/logo/fade.mp3"
define audio.logo_change = "mod_assets/sound/modding/logo/change.mp3"

define audio.achievement_unlock = "mod_assets/sound/modding/achievement_unlock.mp3"

define audio.narrative_changing = "mod_assets/sound/modding/transitions/narrative_changing.mp3"
define audio.narrative_fast_changing = "mod_assets/sound/modding/transitions/narrative_fast_changing.mp3"

define audio.flashback_start = "mod_assets/sound/modding/transitions/flashback_start.mp3"
define audio.flashback_end = "mod_assets/sound/modding/transitions/flashback_end.mp3"

define audio.none_transition = "mod_assets/sound/modding/transitions/none_transition.mp3"
define audio.seconds = "mod_assets/sound/modding/transitions/seconds.mp3"
define audio.magic = "mod_assets/sound/modding/transitions/magic.mp3"

define audio.object_appearance = "mod_assets/sound/modding/transitions/object_appearance.mp3"


############### Тело (звуки соприкосновения и организма) ###############

## Столкновения и соприкосновения

define audio.falldown = "mod_assets/sound/body/falldown.mp3" # Sharp drop
define audio.ram_attack = "mod_assets/sound/body/ram_attack.mp3"
define audio.hit = "mod_assets/sound/body/hit.mp3"
define audio.hit_wood = "mod_assets/sound/body/hit_wood.mp3"
define audio.hit_eyes = "mod_assets/sound/body/hit_eyes.mp3"
define audio.hugs = "mod_assets/sound/body/hugs.mp3"
define audio.fingers_snap = "mod_assets/sound/body/fingers_snap.mp3"


## Прочее

define audio.applause_small = "mod_assets/sound/body/applause_small.mp3"
define audio.clothes_zipping = "mod_assets/sound/body/clothes_zipping.mp3"


## Звуки персонажей

# ГГ
define audio.mc_inhale = "mod_assets/sound/body/mc/inhale.mp3"
define audio.mc_sneeze = "mod_assets/sound/body/mc/sneeze.mp3"
define audio.mc_wake_up = "mod_assets/sound/body/mc/wake_up.mp3"
define audio.mc_neck_crunch_1 = "mod_assets/sound/body/mc/neck_crunch_1.mp3"
define audio.mc_neck_crunch_2 = "mod_assets/sound/body/mc/neck_crunch_2.mp3"
define audio.mc_exciting_heartbeat = "mod_assets/sound/body/mc/exciting_heartbeat.mp3"
define audio.mc_nausea = "mod_assets/sound/body/mc/nausea.mp3"
define audio.mc_vomiting = "mod_assets/sound/body/mc/vomiting.mp3"
define audio.mc_dressing_up = "mod_assets/sound/body/mc/dressing_up.mp3"
define audio.mc_dressing_down = "mod_assets/sound/body/mc/dressing_down.mp3"
define audio.mc_handshake_monikammm = "mod_assets/sound/body/mc/handshake_monikammm.mp3"

# Моника
define audio.monika_lips_popcorn = "mod_assets/sound/body/monika/lips_popcorn.mp3"
define audio.monika_stomach_rumble = "mod_assets/sound/body/monika/stomach_rumble.mp3"
define audio.monika_nausea = "mod_assets/sound/body/monika/nausea.mp3"

# Сайори
define audio.sayori_hide_fast = "mod_assets/sound/body/sayori/hide_fast.mp3"
define audio.sayori_falldown_bed = "mod_assets/sound/body/sayori/falldown_bed.mp3"

# Нацуки
define audio.natsuki_sneeze = "mod_assets/sound/body/natsuki/sneeze.mp3"
define audio.natsuki_stomach_rumble = "mod_assets/sound/body/natsuki/stomach_rumble.mp3"

# Сора
define audio.sora_sneeze = "mod_assets/sound/body/sora/sneeze.mp3"


############### Звуки шагов и бега (noise) ###############

## ГГ
define audio.mc_steps = "mod_assets/sound/body/mc/steps/normal.mp3"
define audio.mc_steps_house = "mod_assets/sound/body/mc/steps/house.mp3"
define audio.mc_steps_house_run = "mod_assets/sound/body/mc/steps/house_run.mp3"
define audio.mc_steps_school_run = "<loop 1.450>mod_assets/sound/body/mc/steps/school_run.mp3"
define audio.mc_steps_outside = "mod_assets/sound/body/mc/steps/outside.mp3"
define audio.mc_steps_outside_jogging = "mod_assets/sound/body/mc/steps/outside_jogging.mp3"
define audio.mc_steps_outside_jogging_wood = "mod_assets/sound/body/mc/steps/outside_jogging_wood.mp3"
define audio.mc_steps_outside_run = "mod_assets/sound/body/mc/steps/outside_run.mp3"

## Моника
define audio.monika_steps_run = "mod_assets/sound/body/monika/steps/run.mp3"

## Сайори
define audio.sayori_steps = "mod_assets/sound/body/sayori/steps/normal.mp3"
define audio.sayori_steps_run = "mod_assets/sound/body/sayori/steps/run.mp3"

## Нацуки
define audio.natsuki_steps_run = "mod_assets/sound/body/natsuki/steps/run.mp3"

## Юри
define audio.yuri_steps_run = "<loop 0.201>mod_assets/sound/body/yuri/steps/run.mp3"


############### Звуки дома ###############

## Кухня

define audio.kitchen_cabinet = "mod_assets/sound/house/kitchen/kitchen_cabinet.mp3"

define audio.microwave_warming_up = "<loop 10.024 to 20.267>mod_assets/sound/house/kitchen/microwave.mp3"
define audio.microwave_finish = "<from 20.529>mod_assets/sound/house/kitchen/microwave.mp3"
define audio.semi_finished_product = "mod_assets/sound/house/kitchen/semi-finished_product.mp3"
define audio.cereals = "mod_assets/sound/house/kitchen/cereals.mp3"
define audio.pouring_wine = "mod_assets/sound/house/kitchen/pouring_wine.mp3"
define audio.boiling_jam = "mod_assets/sound/house/kitchen/boiling_jam.mp3"
define audio.kitchen_whisk_1 = "mod_assets/sound/house/kitchen/kitchen_whisk_1.mp3"
define audio.kitchen_whisk_2 = "mod_assets/sound/house/kitchen/kitchen_whisk_2.mp3"
define audio.trashcan = "mod_assets/sound/house/kitchen/trashcan.mp3"

## Санузел

define audio.sink_open = "<loop 0.845 to 44.520>mod_assets/sound/house/bathroom/sink.mp3"
define audio.sink_close = "<from 45.225>mod_assets/sound/house/bathroom/sink.mp3"
define audio.toilet = "mod_assets/sound/house/bathroom/toilet.mp3"
define audio.shower_open = "<loop 13.047 to 82.971>mod_assets/sound/house/bathroom/shower.mp3"
define audio.shower_close = "<from 82.971>mod_assets/sound/house/bathroom/shower.mp3"

## Двери

define audio.doorbell_mc = "mod_assets/sound/house/doorbell/mc.mp3"
define audio.doorbell_sayori = "mod_assets/sound/house/doorbell/s.mp3"
define audio.doorbell_monika = "mod_assets/sound/house/doorbell/m.mp3"
define audio.doorbell_yuri = "mod_assets/sound/house/doorbell/y.mp3"
define audio.door_knock = "mod_assets/sound/house/door_knock.mp3"
define audio.house_door_open = "mod_assets/sound/house/house_door_open.mp3"
define audio.house_door_close = "mod_assets/sound/house/house_door_close.mp3"
define audio.wardrobe_door_open = "mod_assets/sound/house/wardrobe_door_open.mp3"
define audio.wardrobe_door_close = "mod_assets/sound/house/wardrobe_door_close.mp3"
define audio.shelf_open = "mod_assets/sound/house/shelf_open.mp3"
define audio.shelf_close = "mod_assets/sound/house/shelf_close.mp3"

## Прочее

define audio.light_turning_on = "mod_assets/sound/house/light_turning_on.mp3"
define audio.mc_alarm_clock = "mod_assets/sound/house/alarm_clock/mc.mp3"
define audio.sayori_alarm_clock = "mod_assets/sound/house/alarm_clock/s.mp3"


############### Звуки школы ###############

## Звонок

define audio.school_bell = "mod_assets/sound/school/bell.mp3"

## Двери

define audio.club_door_knock = "mod_assets/sound/school/club_door_knock.mp3"
define audio.club_door_knock_out = "mod_assets/sound/school/club_door_knock_out.mp3"
define audio.club_door_lock = "mod_assets/sound/school/club_door_lock.mp3"
define audio.club_door_lock_close = "mod_assets/sound/school/club_door_lock_close.mp3"

define audio.rooftop_door_knock_out = "mod_assets/sound/school/rooftop_door_knock_out.mp3"


############### Звуки здания (рестораны, магазины, прочее) ###############

## Двери

define audio.building_door_bell = "mod_assets/sound/building/door/bell.mp3"
define audio.building_door_open = "mod_assets/sound/building/door/open.mp3"
define audio.building_door_close = "mod_assets/sound/building/door/close.mp3"

## Лифты

define audio.elevator_button_inside = "mod_assets/sound/building/elevator/button_inside.mp3"
define audio.elevator_button_outside = "mod_assets/sound/building/elevator/button_outside.mp3"
define audio.elevator_door_knock = "mod_assets/sound/building/elevator/door_knock.mp3"
define audio.elevator_mall_arrive = "mod_assets/sound/building/elevator/mall_arrive.mp3"
define audio.elevator_mall_door_open = "<from 6.000>mod_assets/sound/building/elevator/mall_arrive.mp3"
define audio.elevator_mall_door_close = "mod_assets/sound/building/elevator/mall_door_close.mp3"
define audio.elevator_mall_move = "mod_assets/sound/building/elevator/mall_move.mp3"


############### Звуки транспорта и станций ###############

## Автобус

define audio.bus_waiting = "<from 0.026 loop 0.026 to 2.705>mod_assets/sound/transport/bus/waiting.mp3"
define audio.bus_doors = "mod_assets/sound/transport/bus/doors_open_close.mp3"
define audio.bus_inside_1 = "<loop 2.712 to 46.455>mod_assets/sound/transport/bus/inside.mp3"
define audio.bus_inside_2 = "<from 46.322>mod_assets/sound/transport/bus/inside.mp3"
define audio.bus_departure = "mod_assets/sound/transport/bus/departure.mp3"

## Станции электричек и метро

define audio.station_escalator = "mod_assets/sound/transport/metro_train/station_escalator.mp3"
define audio.station_announcement = "<to 12.762>mod_assets/sound/transport/metro_train/train_arrival.mp3"
define audio.station_train_arrival = "<from 17.474>mod_assets/sound/transport/metro_train/train_arrival.mp3"
define audio.station_train_departure = "mod_assets/sound/transport/metro_train/train_departure.mp3"

## Поезд электричек и метро

define audio.train_doors_open = "mod_assets/sound/transport/metro_train/train_doors_open.mp3"
define audio.train_doors_open_inside = "mod_assets/sound/transport/metro_train/train_doors_open_inside.mp3"
define audio.train_doors_close = "mod_assets/sound/transport/metro_train/train_doors_close.mp3"
define audio.train_waiting = "<from 0.032 loop 0.032 to 8.677>mod_assets/sound/transport/metro_train/train_waiting.mp3"
define audio.train_moving_1 = "<loop 23.379 to 54.376>mod_assets/sound/transport/metro_train/train_moving.mp3"
define audio.train_moving_2 = "<from 54.376>mod_assets/sound/transport/metro_train/train_moving.mp3"
define audio.train_moving_3 = "<from 23.379 loop 23.379 to 54.376>mod_assets/sound/transport/metro_train/train_moving.mp3"


############### Звуки окружения (для звуковых каналов noise) ###############

## Природа

define audio.wind = "<loop 11.848>mod_assets/sound/noises/nature/wind.mp3"
define audio.rain_inside = "<loop 5.658>mod_assets/sound/noises/nature/rain_inside.mp3"
define audio.rainfall = "<loop 3.602>mod_assets/sound/noises/nature/rainfall.ogg"
define audio.rainfall_umbrella_mc = "<loop 0.847>mod_assets/sound/noises/nature/rainfall_umbrella_mc.mp3"

## Пригород

define audio.street_suburban_noise = "<loop 0.702 to 72.699>mod_assets/sound/noises/city/street_suburban.mp3"

## Город

define audio.street_full_noise = "mod_assets/sound/noises/city/street_full.mp3"
define audio.street_near_kokoro_noise = "<loop 1.250 to 84.243>mod_assets/sound/noises/city/street_near_kokoro.mp3"
define audio.shop_noise = "mod_assets/sound/noises/city/shop.mp3"
define audio.mall_noise = "mod_assets/sound/noises/city/mall.mp3"

## Госпиталь

define audio.hospital_empty_noise = "mod_assets/sound/noises/city/hospital_empty.ogg"

## Школа

define audio.school_corridor_empty_noise = "mod_assets/sound/noises/school/corridor_empty.mp3"
define audio.school_corridor_light_noise = "<loop 4.279 to 28.536>mod_assets/sound/noises/school/corridor_light.mp3" # обязательно volume 0.5
define audio.school_corridor_hard_noise = "<loop 1.560 to 74.518>mod_assets/sound/noises/school/corridor_hard.mp3"

## Станции

define audio.station_noise = "<loop 17.684 to 108.059>mod_assets/sound/noises/city/station.mp3"
define audio.metro_station_noise = "<loop 3.491 to 53.261>mod_assets/sound/noises/city/metro_station.mp3"


############### Звуки музыкальных инструментов (короткое непосредственное взаимодействие) ###############

## Моника - рояль

define audio.monika_piano_angr = "mod_assets/sound/musical_instruments/monika/piano_angr.mp3"


############### Звуки оружия ###############

## Современный пистолет
define audio.pistol_slide_open = "mod_assets/sound/weapon/pistol/slide_open.mp3"
define audio.pistol_slide_close = "mod_assets/sound/weapon/pistol/slide_close.mp3"
define audio.pistol_shot_single = "mod_assets/sound/weapon/pistol/shot_single.mp3"


############### Прочие звуки ###############

define audio.bag = "mod_assets/sound/other/bag.mp3"
define audio.package_open = "mod_assets/sound/other/package_open.mp3"
define audio.vending_machine_drinks = "mod_assets/sound/other/vending_machine_drinks.mp3"
define audio.soda_open = "mod_assets/sound/other/soda_open.mp3"
define audio.paper_torn_out = "mod_assets/sound/other/paper_torn_out.mp3"
define audio.item_fall_stone = "mod_assets/sound/other/item_fall_stone.mp3"
define audio.book_fall = "mod_assets/sound/other/book_fall.mp3"
define audio.coin_fall = "mod_assets/sound/other/coin_fall.mp3"
define audio.rope_cut = "mod_assets/sound/other/rope_cut.mp3"

define audio.screamer = "mod_assets/sound/horror/screamer.mp3"
define audio.screamer_meme = "mod_assets/sound/horror/screamer_meme.mp3"
define audio.nun_massacre_scream = "mod_assets/sound/horror/nun_massacre_scream.mp3"

define audio.white_noise = "<loop 0.751>mod_assets/sound/horror/white_noise.mp3"
define audio.critical_error = "mod_assets/sound/horror/critical_error.mp3"
define audio.monika_glitch_appearance = "mod_assets/sound/horror/monika_glitch_appearance.mp3"
define audio.monikammm_psyho_control = "<loop 0.784>mod_assets/sound/horror/monikammm_psyho_control.mp3"


############################## Original - backgrounds ##############################

# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image gray = "#808080"
image red = "#FF0000"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat


############################## Mod - backgrounds ##############################

############### Дома ###############

# ГГ
image bg mc house peephole sayori = "mod_assets/bg/houses/inside/mc/peephole_sayori.png"
image bg mc house hallway day = "mod_assets/bg/houses/inside/mc/hallway_day.png"
image bg mc house hallway night = "mod_assets/bg/houses/inside/mc/hallway_night.png"
image bg mc house hallway night light = "mod_assets/bg/houses/inside/mc/hallway_night_light.png"
image bg mc house bathroom day = "mod_assets/bg/houses/inside/mc/bathroom_day.png"
image mc_house_mirror = "mod_assets/bg/houses/inside/mc/mirror.png"

# Моника
image bg monika house outside day = "mod_assets/bg/houses/outside/monika_house_day.png"
image bg monika house outside evening = "mod_assets/bg/houses/outside/monika_house_evening.png"
image bg monika house hallway day = "mod_assets/bg/houses/inside/monika/hallway_day.png"
image bg monika house kitchen day = "mod_assets/bg/houses/inside/monika/kitchen_day.png"
image bg monika house livingroom day = "mod_assets/bg/houses/inside/monika/livingroom_day.png"
image bg monika house bedroom morning = "mod_assets/bg/houses/inside/monika/bedroom_morning.png"
image bg monika house bedroom night light = "mod_assets/bg/houses/inside/monika/bedroom_night_light.png"
image bg monika house bedroom night 1 = "mod_assets/bg/houses/inside/monika/bedroom_night_1.png"
image bg monika house bedroom night 2 = "mod_assets/bg/houses/inside/monika/bedroom_night_2.png"

# Сайори
image bg sayori house outside night = "mod_assets/bg/houses/outside/sayori_house_night.png"
image bg sayori house hallway day = "mod_assets/bg/houses/inside/sayori/hallway_day.png"
image bg sayori house livingroom day = "mod_assets/bg/houses/inside/sayori/livingroom_day.png"
image bg sayori house livingroom night = "mod_assets/bg/houses/inside/sayori/livingroom_night.png"
image bg sayori house bedroom day = "mod_assets/bg/houses/inside/sayori/bedroom_day.png"
image bg sayori house bedroom night = "mod_assets/bg/houses/inside/sayori/bedroom_night.png"
image sayori_house_bedroom_unmade_bed = "mod_assets/bg/houses/inside/sayori/bedroom_unmade_bed.png"
image bg sayori house carpet = "mod_assets/bg/houses/inside/sayori/carpet.png"

# Нацуки
image bg natsuki house outside day = "mod_assets/bg/houses/outside/natsuki_house_day.png"
image bg natsuki house kitchen day = "mod_assets/bg/houses/inside/natsuki/kitchen_day.png"
image bg natsuki house bedroom day = "mod_assets/bg/houses/inside/natsuki/bedroom_day.png"

# Юри
image bg yuri house outside day = "mod_assets/bg/houses/outside/yuri_house_day.png"
image bg yuri house outside day rain = "mod_assets/bg/houses/outside/yuri_house_day_rain.png"
image bg yuri house hallway day = "mod_assets/bg/houses/inside/yuri/hallway_day.png"
image bg yuri house kitchen day = "mod_assets/bg/houses/inside/yuri/kitchen_day.png"
image bg yuri house livingroom day = "mod_assets/bg/houses/inside/yuri/livingroom_day.png"
image bg yuri house bedroom day = "mod_assets/bg/houses/inside/yuri/bedroom_day.png"
image bg yuri house bathroom day = "mod_assets/bg/houses/inside/yuri/bathroom_day.png"


############### Улицы ###############

image bg asphalt:
    "mod_assets/bg/open_places/streets/asphalt.png"
    xsize 1280

image bg residential_day rain = "mod_assets/bg/open_places/streets/niigata/suburban/residential_day_rain.png"
image bg residential_day nearby = "mod_assets/bg/open_places/streets/niigata/suburban/residential_day_nearby.png"

image bg niigata street suburban 1 day = "mod_assets/bg/open_places/streets/niigata/suburban/1_day.png"
image bg niigata street suburban 2 day = "mod_assets/bg/open_places/streets/niigata/suburban/2_day.png"
image bg niigata street suburban 3 day = "mod_assets/bg/open_places/streets/niigata/suburban/3_day.png"
image bg niigata street suburban 4 day = "mod_assets/bg/open_places/streets/niigata/suburban/4_day.png"
image bg niigata street suburban 5 day = "mod_assets/bg/open_places/streets/niigata/suburban/5_day.png"
image bg niigata street suburban 6 day = "mod_assets/bg/open_places/streets/niigata/suburban/6_day.png"
image bg niigata street suburban 7 day = "mod_assets/bg/open_places/streets/niigata/suburban/7_day.png"
image bg niigata street suburban 8 day = "mod_assets/bg/open_places/streets/niigata/suburban/8_day.png"
image bg niigata street suburban 9 day = "mod_assets/bg/open_places/streets/niigata/suburban/9_day.png"
image bg niigata street suburban 10 day = "mod_assets/bg/open_places/streets/niigata/suburban/10_day.png"
image bg niigata street suburban 10 afternoon = "mod_assets/bg/open_places/streets/niigata/suburban/10_afternoon.png"
image bg niigata street suburban 11 day = "mod_assets/bg/open_places/streets/niigata/suburban/11_day.png"
image bg niigata street suburban 11 day rain = "mod_assets/bg/open_places/streets/niigata/suburban/11_day_rain.png"
image bg niigata street suburban 11 afternoon = "mod_assets/bg/open_places/streets/niigata/suburban/11_afternoon.png"
image bg niigata street suburban 11 evening = "mod_assets/bg/open_places/streets/niigata/suburban/11_evening.png"
image bg niigata street suburban 12 day = "mod_assets/bg/open_places/streets/niigata/suburban/12_day.png"
image bg niigata street suburban 13 day = "mod_assets/bg/open_places/streets/niigata/suburban/13_day.png"
image bg niigata street suburban 14 day = "mod_assets/bg/open_places/streets/niigata/suburban/14_day.png"
image bg niigata street suburban 15 day = "mod_assets/bg/open_places/streets/niigata/suburban/15_day.png"
image bg niigata street suburban 16 day = "mod_assets/bg/open_places/streets/niigata/suburban/16_day.png"

image bg niigata street urban 1 day = "mod_assets/bg/open_places/streets/niigata/urban/1_day.png"
image bg niigata street urban 2 day = "mod_assets/bg/open_places/streets/niigata/urban/2_day.png"
image bg niigata street urban 3 day = "mod_assets/bg/open_places/streets/niigata/urban/3_day.png"
image bg niigata street urban 4 day = "mod_assets/bg/open_places/streets/niigata/urban/4_day.png"
image bg niigata street urban 5 day = "mod_assets/bg/open_places/streets/niigata/urban/5_day.png"


############### Школа ###############

### Снаружи

# Вход/выход
image bg school gate 1 = "mod_assets/bg/school/outside/gate/1.png"

# Крыша нового корпуса
image bg school new_rooftop 1 day = "mod_assets/bg/school/outside/rooftop/new_1_day.png"
image bg school new_rooftop 2 day = "mod_assets/bg/school/outside/rooftop/new_2_day.png"

# Крыша старого корпуса
image bg school old_rooftop day = "mod_assets/bg/school/outside/rooftop/old_day.png"


### Внутри

# Коридоры нового корпуса
image bg school f2 new_corridor = "mod_assets/bg/school/inside/corridor/f2_new.png"
image bg school f3 new_corridor = "mod_assets/bg/school/inside/corridor/f3_new.png"

# Коридоры старого корпуса + дверь
image bg school old_corridor wall = "mod_assets/bg/school/inside/corridor/old_wall.png"
image bg school old_corridor door  = "mod_assets/bg/school/inside/corridor/old_door.png"
image bg school f3 old_corridor = "mod_assets/bg/school/inside/corridor/f3_old.png"

# Лестницы старого корпуса
image bg school f1 old_stairwell right = "mod_assets/bg/school/inside/stairwell/f1_old_right.png"
image bg school f1 old_stairwell center = "mod_assets/bg/school/inside/stairwell/f1_old_center.png"
image bg school f2 old_stairwell center = "mod_assets/bg/school/inside/stairwell/f2_old_center.png"

# Классы нового корпуса
image bg school new_class_mc day = "mod_assets/bg/school/inside/class/new_mc_day.png"
image bg school new_class_sayori day = "mod_assets/bg/school/inside/class/new_s_day.png"
image bg school new_class_natsuki day = "mod_assets/bg/school/inside/class/new_n_day.png"
image bg school new_class_yuri day = "mod_assets/bg/school/inside/class/new_y_day.png"

# Классы старого корпуса
image bg school old_class = "mod_assets/bg/school/inside/class/old.png"
image bg school old_class_music = "mod_assets/bg/school/inside/class/old_music.png"

# Литератуный клуб (старый корпус, 2 этаж)
image bg school literature_club board day = "mod_assets/bg/school/inside/literature_club/desk_day.png"
image bg school literature_club morning = "mod_assets/bg/school/inside/literature_club/morning.png"
image school literature_club tea party = "mod_assets/bg/school/inside/literature_club/tea_party.png"

# "Офисные" помещения
image bg school office_reiko = "mod_assets/bg/school/inside/office/r.png"

# Прочее
image bg school library = "mod_assets/bg/school/inside/library.png"


############### Парки ###############

### Японский парк на холме (филиппинский парк)

# Главный вход - с аркой
image bg niigata park japanese off entrance = "mod_assets/bg/open_places/parks/niigata/japanese/entrance_off.png"
image bg niigata park japanese off entrance arc 1 = "mod_assets/bg/open_places/parks/niigata/japanese/entrance_off_arc_1.png"
image bg niigata park japanese off entrance arc 2 = "mod_assets/bg/open_places/parks/niigata/japanese/entrance_off_arc_2.png"
image bg niigata park japanese off entrance arc wall = "mod_assets/bg/open_places/parks/niigata/japanese/entrance_off_arc_wall.png"

# Второй вход - с лестницей (на склоне холма)
image bg niigata park japanese entrance stairs = "mod_assets/bg/open_places/parks/niigata/japanese/entrance_stairs.png"
image bg niigata park japanese path 1 = "mod_assets/bg/open_places/parks/niigata/japanese/path_1.png"
image bg niigata park japanese path 2 = "mod_assets/bg/open_places/parks/niigata/japanese/path_2.png"

# Внутри
image bg niigata park japanese path 3 = "mod_assets/bg/open_places/parks/niigata/japanese/path_3.png"
image bg niigata park japanese path 4 = "mod_assets/bg/open_places/parks/niigata/japanese/path_4.png"
image bg niigata park japanese torii = "mod_assets/bg/open_places/parks/niigata/japanese/torii.png"

# Мост в парке
image bg niigata park japanese bridge 1 = "mod_assets/bg/open_places/parks/niigata/japanese/bridge_1.png"
image bg niigata park japanese bridge 2 = "mod_assets/bg/open_places/parks/niigata/japanese/bridge_2.png"


### Маленький парк в соседнем районе

# Входы
image bg niigata park small entrance 1 = "mod_assets/bg/open_places/parks/niigata/small/entrance_1.png"
image bg niigata park small entrance 2 = "mod_assets/bg/open_places/parks/niigata/small/entrance_2.png"

# Внутри
image bg niigata park small path = "mod_assets/bg/open_places/parks/niigata/small/path.png"


############### Магазины и торговые центры ###############

image bg niigata shop food 1 = "mod_assets/bg/shops/niigata/food/1.png"
image bg niigata shop food 2 = "mod_assets/bg/shops/niigata/food/2.png"
image bg niigata shop food 3 = "mod_assets/bg/shops/niigata/food/3.png"
image bg niigata shop food 4 = "mod_assets/bg/shops/niigata/food/4.png"
image bg niigata shop food 5 = "mod_assets/bg/shops/niigata/food/5.png"

image bg niigata kokoro entrance = "mod_assets/bg/shops/niigata/kokoro/entrance.png"
image bg niigata kokoro f1 corridor = "mod_assets/bg/shops/niigata/kokoro/f1_corridor.png"
image bg niigata kokoro f1 elevator = "mod_assets/bg/shops/niigata/kokoro/f1_elevator.png"
image bg niigata kokoro elevator inside = "mod_assets/bg/shops/niigata/kokoro/elevator_inside.png"
image bg niigata kokoro shop food = "mod_assets/bg/shops/niigata/kokoro/shop_food.png"
image bg niigata kokoro shop clother = "mod_assets/bg/shops/niigata/kokoro/shop_clother.png"
image bg niigata kokoro shop book = "mod_assets/bg/shops/niigata/kokoro/shop_book.png"
image bg niigata kokoro arcade = "mod_assets/bg/shops/niigata/kokoro/arcade.png"
image bg niigata kokoro toilet = "mod_assets/bg/shops/niigata/kokoro/toilet.png"


############### Кафе и рестораны ###############

image bg niigata cafe local inside = "mod_assets/bg/restaurants/niigata/cafe_local/inside.png"


############### Офисы ###############

image bg morioka office inside = "mod_assets/bg/offices/morioka/inside.png"


############### Госпитали ###############

image bg niigata hospital outside day = "mod_assets/bg/hospital/niigata/outside_day.png"
image bg niigata hospital inside day = "mod_assets/bg/hospital/niigata/inside_day.png"


############### Транспорт и станции ###############

image bg train = "mod_assets/bg/transport/train.png"

image bg morioka station morioka platform = "mod_assets/bg/stations/morioka/station_morioka/platform.png"

image bg niigata station niigata entrance outside day = "mod_assets/bg/stations/niigata/station_niigata/entrance_outside_day.png"
image bg niigata station niigata entrance inside = "mod_assets/bg/stations/niigata/station_niigata/entrance_inside.png"
image bg niigata station niigata platform 1 = "mod_assets/bg/stations/niigata/station_niigata/platform_1.png"
image bg niigata station niigata platform 2 = "mod_assets/bg/stations/niigata/station_niigata/platform_2.png"
image bg niigata station niigata bus information = "mod_assets/bg/stations/niigata/station_niigata/bus_information.png"
image bg niigata station niigata bus waiting = "mod_assets/bg/stations/niigata/station_niigata/bus_waiting.png"

image bg bus = "mod_assets/bg/transport/bus.png"

image bg niigata shelter bus = "mod_assets/bg/stations/niigata/shelter_bus/1.png"


############### Прочее фоны ###############

image bg notebook_full_mc = "mod_assets/bg/notebooks/mc.png"
image bg notebook_full_y = "mod_assets/bg/notebooks/y.png"


############### Кошмар ###############

image bg nightmare river = "mod_assets/bg/open_places/nightmare/river.png"



############################## Предметы ##############################

############### Значки ###############

image arrow_triple = "mod_assets/sprites/other/icons/arrow_triple.png"
image arrow_explanation = "mod_assets/sprites/other/icons/arrow_explanation.png"


############### Карты и схемы ###############

image prefecture_niigata = "mod_assets/sprites/other/maps/prefecture_niigata.png"


############### Еда и напитки ###############

image tonkatsu = "mod_assets/sprites/other/items/tonkatsu.png"
image okonomiyaki = "mod_assets/sprites/other/items/okonomiyaki.png"
image taiyaki = "mod_assets/sprites/other/items/taiyaki.png"
image karaage = "mod_assets/sprites/other/items/karaage.png"
image miso_soup = "mod_assets/sprites/other/items/miso_soup.png"
image ramen = "mod_assets/sprites/other/items/ramen.png"

image wine:
    "mod_assets/sprites/other/items/wine.png"
    zoom 0.25
image tea_with_ice = "mod_assets/sprites/other/items/tea_with_ice.png"


############### Руки ###############

image mc_hand_closing_mouth_monika = "mod_assets/sprites/characters/mc/first-person/hand_closing_mouth_monika.png"


############### Оружие ###############

image pistol_view = "mod_assets/sprites/other/weapons/pistol/view.png"
image pistol_open_slide = "mod_assets/sprites/other/weapons/pistol/open_slide.png"
image pistol_idle = "mod_assets/sprites/other/weapons/pistol/idle.png"
image pistol_shot = "mod_assets/sprites/other/weapons/pistol/shot.png"

image school_new_rooftop_1_a1_d12_gun = "mod_assets/sprites/other/weapons/pistol/act_1/d12_n.png"


############################## Предметы от первого лица ##############################

############### Бытовые предметы ###############

image umbrella_mc = "mod_assets/sprites/other/items/first_person/umbrella_mc.png"


############### Еда и напитки ###############

image flattened_onigiri = "mod_assets/sprites/other/items/first_person/flattened_onigiri.png"
image matcha_soda = "mod_assets/sprites/other/items/first_person/matcha_soda.png"
image juice_apple = "mod_assets/sprites/other/items/first_person/juice_apple.png"


############################## Анимированные фоны ##############################

image train_window_field:
    "mod_assets/bg/open_places/train_window/field.png"
    subpixel True xtile 2 pos (-5380, 445)
    linear 9.0 xpos 1285
    repeat

image train_window_niigata:
    "mod_assets/bg/open_places/train_window/niigata.png"
    subpixel True zoom 1.49 pos (-3250, 450)
    linear 7.0 xpos 1247
    repeat


image rain:
    "mod_assets/sprites/other/nature/rain/1.png"
    0.05
    "mod_assets/sprites/other/nature/rain/2.png"
    0.05
    "mod_assets/sprites/other/nature/rain/3.png"
    0.05
    "mod_assets/sprites/other/nature/rain/4.png"
    0.05
    "mod_assets/sprites/other/nature/rain/5.png"
    0.05
    "mod_assets/sprites/other/nature/rain/6.png"
    0.05
    "mod_assets/sprites/other/nature/rain/7.png"
    0.05
    "mod_assets/sprites/other/nature/rain/8.png"
    0.05
    repeat


image crowd_foreground:
    yoffset 20
    "mod_assets/sprites/other/crowd/f1.png" with dissolve
    2.0
    "mod_assets/sprites/other/crowd/f2.png" with dissolve
    2.0
    "mod_assets/sprites/other/crowd/f3.png" with dissolve
    2.0
    repeat

image crowd_background:
    yoffset 20
    "mod_assets/sprites/other/crowd/b1.png" with dissolve
    2.0
    "mod_assets/sprites/other/crowd/b2.png" with dissolve
    2.0
    "mod_assets/sprites/other/crowd/b3.png" with dissolve
    2.0
    repeat


############### Значки загрузки между днями (чтобы упростить их вызов и использование) ###############

image loading_sign_mc = "mod_assets/elements/mod_gui/load/sign/mc.png"


############### Значки в тексте (!вставлять с тегами, указанными в комментариях!) ###############

# {image=accent_call_low_register}{space=-15}
image accent_call_low_register:
    "mod_assets/elements/dialog/signs/in_text/accent.png"
    zoom 0.04
    xoffset -8 yoffset -2
image accent_call_high_register:
    "mod_assets/elements/dialog/signs/in_text/accent.png"
    zoom 0.04
    xoffset -8 yoffset -7

# {image=accent_low_register}{space=-15}
image accent_low_register:
    "mod_assets/elements/dialog/signs/in_text/accent.png"
    zoom 0.06
    xoffset -8 yoffset -15
image accent_high_register:
    "mod_assets/elements/dialog/signs/in_text/accent.png"
    zoom 0.06
    xoffset -8 yoffset -20


############### Подсказки ("at hint_position") ###############

image hint_phone_typing:
    "mod_assets/elements/mod_gui/hints/phone_typing.png"
    size (240, 131)

image hint_phone_menu:
    "mod_assets/elements/mod_gui/hints/phone_menu.png"
    size (240, 131)

image hint_phone_app:
    "mod_assets/elements/mod_gui/hints/phone_app.png"
    size (240, 131)

image hint_phone_call:
    "mod_assets/elements/mod_gui/hints/phone_call.png"
    size (240, 131)

image hint_poem:
    "mod_assets/elements/mod_gui/hints/poem.png"
    size (240, 131)


##############################


# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch:
    Tile("bg/glitch.jpg")
    block:
        yoffset 550 ytile 2
        linear 0.25 yoffset 0
        repeat

# This image transform shows a glitched scene effect during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0




############################## Character Definitions ##############################

############# Моника #############

# "Монобровь" как у Брежнева (гличный спрайт при выходе слева)
image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat


# Моника разваливается на куски
image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


############# Сайори #############

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat


############# Нацуки #############

# Вытекание крови из глазниц (параметры вынесены в вызов изображения, т.к. некорректно работает с ними внутри)
image natsuki_ghost_blood_animation:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 100.0, ramplen=4)

image natsuki ghost_base = "natsuki/ghost1.png" # Белое лицо
image natsuki ghost2 = "natsuki/ghost2.png"     # Улыбка в "половину" лица
image natsuki ghost3 = "natsuki/ghost3.png"     # Ломание шеи
image natsuki ghost4:                           # Бег
    "natsuki ghost3"
    natsuki_ghost_run_animation

### yoffset -20 при доп. параметрах отображения в сюжете (например, alpha 0 -> alpha 1.0) ###

image n_rects_left:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (575, 265)
    size (20, 25)

image n_rects_right:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (647, 259)
    size (20, 25)

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 315)
    size (25, 15)

###

### использовать c: pause 0.2 -> easeout 0.25 zoom 4.5 xoffset 250 yoffset -250 ###

image n_rects_neck_left:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)

image n_rects_neck_right:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)

###


# Лицо + живой рот
image natsuki mouth = Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/0.png", (390, 340), "n_rect", (480, 334), "n_rect")
image n_rect:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

# Рвота
image natsuki vomit = "natsuki/vomit.png"

# Чёрные глазницы и глаз при вылетании из "орбиты"
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"


############# Юри #############

image yuri eyes_base = "yuri/eyes1.png"


############# Моникаммм #############

image monikamm_watch_a1_d5 = "mod_assets/sprites/characters/monikammm/act_1/d5.png"
image monikamm_watch_a1_d10 = "mod_assets/sprites/characters/monikammm/act_1/d10.png"
image monikamm_watch_a1_d11 = "mod_assets/sprites/characters/monikammm/act_1/d11.png"
image monikamm_watch_a1_d12 = "mod_assets/sprites/characters/monikammm/act_1/d12.png"



##############################

## Character Variables
# With assets:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# Without assets:
#   define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")

# Главные персонажи
define mc = DynamicCharacter('mc_name', image='mc', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#aaa9ad")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#4ED42D")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#34B1FF")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#ff367c")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#B957FF")

# Второстепенные персонажи
define r = DynamicCharacter('r_name', image='reiko', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#745eff")
define sor = DynamicCharacter('sor_name', image='sora', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#1e43fc")
define k = DynamicCharacter('k_name', image='kotonoha', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#DDA0DD")
define l = DynamicCharacter('l_name', image='libitina', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#ffedff")
define e = DynamicCharacter('e_name', image='emi', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#ede61a")
define f = DynamicCharacter('f_name', image='fukkacumi', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#14fa70")
define koh = DynamicCharacter('koh_name', image='kohaku', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#ffbf00")
define kam = DynamicCharacter('kam_name', image='kamuko', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#856655")
define h = DynamicCharacter('h_name', image='hiroshi', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#966F33")

# Взрослый контингент
define mm = DynamicCharacter('mm_name', image='monika_mom', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#30b80f")
define md = DynamicCharacter('md_name', image='monika_dad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#289e0b")
define sm = DynamicCharacter('sm_name', image='sayori_mom', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#008ae0")
define sd = DynamicCharacter('sd_name', image='sayori_dad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#007cc9")
define nd = DynamicCharacter('nd_name', image='natsuki_dad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#d91e60")
define ym = DynamicCharacter('ym_name', image='yuri_mom', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#8d2ed1")

define um = DynamicCharacter('um_name', image='uncle_martin', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#0db8a4")
define mi = DynamicCharacter('mi_name', image='mrs_ida', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#f0e0bb")

define clt = Character(_('Классрук'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#e8e8e8")
define dir = Character(_('Директор'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#cfcccc")
define wai = Character(_('Официант'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#cfcccc")
define sta_mall = Character(_('Работник ТЦ'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#cfcccc")

# Совместные фразы
define mcn = Character(_('{color=#aaa9ad}Макс{/color}/{color=#ff367c}Нацу{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ms = Character(_('{color=#4ED42D}Мони{/color}/{color=#34B1FF}Сайо{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define my = Character(_('{color=#4ED42D}Мони{/color}/{color=#B957FF}Юри{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character(_('{color=#ff367c}Нацу{/color}/{color=#B957FF}Юри{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kl = Character(_('{color=#DDA0DD}Кото{/color}/{color=#ffedff}Либи{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ky = Character(_('{color=#DDA0DD}Кото{/color}/{color=#B957FF}Юри{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kny = Character(_('{color=#DDA0DD}К{/color}/{color=#ff367c}Н{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define nsy = Character(_('{color=#ff367c}Н{/color}/{color=#34B1FF}С{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mny = Character(_('{color=#4ED42D}М{/color}/{color=#ff367c}Н{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define msy = Character(_('{color=#4ED42D}М{/color}/{color=#34B1FF}С{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kms = Character(_('{color=#DDA0DD}К{/color}/{color=#4ED42D}М{/color}/{color=#34B1FF}С{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define mnsy = Character(_('{color=#4ED42D}М{/color}/{color=#ff367c}Н{/color}/{color=#34B1FF}С{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define knsy = Character(_('{color=#DDA0DD}К{/color}/{color=#ff367c}Н{/color}/{color=#34B1FF}С{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kmny = Character(_('{color=#DDA0DD}К{/color}/{color=#4ED42D}М{/color}/{color=#ff367c}Н{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define kmnsy = Character(_('{color=#DDA0DD}К{/color}/{color=#4ED42D}М{/color}/{color=#ff367c}Н{/color}/{color=#34B1FF}С{/color}/{color=#B957FF}Ю{/color}'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Прочие персонажи
define mr_cow = Character(_('М-р Коровка'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#fccaca")
define mr_bird = Character(_('М-р Птиц'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#dcfa64")

# Кошмары ГГ
define mmm = DynamicCharacter('mmm_name', image='monikammm', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#000", voice_tag='mmm')

# NVL-screen
define n_nvl = Character(_('Нацуки'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#ff367c", kind=nvl)
define y_nvl = Character(_('Юри'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#B957FF", kind=nvl)
define sm_nvl = Character(_('Мама'), what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#2970ff", kind=nvl)


## Variables
# This section declares variables when the mod runs for the first time on all saves.

define config.developer = False # МЕНЯТЬ ПРИ РЕЛИЗЕ!!!
define _dismiss_pause = config.developer
# define persistent.steam = ("steamapps" in config.basedir.lower())
default basedir = config.basedir.replace('\\', '/') # для Питона
default persistent.first_run = False # первый запуск мода
default persistent.lockdown_warning = False # для проверки версии Renpy и предупреждения, если она выше 8-ой
default persistent.playername = ""
default playername_raw = ""
default persistent.first_poem = False

default allow_skipping = True
default currentpos = 0


############ Mod Variables ################

default pov_key = "mc" # для диалоговых окон

default persistent.full_playthrough = False
default persistent.censorship = False
default persistent.seen_based_menu = False
default random_menu = 0
default persistent.random_menu_past = 0
default persistent.add_random_menu = 3
default splash_message = ""
default persistent.splash_message_past = ""

default persistent.streamer_detected = False

default persistent.first_phone_call = False
default persistent.first_phone_menu_action = False
default persistent.first_phone_typing = False
default persistent.first_phone_menu_apps = False
default persistent.first_phone_call = False

default sprite_main_menu_set = False
default episode = _("Пролог. День 1")
default autosave_number = 0

default nightmare_active = False
default blocker = False
default blocker_key = "poem"

default persistent.clown_ending_open = False
default persistent.secret_monika = 0

default secret_monikammm_chance = False
default persistent.secret_monikammm_active = False
default persistent.secret_monikammm_complite = False
default persistent.secret_monikammm_complite_rofl = False
default persistent.secret_monikammm_quit = False
default secret_monikammm_count = 0
default persistent.secret_monikammm_count_all_menus_limit = 0
default persistent.secret_monikammm_count_screamer_limit = 0


default mc_name = _("Макс")
default m_name = _("Моника")
default s_name = _("Сайори")
default n_name = _("Нацуки")
default y_name = _("Юри")

default k_name = _("Котоноха")
default l_name = _("Либитина")
default r_name = _("Рэйко")
default koh_name = _("Кохаку")
default sor_name = _("Сора")
default e_name = _("Эми")
default f_name = _("Фуккацуми")
default kam_name = _("Камуко")
default h_name = _("Хироши")

default mm_name = _("Харуми-сан")
default md_name = _("М-р Дэн")
default sm_name = _("Юко-сан")
default sd_name = _("Мамору-сан")
default nd_name = _("Тамоцу-сан")
default ym_name = _("Ари-сан")
default um_name = _("Дядя Мартин")
default mi_name = _("M-c Ида")

default mmm_name = _("Моникаммм")
