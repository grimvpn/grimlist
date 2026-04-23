import requests

def fetch_and_clean(urls, title, prefix):
    unique_configs = []
    # Протоколы, которые мы ищем
    protocols = ('vless://', 'ss://', 'vmess://', 'trojan://', 'tuic://', 'hysteria2://', 'hy2://')
    
    for url in urls:
        try:
            print(f"Загрузка: {url}")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    
                    # Проверяем, начинается ли строка с нужного протокола
                    if any(line.startswith(p) for p in protocols):
                        # Очищаем от старого названия (берем всё до символа #)
                        clean_link = line.split('#')[0]
                        
                        if clean_link not in unique_configs:
                            unique_configs.append(clean_link)
            else:
                print(f"Ошибка {response.status_code} для {url}")
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    # Формируем итоговый текст
    # Сначала заголовок подписки
    output = f"# profile-title: {title}\n"
    
    # Добавляем ссылки с твоим названием и нумерацией
    for i, link in enumerate(unique_configs, 1):
        output += f"{link}#{prefix}_{i}\n"
        
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

# Сохраняем результаты в файлы
print("Обработка White List...")
with open("wl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(wl_sources, "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList"))

print("Обработка Black List...")
with open("bl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(bl_sources, "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList"))

print("Обработка All List...")
with open("all.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(all_sources, "🏳️ VPN 🏴 | GrimVPN", "GrimVPN"))

print("Готово!")
