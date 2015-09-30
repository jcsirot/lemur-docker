from setuptools import setup, find_packages

setup(
	name = "lemur_signbox", # https://www.python.org/dev/peps/pep-0426/#name
	version = "0.1.0", # https://www.python.org/dev/peps/pep-0440/
	packages = find_packages(),
	install_requires = [
		'requests==2.7.0',
		'Flask==0.10.1',
	],
	entry_points = {
        'lemur.plugins': [
            'signbox-issuer = lemur_signbox.plugin:SignboxIssuerPlugin'
        ]
    })
