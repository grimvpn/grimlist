import requests

def fetch_and_clean(urls, title, prefix):
    unique_configs = []
    # Список поддерживаемых протоколов
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    
                    # Проверяем, что строка начинается с протокола VPN
                    if any(line.startswith(p) for p in protocols):
                        # Отрезаем старое название после знака #
                        base_config = line.split('#')[0]
                        
                        if base_config not in unique_configs:
                            unique_configs.append(base_config)
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    # Формируем итоговый текст
    output = f"# profile-title: {title}\n"
    
    # Собираем строки: Ссылка#ТвоеНазвание_Номер
    for i, config in enumerate(unique_configs, 1):
        output += f"{config}#{prefix}_{i}\n"
        
    return output

# Источники
wl_sources = [
    "https://githubusercontent.com",
    "https://githubusercontent.com",
    "https://a9fm.site"
]

bl_sources = [
    "https://obprojects.lol",
    "https://vercel.app",
    "https://githubusercontent.com",
    "https://githubusercontent.com",
    "https://githubusercontent.com"
]

all_sources = wl_sources + bl_sources

# Сохранение файлов с твоими названиями
with open("wl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(wl_sources, "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList"))

with open("bl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(bl_sources, "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList"))

with open("all.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(all_sources, "🏳️ VPN 🏴 | GrimVPN", "GrimVPN"))
    
