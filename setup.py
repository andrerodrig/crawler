from setuptools import setup, find_packages


def read(filename):
    return [
        line.strip() for line in open(filename).readlines()
    ]


setup(
    name="crawler",
    version="0.1.0",
    description="A simple application to collect data from correios site"
                "\nhttp://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm",
    packages=find_packages(),
    include_package_data=True,
    install_packages=read('requirements.txt'),
    extras_require={
        "dev": read('requirements_dev.txt')
    }
)
