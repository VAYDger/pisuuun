define a = Character(_(''), color="#575a4e", kind=nvl)

image anim = Movie(play="images/anim3.webm", pos=(0, 0), anchor=(0, 0))

screen imagebutton_rollforward():
    frame:
        padding(-42,-42)
        xalign 0.73 ypos 900
        imagebutton:
            idle "rollfront_idle"
            hover "rollfront_hover"

            action Return()

screen imagebutton_rollback():
    frame:
        padding(-42,-42)
        xalign 0.27 ypos 900
        imagebutton:
            idle "rollback_idle"
            hover "rollback_hover"

            action Rollback()

label start:

    show screen imagebutton_rollback
    show screen imagebutton_rollforward

    scene bg
    pause 0.5
    show text "{size=+8}{font=TimesNewRomanRegular.ttf}{i}Пролог{/i}{/font}{/size}":
        xpos 555 yalign 0.145
    show polar
    show screen bookmark1_disabled
    show ph1 behind polar
    show bgpolar behind ph1
    with dissolve

    a "Это первая реплика пролога." with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "Это вторая реплика пролога." with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "А это третья." with dissolve

    hide screen imagebutton_rollback
    hide screen imagebutton_rollforward
    nvl clear
    with dissolve
    pause 0.5
    
define menu = nvl_menu

menu:   

    "{image=arrow_left}хуй{image=arrow_right}":
        hide text
        hide polar
        hide bgpolar
        hide ph1
        nvl clear
        with dissolve
        show anim
        pause 1.0
        hide anim
        pause 0.5
        jump choise1
    
    "{image=arrow_left}пенис{image=arrow_right}":
        hide text
        hide polar
        hide bgpolar
        hide ph1
        nvl clear
        with dissolve
        show anim
        pause 1.0
        hide anim
        pause 0.5             
        jump choise2
    
label choise1:

    $ renpy.fix_rollback()

    show text "{size=+8}{font=TimesNewRomanRegular.ttf}{i}Не Пролог{/i}{/font}{/size}":
        xpos 580 yalign 0.145
    show polar
    show ph2 behind polar
    show bgpolar behind ph2
    show screen imagebutton_rollback
    show screen imagebutton_rollforward
    with dissolve

    a "Вы выбрали \"хуй\", поздравляю!" with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "Вы хороший мальчик" with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "Мама будет гордиться вами" with dissolve

    jump choisedone1

label choisedone1:

    hide ph2
    nvl clear
    with dissolve
    pause 0.5

    show ph1 behind polar
    a "Гордиться тем, что у нее сын - ПОЛНЫЙ\nИДИОТ" with dissolve

    show black

    "{size=+100}{b}BAD ENDING{/b}{/size}"

    return

label choise2:


    a "ПЕЕЕЕЕЕЕНИИИИИИИС"

    jump choisedone2

label choisedone2:

    "УААА КАКОЙ МОЛОДЕЦ МОЙ ПИЗДЮК"

    show black

    "{size=+100}{b}GOOD ENDING{/b}{/size}"

    return