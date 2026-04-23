import requests

def fetch_and_clean(urls, title, prefix):
    unique_configs = []
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            print(f"Загрузка: {url}")
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    if any(line.startswith(p) for p in protocols):
                        # Отрезаем старое название после # и берем только чистую ссылку
                        link_only = line.split('#')[0]
                        if link_only not in unique_configs:
                            unique_configs.append(link_only)
            else:
                print(f"Ошибка сервера {response.status_code} на {url}")
        except Exception as e:
            print(f"Ошибка сети на {url}: {e}")
    
    # Формируем текст
    content = f"# profile-title: {title}\n"
    for i, link in enumerate(unique_configs, 1):
        content += f"{link}#{prefix}_{i}\n"
    return content

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

# Запись файлов
print("Сохранение wl.txt...")
with open("wl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(wl_sources, "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList"))

print("Сохранение bl.txt...")
with open("bl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(bl_sources, "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList"))

print("Сохранение all.txt...")
with open("all.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(all_sources, "🏳️ VPN 🏴 | GrimVPN", "GrimVPN"))

print("Все задачи выполнены успешно!")
