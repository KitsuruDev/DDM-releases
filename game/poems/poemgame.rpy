## poemgame.rpy

init python:

    class ChibiAnimation:
        def __init__(self):
            self.time = renpy.random.random() * 4 + 4
            self.pos = 0
            self.offset = 0
            self.zoom = 1

        def pause(self, trans, st, at):
            if st > self.time:
                self.time = renpy.random.random() * 4 + 4
                return None
            return 0

        def move(self, trans, st, at):
            if st > .16:
                if self.pos > 0:
                    self.pos = renpy.random.randint(-1,0)
                elif self.pos < 0:
                    self.pos = renpy.random.randint(0,1)
                else:
                    self.pos = renpy.random.randint(-1,1)
                if trans.xoffset * self.pos > 5:
                    self.pos *= -1
                return None
            trans.xzoom = -1 if self.pos > 0 else 1
            trans.xoffset += .16 * 10 * self.pos
            self.offset = trans.xoffset
            self.zoom = trans.xzoom
            return 0

    ChibiAnimation_mc = ChibiAnimation()
    ChibiAnimation_m = ChibiAnimation()
    ChibiAnimation_s = ChibiAnimation()
    ChibiAnimation_n = ChibiAnimation()
    ChibiAnimation_y = ChibiAnimation()
    ChibiAnimation_k = ChibiAnimation()
    ChibiAnimation_kam = ChibiAnimation()


screen poem_game_solo(word, chibi, x, y):
    textbutton word:
        style "poem_button_mc"
        align (x, y)
        action [Function(renpy.show, chibi), Return()]

screen poem_game_duo(word, char_key, x, y):
    textbutton word:
        style "poem_button_" + char_key
        align (x, y)
        action Return()


style poemgame_text:
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []
    yalign 0.5
    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]


########## Images ##########

# Чиби-стикер ГГ
image mc_chibi_poem:
    "mc_chibi turned"
    xoffset ChibiAnimation_mc.offset xzoom ChibiAnimation_mc.zoom
    block:
        function ChibiAnimation_mc.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_mc.move
        repeat


# Чиби-стикер Моники
image m_chibi_poem:
    "m_chibi turned"
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    block:
        function ChibiAnimation_m.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_m.move
        repeat

image m_chibi_poem hop:
    "m_chibi hop"
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "m_chibi_poem"


# Чиби-стикер Сайори
image s_chibi_poem:
    "s_chibi turned"

    xoffset ChibiAnimation_s.offset xzoom ChibiAnimation_s.zoom
    block:
        function ChibiAnimation_s.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_s.move
        repeat
    xoffset ChibiAnimation_s.offset xzoom ChibiAnimation_s.zoom

image s_chibi_poem hop:
    "s_chibi hop"
    xoffset ChibiAnimation_s.offset xzoom ChibiAnimation_s.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "s_chibi_poem"


# Чиби-стикер Нацуки
image n_chibi_poem:
    "n_chibi turned"
    xoffset ChibiAnimation_n.offset xzoom ChibiAnimation_n.zoom
    block:
        function ChibiAnimation_n.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_n.move
        repeat

image n_chibi_poem hop:
    "n_chibi hop"
    xoffset ChibiAnimation_n.offset xzoom ChibiAnimation_n.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "n_chibi_poem"


# Чиби-стикер Юри
image y_chibi_poem:
    "y_chibi turned"
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom
    block:
        function ChibiAnimation_y.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_y.move
        repeat

image y_chibi_poem hop:
    "y_chibi hop"
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "y_chibi_poem"

image y_chibi_poem_cut:
    "y_chibi turned rcut"
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom
    block:
        function ChibiAnimation_y.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_y.move
        repeat

image y_chibi_poem_cut hop:
    "y_chibi hop rcut"
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "y_chibi_poem_cut"


# Чиби-стикер Котонохи
image k_chibi_poem:
    "k_chibi turned"
    xoffset ChibiAnimation_k.offset xzoom ChibiAnimation_k.zoom
    block:
        function ChibiAnimation_k.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_k.move
        repeat

image k_chibi_poem hop:
    "k_chibi hop"
    xoffset ChibiAnimation_k.offset xzoom ChibiAnimation_k.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "k_chibi_poem"


# Чиби-стикер Камуко
image kam_chibi_poem:
    "kam_chibi turned headphones"
    xoffset ChibiAnimation_kam.offset xzoom ChibiAnimation_kam.zoom
    block:
        function ChibiAnimation_kam.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_kam.move
        repeat


###### Хоррорная часть ######

# Чиби-стикер-смесь героинь Литературного клуба
image mix_chibi glitch:
    "mod_assets/sprites/characters/chibi/mix_glitch/1.png"
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    block:
        function ChibiAnimation_m.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_m.move
        repeat

image mix_chibi glitch hop:
    "mod_assets/sprites/characters/chibi/mix_glitch/2.png"
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "mix_chibi glitch"


# Чиби-стикер Нацуки с пиксельными глазами и наклонённой головой
image n_chibi_poem glitch:
    size (226, 184)
    "mod_assets/sprites/characters/chibi/n_glitch/1.png"
    xoffset ChibiAnimation_n.offset xzoom ChibiAnimation_n.zoom
    chibi_hop


# Чиби-стикер нарисованной Сайори
image s_chibi_poem drawing:
    "mod_assets/sprites/characters/chibi/s_drawing/1.png"
    size (134, 196)
    xoffset ChibiAnimation_s.offset xzoom ChibiAnimation_s.zoom
    block:
        function ChibiAnimation_s.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_s.move
        repeat

image s_chibi_poem drawing hop:
    "mod_assets/sprites/characters/chibi/s_drawing/2.png"
    size (134, 196)
    xoffset ChibiAnimation_s.offset xzoom ChibiAnimation_s.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "s_chibi_poem drawing"


# Сломанный чиби-стикер Юри, увеличенный в несколько раз
image y_chibi_poem glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            chibi_move
        parallel:
            function randomMoveYuri
        repeat

# Чиби-стикер Юри с лицом из японского хоррора
image y_chibi_poem hopg:
    "gui/poemgame/y_sticker_2g.png"
    size (128, 184)
    xoffset ChibiAnimation_y.offset xzoom ChibiAnimation_y.zoom
    chibi_hop


# Чиби-стикер Моникаммм
image mmm_chibi_poem:
    "mod_assets/sprites/characters/chibi/mmm/1.png"
    size (139, 196)
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    block:
        function ChibiAnimation_m.pause
        parallel:
            chibi_move
        parallel:
            function ChibiAnimation_m.move
        repeat

image mmm_chibi_poem hop:
    "mod_assets/sprites/characters/chibi/mmm/2.png"
    size (139, 196)
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    chibi_hop
    xoffset 0 xzoom 1
    "mmm_chibi_poem"

image mmm_chibi_poem big hop:
    "mod_assets/sprites/characters/chibi/mmm/2.png"
    size (139, 196)
    xoffset ChibiAnimation_m.offset xzoom ChibiAnimation_m.zoom
    chibi_hop(-180)
    xoffset 0 xzoom 1
    "mmm_chibi_poem"



########## Transform ##########

# Позиция стикеров на середине тетради
transform chibi_pos_center(x):
    subpixel True
    xcenter x yalign 0.5

transform st_c21:
    chibi_pos_center(250)
transform st_c22:
    chibi_pos_center(1030)


# Позиция стикеров внизу тетради
transform chibi_pos_down(x):
    subpixel True
    xcenter x yalign 0.9

transform c_d41:
    chibi_pos_down(250)
transform c_d42:
    chibi_pos_down(480)
transform c_d43:
    chibi_pos_down(800)
transform c_d44:
    chibi_pos_down(1030)

transform c_d51:
    chibi_pos_down(250)
transform c_d52:
    chibi_pos_down(445)
transform c_d53:
    chibi_pos_down(640)
transform c_d54:
    chibi_pos_down(835)
transform c_d55:
    chibi_pos_down(1030)


# Подпрыгивание при перемещении
transform chibi_move:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

# Прыжок
transform chibi_hop(y = -80):
    easein_quad .18 yoffset y
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset y
    easeout_quad .18 yoffset 0



########## Прочее ##########

### Стили кнопок при написании стихотворений

style poem_button_mc is poem_button_base
style poem_button_n is poem_button_base
style poem_button_y is poem_button_base
style poem_button_y_seizure is poem_button_base

style poem_button_mc_text is poem_button_base_text
style poem_button_n_text is poem_button_base_text
style poem_button_y_text is poem_button_base_text
style poem_button_y_seizure_text is poem_button_base_text

style poem_button_base:
    properties gui.button_properties("confirm_button")
    activate_sound "mod_assets/sound/modding/buttons/word/select.mp3"

style poem_button_base_text:
    outlines []
    color "#000"
    hover_color gui.hover_color


# Стиль ГГ
style poem_button_mc:
    hover_sound "mod_assets/sound/modding/buttons/word/hover_mc.mp3"

style poem_button_mc_text:
    font "mod_assets/font/poem/mc_font.ttf"
    size 26


# Стиль Нацуки
style poem_button_n:
    hover_sound "mod_assets/sound/modding/buttons/word/hover_n.mp3"

style poem_button_n_text:
    font "mod_assets/font/poem/n_font.ttf"
    size 50
    line_leading 1


# Стиль Юри
style poem_button_y:
    hover_sound "mod_assets/sound/modding/buttons/word/hover_y.mp3"

style poem_button_y_text:
    font "mod_assets/font/poem/y_font.ttf"
    size 35
    line_leading 5

style poem_button_y_seizure:
    hover_sound "mod_assets/sound/modding/buttons/word/hover_y_seizure.mp3"

style poem_button_y_seizure_text:
    font "mod_assets/font/poem/y_seiz_font.ttf"
    size 35
    line_leading 5
