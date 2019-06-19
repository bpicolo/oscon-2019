protogen-python: venv
	./venv/bin/python -m grpc_tools.protoc -I . --python_out=./ --python_grpc_out=./ proto/*.proto

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

clean: clean-venv clean-generated

clean-venv:
	rm -rf venv

clean-generated:
	rm -rf proto/*.py
