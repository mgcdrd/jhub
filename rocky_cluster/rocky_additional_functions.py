from tornado import gen
import profiles
from ldap3 import Server, Connection

#LDAP variables to be set to get my ldap gidNumber
LDAP_SERVER = 'ipa.LAB_DOMAIN'
LDAP_GRP_NAME_ATTR = 'cn'
LDAP_DN = 'cn=groups,LDAP_DN_INFO'
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
  spawner.supplemental_gids = get_ldap_groups(auth_state['oauth_user']['groups'])
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


# Because my OIDC service doesn't have the LDAP group GIDs, we have to manually pull this.
#  This is the point of this function.  Since Jhub gets the group names, we can use those to get the GIDs to hand to the spawner
#  The parameter is assumed to be in a list, which is how the OIDC token gives it.
def get_ldap_groups(GRP_LIST):
  return_list = []

  server = Server(LDAP_SERVER, port=389, use_ssl=False)
  conn = Connection(server, auto_bind=True)
  for grp in GRP_LIST:
    conn.search(LDAP_DN, f'({LDAP_GRP_NAME_ATTR}={grp})' , attributes=[f'{LDAP_GID_ATTR}'])
    print(conn.entries)
    return_list.append(conn.entries[0][f'{LDAP_GID_ATTR}'].value)

  return return_list
