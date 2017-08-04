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
        print "usage: create_csv <base_path>"
        sys.exit(1)

    base_path = sys.argv[1]

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
            split_by_subjects(base_path)
        elif action_num == 2:
            remove_small_dirs(base_path)
        else:
            remove_small_dirs(base_path, True)

        cont = raw_input(
            "Would you like to continue? (y/n): "
        )
        if cont == "n":
            break
    print "\nThank you for using LFWcrop tools!"


def remove_small_dirs(base_path, reorder=False):
    # recieve size
    size = int(raw_input("Enter the size of directories you would like to keep:\n"))

    dirs = [
        d for d in os.listdir("%s/res" % base_path)
        if os.path.isdir("%s/res/%s" % (base_path, d))
    ]

    for d in dirs:
        if len(os.listdir("%s/res/%s" % (base_path, d))) < size:
            # remove directory
            shutil.rmtree("%s/res/%s" % (base_path, d))

    # reorderif necessary
    if reorder:
        reorder_dirs(base_path)


def reorder_dirs(base_path):
    # change all to - aXXXX (collision purposes)
    new_dirs = [
        d for d in os.listdir("%s/res" % base_path)
        if os.path.isdir("%s/res/%s" % (base_path, d))
    ]

    dir_num = 1
    for d in new_dirs:
        os.rename(
            "%s/res/%s" % (base_path, d),
            "%s/res/a%s" % (base_path, dir_num)
        )
        dir_num += 1

    # change back to sXXXX
    # change all to - aXXXX (collision purposes)
    new_dirs = [
        d for d in os.listdir("%s/res" % base_path)
        if os.path.isdir("%s/res/%s" % (base_path, d))
    ]

    for d in new_dirs:
        os.rename(
            "%s/res/%s" % (base_path, d),
            "%s/res/s%s" % (base_path, d[1:])
        )

def split_by_subjects(base_path):
    # first remove prev directory:
    try:
        shutil.rmtree("%s/res" % base_path)
    except OSError:
        pass

    # create new empty res
    try:
        os.mkdir("%s/res" % base_path)
    except OSError:
        pass

    # mapping of all the subjects to their subject number
    subjects = {}

    # all files in directory
    files = [
        f for f in os.listdir(base_path)
        if os.path.isfile("%s/%s" % (base_path, f))
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
            os.mkdir(
                "%s/res/s%s" % (
                    base_path,
                    subjects[subject_name]["number"]
                )
            )

        #either way, directory is created. Add new photo
        shutil.copyfile(
            "%s/%s" % (base_path, f),
            "%s/res/s%s/%s.pgm" % (
                base_path,
                subjects[subject_name]["number"],
                subjects[subject_name]["count"],
            )
        )
        subjects[subject_name]["count"] += 1


if __name__ == "__main__":
    main()
