# Ansible Role: local-users

This is an Ansible role to create and potentially configure a local user.

I prefer to pass the variables "into" the role from the playbook versus by
including variable files.  This is because I hope to make the role usable by
other projects/roles.  I don't know if this logic makes sense or not, but I am
essentially attempting to remove the variables from the role itself.

## Important Notes

* Creating a user is very simple, so this role is probably overkill

## Requirements

Any package or additional repository requirements will be addressed in the role.

## Role Variables

All of these variables should be considered **optional** however, be aware that
sanity checking is minimal (if at all):

* `users` *ideally you could create/configure multiple users, and this
          nested list of users allows for that*
  * `username`
    * this is the username on the OS *(if this isn't provided, nothing will
      happen, which sounds like it is required)*
  * `fullname`
    * this is technically the *GECOS* field and the username will be used if
      `fullname` is not provided
  * `sudoer`
    * if this is set and is **true** then `username` will be granted
      passwordless sudo privileges
  * `create_dirs`
    * this is a ***list*** of directories to create in the home directory of
      the new user (I added this because I always put git work in a ~/GIT
      directory and this seemed like the appropriate place for that)

## Example Playbook

Playbook with various options specified:

```yaml
- hosts: localhost
  connection: local
  roles:
    - role: ansible-role-local-user
      users:
        - username: user_full_sudoer_dirs
          fullname: "Full Sudoer Dirs"
          sudoer: true
          create_dirs:
            - GIT
            - BACKUP
        - username: user_sudoer_dirs
          sudoer: true
          create_dirs:
            - PERSONAL
        - username: user_full_dirs
          fullname: "Full Dirs"
          create_dirs:
            - newdir
        - username: user_nothing
```

## Inclusion

I envision this role being included in a larger project through the use of a
`requirements.yml` file.  So here is an example of what you would need in your
file:

```yaml
# get the local-user role from github
- src: https://github.com/thisdwhitley/ansible-role-local-user.git
  scm: git
  name: local-user
```

Have the above in a `requirements.yml` file for your project would then allow
you to "install" it (prior to use in some sort of setup script?) with:

```bash
ansible-galaxy install -p ./roles -r requirements.yml
```

## Testing

I am relying heavily on the work by Jeff Geerling in using molecule for testing
this role.  I have, however, modified the tests to make them specific to what I
am attempting to accomplish but this could still use some work.

Please review those files, but here is a list of OSes currently being tested 
(using geerlingguy's container images):

* centos6
* centos7
* fedora27
* fedora28
* fedora29
* ubuntu14
* ubuntu16
* ubuntu18
* debian8
* debian9

### Note

At this point I am **ONLY** testing to ensure that the user is created and not
that the other variables are doing what they should.  I have tested this
manually and am pleased with the results, but I need to figure out how to make
this work with `testinfra` or some other way...

## To-do

* test all the aspects automatically, not just the creation of the user

## References

* [How I test Ansible configuration on 7 different OSes with Docker](https://www.jeffgeerling.com/blog/2018/how-i-test-ansible-configuration-on-7-different-oses-docker)

## License

All parts of this project are made available under the terms of the [MIT
License](LICENSE).
