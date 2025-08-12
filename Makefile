
.PHONY: run test

run:
	cd src && python3 -m triangulator.cli ../data/example_case.json

test:
	pytest -q

cd src
python3 -m triangulator.cli ../data/example_case.json

