import requests

def fetch_and_save(urls, output_file, title):
    # Начинаем файл с твоего заголовка
    combined_content = f"# profile-title: {title}\n"
    unique_configs = []
    
    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                # Разбиваем полученный текст на строки
                lines = response.text.splitlines()
                for line in lines:
                    line = line.strip()
                    # Проверяем, что это VPN ссылка и её еще нет в списке
                    if (line.startswith('vless://') or line.startswith('ss://') or 
                        line.startswith('vmess://') or line.startswith('trojan://')) :
                        if line not in unique_configs:
                            unique_configs.append(line)
        except Exception as e:
            print(f"Ошибка при загрузке {url}: {e}")
    
    # Добавляем все уникальные ссылки в итоговую строку
    combined_content += "\n".join(unique_configs)
    
    # Записываем в файл (как в твоем рабочем примере)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined_content.strip())

# Списки источников
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

# Выполнение
fetch_and_save(wl_sources, "wl.txt", "🏳️ БЕЛЫЕ СПИСКИ 🏳️ WHITE LISTS | CIDR | GrimVPN")
fetch_and_save(bl_sources, "bl.txt", "🏴ЧЕРНЫЕ СПИСКИ 🏴 BLACK LISTS | GrimVPN")
fetch_and_save(all_sources, "all.txt", "🏳️ VPN 🏴 | GrimVPN")
