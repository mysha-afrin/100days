import time

lyrics = '''🎶 Na elo na
Se thake kar vhorasay
E kotha jay
Batashe mishe jay
Se ashe na
Thake na shot bo rone
Dorajay dariye thaka day
Na gelo na
Ar asha rakha gelo na
E byatha jay, andhare she milay
She jane na, mane na kono karone
Janalay dariye thaka day

Jodi biroh thake ami o thaki
Ke bolo shesh hobe age?
Keno je eto bhalobasha more jay
Shudhu shomoy mone rakhe

Eto shunnota e mone rakhi je ami
Dekhe na keu to ar, bole e shob i paglami
Kate na jamini, biroh jeno kete jay
Thame na borosha, tomare daki je ami

Se thake kar vhorasay
E kotha jay
Batashe mishe jay
Se ashe na
Thake na shot bo rone
E dorajay dariye thaka day

Ami eka hoye boshe achi
Birohito moner shukshmo hashi
Ami shudhu cheyechi tomake shuru theke
Jani ashbe na to aj
Oshomapto golpo likhe jai ami-tumi
Tomar bhalobasha ami chaini

Ekhono hoyni rat, akashe koto je tara
Dekho na tumi ar, ami o je dishehara
Ekhane borosha kebol i bhore je ashe
Dake na keu jokhon, thake na tomar i pashe

E ekaki moner sthirata tumi
Tene eno amar gan
Moner gohine shudhu tomar i rup
Batashe jodi dao kan

Eto shunnota e mone rakhi je ami
Dekhe na keu to ar, bole e shob i paglami
Kate na jamini, biroh jeno kete jay
Thame na borosha, tomare daki je ami
Eto shunnota e mone rakhi je ami
Dekhe na keu to ar, bole e shob i paglami
Kate na jamini, biroh jeno kete jay
Thame na borosha, tomare daki je ami
(Ar) 💎'''

# Split by line breaks (\n)
for line in lyrics.splitlines():
    words = line.split()  # Split each line into words
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(0.3)  # Wait 0.3s between words
    print()  # New line after finishing one line
    time.sleep(0.5)  # Small pause between lines