help:
	@echo "---------------HELP-----------------"


install:
	@echo "---------------INSTALL-----------------"
	@pipenv --python 3.8
	pipenv shell
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	pytest test/test.py > result.txt
run:
	python3 app.py > result_py.txt
deploy:
	git add .
	git commit -m "make deploy commit"
	git push