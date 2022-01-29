import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"Name":"Brian", "Age":30, "Hobby":["Guitar", "Baseball", "Coding"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()