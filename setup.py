from distutils.core import setup

setup(
    name='wtframework',
    version='0.0.5',
    author='David Lai',
    author_email='david@wiredrive.com',
    packages=['wtframework.wtf.wdtestobjects',
              'wtframework.wtf.config',
              'wtframework.wtf.email',
              'wtframework.wtf.utils',
              'wtframework.wtf.web',
              'wtframework.wtf.assettools',
              'wtframework.wtf',
              'wtframework',
              'wtframework.wtf._devtools_',
              'wtframework.wtf._devtools_.filetemplates',
              ],
    scripts=['bin/wtf_init.py', 'bin/wtf_tools.py'],
    url='https://github.com/wiredrive/wtframework',
    license='LICENSE.txt',
    description='WTF - Web Test Framework',
    long_description=open('README.md').read(),
    install_requires=[
        "Mox>=0.5.3",
        "nose>=1.2.1",
        "NoseXUnit>=0.3.3",
        "ddt>=0.2.0",
        "pyyaml>=3.10",
        "selenium>=2.29.0",
        "python-rest-client>=0.3",
    ],
)