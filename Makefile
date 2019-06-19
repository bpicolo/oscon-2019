protogen: protogen-python protogen-ts

protogen-python: venv
	./venv/bin/python -m grpc_tools.protoc -I . --python_out=./ --python_grpc_out=./ proto/*.proto

protogen-ts:
	protoc \
		-I . \
		--plugin="protoc-gen-ts=./frontend/node_modules/.bin/protoc-gen-ts" \
		--js_out="import_style=commonjs,binary:./frontend/src/generated" \
		--ts_out="service=true:./frontend/src/generated" \
		proto/*.proto

venv:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

clean: clean-venv clean-generated

clean-venv:
	rm -rf venv

clean-generated:
	rm -rf proto/*.py
