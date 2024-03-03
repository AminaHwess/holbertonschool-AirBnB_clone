<p align="center">
  <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fgithub.com%2Fyeungegs%2FAirBnB_clone&psig=AOvVaw0Ql1TXq9NIvW7KvVkavhTi&ust=1709568476301000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMD_rf-82IQDFQAAAAAdAAAAABAD" alt="HolbertonBnB logo">
</p>


<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone.</p>

## Description :label:
Embarking on the creation of your initial web application, the AirBnB clone, marks the foundational stride. Its significance lies in the fact that what you construct in this phase will serve as a cornerstone for subsequent projects, encompassing HTML/CSS templating, database storage, API utilization, and front-end integration.


## Project Overall Objectives

* Creating a Python package
* Developing a command interpreter in Python utilizing the cmd module
* Understanding Unit testing and implementing it in large projects
* Serialization and deserialization of a Class
* Writing and reading a JSON file
* Managing datetime effectively
* Exploring UUID (Universally Unique Identifier)
* Grasping the concept of *args and its application
* Understanding **kwargs and its usage
* Proficiently handling named arguments in a function

# Prerequisites 

Python3.4+ has to be installed if you desire to use the console:
```
sudo apt-get install python3
```

# Installation

To have access to the console use the following command:

```
git clone https://github.com/AminaHwess/holbertonschool-AirBnB_clone.git ; cd holbertonschool-AirBnB_clone
```

# Run

If you want to execute the console use:

```
python3 console.py
```
or
```
./console.py
```

## Usage 💻

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` 

## How to use the console

The console serves the purpose of facilitating the creation, display, deletion, saving, and updating of all desired classes. It provides the flexibility to initiate and terminate processes as needed, enabling experimentation with file storage for testing preferences. To utilize the console, follow this brief guide using the "console.py" file:

```
AirBnB_clone$ ./console.py
(hbnb) 
(hbnb) all
[]
```

To initiate the console, simply input "./console.py". The console will prompt "(hbnb)". If you type "all" without creating a BaseModel (new class), empty brackets will be displayed in the terminal. However, errors will occur if class names and instances do not exist, as shown in the example below:

```
(hbnb) all hands
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 3695
** no instance found **
```

To create a new User:

```
(hbnb) create User
57b7009e-30c8-4084-9968-a7309c673e4e
(hbnb) all User
["[User] (57b7009e-30c8-4084-9968-a7309c673e4e) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164392), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 27, 164366), 'last_name': '', 'password': '', 'id': '1bab8a19-a0c7-43ef-956b-b3271bdd684f', 'first_name': ''}"]
```

To show a specific User, you'll have to use the "show" command. The show command takes in two arguments - name and id. 

```
(hbnb) show User 18a48e8f-d3a0-437e-8556-74bfcff6b696
[User] (777f8007-5aeb-4568-8334-807d507edce0) {'updated_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114711), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 18, 21, 59, 114685), 'last_name': '', 'password': '', 'id': '777f8007-5aeb-4568-8334-807d507edce0', 'first_name': ''}
```

To destroy a User, use the "destroy" command. The command takes in two arguments - name and id. When successfully implemented, destroy will delete the User from file storage. Please see example below:

```
(hbnb) create User
18a48e8f-d3a0-437e-8556-74bfcff6b696
(hbnb) show User 18a48e8f-d3a0-437e-8556-74bfcff6b696
[User] (18a48e8f-d3a0-437e-8556-74bfcff6b696) {'id': '06505348-0c86-4273-b1c2-68eefcbbab0c', 'last_name': '', 'updated_at': datetime.datetime(2017, 10, 4, 19, 18, 40, 976205), 'email': '', 'created_at': datetime.datetime(2017, 10, 4, 19, 18, 40, 976174), 'password': '', 'first_name': ''}
(hbnb) destroy User 18a48e8f-d3a0-437e-8556-74bfcff6b696
(hbnb) show User 18a48e8f-d3a0-437e-8556-74bfcff6b696
** no instance found **
```

The "all" command prints all string representation of all instances and the "update" command is used to update the User information. In the example below, the first name is updated to "Amina". Everything can be updated except the id, created and updated datetime.

```
(hbnb) update BaseModel d910f04d-454a-4500-a156-d6918933c584 first_name "Amina"
(hbnb) show BaseModel d910f04d-454a-4500-a156-d6918933c584
[BaseModel] (d910f04d-454a-4500-a156-d6918933c584) {'first_name': 'Amina', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```



## Authors :black_nib:
Amina Hwess <https://github.com/AminaHwess>
Saif Chaari <https://github.com/sachihiroo/>
