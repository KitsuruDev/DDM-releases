## effects.rpy

init python:
    # This function hides all the windows in-game.
    def hide_windows_enabled(enabled=True):
        global _windows_hidden
        _windows_hidden = not enabled

    # monika room highlight alpha
    def monika_alpha(trans, st, at):
        trans.alpha = math.pow(math.sin(st / 8), 64) * 1.4
        return 0


init -1 python in Effects:
    from store import SpriteManager, Null
    import random
    import math

    def screenshot_srf():
        if renpy.version_tuple > (7, 3, 5, 606): srf = renpy.display.draw.screenshot(None)
        else: srf = renpy.display.draw.screenshot(None, False)
        return srf


    ############################## INVERT ##############################

    # This class defines the code to invert the screen in 'screen invert'
    class InvertScreenAnimated(renpy.Displayable):
        def __init__(self, delay=0.0, screenshot_delay=0.0):
            super(InvertScreen, self).__init__()
            self.width, self.height = renpy.get_physical_size()
            self.height = self.width * 9 / 16
            self.delay = delay

        def invert():
            srf = screenshot_srf()
            inv = renpy.Render(srf.get_width(), srf.get_height()).canvas().get_surface()
            inv.fill((255,255,255,255))
            inv.blit(srf, (0,0), None, 2)
            return inv

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            if st >= self.delay:
                render.blit(self.invert(), (0, 0))
            return render


    ############################## TEAR ##############################

    # TearObject - один сдвиг глитчей (не меняются)
    # TearObjectAnimated - повторение сдвигов (меняются)

    ###### TearObjectAnimated ######
    #
    # timeout_base:
    #     The time in seconds between two changes of the glitching.
    #     Can be either single float (or integer) value, or a tuple of two values between which the timeout
    #     will be chosen following a uniform distribution, respecting the randomkey.
    #     Defaults to .1 second.
    #
    # timeout_vanilla:
    #     The length in seconds of the periods of time over which the child will be shown without any glitch.
    #     Same values and meaning as `timeout_base`, except that if False, the child will never be shown without glitching.
    #     If `timeout_base` is passed, defaults to the same value. Otherwise, defaults to (1, 3).

    ###### TearObject ######
    #
    # randomkey:
    #     Follows the rules of the random modume's seed function.
    #     If not set, a random seed is generated when the transform is applied,
    #     and stays the same afterwards.
    #     If you want the effect to be random for each render operation, set to None.
    #
    # chroma: Boolean, whether to apply the chromatic aberration effect.
    #
    # minbandheight: Minimum height of each slice.
    #
    # offset: The offset of each slice will be between -offset and offset pixels.
    #
    # nslices:
    #     Number of slicings to do (the number of slices will be nslices + 1).
    #     Setting this to 0 is not supported.
    #     None (the default) makes it random.

    class TearObject(renpy.Displayable):
        NotSet = object()

        def __init__(self, child, *, randomkey=NotSet, chroma=True, minbandheight=1, offset=30, nslices=None, **properties):
            super().__init__(**properties)
            self.child = renpy.displayable(child)
            if randomkey is self.NotSet:
                randomkey = renpy.random.random()
            self.randomkey = randomkey
            self.chroma = chroma
            self.minbandheight = minbandheight
            self.offset = offset
            self.nslices = nslices

        def render(self, width, height, st, at):
            child = self.child
            child_render = renpy.render(child, width, height, st, at)
            cwidth, cheight = child_render.get_size()
            if not (cwidth and cheight):
                return child_render
            render = renpy.Render(cwidth, cheight)
            randomobj = renpy.random.Random(self.randomkey)
            chroma = self.chroma and renpy.display.render.models
            offset = self.offset
            minbandheight = self.minbandheight
            nslices = self.nslices
            if nslices is None:
                nslices = min(int(cheight/minbandheight), randomobj.randrange(10, 21))

            theights = sorted(randomobj.randrange(int(cheight)+1) for k in range(nslices)) # y coordinates demarcating all the strips
            offt = 0 # next strip's lateral offset
            fheight = 0 # sum of the size of all the strips added this far

            while fheight < cheight:
                # theight is the height of this particular strip
                if theights: theight = max(theights.pop(0)-fheight, minbandheight)
                else: theight = cheight-theight

                slice_render = child_render.subsurface((0, fheight, cwidth, theight))

                if offt and chroma:
                    for color_mask, chponder in (((False, False, True, True), 1.25), ((False, True, False, True), 1.), ((True, False, False, True), .75)):
                        chroma_render = slice_render.subsurface((0, 0, cwidth, theight))
                        chroma_render.add_property("gl_color_mask", color_mask)
                        render.blit(chroma_render, (round(offt*chponder), round(fheight)))
                else:
                    render.blit(slice_render, (offt, round(fheight)))

                fheight += theight
                if offt: offt = 0
                else: offt = randomobj.randrange(-offset, offset+1)

            return render

        def visit(self):
            return [self.child]

    class TearObjectAnimated(TearObject):
        def __init__(self, *args, timeout_base=None, timeout_vanilla=None, **kwargs):
            super().__init__(*args, **kwargs)
            if timeout_vanilla is None:
                if timeout_base is None: timeout_vanilla = (1, 3)
                else: timeout_vanilla = timeout_base
            if timeout_base is None: timeout_base = .1

            self.timeout_base = timeout_base
            self.timeout_vanilla = timeout_vanilla
            self.set_timeout(vanilla=(timeout_vanilla is not False))

        def set_timeout(self, vanilla, st=0):
            if vanilla: timeout = self.timeout_vanilla
            else: timeout = self.timeout_base

            if not isinstance(timeout, (int, float)):
                timeout = renpy.random.Random(self.randomkey).uniform(*timeout)

            self.timeout = timeout + st
            self.showing_vanilla = vanilla

        def render(self, width, height, st, at):
            vanilla = self.showing_vanilla

            if st >= self.timeout:
                randomkey = self.randomkey
                randomobj = renpy.random.Random(randomkey)
                self.randomkey = randomobj.random()

                if vanilla or (self.timeout_vanilla is False): # determine whether to show vanilla or not
                    vanilla = False # if we were showing it or if showing it is disabled
                else:
                    vanilla = (randomobj.random() < .3)

                self.set_timeout(vanilla, st)

            renpy.redraw(self, st-self.timeout)

            if vanilla:
                return renpy.render(self.child, width, height, st, at)
            else:
                return super().render(width, height, st, at)


    # This class defines the code for the tear piece effect in 'screen tear'.
    class TearScreenPiece:
        def __init__(self, startY, endY, offtimeMult, ontimeMult, offsetMin, offsetMax):
            self.startY = startY
            self.endY = endY
            self.offTime = (random.random() * 0.2 + 0.2) * offtimeMult
            self.onTime = (random.random() * 0.2 + 0.2) * ontimeMult
            self.offset = 0
            self.offsetMin = offsetMin
            self.offsetMax = offsetMax

        def update(self, st):
            st = st % (self.offTime + self.onTime)
            if st > self.offTime and self.offset == 0:
                self.offset = random.randint(self.offsetMin, self.offsetMax)
            elif st <= self.offTime and self.offset != 0:
                self.offset = 0

    # This class defines the code for the 'screen tear' effect in-game.
    class TearScreenAnimated(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf=None):
            super(TearScreenAnimated, self).__init__()
            self.width, self.height = renpy.get_physical_size()

            if float(self.width) / float(self.height) > 16.0 / 9.0:
                self.width = self.height * 16 // 9
            else:
                self.height = self.width * 9 // 16

            self.number = number
            self.srf = srf if srf else screenshot_srf()

            self.pieces = []
            tearpoints = [0, self.height]

            for i in range(number):
                tearpoints.append(random.randint(0, self.height))

            tearpoints.sort()

            for i in range(number + 1):
                self.pieces.append(TearScreenPiece(tearpoints[i], tearpoints[i+1], offtimeMult, ontimeMult, offsetMin, offsetMax))

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            render.blit(self.srf, (0,0))
            for piece in self.pieces:
                piece.update(st)
                subsrf = self.srf.subsurface(0, max(0, piece.startY - 1), self.width, max(0, piece.endY - piece.startY))
                render.blit(subsrf, (piece.offset, piece.startY))
            renpy.redraw(self, 0)
            return render


    ############################## ANIMATED MASK ##############################

    class AnimatedMask(renpy.Displayable):

        def __init__(self, child, mask, maskb, oc, op, moving=True, speed=1.0, frequency=1.0, amount=0.5, **properties):
            super(AnimatedMask, self).__init__(**properties)
            self.child = renpy.displayable(child)
            self.mask = renpy.displayable(mask)
            self.maskb = renpy.displayable(maskb)
            self.oc = oc
            self.op = op
            self.null = None
            self.size = None
            self.moving = moving
            self.speed = speed
            self.amount = amount
            self.frequency = frequency

        def render(self, width, height, st, at):
            cr = renpy.render(self.child, width, height, st, at)
            mr = renpy.render(self.mask, width, height, st, at)
            mb = renpy.Render(width, height)

            if self.moving:
                mb.place(self.mask, ((-st * 50) % (width * 2)) - (width * 2), 0)
                mb.place(self.maskb, -width / 2, 0)
            else:
                mb.place(self.mask, 0, 0)
                mb.place(self.maskb, 0, 0)

            cw, ch = cr.get_size()
            mw, mh = mr.get_size()

            w, h = min(cw, mw), min(ch, mh)

            if self.size != (w, h):
                self.null = Null(w, h)

            nr = renpy.render(self.null, width, height, st, at)

            rv = renpy.Render(w, h)

            complete = self.oc + math.pow(math.sin(st * self.speed / 8), 64 * self.frequency) * self.amount

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = 1.0
            rv.operation_complete = complete
            rv.operation_parameter = self.op

            ### Фикс GL2 ###

            op = self.op
            if op < 1: op = 1

            start, end = -1.0, op / 256.0
            offset = start + (end - start) * complete

            rv.mesh = True # Применение шейдера к изображению

            rv.add_shader("renpy.imagedissolve")
            rv.add_uniform("u_renpy_dissolve_offset", offset)
            rv.add_uniform("u_renpy_dissolve_multiplier", 256.0 / op)

            # Mipmaps - предварительно отрендеренные версии текстуры разных размеров, которые используются для улучшения качества изображения
            # при масштабировании
            rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            ################

            rv.blit(mb, (0, 0), focus=False, main=False)
            rv.blit(nr, (0, 0), focus=False, main=False)
            rv.blit(cr, (0, 0))

            renpy.redraw(self, 0)
            return rv


    ############################## SHAKE ##############################

    # Пример (экран/спрайт): with shake(позиция экрана, время, отклонение)
    class Shaker(object):
        anchors = { 'top': 0.0, 'center': 0.5, 'bottom': 1.0, 'left': 0.0, 'right': 1.0 }

        def __init__(self, start, dist, child):
            if start is None: start = child.get_placement()
            self.start = [ self.anchors.get(i, i) for i in start ]
            self.dist = dist
            self.child = child

        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None: x = 0
                if isinstance(x, float): return int(x * r)
                else: return x

            xpos, ypos, xanchor, yanchor = [fti(a, b) for a, b in zip(self.start, sizes)]
            xpos, ypos = xpos - xanchor, ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start=(0, 0, 0, 0), time=1.0, dist=30, child=None, **properties):
        return renpy.display.layout.Motion(Shaker(start, dist, child), time, child, add_sizes=True, **properties)

    shake = renpy.curry(_Shake)



    ############################## RECT, PARTICLEBURST, BLOOD ##############################

    # Пиксели-помехи (поломанный спрайт Сайори в меню во 2 акте)
    class RectStatic(object):
        def __init__(self, theDisplayable, numRects=12, rectWidth = 30, rectHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.timers = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.rectWidth = rectWidth
            self.rectHeight = rectHeight

            for i in range(self.numRects):
                self.add(self.displayable)
                self.timers.append(random.random() * 0.4 + 0.1)

        def add(self, d):
            s = self.sm.create(d)
            s.x = random.randint(0, 40) * 32
            s.y = random.randint(0, 23) * 32
            s.width = self.rectWidth
            s.height = self.rectHeight
            self.rects.append(s)

        def update(self, st):
            for i, s in enumerate(self.rects):
                if st >= self.timers[i]:
                    s.x = random.randint(0, 40) * 32
                    s.y = random.randint(0, 23) * 32
                    self.timers[i] = st + random.random() * 0.4 + 0.1
            return 0

    # Пиксельные глаза и рот Нацуки
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth=30, areaHeight=30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight

            for i in range(self.numRects):
                self.add(self.displayable)

        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)

        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

    class ParticleBurst(object):
        def __init__(self, theDisplayable, pos_x = 640, pos_y = 360, explodeTime=0, numParticles=20, particleTime = 0.500, particleXSpeed = 3, particleYSpeed = 5):
            self.sm = SpriteManager(update=self.update)

            self.stars = [ ]
            self.displayable = theDisplayable
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.explodeTime = explodeTime
            self.numParticles = numParticles
            self.particleTime = particleTime
            self.particleXSpeed = particleXSpeed
            self.particleYSpeed = particleYSpeed
            self.gravity = 240
            self.timePassed = 0

            for i in range(self.numParticles):
                self.add(self.displayable, 1)

        def add(self, d, speed):
            s = self.sm.create(d)
            speed = random.random()
            angle = random.random() * 3.14159 * 2
            xSpeed = speed * math.cos(angle) * self.particleXSpeed
            ySpeed = speed * math.sin(angle) * self.particleYSpeed - 1
            s.x = self.pos_x + xSpeed * 24
            s.y = self.pos_y + ySpeed * 24
            pTime = self.particleTime
            self.stars.append((s, ySpeed, xSpeed, pTime))

        def update(self, st):
            sindex=0
            for s, ySpeed, xSpeed, particleTime in self.stars:
                if (st < particleTime):
                    s.x = self.pos_x + xSpeed * 120 * (st + .20)
                    s.y = self.pos_y + (ySpeed * 120 * (st + .20) + (self.gravity * st * st))
                else:
                    s.destroy()
                    self.stars.pop(sindex)
                sindex += 1
            return 0

    class Blood(object):
        def __init__(self, theDisplayable, density=120.0, particleTime=1.0, dripChance=0.05, dripSpeedX=0.0, dripSpeedY=120.0, dripTime=180.0, burstSize=100, burstSpeedX=200.0, burstSpeedY=400.0, numSquirts=4, squirtPower=400, squirtTime=0.25):
            self.sm = SpriteManager(update=self.update)
            self.drops = []
            self.squirts = []
            self.displayable = theDisplayable
            self.density = density
            self.particleTime = particleTime
            self.dripChance = dripChance
            self.dripSpeedX = dripSpeedX
            self.dripSpeedY = dripSpeedY
            self.gravity = 800.0
            self.dripTime = dripTime
            self.burstSize = burstSize
            self.burstSpeedX = burstSpeedX
            self.burstSpeedY = burstSpeedY
            self.lastUpdate = 0
            self.delta = 0.0

            for i in range(burstSize): self.add_burst(theDisplayable, 0)
            for i in range(numSquirts): self.add_squirt(squirtPower, squirtTime)

        # This function makes a single squirt of blood that follows an arc.
        def add_squirt(self, squirtPower, squirtTime):
            angle = random.random() * 6.283
            xSpeed = squirtPower * math.cos(angle)
            ySpeed = squirtPower * math.sin(angle)
            self.squirts.append([xSpeed, ySpeed, squirtTime])

        # This function makes a burst of blood that pops out of some area
        def add_burst(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.burstSpeedX + 20
            ySpeed = (random.random() - 0.75) * self.burstSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        # This function makes a dripping stream of blood
        def add_drip(self, d, startTime):
            s = self.sm.create(d)
            xSpeed = (random.random() - 0.5) * self.dripSpeedX + 20
            ySpeed = random.random() * self.dripSpeedY + 20
            pTime = self.particleTime
            self.drops.append([s, xSpeed, ySpeed, pTime, startTime])

        def update(self, st):
            delta = st - self.lastUpdate
            self.delta += st - self.lastUpdate
            self.lastUpdate = st

            sindex = 0
            for xSpeed, ySpeed, squirtTime in self.squirts:
                if st > squirtTime: self.squirts.pop(sindex)
                sindex += 1

            pindex = 0
            if st < self.dripTime:
                while self.delta * self.density >= 1.0:
                    self.delta -= (1.0 / self.density)
                    if random.random() >= 1 - self.dripChance: self.add_drip(self.displayable, st)
                    for xSpeed, ySpeed, squirtTime in self.squirts:
                        s = self.sm.create(self.displayable)
                        s.x += (random.random() - 0.5) * 5
                        s.y += (random.random() - 0.5) * 5
                        self.drops.append([s, xSpeed + (random.random() - 0.5) * 20, ySpeed + (random.random() - 0.5) * 20, self.particleTime, st])
            for s, xSpeed, ySpeed, particleTime, startTime in self.drops:
                if (st - startTime < particleTime):
                    s.x += xSpeed * delta
                    s.y += ySpeed * delta
                    self.drops[pindex][2] += self.gravity * delta
                else:
                    s.destroy()
                    self.drops.pop(pindex)
                pindex += 1
            return 0

## invert_screen
# Syntax
#   length - This declares how long the effect plays for.
#   delay - Delays the effect for X time before it starts.
screen invert_screen(length, delay=0.0):
    add InvertScreenAnimated(delay) size(1280, 720)
    timer delay action PauseAudio("music")
    timer delay action Play("sound", "sfx/glitch1.ogg")
    timer length + delay action Hide("invert")
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action [PauseAudio("music", False), Stop("sound"), Function(hide_windows_enabled, enabled=True)]

## tear_screen
# Syntax
#   number - This declares how many pieces the screen tears on-screen.
#   offtimeMult - This declares the multiplier of time the effect lasts off.
#   ontimeMult - This declares the multiplier of time the effect lasts on.
#   offsetMin - This declares the minimum offset of time by the multiplier.
#   offsetMax - This declares the minimum offset of time by the multiplier.
#   srf - This declares the screen image from 'screenshot_srf' if it is declared.
screen tear_screen(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None):
    zorder 150
    add TearScreenAnimated(number, offtimeMult, ontimeMult, offsetMin, offsetMax, srf) size(1280, 720)
    on "show" action Function(hide_windows_enabled, enabled=False)
    on "hide" action Function(hide_windows_enabled, enabled=True)


# multiple black squares to the screen
image m_rectstatic:
    RectStatic(Solid("#000"), 32, 32, 32).sm
    pos (0, 0)
    size (32, 32)

# multiple squares of the DDLC logo to the screen
image m_rectstatic2 = RectStatic(im.FactorScale(im.Crop("gui/logo.png", (100, 100, 128, 128)), 0.25), 2, 32, 32).sm

# multiple squares of Sayori's menu sprite to the screen
image m_rectstatic3 = RectStatic(im.FactorScale(im.Crop("gui/menu_art_s.png", (100, 100, 64, 64)), 0.5), 2, 32, 32).sm


# Звёзды при столкновениях
image particle_star:
    alpha 1.0
    ParticleBurst("gui/menu_particle.png", pos_x=640, pos_y=275, explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=15, particleYSpeed=15).sm
    easeout 1.5 alpha 0


# This image transform adds a blood drop that gets longer and thinner over time.
image particle_blood_drip:
    "gui/blood_drop.png"
    yzoom 0 yanchor 0.2 subpixel True
    linear 10 yzoom 8

# This image transform adds a blood drop that gets thinner randomly by time.
image particle_blood:
    "gui/blood_drop.png"
    subpixel True alpha 0.75
    zoom 0.75
    choice:
        linear 0.25 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.35 zoom 0
    choice:
        linear 0.55 zoom 0

# This image transform adds a blood drop that squirts and drops for three minutes.
image blood:
    size (1, 1)
    truecenter
    Blood("particle_blood").sm

# This image transform adds a blood drop that doesn't squirts, and increases the chance of dropping.
image blood_eye:
    size (1, 1)
    truecenter
    Blood("particle_blood", dripChance=0.5, numSquirts=0).sm

image blood_eye_rare:
    size (1, 1)
    truecenter
    Blood("particle_blood", dripChance=0.005, numSquirts=0, burstSize=0).sm


## Veins
image veins:
    AnimatedMask("images/bg/veinmask.png", "images/bg/veinmask.png", "images/bg/veinmaskb.png", 0.15, 16, moving=False, speed=10.0, frequency=0.25, amount=0.1)
    subpixel True
    xanchor 0.05 zoom 1.10
