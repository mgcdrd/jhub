from tornado import gen
import profiles

@gen.coroutine
def get_profiles(spawner):

  #print(vars(spawner))

  profile_list = []

  profile_list.append(profiles.small_instance)
  profile_list.append(profiles.medium_instance)

  return profile_list

#debug
def print_auth_hook(authenticator, handler, authentication):
  print(vars(authenticator))
  return authentication

#debug
def userdata_hook(spawner, auth_state):
  print(vars(auth_state))
  spawner.userdata = auth_state["userdata"]