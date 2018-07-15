from setuptools import setup

setup(
    name='lp-rest-kernel',
    version='1.0.0',
    author='Infrabel Linux Team',
    author_email='linux@infrabel.be',
    packages=[
        'lp_rest_kernel',
        'lp_rest_kernel.rest'
    ],
    install_requires=[
        'requests',
        'flask',
        'urllib3',
        'redis',
        'lp_api_kernel',
        'werkzeug'
    ],
    url='https://git.msnet.railb.be/linux-infrastructure/lp-rest-kernel',
    license='Apache',
    description='Basic REST kernel.'
)
