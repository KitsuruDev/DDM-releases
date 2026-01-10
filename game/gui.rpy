## gui.rpy

init -2 python:
    gui.init(1280, 720)


## GUI Sounds

define -2 gui.hover_sound = "mod_assets/sound/modding/buttons/button/hover.mp3" # Hover Sound Effect
define -2 gui.activate_sound = "mod_assets/sound/modding/buttons/button/select.mp3" # Click Sound Effect
define -2 gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg" # Glitched Sound Effect


## Colors

# label and highlight text
define -2 gui.accent_color = '#ffffff'

# text button when it is neither selected nor hovered
define -2 gui.idle_color = '#aaaaaa'

# small text, which needs to be brighter/darker to achieve the same effect
define -2 gui.idle_small_color = '#333'

# buttons and bars that are hovered
define -2 gui.hover_color = '#cc6699'

# text button when it is selected but not focused
define -2 gui.selected_color = '#bb5588'

# text button when it cannot be selected
define -2 gui.insensitive_color = '#aaaaaa7f'

# bars that are not filled in completely. They are not used directly, but are used when re-generating bar image files.
define -2 gui.muted_color = '#6666a3'
define -2 gui.hover_muted_color = '#9999c1'

# dialogue and menu choice text.
define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes

define -2 gui.default_font = "mod_assets/font/menu/UZSans-Regular.ttf"
define -2 gui.name_font = "mod_assets/font/menu/UZSans-SemiBold.ttf"
define -2 gui.interface_font = "mod_assets/font/menu/Vivl-rail.ttf"

define -2 gui.text_size = 24
define -2 gui.name_text_size = 24
define -2 gui.interface_text_size = 24

define -2 gui.label_text_size = 28 # user interface
define -2 gui.notify_text_size = 16 # notify_text
define -2 gui.title_text_size = 38 # main_menu_text


## Main Menu and Game Menu

define -2 gui.main_menu_background = "menu_bg"
default game_menu_background_color = "#ffe8f8d7"


## Dialogue

define -2 gui.textbox_height = 182
define -2 gui.textbox_yalign = 0.99

define gui.name_xpos = 350
define gui.name_ypos = -5
define gui.name_xalign = 0.5

define gui.namebox_width = 176
define gui.namebox_height = 42
define gui.namebox_borders = Borders(5, 12, 5, 2)
define gui.namebox_tile = False # frame containing the namebox

define gui.text_xpos = 268
define gui.text_ypos = 57
define gui.text_width = 744
define gui.text_xalign = 0.0


## Buttons

define gui.button_width = None # Ren'Py computes size automatically
define gui.button_height = 36
define gui.button_borders = Borders(4, 4, 4, 4)

# whether the button background is tiled and increase/decrease its' size or are centered and scale
# True - Button BG is Tiled | False - Button BG is centered.
define gui.button_tile = False
define gui.button_text_font = gui.interface_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

define gui.radio_button_borders = Borders(28, 4, 4, 4)
define gui.check_button_borders = Borders(28, 4, 4, 4)
define gui.confirm_button_text_xalign = 0.5
define gui.page_button_borders = Borders(10, 4, 10, 4)


## Choice Buttons

define gui.choice_button_width = 420
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(20, 13, 20, 5)
define gui.choice_button_text_font = gui.default_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#000"
define gui.choice_button_text_hover_color = "#fa9"


## File Slot Buttons

define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_hover_color = gui.hover_color

# thumbnails screenshots of saves
define config.thumbnail_width = 256
define config.thumbnail_height = 144

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing

define gui.navigation_xpos = 40
define gui.skip_ypos = 10
define gui.notify_ypos = 45
define gui.choice_spacing = 22
define gui.navigation_spacing = 7
define gui.pref_spacing = 10
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.slot_spacing = 10

## Frames

define gui.frame_borders = Borders(4, 4, 4, 4)
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define gui.skip_frame_borders = Borders(16, 5, 50, 5)
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

# whether the frames should be tiled or scaled.
# True - Button BG is Tiled | False - Button BG is centered.
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders

define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30

# whether the frames should be tiled or scaled.
# True - Button BG is Tiled | False - Button BG is centered.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

# what to do with bars that cannot be scrolled.
# "hide" - hides the bar | None - keeps the bar shown
define gui.unscrollable = "hide"

## History

define config.history_length = 50

define gui.history_height = None # make the height vary at a cost to performance

define gui.history_name_xpos = 185
define gui.history_name_ypos = 2
define gui.history_name_width = 200
define gui.history_name_xalign = 1.0

define gui.history_text_xpos = 205
define gui.history_text_ypos = 5
define gui.history_text_width = 700
define gui.history_text_xalign = 0.0

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art", "s", "size", "b", "color", "image", "space" } # sc, bt убраны из-за «тормозов»


## NVL

define gui.nvl_borders = Borders(0, 10, 0, 20)
define gui.nvl_height = 115 # None allow each NVL entry to vary in size.
define gui.nvl_spacing = 10

define gui.nvl_name_xpos = 345
define gui.nvl_name_ypos = 7
define gui.nvl_name_width = 100
define gui.nvl_name_xalign = 1.0

define gui.nvl_text_xpos = 365
define gui.nvl_text_ypos = 7
define gui.nvl_text_width = 640
define gui.nvl_text_xalign = 0.0

# narrator's dialogue
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


## Mobile Phones & Tablets

init python:

    # changes the size and spacing of various GUI elements to ensure they are easily visible on smaller devices
    if renpy.variant("small"):

        gui.text_size = 24
        gui.name_text_size = 24
        gui.notify_text_size = 24
        gui.interface_text_size = 26
        gui.button_text_size = 26
        gui.label_text_size = 28

        gui.textbox_height = 182
        gui.name_xpos = 350
        gui.text_xpos = 268
        gui.text_ypos = 62
        gui.text_width = 744
        gui.text_xalign = 0.0

        gui.choice_button_width = 420

        gui.navigation_spacing = 6
        gui.pref_button_spacing = 10

        gui.history_height = None
        gui.history_text_width = 650

        gui.file_slot_cols = 3
        gui.file_slot_rows = 2

        gui.nvl_height = 115

        gui.nvl_name_width = 150
        gui.nvl_name_xpos = 430

        gui.nvl_text_width = 590
        gui.nvl_text_xpos = 450
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 780
        gui.nvl_thought_xpos = 240

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 450
