# __imports__.rpy

python early:
    from datetime import date
    import math
    import random
    import re, os
    import subprocess, platform

init python:
    from store.Tags import (
        bounce_tag, scare_tag, rotate_tag, swap_tag, move_tag, gradient_tag, gradientMove_tag, glitch_tag, explode_tag,
        explodeVolumetric_tag, atl_tag
    )

    from store.Effects import (
        InvertScreenAnimated, TearObjectAnimated, TearScreenAnimated, AnimatedMask, RectStatic, RectCluster, ParticleBurst,
        Blood, shake, screenshot_srf
    )
    
    from store.Achievements import Achievement, AchievementCount
    from store.GalleryCG import GalleryCGImage
    from store.GalleryBG import GalleryBGImage
    from store.Characters import CharactersImage
    from store.MusicPlayer import Track

    # Проверка установленных библиотек
    def available_libraries(output_file = config.basedir + "/available_libraries.txt"):
        modules = set()
        for module_name in sys.modules.keys():
            parts = module_name.split('.')
            modules.add(parts[0]) # только имена верхнего уровня
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("Список доступных библиотек Python (модули верхнего уровня):\n")
            for module_name in sorted(modules):
                f.write(f"- {module_name}\n")
