from setuptools import setup, find_packages

setup(
    name="allicia-rocha-calculadora",
    version="0.1.0",
    author="Allicia Rocha",
    description="Uma API de calculadora simples com FastAPI",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)