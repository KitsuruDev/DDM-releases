
########## !!! УЧИТЫВАТЬ ПРИ ИСПОЛЬЗОВАНИИ МОБИЛЬНИКА !!! ##########

## 1) от чьего лица (разговоры, настройки и т.д.) - pov_key_mobile

## 2) соединение с Wi-Fi и прочее (Bluetooth, мобильный Интернет, режим полёта):
## call phone_status_bar_button('callular_data', disable = False)

## 3) время в шторке телефона - phone.system.clock = (часы, минуты)
##    время в чате (указывается, если в чате не было сообщений в этот день) - time year 2023 day 2 month 4 hour 16 minute 30

## 4) уровень заряда батареи - phone.system.battery_level

## 5) день недели по календарю, если вызывается общий экран с приложениями - phone.calendar.current_day = (день месяца, "день недели")

## 6) заметки в календаре: phone.calendar.april_2018_mc[день месяца].description = "ТЕКСТ."

## 7) если появляется новый "контакт" у персонажа:
## contact_list["mc"].extend(["mc_mcm_chat", "mc_s_chat"]) или .append("mc_mcm_chat")

########################################


# От чьего лица мобильник:
default pov_key_mobile = "mc"


############### ИНИЦИАЛИЗИРОВАННЫЕ ПЕРСОНАЖИ В ЧАТАХ ###############

### !!!default!!!
### pc - phone character

## Чат

default pc_mc = phone.character.Character(_("Макс"), phone.config.basedir + "icons/mc.png", "mc", 25, "#484848")
default pc_monika = phone.character.Character(_("Моника"), phone.config.basedir + "icons/m.png", "m", 22, "#0a0")
default pc_sayori = phone.character.Character(_("Сайори"), phone.config.basedir + "icons/s.png", "s", 40, "#22Abf8")
default pc_natsuki = phone.character.Character(_("Нацуки"), phone.config.basedir + "icons/n.png", "n", 30, "#fbb")
default pc_yuri = phone.character.Character(_("Юри"), phone.config.basedir + "icons/y.png", "y", 20, "#a327d6")
default pc_kotonoha = phone.character.Character(_("Котоноха"), phone.config.basedir + "icons/k.png", "k", 19, "#c248c2")
default pc_kamuko = phone.character.Character(_("Камуко"), phone.config.basedir + "icons/kam.png", "kam", 50, "#856655")
default pc_voires = phone.character.Character("Voires", phone.config.basedir + "icons/v.png", "v", 25, "#b5b5b5")

default pc_mc_mom = phone.character.Character(_("Мама"), phone.config.basedir + "icons/default_icon.png", "mc_mom", 15, "#616161")

default pc_monikammm = phone.character.Character(_("Неизвестный"), phone.config.basedir + "icons/default_icon.png", "mmm", 25, "#000")

## Звонки

define phone_mc = Character(_("Макс"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#aaa9ad")
define phone_m = Character(_("Моника"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#4ED42D")
define phone_s = Character(_("Сайори"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#34B1FF")
define phone_n = Character(_("Нацуки"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#ff367c")
define phone_y = Character(_("Юри"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#B957FF")

define phone_mcm = Character(_("Мама"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#787878")

define phone_wor = Character(_("Офисный работник"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#cfcccc")

define phone_mmm = Character(_("Моникаммм"), screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue", color="#000")


############### ИНИЦИАЛИЗИРОВАННЫЕ ЗВУКИ УВЕДОМЛЕНИЙ И РИНГТОНОВ ###############

define audio.new_message_vibration = "phone/assets/sounds/new_message_vibration.mp3"
define audio.new_message_mc = "phone/assets/sounds/new_message_mc.mp3"
define audio.new_message_monika = "phone/assets/sounds/new_message_monika.mp3"
define audio.new_message_sayori = "phone/assets/sounds/new_message_sayori.mp3"
define audio.new_message_natsuki = "phone/assets/sounds/new_message_natsuki.mp3"
define audio.new_message_yuri = "phone/assets/sounds/new_message_yuri.mp3"

define audio.ringtone_vibration = "<loop 0>phone/assets/sounds/ringtone_vibration.mp3"
define audio.ringtone_mc = "<loop 0>phone/assets/sounds/ringtone_mc.mp3"
define audio.ringtone_yuri_1 = "<loop 0 to 11.962>phone/assets/sounds/ringtone_yuri.mp3" # до принятия звонка
define audio.ringtone_yuri_2 = "<from 11.962>phone/assets/sounds/ringtone_yuri.mp3" # после принятия звонка


############### ИНИЦИАЛИЗИРОВАННЫЕ ПРИЛОЖЕНИЯ ###############

## Приложения
init 100 python in phone.application:
    add_app_to_all_characters(app_message)
    add_app_to_all_characters(app_call_history)
    add_app_to_all_characters(app_calendar)
    add_application(app_game_snake, 0, "mc")

init 100 python in phone.calendar:
    april_2018_mc = Calendar(MONDAY, 4, 2018)
    add_calendar(april_2018_mc, "mc")

default phone.calendar.current_day = (2, _("ПН"))


############### ЧАТЫ, ОТОБРАЖАЮЩИЕСЯ В ПРИЛОЖЕНИИ ПЕРСОНАЖЕЙ ###############

default contact_list = { "mc": [] }


############### ИНИЦИАЛИЗИРОВАННЫЕ ЧАТЫ ###############

## Пробелы у имён для того, чтобы названия чатов не пересекались

######## Телефон ГГ ########

init phone register:
    define "Мама":
        icon phone.config.basedir + "icons/default_icon.png"
        add "mc" add "mc_mom"
        key "mc_mcm_chat"

init phone register:
    define "Моника":
        icon phone.config.basedir + "icons/m.png"
        add "mc" add "m"
        key "mc_m_chat"

init phone register:
    define "Сайори":
        icon phone.config.basedir + "icons/s.png"
        add "mc" add "s"
        key "mc_s_chat"

init phone register:
    define "Нацуки":
        icon phone.config.basedir + "icons/n.png"
        add "mc" add "n"
        key "mc_n_chat"

init phone register:
    define "Юри":
        icon phone.config.basedir + "icons/y.png"
        add "mc" add "y"
        key "mc_y_chat"

init phone register:
    define "Voires":
        icon phone.config.basedir + "icons/v.png"
        add "mc" add "v"
        key "mc_v_chat"

init phone register:
    define "ДДЛК":
        icon phone.config.basedir + "icons/default_group.png"
        add "mc" add "m" add "s" add "n" add "y" add "k"
        key "ddlc_chat"


######## Телефон Моники ########

init phone register:
    define "Юри Химэ":
        icon phone.config.basedir + "icons/y.png"
        add "m" add "y"
        key "m_y_chat"


######## Телефон Сайори ########

init phone register:
    define "Мони":
        icon phone.config.basedir + "icons/m.png"
        add "s" add "m"
        key "s_m_chat"


######## Телефон Нацуки ########

init phone register:
    define "Ракета":
        icon phone.config.basedir + "icons/s.png"
        add "n" add "s"
        key "n_s_chat"

init phone register:
    define "Подруга":
        icon phone.config.basedir + "icons/y.png"
        add "n" add "y"
        key "n_y_chat"


######## Телефон Юри ########

init phone register:
    define "Президент":
        icon phone.config.basedir + "icons/m.png"
        add "y" add "m"
        key "y_m_chat"

init phone register:
    define "Кото":
        icon phone.config.basedir + "icons/k.png"
        add "y" add "k"
        key "y_k_chat"

init phone register:
    define "Камуко-тян":
        icon phone.config.basedir + "icons/kam.png"
        add "y" add "kam"
        key "y_kam_chat"



############### ПРИМЕРЫ ЧАТОВ И ЗВОНКОВ ###############

### Регистрации группового чата (ключ обязателен, можно назвать так же, как и сам чат)
# init phone register:
#     define "Welcome":
#         add "s" add "mc" add "y" add "m" add "n"
#         icon phone.config.basedir + "icons/default_group.png"
#         as thanks_for_using_my_framework key "ddu"

### Пример группового чата (общий/личный)
# phone discussion "ddu":
#     time year 2023 day 5 month 6 hour 16 minute 30 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
#     label "'Sayori' has been added to the group"
#     label "'MC' has been added to the group"
#     label "'Yuri' has been added to the group"
#     label "'Monika' has been added to the group"
#     label "'Natsuki' has been added to the group"
#     "m" "Hey there!"
#     "n" "Thank you for using my framework."
#     "n" "I mean {i}of course{/i} you're using {b}this{/b} framework."
#     "n" "...not like there are any better ones out there~"
#     "s" "natsuki!!!!!"
#     "s" "no being a meanie!!!!!!!"
#     "y" "If you are interested in DDLC mods, be sure to check out our mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}!"
#     "mc" "In case you encounter an issue (or wanna make a suggestion),"
#     "mc" "please DM me at Elckarow#8399 or open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a}."
# phone end discussion transition

### Пример звонка
# phone call "s" transition
# phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
# phone_mc "Hey!"
# "Why is she always this energetic?"
# phone end call "01/01/2018" transition
# "..."

############### КОМПЛЕКСНЫЙ ПРИМЕР ЧАТА ###############

### Создание чата:
# init phone register:
#     define "Болтовня":
#         add "mc" add "s" add "n"
#         icon phone.config.basedir + "icons/n.png"
#         key "Болтовня"
#

### Если нужны уже готовые в нём сообщения (+ здесь указано время чата - можно и в др. местах)
# phone register "Болтовня":
#     time year 2023 day 5 month 6 hour 16 minute 30
#     "n" "Этот тест написан раньше, чем ты открыл чат!"

### Сам чат при непосредственном общении
# phone discussion "Болтовня":
#     "n" "Раз, два, три"
#     "n" "Получается писать, ура! А то надоело уже ошибки получать"
#     "s" "Вививививививививививививививи"
#     "mc" "ТИХО"
#     "mc" "Спокойно"
#     "s" "123 456 789"
#     "n" "Бла-бла-бла! Раз-два-три!"

### Его можно прерывать обычными диалоговыми фразами
# "Делать нечего?"

### Продолжение общения и его завершение
# phone discussion "Болтовня":
#     "n" "Ага"
# phone end discussion transition
