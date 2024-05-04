startmustard = 0
startplum = 0
startgreen = 0
startpeacock = 0
startscarlet = 0
startwhite = 0
starthall = 0
startdiningroom = 0
startkitchen = 0
startpatio = 0
startobservatory = 0
starttheater = 0
startlivingroom = 0
startspa = 0
startguesthouse = 0
startknife = 0
startcandlestick = 0
startpistol = 0
startpoison = 0
starttrophy = 0
startrope = 0
startbat = 0
startaxe = 0
startdumbell = 0
mustard = 1
plum = 1
green = 1
peacock = 1
scarlet = 1
white = 1
hall = 1
diningroom = 1
kitchen = 1
patio = 1
observatory = 1
theater = 1
livingroom = 1
spa = 1
guesthouse = 1
knife = 1
candlestick = 1
pistol = 1
poison = 1
trophy = 1
rope = 1
bat = 1
axe = 1
dumbell = 1
personlist = ""
roomlist = ""
weaponlist = ""
persons = 0
rooms = 0
weapons = 0
for loop in range(1000):
  startrumor = 0
  rpersonprint = 0
  rroomprint = 0
  rweaponprint = 0
  #Person
  person = input("Person: ")
  if person == "Mustard":
    if mustard == 1:
      personlist = personlist + " " + "Mustard"
      persons = persons + 1
      mustard = mustard -1
      smus = input("Start? ")
      if smus == "Yes":
        startmustard = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  if person == "Plum":
    if plum == 1:
      personlist = personlist + " " + "Plum"
      persons = persons + 1
      plum = plum -1
      splu= input("Start? ")
      if splu == "Yes":
        startplum = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  if person == "Green":
    if green == 1:
      personlist = personlist + " " + "Green"
      persons = persons + 1
      green = green -1
      sgre = input("Start? ")
      if sgre == "Yes":
        startgreen = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  if person == "Peacock":
    if peacock == 1:
      personlist = personlist + " " + "Peacock"
      persons = persons + 1
      peacock = peacock -1
      spea= input("Start? ")
      if spea == "Yes":
        startpeacock = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  if person == "Scarlet":
    if scarlet == 1:
      personlist = personlist + " " + "Scarlet"
      persons = persons + 1
      scarlet = scarlet -1
      sscar= input("Start? ")
      if sscar == "Yes":
          startscarlet = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  if person == "White":
    if scarlet == 1:
      personlist = personlist + " " + "White"
      persons = persons + 1
      white = white -1
      swhi = input("Start? ")
      if swhi == "Yes":
        startwhite = 1
    if persons >= 5:
      if mustard == 1:
        print("Mustard")
      if plum == 1:
        print("Plum")
      if green == 1:
        print("Green")
      if peacock == 1:
        print("Peacock")
      if scarlet == 1:
        print("Scarlet")
      if white == 1:
        print("White")
  #Room
  room = input("Room: ")
  if room == "Hall":
    if hall == 1:
      rooomlist = roomlist + " " + "Hall"
      rooms = rooms + 1
      hall = hall -1
      shal = input("Start? ")
      if shal == "Yes":
        starthall = 1
    if rooms >= 5:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Dining Room":
    if diningroom == 1:
      rooomlist = roomlist + " " + "Dining Room"
      rooms = rooms + 1
      diningroom = diningroom -1
      sdin = input("Start? ")
      if sdin == "Yes":
        startdingingroom = 1
    if rooms >= 5:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Kitchen":
    if kitchen == 1:
      rooomlist = roomlist + " " + "Kitchen"
      rooms = rooms + 1
      kitchen = kitchen -1
      skit = input("Start? ")
      if skit == "Yes":
        startkitchen = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Patio":
    if patio == 1:
      rooomlist = roomlist + " " + "Patio"
      rooms = rooms + 1
      patio = patio -1
      spat = input("Start? ")
      if spat == "Yes":
        startpatio = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Observatory":
    if observatory == 1:
      rooomlist = roomlist + " " + "Observatory"
      rooms = rooms + 1
      observatory = observatory -1
      sobs = input("Start? ")
      if sobs == "Yes":
        startobservatory = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Theater":
    if theater == 1:
      rooomlist = roomlist + " " + "Theater"
      rooms = rooms + 1
      theater = theater -1
      sthe = input("Start? ")
      if sthe == "Yes":
        starttheater = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Living Room":
    if livingroom == 1:
      rooomlist = roomlist + " " + "Living Room"
      rooms = rooms + 1
      livingroom = livingroom -1
      sliv = input("Start? ")
      if sliv == "Yes":
        startlivingroom = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Spa":
    if spa == 1:
      rooomlist = roomlist + " " + "Spa"
      rooms = rooms + 1
      spa = spa -1
      sspa = input("Start? ")
      if sspa == "Yes":
        startspa = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  if room == "Guest House":
    if guesthouse == 1:
      rooomlist = roomlist + " " + "Guest House"
      rooms = rooms + 1
      guesthouse = guesthouse -1
      sgue = input("Start? ")
      if sgue == "Yes":
        startguesthouse = 1
    if rooms >= 8:
      if hall == 1:
        print("Hall")
      if diningroom == 1:
        print("Dining Room")
      if kitchen == 1:
        print("Kitchen")
      if patio == 1:
        print("Patio")
      if observatory == 1:
        print("Observatory")
      if theater == 1:
        print("Theater")
      if livingroom == 1:
        print("Living Room")
      if spa == 1:
        print("Spa")
      if guesthouse == 1:
        print("Guest House")
  #weapon
  weapon = input("Weapon: ")
  if weapon == "Knife":
    if knife == 1:
      weaponlist = weaponlist + " " + "Knife"
      weapons = weapons + 1
      knife = knife -1
      skni = input("Start? ")
      if skni == "Yes":
        startknife = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Candlestick":
    if candlestick == 1:
      weaponlist = weaponlist + " " + "Candlestick"
      weapons = weapons + 1
      candlestick = candlestick -1
      scan = input("Start? ")
      if scan == "Yes":
        startcandlestick = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Pistol":
    if pistol == 1:
      weaponlist = weaponlist + " " + "Pistol"
      weapons = weapons + 1
      pistol = pistol - 1
      spis = input("Start? ")
      if spis == "Yes":
        startpistol = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Poison":
    if poison == 1:
      weaponlist = weaponlist + " " + "Poison"
      weapons = weapons + 1
      poison = poison -1
      spoi = input("Start? ")
      if spoi == "Yes":
        startpoison = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Trophy":
    if trophy == 1:
      weaponlist = weaponlist + " " + "Trophy"
      weapons = weapons + 1
      trophy = trophy -1
      stro = input("Start? ")
      if stro == "Yes":
        startstrophy = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Rope":
    if rope == 1:
      weaponlist = weaponlist + " " + "Rope"
      weapons = weapons + 1
      rope = rope -1
      srop = input("Start? ")
      if srop == "Yes":
        startrope = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Bat":
    if bat == 1:
      weaponlist = weaponlist + " " + "Bat"
      weapons = weapons + 1
      bat = bat -1
      sbat = input("Start? ")
      if sbat == "Yes":
        startbat = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Axe":
    if axe == 1:
      weaponlist = weaponlist + " " + "Axe"
      weapons = weapons + 1
      axe = axe -1
      saxe = input("Start? ")
      if saxe == "Yes":
        startaxe = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  if weapon == "Dumbell":
    if dumbell == 1:
      weaponlist = weaponlist + " " + "Dumbell"
      weapons = weapons + 1
      dumbell = dumbell -1
      sdum = input("Start? ")
      if sdum == "Yes":
        startdumbell = 1
    if weapons >= 8:
      if knife == 1:
        print("Knife")
      if candlestick == 1:
        print("Candlestick")
      if pistol == 1:
        print("Pistol")
      if poison == 1:
        print("Poison")
      if trophy == 1:
        print("Trophy")
      if rope == 1:
        print("Rope")
      if bat == 1:
        print("Bat")
      if axe == 1:
        print("Axe")
      if dumbell == 1:
        print("Dumbell")
  #pickcard
  rperson = input("Person: ")
  if rperson == "Mustard":
    if startmustard == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  if rperson == "Plum":
    if startplum == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  if rperson == "Green":
    if startgreen == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  if rperson == "Peacock":
    if startpeacock == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  if rperson == "Scarlet":
    if startscarlet == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  if rperson == "White":
    if startwhite == 1:
      startrumor = startrumor + 1
    else:
      rpersonprint = 1
  rroom = input("Room: ")
  if rroom == "Hall":
    if starthall == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Dining Room":
    if startdiningroom == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Kitchen":
    if startkitchen == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Patio":
    if startpatio == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Observatory":
    if startobservatory == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Theater":
    if starttheater == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Living Room":
    if startlivingroom == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Spa":
    if startspa == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  if rroom == "Guest House":
    if startguesthouse == 1:
      startrumor = startrumor + 1
  else:
    rroomprint = 1
  rweapon = input("Weapon: ")
  if rweapon == "Knife":
    if startknife == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Candlestick":
    if startcandlestick == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Pistol":
    if startpistol == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Poison":
    if startpoison == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Trophy":
    if starttrophy == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Rope":
    if startrope == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Bat":
    if startbat == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Axe":
    if startaxe == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  if rweapon == "Dumbell":
    if startdumbell == 1:
      startrumor = startrumor + 1
  else:
    rweaponprint = 1
  cardshown = input("Did someone show a card? ")
  if cardshown == "Yes":
    if startrumor == 2:
      if rpersonprint == 0:
        if rperson == "Mustard":
          if mustard == 1:
            personlist = personlist + " " + "Mustard"
            persons = persons + 1
            mustard = mustard -1
          if rperson == "Green":
             if green == 1:
                personlist = personlist + " " + "Green"
                persons = persons + 1
                green = green -1
          if rperson == "Peacock":
            if peacock == 1:
              personlist = personlist + " " + "Peacock"
              persons = persons + 1
              peacock = peacock -1
          if rperson == "Scarlet":
            if scarlet == 1:
              personlist = personlist + " " + "Scarlet"
              persons = persons + 1
              scarlet = scarlet -1
          if rperson == "White":
            if white == 1:
              personlist = personlist + " " + "White"
              persons = persons + 1
              white = white -1
              if persons >= 5:
                if mustard == 1:
                  print("Mustard")
                if plum == 1:
                  print("Plum")
                if green == 1:
                  print("Green")
                if peacock == 1:
                  print("Peacock")
                if scarlet == 1:
                  print("Scarlet")
                if white == 1:
                  print("White")
    if cardshown == "Yes":                  
      if rroomprint == 0:
        if rroom == "Hall":
          if hall == 1:
            rooomlist = roomlist + " " + "Hall"
            rooms = rooms + 1
            hall = hall - 1
        if rroom == "Dining Room":
          if dingingroom == 1:
            rooomlist = roomlist + " " + "Dining Room"
            rooms = rooms + 1
            diningroom = diningroom - 1
        if rroom == "Kitchen":
          if kitchen == 1:
            rooomlist = roomlist + " " + "Kitchen"
            rooms = rooms + 1
            kitchen = kitchen - 1
        if rroom == "Patio":
          if patio == 1:
            rooomlist = roomlist + " " + "Patio"
            rooms = rooms + 1
            patio = patio - 1
        if rroom == "Observatory":
          if observatory == 1:
            rooomlist = roomlist + " " + "Observatory"
            rooms = rooms + 1
            observatory = observatory - 1
        if rroom == "Theater":
          if theater == 1:
            rooomlist = roomlist + " " + "Theater"
            rooms = rooms + 1
            theater = theater - 1
        if rroom == "Living Room":
          if livingroom == 1:
            rooomlist = roomlist + " " + "Living Room"
            rooms = rooms + 1
            livingroom = livingroom - 1
        if rroom == "Spa":
          if spa == 1:
            rooomlist = roomlist + " " + "Spa"
            rooms = rooms + 1
            spa = spa - 1
        if rroom == "Guest House":
          if guesthouse == 1:
            rooomlist = roomlist + " " + "Guest House"
            rooms = rooms + 1
            guesthouse = guesthouse - 1
            if rooms >= 8:
              if hall == 1:
                print("Hall")
              if diningroom == 1:
                print("Dining Room")
              if kitchen == 1:
                print("Kitchen")
              if patio == 1:
                print("Patio")
              if observatory == 1:
                print("Observatory")
              if theater == 1:
                print("Theater")
              if livingroom == 1:
                print("Living Room")
              if spa == 1:
                print("Spa")
              if guesthouse == 1:
                print("Guest House")
  if cardshown == "Yes":
      if rweaponprint == 0:
        if rweapon == "Knife":
          if knife == 1:
            weaponlist = weaponlist + " " + "Knife"
            weapons = weapons + 1
            knife = knife - 1
        if rweapon == "Candlestick":
          if candlestick == 1:
            weaponlist = weaponlist + " " + "Candlestick"
            weapons = weapons + 1
            candlestick = candlestick - 1
        if rweapon == "Pistol":
          if pistol == 1:
            weaponlist = weaponlist + " " + "Pistol"
            weapons = weapons + 1
            pistol = pistol - 1
        if rweapon == "Poison":
          if poison == 1:
            weaponlist = weaponlist + " " + "Poison"
            weapons = weapons + 1
            poison = poison - 1
        if rweapon == "Trophy":
          if trophy == 1:
            weaponlist = weaponlist + " " + "Trophy"
            weapons = weapons + 1
            trophy = trophy - 1
        if rweapon == "Rope":
          if rope == 1:
            weaponlist = weaponlist + " " + "Rope"
            weapons = weapons + 1
            rope = rope -1
        if rweapon == "Bat":
          if bat == 1:
            weaponlist = weaponlist + " " + "Bat"
            weapons = weapons + 1
            bat = bat -1
        if rweapon == "Axe":
          if axe == 1:
            weaponlist = weaponlist + " " + "Axe"
            weapons = weapons + 1
            axe = axe -1
        if rweapon == "Dumbell":
          if dumbell == 1:
            weaponlist = weaponlist + " " + "Dumbell"
            weapons = weapons + 1
            dumbell = dumbell -1
            if weapons >= 8:
              if knife == 1:
                print("Knife")
              if candlestick == 1:
                print("Candlestick")
              if pistol == 1:
                print("Pistol")
              if poison == 1:
                print("Poison")
              if trophy == 1:
                print("Trophy")
              if rope == 1:
                print("Rope")
              if bat == 1:
                print("Bat")
              if axe == 1:
                print("Axe")
              if dumbell == 1:
                print("Dumbell")