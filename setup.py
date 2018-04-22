from setuptools import setup

setup(
    name='specsavers',
    packages=['specsavers'],
    version='1.0',
    description='A Python wrapper around the Specsavers appointment booking API',
    author='Alex Ward',
    author_email='alxwrd@googlemail.com',
    url='https://github.com/alxwrd/specsavers',
    long_description=open('README.md').read(),
    install_requires=['requests', 'maya', 'requests-html'],
    license='MIT',
    python_requires='>=3.6',
)
