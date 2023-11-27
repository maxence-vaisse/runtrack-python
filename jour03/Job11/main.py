def time_to_text(minutes):
    if minutes >=0:
        print(f"{int(minutes)//60} heures, {int(minutes)%60} minutes")
    else:
        print("Veuillez entrer un nombre entier positif de minutes.")
time_to_text(70)