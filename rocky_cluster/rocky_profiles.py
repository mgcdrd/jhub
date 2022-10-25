# display_name, slug, default are own things
# profile_options allows for options to the user for things 
# Most modifications will go under kubespawner_override - even things inside profile_options
#
small_instance = {
  "display_name": "Small Instance",
  "slug":  "sm-instance",
  "default": True,
  "kubespawner_override":{
    "cpu_limit": 1,
    "mem_limit": '512M',
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