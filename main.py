from tkinter import *
import argparse
from src.backup import BackupSystem

def desktop_app():
    root = Tk()
    root.title("Gestion des sauvegardes")

    # Création des champs de saisie et des boutons
    Label(root, text="Source:").grid(row=0, column=0)
    source_entry = Entry(root)
    source_entry.grid(row=0, column=1)

    Label(root, text="Destination:").grid(row=1, column=0)
    destination_entry = Entry(root)
    destination_entry.grid(row=1, column=1)

    transfer_button = Button(root, text="Transférer")
    transfer_button.grid(row=2, column=0)

    copy_button = Button(root, text="Copier")
    copy_button.grid(row=2, column=1)

    status_label = Label(root, text="")
    status_label.grid(row=4, columnspan=2)

    root.mainloop()

def main():
    # Définition du parser
    parser = argparse.ArgumentParser(description='Backup management')

    # Ajout d'un argument positionnel
    parser.add_argument('gui', const=True, nargs="?", default=False, help='Start GUI mode ')
    parser.add_argument('-m', const=True, nargs="?", default=False, help='Move source to destination ')
    parser.add_argument('-c', const=True, nargs="?", default=False, help='Copy source to destination ')
    parser.add_argument('-s', type=str, nargs="?", default=False, help='Add source directory')
    parser.add_argument('-d', type=str, nargs="?", default=False, help='Add destination directory')

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    if not any(vars(args).values()):
        desktop_app()
        return

    if args.m is None and args.c is None:
        print('You must be identified if you want copy or move')

    if args.s is None and args.d is None:
        print("You haven't specified source or destination")
    else:
        if args.m:
            move = BackupSystem()
            move.set_name('MoveSystem')
            move.set_source(args.s)
            move.set_destination(args.d)
            print(move.move_exec())
        elif args.c:
            copy = BackupSystem()
            copy.set_name('CopySystem')
            copy.set_source(args.s)
            copy.set_destination(args.d)
            print(copy.copy_exec())
        elif args.gui:
            desktop_app()
        else:
            raise ValueError('Something is missing!')


if __name__ == '__main__':
    main()
