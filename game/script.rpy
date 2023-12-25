define a = Character(_(''), color="#575a4e", kind=nvl)

label start:
    
    scene bg
    pause 0.5
    show text "{size=+8}{font=TimesNewRomanRegular.ttf}{i}Пролог{/i}{/font}{/size}":
        xpos 555 yalign 0.145
    show polar 
    show ph1 behind polar
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

    window hide
    pause 0.5
    nvl clear

define menu = nvl_menu

menu:
    a "Ну и четвертая."
    "хуй":
        window hide
        pause 0.5
        nvl clear
        window show
        jump choise1
    
    "пенис":
        window hide
        pause 0.5
        nvl clear
        window show        
        jump choise2
    
label choise1:

    hide text
    hide polar
    hide ph1
    nvl clear
    with dissolve
    pause 0.5

    show text "{size=+8}{font=TimesNewRomanRegular.ttf}{i}Не Пролог{/i}{/font}{/size}":
        xpos 580 yalign 0.145
    show polar
    show ph2 behind polar
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

    hide polar
    hide ph2
    nvl clear
    with dissolve
    pause 0.5

    jump choisedone1

label choisedone1:

    show polar
    show ph1 behind polar
    with dissolve

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