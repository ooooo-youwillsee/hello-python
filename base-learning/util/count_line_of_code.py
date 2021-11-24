import os

from sys import argv


def count_java(dir_name):
    if dir_name is None or len(dir_name) == 0:
        return 0
    total_count = 0
    for dir_path, dir_names, file_names in os.walk(dir_name):
        if dir_path.replace('\\', '/').find("src/test") >= 0:
            continue

        for file_name in file_names:
            if not file_name.endswith(".java"):
                continue
            read_file_name = os.path.join(dir_path, file_name)

            calc_enabled = True

            file_count = 0
            with open(read_file_name, encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) == 0 or line in {'{', '}', '(', ')'} or line.startswith("//") \
                            or line.startswith("package ") or line.startswith("import "):
                        continue
                    if line.startswith("/*"):
                        calc_enabled = False
                        continue
                    if line.endswith("*/"):
                        calc_enabled = True
                        continue
                    if calc_enabled:
                        file_count += 1
            total_count += file_count
            # print("file_name: %s, count: %d" % (read_file_name, file_count))
    return total_count


def count_go(dir_name):
    if dir_name is None or len(dir_name) == 0:
        return 0
    total_count = 0
    for dir_path, dir_names, file_names in os.walk(dir_name):
        if dir_path.find('vendor') >= 0:
            continue

        for file_name in file_names:
            if not file_name.endswith(".go") or file_name.endswith("_test.go"):
                continue
            read_file_name = os.path.join(dir_path, file_name)

            calc_enabled, import_enabled = True, False

            file_count = 0
            with open(read_file_name, encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()
                    if len(line) == 0 or line in {'{', '}', '(', ')'} or line.startswith("//") \
                            or line.startswith("package ") or line.startswith("var ("):
                        if import_enabled and line.endswith(")"):
                            import_enabled = False
                        continue
                    if line.startswith("/*"):
                        calc_enabled = False
                        continue
                    if line.endswith("*/"):
                        calc_enabled = True
                        continue
                    if line.startswith("import ("):
                        import_enabled = True
                        continue
                    if calc_enabled and not import_enabled:
                        file_count += 1
            total_count += file_count
            # print("file_name: %s, count: %d" % (read_file_name, file_count))
    return total_count


def check_argv(language_handlers, args):
    dir_name, language = args[1], args[2]
    if language not in language_handlers.keys():
        raise language + " 不支持"
    return dir_name, language


def register_handlers():
    language_handlers = dict()
    language_handlers["go"] = count_go
    language_handlers["java"] = count_java
    return language_handlers


def count_main(argv):
    language_handlers = register_handlers()
    dir_name, language = check_argv(language_handlers, argv)
    count = language_handlers[language](dir_name)
    print("dir: %s, count: %d" % (dir_name, count))
    return count


if __name__ == '__main__':
    count_main(['', 'C:/Users/ooooo/Development/Code/Demo/rocketmq', "java"])
    count_knative_serving = count_main(['', 'C:/Users/ooooo/Development/Code/Demo/knative-serving', "go"])
    count_knative_eventing = count_main(['', 'C:/Users/ooooo/Development/Code/Demo/knative-eventing', "go"])
    print("dir: %s, count: %d" % ('dir_name', count_knative_serving + count_knative_eventing))
