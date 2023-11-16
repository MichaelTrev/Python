from pydriller import Repository
import pprint
pp = pprint.PrettyPrinter()
    
def traverse_commits():
            """
    traverse_commits() allows us to walk through the commit history.
    """
    print_separator("traverse_commits")

    # for commit in Repository('https://github.com/jgraber/PythonFriday').traverse_commits():
