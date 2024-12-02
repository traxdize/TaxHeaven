# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character('Joko', color="#c000fb")
define a = Character('Amanda Kartikasari', color="#eeff00")
define seller = Character('Kang Gorengan', color="#ffffff")
define unk = Character('???')
define ceo = Character('CEO')
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

    j "Bang minta tahu gorengnya 5 biji ya"
    seller "Siapp mas!🫡"

    # show cg bungkus gorengan
    
    j "Hmmm, ada yang aneh dengan kertas gorengan ini..."

    "Coba kita lihat, transfer sebesar Rp3.5 miliar kepada perusahaan (placeholder) dari ketua departemen keuangan. Kok nominalnya tidak asing ya?"

    "Sepertinya aku harus simpan kertas ini dan menanyakan ini ke Amanda."

    ## MASUK WARUNG SUNDA

    scene bg warung sunda
    with dissolve

    "Siang ini aku makan dengan salah satu temanku."

    show amanda with dissolve

    j "Hei lihat yang aku temukan."
    
    a "Hah apaan lagi ini,"

    hide amanda
    show amanda-ketawa with dissolve

    extend " kamu main detektif-detektifan lagi?"

    show amanda-senyum with dissolve

    j "Sudahlah, lihat ini saja."
    j "Kenapa angka Rp3.5 miliar ini tidak asing ya?"

    show amanda-bingung with dissolve

    a "Itu bukannya..... sebentar....."
    a "Gak mungkin sih...."

    ## LAPTOP SCENE

    # scene cg laptop idk

    scene koran with dissolve

    a "Kamu inget gak ini?"
    a "Berita tahun lalu yang uang pajak kota kita hilang sebesar Rp3.5 miliar!"

    j "Tidak mungkin deh, pelakunya udah ditangkep."

    scene bg warung sunda with dissolve

    show amanda-senyum with dissolve
    a "Bener, tapi semuanya aneh, masa pelakunya secara sukarela menyerahkan diri?"

    show amanda-bingung with dissolve
    a "Sudah gitu, masa uangnya full dipake buat judi online?"
    a "Kalaupun benar dia melakukan itu, kenapa dia langsung ngaku dan kenapa uang sebesar itu bisa buat judol doang.."

    j "Iya sih, kalau dipikir-pikir memang ada yang janggal."
    j "{size=40}Kecuali, mungkin, dia bukan pelaku sebenarnya!{/size}"

    show amanda-shock with dissolve
    a "Bisa jadi dia hanya pion untuk menyembunyikan pelaku sebenarnya!"

    show amanda-bingung with dissolve
    a "Kalau begitu apa yang harus kita lakukan?"

    j "Aku harus segera ke tukang gorengan itu!"
    j "Aku harus cari tahu dari mana dia dapat kertas itu!"

    scene bg trotoar with dissolve
    show kang gorengan
    
    j "Punten bang, boleh tanya gak?"
    seller "Wah ada apa ya a?"
    seller "Makanan saya bersih lho!"

    j "Bukan itu kang, bungkus gorengan yang kang pake biasanya dari mana ya?"
    seller "Oalah kirain, itu mah dari belakang noh"
    seller "biasa dikasih banyak sekaligus kertasnya"

    "Kang Gorengan menunjuk ke belakang, di mana terdapat sebuah gedung perusahaan"

    j "Oh oke, makasih kang."

    "Hmmmmm, satu-satunya cara untuk dapat lebih banyak info adalah masuk ke sana."

    ## INFILTRASI

    # scene bg cari jalan

    scene bg kota ## placeholder

    "Hmmm, aku harus mencari jalur yang aman untuk infiltrasi gedung ini..."
    "Lewat mana yak?"

    # scene bg pintujendela

    scene bg pintujendela ## placeholder

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
