## cgs.rpy

############################################## АКТ 1 «НОВАЯ ЖИЗНЬ» ##############################################


############################## ДЕНЬ 1 ##############################

### Юри читает книгу у стены:

# Фон (с бликами)
image y_cg2_bg:
    "images/cg/y_cg2_bg1.png"
    6.0
    "images/cg/y_cg2_bg2.png" with Dissolve(1)
    2
    "images/cg/y_cg2_bg1.png" with Dissolve(1)
    1
    repeat

# Cпокойный взгляд Юри на книгу + шоколад во рту
image y_cg2_base:
    "images/cg/y_cg2_base.png"

# Рот Юри без шоколада, слегка приоткрыт
image y_cg2_nochoc:
    "images/cg/y_cg2_nochoc.png"

# Блики на теле Юри
image y_cg2_details:
    "images/cg/y_cg2_details.png"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

# Шокированные глаза Юри
image y_cg2_exp2:
    "images/cg/y_cg2_exp2.png"

# Глаза Юри смотрят на ГГ
image y_cg2_exp3:
    "images/cg/y_cg2_exp3.png"

# Частицы пыли на свету
image y_cg2_dust1:
    "images/cg/y_cg2_dust1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 14.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust2:
    "images/cg/y_cg2_dust2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 32.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust3:
    "images/cg/y_cg2_dust3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 17.0 xoffset -100 yoffset 100
        repeat

image y_cg2_dust4:
    "images/cg/y_cg2_dust4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear 19.0 xoffset -100 yoffset 100
        repeat



############################## ДЕНЬ 2 ##############################

### Юри читает книгу на парте:

# Фон + спокойный взгляд Юри на книгу
image y_cg1_base:
    "images/cg/y_cg1_base.png"

# Глаза Юри смотрят на ГГ
image y_cg1_exp1:
    "images/cg/y_cg1_exp1.png"

# Улыбка Юри
image y_cg1_exp2:
    "images/cg/y_cg1_exp2.png"

# Бесспокойный взгляд Юри на книгу (яндере)
image y_cg1_exp3:
    "images/cg/y_cg1_exp3.png"



############################## ДЕНЬ 4 ##############################

### Нацуки в кладовке с коробкой в руках на стуле:

# Фон
image n_cg2_bg:
    "images/cg/n_cg2_bg.png"

# Радостное выражение лица Нацуки, взгляд в сторону
image n_cg2_base:
    "images/cg/n_cg2_base.png"

# Удивлённое выражение лица Нацуки, взгляд на ГГ
image n_cg2_exp1:
    "images/cg/n_cg2_exp1.png"

# Паническое выражение лица Нацуки, глаза закрыты
image n_cg2_exp2:
    "images/cg/n_cg2_exp2.png"

# Уставшее выражение лица Нацуки, взгляд в сторону
image n_cg2_exp3:
    "mod_assets/cg/main_history/act_1/day_4/n_exp3.png"

# Единичное дёрганье спрайта Нацуки
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

# Зацикленное дёрганье спрайта Нацуки
transform n_cg2_wiggle_loop:
    subpixel True
    xoffset 0
    block:
        easein 0.15 xoffset 10
        easeout 0.15 xoffset 0
        easein 0.15 xoffset -15
        easeout 0.15 xoffset 0
        easein 0.15 xoffset 15
        easeout 0.15 xoffset 0
        easein 0.15 xoffset -10
        ease 0.15 xoffset 0
        repeat



### Нацуки сидит на полу у кладовки рядом с ГГ:

# Фон
image n_cg1_bg:
    "images/cg/n_cg1_bg.png"

# Удивлённое выражение лица Нацуки, взгляд на ГГ
image n_cg1_base:
    "images/cg/n_cg1_base.png"

# Радостное выражение лица Нацуки, глаза закрыты
image n_cg1_exp1:
    "images/cg/n_cg1_exp1.png"

# Нервно-злое выражение лица Нацуки, взгляд в сторону
image n_cg1_exp2:
    "images/cg/n_cg1_exp2.png"

# Злое выражение лица Нацуки (ГЛАЗ НЕТ - ИСПОЛЬЗОВАТЬ BASE)
image n_cg1_exp3:
    "images/cg/n_cg1_exp3.png"

# Спящее выражение лица Нацуки, глаза закрыты
image n_cg1_exp4:
    "images/cg/n_cg1_exp4.png"

# Уставшее выражение лица Нацуки, взгляд на ГГ
image n_cg1_exp5:
    "images/cg/n_cg1_exp5.png"



############################## ДЕНЬ 5 ##############################

### Повешенная Сайори в своей комнате (кошмар ГГ):

# Sayori's Room
image s_kill_bg:
    "images/cg/s_kill_bg.png"
    subpixel True

# Sayori hanging in the CG
image s_kill:
    "images/cg/s_kill.png"
    subpixel True

# Glitched background
image s_kill_bg2:
    "images/cg/s_kill_bg2.png"
    subpixel True

# Glitched sprite of Sayori hanging
image s_kill2:
    "images/cg/s_kill2.png"
    subpixel True

# Starts off the animation for the background
transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

# Starts off the animation for Sayori's hanging sprite
transform s_kill_start:
    truecenter
    zoom 0.8 align (0.3, 0.25)
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

# Zooms in on the background
image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        align (0.2, 0.3) zoom 2.0
    dizzy(0.25, 1.0)

# Zooms in on Sayori's hanging sprite
image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        align (0.5, 0.05) zoom 2.0
    dizzy(1, 1.0)

# Повторный спрайт Сайори для эффекта расплывания
image s_kill_zoom_trans:
    contains:
        "s_kill"
        truecenter
        align (0.5, 0.05) zoom 2.0 alpha 0.5
    0.5
    dizzy(1, 1.0)

# Zooms in on the glitched background
image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        align (0.2, 0.3) zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

# Zooms in on the glitched Sayori hanging sprite
image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        align (0.5, 0.05) zoom 2.0
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat



############################## ДЕНЬ 6 ##############################

### Грустная Сайори в кровати:

# Фон с Сайори
image sayori_cg_act_1_day_6:
    "mod_assets/cg/main_history/act_1/day_6/s.png"



### ГГ обнимает расстроенную Сайори у её дома (ОТЗЕРКАЛЕНО для правильного отображения):

# Фон + заплаканное лицо Сайори
image s_cg3:
    "images/cg/s_cg3.png"
    xzoom -1



############################## ДЕНЬ 7 ##############################

### ГГ поймал Нацуки на своей кухне:

# Фон + расстроенное выражение лица Нацуки, взгляд на ГГ
image n_cg3_base:
    "images/cg/n_cg3_base.png"

# Глазурь на пальце правой руки Нацуки
image n_cg3_cake:
    "images/cg/n_cg3_cake.png"

# Радостное выражение лтица Нацуки, глаза закрыты
image n_cg3_exp1:
    "images/cg/n_cg3_exp1.png"

# Шокированное выражение лица Нацуки, взгляд на ГГ
image n_cg3_exp2:
    "images/cg/n_cg3_exp2.png"



### Кексы в доме ГГ:

# Фон
image cupcakes_cg_act_1_day_7:
    "mod_assets/cg/main_history/act_1/day_7/cup.png"



############################## ДЕНЬ 8 ##############################

### ГГ поправляет одежду Сайори в классе:

# Фон + уставшее выражение лица Сайори, взгляд на ГГ
image s_cg1_base:
    "images/cg/s_cg1.png"

# Радостное лицо Сайори, взгляд на ГГ
image s_cg1_exp1:
    "mod_assets/cg/main_history/act_1/day_8/s_exp1.png"

# Зажмуренное лицо Сайори, глаза закрыты
image s_cg1_exp2:
    "mod_assets/cg/main_history/act_1/day_8/s_exp2.png"



############################## ДЕНЬ 10 ##############################

### Хоррорное дополнение к CG, где Нацуки в кладовке с коробкой в руках на стуле (день 4) (кошмар ГГ):
image n_cg2_base_horror:
    "mod_assets/cg/main_history/act_1/day_10/n_base_horror.png"

# Для gallery_cg
image n_cg2_base_horror_gallery_cg:
    "n_cg2_base"
    choice:
        0.5
    choice:
        1.5
    choice:
        2.0
    choice:
        2.5
    choice:
        3.0
    choice:
        3.5
    choice:
        4.0
    "mod_assets/cg/main_history/act_1/day_10/n_base_horror.png"
    choice:
        0.10
    choice:
        0.15
    choice:
        0.20
    repeat



### Хоррорное дополнение к CG, где Нацуки сидит на полу у кладовки рядом с ГГ (день 4) (кошмар ГГ):

# Кошмарная версия Нацуки (пиксели на глазах)
image n_cg1b = Composite((1280, 720), (0, 0), "images/cg/n_cg1b.png", (882, 325), "n_rects1", (732, 400), "n_rects2", (850, 475), "n_rects3")

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    xysize (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    xysize (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    xysize (30, 20)



############################## ДЕНЬ 11 ##############################

### Юри держит руку ГГ с полотенцем в спальне дома ГГ:

# Фон + взгляд Юри на ГГ
image y_cg3_base:
    "images/cg/y_cg3_base.png"

# Закрытые глаза Юри
image y_cg3_exp1:
    "images/cg/y_cg3_exp1.png"



### Скример с Моникаммм после экрана BSOD (кошмар ГГ):
image monikammm_cg_act_1_day_11:
    "mod_assets/cg/main_history/act_1/day_11/mmm.png"

# Для gallery_cg
image monikammm_cg_act_1_day_11_gallery_cg:
    "mod_assets/cg/main_history/act_1/day_11/mmm.png"
    subpixel True zoom 1.2
    block:
        linear 0.01 rotate 5
        linear 0.01 rotate 0
        linear 0.01 rotate -5
        linear 0.01 rotate 0
        repeat



############################## ДЕНЬ 12 ##############################

### Сайори врезалась в косяк у кладовки и держится за голову:

# Фон + открытый правый глаз и улыбка на лице
image s_cg2_base1:
    "images/cg/s_cg2_base1.png"

# Фон + открытый правый глаз и улыбка на лице + бутылка у лба
image s_cg2_base2:
    "images/cg/s_cg2_base2.png"

# Искривлённый от боли рот
image s_cg2_exp1:
    "images/cg/s_cg2_exp1.png"

# Закрытый рот
image s_cg2_exp2:
    "images/cg/s_cg2_exp2.png"

# Закрытый правый глаз
image s_cg2_exp3:
    "images/cg/s_cg2_exp3.png"



### Убитая ножом Юри на полу в классе (кошмар ГГ):
image y_kill = ConditionSwitch(
    "yuri_ghost_death >= 2380", "images/cg/y_kill/3a.png",
    "yuri_ghost_death >= 1980", "images/cg/y_kill/3c.png",
    "yuri_ghost_death >= 1820", "images/cg/y_kill/3b.png",
    "yuri_ghost_death >= 1520", "images/cg/y_kill/3a.png",
    "yuri_ghost_death >= 1220", "images/cg/y_kill/2c.png",
    "yuri_ghost_death >= 1060", "images/cg/y_kill/2b.png",
    "yuri_ghost_death >= 760", "images/cg/y_kill/2a.png",
    "yuri_ghost_death >= 460", "images/cg/y_kill/1c.png",
    "yuri_ghost_death >= 300", "images/cg/y_kill/1b.png",
    "True", "images/cg/y_kill/1a.png",
    )



############################## ДЕНЬ 13 ##############################

### Комната Моникаммм (кошмар ГГ):

## Фон:

# Эффекты снаружи комнаты:
image monikammm_cg_act_1_day_13_mask_smoke: # дым
    "images/cg/monika/mask.png"
    xtile 3 subpixel True
    block:
        xoffset 0
        linear 180 xoffset -1280
        repeat

image monikammm_cg_act_1_day_13_mask_smoke_flip: # дым (для световых всполыхов)
    "images/cg/monika/mask.png"
    xzoom -1 xtile 3 subpixel True
    parallel:
        xoffset 0
        linear 180 xoffset -1280
        repeat
    parallel:
        function monika_alpha

image monikammm_cg_act_1_day_13_mask_grain: # белая зернистость ("звёзды" на небе)
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image monikammm_cg_act_1_day_13_mask_gas_cloud: # зернистое космическое газовое облако
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

# Комната:
image monika_room = "images/cg/monika/monika_room.png" # пустая комната

image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png" # пустая с более сильным освещением из-за эффектов снаружи ("всполохи" света)
    function monika_alpha

image monika_room_desk:
    "mod_assets/MPT/monikammm/desk/desk.png" # стол
    ypos 734



############################## ДЕНЬ 14 ##############################

### Моника в комнате вблизи смотрит на ГГ и улыбается:

# Фон + взгляд Моники на ГГ, нейтральное выражение лица, рот закрыт, глаза открыты
image monika_cg_act_1_day_14_base:
    "mod_assets/cg/main_history/act_1/day_14/m_base.png"

# Открытый улыбающийся рот
image monika_cg_act_1_day_14_exp1:
    "mod_assets/cg/main_history/act_1/day_14/m_exp1.png"

# Закрытые вниз глаза
image monika_cg_act_1_day_14_exp2:
    "mod_assets/cg/main_history/act_1/day_14/m_exp2.png"

# Указательный палец поставлен ко рту, рот улыбается, закрыт, Моника облизывается
image monika_cg_act_1_day_14_exp3:
    "mod_assets/cg/main_history/act_1/day_14/m_exp3.png"



############################################## CG - TRANSFORMS ##############################################

transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0
