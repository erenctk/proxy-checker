# Advanced Proxy Checker / Gelişmiş Proxy Kontrol Aracı

[English](#english) | [Türkçe](#turkish)

## English

A fast and efficient proxy checker with a beautiful terminal interface. This tool checks multiple proxies simultaneously using asynchronous processing and provides detailed information about each proxy.

### Features

- Fast asynchronous proxy checking
- Beautiful terminal interface with colors
- Real-time progress bar
- Proxy speed measurement
- Automatic country detection
- Saves results to separate files
- Easy-to-use command line interface

### Requirements

- Python 3.7+
- aiohttp
- colorama
- tqdm

### Installation

1. Clone the repository:
```bash
git clone https://github.com/erenctk/proxy-checker.git
cd proxy-checker
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

### Usage

1. Create a proxy.txt file and add your proxies (one per line):
```
1.1.1.1:8080
2.2.2.2:3128
```

2. Run the application:
```bash
python proxy_checker.py
```

### Output Files

- `working_proxies.txt`: Contains working proxies with their speed and country information
- `not_working_proxies.txt`: Contains non-working proxies

### Technical Details

- Uses aiohttp for asynchronous HTTP requests
- Colorama for terminal colors
- tqdm for progress tracking
- IP-API for country detection
- Asynchronous architecture for maximum performance

---

## Turkish

Güzel bir terminal arayüzüne sahip, hızlı ve verimli bir proxy kontrol aracı. Bu araç, asenkron işleme kullanarak birden fazla proxy'i aynı anda kontrol eder ve her proxy hakkında detaylı bilgi sağlar.

### Özellikler

- Hızlı asenkron proxy kontrolü
- Renkli ve güzel terminal arayüzü
- Gerçek zamanlı ilerleme çubuğu
- Proxy hız ölçümü
- Otomatik ülke tespiti
- Sonuçları ayrı dosyalara kaydetme
- Kullanımı kolay komut satırı arayüzü

### Gereksinimler

- Python 3.7+
- aiohttp
- colorama
- tqdm

### Kurulum

1. Depoyu klonlayın:
```bash
git clone https://github.com/erenctk/proxy-checker.git
cd proxy-checker
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

### Kullanım

1. proxy.txt dosyası oluşturun ve proxylerinizi ekleyin (her satıra bir tane):
```
1.1.1.1:8080
2.2.2.2:3128
```

2. Uygulamayı çalıştırın:
```bash
python proxy_checker.py
```

### Çıktı Dosyaları

- `working_proxies.txt`: Çalışan proxyleri, hızları ve ülke bilgileriyle birlikte içerir
- `not_working_proxies.txt`: Çalışmayan proxyleri içerir

### Teknik Detaylar

- HTTP istekleri için aiohttp kullanır
- Terminal renkleri için colorama
- İlerleme takibi için tqdm
- Ülke tespiti için IP-API
- Maksimum performans için asenkron mimari

## Özellikler

- Çoklu proxy kontrolü
- Asenkron işlem desteği ile hızlı kontrol
- Proxy hız testi
- Ülke tespiti
- Anonimlik seviyesi kontrolü
- Gerçek zamanlı sonuç gösterimi
- Mobil uyumlu arayüz
- Detaylı istatistikler
- Görsel geri bildirimler

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı başlatın:
```bash
python proxy_checker.py
```
Bu uygulama, proxy kontrolü için modern ve kullanıcı dostu bir çözüm sunmak amacıyla geliştirilmiştir. 