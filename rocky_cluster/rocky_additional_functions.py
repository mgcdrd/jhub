from tornado import gen
import profiles

@gen.coroutine
def get_profiles(spawner):

  print(vars(spawner.user.oauth_user.groups))

  profile_list = []
  profile_list.append(profiles.small_instance)
  profile_list.append(profiles.medium_instance)

  return profile_list


#debug
def userdata_hook(spawner, auth_state):
  #print(auth_state)
  spawner.userdata = auth_state["userdata"]