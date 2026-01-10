## gallery_bg.rpy

init -1 python in GalleryBG:
    from store import config, Transform, Hide
    import os

    dict, keys, current = {}, None, None

    def next(back=False):
        global current, dict, keys
        if not keys:
            keys = [k for k, v in dict.items()]
        index_current = keys.index(current)
        index_next = index_current - 1 if back else index_current + 1
        try:               current = keys[index_next]
        except IndexError: current = keys[0]

    class GalleryBGImage:
        def __init__(self, image, name, artist=None):
            self.file = image
            self.image = Transform(image, size=(config.screen_width, config.screen_height))
            self.small_size = Transform(image, size=(234, 132))
            self.name = name
            self.artist = artist
            dict[self.name] = self


image bg_train_1_image_back:
    "mod_assets/bg/open_places/train_window/field.png"
    zoom 1.49 crop(0, 0, 858, 300)
image bg_train_1_image = Composite((1280, 720), (0, 0), "bg_train_1_image_back", (0, 0), "bg train")
image bg_train_2_image_back:
    "mod_assets/bg/open_places/train_window/niigata.png"
    zoom 1.49 crop(0, 0, 858, 300)
image bg_train_2_image = Composite((1280, 720), (0, 0), "bg_train_2_image_back", (0, 0), "bg train")


init python:
    # не словари, т.к. f-форматирование не поддерживает ссылки через ключи
    # менять f-форматирование на конкатенацию (+) не буду: по времени выполнения они практически одинаковы + конкатенация убого смотрится
    # другие форматирования громоздкие и медленные по времени

    bg_artist_one = _("Художник")
    bg_artist_two = _("Художники")
    bg_artist_edit = _("Редактирование")
    bg_artist_command = _("из команды")
    bg_artist_version = _("Ночная версия")
    bg_artist_old_discord = _("Discord, старый ник")

    bg_description_wikimedia = _("Фотография с сайта {a=https://commons.wikimedia.org/wiki/Main_Page}commons.wikimedia.org{/a}")
    bg_description_free = _("Свободная фотография")
    bg_description_license = _("под лицензией")

    bg_description_license_CC_BY_2 = "{a=https://creativecommons.org/licenses/by/2.0/deed.en}Creative Commons Attribution 2.0 Generic{/a}"
    bg_description_license_CC_BY_3 = "{a=https://creativecommons.org/licenses/by/3.0/deed.en}Creative Commons Attribution 3.0 License{/a}"
    bg_description_license_CC_BY_4 = "{a=https://creativecommons.org/licenses/by/4.0/deed.en}Creative Commons Attribution 4.0 License{/a}"
    bg_description_license_CC_BY_SA_2 = "{a=https://creativecommons.org/licenses/by-sa/2.0/deed.en}Creative Commons Attribution-Share Alike 2.0 International{/a}"
    bg_description_license_CC_BY_SA_3 = "{a=https://creativecommons.org/licenses/by-sa/3.0/deed.en}Creative Commons Attribution-Share Alike 3.0 International{/a}"
    bg_description_license_CC_BY_SA_4 = "{a=https://creativecommons.org/licenses/by-sa/4.0/deed.en}Creative Commons Attribution-Share Alike 4.0 International{/a}"

    bg_name_house_owner_mc = _("Дом Макса")
    bg_name_house_owner_s = _("Дом Сайори")
    bg_name_house_owner_m = _("Дом Моники")
    bg_name_house_owner_n = _("Дом Нацуки")
    bg_name_house_owner_y = _("Дом Юри")

    bg_name_class_owner_mc = _("класс Макса")
    bg_name_class_owner_s = _("класс Сайори")
    bg_name_class_owner_n = _("класс Нацуки")
    bg_name_class_owner_y = _("класс Юри")

    bg_name_inside_door = _("дверь")
    bg_name_inside_hallway = _("прихожая")
    bg_name_inside_livingroom = _("гостиная")
    bg_name_inside_kitchen = _("кухня")
    bg_name_inside_bathroom = _("ванная")
    bg_name_inside_bedroom = _("спальня")
    bg_name_inside_enter = _("вход")
    bg_name_inside_corridor = _("коридор")
    bg_name_inside_stairs_center = _("центр. лестница")
    bg_name_inside_stairs_right = _("правая лестница")
    bg_name_inside_floor = _("этаж")
    bg_name_inside_wall = _("стена")
    bg_name_inside_rooftop = _("крыша")
    bg_name_inside_class = _("класс")
    bg_name_inside_class_music = _("музыкальный класс")
    bg_name_inside_board = _("доска")
    bg_name_inside_space = _("помещение")
    bg_name_inside_storage = _("кладовка")
    bg_name_inside_school_library = _("школьная библиотека")
    bg_name_inside_elevator = _("лифт")
    bg_name_inside_cabin = _("кабина")
    bg_name_inside_arcade = _("аркад. зал")
    bg_name_inside_toilet = _("туалет")
    bg_name_inside_turnstile = _("турникеты")
    bg_name_inside_platform = _("платформа")

    bg_name_outside_field = _("поле")
    bg_name_outside_river = _("река")
    bg_name_outside_city = _("город")
    bg_name_outside_street = _("улица")
    bg_name_outside_street_native = _("родная улица")
    bg_name_outside_park_japanese = _("японский парк")
    bg_name_outside_park_small = _("маленький парк")
    bg_name_outside_enter = _("вход")
    bg_name_outside_enter_south = _("южный вход")
    bg_name_outside_enter_official = _("офиц. вход")
    bg_name_outside_arch = _("арка")
    bg_name_outside_path = _("дорожка")
    bg_name_outside_torii = _("тории")
    bg_name_outside_bridge = _("мостик")
    bg_name_outside_shop_food = _("продуктовый магазин")
    bg_name_outside_shop_clother = _("магазин одежды")
    bg_name_outside_shop_book = _("книжный магазин")
    bg_name_outside_mall_kokoro = _("ТЦ KoKoRo")
    bg_name_outside_cafe_local = _("местное кафе")
    bg_name_outside_hospital = _("госпиталь")
    bg_name_outside_office = _("офис")
    bg_name_outside_station_morioka = _("Cтанция Мориока")
    bg_name_outside_station_niigata = _("Cтанция Ниигата")
    bg_name_outside_station_bus = _("автобусный вокзал")
    bg_name_outside_shelter_bus = _("автобусная остановка")
    bg_name_outside_office_ticket = _("кассы")

    bg_name_school_structure_old = _("Школа (старый корпус)")
    bg_name_school_structure_new = _("Школа (новый корпус)")
    bg_name_school_club = _("Литер. клуб")
    bg_name_school_office = _("офис Рэйко")

    bg_name_city_niigata = _("Ниигата")
    bg_name_city_morioka = _("Мориока")

    bg_name_transport_interior = _("салон")
    bg_name_transport_bus = _("Автобус")
    bg_name_transport_bus_short = _("автоб.")
    bg_name_transport_train = _("Поезд")
    bg_name_transport_train_short = _("поезд")

    bg_name_nightmare = _("кошмар")


    ##### Дом ГГ #####

    bg_mc_house_1 = GalleryBGImage(
        "bg mc house hallway day",
        f"{bg_name_house_owner_mc} -- {bg_name_inside_hallway}",
        bg_artist_one + ": {font=mod_assets/font/menu/GL-NovantiquaMinamoto.ttf}すこあ{/font}"
    )
    bg_mc_house_2 = GalleryBGImage(
        "bg kitchen",
        f"{bg_name_house_owner_mc} -- {bg_name_inside_kitchen}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_mc_house_3 = GalleryBGImage(
        "bg mc house bathroom day",
        f"{bg_name_house_owner_mc} -- {bg_name_inside_bathroom}",
        bg_artist_one + ": {font=mod_assets/font/menu/GL-NovantiquaMinamoto.ttf}すこあ{/font}"
    )
    bg_mc_house_4 = GalleryBGImage(
        "bg bedroom",
        f"{bg_name_house_owner_mc} -- {bg_name_inside_bedroom}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )


    ##### Дом Сайори #####

    bg_s_house_1 = GalleryBGImage(
        "bg house",
        bg_name_house_owner_s,
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\n{bg_artist_version} -- Alex [[ORG]]#9077 ({bg_artist_old_discord})"
    )
    bg_s_house_2 = GalleryBGImage(
        "bg sayori house hallway day",
        f"{bg_name_house_owner_s} -- {bg_name_inside_hallway}",
        f"{bg_artist_two}: QQQnoQnoQ, minikle\n{bg_artist_edit} -- Nuxill (Reddit)"
    )
    bg_s_house_3 = GalleryBGImage(
        "bg sayori house livingroom day",
        f"{bg_name_house_owner_s} -- {bg_name_inside_livingroom}",
        f"{bg_artist_one}: Nuxill (Reddit)\n{bg_artist_edit} -- Yagamirai10 (Reddit)"
    )
    bg_s_house_4 = GalleryBGImage(
        "bg sayori house bedroom day",
        f"{bg_name_house_owner_s} -- {bg_name_inside_bedroom}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\n{bg_artist_version} -- Mattyd (Reddit) (MacDaddyMatty.com)"
    )


    ##### Дом Моники #####

    bg_m_house_1 = GalleryBGImage(
        "bg monika house outside day",
        bg_name_house_owner_m,
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_m_house_2 = GalleryBGImage(
        "bg monika house hallway day",
        f"{bg_name_house_owner_m} -- {bg_name_inside_hallway}",
        f"{bg_artist_one}: Yui Anno\n{bg_artist_edit} -- Reitanna Seishin (Reddit)"
    )
    bg_m_house_3 = GalleryBGImage(
        "bg monika house livingroom day",
        f"{bg_name_house_owner_m} -- {bg_name_inside_livingroom}",
        f"{bg_artist_one}: Noraneko Games"
    )
    bg_m_house_4 = GalleryBGImage(
        "bg monika house kitchen day",
        f"{bg_name_house_owner_m} -- {bg_name_inside_kitchen}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_m_house_5 = GalleryBGImage(
        "bg monika house bedroom morning",
        f"{bg_name_house_owner_m} -- {bg_name_inside_bedroom}",
        f"{bg_artist_one}: Uncle Muggen"
    )


    ##### Дом Нацуки #####

    bg_n_house_1 = GalleryBGImage(
        "bg natsuki house outside day",
        bg_name_house_owner_n,
        f"{bg_artist_two}: kjkjmulo, Team Relations"
    )
    bg_n_house_2 = GalleryBGImage(
        "bg natsuki house kitchen day",
        f"{bg_name_house_owner_n} -- {bg_name_inside_kitchen}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_n_house_3 = GalleryBGImage(
        "bg natsuki house bedroom day",
        f"{bg_name_house_owner_n} -- {bg_name_inside_bedroom}",
        f"{bg_artist_one}: Kimagure After"
    )


    ##### Дом Юри #####

    bg_y_house_1 = GalleryBGImage(
        "bg yuri house outside day",
        bg_name_house_owner_y,
        f"{bg_artist_one}: Kimagure After\n{bg_artist_edit} -- Wretched Team (Doki Doki Exit Music)"
    )
    bg_y_house_2 = GalleryBGImage(
        "bg yuri house hallway day",
        f"{bg_name_house_owner_y} -- {bg_name_inside_hallway}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_y_house_3 = GalleryBGImage(
        "bg yuri house kitchen day",
        f"{bg_name_house_owner_y} -- {bg_name_inside_kitchen}",
        f"{bg_artist_one}: {{a=https://spiralatlas.github.io/}}Sean Atlas{{/a}} {bg_description_license} {bg_description_license_CC_BY_4}"
    )
    bg_y_house_4 = GalleryBGImage(
        "bg yuri house livingroom day",
        f"{bg_name_house_owner_y} -- {bg_name_inside_livingroom}",
        f"{bg_artist_one}: {{a=https://spiralatlas.github.io/}}Sean Atlas{{/a}} {bg_description_license} {bg_description_license_CC_BY_4}"
    )
    bg_y_house_5 = GalleryBGImage(
    "bg yuri house bathroom day",
    f"{bg_name_house_owner_y} -- {bg_name_inside_bathroom}",
    f"{bg_artist_one}: {{a=https://spiralatlas.github.io/}}Sean Atlas{{/a}} {bg_description_license} {bg_description_license_CC_BY_4}"
    )
    bg_y_house_6 = GalleryBGImage(
        "bg yuri house bedroom day",
        f"{bg_name_house_owner_y} -- {bg_name_inside_bedroom}",
        f"{bg_artist_two}: QQQnoQnoQ, minikle\n{bg_artist_edit} -- Nuxill (Reddit)"
    )


    ##### Тетради #####

    bg_notebook = GalleryBGImage(
        "bg notebook_full_mc",
        _("Тетрадь"),
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )


    ##### Школа - вход #####

    bg_school_outside_1 = GalleryBGImage(
        "bg school gate 1",
        f"{bg_name_school_structure_new} -- {bg_name_inside_enter}",
        f"{bg_artist_one}: Uncle Muggen"
    )


    ##### Школа - крыша #####

    bg_school_rooftop_1 = GalleryBGImage(
        "bg school new_rooftop 1 day",
        f"{bg_name_school_structure_new}  -- {bg_name_inside_rooftop} 1",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_rooftop_2 = GalleryBGImage(
        "bg school new_rooftop 2 day",
        f"{bg_name_school_structure_new}  -- {bg_name_inside_rooftop} 2",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_rooftop_3 = GalleryBGImage(
        "bg school old_rooftop day",
        f"{bg_name_school_structure_old}  -- {bg_name_inside_rooftop}",
        f"{bg_artist_one}: Kimagure After"
    )


    ##### Школа - внутри #####

    bg_school_inside_1 = GalleryBGImage(
        "bg school f2 new_corridor",
        f"{bg_name_school_structure_new} -- {bg_name_inside_corridor}, 2 {bg_name_inside_floor}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_2 = GalleryBGImage(
        "bg school f3 new_corridor",
        f"{bg_name_school_structure_new} -- {bg_name_inside_corridor}, 3 {bg_name_inside_floor}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_3 = GalleryBGImage(
        "bg corridor",
        f"{bg_name_school_structure_old} -- {bg_name_inside_corridor}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_4 = GalleryBGImage(
        "bg school f3 old_corridor",
        f"{bg_name_school_structure_old} -- {bg_name_inside_corridor}, 3 {bg_name_inside_floor}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\nТорговый автомат взят со свободной фотографии"
    )
    bg_school_inside_5 = GalleryBGImage(
        "bg school old_corridor wall",
        f"{bg_name_school_structure_old} -- {bg_name_inside_corridor}, {bg_name_inside_wall}",
        f"{bg_artist_one}: Cyrke (Reddit)"
    )
    bg_school_inside_6 = GalleryBGImage(
        "bg school old_corridor door",
        f"{bg_name_school_structure_old} -- {bg_name_inside_corridor}, {bg_name_inside_door}",
        f"{bg_artist_one}: null1fy {bg_artist_command} Wretched Team (Doki Doki Exit Music)"
    )
    bg_school_inside_7 = GalleryBGImage(
        "bg school f1 old_stairwell right",
        f"{bg_name_school_structure_old} -- {bg_name_inside_stairs_right}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_8 = GalleryBGImage(
        "bg school f1 old_stairwell center",
        f"{bg_name_school_structure_old} -- {bg_name_inside_stairs_center}, 1 {bg_name_inside_floor}",
        f"{bg_artist_one}: Nuxill (Reddit)"
    )
    bg_school_inside_9 = GalleryBGImage(
        "bg school f2 old_stairwell center",
        f"{bg_name_school_structure_old} -- {bg_name_inside_stairs_center}, 2 {bg_name_inside_floor}",
        f"{bg_artist_one}: Nuxill (Reddit)\n{bg_artist_edit} -- MrRocketman999 (Reddit)"
    )
    bg_school_inside_10 = GalleryBGImage(
        "bg school new_class_mc day",
        f"{bg_name_school_structure_new} -- {bg_name_class_owner_mc}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_11 = GalleryBGImage(
        "bg school new_class_sayori day",
        f"{bg_name_school_structure_new} -- {bg_name_class_owner_s}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_12 = GalleryBGImage(
        "bg school new_class_natsuki day",
        f"{bg_name_school_structure_new} -- {bg_name_class_owner_n}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_13 = GalleryBGImage(
        "bg school new_class_yuri day",
        f"{bg_name_school_structure_new} -- {bg_name_class_owner_y}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_14 = GalleryBGImage(
        "bg class_day",
        f"{bg_name_school_structure_old} -- {bg_name_inside_class}, {bg_name_inside_board}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_15 = GalleryBGImage(
        "bg school old_class",
        f"{bg_name_school_structure_old} -- {bg_name_inside_class}, {bg_name_inside_space}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\n{bg_artist_edit} -- BestoGril"
    )
    bg_school_inside_16 = GalleryBGImage(
        "bg school literature_club board day",
        f"{bg_name_school_structure_old} -- {bg_name_school_club}, {bg_name_inside_board}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\n{bg_artist_edit} -- KingBoosted#5085 ({bg_artist_old_discord})"
    )
    bg_school_inside_17 = GalleryBGImage(
        "bg club_day",
        f"{bg_name_school_structure_old} -- {bg_name_school_club}, {bg_name_inside_space}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_18 = GalleryBGImage(
        "bg closet",
        f"{bg_name_school_structure_old} -- {bg_name_school_club}, {bg_name_inside_storage}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_19 = GalleryBGImage(
        "bg school old_class_music",
        f"{bg_name_school_structure_old} -- {bg_name_inside_class_music}",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato"
    )
    bg_school_inside_20 = GalleryBGImage(
        "bg school office_reiko",
        f"{bg_name_school_structure_new} -- {bg_name_school_office}",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_school_inside_21 = GalleryBGImage(
        "bg school library",
        f"{bg_name_school_structure_new} -- {bg_name_inside_school_library}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )


    ##### Улицы #####

    bg_street_01 = GalleryBGImage(
        "bg residential_day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street_native} 1",
        f"{bg_artist_one}: Velinquent {bg_artist_command} Team Salvato\n{bg_artist_edit} -- Wretched Team (Doki Doki Exit Music)"
    )
    bg_street_02 = GalleryBGImage(
        "bg residential_day nearby",
        f"{bg_name_city_niigata} -- {bg_name_outside_street_native} 2",
        f"{bg_artist_one}: Noraneko Games"
    )
    bg_street_1 = GalleryBGImage(
        "bg niigata street suburban 1 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 1",
        f"{bg_artist_one}: Kimagure After\n{bg_artist_edit} -- Wretched Team (Doki Doki Exit Music)"
    )
    bg_street_2 = GalleryBGImage(
        "bg niigata street suburban 2 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 2",
        f"{bg_artist_one}: Kimagure After\n{bg_artist_edit} -- Wretched Team (Doki Doki Exit Music)"
    )
    bg_street_3 = GalleryBGImage(
        "bg niigata street suburban 3 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 3",
        bg_description_wikimedia
    )
    bg_street_4 = GalleryBGImage(
        "bg niigata street suburban 4 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 4",
        bg_description_wikimedia
    )
    bg_street_5 = GalleryBGImage(
        "bg niigata street suburban 5 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 5",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Street_in_Kaneyama_Town,_Yamagata.jpg}}{{font=mod_assets/font/menu/GL-NovantiquaMinamoto.ttf}}掬茶{{/font}}{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_4}"
    )
    bg_street_6 = GalleryBGImage(
        "bg niigata street suburban 6 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 6",
        bg_description_wikimedia
    )
    bg_street_7 = GalleryBGImage(
        "bg niigata street suburban 7 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 7",
        f"{bg_description_wikimedia} (полная версия) -- {{a=https://commons.wikimedia.org/wiki/File:Chiba_Prefectural_Road_Route_228_(Ichinomiya_Station_Line)_in_Ichinomiya,_Ichinomiya_Town_04.jpg}}{{font=mod_assets/font/menu/GL-NovantiquaMinamoto.ttf}}小石川人晃{{/font}}{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_4}"
    )
    bg_street_8 = GalleryBGImage(
        "bg niigata street suburban 8 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 8",
        bg_description_wikimedia
    )
    bg_street_9 = GalleryBGImage(
        "bg niigata street suburban 9 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 9",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Tochigi_prefectural_road_301_at_1chome-1_Shiho_Mibu_town_20210803_094332.jpg}}LERK{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_4}"
    )
    bg_street_10 = GalleryBGImage(
        "bg niigata street suburban 10 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 10",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_street_11 = GalleryBGImage(
        "bg niigata street suburban 11 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 11",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_street_12 = GalleryBGImage(
        "bg niigata street suburban 12 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 12",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_street_13 = GalleryBGImage(
        "bg niigata street suburban 13 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 13",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_street_14 = GalleryBGImage(
        "bg niigata street suburban 14 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 14",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_street_15 = GalleryBGImage(
        "bg niigata street suburban 15 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 15",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_street_16 = GalleryBGImage(
        "bg niigata street suburban 16 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 16",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_street_17 = GalleryBGImage(
        "bg niigata street urban 1 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 17",
        f"{bg_artist_one}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_street_18 = GalleryBGImage(
        "bg niigata street urban 2 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 18",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_street_19 = GalleryBGImage(
        "bg niigata street urban 3 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 19",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_street_20 = GalleryBGImage(
        "bg niigata street urban 4 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 20",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_street_21 = GalleryBGImage(
        "bg niigata street urban 5 day",
        f"{bg_name_city_niigata} -- {bg_name_outside_street} 21",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )


    ##### Парки #####

    bg_park_japan_1 = GalleryBGImage(
        "bg niigata park japanese off entrance",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_enter_official}",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Entrance_of_the_Seitaikei_Park.jpg}}{{font=mod_assets/font/menu/GL-NovantiquaMinamoto.ttf}}掬茶{{/font}}{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_4}"
    )
    bg_park_japan_21 = GalleryBGImage(
        "bg niigata park japanese off entrance arc 1",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_enter_official}, {bg_name_outside_arch} 1",
        bg_description_wikimedia
    )
    bg_park_japan_22 = GalleryBGImage(
        "bg niigata park japanese off entrance arc 2",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_enter_official}, {bg_name_outside_arch} 2",
        bg_description_wikimedia
    )
    bg_park_japan_3 = GalleryBGImage(
        "bg niigata park japanese off entrance arc wall",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_enter_official}, {bg_name_inside_wall}",
        bg_description_wikimedia
    )
    bg_park_japan_4 = GalleryBGImage(
        "bg niigata park japanese entrance stairs",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_enter}",
        bg_description_wikimedia
    )
    bg_park_japan_5 = GalleryBGImage(
        "bg niigata park japanese path 1",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_path} 1",
        bg_description_wikimedia
    )
    bg_park_japan_6 = GalleryBGImage(
        "bg niigata park japanese path 2",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_path} 2",
        bg_description_wikimedia
    )
    bg_park_japan_7 = GalleryBGImage(
        "bg niigata park japanese path 3",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_path} 3",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Japanese_Garden_-_Seattle_-_path_01.jpg}}Jmabel{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_3}"
    )
    bg_park_japan_8 = GalleryBGImage(
        "bg niigata park japanese path 4",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_path} 4",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Japanese_Garden_-_Seattle_-_path_02.jpg}}Jmabel{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_3}"
    )
    bg_park_japan_9 = GalleryBGImage(
        "bg niigata park japanese torii",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_torii}",
        bg_description_wikimedia
    )
    bg_park_japan_10 = GalleryBGImage(
        "bg niigata park japanese bridge 1",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_bridge} 1",
        bg_description_wikimedia
    )
    bg_park_japan_11 = GalleryBGImage(
        "bg niigata park japanese bridge 2",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_japanese}, {bg_name_outside_bridge} 2",
        bg_description_wikimedia
    )
    bg_park_small_1 = GalleryBGImage(
        "bg niigata park small entrance 1",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_small}, {bg_name_outside_enter} 1",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_park_small_2 = GalleryBGImage(
        "bg niigata park small entrance 2",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_small}, {bg_name_outside_enter} 2",
        f"{bg_artist_one}: Uncle Muggen"
    )
    bg_park_small_3 = GalleryBGImage(
        "bg niigata park small path",
        f"{bg_name_city_niigata} -- {bg_name_outside_park_small}, {bg_name_outside_path}",
        f"{bg_artist_one}: Uncle Muggen"
    )


    ##### Магазины #####

    bg_shop_food_1 = GalleryBGImage(
        "bg niigata shop food 1",
        f"{bg_name_city_niigata} -- {bg_name_outside_shop_food} 1",
        bg_description_wikimedia
    )
    bg_shop_food_2 = GalleryBGImage(
        "bg niigata shop food 2",
        f"{bg_name_city_niigata} -- {bg_name_outside_shop_food} 2",
        bg_description_wikimedia
    )
    bg_shop_food_3 = GalleryBGImage(
        "bg niigata shop food 3",
        f"{bg_name_city_niigata} -- {bg_name_outside_shop_food} 3",
        bg_description_wikimedia
    )
    bg_shop_food_4 = GalleryBGImage(
        "bg niigata shop food 4",
        f"{bg_name_city_niigata} -- {bg_name_outside_shop_food} 4",
        bg_description_wikimedia
    )
    bg_shop_food_5 = GalleryBGImage(
        "bg niigata shop food 5",
        f"{bg_name_city_niigata} -- {bg_name_outside_shop_food} 5",
        bg_description_wikimedia
    )
    bg_mall_1 = GalleryBGImage(
        "bg niigata kokoro entrance",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_outside_enter}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_mall_2 = GalleryBGImage(
        "bg niigata kokoro f1 corridor",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, 1 {bg_name_inside_floor}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_mall_3 = GalleryBGImage(
        "bg niigata kokoro f1 elevator",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, 1 {bg_name_inside_floor}, {bg_name_inside_elevator}",
        bg_description_wikimedia
    )
    bg_mall_4 = GalleryBGImage(
        "bg niigata kokoro elevator inside",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_inside_elevator}, {bg_name_inside_cabin}",
        bg_description_free
    )
    bg_mall_5 = GalleryBGImage(
        "bg niigata kokoro shop food",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_outside_shop_food}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_mall_6 = GalleryBGImage(
        "bg niigata kokoro shop clother",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_outside_shop_clother}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_mall_7 = GalleryBGImage(
        "bg niigata kokoro shop book",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_outside_shop_book}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_mall_8 = GalleryBGImage(
        "bg niigata kokoro arcade",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_inside_arcade}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )
    bg_mall_11 = GalleryBGImage(
        "bg niigata kokoro toilet",
        f"{bg_name_city_niigata} -- {bg_name_outside_mall_kokoro}, {bg_name_inside_toilet}",
        f"{bg_artist_one}: Uncle Muggen"
    )


    ##### Кафе и рестораны #####

    bg_local_cafe = GalleryBGImage(
        "bg niigata cafe local inside",
        f"{bg_name_city_niigata} -- {bg_name_outside_cafe_local}",
        f"{bg_artist_two}: Wretched Team (Doki Doki Exit Music)"
    )


    ##### Офисы #####

    bg_local_cafe = GalleryBGImage(
        "bg morioka office inside",
        f"{bg_name_city_morioka} -- {bg_name_outside_office}, {bg_name_inside_space}",
        f"{bg_artist_two}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )


    ##### Госпитали #####

    bg_niigata_hospital_outside_day = GalleryBGImage(
        "bg niigata hospital outside day",
        f"{bg_name_city_niigata} -- {bg_name_outside_hospital}({bg_name_outside_enter})",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_niigata_hospital_inside_day = GalleryBGImage(
        "bg niigata hospital inside day",
        f"{bg_name_city_niigata} -- {bg_name_outside_hospital}({bg_name_inside_space})",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )


    ##### Станции и транспорт #####

    bg_station_prologue = GalleryBGImage(
        "bg morioka station morioka platform",
        bg_name_outside_station_morioka,
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_station_niigata_1 = GalleryBGImage(
        "bg niigata station niigata entrance outside day",
        f"{bg_name_outside_station_niigata} -- {bg_name_outside_enter_south}",
        f"{bg_artist_one}: Kimagure After"
    )
    bg_station_niigata_2 = GalleryBGImage(
        "bg niigata station niigata entrance inside",
        f"{bg_name_outside_station_niigata} -- {bg_name_inside_turnstile}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )
    bg_station_niigata_3 = GalleryBGImage(
        "bg niigata station niigata platform 1",
        f"{bg_name_outside_station_niigata} -- {bg_name_inside_platform} 1",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Niigata_20220625055856_(52273746607).jpg}}inunami{{/a}} {bg_description_license} {bg_description_license_CC_BY_2}\n{bg_artist_edit} -- KitsuruDev"
    )
    bg_station_niigata_4 = GalleryBGImage(
        "bg niigata station niigata platform 2",
        f"{bg_name_outside_station_niigata} -- {bg_name_inside_platform} 2",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Niigata_20220625055720_(52274983169).jpg}}inunami{{/a}} {bg_description_license} {bg_description_license_CC_BY_2}"
    )
    bg_station_niigata_5 = GalleryBGImage(
        "bg niigata station niigata bus information",
        f"{bg_name_outside_station_niigata} -- {bg_name_outside_station_bus}, {bg_name_outside_office_ticket}",
        bg_description_wikimedia
    )
    bg_station_niigata_6 = GalleryBGImage(
        "bg niigata station niigata bus waiting",
        f"{bg_name_outside_station_niigata} -- {bg_name_outside_station_bus}, {bg_name_transport_bus_short}",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Seibu_Bus_A1-574_at_Kiyose_Station_North_Exit.jpg}}Suikotei{{/a}} {bg_description_license} {bg_description_license_CC_BY_SA_4}"
    )

    bg_train_1 = GalleryBGImage(
        "bg_train_1_image",
        f"{bg_name_transport_train} -- {bg_name_transport_interior}, {bg_name_outside_field}",
        f"{bg_artist_one} ({bg_name_transport_train_short}): Noraneko Games\n{bg_description_wikimedia} ({bg_name_outside_field}) -- {{a=https://commons.wikimedia.org/wiki/File:%E5%8E%9F%E5%9F%8E%E8%B7%A1_-_panoramio.jpg}}shikabane taro{{/a}} {bg_description_license} {bg_description_license_CC_BY_3}"
    )
    bg_train_2 = GalleryBGImage(
        "bg_train_2_image",
        f"{bg_name_transport_train} -- {bg_name_transport_interior}, {bg_name_city_niigata}",
        f"{bg_artist_one} ({bg_name_transport_train_short}): Noraneko Games\n{bg_description_wikimedia} ({bg_name_outside_city}) -- {{a=https://commons.wikimedia.org/wiki/File:%E6%B7%B1%E8%B0%B7%E5%B8%82%E7%9C%BA%E6%9C%9B_Fukaya_city_view_from_high_rise_building_-_panoramio.jpg}}404moon{{/a}} {bg_description_license} {bg_description_license_CC_BY_3}"
    )

    bg_bus_station = GalleryBGImage(
        "bg niigata shelter bus",
        f"{bg_name_city_niigata} -- {bg_name_outside_shelter_bus}",
        bg_description_wikimedia
    )

    bg_bus = GalleryBGImage(
        "bg bus",
        f"{bg_name_transport_bus} -- {bg_name_transport_interior}",
        f"{bg_description_wikimedia} -- {{a=https://commons.wikimedia.org/wiki/File:Kanto_Bus_Tochigi_Inside.jpg}}Akinori Takemoto{{/a}} {bg_description_license} {bg_description_license_CC_BY_3}"
    )


    ##### Всё, что связано с кошмарами #####

    bg_nightmare_river = GalleryBGImage(
        "bg nightmare river",
        f"{bg_name_nightmare} -- {bg_name_outside_river}",
        f"{bg_artist_one}: {{a=https://min-chi.material.jp}}Min-chi{{/a}}"
    )



## Gallery Background Screen #############################################################

screen gallery_bg():
    tag menu

    style_prefix "gallery_bg"

    use game_menu(_("Галерея")):

        fixed:

            vpgrid id "gbgvp":
                rows math.ceil(len(GalleryBG.dict) / 3.0)
                cols 3

                mousewheel True
                arrowkeys True
                allow_underfull True

                spacing 35
                xalign 0.5 yalign 0.5

                for name, gl in GalleryBG.dict.items():
                    vbox:
                        imagebutton:
                            idle gl.small_size
                            action [SetVariable("GalleryBG.current", name), ShowMenu("preview_bg"), With(Dissolve(0.5))]

                        null height 10

                        text "[name]"

            vbar value YScrollValue("gbgvp") xalign 1.012 ypos -0.08 ysize 570


        textbutton "?":
            style "return_button"
            text_size 35
            pos (0.985, 1.1)
            action ShowMenu(
                "extra_screen_help",
                _("Помощь\nДля просмотра фона во весь экран нажмите на его миниатюру.\nЧтобы переключать фоны при просмотре, нажмите на боковые стрелки.\nЧтобы выйти из режима просмотра, нажмите \"X\".\nЭкспорт фонов недоступен в виду сложности его реализации."),
                ok_action = Hide("extra_screen_help"),
                chibi = "y_chibi turned magnifier",
                chibi_pos = 50
            )


style gallery_bg_text is gui_text:
    font "mod_assets/font/menu/AA_Futured.ttf"
    color "#000"
    outlines []
    size 18
    text_align 0.5
    xalign 0.5



## Gallery Background Screen #################################################################

screen preview_bg():
    tag menu

    hbox:
        add GalleryBG.dict[GalleryBG.current].image

    hbox:
        xalign 0.999 ypos 0.01
        spacing 7

        textbutton "i":
            text_style "preview_bg_textbutton_text"
            text_size 30
            activate_sound gui.activate_sound
            action Show("dialog", message=GalleryBG.dict[GalleryBG.current].artist, ok_action=Hide("dialog"))

        textbutton "X":
            text_style "preview_bg_textbutton_text"
            text_size 30
            activate_sound gui.activate_sound
            action ShowMenu("gallery_bg")

    hbox:
        ypos 0.01

        null width 5

        text GalleryBG.dict[GalleryBG.current].name:
            font "mod_assets/font/menu/UZSans-SemiBold.ttf"
            color "#fff"
            outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]

    textbutton "<":
        text_style "preview_bg_textbutton_text"
        align (0.0, 0.5)
        action Function(GalleryBG.next, True)

    textbutton ">":
        text_style "preview_bg_textbutton_text"
        align (1.0, 0.5)
        action Function(GalleryBG.next)

    on "replaced" action With(Dissolve(0.5))


style preview_bg_textbutton_text is navigation_button_text
style preview_bg_textbutton_text:
    font "mod_assets/font/menu/UZSans-SemiBold.ttf"
    size 40
