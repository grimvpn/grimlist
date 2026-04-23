import requests

def fetch_and_clean(urls, title, prefix):
    unique_configs = []
    
    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    # Пропускаем пустые строки, комментарии и спец. заголовки
                    if not line or line.startswith('#') or line.startswith('//'):
                        continue
                    
                    # Очищаем от старого названия (все после #)
                    base_config = line.split('#')[0]
                    
                    if base_config not in unique_configs:
                        unique_configs.append(base_config)
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    # Формируем итоговый текст
    output = f"# profile-title: {title}\n"
    
    # Добавляем нумерацию к каждому конфигу для красоты в приложении
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

# Параметры (Заголовок, Префикс для серверов)
wl_data = ("🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN", "WhiteList")
bl_data = ("🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN", "BlackList")
all_data = ("🏳️ VPN 🏴 | GrimVPN", "GrimVPN")

# Сохранение
with open("wl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(wl_sources, wl_data[0], wl_data[1]))

with open("bl.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(bl_sources, bl_data[0], bl_data[1]))

with open("all.txt", "w", encoding="utf-8") as f:
    f.write(fetch_and_clean(all_sources, all_data[0], all_data[1]))
    
