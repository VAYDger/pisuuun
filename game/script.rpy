define a = Character(_(''), color="#575a4e", kind=nvl)

label start:

    scene bg
    
    show text "{i}Пролог{/i}":
        xalign 0.275 yalign 0.145

    show polar 
    show ph1 behind polar

    a "Пролог_пролог_пролог_пролог_пролог_пролог пролог_пролог_пролог_пролог_пролог_пролог пролог_пролог_пролог_пролог_пролог_пролог" with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "дрдрдрдрдрдрдрдрдррддрдрдрдрдрдрдр" with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "dfdfdfdfdfdfdfdf" with dissolve

    window hide
    hide text
    hide polar
    hide ph1
    with dissolve

menu:

    "хуй":
        jump choise1

    "пенис":
        jump choise2

label choise1:

    show text "{i}НеПролог{/i}":
        xalign 0.275 yalign 0.145

    show polar
    show ph2 behind polar
    window show
    with dissolve

    a "ХХХХХУУУУУУУУУУЙ" with dissolve

    window hide
    pause 0.5
    nvl clear
    window show

    a "dsadad" with dissolve

    with dissolve
    hide polar
    hide ph2
    with dissolve

    jump choisedone1

label choisedone1:

    show polar
    show ph1 behind polar
    with dissolve

    a "ДИ НАХУ БИЛЯ" with dissolve

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