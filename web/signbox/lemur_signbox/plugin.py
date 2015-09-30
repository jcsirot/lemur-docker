import lemur_signbox
from lemur.plugins.bases.issuer import IssuerPlugin
import requests
import json

from flask import current_app

class SignboxIssuerPlugin(IssuerPlugin):
	title = 'signbox'
	slug = 'signbox-issuer'
	description = 'Enables the creation of certificates with SignBox'
	version = lemur_signbox.VERSION

	author = 'Jean-Christophe Sirot'
	author_url = 'https://github.com/jcsirot'

	def create_authority(self, options):
		role = {'username': '', 'password': '', 'name': 'signbox'}
		return SIGNBOX_ROOT, "", [role]

	def create_certificate(self, csr, options):
		url = "http://signbox:9090/certificate/enroll"
		r1 = requests.post(url, data=csr)
		options["authority"] = None
		r2 = requests.post(url, json=options)
		current_app.logger.info("Requesting a new SignBox certificate: {0}".format(options))
		return None

SIGNBOX_ROOT = """-----BEGIN CERTIFICATE-----
MIIFYjCCA0qgAwIBAgIUQlbGpm+hdR7A4zSgGfVh21q/tVAwDQYJKoZIhvcNAQEL
BQAwSTELMAkGA1UEBhMCRlIxCzAJBgNVBAsTAlFBMQ8wDQYDVQQKEwZBcmtlbmEx
HDAaBgNVBAMTE0Fya2VuYSBRQSBSb290IENBIDEwHhcNMTUwODMxMjIwMDAwWhcN
MjUwOTI5MjIwMDAwWjBJMQswCQYDVQQGEwJGUjELMAkGA1UECxMCUUExDzANBgNV
BAoTBkFya2VuYTEcMBoGA1UEAxMTQXJrZW5hIFFBIFJvb3QgQ0EgMTCCAiIwDQYJ
KoZIhvcNAQEBBQADggIPADCCAgoCggIBAI6e5+8T8FK3aHE/LSqK+v/VnLcDaFE6
PgLkDMTb0umj6JctHEkE0eXAD5w9vAkTRAsn5ViyjlJlpT2daRp0XanXK7GDA9jA
5jdkNbcl9dufKYbtRopsytoVZUbyhK7BtjfGGnL04Irnm8NZrxA+LSt6As2lvoge
i3RVaSS9h80g6hkfuw8MHNrqxN0rVdFrBUk9fmsYSJE++VXZGxn8+bG6YVx43Psl
1pVTJvsNPwKlh4ZeZICZu0rXavMUIrUuA7ybUpiTSRMS4JfL2gugTeYuTGjPaigK
qm7jCMDcQq3oLXpWe60xC14wpE2whbBTmtOs6DS/bfAhOsLRWceGskWXwpWwJ74H
4OueJ+ZWEgUomW6nj9xumQKESd3ykFZo1k3xJtklu/+NxU5G7gn0ozzdUrjtF/kH
Q4WHwRjqnjYfWu8J5bGayyyoEAFWwwXOR7xQvzs3/qScjfXgYVQD4sRTNqWFaq++
pobTw+Olth5aSiQx66iLi+xmBlMgLt78GON1mnW/jQTYNgCEdl+vuOqWtLBWrfmp
H/mV0OeelWPneG2qI0EzpweZnJxFpNYvkPaKGdn7JthQOyNR8yoNH/QB/24TG3hk
GLkLAVjntSdHFvwiMeVVtxSbG09lWwt5kkARr06Dw4AGXuBj084DlzvhMmM/ALex
qtWR7uo3PeElAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUbooI
Mr8I1t/dQPJ7PTgm5GAmEk0wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsF
AAOCAgEAGE12bfbJMSYWt16Og+c9EhegpLeNgsF50l6KGcyWS4jRGG68b/wCw256
jJd73rFYnGlFMLgwKh4+pXUr1/xi94FeMAn/8gm3Zqxrfx4DSHNg6te1VdWUIcJF
jMVL9771sb5mTFnjzMuEqLgecJCGJBW1M5MeUlcA/sDUGIhw4SdEFmjr+B+djgrp
eqtw29EaLefDK72zhHNRXHcsTA0dx9VqmNltLJek9q31tP/7dUt/W0SfZ/0XJB3W
7osx2U8zTNqeeau77P0npM/mMmm6MazRVb1WeYQzVYWQExnfduCJCQEhMa7QQcVa
B3ssWmAsax7rUcUvnchF/etUcDPIYFKaTdh8CNtbbMuExEpYcMnFWvx+qLQSCgxI
b6v1Af1FBk5T3ZPvSsQVf21hWlgpO5cyREP/UD6YKDbeyP5toaZ0nEUNB5BvtdX/
2lBDJfpsRRuPCG/HSFx+TH6BhMIaS2XJs7EBglRdYrJpY8GYpzXUOaoa824aRFJ/
JbCyOXyAPRMXN+NM5juYrTW69wovgHtlKM/7FvcWVT8PtWMdoikG3GYN/DukRre3
2UxbnAVm2gWkYc/AiSPpd/JAeVtc8jpHzY8jqp9Q0oA7ccd6FSK4seC/DuAdoAzd
jX+OyF4TQY/uX+kDCxy+kGSsUMAnUMcmLC3Lwlz922xDu9GEDn4=
-----END CERTIFICATE-----"""
