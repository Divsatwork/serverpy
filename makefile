run-server:
	python3 servpy-runner.py -c test.json

ui-server:
	cd front_end && npm run dev

ui-build:
	cd front_end && npm install && npm build