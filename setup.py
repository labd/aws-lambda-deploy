from setuptools import find_packages, setup


with open('README.rst', 'r') as fh:
    description = '\n'.join(fh.readlines())


tests_require = [
    'moto>=1.3.4',
    'pytest>=3.5.1',
    'pytest-cov>=2.5.1',
    'pytest-click',
]


setup(
    name='aws-lambda-deploy',
    version='0.0.1',
    description=description,
    url='https://github.com/labd/aws-lambda-deploy',
    author="Michael van Tellingen",
    author_email="opensource@labdigital.nl",
    install_requires=[
        'boto3>=2.49.0,<3.0',
        'click>=7.1.2',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    py_modules=['aws_lambda_deploy'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': {
            'aws-lambda-deploy = aws_lambda_deploy:main'
        }
    },
    zip_safe=False,
)
