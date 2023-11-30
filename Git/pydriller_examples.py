from pydriller import Repository
import pprint
pp = pprint.PrettyPrinter()
    
def traverse_commits():
            """
    traverse_commits() allows us to walk through the commit history.
    """
    print_separator("traverse_commits")

    # for commit in Repository('https://github.com/jgraber/PythonFriday').traverse_commits():
    for commit in Repository('..\..\PythonFriday').traverse_commits():
        print(f"{commit.committer_date} - {commit.hash[0:8]} - {commit.author.name}")
        
    # Sample output:
    # 2021-10-21 22:33:00+02:00 - 1be83b81 - Johnny Graber
    # 2021-10-22 23:30:00+02:00 - c816a116 - Johnny Graber
    # 2021-10-23 23:15:00+02:00 - 4f379c7a - Johnny Graber
    # 2021-10-24 11:18:10+02:00 - 64ec912d - Johnny Graber
    # 2021-10-25 15:37:05+02:00 - 0a9b1109 - Johnny Graber

def traverse_commits_and_files():
    """
    traverse_commits() allows us to walk through the commit history.
    """
    print_separator("traverse_commits")
   
    # for commit in Repository('https://github.com/jgraber/PythonFriday').traverse_commits():
    for commit in Repository('..\..\PythonFriday').traverse_commits():
