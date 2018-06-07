###Airbnb Clone

![hobnob](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20180607%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180607T203101Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5f1add52ce276305456ba409d476fff768b4fe2950ff854577e62449e1f89bd9 "hobnob")](http://https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJIMMWEC6CH2PXSCQ%2F20180607%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180607T203101Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5f1add52ce276305456ba409d476fff768b4fe2950ff854577e62449e1f89bd9 "hobnob")


Clone of Airbnb Website

Command Module 
Manages the objects of the project. Capabilities include:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

####Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```