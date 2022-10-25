from tornado import gen
import profiles

@gen.coroutine
def get_profiles(spawner):

  print(vars(spawner))

  profile_list = []

  profile_list.append(profiles.small_instance)
  profile_list.append(profiles.medium_instance)

  return profile_list
