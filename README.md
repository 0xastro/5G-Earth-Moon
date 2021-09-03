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


## BRIEF

In other words, as descriped above in the requirements. The wireless communication link should be established first by running the 5G network.

- Start the Core Network (EPC)
- Start the gNodeB
- Turn the UE on.

After successful random access and accordingly attach to the 5g network, the UE gets an IP from the S-PGW. The IP is permanent as long as the UE is attached to the network but dynamically allocated at run time by the core network.

<p align="center">
<img  src="https://github.com/astroa-git/5G-Earth-Moon/blob/main/fig2.png" alt="5G tunnel" class="inline"/>
</p>


A bi-directional communication should be established between the ROVER and the ROS controller. Accordingly, the rover will periodically send telemetry data to the ROS controller such as lidar point clouds, real-time video streaming, battery status, wheel pressures among many other information. On the other hand, the ROS controller should be able to control the rover through a keyboard, joystick or a haptic device.

To achieve a successful communication between the ROS controller and the ROVER, the communication should be routed and encapsulated through the 5G tunnel. This is achieved by updating the linux kernel routing table.

<p align="center">
<img  src="https://github.com/astroa-git/5G-Earth-Moon/blob/main/fig3.png" alt="E2E system" class="inline"/>
</p>
