"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.
"""



class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None or user is None:
        return False
    # want to avoid a cycle, of a deeply nested sub group contains a parent
    # group then the recursion would never end
    explored = set()
    return is_user_in_group_recursive(user, group, explored)

    #if user in group.get_users():
    #   return True
    #else:
    #   for g in group.get_groups():
    #       if is_user_in_group(user, g):
    #           return True
    #return False

def is_user_in_group_recursive(user, group, explored):
    if user in group.get_users():
        return True
    else:
        for sub_group in group.get_groups():
            name = group.get_name()
            # for testing loops
            #if name in explored:
            #    print(name)
            if name not in explored:
                explored.add(name)
                if is_user_in_group_recursive(user, sub_group, explored):
                    return True
    return False
            
print("Test 1")
print(is_user_in_group(sub_child_user, parent))
# expect True

print("Test 2")
print(is_user_in_group("not_a_user", parent))
# expect False

# test that recursive step ends
print("Test 3")
sub_child.add_group(parent)
print(is_user_in_group("not_a_user", parent))
# expect False

print("Test 4")
print(is_user_in_group(sub_child_user, None))
# expect None


print("Test 5")
print(is_user_in_group(None, parent))

