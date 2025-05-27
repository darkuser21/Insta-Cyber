import instaloader
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = Fore.GREEN + r"""
##################################################
#                                                #
#      ██████  ██   ██ ████████  ██████           #
#     ██    ██ ██   ██    ██    ██    ██          #
#     ██    ██ ██   ██    ██    ██    ██          #
#     ██ ▄▄ ██ ██   ██    ██    ██    ██          #
#      ██████   ██████    ██     ██████           #
#        ▀▀                                        #
#        [ I N S T A - C Y B E R  O S I N T ]      #
##################################################
""" + Style.RESET_ALL
    print(banner)

def print_footer():
    print(Fore.CYAN + "\n          >>> made by cybexcel.io <<<\n" + Style.RESET_ALL)

def get_instagram_info(username, loader):
    try:
        profile = instaloader.Profile.from_username(loader.context, username)

        print(Fore.YELLOW + "\n--- Instagram OSINT Info ---" + Style.RESET_ALL)
        print(Fore.GREEN + f"[+] Username       : {profile.username}")
        print(f"[+] Full Name      : {profile.full_name}")
        print(f"[+] User ID        : {profile.userid}")
        print(f"[+] Bio            : {profile.biography}")
        print(f"[+] Followers      : {profile.followers}")
        print(f"[+] Following      : {profile.followees}")
        print(f"[+] Posts          : {profile.mediacount}")
        print(f"[+] Private        : {profile.is_private}")
        print(f"[+] Verified       : {profile.is_verified}")
        print(f"[+] Profile Pic URL: {profile.profile_pic_url}")
        print(f"[+] External URL   : {profile.external_url}" + Style.RESET_ALL)
        print(Fore.YELLOW + "------------------------------\n" + Style.RESET_ALL)
        return profile

    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}" + Style.RESET_ALL)
        return None

def download_followers(profile, filename="followers.txt"):
    print(Fore.CYAN + f"[+] Downloading followers of {profile.username}..." + Style.RESET_ALL)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for follower in profile.get_followers():
                f.write(f"{follower.username}\n")
        print(Fore.GREEN + f"[✓] Followers list saved to {filename}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error downloading followers: {e}" + Style.RESET_ALL)

def download_following(profile, filename="following.txt"):
    print(Fore.CYAN + f"[+] Downloading following of {profile.username}..." + Style.RESET_ALL)
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for followee in profile.get_followees():
                f.write(f"{followee.username}\n")
        print(Fore.GREEN + f"[✓] Following list saved to {filename}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[!] Error downloading following: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    print_banner()
    username = input(Fore.CYAN + "[?] Enter Instagram username: " + Style.RESET_ALL).strip()

    loader = instaloader.Instaloader()

    # Optional login (uncomment to enable)
    # loader.login('your_username', 'your_password')

    profile = get_instagram_info(username, loader)

    if profile:
        if profile.is_private and not profile.followed_by_viewer:
            print(Fore.RED + "[!] Cannot fetch followers/following from a private account unless you follow them and are logged in." + Style.RESET_ALL)
        else:
            print(Fore.MAGENTA + "What would you like to do next?")
            print("1. Download followers")
            print("2. Download following")
            print("3. Download both")
            print("4. Exit" + Style.RESET_ALL)
            choice = input(Fore.YELLOW + "[?] Enter choice (1/2/3/4): " + Style.RESET_ALL).strip()

            if choice == '1':
                download_followers(profile)
            elif choice == '2':
                download_following(profile)
            elif choice == '3':
                download_followers(profile)
                download_following(profile)
            elif choice == '4':
                print(Fore.CYAN + "[✓] Exiting..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "[!] Invalid choice." + Style.RESET_ALL)

    print_footer()
