import requests

def fetch_and_process(urls, output_file, title, prefix):
    combined_content = f"# profile-title: {title}\n"
    unique_configs = []
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    # Проверяем, что это ссылка на конфиг
                    if any(line.startswith(p) for p in protocols):
                        # Убираем старое название (все после #)
                        clean_link = line.split('#')[0]
                        if clean_link not in unique_configs:
                            unique_configs.append(clean_link)
        except Exception as e:
            print(f"Ошибка с {url}: {e}")
    
    # Добавляем ссылки с твоим названием и номером
    for i, link in enumerate(unique_configs, 1):
        combined_content += f"{link}#{prefix}_{i}\n"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined_content.strip())

# Источники
wl_sources = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile-2.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Vless-Reality-White-Lists-Rus-Mobile.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-all.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-CIDR-RU-checked.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/WHITE-SNI-RU-all.txt",
    "https://raw.githubusercontent.com/dequar/deqwl/main/vless_checked.txt",
    "https://raw.githubusercontent.com/tankist939-afk/Obhod-WL/refs/heads/main/Obhod%20WL",
    "https://etoneya.a9fm.site/whitelist",
    "https://obwl.obprojects.lol/sub.txt",
    "https://obwl.vercel.app/sub.txt",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless_lite.txt"
]

bl_sources = [
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt",
    "https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt",
    "https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_base64_Sub.txt",
    "https://github.com/AvenCores/goida-vpn-configs/raw/refs/heads/main/githubmirror/26.txt"
]

all_sources = wl_sources + bl_sources

# Выполнение (Файл, Заголовок, Префикс для серверов)
fetch_and_process(wl_sources, "wl.txt", "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList")
fetch_and_process(bl_sources, "bl.txt", "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList")
fetch_and_process(all_sources, "all.txt", "🏳️ VPN 🏴 | GrimVPN", "GrimVPN")
