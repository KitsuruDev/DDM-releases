init -100 python in phone.game_snake:
    from renpy import store
    from store import Text, persistent
    from random import randint
    import pygame

    class Game(renpy.Displayable):
        block_size, area_size, render_size = 20, 360, (360, 620)
        area_left, area_top, area_right, area_bottom = 0, 130, 340, 470

        area_left_scale, area_right_scale = int(area_left / block_size), int(area_right / block_size)
        area_top_scale, area_bottom_scale = int(area_top / block_size), int(area_bottom / block_size)

        map_dir = {
            pygame.K_UP:    (0, -block_size), # Вверх
            pygame.K_DOWN:  (0, block_size),  # Вниз
            pygame.K_LEFT:  (-block_size, 0), # Влево
            pygame.K_RIGHT: (block_size, 0)   # Вправо
        }

        def __init__(self, **kwargs):
            super(Game, self).__init__(**kwargs)
            self.last_move_time = 0.0
            self.new_game()

        def new_game(self):
            self.snake_body = [(40, 40)]
            self.snake_dir = (0, Game.block_size)
            self.move_interval = 0.12
            self.stone_pos = self.set_pos_stone()
            self.stone_area = [pygame.Rect((x, y), (Game.block_size, Game.block_size)) for x, y in self.stone_pos]
            self.food_pos = self.set_pos_food()
            self.score = 0
            self.finish = False

        def update_high_score(self):
            global score
            score = self.score
            if score > persistent.phone_game_snake_score_high:
                persistent.phone_game_snake_score_high = score
                renpy.save_persistent()

        def set_pos_stone(self):
            pos_stone_list = []
            for i in range(randint(4, 7)):
                while True:
                    pos_stone = (
                        randint(Game.area_left_scale, Game.area_right_scale) * Game.block_size,
                        randint(Game.area_top_scale, Game.area_bottom_scale) * Game.block_size
                    )
                    if pos_stone not in pos_stone_list and pos_stone not in (40, 40):
                        pos_stone_list.append(pos_stone)
                        break
            return pos_stone_list

        def set_pos_food(self):
            while True:
                pos_food = (
                    randint(Game.area_left_scale, Game.area_right_scale) * Game.block_size,
                    randint(Game.area_top_scale, Game.area_bottom_scale) * Game.block_size
                )
                if pos_food not in self.snake_body and pos_food not in self.stone_pos:
                    return pos_food

        def render(self, width, height, st, at):
            # ЛОГИКА - выполняется только когда прошёл интервал движения
            if st - self.last_move_time >= self.move_interval:
                self.last_move_time = st

                # Проверка столкновения головы с телом (до движения)
                head = self.snake_body[0]
                if len(self.snake_body) > 1 and head in self.snake_body[1:]:
                    self.finish = True
                if head in self.stone_pos:
                    self.finish = True

                if self.finish:
                    self.update_high_score()
                    renpy.end_interaction(True)
                    # дальнейшая отрисовка не важна, но для безопасности вернётся пустой Render
                    return renpy.Render(Game.render_size[0], Game.render_size[1])

                new_head = tuple(map(lambda i, j: i + j, self.snake_body[0], self.snake_dir))
                new_head = (new_head[0] % Game.render_size[0], new_head[1] % Game.render_size[1])
                self.snake_body.insert(0, new_head)

                if new_head == self.food_pos:
                    self.food_pos = self.set_pos_food()
                    self.score += 1
                else:
                    self.snake_body.pop()

            # ОТРИСОВКА
            render = renpy.Render(Game.render_size[0], Game.render_size[1])
            render_canvas = render.canvas()

            # Камни
            for stone in self.stone_area:
                render_canvas.rect((94, 94, 94), stone)

            # Еда
            food_area = pygame.Rect((self.food_pos[0], self.food_pos[1]), (Game.block_size, Game.block_size))
            render_canvas.rect((240, 0, 0), food_area)

            # Змейка: голова и тело
            head = self.snake_body[0]
            render_canvas.rect((240, 240, 0), [head[0], head[1], Game.block_size, Game.block_size])
            for segment in self.snake_body[1:]:
                render_canvas.rect((255, 165, 0), [segment[0], segment[1], Game.block_size, Game.block_size])

            # Запрос следующей перерисовки
            renpy.redraw(self, 0.0)
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    renpy.end_interaction(True)
                if new_dir := Game.map_dir.get(ev.key):
                    if (new_dir[0] * -1, new_dir[1] * -1) != self.snake_dir: # Запрет разворота на 180 градусов
                        self.snake_dir = new_dir

default phone.game_snake.score = 0
default persistent.phone_game_snake_score_high = 0
default phone.game_snake.first_start = True

screen phone_game_snake_background:
    add Solid("#7cde7c")

screen phone_game_snake:
    use _phone():
        use phone_game_snake_background

        style_prefix "phone_game_snake"

        vbox:
            label _("Мини-игра «Змейка»")

            null height 5

            textbutton _("Новая игра") at _phone_application_button:
                action PhoneMenu("phone_game_snake_before_after_round")
            textbutton _("Рекорд") at _phone_application_button:
                action PhoneMenu("phone_game_snake_record")
            textbutton _("Выйти") at _phone_application_button:
                action PhoneReturn()

screen phone_game_snake_record:
    use _phone():
        use phone_game_snake_background

        style_prefix "phone_game_snake"

        vbox:
            label _("Ваш текущий рекорд:")
            text str(persistent.phone_game_snake_score_high) + " очков"

            null height 5

            textbutton _("Вернуться в меню") at _phone_application_button:
                action PhoneReturn()

screen phone_game_snake_round:
    use _phone():
        use phone_game_snake_background
        $ snake = phone.game_snake.Game()
        add snake

screen phone_game_snake_before_after_round():
    use _phone():
        use phone_game_snake_background

        style_prefix "phone_game_snake_before_after_round"

        if phone.game_snake.first_start:
            vbox:
                label _("Правила:")
                text _("1) используйте стрелки для передвижения;")
                text _("2) ешьте яблоки, чтобы набрать очки;")
                text _("3) избегайте камней и попадания в себя;")
                text _("4) продержитесь как можно дольше!")

                null height 5

                textbutton _("Начать игру!") at _phone_application_button:
                    action [PhoneMenu("phone_game_snake_round"), SetVariable("phone.game_snake.first_start", False)]
        else:
            vbox:
                spacing 20

                label _("Игра окончена!")

                null height 10

                label _("Ваши результаты:")
                text _("Cчёт: [phone.game_snake.score] очков")
                text _("Рекорд: [persistent.phone_game_snake_score_high] очков")

                null height 15

                textbutton _("Попробовать снова") at _phone_application_button:
                    action PhoneMenu("phone_game_snake_round")

                null height 5

                textbutton _("Вернуться в меню") at _phone_application_button:
                    action [PhoneReturn(), SetVariable("phone.game_snake.first_start", True)]


style phone_game_snake_vbox:
    align (0.5, 0.5)
    spacing 50

style phone_game_snake_button:
    xalign 0.5

style phone_game_snake_text:
    font phone.config.basedir + "fonts/JetBrainsMono-Regular.ttf"
    color "#f5d120" outlines [(1, "#505050", 0, 0)]
    size 30
    xalign 0.5
    text_align 0.5

style phone_game_snake_label:
    xalign 0.5

style phone_game_snake_label_text is phone_game_snake_text:
    font phone.config.basedir + "fonts/JetBrainsMono-ExtraBold.ttf"

style phone_game_snake_button_text is phone_game_snake_text


style phone_game_snake_before_after_round_vbox is phone_game_snake_vbox:
    spacing 10
style phone_game_snake_before_after_round_button is phone_game_snake_button
style phone_game_snake_before_after_round_button_text is phone_game_snake_text
style phone_game_snake_before_after_round_text is phone_game_snake_text:
    size 26
style phone_game_snake_before_after_round_label is phone_game_snake_label
style phone_game_snake_before_after_round_label_text is phone_game_snake_label_text:
    xalign 0.5
