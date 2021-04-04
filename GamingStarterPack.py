import requests
import os

def Request(URL, file):
    r = requests.get(URL, allow_redirects = True)
    open(file, 'wb').write(r.content)

print("""
        Gaming Launchers Starter Pack(All platforms Version)
        _____________________________________
        |Values:                             |
        |Steam = steam                       | //Fully Supported
        |Epic Games = epgames                | //Windows only
        |Ubisoft Connect = ubi               | //Windows only
        |Rockstar Games Launcher = rockstar  | // Windows only
        |Valorant = val                      | // Windows only
        |League of Legends = lol             | // Windows and Mac only
        |BattleNet = battle.net              | // Windows and Mac only
        |GOG Galaxy = gog                    | // Windows and Mac only 
        |Origin(EA) = origin                 | // Windows and Mac only
        |Bethesda Launcher = bethesda        | // Windows only     
        |____________________________________|\n
        
        Note: MACOS and Linux files can't be auto opened. Sorry if you need to have faster access to those files.
""")

download = input("Enter the launcher value you want to download:").lower()
platform = input("Enter the platform your device runs on:").lower()

windowsurls = ["https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe",
"https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi",
"https://ubi.li/4vxt9",
"https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe",
"https://valorant.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.live.",
"https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.",
"https://eu.battle.net/download/getInstaller?os=win&installer=Battle.net-Setup.exe",
"https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe",
"https://www.dm.origin.com/download",
"https://download.cdp.bethesda.net/BethesdaNetLauncher_Setup.exe"]

linuxurls = ["https://cdn.akamai.steamstatic.com/client/installer/steam.deb"]

macosurls = ["https://cdn.akamai.steamstatic.com/client/installer/steam.dmg", "https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live", "https://eu.battle.net/download/getInstaller?os=mac&installer=Battle.net-Setup.zip", "https://content-system.gog.com/open_link/download?path=/open/galaxy/client/2.0.37.330/galaxy_client_2.0.37.330.pkg", "https://www.dm.origin.com/mac/download"]

if download == "steam":
    if platform == "windows":
        url = windowsurls[0]
        Request(url, 'SteamSetup.exe')
        os.system('SteamSetup.exe')
    elif platform == "linux":
            url = linuxurls[0]
            Request(url, 'steam.deb')
            
    elif platform == "macos":
                url = macosurls[0]
                Request(url, 'steam.dmg')
                
  
    

    

elif download == "epgames":
    url = windowsurls[1]
    Request(url, 'EpicGames.msi')
    os.system('EpicGames.msi')

elif download == "ubi":
    url = windowsurls[2]
    Request(url, 'UbisoftConnect.exe')
    os.system('UbisoftConnect.exe')

elif download == "rockstar":
    url = windowsurls[3]
    Request(url,'RockstarGamesLauncher.exe')
    os.system('RockstarGamesLauncher.exe')

elif download == "val":
    region = input("Enter your region:").lower() + '.exe'
    url = windowsurls[4] + region
    Request(url, 'Valorant.exe')
    os.system('Valorant.exe')

if download == "lol":
    if platform == "windows":
        region = input("Enter your region:").lower() + '.exe'
        url = windowsurls[5] + region
        Request(url, 'LOLInstaller.exe')
        os.system('LOLInstaller.exe')
    elif platform == "macos":
        region = input("Enter your region:").lower() + '.zip'
        url = macosurls[1] + region
        Request(url, 'LOLInstaller.zip')
        

if download == "battle.net":
    if platform == "windows":
        url = windowsurls[6]
        Request(url, 'BattleNetWin.exe')
        os.system('BattleNetWin.exe')
    elif platform == "macos":
        url = macosurls[2]
        Request(url, 'BattleNetMac.zip')
        

if download == "gog":
    if platform == "windows":
        url = windowsurls[7]
        Request(url, 'GOGGalaxy2.0.exe')
        os.system('GOGGalaxy2.0.exe')
    elif platform == "macos":
        url = macosurls[3]
        Request(url, 'GOGGalaxy2.0.pkg')
        

if download == "origin":
    if platform == "windows":
        url = windowsurls[8]
        Request(url, 'OriginSetup.exe')
        os.system('OriginSetup.exe')
    elif platform == "macos":
        url = macosurls[4]
        Request(url, 'Origin.dmg')
        

elif download == "bethesda":
    url = windowsurls[9]
    Request(url, 'BethesdaLauncherSetup.exe')
    os.system('BethesdaLauncherSetup.exe')
    

else:
  print("Name not valid!")