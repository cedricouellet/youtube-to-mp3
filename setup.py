"""setup.py: setuptools control."""


from re import search, M
from setuptools import setup


version = search(
    '^__version__\s*=\s*"(.*)"',
    open('yt2mp3/yt2mp3.py').read(),
    M
).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="youtube-to-mp3",
    packages=["yt2mp3"],
    entry_points={
        "console_scripts": ['yt2mp3 = yt2mp3.yt2mp3:main']
    },
    version=version,
    description="Download YouTube videos or playlists as MP3 audio files from a url.",
    long_description=long_descr,
    author="cedricao",
    author_email="cedricao.noreply@gmail.com",
    url="https://github.com/cedricouellet/youtube-to-mp3.git"
)