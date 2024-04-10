from tkinter import *
import argparse
from backup import BackupSystem


def main():
    # Définition du parser
    parser = argparse.ArgumentParser(description='Backup management')

    # Ajout d'un argument positionnel
    parser.add_argument('-m', type=str, help='Move source to destination ')
    parser.add_argument('-c', type=str, help='Copy source to destination ')
    parser.add_argument('-s', type=str, help='Add source directory')
    parser.add_argument('-d', type=str, help='Add destination directory')

    # Analyser les arguments de la ligne de commande
    args = parser.parse_args()

    if args.m is None and args.c is None:
        raise ValueError('You must be identified if you want copy or move')

    if args.s is None and args.d is None:
        raise ValueError("You haven't specified source or destination")
    else:
        if args.m:
            move = BackupSystem()
            move.set_name('MoveSystem')
            move.set_source(args.s)
            move.set_destination(args.d)
            move.move_exec()
        elif args.c:
            copy = BackupSystem()
            copy.set_name('CopySystem')
            copy.set_source(args.s)
            copy.set_destination(args.d)
            copy.copy_exec()
        else:
            raise ValueError('Something is missing!')


if __name__ == '__main__':
    main()
