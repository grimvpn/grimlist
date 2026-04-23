import requests

def fetch_and_clean(urls, title, prefix):
    unique_configs = []
    # Список протоколов, которые мы ищем в строках
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            response = requests.get(url, timeout=20)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    # Проверяем, что строка начинается с одного из VPN протоколов
                    if any(line.startswith(p) for p in protocols):
                        # Отрезаем старое название (все, что после первого символа #)
                        link_part = line.split('#')[0]
                        
                        # Добавляем в список уникальных, если такой ссылки еще нет
                        if link_part not in unique_configs:
                            unique_configs.append(link_part)
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    # Формируем итоговый текст
    # 1. Заголовок для приложения
    content = f"# profile-title: {title}\n"
    
    # 2. Список ссылок с твоим названием и нумерацией
    for i, link in enumerate(unique_configs, 1):
        content += f"{link}#{prefix}_{i}\n"
        
    return content

# Источники данных
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

# Запись в файлы
with open("wl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(wl_sources, "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList"))

with open("bl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(bl_sources, "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList"))

with open("all.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(all_sources, "🏳️ VPN 🏴 | GrimVPN", "GrimVPN"))
    
