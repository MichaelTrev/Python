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
