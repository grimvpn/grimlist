import requests

def fetch_and_save(urls, output_file):
    combined_content = ""
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                combined_content += response.text + "\n"
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined_content.strip())

# Списки источников
wl_sources = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile-2.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/WHITE-CIDR-RU-all.txt",
    "https://etoneya.a9fm.site/whitelist"
]

bl_sources = [
    "https://obwl.obprojects.lol/sub.txt",
    "https://obwl.vercel.app/sub.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt"
]

all_sources = wl_sources + bl_sources

# Выполнение
fetch_and_save(wl_sources, "wl.txt")
fetch_and_save(bl_sources, "bl.txt")
fetch_and_save(all_sources, "all.txt")
