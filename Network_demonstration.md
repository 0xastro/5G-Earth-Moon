

## System Specifications

1. Machine 1 is a generic ubunutu workstation  which is connected via ethernet cable to Machine 2
2. Machine 2 is running OAI eNodeB and srsEPC
3. Machine 3 is running srsUE
4. Machine 4 is a generic ubuntu workstation that is connected to Machine 3 via Hotspot



## Network Parameters

| Network Interface | Machine 1      | Machine 2 (eNB)     | Machine 3 (UE)    | Machine 4     |
|-------------------|----------------|----------------|---------------|---------------|
| eno1              | 192.168.11.159 | 192.168.11.158 |               |               |
| srs_spgw_sgi      |                | 172.16.0.1     |               |               |
| wlp1              |                |                | 192.168.1.103 | 192.168.1.103 |
| tun_srsue         |                |                | 172.16.0.2    |               |


## Physical Topology

- Machine 1 and Machine 2 are connected via an Ethernet cable.
- Machine 3 and Machine 4 are connected using Hotspot Wi-Fi.
- Machine 2 and Machine 3 are conneced via LTE network.

## Execution Story 

1. Machine2: Start the EPC and eNB respecitvely 
2. Machine3: Start the UE 
3. Apply the network configuration as below


## Network Configuration and Routing Tables

> Common Configuration across all machines
All firewalls have been disabled, in addition to enabling the network forwarding

```
sysctl net.ipv4.conf.all.forwarding=1
ufw disable
systemctl disable firewalld.service
```

> Machine 1

```
route add default gw 192.168.11.159
```

> Machine 2

```
ip route add 192.168.1.103 via 172.16.0.1 dev srs_spgw_sgi
ip route add 192.168.1.102 via 172.16.0.1 dev srs_spgw_sgi
```

> Machine 3

```
ip route add 192.168.11.159 via 172.16.0.4 dev tun_srsue
ip route add 192.168.11.158 via 172.16.0.4 dev tun_srsue
```

> Machine 4

```
route add default gw 192.168.1.103
```

## Results:

- Successfull Ping: Machine 4 -> Machine 3 (UE) -> Machine 2 (eNB) -> Machine 1
- Failure: Machine 1 -> Machine 2 -> Machine 3 -> Machine 4

## Point of failure

```
ping -I 172.16.0.1 172.16.0.4
## Works: eNB to UE

ping -I 172.16.0.1 192.168.1.103
## Doesn't work: eNB to a physical private IP on the UE machine

```
