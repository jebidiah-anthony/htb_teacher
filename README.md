# HTB Teacher (10.10.10.153) Write-up

## PART 1 : Initial Recon

```console
nmap --min-rate 1000 -p- -v 10.10.10.153
```
```
PORT   STATE SERVICE
80/tcp open  http
```
```console
nmap -oN teacher.nmap -p 80 -sC -sV -v 10.10.10.153
```
```
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
| http-methods:
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Blackhat highschool
```
---

## PART 2 : Port Enumeration
