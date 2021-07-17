"""setup.py: setuptools control."""


from re import search, M
from setuptools import setup


version = search(
    '^__version__\s*=\s*"(.*)"',
    open('yturl2mp3/yturl2mp3.py').read(),
    M
).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="youtube-to-mp3",
    packages=["yturl2mp3"],
    entry_points={
        "console_scripts": ['yturl2mp3 = yturl2mp3.yturl2mp3:main']
    },
    version=version,
    description="Download YouTube videos or playlists as MP3 audio files from a url.",
    long_description=long_descr,
    long_description_content_type="text/markdown",
    author="cedricao",
    author_email="cedricao.noreply@gmail.com",
    url="https://github.com/cedricouellet/youtube-to-mp3.git"
)