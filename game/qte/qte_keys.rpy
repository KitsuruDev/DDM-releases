# qte_keys.rpy

init python:

    qte_keys = {
        _("ЛКМ"): "mousedown_1",
        "A": ["a", "ф"],
        "D": ["d", "в"],
        "S": ["s", "ы"],
        "W": ["w", "ц"],
        _("ПРОБЕЛ"): "K_SPACE",
        "↑": "K_UP",
        "↓": "K_DOWN",
        "←": "K_LEFT",
        "→": "K_RIGHT",
    }


screen qte_key_interactive(need_key, sec=3, lim=10):
    style_prefix "qte_key_interactive"

    text "[need_key]" at animation_qte_text

    key qte_keys[need_key] action If(qte_progress < lim, true=SetVariable("qte_progress", qte_progress+1), false=[SetVariable("qte_progress", 0), Return(1)])

    timer sec action Return(0)


style qte_key_interactive_text:
    font "mod_assets/font/menu/Vivl-rail.ttf"
    color "#0ef"
    size 90
    text_align 0.5
    align (0.5, 0.5)


transform animation_qte_text:
    parallel:
        ease 0.9 alpha 0.2
        ease 0.9 alpha 1.0
        repeat
    parallel:
        ease 0.15 yoffset(-6)
        ease 0.15 yoffset(6)
        repeat
