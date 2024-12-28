from setuptools import setup, find_packages

setup(
    name="autochatgpt",
    version="1.0.0",
    description="Automated ChatGPT interaction framework with human-like behavior",
    author="Vibhek Soni",
    author_email="vibheksoni@engineer.com",
    url="https://github.com/vibheksoni/AutoChatgpt",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "undetected-chromedriver",
        "beautifulsoup4",
        "typing",
        "dataclasses",
        "schedule",
        "python-dotenv"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Testing :: Traffic Generation",
    ],
    python_requires=">=3.8",
)
