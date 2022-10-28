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
  
  auth_state = yield spawner.user.get_auth_state()

  spawner.uid = int(auth_state['oauth_user']['uid'])
  spawner.gid = int(auth_state['oauth_user']['gid'])
  spawner.fs_gid = int(auth_state['oauth_user']['gid'])
  spawner.notbook_dir = auth_state['oauth_user']['home']
  spawner.working_dir = auth_state['oauth_user']['home']
  spawner.environment['NB_USER'] = auth_state['oauth_user']['preferred_username']
  spawner.environment['NB_UID'] = auth_state['oauth_user']['uid']
  spawner.environment['NB_GID'] = auth_state['oauth_user']['gid']
  spawner.environment['HOME'] = auth_state['oauth_user']['home']
  spawner.environment['USER'] = auth_state['oauth_user']['preferred_username']

  #some others that can be tested for security
  spawner.disable_user_config = False

#debug
def userdata_hook(spawner):
  #spawner.userdata = auth_state["userdata"]
  print(" ")