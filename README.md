AWS Domain Delegation
=====================

This script helps to automate the process of subdomain delegation between two AWS accounts.
One has the domain, and transfers the (DNS) management of it to the other account.

## Prerequisites

- python
- pipenv

## Usage

One timer:
```
pipenv install
```

Now execute:
```
$ pipenv run ./delegate --help

Usage: delegate [OPTIONS]

  Delegate the domain responsibility from the source account to the target
  account. The source account is hosting the zone of the (parent)domain. A
  subdomain entry will be created in this zone. In the target account, a
  zone for the (sub)domain will be created.  The nameserver of this (target)
  zone will be used in the source accounts subdomain entry.

  You need to run this with aws credentials for a role which can assume a
  role in the source and target account,  which is able to modify the
  route53 config.

Options:
  --domain TEXT           The full domain name you wanna host in the target
                          account.
  --source TEXT           The AWS Account with the parent domain.
  --target TEXT           AWS Account ID you want to delegate the domain to.
  -n, --dryrun            This will skip the real creation of resources
  -a, --assume-role TEXT  This role will be assumed in the accounts.
  --help                  Show this message and exit.
```

### Common usage


```
pipenv run ./delegate --domain my.example.org --source 123456789 --target 987654321
```

```
pipenv run ./delegate --domain my.example.org --source 123456789 --target 987654321 -a GenericDeploymentRole -n
```
