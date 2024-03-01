#!/usr/bin/python3

""" program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class : HBNHCOMMAND"""

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
