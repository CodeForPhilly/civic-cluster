# Team Machines

## TODO

- [ ] Block all inbound traffic on public IP so that only members of ZeroTier network can reach machines

## Setup

1. Generate and save a secure root password under the *Team Machines* collection at [bitwarden.phl.io](https://bitwarden.phl.io/)
2. Add a page to the *Team Machines* section of this book, documenting at least who the *Team Admin* is to start
   - The *Team Admin* should be a member of the team who is familiar with managing Linux systems and agrees to take responsibility for administering access for their teammates
3. Create a new Linode
   - Choose a Distribution: **Ubuntu 18.04 LTS**
   - Region: **Newark, NJ**
   - Linode Plan: **Standard > Linode 4GB** (2 CPUs)
   - Linode Label: `${team_name}.team-machine.phl.io`
   - Add Tags: **team-machine**
   - Root Password: *use password saved to BitWarden in step 1*
   - Backups: **no**
   - Private IP: **no**
4. Add an `A` record to [the `phl.io` zone](https://console.cloud.google.com/net-services/dns/zones/phl-io/rrsets/create?project=openphl-1177)
   - DNS Name: `${team_name}.team-machine`.phl.io
   - IPv4 Address: *copy from created Linode*
5. Add public SSH keys for the *Team Admin*

    ```bash
    mkdir ~/.ssh
    vim ~/.ssh/authorized_keys
    chmod 600 ~/.ssh/authorized_keys
    ```

6. Install Docker Engine from Docker's repository:

    ```bash
    # install prereqs for using repository
    apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common

    # add Docker's official GPG key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

    # add stable repository
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"

    # update package cache
    apt-get update

    # install Docker Engine
    apt-get install docker-ce docker-ce-cli containerd.io
    ```

7. Install ZeroTier and join `code-for-philly` network:

    ```bash
    curl -s https://install.zerotier.com | bash

    zerotier-cli join e5cd7a9e1c5330df
    ```

8. [Authorize machine to connect to ZeroTier network](https://my.zerotier.com/network/e5cd7a9e1c5330df) and label connection `${team_name}.team-machine.phl.io`
9. Verify Docker installation and machine reachability by starting nginx "hello world" container:

    ```bash
    docker run -p 80:80 -d nginxdemos/hello
    ```

10. Share `http://${team_name}.team-machine.phl.io/` link with *Team Admin*, showing nginx demo page and let them know they can destroy that container
