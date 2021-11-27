generate:
	python3 -m grpc_tools.protoc -I /proto --python_out=/proto \
         --grpc_python_out=/proto ../proto/bip44.proto


install:
	pip3 install -r requirements.txt