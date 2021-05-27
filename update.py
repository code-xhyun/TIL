#!/usr/bin/env python

import os
import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))
nowDatetime = datetime.datetime.now().astimezone(
    tz=KST).strftime('%Y-%m-%d %H:%M:%S')

title = """# TIL

> :alien:Today I Learned:alien:


A collection of software engineering tips that I learn every day :fire:


"""


def main():
    content = ""
    count = 0
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        file_list = os.listdir(root)
        count += len(file_list)
        content += "### {}\n\n".format(category)

        for file in files:
            name = os.path.basename(file).split('.')[0]
        #     updateTime = datetime.datetime.fromtimestamp(
        #        os.path.getmtime(category+"/"+file)).strftime('%Y/%m/%d %H:%M')
            name = " ".join(word.capitalize() for word in name.split('-'))
            content += "- [{}]({})\n".format(name,
                                             os.path.join(category, file))
        content += "\n"

    meta = """TIL count : {}\n
Last Update Time: {} (KST) 

---
    """.format(
        str(count), nowDatetime)
    head = title+meta
    with open("README.md", "w") as fd:
        fd.write(head + "\n" + content)


if __name__ == "__main__":
    main()
