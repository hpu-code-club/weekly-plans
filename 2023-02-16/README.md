# February 16th, 2023

# Announcments 
- [CyberSEED 2023](https://cyberskyline.com/events/cyberseed) (Mar 4, 10am - 5pm EST)
- [US Cyber Challenge 2023](https://app.joinhandshake.com/stu/events/1241482) (Feb 19, 6:00 am - Mar 12, 10:55 pm)

# Ports and Services
When a company wants to host a service like a website or SSH server, they have to expose it to the internet through a *socket*. A socket is a combination of an IP
address (like 127.0.0.1) and a port (0-65535). Given an ip address, you can scan the ports on the server to determine the services running on those ports. The first
1000 ports are unofficially reserved for commonly-used services like HTTP (80), HTTPS (443), and SSH (22).

Reconnaisance is arguably one of the most important steps in the [cyber kill chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html) as it 
allows you discover attack vectors (services that could be exploited) and gain a foothold.

# An Introduction to *Nmap*
[_Nmap_](https://nmap.org/book/man.html#man-description), short for '_network mapper_', is "an open source tool for network exploration and security auditing. It was 
designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on 
the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet
filters/firewalls are in use, and dozens of other characteristics. While Nmap is commonly used for security audits, many systems and network administrators find it useful 
for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime." -Nmap Docs Chapter 15, [_Nmap Reference Guide_](https://nmap.org/book/man.html#man-description)

Although you can use Nmap without really understanding [networking protocols](https://www.cloudflare.com/learning/network-layer/what-is-a-protocol/), I highly recommend 
learning about at least [TCP](https://www.techtarget.com/searchnetworking/definition/TCP) and [UDP](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/) protocols.
