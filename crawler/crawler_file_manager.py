import os


# Each website is a separate project (folder)
def create_website_dir(directory):
    try:
        if not os.path.exists(directory):
            print('Creating directory ' + directory)
        os.makedirs(directory)
    except:
        print("Error: creating file")


def create_index_file(project_name, base_url):
    name = os.path.join(project_name, "content")
    print(name)
    if not os.path.isfile(name):
        
        write_file(name, "INDEXER\n")
def append_index_to_file(project_name, base_url, data):
    create_index_file(project_name, base_url)
    name = os.path.join(project_name, "content.txt")
    append_to_file(name, """
    {}:
    {}

    """.format(base_url, data))

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    try:
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
    except:
        print("Error: ")

    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")


def main():
    create_website_dir("example")


if __name__ == "__main__":
    main()
