from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vastcap',
    version='1.0.1',
    packages=find_packages(),
    description='VastCap Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='vastien',
    author_email='contact@vast.sh',
    license='MIT',
    url='https://github.com/vastien/vastcap-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
