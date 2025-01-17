# An influencer is a person who can influence other people's behaviour. 
# An influencer communicates with other people using social networking sites. 
# Write a program that checks whether a given person is a good influencer, that is, 
# whether the person has at least two of the following accounts: Facebook, Twitter or Instagram.
# Use logical type variables: facebook, twitter, instagram, the value of which indicates whether
#  the person has an account on the social networking site.

# Sample result:
# facebook = True
# twitter = False
# instagram = True
# You are a good influencer!

# Influencer to osoba, która może wpływać na zachowanie innych ludzi
# Influencer komunikuje się z innymi ludźmi za pomocą serwisów społecznościowych
# Program sprawdza, czy osoba ma co najmniej dwa konta w popularnych serwisach: Facebook, Twitter, Instagram

# Zapytanie użytkownika o posiadanie konta w serwisach społecznościowych
print("Do you have...")
s_facebook = input("Facebook? (Y/N): ")  # Pytanie o Facebook
s_instagram = input("Instagram? (Y/N): ")  # Pytanie o Instagram
s_twitter = input("Twitter? (Y/N): ")  # Pytanie o Twitter

# Przypisanie wartości True lub False do zmiennych w zależności od odpowiedzi użytkownika
if s_facebook.upper() == "Y":
    facebook = True  # Osoba ma konto na Facebooku
else:
    facebook = False  # Osoba nie ma konta na Facebooku

if s_instagram.upper() == "Y":
    instagram = True  # Osoba ma konto na Instagramie
else:
    instagram = False  # Osoba nie ma konta na Instagramie

if s_twitter.upper() == "Y":
    twitter = True  # Osoba ma konto na Twitterze
else:
    twitter = False  # Osoba nie ma konta na Twitterze

# Lista zmiennych odpowiadających za posiadanie kont w serwisach
apps = [facebook, twitter, instagram]
apps_count = 0  # Licznik kont w serwisach społecznościowych

# Liczenie, ile kont w serwisach społecznościowych posiada użytkownik
for app in apps:
    if app == True:
        apps_count += 1

# Sprawdzanie, czy użytkownik ma co najmniej dwa konta
if apps_count >= 2:
    print("You are a good influencer!")  # Osoba jest influencerem
else:
    print("You are not so good at influencing...")  # Osoba nie jest influencerem
