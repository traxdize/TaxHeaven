# The script of the game goes in this file.

##regular taps, medium intervals
define soundhard = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

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

    def type_soundhard(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing hard until the text ends
            renpy.sound.play(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            renpy.sound.queue(renpy.random.choice(soundhard))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define joko = Character('Joko', color="#c000fb",callback=type_soundsoft)
define amanda = Character('Amanda Kartikasari', color="#007bff", callback=type_soundsoft)
define seller = Character('Kang Gorengan', color="#ffaa00", callback=type_soundsoft)
define center = Position(xalign=0.5, yalign=0.5)
define left = Position(xalign=0.1, yalign=0.5)
define right = Position(xalign=0.9, yalign=0.5)

label start:
    
    stop music
    play music "type.mp3" loop volume 0.8

    centered "{size=40}{cps=10}SABTU, 19 NOVEMBER 2023\n{cps=5}BANDUNG\n{cps=2}11:40"

    stop music

    play music "street.mp3" volume 0.7 loop

    scene bg kota with dissolve

    joko "Ah, kota Bandung{cps=5}..."
    "Menurutku kota ini bagus, ada banyak tempat indah dan banyak potensi."
    "Lokasinya yang berada di daerah bukit juga membuat kota ini bisa menjadi tempat wisata."
    "Tetapi ada keganjalan, kota ini selalu begini selama 10 tahun terakhir,"
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

    joko "Bang minta tahu gorengnya 5 biji ya"
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

    play sound "<from 2.0 to 6.0>doorslam.mp3"
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
    play music "type.mp3" loop volume 0.8

    centered "{color=#ffffff}{size=60}{cps=2}ACT I"

    stop music

    ## ACT 1

    # show cg bungkus gorengan

    scene bg cek kertas with Dissolve(3.0)
    
    joko "Hmmm, ada yang aneh dengan kertas gorengan ini..."

    "Coba kita lihat, transfer sebesar Rp3.5 miliar kepada perusahaan {b}Metecom{/b} dari ketua departemen keuangan{cps=5}... Kok nominalnya tidak asing ya?"

    "Sepertinya aku harus simpan kertas ini dan menanyakan ini ke Amanda saat di warung nanti."

    ## MASUK WARUNG SUNDA

    scene bg warung sunda
    with dissolve

    show amanda-senyum with Dissolve(1.0)

    joko "Hei Amanda! Lihat yang aku temukan."
    
    amanda "Hah apaan lagi ini?"

    show amanda-ketawa with dissolve

    extend " kamu main detektif-detektifan lagi?"

    show amanda-senyum with dissolve

    joko "Sudahlah, lihat ini saja."
    joko "Kenapa angka Rp3.5 miliar ini tidak asing ya?"

    show amanda-bingung with dissolve

    amanda "Itu bukannya{cps=8}.... sebentar{cps=5}.."
    amanda "Gak mungkin sih{cps=5}..."

    ## LAPTOP SCENE

    scene koran with dissolve

    amanda "Kamu inget gak ini?"
    amanda "Berita tahun lalu yang uang pajak kota kita hilang sebesar Rp3.5 miliar!"

    joko "Tidak mungkin deh, pelakunya udah ditangkep."

    scene bg warung sunda with dissolve

    show amanda-senyum with Dissolve(0.3)
    amanda "Bener, tapi semuanya aneh, masa pelakunya secara sukarela menyerahkan diri?"

    show amanda-bingung with dissolve
    amanda "Sudah gitu, masa uangnya full dipake buat judi online?"
    amanda "Kalaupun benar dia melakukan itu, kenapa dia langsung ngaku dan kenapa uang sebesar itu bisa buat judol doang.."

    joko "Iya sih, kalau dipikir-pikir memang ada yang janggal."
    joko "{size=40}Kecuali, mungkin, dia bukan pelaku sebenarnya!{/size}"

    show amanda-shock with dissolve
    amanda "Bisa jadi dia hanya pion untuk menyembunyikan pelaku sebenarnya!"

    show amanda-bingung with dissolve
    amanda "Kalau begitu apa yang harus kita lakukan?"

    joko "Aku harus segera ke tukang gorengan itu!"
    joko "Aku harus cari tahu dari mana dia dapat kertas itu!"

    scene bg gorengan with dissolve
    show seller with dissolve
    
    joko "Punten bang, boleh tanya gak?"
    seller "Wah ada apa ya Joko?"
    seller "Makanan saya bersih lho!"

    joko "Bukan itu kang, bungkus gorengan yang kang pake biasanya dari mana ya?"
    seller "Oalah kirain, itu mah dari belakang noh"
    seller "biasa dikasih banyak sekaligus kertasnya"

    "Kang Gorengan menunjuk ke belakang, di mana terdapat sebuah gedung perusahaan"

    joko "Oh oke, makasih kang."

    "Hmmmmm, satu-satunya cara untuk dapat lebih banyak info adalah masuk ke sana."

    ## INFILTRASI

    # scene bg cari jalan

    scene bg kota with dissolve ## placeholder

    "Hmmm, aku harus mencari jalur yang aman untuk infiltrasi gedung ini..."
    "Lewat mana yak?"

    # scene bg pintujendela

    scene bg pintujendela with dissolve ## placeholder

    "AHA! Itu dia, hmm aku bisa masuk dari jendela atau dari pintu ini..."
    menu:
        "Sebaiknya lewat mana?"
        "Masuk melewati pintu":
            $ pintu = True
            jump choicemasuk_pintu
        "Masuk melewati jendela":
            jump choicemasuk_jendela
    
label choicemasuk_pintu:
    # scene bg koridor
    scene bg koridor ## placeholder

    "Hmmm, sebuah koridor yang lumayan panjang.."
    "Untungnya sepi sih."

    # play music "footsteps.mp3"
    "Waduh, ada langkah kaki"
    "Aku harus sembunyi!"

    # scene bg tworooms

    menu:
        "Masuk ke pintu ruangan janitor":
            jump choicepintu_janitor
        "Masuk ke pintu ruangan tanpa tulisan":
            jump choicepintu_nameless
    
    label choicepintu_janitor:
        # scene bg blackout
        "Phew, harusnya sudah aman."
        "Hmm, aku mendengar seseorang."

        unk "Pak untuk transaksinya nanti di ruangan saya yang di lantai 14"
        unk "Baik pak, saya akan segera ke sana setelah telepon ini"

        "Transaksi? Mungkinkah ada kaitannya?"
        "Tapi sebelum itu aku harus mencari cara untuk keliling gedung ini dengan aman"
        "Cepatlah pergi!!"

        # play music "footsteps.mp3"
        "Oke, dia sudah pergi"
        "Hmmm, mana saklarnya?"

        # scene bg whiteout
        "Hehe, aku mempunyai ide cemerlang!"

        jump pintuconvergent

    label choicepintu_nameless:
        # scene bg blackout
        "Phew, untung aman-aman aja."
        "Hmm, aku mendengar seseorang."

        unk "Pak untuk transaksinya nanti di ruangan saya yang di lantai 14"
        unk "Baik pak, saya akan segera ke sana setelah telepon ini"

        "Transaksi? Mungkinkah ada kaitannya?"
        "Tapi sebelum itu aku harus mencari cara untuk keliling gedung ini dengan aman"
        "Cepatlah pergi!!"

        # play music "footsteps.mp3"
        "Oke, dia sudah pergi"
        "Hmmm, mana saklarnya?"

        # scene bg kantor
        "Hehe, aku mempunyai ide bagus!"

        jump pintuconvergent
    
    label pintuconvergent:
        # scene bg lift
        "Wah ada lift, hoki"
        
        # scene bg tombollift
        "Tadi apa katanya? Lantai 14 ya.."

        # scene bg koridor
        "Oke, sekarang yang mana ruangannya?"

        # scene bg pintuceo
        "Ruang CEO? Sepertinya penting."

        # scene bg ruangceo
        "Aku harus mencari cara untuk menangkap pembicaraan mereka nanti"

        menu:
            "Sembunyi di ventilasi":
                jump choicehide_ventilasi
            "Sembunyi di ruangan sebelah":
                jump choicehide_alternate

        label choicehide_ventilasi:
            # scene bg ventilasi
            "Nah, aku bisa menyelipkan HPku di sini dan merekam video!"

            # scene bg blackout
            "Mmhmm, susah juga.."
            
            # scene bg ruangceo
            "Nah oke, sekarang sudah pas."
            "Sekarang aku harus sembunyi."
            "Wah, ukuran lemari itu pas sekali"

            # scene bg blackout
            "Gelap banget..."
            
            # play music "suarapintu.mp3"

            show ceo-rokok with dissolve

            ceo "Silahkan masuk pak, silahkan duduk dulu."
            unk "Terima kasih pak"
            ceo "Jadi bagaimana persetujuan kita? Jadikah?"
            unk "Ohh tentu pak, sudah disetujui oleh pak ketua selama bapak memenuhi bagian persetujuan bapak juga."

            hide ceo-rokok
            show ceo-sombong with dissolve
            ceo "Ohh iya aman dong, nah sekarang pertanyaannya, siapa yang jadi korbannya?"
            unk "Aman saja, itu bisa kita atur pak"

            show ceo-ketawa
            ceo "Hahahaha, baik pak, atur saja!"

            "Wah, sepertinya aku menemukan sesuatu yang penting!"
            "Aku harus menunggu sampai mereka pergi."

            # scene bg blackout
            centered "{color=#ffffff}{cps=10}Setelah beberapa menit"

            # scene bg ruangceo
            "Oke mereka sudah pergi, aku harus mengambil handphoneku"
            "Oke ayo kita cek"

            # scene bg blackout
            "Wah gelap doang.."
            "Tak apa-apa, setidaknya ada suara mereka."

            # END ACT 1 BAD CLUE
            $ badclue1 = True
            
    return

    label choicemasuk_jendela:
        # scene bg emptyroom
        scene bg emptyroom ## placeholder

        "Ah, untungnya sebuah ruangan kosong, tapi aku harus segera keluar!"

        # play music "footsteps.mp3"

        "WADUH AKU HARUS CARI TEMPAT SEMBUNYI!"

    return