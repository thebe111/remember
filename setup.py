import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="tb111-remember",
    version="1.0.0",
    description="Simple CLI flashcard system based on ANKI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gabriel Fonseca",
    author_email="fonsecacrz7@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keyords="python, flashcard, anki, monolothic, modular, ddd, clean architecture",
    python_requires=">=3.6, <4",
    url="https://gitlab.com/thebe111/remember",
    project_urls={
        "Issues": "https://gitlab.com/thebe111/remember/-/issues",
        "Source": "https://gitlab.com/thebe111/remember",
    },
)

