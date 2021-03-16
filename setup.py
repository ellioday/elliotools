"""Set up files
"""

import setuptools

setuptools.setup(name="elliotools",
	version = "0.0.0",
	description = "Useful python functions",
	author = "Elliott Day",
	url = "https://github.com/ellioday/elliotools",
	packages = setuptools.find_packages(exclude=["test"]),
	classifiers = ["Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	],
	python_requires=">=3.6",
	install_requires=["numpy", "scipy", "matplotlib", "aacgmv2"],
)
