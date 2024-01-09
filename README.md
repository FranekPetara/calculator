# calculator
requirements:

1. docker
2. docker-compose
   
how to use:

1. In main folder run command:
docker-compose build
2. When build is done run by command:
docker-compose up
3. To use the application, enter into your browser
http://localhost:8080/

Author's comments

the application is based on vue.js and fastApi. Unfortunately, hot reload vue does not work in docker as it should, despite various configurations. I didn't write a classic architecture, but I tried an original approach with dynamic loading of endpoints. Adding endpoints works similarly to adding plagins to the application. Just add two files from the backend side and a new operation is added without interfering with the application code - details in files in the operations and schema folders. After completing this task, I see some points for improvement, but time is running out...
