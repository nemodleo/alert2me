import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

version = '0.0.2'

setuptools.setup(
    name='alert2me',
    version=version,
    url='https://github.com/nemodleo/alert2me',
    author='Hyun Park',
    author_email='nemod.leo@snu.ac.kr',
    license='MIT',
    description='cli tool that alert to me.',
    keywords='alert slack cli',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    python_requires=">= 3.6",
    packages=setuptools.find_packages(),
    install_requires=[
        "slack-sdk>=3.17.2",
    ],
    include_package_data=True,
    zip_safe=False,
    package_data={'alert2me': ['alme']},
    script=['alert2me'],
    entry_points={
        "console_scripts": [
            "alme-configure = alert2me.configure:set_configure"
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ]
)