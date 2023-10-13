# Weekly Plans: Feb. 2nd, 2023

# Announcements
- National Cyber League codes will be distributed in the next few days. Once you've recieved your code, sign up at [National Cyber League - Registration](https://cyberskyline.com/events/ncl/welcome)
- [TracerFire Cyber Competition](https://www.acsac.org/2022/workshops/tracerfire/) (Feb. 17-19th) is a cybersecurity comeptition that TracerFIRE (Forensic and 
Incident Response Exercise) holds annually. The comeptition focuses heavily on blue-team cyber (foresnics, system and network administration/security,
reverse engineering, etc). Looking for 1 replacement
- If you've run out of PwnBox for this month, you can follow [this tutorial](https://github.com/hpu-code-club/cybersecurity/blob/main/guides/installing-openvpn.md) to install OpenVPN.

# HackTheBox Academy
[HackTheBox Academy](https://academy.hackthebox.com/) is the counterpart to HackTheBox labs, which we've been using over the past few weeks as hacking grounds. 
All of the labs, espcially the starting points, are based on the modules from HackTheBox academy. Because of that, we recommend signing up at [HackTheBox Academy - Register](https://academy.hackthebox.com/register).
Modules (groups of lessons) on Academy cost *cubes*, but every time you complete a module you'll be rewarded with cubes. Tier-0 modules refund the their cost in cubes
on completion, so you can complete all the tier 0 modules for free. You start out with 30 cubes - enough to buy 3 tier-0 modules at once. We recommend starting with
the following (in order):

| Module | Tier/Cost | Reason |
| ------ | ---- | ------ |
| [Setting Up](https://academy.hackthebox.com/course/preview/setting-up) | Tier 0, 10 cubes | Sets up the virtual machine environment and toolset |
| [Getting Started](https://academy.hackthebox.com/course/preview/getting-started) | Tier 0, 10 cubes | Learning basic tools, walkthrough of how to exploit a machine |
| [Introduction to Networking](https://academy.hackthebox.com/course/preview/introduction-to-networking) | Tier 0, 10 cubes | Basics of networking -- necessary for recon |

# HackTheBox Labs
This week's starting point machine is *Dancing*. In *Dancing*, you attempt to gain access to an unsecured [SMB](https://en.wikipedia.org/wiki/Server_Message_Block) 
service running on a Windows server. As always, you should first start by using [nmap](https://nmap.org/book/man.html#man-description) to scan the target server and
[determine the version of the software running on the server](https://nmap.org/book/man-version-detection.html). After identifying the service, use 
[smbclient](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html) to log into the shares (there is no password). For a step-by-step tutorial, 
to the `#walkthroughs` section of the [HPU Code Club Discord](https://discord.gg/7bD3jbDVRc).

Like the previous two exercises, this week focuses heavily on the reconnaissance portion of the [cyber kill chain](https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/cyber-kill-chain-seven-steps-cyberattack/). Every cyber attack begins with identifying potential attack vectors. In these earlier exercises, that
usually means running `nmap -sV IP_ADDR` to identify the version of the services running on the server. Once you've identified the vulnerable service, it's a matter of
exploiting it. Again, these earlier exercises will have intentionally weakly or misconfigured services that allow you to log in without a password.
