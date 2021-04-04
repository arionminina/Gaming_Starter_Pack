import requests
import os

def Request(URL, file):
    r = requests.get(URL, allow_redirects = True)
    open(file, 'wb').write(r.content)

print("""
        Gaming Launchers Starter Pack(All platforms Version)
        _____________________________________
        |Values:                             |
        |Steam = steam    //Fully Supported  |
        |Epic Games = epgames  //Windows only|
        |Ubisoft Connect = ubi //Windows only|
        |Rockstar Games Launcher = rockstar  | // Windows only
        |Valorant = val // Windows only      |
        |____________________________________|\n
""")

download = input("Enter the launcher value you want to download:").lower()
platform = input("Enter the platform your device runs on:").lower()

windowsurls = ["https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
"https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi",
"https://ubi.li/4vxt9",
"https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe",
"https://valorant.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.live."]

linuxurls = ["https://cdn.akamai.steamstatic.com/client/installer/steam.deb"]

macosurls = ["https://cdn.akamai.steamstatic.com/client/installer/steam.dmg"]

if download == "steam":
   if platform == "windows":
       url = windowsurls[0]
       Request(url, 'SteamSetup.exe')
   elif platform == "linux":
      url = linuxurls[0]
      Request(url, 'steam.deb')
  elif platform == "macos":
      url = macosurls[0]
      Request(url, 'steam.dmg')
    

    

elif download == "epgames":
    url = windowsurls[1]
    Request(url, 'EpicGames.msi')

elif download == "ubi":
    url = windowsurls[2]
    Request(url, 'UbisoftConnect.exe')

elif download == "rockstar":
    url = windowsurls[3]
    Request(url,'RockstarGamesLauncher.exe')

elif download == "val":
    region = input("Enter your region:") + '.exe'
    url = windowsurls[4] + region
    Request(url, 'Valorant.exe')

else:
  print("Name not valid!")
