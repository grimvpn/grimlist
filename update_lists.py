import requests

def fetch_and_process(urls, output_file, title):
    # Добавляем заголовок профиля (твое брендирование подписки)
    combined_content = f"# profile-title: {title}\n"
    unique_configs = [] 
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            print(f"Загрузка: {url}")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                for line in response.text.splitlines():
                    line = line.strip()
                    # Проверяем, что это VPN ссылка
                    if any(line.startswith(p) for p in protocols):
                        # Добавляем строку целиком (со всеми оригинальными названиями)
                        if line not in unique_configs:
                            unique_configs.append(line)
        except Exception as e:
            print(f"Ошибка с {url}: {e}")
    
    # Собираем всё в один текст
    combined_content += "\n".join(unique_configs)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined_content.strip())

# Твои источники
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

# Запись файлов с сохранением оригинальных имен серверов
fetch_and_process(wl_sources, "wl.txt", "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN")
fetch_and_process(bl_sources, "bl.txt", "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN")
fetch_and_process(all_sources, "all.txt", "🏳️ VPN 🏴 | GrimVPN")
