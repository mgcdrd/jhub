# display_name, slug, default are own things
# profile_options allows for options to the user for things 
# Most modifications will go under kubespawner_override - even things inside profile_options
#
small_instance = {
  "display_name": "Small Instance",
  "slug":  "sm-instance",
  "default": False,
  "kubespawner_override":{
    "cpu_limit": 1,
    "mem_limit": '1G',
  },
  "profile_options": {
    "image": {
      "display_name": "Image",
      "choices": {
        "latest": {
          "display_name": "singleuser:latest",
          "kubespawner_override": {
            "image": "jupyterhub/singleuser:latest"
          }
        },
        "3.0": {
          "display_name": "singleuser:3.0",
          "kubespawner_override": {
            "image": "jupyterhub/singleuser:3.0"
          }
        }
      }
    }
  }
}

medium_instance = {
  "display_name": "Medium Instance",
  "slug":  "md-instance",
  "default": True,
  "kubespawner_override":{
    "cpu_limit": 2,
    "mem_limit": '1G',
    "volumes": [
      {
        "name": "ldap-mnt",
        "nfs": {
          "server": "nfsserver.LAB_DOMAIN",
          "path": "/nfs/containers/srv_data/rocky_pgsql/ldap/"
        }
      },
      {
        "name": "home-dirs",
        "nfs": {
          "server": "nfsserver.LAB_DOMAIN",
          "path": "/nfs/backups/desktop_backups/20220617/rocky_vm"
        }
      },
      {
        "name": "var-lib-sss",
        "hostPath": {
          "path": "/tmp/sss",
          "type": "DirectoryOrCreate"
        }
      }
    ],
    "volume_mounts": [
      {
        "name": "ldap-mnt",
        "mountPath": "/etc/ldap"
      },
      {
        "name": "home-dirs",
        "mountPath": "/home/provenzawt"
      },
      {
        "name": "var-lib-sss",
        "mountPath": "/var/lib/sss"
      }
    ]
  },
  "profile_options": {
    "image": {
      "display_name": "Image",
      "choices": {
        "latest": {
          "display_name": "singleuser:latest",
          "kubespawner_override": {
            "image": "registry.LAB_DOMAIN/forme/jhub-tensorflow:latest",
            "image_pull_policy": "Always"
          }
        },
        "3.0": {
          "display_name": "singleuser:3.0",
          "kubespawner_override": {
            "image": "registry.LAB_DOMAIN/forme/jhub-tensorflow:latest",
            "image_pull_policy": "Always"
          }
        }
      }
    }
  }
}