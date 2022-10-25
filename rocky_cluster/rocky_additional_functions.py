from tornado import gen

@gen.coroutine
def get_profiles(spawner):

  print(vars(spawner))

  profiles = []

  profiles.append(small_instance)
  profiles.append(medium_instance)

  return profiles

c.KubeSpawner.profile_list = get_profiles
