from setuptools import find_packages, setup

setup(
    name="gethist",
    version="0.0.1",
    description="CLI to download versions of targeted files in git history.",
    author="Kelly Christensen",
    keywords="git",
    license="GPL-3.0",
    python_requires=">=3.11",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "GitPython==3.1.40",
        "click==8.1.7",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "pygments==2.17.2",
        "rich==13.7.0",
    ],
    entry_points={
        "console_scripts": ["gethist=src.cli:cli"],
    },
    zip_safe=True,
)
