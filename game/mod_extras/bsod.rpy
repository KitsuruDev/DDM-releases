# bsod.rpy

## BSOD screen ##################################################################\
##
## This screen is used to fake a BSOD/kernel panic on the players' computer
## on all platforms (Mobile devices defaults to the Linux BSOD).
##
## Syntax:
##     bsodCode - The error code message you want to show the player. Defaults to
##                DDLC_ESCAPE_PLAN_FAILED if no message is given.
##     bsodFile (Windows 7 Only) - The fake file name that caused the
##                error. Defaults to libGLESv2.dll if no file name is given.
##     rsod (Windows 11 Only) - Swaps the Windows 11 BSOD with a RSOD -- заменён на рандомную активацию 50/50
##
## Examples:
##     show screen bsod("DOKI_DOKI", "renpy32.dll")      #, False)
##     show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED")  #, rsod=True)

init python:

    cursor = 0

    def fakePercent(st, at, winver):
        percent = int(0 + (st * 5)) if int(0 + (st * 5)) < 100 else 100
        if winver == 8:
            d = Text(_("перезагрузка. (выполнено: %(percent)s%%)") % {"percent": str(percent)}, style="bsod_win8_text", size=26)
        else:
            d = Text(_("(выполнено: %(percent)s%%)") % {"percent": str(percent)}, style="bsod_win10_text", line_leading=25)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.3
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.3

    if renpy.windows:
        try: osVer = tuple(map(int, subprocess.run("powershell (Get-WmiObject -class Win32_OperatingSystem).Version", check=True, shell=True, stdout=subprocess.PIPE).stdout.split(b"."))) # Vista+
        except: osVer = tuple(map(int, platform.version().split("."))) or (5, 1, 2600) # XP returns JIC (but Ren'Py 8 doesn't even support XP...)


## Если нет подсчёта процентов
## Вызов: call screen bsod_enter
screen bsod_enter:
    key ["K_KP_ENTER", "K_RETURN"] action Return()


screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll"):
    layer "master"

    if renpy.windows:
        if osVer < (6, 2, 9200): # Windows 7 - самый оригинальный экран в итоге остаётся за кулисами...

            add Solid("#000082")

            vbox:
                style_prefix "bsod_win7"

                text _("Проблема была обнаружена, и Mindows был закрыт для предотвращения повреждения компьютера.")
                text _("Похоже, что проблема вызвана следующим файлом: %(filename)s") % {"filename": bsodFile.upper()}
                text bsodCode.upper()
                text _("Если вы впервые видите этот экран стоп-ошибки, проанализируйте мысли. Если этот экран появляется снова, выполните следующие действия:")
                text _("Проверьте, правильно ли установлена новая информация или логические заключения. Если это новая установка, обратитесь к психологу-специалисту или производителю информации или логических заключений за обновлениями Mindows, которые могут вам понадобиться.")
                text _("Если проблемы продолжаются, отключите или удалите всю установленную информацию или логические заключения. Отключите параметры памяти Amygdala, такие как страх или эмоциональная реакция. Если вам необходимо использовать режим реальной жизни для восстановления работы мозга, то перезагрузите его, нажав клавишу Enter.")
                text _("Техническая информация:")
                text _("*** СТОП: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317, 0x00000000)\n")
                text "*** " + bsodFile.upper() + "  -  Address FBF92317 base at FBF102721, Datestamp 3d6dd67c"

        elif osVer < (10, 0, 10240): # Windows 8/8.1

            add Solid("#1273aa")

            vbox:
                style_prefix "bsod_win8"
                xalign 0.5 yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text _("В вашем мозге возникла проблема, и его необходимо")
                text _("перезагрузить. Мы собираем сведения о логике")
                text _("ошибки, а затем будет автоматически выполнена")
                add DynamicDisplayable(fakePercent, 8)
                text _("Файл, в котором вызвана ошибка: %(filename)s") % {"filename": bsodFile.upper()} style "bsod_win10_sub_text"
                text _("\nПри желании вы можете найти в психологии информацию по этому коду ошибки: ") + bsodCode.upper() style "bsod_win8_sub_text"

        else: # Windows 10/11

            if osVer < (10, 0, 22000):
                add Solid("#0078d7")
            else:
                if renpy.random.randint(0, 1) == 0:
                    add Solid("#000000")
                    python:
                        blackCol = "#0078d7"
                else:
                    add Solid("#d40e0eff")
                    python:
                        blackCol = "#f00"


            vbox:
                style_prefix "bsod_win10"
                xalign 0.3 yalign 0.3

                text ":(" style "bsod_win10_sad_text"
                text _("В вашем мозге возникла проблема, и его необходимо перезагрузить.")
                text _("Мы собираем сведения о логике ошибке, а затем будет автоматически")
                text _("выполнена перезагрузка.")

                add DynamicDisplayable(fakePercent, 10)

                hbox:
                    if osVer < (10, 0, 22000):
                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/mod_extra_images/bsod_qr_code.png", im.matrix.colorize("#0078d7", "#fff"), ) at bsod_qrcode(100)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text _("Доп. сведения об этой проблеме и возможные способы её решения см. здесь: http://ddlc.moe/help.html") style "bsod_win10_info_text" line_leading 25
                            text _("При обращении в службу психологической поддержки предоставьте следующие данные:") style "bsod_win10_sub_text" line_leading 25
                            text _("Файл, в котором вызвана ошибка: %(filename)s") % {"filename": bsodFile.upper()} style "bsod_win10_sub_text"
                            text _("Код остановки: %(code)s") % {"code": bsodCode.upper()} style "bsod_win10_sub_text"
                    else:
                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/mod_extra_images/bsod_qr_code.png", im.matrix.colorize(blackCol, "#fff"), ) at bsod_qrcode(150)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text _("Дополнительные сведения об этой проблеме и возможные способы её решения см. здесь:") style "bsod_win10_info_text" line_leading 25
                            text "http://ddlc.moe/help.html\n" style "bsod_win10_info_text"
                            text _("При обращении в службу психологической поддержки предоставьте следующие данные:") style "bsod_win10_sub_text"
                            text _("Файл, в котором вызвана ошибка: %(filename)s") % {"filename": bsodFile.upper()} style "bsod_win10_sub_text"
                            text _("Код остановки: %(code)s") % {"code": bsodCode.upper()} style "bsod_win10_sub_text"

    elif renpy.macintosh: # Mac OS - как по мне - самый криповый из всех

        add Solid("#222")
        add im.MatrixColor("mod_assets/elements/logo/window_icon.png", im.matrix.desaturate() * im.matrix.brightness(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54

        vbox:
            style_prefix "bsod_mac"
            xalign 0.53 yalign 0.51

            text "Вам необходимо перезагрузить мозг. Нажмите кнопку Enter,\n"
            text "чтобы он выключился, затем снова возвращайтесь в реальный мир." line_spacing 25
            text "You need to restart your mind. Press Enter button\n"
            text "to turn it off, then return to the real world again." line_spacing 25
            text "Redémarrez l'esprit. Appuyez sur la touche Entrée\n"
            text "pour l'éteindre, puis revenir au monde réel." line_spacing 25
            text "Necesitas reiniciar tu mente. Presione el botón Enter\n"
            text "para que se apague, luego regrese al mundo real nuevamente." line_spacing 25
            text "Sie müssen Ihr Gehirn neu starten. Drücken Sie die Enter-Taste,\n"
            text "um sie auszuschalten, und kehren Sie dann wieder in die reale\n"
            text "Welt zurück." line_spacing 25
            text "È necessario riavviare il cervello. Premi il pulsante Invio\n"
            text "per spegnerlo, quindi torna di nuovo nel mondo reale."

    else: # Linux - создатели шаблона настолько увлеклись текстом, что часть строк вылезла за экран. Пришлось, к сожалению, их урезать

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "Mindux-pci.c:v[config.version] 9/01/2022 Mindux"
            text "hd0: MINDUX VIRTUAL HARDDISK, ATA DISK drive"
            text "sda0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: MINDUX VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "sr0 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: MINDUX VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A] -> Link [[LNKC] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Mindux LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "sda: max request size: 4MiB"
            text "sda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "sr0: ATAPI 16x CD-ROM drive, 2MB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: [renpy.version_tuple]"
            text "Begin: Mind.so"
            text "Mind.so[[3352]: Faled to initialize thoughts: FileNotFoundError(\"Could not find module '/usr/app/ddlc/lib/py3-linux-x86_64/thoughts_api64.so') (or one of its dependencies). Try using the full path with constructor syntax.\")"
            text "Mind.so[[3352]: nvdrs: Loaded, about to disable thread optimizations."
            text "Mind.so[[3352]: nvdrs: Disabled thread optimizations."
            text "Mind.so: SUCCESS."
            text "Begin: Mind.so -> linux-5.18"
            text "/init: /init: 151: " + bsodCode.upper() + ": 0xforce=panic"
            text "Kernel panic - not syncing: Attempted to kill init!"
            text "The system waits for the Enter key to reboot the mind and return to the real world..."
            add DynamicDisplayable(constantCursor)

    add Solid("#000000") at bsod_transition

style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 24
    line_leading 3
    line_spacing 0
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 16

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 136
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_mac_text is gui_text
style bsod_mac_text:
    font gui.default_font
    size 28
    outlines []
    line_spacing -30

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/F25_Bank_Printer.ttf"
    size 15
    outlines []
    line_leading 5

transform bsod_transition:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

transform bsod_qrcode(x):
    xysize(x,x)
