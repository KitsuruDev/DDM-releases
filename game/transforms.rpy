## transforms.rpy

transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein 0.25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein 0.55 xcenter x zoom z*1.00
        parallel:
            easein 0.15 yoffset 0 ypos 1.03

# tcommon без анимаций появления и пропадания
transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0


transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein 0.3 xoffset 20
        ease 0.6 xoffset -20
        easeout 0.3 xoffset 0
        repeat


transform leftin(x=640, z=0.80, t=0.55):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein t xcenter x

transform rightin(x=640, z=0.80, t=0.55):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein t xcenter x


transform face(z=0.80, y=500):
    subpixel True xcenter 640 yanchor 1.0 ypos 1.03 yoffset y zoom z*2.00

transform eyes(x=640, y=500, z=0.80):
    subpixel True xcenter x yanchor 1.0 ypos 1.23 yoffset y zoom z*2.00
    on show:
        alpha 0.00
        linear 0.25 alpha 1.00
    on hide:
        alpha 1.00
        linear 0.25 alpha 0.00


transform tphone(y = 280):
    xcenter 152 ycenter y
    zoom 0.8


transform thide(z=0.80):
    subpixel True transform_anchor True
    on hide:
        easein 0.25 zoom z*0.95 alpha 0.00 yoffset -20

transform lhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter -300

transform rhide:
    subpixel True
    on hide:
        easeout 0.25 xcenter 1580


transform t51:
    tcommon(130)
transform t52:
    tcommon(385)
transform t53:
    tcommon(640)
transform t54:
    tcommon(895)
transform t55:
    tcommon(1150)
transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

transform i51:
    tinstant(130)
transform i52:
    tinstant(385)
transform i53:
    tinstant(640)
transform i54:
    tinstant(895)
transform i55:
    tinstant(1150)
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

transform s51:
    sink(130)
transform s52:
    sink(385)
transform s53:
    sink(640)
transform s54:
    sink(895)
transform s55:
    sink(1150)
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

transform h51:
    hop(130)
transform h52:
    hop(385)
transform h53:
    hop(640)
transform h54:
    hop(895)
transform h55:
    hop(1150)
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

transform l51:
    leftin(130)
transform l52:
    leftin(385)
transform l53:
    leftin(640)
transform l54:
    leftin(895)
transform l55:
    leftin(1150)
transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)

transform r51:
    rightin(130)
transform r52:
    rightin(385)
transform r53:
    rightin(640)
transform r54:
    rightin(895)
transform r55:
    rightin(1150)
transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)

transform j51:
    jugging_sprite(130)
transform j52:
    jugging_sprite(385)
transform j53:
    jugging_sprite(640)
transform j54:
    jugging_sprite(895)
transform j55:
    jugging_sprite(1150)
transform j41:
    jugging_sprite(200)
transform j42:
    jugging_sprite(493)
transform j43:
    jugging_sprite(786)
transform j44:
    jugging_sprite(1080)
transform j31:
    jugging_sprite(240)
transform j32:
    jugging_sprite(640)
transform j33:
    jugging_sprite(1040)
transform j21:
    jugging_sprite(400)
transform j22:
    jugging_sprite(880)
transform j11:
    jugging_sprite(640)

transform e21:
    eyes(275)
transform e22:
    eyes(925)
transform e11:
    eyes(640)

# для низких персонажей
transform el11:
    eyes(640, 400)


###### Переходы ######

define dissolve = Dissolve(0.25)
define dissolve_cg = Dissolve(0.75)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0), Solid("#000"),
    Pause(1.0),
    Solid("#000"), Dissolve(1.0), True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"),
    Pause(1.0),
    Solid("#000"), Dissolve(1.0), True])

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64), Solid("#000"),
    Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64), True])


###### Эффекты ######

# Потемнение по краям
image vignette:
    truecenter
    "images/bg/vignette.png"

# Пульсирование экрана с приближением
transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

# Потемнения при тряске
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

# Тряска при фейковом пропуске текста
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

transform heartbeat(m, t1=0, t2=0):
    truecenter
    parallel:
        t1
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.279 zoom 1.00 + 0.07 * m
        zoom 1.00
        t2
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat



################################### Mod ###################################

################ Экраны ################

transform call_screen_fade(t=0.25):
    on show:
        alpha 0.0
        ease t alpha 1.0


################ Позиции спрайтов ################

# Моника в позе lean выглядывает справа
transform t_monika_watch:
    tcommon(1300)


################ Анимации экрана и спрайтов ################

# ДЛЯ РЕЗКИХ ПРЫЖКОВ ПОСЛЕ face/eyes
transform tfast(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

# Влетание персонажа в игрока (иллюзия параболы - напрыгивает)
transform movein_hugs:
    align (0.5, 0.6) anchor (0.5, 0.5) alpha 0 zoom 0
    linear 0.1 zoom 1 alpha 1
    linear 0.4 zoom 5 yalign 0.3

transform dizzy(x, t):
    subpixel True
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * x
        ease 0.75 * t xoffset 5 * x
        ease 0.75 * t xoffset -5 * x
        ease 0.75 * t xoffset -3 * x
        ease 0.75 * t xoffset -10 * x
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * x
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * x
        ease 2.0 * t yoffset -5 * x
        easein 1.0 * t yoffset 0
        repeat

# Дрожание для слоя master
transform stress(x=1.0, t=1.0):
    anchor (0.5, 0.5) pos (640, 360) zoom 1.05
    dizzy(x, t)

# Дрожание (спрайт)
transform tremble(x=640, y=0, z=0.8):
    xcenter x yoffset y zoom z
    block:
        choice:
            block:
                linear 0.05 xoffset 10
                linear 0.05 xoffset -10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
        choice:
            block:
                linear 0.05 xoffset -10
                linear 0.05 xoffset 10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
        repeat

# Бег (фон/экран) - приближение c тряской
transform run_center:
    subpixel True
    align (0.5, 0.5) anchor (0.5, 0.5) zoom 1.0 yoffset 0
    parallel:
        block:
            easein 0.15 yoffset 20
            easeout 0.15 yoffset 0
            easein 0.15 yoffset -20
            easeout 0.15 yoffset 0
            repeat
    parallel:
        linear 7.5 zoom 4.0

# Бег (фон/экран) - тряска
transform run_shaking:
    subpixel True
    align (0.5, 0.5) anchor (0.5, 0.5) zoom 1.25 yoffset 0
    block:
        easein 0.15 yoffset 15
        easeout 0.15 yoffset 0
        easein 0.15 yoffset -15
        easeout 0.15 yoffset 0
        repeat

# Пробежка (фон/экран) - лёгкая тряска
# 0.2, 0.3 - обычная пробежка
# 0.4, 0.4 - лёгкая пробежка
transform jugging(t1=0.2, t2=0.3):
    subpixel True align (0.5, 0.5) anchor (0.5, 0.5) zoom 1.25 yoffset 0
    block:
        easein t1 yoffset 15
        easeout t2 yoffset 0
        repeat

# Пробежка/бег (спрайт)
transform jugging_sprite(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
        block:
            easein 0.15 yoffset 15
            easeout 0.25 yoffset 0
            repeat
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03
        parallel:
            easein 0.15 yoffset 15
            easeout 0.25 yoffset 0
            repeat


# 640 - угол, 1000 - стеллажи
transform sayori_shop(x = 640):
    subpixel True xcenter x yanchor 1.0 ypos 1.35 zoom 0.80*1.25 alpha 0
    easein 0.25 alpha 1.0


transform natsuki_ghost_run_animation:
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat


################ Различные места - приближения ################

## Школа

# Крыша старого корпуса - забор
transform old_rooftop_fence:
    anchor (0.3, 0.2) zoom 4.0

# Музыкальный класс - рояль
transform class_music_piano:
    anchor (0.01, 0.41) zoom 4.5

# Правая лестница на первом этаже старого корпуса (любимое место Юри)
transform f1_old_stairwell_right_board:
    anchor (0.15, 0.25) zoom 2.5


################ Дома - приближения слоя master ################

## ГГ:

# Кровать ГГ (с тумбочкой)
transform mc_bed:
    anchor (0.44, 0.44) zoom 3.0

# Кровать ГГ (между подушек)
transform mc_bed_deep:
    anchor (0.755, 0.57) zoom 5.0

# Стол ГГ на кухне
transform mc_kitchen_table: # если ГГ сидит с персонажем
    anchor (0.2, 0.44) zoom 5.0
transform mc_kitchen_table_alone: # если ГГ один
    anchor (0.15, 0.44) zoom 3.5


## Моника:

# Калитка снаружи
transform monika_gate:
    anchor (0.15, 0.5) zoom 3.0

# Диван Моники
transform monika_sofa:
    anchor (0.6, 0.41) zoom 4.0

# Кровать Моники
transform monika_bed:
    anchor (0.01, 0.51) zoom 3.5

# Стол Моники на кухне
transform monika_kitchen_table:
    anchor (0.54, 0.34) zoom 4.25


## Сайори:

# Диван Сайори
transform sayori_sofa:
    anchor (0.25, 0.39) zoom 4.0


## Юри:

# Калитка снаружи
transform yuri_gate:
    anchor (0.35, 0.55) zoom 4.0

# Диван Юри
transform yuri_sofa:
    anchor (0.6, 0.25) zoom 4.5

# Кровать Юри
transform yuri_bed:
    anchor (0.2, 0.41) zoom 3.0

# Стол Юри на кухне (основной)
transform yuri_kitchen_table: # два дальних места
    anchor (0.24, 0.25) zoom 3.75
transform yuri_kitchen_table_fifth_place: # пятое место справа от стола
    anchor (0.5, 0.25) zoom 3.75


################ Прочее ################

## Значок загрузки в переходах по сюжету
transform loading_sign_position:
    subpixel True
    size (128, 128) align (0.9, 0.9)
    block:
        rotate 0
        linear 1.85 rotate 360
        repeat

## Область для отображения подсказки
transform hint_position:
    subpixel True
    pos (-200, 589)
    on show:
        easein_back 1.0 xpos 0
    on hide:
        easeout_back 1.0 xpos -300
