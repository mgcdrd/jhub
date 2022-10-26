from tornado import gen
import profiles

@gen.coroutine
def get_profiles(spawner):

  auth_state = yield spawner.user.get_auth_state()
  print(auth_state)
  profile_list = []
  profile_list.append(profiles.small_instance)
  
  if 'grp-jhub-admin' in auth_state['oauth_user']['groups']:
    profile_list.append(profiles.medium_instance)

  return profile_list


@gen.coroutine
def set_env(spawner):
  print(" ")
  #auth_state = yield spawner.user.get_auth_state()

  
  #spawner.uid = #the uid from the get__auth_state
  #supplemental_gids
  #gid



  #volumes #just like volumes on a pod
  #volume_mounts #just like volumeMounts on a pod
  #working_dir




#debug
def userdata_hook(spawner):
  spawner.userdata = auth_state["userdata"]
  #print(auth_state)