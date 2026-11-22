# 🎤 Голосовой ассистент Васисуалий

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-GPL%203.0-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Android-lightgrey.svg)

**Простой модульный голосовой помощник с открытым исходным кодом**

[Возможности](#-васисуалий-может) • [Установка](#-установка) • [Платформы](#-поддерживаемые-платформы) • [Помощь проекту](#-помочь-проекту)

[<img src="vasisualy/assets/icons/white icon.png" width="100"></img>]()

</div>

---

## 📋 Описание

**Васисуалий** — это простой модульный голосовой помощник, уважающий вашу свободу, хотя и может нахамить 😊. Пока поддерживается только русский язык.

### ✨ Особенности

- 🎯 **Модульная архитектура** - легко добавлять новые навыки
- 🔓 **Свободное ПО** - открытый исходный код под лицензией GPL 3.0
- 🎨 **Графический интерфейс** - удобный Qt5 интерфейс
- 💻 **CLI версия** - для любителей командной строки
- 📱 **Кроссплатформенность** - работает на Linux, Windows и Android

> ⚠️ **Важно:** Не рекомендуется использовать управление голосом (кнопка справа от поля ввода текста) в данной версии, так как используется распознавание речи от Google. Если вы хотите использовать голосовое управление без отправки голоса в Google, воспользуйтесь [веткой со свободным оффлайн распознавателем речи](https://github.com/Oknolaz/vasisualy/tree/free-speech).

---

## 🖥 Поддерживаемые платформы

| Платформа | Статус | Интерфейс |
|-----------|--------|-----------|
| **GNU/Linux** | ✅ Полная поддержка | Qt5 и CLI |
| **Microsoft Windows** | ⚠️ Частичная поддержка | Qt5 |
| **Android** | ✅ Поддерживается | CLI |

---

## 🎯 Васисуалий может:

### 📅 Время и дата
- Сказать текущую дату и время

### 😄 Развлечения
- Рассказать анекдот
- Сказать скороговорку
- Подкинуть монетку
- Сыграть в "Угадай число"
- Сыграть в Русскую рулетку

### 🌐 Интернет и информация
- Сказать о текущей погоде в любом городе мира
- Искать информацию в Интернете
- Искать видео на YouTube
- Искать ответ на вопрос в [Википедии](https://wikipedia.org)
- Рассказать новости с [Wikinews](https://wikinews.org/)

### 🎵 Медиа
- Включить радио
- Воспроизведение музыки

### 💻 Система
- Открыть браузер или веб-сайт (например, YouTube)
- Запустить программу, установленную на вашем ПК
- Сделать снимок экрана
- Выключить или перезагрузить компьютер

### 🗺 Геолокация
- Сказать где вы находитесь
- Открыть карты (OpenStreetMap)

### 🌍 Переводчик
- Перевести текст с любого языка на русский, испанский, английский, французский, итальянский и другие языки

### 💬 Общение
- Повторять ваши слова, как попугай
- Примитивно общаться

### И многое другое...

📚 [Полный список возможностей](https://github.com/Oknolaz/vasisualy/wiki/%D0%92%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8)

---

## 📦 Установка

### 🐧 GNU/Linux

#### 📥 Быстрая установка (AppImage)

Вы можете скачать AppImage, работающий во многих дистрибутивах, со [страницы релизов](https://github.com/Oknolaz/vasisualy/releases).

#### 📦 Debian/Ubuntu

**Шаг 1: Установка синтезатора речи RHVoice**

```bash
sudo add-apt-repository ppa:linvinus/rhvoice
sudo apt-get update
sudo apt-get install speech-dispatcher-rhvoice rhvoice-russian
```

**Шаг 2: Установка системных зависимостей**

```bash
sudo apt-get install python3-speechd python3-pyqt5 vlc python3-pyqt5.qtwebengine python3-pyaudio python3-vlc python3-alsaaudio
```

**Шаг 3: Клонирование репозитория**

```bash
git clone --recursive https://github.com/QuestGuideRF/vasisualy
cd vasisualy
```

**Шаг 4: Установка Python-зависимостей**

```bash
pip3 install -r requirements.txt
```

**Шаг 5: Запуск**

```bash
python3 run.py
```

#### 🎯 Arch Linux

**Шаг 1: Установка из AUR**

```bash
yay -Sy rhvoice python-vlc
```

**Шаг 2: Установка системных пакетов**

```bash
pacman -Sy python-pyaudio python-pyqt5 python-pyalsa speech-dispatcher qt5-webengine vlc python-pyqt5-webengine
```

**Шаг 3: Клонирование репозитория**

```bash
git clone --recursive https://github.com/QuestGuideRF/vasisualy
cd vasisualy
```

**Шаг 4: Установка Python-зависимостей**

```bash
pip3 install -r requirements.txt
```

**Шаг 5: Запуск**

```bash
python3 run.py
```

> 💡 **Также доступен [AUR репозиторий](https://aur.archlinux.org/packages/vasisualy-git/)**

#### 🖥 CLI версия для GNU/Linux

Для [CLI версии](https://github.com/Oknolaz/vasisualy-pi) с распознаванием речи, адаптированной для одноплатных компьютеров (Raspberry Pi, Orange Pi и др.):

```bash
git clone --recursive https://github.com/Oknolaz/vasisualy-pi
cd vasisualy-pi
python3 run.py
```

### 🪟 Windows

**Шаг 1: Установка необходимого ПО**

- Установите [интерпретатор Python 3](https://python.org)
- Установите [VLC media player](https://videolan.org/)

**Шаг 2: Скачивание проекта**

Скачайте [данный репозиторий](https://github.com/Oknolaz/vasisualy-windows/), распакуйте скачанный архив и перейдите в папку с программой.

**Шаг 3: Установка зависимостей**

```bash
pip install -r requirements.txt
```

**Шаг 4: Запуск**

```bash
python run.py
```

🎉 **Поздравляю Вас!** Васисуалий готов к работе!

---

## 🛠 Создание собственного навыка

Вы можете создать собственный навык для голосового ассистента и добавить его в официальный репозиторий!

📖 [Инструкция по созданию навыка](https://github.com/Oknolaz/vasisualy/wiki/%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BD%D0%B0%D0%B2%D1%8B%D0%BA%D0%B0)

---

## 🏥 Помочь проекту

Мы приветствуем любую помощь в развитии проекта!

### Как помочь:

- 🐛 **Сообщить об ошибке** - откройте `Issue` и расскажите об ошибках
- 💡 **Предложить идею** - поделитесь своими идеями и предложениями
- 🔧 **Создать навык** - разработайте собственный навык для ассистента
- 📝 **Улучшить документацию** - помогите улучшить README и документацию
- ⭐ **Поставить звезду** - это мотивирует разработчиков!

---

Подпись относится к текущей версии проекта.

---

Автор: legenda  
Telegram: [@LEGENDA_SD](https://t.me/LEGENDA_SD)
