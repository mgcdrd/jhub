from tornado import gen
import profiles
from ldap3 import Server, Connection

#LDAP variables to be set to get my ldap gidNumber
LDAP_SERVER = 'ipa.lab.provenzawt.dev'
LDAP_USER =  'admin'
LDAP_PASSWD =  '11P@ssword12'
LDAP_GRP_NAME_ATTR = 'cn'
LDAP_DN = 'cn=groups,cn=accounts,dc=lab,dc=provenzawt,dc=dev'
LDAP_GID_ATTR = 'gidNumber'


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

  #spawner.supplemental_gids = get_ldap_groups(auth_state['oauth_user']['groups'])
  get_ldap_groups(auth_state['oauth_user']['groups']) #debug

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

def get_ldap_groups(GRP_LIST):
  return_list = []  
  
  server = Server(LDAP_SERVER, port=389, use_ssl=False)
  conn = Connection(server, user=LDAP_USER, password=LDAP_PASSWD)
  for grp in GRP_LIST:
    temp_string = "'(" + LDAP_GRP_NAME_ATTR + "=" + grp + ")'"
    conn.search(LDAP_DN, temp_string, attributes=[LDAP_GID_ATTR])
    print(conn.entries)
  
