from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Blockthon",
    version="2.4.6",
    author="Pymmdrza",
    author_email="Pymmdrza@gmail.com",
    description="Blockthon: Fast and easy generation of Private Keys and Mnemonics, converting Seed, Binary, and Decimal.",
    keywords=['blockthon','bitcoin', 'ethereum', 'tron', 'dogecoin', 'dash', 'qtum', 'litecoin', 'bitcoingold', 'wallet', 'private key', 'mnemonic', 'seed', 'binary', 'hex', 'hunter', 'compress', 'un compress', 'compress address', 'un compress address'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blockthon/Blockthon",
    project_urls={
        "Documentation": "https://mmdrza.gitbook.io/blockthon/",
        "Personal Website": "https://mmdrza.com",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bit==0.8.0',
        'hdwallet==2.2.1',
        'requests==2.28.2',
        'requests-html==0.10.0',
        'ecdsa==0.18.0',
        'bip-utils==2.7.1',
        'bip32utils==0.3.post4',
        'pycryptodome==3.18.0',
        'pbkdf2==1.3',
        'base58==2.1.1'
    ],
)
