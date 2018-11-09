from random_forest import *

current_model = load_RF_File()


def main():
    user_input = input("What would you like to do? ")
    while(user_input != 'x'):
        if(user_input == "update-d"):
            update_default()
        if(user_input == "new"):
            user_input = input("Please enter a file name: ")
            build_proto_forest(user_input)
        user_input = input("What would you like to do? ")


def update_default():
    update_To_File(update_Random_Forest())


def build_proto_forest(model_path):
    partition = input("Partition Size: ")
    random_int = input("Random int seed (split): ")
    estimators = input("Number of Trees: ")
    criteria = input("gini or entropy: ")
    random = input("Random int seed (classifier): ")
    new_model = build_New_Forest(float(partition), int(random_int), int(estimators), criteria, int(random))
    to_save = input("Save y/n? ")
    if(to_save == 'y'):
        RF_To_File(new_model, model_path)
    return


main()