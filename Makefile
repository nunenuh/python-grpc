

proto-build-books:
	/usr/bin/mkdir -p ./fastapi-server/app/proto/books
	/usr/bin/mkdir -p ./grpc-server-books/app/services/books

	/usr/bin/touch ./fastapi-server/app/proto/books/__init__.py
	/usr/bin/touch ./grpc-server-books/app/services/books/__init__.py
	
	python3 -m grpc_tools.protoc -I ./protos --python_out=./fastapi-server/app/proto/books --grpc_python_out=./fastapi-server/app/proto/books ./protos/books.proto
	python3 -m grpc_tools.protoc -I ./protos --python_out=./grpc-server-books/app/services/books --grpc_python_out=./grpc-server-books/app/services/books ./protos/books.proto

	
proto-build-socials:
	/usr/bin/mkdir -p ./fastapi-server/app/proto/socials
	/usr/bin/mkdir -p ./grpc-server-socials/app/services/socials

	/usr/bin/touch ./fastapi-server/app/services/socials/__init__.py
	/usr/bin/touch ./grpc-server-socials/app/services/socials/__init__.py
	
	python3 -m grpc_tools.protoc -I ./protos --python_out=./fastapi-server/app/proto/socials --grpc_python_out=./fastapi-server/app/proto/socials ./protos/socials.proto
	python3 -m grpc_tools.protoc -I ./protos --python_out=./grpc-server-socials/app/services/socials --grpc_python_out=./grpc-server-socials/app/services/socials ./protos/socials.proto

	

