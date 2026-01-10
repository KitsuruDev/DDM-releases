## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

## lockdown_check.rpy
# This file is mainly designed to warn new modders about bugs with certain Ren'Py versions or warn them about QA issues with
# running Ren'Py versions higher than the one the mod template was tested for.
# New in 4.0.0: Add lockout for Ren'Py 6/7 on Py 3 templates.

## DO NOT MODIFY THIS FILE! ##

# Checks if we are on Ren'Py 8
init -100 python:
    if renpy.version_tuple < (8, 0, 0):
        raise NotRenPyEight

label lockdown_check:
    $ version = renpy.version()

    if renpy.version_tuple > (8, 5, 0, 25111603):
        scene black
        "{b}ВНИМАНИЕ:{/b} Версия RenPy, на которой вы хотите запустить данный мод, не была протестирована на совместимость с ним."
        "Последняя версия 8-ого RenPy, которая гарантированно работает с данным модом без ошибок -- \"{b}Ren'Py 8.3.7{/b}\"."
        "Запуск мода на более новой версии может привести к возникновению ошибок и багов, нарушающих работу игры."
        menu:
            "Продолжая запускать свой мод на [version!q], вы подтверждаете, что ознакомились с данным предупреждением, и готовы к проблемам, которые могут возникнуть в непроверенной версии RenPy."
            "Подтверждаю":
                pass

    $ persistent.lockdown_warning = True

    return
