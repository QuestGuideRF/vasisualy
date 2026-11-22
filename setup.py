from setuptools import setup ,find_packages
import pathlib
here =pathlib .Path (__file__ ).parent .resolve ()
long_description =(here /'README.md').read_text (encoding ='utf-8')
setup (
name ='Vasisualy',
version ='0.8.1',
description ='Русский голосовой помощник для GNU/Linux.',
license ='GPLv3',
long_description =long_description ,
long_description_content_type ='text/markdown',
url ='https://github.com/Oknolaz/vasisualy',
author ='Oknolaz',
author_email ='oknolaz.freedom@protonmail.com',
classifiers =[
'Статус разработки :: 3 - Альфа',
'Целевая аудитория :: Конечные пользователи/рабочие столы',
'Тема :: Общение :: Чат',
'Тема :: Игры/Развлечения',
'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
'Естественный язык :: Русский',
'Операционная система :: Android',
'Операционная система :: POSIX :: Linux',
'Окружающая среда :: Приложения X11 :: Qt',
'Язык программирования :: Python :: 3',
],
keywords ='голосовой помощник, голос, помощник, русский язык',
packages =find_packages (),
package_data ={
'vasisualy':['assets/shot.wav','assets/misfire.wav','music/test.wav','assets/beep.wav'],
'vasisualy.ui':['vas.png'],
'vasisualy.skills.hello_world':['hello_world.trigger'],
'vasisualy.skills.jokes':['jokes.trigger'],
'vasisualy.skills.guess_the_animal':['guess_the_animal.trigger'],
},
python_requires ='>=3.7, <4',
install_requires =['pyowm','python-vlc','pyaudio','translate','wikipedia','mss','qt-material','geocoder','beautifulsoup4','lxml','speechrecognition','pyqt5','pyqtwebengine','scipy','sounddevice','ru_word2number','pyalsaaudio','plyer'],
project_urls ={
'Отчеты об ошибках':'https://github.com/Oknolaz/vasisualy/issues/',
'Source':'https://github.com/Oknolaz/vasisualy/',
'Releases':'https://github.com/Oknolaz/vasisualy/releases/'
},
)