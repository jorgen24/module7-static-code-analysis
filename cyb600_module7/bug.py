"""
Example file to show a SonarQube bug
"""


def unlock_the_locks():
    """
    Example showing a Sonar Bug
    :return: Locked or unlocked
    """


word1 = input("Input the first key: ")
word2 = input("Input the second key: ")

if word1 == "key1":
    if word2 == "key2":
        print("Unlocked!")
else:
    print("Access denied.")
