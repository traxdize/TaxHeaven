# The script of the game goes in this file.

##light taps, smaller intervals
define soundsoft = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_soundsoft(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing soft until the text ends
            renpy.sound.play(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            renpy.sound.queue(renpy.random.choice(soundsoft))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define joko = Character('Joko', color="#c000fb",callback=type_soundsoft)
define amanda = Character('Amanda Kartikasari', color="#007bff", callback=type_soundsoft)
define seller = Character('Kang Gorengan', color="#ffaa00", callback=type_soundsoft)
define chg = Character('NPC', color="#eeee1a", callback=type_soundsoft)
define unk = Character('???', color="#ffffff", callback=type_soundsoft)
define ceo = Character('CEO', color="#ff0000", callback=type_soundsoft)
define akuntan = Character('Akuntan', color="#29ce47", callback=type_soundsoft)
define satpam = Character("Satpam", color="#ffffff", callback=type_soundsoft)
define polisi = Character("Polisi", color="#1c16be", callback=type_soundsoft)
define hakim = Character("Hakim", color="#16dfdf", callback=type_soundsoft)
define center = Position(xalign=0.5, yalign=0.5)
define left = Position(xalign=0.1, yalign=0.5)
define right = Position(xalign=0.9, yalign=0.5)
define rightcenter = Position(xalign=0.7, yalign=0.5)

label splashscreen:
    scene bg white with Dissolve(1)
    with Pause(1)
    show itb at center with Dissolve(1)
    with Pause(2)
    hide itb with Dissolve(1)
    show text "{color=#000000}Group 7 of PKWN Final Project{/color}" with Dissolve(1)
    with Pause(2)
    hide text with Dissolve(1)
    return

label start:
    stop music
    $ goodclue1= False
    $ goodclue2 = False
    $ badclue1 = False
    $ badclue2 = False
    $ goodclueact2 = False
    $ badclueact2 =False

    scene bg white with dissolve
    show itb at center with Dissolve(1)

    pause(2)

    hide itb
    scene bg blackout
    with Dissolve(1)

python:
    badend = 0
    name = ""
    while name != "Joko" and name != "joko" and name != "JOKO" and badend < 5:
        if badend == 0:
            name = renpy.input("Input namamu!")
        elif badend == 1:
            name = renpy.input("Namanya harus Joko btw")
        elif badend == 2:
            name = renpy.input("Namamu Joko!")
        elif badend == 3:
            name = renpy.input("NGERTI GA SIH NAMA LU JOKO")
        else:
            name = renpy.input("YANG BENER JOKO!!!!!!!")
        name = name.strip()
        if name == "Joe":
            name = renpy.input("WOLOH DARK SYSTEM ITU MAH!")
        badend += 1
    
if badend == 5:
    $ badend_n = True
    jump badend_nama
else:
    $ badend_n = False

    if badend_n:
        label badend_nama:
            scene bg horror with dissolve
            show chillguy_cropped at center with Dissolve(2.0)
            "DIBILANG NAMA LU JOKO!"
            hide chillguy_cropped
            scene bg darksouls 
            with dissolve
            pause(2)
            return
    
    play sound "type.mp3" volume 0.8

    centered "{size=40}{cps=10}SABTU, 19 NOVEMBER 2023\n{cps=5}BANDUNG\n{cps=2}11:40"

    stop sound

    play music "street.mp3" volume 0.7 loop

    scene bg kota with dissolve

    joko "Ah, kota Bandung{cps=5}..."
    "Menurutku kota ini bagus, ada banyak tempat indah dan banyak potensi."
    "Lokasinya yang berada di daerah bukit juga membuat kota ini bisa menjadi tempat wisata."
    "Tetapi ada sesuatu yang aneh, kota ini selalu begini selama 10 tahun terakhir,"
    "hanya muncul bangunan kantor dan pabrik yang mengotori udara,"
    "wali kota sudah menjanjikan akan mengubahnya, "
    "tetapi selama ini tetap tidak ada apa-apa."

    scene bg trotoar with dissolve

    pause(0.2)
    
    "Semuanya aneh{cps=5}....sangat aneh,"
    "pajak yang besar untuk kota ini,"
    "semua pembuatan bangunan yang menjanjikan kemajuan."
    "Sangat tidak masuk akal."

    stop music fadeout 3.0

    scene bg gorengan with dissolve

    play music "<from 3.0 to 54.0>gorengan.mp3" fadein 1.0 volume 0.03 loop

    show seller at center with Dissolve(0.6) 

    joko "Kang minta tahu gorengnya 5 biji ya"
    seller "Siapp mas!🫡"
    
    play sound "key item obtained.mp3"
    scene bg kertas with dissolve

    pause(4)

    "{cps=2}...{cps=15}!!!"

    "{cps=25}Tidak mungkin{cps=5}..."

    stop music fadeout 2.0

    play music "fastrun.mp3" loop volume 1.0
    play music "<from 22.0 to 94.0>trailer.mp3" fadein 3.0 volume 0.3

    scene bg lari with Dissolve(0.3)

    pause(4)

    scene bg buka with Dissolve(0.3)
    
    stop music
    play music "<from 26.6 to 94.0>trailer.mp3" volume 0.3

    play sound "pintu.mp3"
    pause(2)

    scene bg cek kertas with Fade(0.2, 0.2, 1, color="#FFFFFF")

    "{cps=20}SUDAH KUDUGA {cps=40}!!!"
    "Ada sesuatu yang berjalan dibelakang kota ini, penyebab kota ini tidak pernah 
    maju selama 10 tahun, semua ada hubungannya{cps=5}..."

    scene bg cinema with dissolve

    "Semua ada koneksinya, hanya aku yang bisa memecahkan ini, demi kotaku, demi keluargaku{cps=5}..."

    scene bg black with fade

    pause(0.5)

    show title at center with Dissolve(3)

    pause(4)

    stop music fadeout 3.0
    scene bg black with Dissolve(2.0)
    play sound "type.mp3" loop volume 0.8

    centered "{color=#ffffff}{size=60}{cps=2}ACT I"

    stop sound

    ## ACT 1

    # show cg bungkus gorengan

    scene bg cek kertas with Dissolve(3.0)
    
    joko "Hmmm, ada yang aneh dengan kertas gorengan ini..."

    "Coba kita lihat, transfer sebesar Rp4.5 miliar kepada perusahaan {b}Metecom{/b} dari ketua departemen keuangan{cps=5}...{cps=40} Kok nominalnya tidak asing ya?"

    "Sepertinya aku harus simpan kertas ini dan menanyakan ini ke Amanda saat di warung nanti."

    ## MASUK WARUNG SUNDA

    play music "warungsunda.mp3" volume 0.75

    scene bg warung sunda
    with dissolve

    show amanda-senyum with Dissolve(1.0)

    joko "Hei Amanda! Lihat yang aku temukan."
    
    amanda "Hah apaan lagi ini?"

    hide amanda-senyum 
    show amanda-ketawa
    with dissolve

    extend " kamu main detektif-detektifan lagi?"

    hide amanda-ketawa
    show amanda-senyum 
    with dissolve

    joko "Sudahlah, lihat ini saja."
    joko "Kenapa angka Rp4.5 miliar ini tidak asing ya?"

    hide amanda-senyum 
    show amanda-bingung 
    with dissolve

    amanda "Itu bukannya{cps=8}.... sebentar{cps=5}.."
    amanda "Gak mungkin sih{cps=5}..."

    ## KORAN SCENE

    scene bg koran with dissolve

    amanda "Kamu inget gak ini?"
    amanda "Berita tahun lalu yang uang pajak kota kita hilang sebesar Rp4.5 miliar!"

    joko "Tidak mungkin deh, pelakunya udah ditangkep."

    scene bg warung sunda with dissolve

    show amanda-senyum with Dissolve(0.3)
    amanda "Bener, tapi semuanya aneh, masa pelakunya secara sukarela menyerahkan diri?"
    
    hide amanda-senyum
    show amanda-bingung 
    with dissolve
    amanda "Sudah gitu, masa uangnya full dipake buat judi online?"
    amanda "Kalaupun benar dia melakukan itu, kenapa dia langsung ngaku dan kenapa uang sebesar itu bisa buat judol doang.."

    joko "Iya sih, kalau dipikir-pikir memang ada yang janggal."
    joko "{size=40}Kecuali, mungkin, dia bukan pelaku sebenarnya!{/size}"
    
    hide amanda-bingung
    show amanda-shock 
    with dissolve
    amanda "Bisa jadi dia hanya pion untuk menyembunyikan pelaku sebenarnya!"
    
    hide amanda-shock
    show amanda-bingung 
    with dissolve
    amanda "Kalau begitu apa yang harus kita lakukan?"

    joko "Aku harus segera ke tukang gorengan itu!"
    joko "Aku harus cari tahu dari mana dia dapat kertas itu!"

    stop music
    play music "<from 3.0 to 54.0>gorengan.mp3" fadein 1.0 volume 0.03 loop

    scene bg gorengan with dissolve
    show seller with dissolve
    
    joko "Punten kang, boleh tanya gak?"
    seller "Wah ada apa ya Joko?"
    seller "Makanan saya bersih loh!"

    joko "Bukan itu kang, bungkus gorengan yang kang pake biasanya dari mana ya?"
    seller "Oalah kirain, itu mah dari belakang noh"
    seller "biasa dikasih banyak sekaligus kertasnya"

    "Kang Gorengan menunjuk ke belakang, di mana terdapat sebuah gedung perusahaan"

    joko "Oh oke, makasih kang."

    "Hmmmmm, satu-satunya cara untuk dapat lebih banyak info adalah masuk ke sana."

    ## INFILTRASI

    stop music fadeout 2.0

    scene bg cari jalan with dissolve

    pause(1)

    scene bg kota with dissolve

    "Hmmm, aku harus mencari jalur yang aman untuk infiltrasi gedung ini..."
    "Lewat mana yak?"

    # scene bg pintujendela

    scene bg pintujendela with dissolve

    "AHA! Itu dia, hmm aku bisa masuk dari jendela atau dari pintu ini..."
    menu:
        "Sebaiknya lewat mana?"
        "Masuk melewati pintu":
            $ pintu = True
            play music "pintu.mp3"
            jump choicemasuk_pintu
        "Masuk melewati jendela":
            jump choicemasuk_jendela
    
label choicemasuk_pintu:
    scene bg koridor with dissolve

    "Hmmm, sebuah koridor yang lumayan panjang.."
    "Untungnya sepi sih."

    scene bg koridorfootstep with dissolve
    play music "langkahkaki.mp3"
    "Waduh, ada langkah kaki"
    "Aku harus sembunyi!"

    menu:
        "Masuk ke pintu ruangan janitor":
            play music "pintu.mp3"
            stop music
            jump choicepintu_janitor
        "Masuk ke pintu ruangan tanpa tulisan":
            play music "pintu.mp3"
            stop music
            jump choicepintu_nameless
    
    label choicepintu_janitor:
        scene bg blackout with dissolve
        "Phew, harusnya sudah aman."
        "Hmm, aku mendengar seseorang."

        unk "Pak untuk transaksinya nanti di ruangan saya yang di lantai 14"
        unk "Baik pak, saya akan segera ke sana setelah telepon ini"

        "Transaksi? Mungkinkah ada kaitannya?"
        "Tapi sebelum itu aku harus mencari cara untuk keliling gedung ini dengan aman"
        "Cepatlah pergi!!"

        play sound "langkahkaki.mp3"
        "Oke, dia sudah pergi"
        "Hmmm, mana saklarnya?"

        play sound "lampu.mp3"
        stop music

        scene bg janitor with dissolve
        "Hehe, aku mempunyai ide cemerlang!"

        jump pintuconvergent

    label choicepintu_nameless:
        scene bg blackout with dissolve
        "Phew, untung aman-aman aja."
        "Hmm, aku mendengar seseorang."

        play sound "telepon.mp3"

        unk "Pak untuk transaksinya nanti di ruangan saya yang di lantai 14"
        unk "Baik pak, saya akan segera ke sana setelah telepon ini"

        "Transaksi? Mungkinkah ada kaitannya?"
        "Tapi sebelum itu aku harus mencari cara untuk keliling gedung ini dengan aman"
        "Cepatlah pergi!!"

        play sound "langkahkaki.mp3"
        "Oke, dia sudah pergi"
        "Hmmm, mana saklarnya?"

        play sound "lampu.mp3"

        scene bg kantor with dissolve
        "Hehe, aku mempunyai ide bagus!"

        jump pintuconvergent
    
    label pintuconvergent:
        scene bg lift with dissolve
        "Wah ada lift, hoki"
        
        scene bg tombollift with dissolve
        "Tadi apa katanya? Lantai 14 ya.."

        play sound "lift.mp3"
        scene bg lift14 with dissolve
        "Oke.."

        scene bg lantai14 with dissolve
        "Oke, sekarang yang mana ruangannya?"

        scene bg pintu ceo with dissolve    
        "Ruang CEO? Sepertinya penting."

        scene bg ruangceo with dissolve
        "Aku harus mencari cara untuk menangkap pembicaraan mereka nanti"

        menu:
            "Sembunyi di ventilasi":
                jump choicehide_ventilasi
            "Sembunyi di ruangan sebelah":
                jump choicehide_alternate

        label choicehide_ventilasi:
            scene bg ventilasi with dissolve
            "Nah, aku bisa menyelipkan HPku di sini dan merekam video!"


            "Mmhmm, susah juga.."
            scene bg ventilasihp with dissolve
            
            "Nah oke, sekarang sudah pas."

            scene bg ruangceo
            "Sekarang aku harus sembunyi."
            "Wah, ukuran lemari itu pas sekali"

            scene bg blackout with dissolve
            "Gelap banget..."
            
            play sound "pintu.mp3"

            show ceo-ngeroko_cropped at right with dissolve
            show bapa-senyum biasa_cropped at left with dissolve

            ceo "Silahkan masuk pak, silahkan duduk dulu."
            unk "Terima kasih pak"
            ceo "Jadi bagaimana persetujuan kita? Jadikah?"
            unk "Ohh tentu pak, sudah disetujui oleh pak ketua selama bapak memenuhi bagian persetujuan bapak juga."

            hide ceo-ngeroko_cropped
            show ceo-sombong_cropped at right
            with dissolve

            ceo "Ohh iya aman dong, nah sekarang pertanyaannya, siapa yang jadi korbannya?"
            unk "Aman saja, itu bisa kita atur pak"
            
            hide bapa-senyum biasa_cropped
            hide ceo-sombong_cropped 
            show ceo-ketawa sinis_cropped at right
            show bapa-senyum ketawa_cropped at left
            ceo "Hahahaha, baik pak, atur saja!"

            play music "tegang.mp3"
            "Wah, sepertinya aku menemukan sesuatu yang penting!"
            "Aku harus menunggu sampai mereka pergi."

            scene bg cari jalan with dissolve

            pause(1)

            scene bg ruangceo with dissolve
            "Oke mereka sudah pergi, aku harus mengambil handphoneku"

            scene bg ventilasihp with dissolve
            "Oke ayo kita cek"

            scene bg hpgelap with dissolve
            "Wah gelap doang.."
            "Tak apa-apa, setidaknya ada suara mereka."

            # END ACT 1 BAD CLUE
            $ badclue1 = True
            jump bridging_2

        label choicehide_alternate:
            scene bg jendelakorden with dissolve
            "Nah dari sini sepertinya bisa ngerekam semuanya."

            scene bg ruangkosong with dissolve

            "Oke belum ada orang, aku harus mencari tempat yang bisa melihat ruangan sebelah."

            scene bg liatruangsebelah with dissolve
            "Dari sini sepertinya bisa.."


            "Nice, kelihatan semuanya. Sekarang tinggal menunggu mereka datang."
            play sound "langkahkaki.mp3"
            "Nah itu pasti mereka, mana handphoneku.."
            scene bg rekamceo with dissolve

            show ceo-ngeroko_cropped at rightcenter with dissolve
            show bapa-senyum biasa_cropped at left with dissolve

            ceo "Silahkan masuk pak, silahkan duduk dulu."
            unk "Terima kasih pak"
            ceo "Jadi bagaimana persetujuan kita? Jadikah?"
            unk "Ohh tentu pak, sudah disetujui oleh pak ketua selama bapak memenuhi bagian persetujuan bapak juga."

            hide ceo-ngeroko_cropped
            show ceo-sombong_cropped at rightcenter
            with dissolve

            ceo "Ohh iya aman dong, nah sekarang pertanyaannya, siapa yang jadi korbannya?"
            unk "Aman saja, itu bisa kita atur pak"
            
            hide bapa-senyum biasa_cropped
            hide ceo-sombong_cropped 
            show ceo-ketawa sinis_cropped at rightcenter
            show bapa-senyum ketawa_cropped at left
            ceo "Hahahaha, baik pak, atur saja!"

            play music "tegang.mp3"

            "Wah, sepertinya aku menemukan sesuatu yang penting!"
            "Aku harus menunggu sampai mereka pergi dan segera pergi dari sini."

            # END ACT 1 GOOD CLUE
            $ goodclue1 = True
            jump bridging_2
            
return

label choicemasuk_jendela:
    play sound "Manjat.mp3"
    scene bg emptyroom with dissolve

    "Ah, untungnya sebuah ruangan kosong, tapi aku harus segera keluar!"

    play sound "langkahkaki.mp3"

    "WADUH AKU HARUS CARI TEMPAT SEMBUNYI!"

    menu:
        "Sembunyi di bawah meja":
            jump choicehide_meja
        "Sembunyi di belakang papan":
            jump choicehide_papan
    
    label choicehide_meja:
        scene bg meja with dissolve
        "Aduduh, kepalaku kejedot.."
        "Hmm, aku mendengar seseorang.."

        unk "Jadi bagaimana pak? Apakah kita jadi ketemu?"
        unk "Ohh, baik pak. Lantai 14 kan ruangan bapak?"
        unk "Saya segera ke sana."
        jump jendelaconvergent

    label choicehide_papan:
        scene bg papan with dissolve
        "Aduduh, tanganku kegores.."
        "Hmm, aku mendengar seseorang.."

        unk "Jadi bagaimana pak? Apakah kita jadi ketemu?"
        unk "Ohh, baik pak. Lantai 14 kan ruangan bapak?"
        unk "Saya segera ke sana."
        jump jendelaconvergent

    label jendelaconvergent:
        "Sepertinya aku baru saja mendengar hal penting."
        "Transaksi? Lantai 14??"
        "Baik, aku harus segera ke sana!"

        scene bg emptyroom with dissolve
        "Oke, ayo keluar dari ruangan ini."
    
        scene bg koridor with dissolve
        "Hmm, bagaimana aku ke lantai 14?"

        play sound "lift.mp3"
        scene bg lift with dissolve
        "Aha itu dia"
        "Aku bisa menggunakan ini untuk ke lantai 14!"

        scene bg liftkeycard with dissolve
        "Hmmm, butuh keycard.."

        show lift_chillguy with dissolve
        chg "Permisi yaa.."

        joko "Oh iya, maaf ya."

        show bg liftvip with dissolve
        joko "Oh iya pak, boleh pencet untuk lantai 14 tidak ya?"
        chg "Ohh boleh.. boleh.."

        "Wah, aku beruntung!"

        scene bg lantai14 with dissolve
        "Hmm oke, sekarang aku harus mencari ruangan yang dapat melihat transaksi itu."

        scene bg bukapintu with dissolve

        "Sepertinya terkunci..."

        scene bg lantai14 with dissolve
        "Ah semua ruangan di sini terkunci, bagaimana ya?"

        scene bg ventilasilagi with dissolve
        "Hmm, bisa di sana."

        scene bg bukaventilasi with dissolve
        "Oke, memang bisa ternyata."
        "Aku akan lewat sini."

        scene bg dalemventilasi with dissolve
        "Berdebu sekali di sini.."
        scene bg ventilasikotor with dissolve
        "Apa gak pernah mereka bersihin?"
        "Okee, sekarang waktunya menunggu mereka naik ke lantai 14."

        scene bg cari jalan with dissolve

        pause(1)

        scene bg koridor with dissolve
        "Nah itu mereka, sekarang aku harus cari tahu transaksinya di ruangan mana."

        scene bg persimpangan ventilasi with dissolve
        "Sial, sebuah persimpangan. Aku harus lewat mana?"

        menu:
            "Sebaiknya lewat mana?"
            "Jalur kanan":
                $ kanan = True
                jump choicevent_kanan
            "Jalur kiri":
                jump choicevent_kiri

        label choicevent_kanan:
            scene bg ventilasikanan with dissolve
            play sound "langkahkaki.mp3"
            "Suaranya membesar..."
            "Sepertinya aku di jalur yang tepat."

            scene bg ruangceovent with dissolve
            "Aku pas di atas mereka!"
            "Aku harus merekam ini."

            scene bg rekamceovent with dissolve
            "Aduh gelap banget... gak keliatan apa-apa di kamera."
            "Suaranya masih terdengar sih."
            "Yasudahlah tidak apa-apa."
            
            scene bg ruangceo with dissolve
            show ceo-ngeroko_cropped at rightcenter with dissolve
            show bapa-senyum biasa_cropped at left with dissolve

            ceo "Silahkan masuk pak, silahkan duduk dulu."
            unk "Terima kasih pak"
            ceo "Jadi bagaimana persetujuan kita? Jadikah?"
            unk "Ohh tentu pak, sudah disetujui oleh pak ketua selama bapak memenuhi bagian persetujuan bapak juga."

            hide ceo-ngeroko_cropped
            show ceo-sombong_cropped at rightcenter
            with dissolve

            ceo "Ohh iya aman dong, nah sekarang pertanyaannya, siapa yang jadi korbannya?"
            unk "Aman saja, itu bisa kita atur pak"
            
            hide bapa-senyum biasa_cropped
            hide ceo-sombong_cropped 
            show ceo-ketawa sinis_cropped at rightcenter
            show bapa-senyum ketawa_cropped at left
            ceo "Hahahaha, baik pak, atur saja!"
            
            scene bg ruangceovent with dissolve
            play music "tegang.mp3"
            "Wah, sepertinya aku menemukan sesuatu yang penting!"
            "Aku harus menunggu sampai mereka pergi dan segera pergi dari sini."

            # END ACT 1 (BAD CLUE)
            $ badclue2 = True
            jump bridging_2

        label choicevent_kiri:
            scene bg ventjauh with dissolve
            play sound "langkahkaki.mp3" volume 0.2
            "Ah, suaranya makin menjauh."
            "Aku tidak punya pilihan, aku harus turun dari sini!"
            scene bg ventturun with dissolve
            "Sepertinya aku bisa keluar lewat sini.."

            play sound "Manjat.mp3"

            scene bg blackout with dissolve
            "Sepertinya ruangan kosong, tapi gelap sekali...."

            unk "Suara apa itu?"
            ceo "Mungkin hanya barang terjatuh?"

            "Hmm, ini saklarnya.."

            play sound "lampu.mp3"

            scene bg ruangkosong with dissolve

            "Hampir saja aku ketahuan.."
            scene bg liatruangsebelah with dissolve
            "Hmm, aku bisa melihat ruangan samping dari jendela ini!"

            scene bg ruangceo with dissolve
            "Aku harus merekam ini..."

            scene bg rekamceo with dissolve

            play sound "bisik.mp3"
            play sound "pintu.mp3"

            show ceo-ngeroko_cropped at rightcenter with dissolve
            show bapa-senyum biasa_cropped at left with dissolve

            ceo "Silahkan masuk pak, silahkan duduk dulu."
            unk "Terima kasih pak"
            ceo "Jadi bagaimana persetujuan kita? Jadikah?"
            unk "Ohh tentu pak, sudah disetujui oleh pak ketua selama bapak memenuhi bagian persetujuan bapak juga."

            hide ceo-ngeroko_cropped
            show ceo-sombong_cropped at rightcenter
            with dissolve

            ceo "Ohh iya aman dong, nah sekarang pertanyaannya, siapa yang jadi korbannya?"
            unk "Aman saja, itu bisa kita atur pak"
            
            hide bapa-senyum biasa_cropped
            hide ceo-sombong_cropped 
            show ceo-ketawa sinis_cropped at rightcenter
            show bapa-senyum ketawa_cropped at left
            ceo "Hahahaha, baik pak, atur saja!"

            play music "tegang.mp3"

            "Wah, sepertinya aku menemukan sesuatu yang penting!"
            "Aku harus segera melaporkan ini!"

            # END ACT 1 (GOOD CLUE)
            $ goodclue2 = True
            jump bridging_2

    return

label bridging_2:
    stop music

    play music "tegang.mp3" loop volume 0.7 fadein 1.0
    scene bg hallway_fexit with dissolve

    "Aku harus menemukan pintu keluar secepat mungkin, jangan sampai terlihat siapapun!"
    "Wah ada pintu darurat, coba lewat situ deh"

    scene bg fexit with dissolve    
    "Loh, ini kan emergency exit, kenapa pintunya bisa terkunci?"
    "Emang ada yang gak beres sama nih perusahaan."

    play sound "<from 5 to 8>langkahkaki.mp3"
    
    scene bg black with fade
    "WADUH ADA ORANG GIMANA NIH!!!"
    scene bg hallway_fexit with dissolve
    show akuntan with Dissolve(0.5)
    joko "Uhh… selamat siang pak… ada yang bisa saya bantu…?"
    akuntan "Sudah… tidak usah basa-basi"

    scene bg fexit with dissolve
    scene bg fexit_open with dissolve
    akuntan "Ayo keluar, Tadi kamu mau jalan keluar bukan?"
    joko "Uhh...."
    akuntan "Gak usah takut, saya tau tadi kamu ngapain."
    akuntan "Supaya lebih santai, kita obrolin sambil makan ya."
    joko "O-oke...."

    scene bg kedai_taichan with dissolve
    stop music fadeout 1.0
    play music "rame.mp3" loop volume 0.8

    show akuntan at left with dissolve
    joko "Uhh... ku boleh bertanya?"
    
    akuntan "Boleh dong!"
    
    joko "Apa hubungan paman dengan kantor tadi?"
    
    akuntan "Aku adalah seorang akuntan di perusahaan itu."
    akuntan "Aku baru masuk beberapa bulan yang lalu"

    joko "Aku yakin paman sadar bahwa aku bukanlah karyawan di perusahaan itu."
    joko "Gerak-gerik ku juga sudah cukup mencurigakan. Jadi, mengapa paman menolongku?"
    
    akuntan "Ya, semua yang kamu katakan benar. Aku melihatmu saat kamu berada di lorong."
    akuntan "Aku juga melihatmu memata-matai CEO perusahaan. Alasan aku menolongmu karena ingin tahu apa tujuanmu."
    akuntan "Kalau aku laporkan kejadian ini ke pihak keamanan, pasti akan jauh lebih rumit."
    akuntan "Jadi, Apa tujuan mu melakukan semua ini?"

    joko "Aku sebenarnya ingin memecahkan sebuah kasus."
    
    akuntan "Kasus?"
    
    joko "Iya paman, Ini tentang kemungkinan terjadinya penggelapan pajak yang dilakukan seseorang. Aku yakin bahwa CEO perusahaan itu terlibat."
    
    akuntan "Hmm... Apakah pengalaman saya ini berhubungan dengan kasusmu?"
    
    joko "Maksud paman?"

    akuntan "Sebagai akuntan perusahaan, tentunya saya memiliki informasi keuangan perusahaan."
    akuntan "Saya sempat melakukan audit terhadap pendapatan perusahaan. Dalam audit itu, saya menyadari ada kejanggalan tentang aliran dana yang diterima perusahaan."
    akuntan 'Ketika saya tanyakan kejanggalan ini kepada atasan saya, Beliau hanya mengatakan "Sudah, lakukan saja tugasmu. Anak baru sepertimu tidak usah banyak tanya". ' 

    joko 'Wah, ini memperkuat asumsi awalku bahwa benar-benar terjadi penggelapan pajak.'
    joko 'Bagaimana orang-orang itu bisa sangat tega ya? Menggunakan pajak dari rakyat kecil untuk kepentingan pribadinya!'

    akuntan 'Ya begitulah orang-orang dengan kuasa. Untung saya sudah lama tidak bayar pajak, Haha.'

    joko 'HAH?!? Bagaimana paman bisa merasa bangga setelah menghindari pajak. Itu kan melanggar hukum!'

    akuntan 'Kamu terlalu naif jika hanya mengambil sudut pandang tersebut. Kamu sudah lihat secara langsung bahwa terjadi penggelapan pajak.'
    akuntan 'Untuk apa aku membayar pajak jika dananya hanya akan disalahgunakan oleh orang-orang seperti mereka.'

    joko 'Ya.. jika dilihat dari sudut pandang itu, aku cukup paham apa yang paman maksud.'

    akuntan 'Andai saja orang-orang seperti mereka bisa mendapatkan ganjaran untuk perbuatan mereka...'

    joko 'AKU PUNYA IDE !'
    joko 'Bagaimana jika paman membantuku untuk membongkar kasus ini, supaya publik bisa tahu.'
    joko 'Tapi, kalau kita berhasil, paman harus berjanji untuk membayar pajak sesuai tanggungan paman!'

    akuntan 'Wah ide bagus. Jika birokrasi kita bersih dan terpercaya, saya tidak akan merasa tertipu saat membayar pajak!'

    joko 'Baiklah, ayo ikuti aku paman! Kita akan bertemu dengan temanku.'
    joko'Dia sudah sering membantuku memecahkan kasus-kasus seperti ini.'
    stop music fadeout 1.0
    scene bg black with fade
    joko 'Halo Amanda, aku datang bersama akuntan bernama Santoso, dia akan membantu kita menyelesaikan kasus ini....'

    scene bg basement with dissolve
    play music "rippleair.mp3" volume 0.8
    show akuntan at left
    show amanda-senyum at right 
    with dissolve
    amanda 'Halo Joko dan pak Santoso. Aku dengar kalian mendapatkan clue baru?'
    joko"Iya, aku berhasil 'menyelinap' ke dalam kantor dan mendapatkan sesuatu yang menarik. Coba lihat ini."

    if goodclue1 or goodclue2:
        scene bg table_goodclue with dissolve
        play sound "<from 2.5 to 3>doorslam.mp3"
        joko "Ini adalah rekaman video percakapan antara CEO dan seseorang yang tidak dikenal."
        amanda "Hmm.... Aku juga tidak mengenalnya..."
        amanda "Akan tetapi dari percakapannya, aku juga tidak mengerti tentang pengorbanan yang mereka maksud itu."
        joko "Hmm baiklah, mungkin jika kita tahu identitas orang itu, kita akan mendapatkan pentunjuk baru tentang kasus ini."
        joko "Tapi, kira-kira bagaimana yah caranya..."
        jump converge_bridge
    if badclue1 or badclue2:
        scene bg table_badclue with dissolve
        play sound "<from 2.5 to 3>doorslam.mp3"
        joko "Ini adalah rekaman video percakapan antara CEO dan seseorang yang tidak dikenal.Visualnya buruk, tetapi aku rasa dapat didengar dengan cukup jelas."
        amanda "Hmm.... Aku seperti mengenal suaranya..."
        joko "Benarkah?"
        amanda "Yaa, tapi sepertinya hanya perasaanku saja. Dari mana kamu dapat rekaman ini?"
        scene bg basement with dissolve
        show akuntan at left
        show amanda-senyum at right
        menu:
            "Kasih nama perusahaannya":
                jump choicevent_namaperusahaan
            "Kasih nama distrik bisnisnya":
                jump choicevent_disbis
        label choicevent_namaperusahaan:
            joko "Rekaman ini diambil di gedung PT.{b}Metecom{/b}."
            joko "Kamu tahu sesuatu tentang perusahaan itu?"
            amanda "Ngak juga sih.."
            amanda "Oke kembali ke topik rekamannnya."
            amanda "Berdasarkan percakapannya, akan  ada suatu transaksi yang akan terjadi yang akan menjadikan suatu pihak ketiga sebagai korbannya."
            joko "Terdengar familiar bukan?"
            amanda "Iya, sepertinya kasus penggelapan pajak beberapa waktu yang lalu."
            amanda "Jika ini mengikuti modus yang sama, artinya akan ada orang yang disalahkan dengan tuduhan penggelapan pajak"
            amanda "Sedangkan, pelaku aslinya akan aman dari jeratan hukum."

            joko "Aku juga memikirkan hal yang sama."
            joko "Aku jadi semakin yakin bahwa ini adalah modus yang sama."
            joko "Menurutku, yang harus kita lakukan sekarang adalah mencari tahu identitas pria itu."
            joko "Tetapi aku bingung cara mendapatkannya..."

            jump converge_bridge
        

        label choicevent_disbis:
            joko "Rekaman ini diambil di suatu perusahaan dari distrik X."
            amanda "Baiklah kembali ke topik rekamannnya."
            amanda "Berdasarkan percakapannya, akan  ada suatu transaksi yang akan terjadi yang akan menjadikan suatu pihak ketiga sebagai korbannya."
            joko "Terdengar familiar bukan?"
            amanda "Iya, sepertinya kasus penggelapan pajak beberapa waktu yang lalu."
            amanda "Jika ini mengikuti modus yang sama, artinya akan ada orang yang disalahkan dengan tuduhan penggelapan pajak"
            amanda "Sedangkan, pelaku aslinya akan aman dari jeratan hukum."

            joko "Aku juga memikirkan hal yang sama."
            joko "Aku jadi semakin yakin bahwa ini adalah modus yang sama."
            joko "Menurutku, yang harus kita lakukan sekarang adalah mencari tahu identitas pria itu."
            joko "Tetapi aku bingung cara mendapatkannya..."

            jump converge_bridge




label converge_bridge:

    akuntan "Saya rasa ada suatu cara."
    akuntan "Setiap orang yang masuk ke area kantor umumnya memiliki kartu registrasi."
    akuntan "Setiap seseorang masuk atau keluar kantor, kartu itu harus di-tap ke perangkat logger."
    akuntan "Logger itu akan mencatat data diri pengguna kartu untuk disimpan di database perusahaan."

    amanda "Akan tetapi, apakah ia pasti masuk dengan kartu registrasi?"

    joko "Mengingat bahwa pria tersebut mengenal CEO dan tidak pernah sekalipun menunjukan gerak-gerik bahwa ia sedang menyelinap atau bingung,"
    joko "Kemungkinan besar ia sudah pernah datang ke kantor itu sebelumnya"
    joko "Berdasarkan deduksiku, besar kemungkinan ia memiliki kartu registrasi."
    scene bg table_clueall with dissolve
    amanda "Aku rasa kamu benar."
    amanda "Namun, aku yakin database perusahaan hanya bisa diakses melalui server perusahaan."
    amanda "Terlebih lagi, pasti hanya beberapa orang memiliki akses untuk data tersebut."
    amanda "Bagaimana kita mengaksesnya?"

    akuntan "Aku tahu lokasi fisik dari datacenter itu."
    akuntan "Akan tetapi, aku tidak memiliki akses untuk database itu."

    joko "Tenang saja, itu saja sudah lebih dari cukup."
    joko "Aku pernah belajar mengenai keamanan siber sehingga aku akan mencoba membobol databasenya."

    amanda "Kamu tahu tidak akan semudah itu kan...?"

    joko"Tenang saja, perusahaan itu memiliki emergency exit yang terkunci."
    joko "Dengan implementasi keamanan dan keselamatan yang sepayah itu, aku yakin keamanan siber mereka juga sama payahnya."
    joko "Ayo pergi paman, kita harus bersiap-siap."
    joko "Penyelinapan  yang kedua ini akan dilakukan esok hari, pukul 5 sore."

    amanda "Tunggu, apa aku boleh ikut, aku juga penasaran..."
    joko "Sebaiknya tidak, karena ini penyelinapan. Jika terlalu banyak orang, peluang kita tertangkap akan semakin besar."
    amanda "Huft.... Baiklah..."

    stop music fadeout 2.0
    
    scene bg black with Dissolve(2.0)
    play sound "type.mp3" volume 0.8

    centered "{color=#ffffff}{size=60}{cps=2}ACT II"
    stop sound
    jump act2

label act2:
    #kantor depan
    play music "tegang.mp3" volume 0.7 fadein 1.0
    scene bg officefront with dissolve
    play sound "langkahkaki.mp3"
    pause(0.5)
    show akuntan at center with dissolve
    pause(0.1)
    stop sound
    akuntan "Baik kita akan menuju kantor saya dulu untuk menentukan rencana berikutnya"
    joko"Baik akan aku ikutin paman"
    play sound "pintu.mp3"
    scene bg officetables with dissolve
    show akuntan with dissolve
    
    akuntan "Oke aku mengetahui lokasi databasenya berada di lantai 13, tetapi aku yakin kita perlu akses khusus untuk mengakses databasenya. "
    akuntan "Apakah kamu yakin kamu bisa membobol database tersebut ? "

    joko "Saya cukup yakin paman, tetapi mungkin saya memerlukan bantuan bapak sedikit,"
    joko "Saya kepikiran mungkin kita bisa menemukan clue lain dari database itu seperti bukti-bukti lainnya"
    akuntan "Baiklah saya mungkin bisa mencoba melihat database yang ada keanehan dan tidak sesuai dengan pekerjaan perusahaan ini."
    #elevator
    scene bg elevator1 with dissolve
    pause(0.2)
    scene bg elevator2 with dissolve
    pause (0.2)
    scene bg elevatorfinal with dissolve
    pause (0.2)
    play sound "lift.mp3" volume 0.7
    scene bg elevatorinside with dissolve
    pause(0.2)
    scene bg elevatorpressed
    akuntan "Baik setelah pintu ini terbuka, ruang database akan berada di koridor sebelah kiri kita, berjarak 3 pintu dari elevator ini.. "
    akuntan "Kita harus bersiap, pastikan tidak ada yang mencurigai kita"
    scene bg elevatoropened with dissolve
    pause(0.2)
    scene bg hallwaysillhouette with dissolve
    joko "Hah tidak mungkin.. itu bukannya.."
    show akuntan at center
    akuntan "Iya itu bapak ceo perusahaan ini.. ah kenapa dia ada disini sekarang"
    joko "Aku ada ide.. bagaimana jika.."
    menu:
        "Suruh akuntan membuat distraksi":
            jump choiceevent_distract
        "Suruh akuntan memanggil CEO keluar":
            jump choiceevent_callout
    label choiceevent_distract:
        play sound "bisik.mp3"
        joko "Bagaimana jika paman membuat distraksi dan kemudian saya masuk kedalam ruangan database dan mengambil datanya secepat mungkin?"
        akuntan "Hmm mungkin itu bisa berhasil.. "
        akuntan "Aku akan mencoba untuk menyalakan alarm apinya dan setelah CEO tersebut keluar dari ruangan database kau harus langsung masuk kedalam."
        joko "Baik kita bisa mencoba itu"
        scene bg falarmhallway with dissolve
        show akuntan with dissolve
        pause(1)
        scene bg database
        "Sekarang tinggal kita tunggu sampai...."
        play music "alarm.mp3" volume 0.5
        "Nah, itu dia.. sekarang dia akan..."
        show ceo-sombong with dissolve
        ceo "?!?!"
        
        joko "PAK KEBAKARAN PAK CEPAT KELUARRRRRR!!!!"
        show ceo-sombong at right with dissolve
        hide ceo-sombong with fade
        "Hm.. cepat juga dia lari."
        "Baiklah, waktunya beraksi!"
        scene bg serverroom with dissolve
        stop music fadeout 0.7
        play sound "typing.mp3" loop volume 0.8
        "Oke, mari kita mulai..."
        "Database registrasi..."
        "Database akuntan.."
        "Nah ini dia database akses.. "
        "Mari kita lihat...Hmmm akses dalam beberapa hari lalu"
        "Akses pihak luar.. oke mari kita download ini!"
        stop sound
        scene bg black
        play sound "pintu.mp3"
        "!!!"
        scene bg serverroom
        show akuntan at right with dissolve
        joko "Yaampun paman jangan kagetin saya begitu dong."
        akuntan"Maaf, tadi saya harus menunggu lantai ini tidak ada orang dulu baru saya bisa kesini. "
        akuntan "Apakah kamu sudah menemukannya?"
        joko "Sudah, coba paman lihat ini."
        akuntan"Baik data akses, baguslah kita bisa menggunakan itu..  "
        akuntan "Bentarrrr… coba buka itu data keuangan"
        joko "Data keuangan.. bukannya paman seharusnya punya akses database ini??"
        akuntan "Tidak bisa melihat semua filenya karena memerlukan akses database internal"
        joko "Baiklah.. mari kita lihat..."
        hide akuntan
        show akuntan-shock at right
        with dissolve
        joko "Ini.. ternyata semuanya benar.."
        akuntan"Aku tidak percaya ini… "
        akuntan "Ini semua data pajak kota ini, lengkap ada nama dari siapa yang membayar dan kapan… Semua uang tersebut disalurkan kesini.."
        joko "Kita harus mengambil data ini…"
        akuntan "Sepertinya itu sudah cukup, mari kita lari dari sini!"
        $ goodclueact2 =True
        jump act2_converge_final
    
    label choiceevent_callout:
        play sound "bisik.mp3"
        joko "Bagaimana jika paman mencoba untuk mendistraksi CEO dan selama paman mendistraksi dia saya akan mencoba untuk menyelinap masuk dan mengambil datanya."
        akuntan "Hmmm baiklah mungkin itu bisa berhasil, tapi saya tidak bisa menjanjikan saya bisa mendistraksinya dengan lama"
        joko "Tidak apa-apa pak, saya akan mencoba untuk dengan cepat mengambil datanya"
        scene bg black with Dissolve(1.0)

        centered "{color=#ffffff}{size=40}AKUNTAN POV"
        scene bg database
        play sound "ketuk.mp3" volume 0.5 #Belum ada
        pause(2.0)
        play sound "pintu.mp3" 
        pause(3.0)

        show ceo-sombong with dissolve
        akuntan "Permisi Pak.. saya sudah menyiapkan laporan keuangan bulan ini, apakah bapak ingin melihatnya sekarang ? "
        hide ceo-sombong
        show ceo-ketawasinis
        ceo "Ah laporan keuangan ya, tumben juga cepat.. baiklah mari kita lihat bentar."
        akuntan "Baik pak, saya sudah menyiapkannya di kantor saya pak. Kita bisa turun dulu kesana untuk melihatnya"
        ceo "Baiklah kalau begitu.."
        scene bg black
        "Semua ada di tangan mu, Joko!"
        centered "{color=#ffffff}{size=40}JOKO POV"
        scene bg database with dissolve
        "Mereka sudah pergi..."
        scene bg serverroom with dissolve
        play sound "typing.mp3"
        "Oke... Hmmmm..."
        "Oke, mari kita mulai..."
        "Database registrasi..."
        "Database akuntan.."
        "Nah ini dia database akses.. "
        "Mari kita lihat...Hmmm akses dalam beberapa hari lalu"
        "Akses pihak luar.. oke mari kita download ini!"
        stop sound
        scene bg black
        play sound "pintu.mp3"
        "!!!"
        ceo "Ah bisa-bisanya akuntan itu kehilangan laporannya.."
        ceo "?!??"
        ceo "Hmm apakah aku tadi hanya membayangkan ada seseorang disini?"
        scene bg serverroom with dissolve
        play sound "manjat.mp3"
        ceo "Ah aku pasti stress karena akuntan tadi.."
        $ badclueact2 =True
        jump act2_converge_final

label act2_converge_final:
    scene bg database with fade
    if badclueact2:
        "Phew...."
        akuntan "Kamu sudah dapatkan datanya kan? Ayo CEPAT!"
        joko "Kita harus segera laporkan ini!"
    play sound "fastrun.mp3"
    scene bg elevatorfinal with dissolve
    "Itu dia elevatornya!!"
    scene bg black
    amanda "BERHENTIIII!!!!!!!!!!!!!!!!"
    jump bridge_ending

label bridge_ending:
    scene bg elevatorfinal
    play music "tegang.mp3" volume 0.7 fadein 1.0
    show akuntan at left
    show amanda-shock_cropped at right

    joko "Amanda? Apa yang kamu lakukan di sini?"
    amanda "Itu tidak penting? Yang penting adalah kalian berhenti melakukan hal ini!"
    joko "Apa maksudmu? Bukankah rencana kita sejak awal adalah membongkar kasus ini dan memberitahukan kebenaran kepada dunia?"
    amanda "{cps=3}I-{cps=40}iya{cps=3}..."
    joko "Lihat! Kita sudah mendapatkan informasi mengenai database akses perusahaan. Bahkan, kita juga berhasil mendapatkan data pajak masyara–"
    amanda "{size=+5}CUKUP! Pada rekaman yang kamu berikan{cps=4}...{cps=40} orang yang berbicara dengan CEO{cps=4}...{cps=40} adalah ayahku!{/size}"
    
    hide akuntan
    show akuntan-shock at left
    with Dissolve(0.3)

    joko "{cps=3}B-{cps=20}Bagaimana bisa{cps=3}..."
    akuntan "Tidak ada yang bisa kita lakukan. Kita sudah sampai sejauh ini. Kebenaran harus diungkapkan! Ayo Joko, kita pergi."

    hide akuntan_scream
    show akuntan-shock at left
    show amanda-shock_cropped at right

    amanda "{size=-5}Jika kalian tetap ingin pergi, aku akan menekan alarm security ini karena hampir seluruh satpam sudah pulang, satpam yang tersisa pasti akan menelpon polisi. Kalian akan ditangkap karena masuk ke ruangan database tanpa izin.{/size}"
    
    hide akuntan-shock
    show akuntan at left
    with dissolve

    akuntan "Lakukan sesuka hatimu! Ayo pergi Joko!"
    
    stop music
    play music "alarm.mp3" volume 0.4
    scene bg cctv with dissolve
    
    satpam "Wah siapa itu, berlarian di lorong. Saya tidak pernah melihatnya di sini. PASTI PENYUSUP! Saya harus cepat-cepat telpon polisi!"
    
    play sound "lift.mp3"
    
    scene bg tombollift with dissolve

    pause(1)
    
    scene bg elevatoropened with dissolve

    show polisi_cropped_1 at left
    show polisi_cropped_2 at center
    show polisi_cropped_3 at right
    with Dissolve(0.3)

    polisi "Selamat siang, kami mendapat laporan bahwa ada penyusup di perusahaan ini. Apakah Anda tahu mengenai hal ini?"
    akuntan "Uh{cps=5}..."

    hide polisi_cropped_3
    show ceo-ketawasinis at right
    with dissolve

    ceo "Pemuda itu pak penyusupnya. Satpam bilang ia terlihat berlarian di lorong lantai 13. Lorong itu juga dekat dengan database. Pasti ia mencuri data perusahaan!!!"
    polisi "Apakah benar begitu?"
    joko "{cps=20}Betul, Pak. Tetapi{cps=3}..."
    ceo "Dia sudah mengaku pak cepat borgol dia. jangan sampai dia kabur membawa data perusahaan saya!!!"
    
    stop music
    scene bg officefront
    show akuntan at left
    show polisi_cropped_2 at right
    with dissolve

    joko "Pak polisi, bapak boleh borgol saya. Saya juga tidak akan lari. Akan tetapi, saya harus menunjukkan sesuatu kepada bapak"
    polisi "Baiklah."
    "Joko menunjukkan data-data yang sudah diambil dari database perusahaan."
    "Polisi menganggukan kepalanya dan menghampiri CEO perusahan"

    hide akuntan
    hide polisi_cropped_2
    with dissolve

    show polisi_cropped_2 at left
    show ceo-ketawasinis at right
    with dissolve

    ceo "Bagaimana pak? Benarkah dia mencuri data perusahaan saya?"
    polisi "Ya, benar"
    ceo "Bapak tunggu apa lagi?! Cepat borgol si penjahat itu, Pak!"
    "Polisi memborgol CEO perusahaan"
    
    hide ceo-ketawasinis
    show ceo-sombong at right
    with Dissolve(0.2)

    ceo "Loh!!! Kok saya yang diborgol, pak???"
    polisi "Sudah ikut saya dulu ke kantor!"
    ceo "{size=-4}Penyusupnya dia pak, bukan saya. Kok bapak menangkap saya. Jangan-jangan bapak diberi sesuatu oleh pemuda itu ya? Ternyata kepolisian masih melakukan praktik suap-menyuap ya Pak???{/size}"
    polisi "Enak saja! Itu mah kamu!!!"
    ceo "{size=+10}LOH?!?! ADA APA INI PAK???{/size}"
    polisi "Anda terduga telah melakukan kegiatan penggelapan uang yang melibatkan pajak warga hingga Anda bisa membuktikan Anda tidak bersalah, Anda akan ditahan."
    ceo "Tidak mungkin, apa yang telah dilakukan oleh pemuda itu?!?"

    scene bg blackout with Dissolve(1)
    
    jump ending

label ending:
    play music "type.mp3" loop volume 0.8
    centered "{size=+10}{cps=10}Beberapa hari kemudian{cps=5}..."

    stop music
    play music "tegang.mp3" volume 0.5
    scene bg persidangan with Dissolve(1)

    pause(0.5)

    scene bg hakim 
    show hakim_cropped at center 
    with dissolve

    play sound "hammer.mp3"
    hakim "SIDANG KASUS PENGGELAPAN PAJAK DAN KORUPSI PERUSAHAAN {b}Metecom{/b} DIMULAI"
    hakim "Untuk Joko silahkan berikan bukti yang Anda temukan"

    scene bg ceo
    show ceo-sombong at center
    with dissolve
    
    if ((goodclue1 or goodclue2) and goodclueact2):
        joko "Saya telah menemukan beberapa bukti untuk penggelapan pajak yang telah dilakukan oleh bapak"
        joko "Saya harus mengakui bahwa saya memang melanggar beberapa aturan dengan secara illegal masuk ke gedung perusahaan metecom,"
        joko "tetapi saya rela menerima hukumannya demi memperlihatkan kebenaran tentang kota ini."
        joko "Pertama."

        scene bg goodclue1 with dissolve

        joko "Saya merekam perbincangan antara bapak CEO dengan pria yang merupakan perwakilan dari departemen keuangan yang memegak PAJAK KITA!!!"

        scene bg hakim 
        show hakim_cropped at center 
        with dissolve

        show usb at left

        joko "Saya juga mendapatkan database dengan data yang menunjukkan bahwa pria yang berkaitan tersebut merupakan seseorang dari departemen keuangan"
        joko "dan diluar itu saya mendapatkan bukti lain yang menunjukkan keseluruhan data keuangan dengan fakta asli bahwa perusahaan METECOM berkaitan dengan hilangnya pajak kota ini."

        hide usb

        hakim "Baik, ini merupakan bukti yang sangat kuat.. Kami sudah melakukan penyelidikan lebih lanjut lagi kepada perusahaan Metecom dan juga departemen keuangan dan iya sudah terbukti bahwa bapak melakukan kegiatan penggelapan pajak."

        ceo "TIDAK SAYA MENOLAK ITU!"

        scene bg ceo
        show ceo-sombong at center
        with dissolve

        ceo "SEMUA BUKTI ITU PALSU. SEMUANYA BOHONGAN. ITU DATA PALSU DAN ITU REKAMAN DIBUAT AI!!!"
        hakim "Maaf pak, ini semua merupakan bukti yang sudah terverifikasi dan sayangnya bapak terbukti bersalah."
        hakim "Saya memutuskan untuk Bapak Abdul dimasukkan dalam penjara selama 70 tahun dan untuk bapak Kartono dimasukkan dalam penjara selama 50 tahun. Untuk departemen keuangan akan dilakukan penyelidikan lebih lanjut untuk mencari akar dari permasalahan ini."
        
        play sound "hammer.mp3"

        stop music fadeout 1.0

        scene bg blackout with Dissolve(1)

        scene bg beberapatahun with Dissolve(1)

        pause(2)

        play music "warungsunda.mp3"

        scene bg kota with Dissolve(1)

        joko "Ah kota Bandung{cps=5}..."
        "Setelah kejadian dulu, semuanya berubah, kota bandung ini menjadi lebih baik."
        "Pajak sudah tersalurkan dengan benar dan kita bisa melihat pembangunan kota ini, sudah banyak gedung baru, bahkan ada pusat perbelanjaan baru sekarang bernama London Van Java."
        "Tetapi sudah lama aku tidak mendengar dari Amanda setelah kejadian itu{cps=5}..{cps=40} Semoga dia tidak apa-apa. Tapi sekarang semuanya sudah lebih bagus{cps=4}..."

        scene bg kota with dissolve

        centered "{size=+10}{cps=4}THE END\nGOOD ENDING"

        pause(2)

        jump credit



label credit:
    scene bg blackout with Dissolve(1)
    centered "{cps=150}Project Manager\nWillliam Anthony | 13223048 | Teknik Elektro | @wlmoi"
    centered "{cps=150}Game Designer\nJonathan Otto | 18323017 | Teknik Biomedis | @jonathanotto_\nJoenathan Luther Sihotang | 13223022 | Teknik Elektro | @joe.luther1311"
    centered "{cps=150}Script Writer/Story Developer\nJerry Alexander Tjoa | 18323026 | Teknik Biomedis | @jerrytjoa\nRaehan Fitrozikre | 132230014 | Teknik Elektro | @raehanfz"
    centered "{cps=150}Programmer\nDarren Johan | 13223032 | Teknik Elektro | @darrenjohan_\nMichael Liebing | 18323016 | Teknik Biomedis | @m.liebing\nKenneth Alexander Jims | 13223004 | Teknik Elektro | @kenneth.a.jims"
    centered "{cps=150}Graphic Designer/Illustrator\nTakAsu | @ArtTakasu | https://arttakasu.carrd.co/\nBonaventura Aditya J H P | 18023019 | Teknik Tenaga Listrik | @bona_ajeha.p\nStanislaus Justin Widjaya | 13223098 | Teknik Elektro | @justinwidjaya\nLionel Naythan Liu | 13223088 | Teknik Elektro | @lionel_naythan"
    centered "{cps=150}UI/UX Designer\nVico A C Silalahi | 13223067 | Teknik Elektro | @vicoco.lahi "
    centered "{cps=150}Sound Designer/Composer\neinhard Iven Winata | 13223009 | Teknik Elektro | @ri.winnata"
    centered "{cps=150}Quality Assurance (QA) Tester\nMuhammad Nabil Raihan | 13223014 | Teknik Elektro | @bilrey_19\nAbdul Aziz | 13223023 | Teknik Elektro | @abdaziz_46"
    centered "{cps=150}Publication Specialist\nWillliam Anthony | 13223048 | Teknik Elektro | @wlmoi"
    centered "{cps=60}THANKYOU FOR PLAYING\nOUR GAME\n❤️"
    show title at center with Dissolve(2.0)
    pause(3)
    stop music fadeout 2.0
    hide title
    scene bg blackout
    with Dissolve(2.0)
    return






