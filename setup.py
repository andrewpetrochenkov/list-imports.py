import setuptools

setuptools.setup(
    name='list-imports',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
