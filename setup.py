from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'pytest-tornasync',
    'mypy'
]

setup(
    name='kws_transformer',
    version='1.0.0rc0',
    author_email='anhquan.le52@gmail.com',
    description='KWS Audio Transformer',
    long_description=open('README.md').read(),
    python_requires='>=3.8',
    packages=find_packages("KWSTransformer/kws_transformer"),
    install_requires=[
        "kserve==0.8.0",
        "scipy"
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require}
)