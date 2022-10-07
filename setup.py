from distutils.core import setup

setup(
    name='ezlogging',
    version='1.0.0',
    description='An incredibly versatile yet simple logging system.',
    author='Parth Mittal',
    author_email='parth@thekoalaco.in',
    url='https://www.github.com/PrivatePandaCO/ezlogging',
    license='MIT',
    packages=['ezlogging'],
    install_requires=['rich'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Documentation": "https://github.com/PrivatePandaCO/ezlogging/blob/master/README.md",
        "Github": "https://github.com/PrivatePandaCO/ezlogging",
        "Changelog": "https://github.com/PrivatePandaCO/ezlogging/blob/master/Changelog.md"
    }
)
