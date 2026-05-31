from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="loz-whook",
    version="0.1.0",
    author="MinhSangGD",
    author_email="minhsanggd@mscrew.io.vn",
    description="Thư viện monitor lỗi và custom log gửi về Discord Webhook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinhSangGD/loz-whook",
    license="MIT", 
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)