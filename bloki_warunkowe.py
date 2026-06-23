pensja = 12000
wczasy = "morze"

if pensja < 5000 and wczasy == "mazury":
    message = "nie za wiele na wczasy"
            # \podział wiersza na kilka linii
elif pensja < 8000 and \
        (wczasy == "mazury"
         or wczasy == "morze"):
    message = "może tak być"
elif pensja < 13000 and pensja >= 8000:
    message = "super"
else:
    message = "może być x 2"

#komunikaty
print(message)
