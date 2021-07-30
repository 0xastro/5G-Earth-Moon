# 5G-Earth-Moon
5G Earth-Moon mission Networking Setup and Requirements

| Facility | Description | IP |
| --- | --- | --- | 
| `SATCOM` | Contains the 5G base-station **gNodeB** and **Amplifiers(PA/LNA)** | 10.10.10.3 |
| `LUNA` | Contains the **ROS Controller**, the **Rover** and the User Equibment **UE**  | 10.10.10.2 |
| `CDF` | Interconnect SATCOM and LUNA | 10.10.10.1 |

<p align="center">
<img  src="https://github.com/astroa-git/5G-Earth-Moon/blob/main/fig1.jpg" alt="system architicture" class="inline"/>
</p>


## Procedures and Requirements

### Req1

Start **Core Network**. The connected UE which is mounted on top of the rover will be assigned an IP in this network `172.16.0.1`

### Req2

Start **gNodeB**. The base-station will establish a connection with the corresponding core network. Therefore, it start broadcasting the network information.

### Req3

Start **UE**. The UE mounted on the rover should be able to syncronize and attach to the corresponding **gNodeB**

### Req4

Setup an **E2E** Network tunnel in the following order. ROS controller, Rover, gNodeB, and UE.

### Req5

ROS controller should connect to the ROVER over the 5G Tunnel. Additionally, It should recieve near real-time telemetry data and control the rover.
