ifeq ($(OS),Windows_NT)

    install:
        pip install -r requirements.txt

else

    install:
        pip3 install -r requirements.txt


endif
