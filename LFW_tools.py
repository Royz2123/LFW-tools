#!/usr/bin/env python

import shutil
import sys
import os

# This is a tiny script to help you creating a CSV file from a face
# database with a similar hierarchie:
#

SEPARATOR=";"
ACTION_DESC=(
    "1) Split into directories based on subject names\n"
    + "2) Remove all directories with less than n elements\n"
    + "3) Remove all directories with less than n elements"
    + ", and rename dirs so that their numbering is 1 ... n \n"
)

def main():
    if len(sys.argv) != 2:
        print "usage: create_csv <images_path>"
        sys.exit(1)

    images_path = sys.argv[1]

    print "Welcome! Here are a few scripts I offer for arranging LFW database.\n\n"

    while True:
        while True:
            action_num = int(raw_input(
                "Please choose an action:\n%s" % ACTION_DESC
            ))
            if action_num not in range(1, 4):
                print "Action number not supported!\n"
            else:
                break

        if action_num == 1:
            split_by_subjects(images_path)
        elif action_num == 2:
            remove_small_dirs(images_path)
        else:
            remove_small_dirs(images_path, True)

        cont = raw_input(
            "Would you like to continue? (y/n): "
        )
        if cont == "n":
            break
    print "\nThank you for using LFWcrop tools!"


def remove_small_dirs(images_path, reorder=False):
    # recieve size
    size = int(raw_input("Enter the size of directories you would like to keep:\n"))

    dirs = [
        d for d in os.listdir("res") if os.path.isdir("res/%s" % d)
    ]

    for d in dirs:
        if len(os.listdir("res/%s" % d)) < size:
            # remove directory
            shutil.rmtree("res/%s" % d)

    # reorderif necessary
    if reorder:
        reorder_dirs()


def reorder_dirs():
    # change all to - aXXXX (collision purposes)
    new_dirs = [
        d for d in os.listdir("res") if os.path.isdir("res/%s" % d)
    ]

    dir_num = 1
    for d in new_dirs:
        os.rename(
            "res/%s" % d,
            "res/a%s" % dir_num
        )
        dir_num += 1

    # change back to sXXXX
    # change all to - aXXXX (collision purposes)
    new_dirs = [
        d for d in os.listdir("res") if os.path.isdir("res/%s" % d)
    ]

    for d in new_dirs:
        os.rename(
            "res/%s" % d,
            "res/s%s" % d[1:]
        )

def split_by_subjects(images_path):
    # first remove prev directory:
    try:
        shutil.rmtree("res")
    except OSError:
        pass

    # create new empty res
    try:
        os.mkdir("res")
    except OSError:
        pass

    # mapping of all the subjects to their subject number
    subjects = {}

    # all files in directory
    files = [
        f for f in os.listdir(images_path)
        if os.path.isfile("%s/%s" % (images_path, f))
    ]

    # loop through all the files
    for f in files:
        subject_name = (f.replace('_', '', 1)).split('_')[0]

        # check if new subject
        if subject_name not in subjects.keys():
            # add to subjects
            subjects[subject_name] = {
                "number" : len(subjects.keys()),
                "count" : 1,
            }

            # create new directory
            os.mkdir("res/s%s" % subjects[subject_name]["number"])

        #either way, directory is created. Add new photo
        shutil.copyfile(
            "%s/%s" % (images_path, f),
            "res/s%s/%s.pgm" % (
                subjects[subject_name]["number"],
                subjects[subject_name]["count"],
            )
        )
        subjects[subject_name]["count"] += 1


if __name__ == "__main__":
    main()
