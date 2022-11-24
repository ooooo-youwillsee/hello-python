import os

target_dir = 'C:/Users/ooooo/Desktop/test/aliyun-gradle'
repository_id = '3rd_sync'
url = 'http://maven.cairenhui.com/nexus/content/repositories/3rd_sync/'
mvn_cmd = "mvn deploy:deploy-file -DrepositoryId=%s -Durl=%s" % (repository_id, url)


def execute_cmd(cmd):
    print("executing cmd %s" % cmd)
    # os.system(cmd)


def upload_jar(jar_dir, group, artifact, version):
    jar_files, classifier_files, pom_files, = [], {}, []
    for random_id in os.listdir(jar_dir):
        for file_name in os.listdir(jar_dir + '/' + random_id):
            path = jar_dir + '/' + random_id + '/' + file_name
            if '.pom' in file_name:
                pom_files.append(path)
            elif '.jar' in file_name:
                classifier = file_name.replace("%s-%s" % (artifact, version), '').replace(".jar", '')[1:]
                if classifier == '':
                    jar_files.append(path)
                    continue
                classifier_files[classifier] = path

    cmd = mvn_cmd

    if len(jar_files) == 0:
        jar_files.append(classifier_files.values()[0])

    if len(jar_files) == 1:
        cmd += " -Dfile=%s -Dpackaging=jar" % jar_files[0]

    if len(classifier_files) > 0:
        cmd += " -Dfiles=%s" % (','.join(classifier_files.values()))

    if len(pom_files) == 1:
        cmd += " -DpomFile=%s " % (pom_files[0])

    execute_cmd(cmd)


def travel(path):
    for group in os.listdir(path):
        for artifact in os.listdir(path + '/' + group):
            for version in os.listdir(path + '/' + group + '/' + artifact):
                upload_jar(path + '/' + group + '/' + artifact + '/' + version, group, artifact, version)


if __name__ == '__main__':
    # file-2.1
    path = target_dir + "/caches/modules-2/files-2.1"
    travel(path)
