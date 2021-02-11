import setuptools

NAME = "ppmpmessage"

DEPENDENCIES_ARTIFACTORY = [
    'unide-python',
    'jsonpickle',
    'getmac'
]
DEPENDENCIES_GITHUB = [
]


def generate_pip_links_from_https(url, credentials):
    """ Generate pip compatible links from Socialcoding clone URLs

    Arguments:
        url {str} -- Clone URL from Socialcoding
    """
    package = url.split('/')[-1].split('.')[0]
    url = url.replace("https://", f"{package}@git+https://")
    url = url + f"#egg={package}"

    return url

# create pip compatible links
DEPENDENCIES_GITHUB = list(map(generate_pip_links_from_https, DEPENDENCIES_GITHUB))
DEPENDENCIES = DEPENDENCIES_ARTIFACTORY + DEPENDENCIES_GITHUB

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name=NAME,
    version_format='{tag}.dev{commitcount}+{gitsha}',
    author="srw2ho",
    author_email="",
    description="",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={},
    setup_requires=[
        'setuptools-git-version',
    ],
    install_requires=DEPENDENCIES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License"
        "Operating System :: OS Independent",
    ],
)