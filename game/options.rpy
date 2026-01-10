## This template version is 4.0.0. When asked to provide the template version you are using, give them this version number.
### DO NOT REMOVE OR CHANGE THE ABOVE COMMENT. ###

## options.rpy

define config.name = "Doki Doki Метанойя"
define config.version = "Alpha-1.0"

# name of your mod build when you package mod in the Ren'Py Launcher or DDMM (Doki Doki Mod Maker)
# Note:
#   The build name is ASCII only - no numbers, spaces, semicolons
#   Example: Doki Doki Yuri Time to DokiDokiYuriTime
define build.name = "DDM"
define build.version = "Alpha"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.voice_filename_format = "mod_assets/voice/{filename}.mp3"

init python:
    def game_menu_music_active():
        if renpy.music.is_playing(channel='music') or renpy.music.is_playing(channel='music_poem'):
            track = None
        else:
            track = audio.mod_game_menu if not getattr(renpy.store, 'nightmare_active', False) else audio.mod_game_menu_nightmare
        config.game_menu_music = track

define config.main_menu_music = audio.mod_main_menu_after_disclaimer
define config.context_callback = game_menu_music_active

define config.enter_transition = MultipleTransition([
    False, Dissolve(0.05), Solid("#ebebeb"),
    Pause(0.05),
    Solid("#ebebeb"), Dissolve(0.2), True])
define config.exit_transition = Dissolve(.2)
define config.after_load_transition = Dissolve(.2)
define config.end_game_transition = Dissolve(.5)

# "auto" - hide textbox during scenes and show when a character speaks
# "show" - show textbox at all times
# "hide" - only show dialogue when a character speaks.
define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 50
default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
default preferences.voice_volume = 0.75

# save folder name of your mod
# Finding your Saves:
#   Windows: %AppData%/RenPy/
#   macOS: $HOME/Library/RenPy/ (Un-hide the Library Folder)
#   Linux: $HOME/.renpy/
define config.save_directory = "DDM_Alpha_CBT"

define config.window_icon = "mod_assets/elements/logo/window_icon.png"

# whether your mod allows the player to skip dialogue
define config.allow_skipping = True

# отключено из-за своей «системы» автосохранений
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0

define config.rollback_enabled = config.developer

define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1:
        del(renpy.loadsave.location.locations[1])

    renpy.game.preferences.pad_enabled = False

    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s

    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu:
            renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)


## Build configuration #########################################################
##
## how Ren'Py turns your project into distribution files.

init python:
    ## The following variables take file patterns. File patterns are case-insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is used.
    ##
    ## In a pattern:
    ##  * matches all characters, except the directory separator.
    ##  ** matches all characters, including the directory separator.
    ##
    ## Examples:
    ##  "*.txt" matches txt files in the base directory.
    ##  "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories.
    ##  "**.psd" matches psd files anywhere in the project.

    # These variables declare the packages to build your mod that is Team Salvato
    # IPG compliant. Do not mess with these variables whatsoever.
    build.package("Renpy8-DDLCMod", 'zip', 'windows linux mac renpy mod', description="Ren'Py 8 DDLC Compliant Mod")

    # These variables declare the archives that will be made to your packaged mod.
    # To add another archive, make a build.archive variable like in this example:
    build.archive("scripts", 'mod')
    build.archive("mod_assets", 'mod')

    # Do not touch these lines. This is so Ren'Py can add your mods' py file
    # and a special launcher for Linux and macOS to run your mod.
    try:
        build.renpy_patterns.remove(('renpy.py', ['all']))
        build.classify_renpy("renpy.py", "renpy all")
    except: pass

    try:
        build.early_base_patterns.remove(('*.sh', None))
        build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
        build.classify("*.sh", None)
    except: pass

    #############################################################
    # These variables classify packages for PC and Android platforms.
    # Make sure to add 'all' to your build.classify variable if you are planning
    # to build your mod on Android like in this example.
    #   Example: build.classify("game/**.pdf", "scripts all")

    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/phone/assets/**", "mod_assets all")

    build.classify("game/presplash.png", "scripts all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/**.txt", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") ## Backwards Compatibility
    build.classify("game/tl/**", "scripts all") ## Translation Folder

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.rpa', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)

    build.include_olds = False
