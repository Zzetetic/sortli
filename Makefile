.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

venv:
	$(python) -m venv --prompt '|> sortli <| ' env
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo
	@echo "venv Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	@PYTHONPATH=PYTHONPATH:$(shell pwd)/sort python3 -m unittest \
		-v \
		$(arg)

docker: clean
	docker build -t sort:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
