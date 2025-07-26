from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyCypherLib",
    version="1.3.5",
    author="eaannist",
    author_email="your-email@example.com",
    description="Secure file encryption and decryption library with fluent API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PyCypher",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=3.0.0",
    ],
    keywords="encryption, decryption, cryptography, security, files",
)