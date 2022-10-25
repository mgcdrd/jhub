from tornado import gen
import profiles

@gen.coroutine
def get_profiles(spawner):

  print(vars(spawner))

  profiles = []

  profiles.append(profiles.small_instance)
  profiles.append(profiles.medium_instance)

  return profiles
