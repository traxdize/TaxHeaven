# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character('Joko', color="#c000fb")
define amanda = Character('Amanda Kartikasari', color="#eeff00")
define seller = Character('Kang Gorengan', color="#ffffff")
define center = Position(xalign=0.5, yalign=0.5)
define left = Position(xalign=0.1, yalign=0.5)
define right = Position(xalign=0.9, yalign=0.5)
define center_screen = Position(xalign=0.5, yalign=0.5)

label start:
    
    stop music
    play music "type.mp3"

    centered "{color=#ffffff}{cps=10}SABTU, 19 NOVEMBER 2023\n{cps=5}BANDUNG\n{cps=2}11:40"
    
    stop music
    play music "warung.mp3"

    scene bg kota
    with dissolve

    "{cps=40}Ah, kota Bandung{cps=10}..."
    "{cps=40}Menurutku kota ini bagus, ada banyak tempat indah dan banyak potensi."
    "Lokasinya yang berada di daerah bukit juga membuat kota ini bisa menjadi tempat wisata."
    "Tetapi ada keganjalan, kota ini selalu begini selama 10 tahun terakhir,"
    "hanya muncul bangunan kantor dan pabrik yang mengotori udara,"
    "wali kota sudah menjanjikan akan mengubahnya, "
    "tetapi selama ini tetap tidak ada apa-apa."

    jump cutscene1

label cutscene1:

    scene bg trotoar
    with dissolve

    pause(1)
    
    "Semuanya aneh....sangat aneh,"
    "pajak yang besar untuk kota ini,"
    "semua pembuatan bangunan yang menjanjikan kemajuan."
    "Sangat tidak masuk akal."

    jump cutscene2

label cutscene2:

    scene bg gorengan
    with dissolve

    show kang gorengan at center
    with dissolve

    joko "Bang minta tahu gorengnya 5 biji ya"
    seller "Siapp mas!🫡"

    # show cg bungkus gorengan
    
    


    return
