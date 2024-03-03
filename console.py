#!/usr/bin/python3

""" program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """Class : HBNHCOMMAND"""

    prompt = "(hbnb) "
    myclasses = ['BaseModel']

    def do_quit(self, inp):
        """handle quit input."""
        return True

    def do_EOF(self, inp):
        """handle EOF (Ctrl+D) input."""
        return True

    def help_quit(self):
        """Help command for quit input"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, args):
        if args is None or not args:
            print('** class name missing **')
        elif args not in HBNBCommand.myclasses:
            print('** class doesn\'t exist **')
        else:
            class_name = args
            cls = globals()[class_name]()
            print(cls.id)
            storage.save()

    def do_show(self, args):
        argss = args.split(' ')
        if len(argss) < 1 or not argss[0]:
            print('** class name missing **')
        elif argss[0] not in HBNBCommand.myclasses:
            print('** class doesn\'t exist **')
        elif len(argss) < 2 or not argss[1]:
            print('** instance id missing **')
        elif f"{argss[0]}.{argss[1]}" not in storage.all():
            print ('** no instance found **')
        else:
            print(storage.all()[f"{argss[0]}.{argss[1]}"])

    def do_destroy(self, args):
        argss = args.split(' ')
        if len(argss) < 1 or not argss[0]:
            print('** class name missing **')
        elif argss[0] not in HBNBCommand.myclasses:
            print('** class doesn\'t exist **')
        elif len(argss) < 2 or not argss[1]:
            print('** instance id missing **')
        elif f"{argss[0]}.{argss[1]}" not in storage.all():
            print ('** no instance found **')
        else:
            del storage.all()[f"{argss[0]}.{argss[1]}"]
            storage.save()

    def do_all(self, args):
        if len(args) < 1 or not args:
            lista = []
            for key, value in storage.all().items():
                lista.append(str(value))
            print(lista)
        elif args not in HBNBCommand.myclasses:
            print('** class doesn\'t exist **')
        else:
            lista2 = []
            for key, value in storage.all().items():
                keyy = key.split('.')
                if keyy[0] in key:
                    lista2.append(str(value))
            print(lista2)

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
