star_signs = { #individual star signs saved in dictionaries
    'aquarius':'Aquarius.Aquarius is actually the last air sign of the zodiac. Innovative, progressive, and shamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At the end of the day, Aquarius is dedicated to making the world a better place.', #jan20-feb18

    'picses':'Pisces. Pisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that\'s because it\'s the last of the last. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs. It\'s symbolized by two fish swimming in opposite directions, representing the constant division of Pisces\' attention between fantasy and reality.', #feb19-march20

    'aries':'Aries. Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. Bold and ambitious, Aries dives headfirst into even the most challenging situations and they\'ll make sure they always come out on top',#march21-april19

    'taurus':'Taurus. Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors.', #april20-may20

    'gemini':'Gemini. Gemini\'s are Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself.', #may21-june21

    'cancer':'Cancer. Cancer seamlessly weaves between the sea and shore representing Cancers ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. But—just like the hard shelled crustaceans-this water sign is willing to do whatever it takes to protect itself emotionally. In order to get to know this sign, you\'re going to need to establish trust', #jue22-july22

    'leo':'Leo. Leo\'s are Passionate, loyal, and infamously dramatic, Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They\'re delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and celebrate… well, themselves.', #july23-aug22

    'virgo':'Virgo. Virgo\'s are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo\'s deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn\'t afraid to improve skills through diligent and consistent practice.', #aug23-sep22

    'libra':'Libra. As a cardinal air sign, Libra is represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra\'s fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life — especially when it comes to matters of the heart', #sep23-oct23

    'scorpio':'Scorpion. Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this sign one of the most complicated, dynamic signs of the zodiac', #oct24-nov21

    'sagittarius':'Sagitarius. This fire sign knows no bounds. Represented by the archer, Sagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits like blazing arrows, chasing after geographical, intellectual, and spiritual adventures.', #nov22-dec21

    'capricorn':'Capricorn. Capricorn is climbing the mountain straight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign of the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.' #dec22-jan19
}

horoscope = '' #this will be reassigned on every if statement

import logging
logging.basicConfig(level=logging.WARNING, filename='star.log', filemode='w', format= '%(asctime)s: %(levelname)s: %(message)s')
try:
    day= int(input('Enter birth day: ')) #users birth day
    month = int(input('Enter birth month(in number form eg 9): ')) #users birth month

    if (20<= day <=31 and month ==1) or ( 1<=day<=18 and month==2):
        horoscope =star_signs.get('aquarius')
    elif (19<=day<=29 and month==2) or (1<=day<=20 and month==3):
        horoscope =star_signs.get('picses')
    elif (21<=day<=31 and month==3) or (1<=day<=19 and month==4):
        horoscope = star_signs.get('aries')
    elif (20<=day<=30 and month==4) or (1<=day<=20 and month==5):
        horoscope = star_signs.get('taurus')
    elif (21<=day<=31 and month==5) or (1<=day<=21 and month==6):
        horoscope = star_signs.get('gemini')
    elif (22<=day<=30 and month==6) or (1<=day<=22 and month==7):
        horoscope = star_signs.get('cancer')
    elif (23<=day<=31 and month==7) or (1<=day<=22 and month==8):
        horoscope = star_signs.get('leo')
    elif (23<=day<=30 and month==8) or (1<=day<=22 and month==9):
        horoscope = star_signs.get('virgo')
    elif (23<=day<=30 and month==9) or (1<=day<=23 and month==10):
        horoscope = star_signs.get('libra')
    elif (24<=day<=31 and month==10) or (1<=day<=21 and month==11):
        horoscope = star_signs.get('scorpio')
    elif (22<=day<=30 and month==11) or (1<=day<=21 and month==12):
        horoscope = star_signs.get('sagittarius')
    elif (22<=day<=31 and month==12) or (1<=day<=19 and month==1):
        horoscope = star_signs.get('capricorn')
except:
    logging.exception('ERROR')

#12  if statements that will evelute the day_of_birt AND month_of_birth. if both conditions are true then the correspoding reassigned horoscope will print
user_name= input('Enter your name: ').title().strip() #users name
print(f'Hi {user_name}. You are a {horoscope}') #this will print the final horoscope based on the if statement and the variable reassignment