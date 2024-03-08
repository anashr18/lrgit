from setuptools import setup, find_packages

setup(
    name="yg-transformers",
    # packages=find_packages(exclude=["examples"]),
    packages=find_packages(exclude=["examples*", "myexp*"]),
    version="0.0.1",
    license="MIT",
    description="yg-Transformers - Pytorch",
    author="yug",
    author_email="anand.shri18@gmail.com",
    # url="https://github.com/lucidrains/x-transformers",
    long_description_content_type="text/markdown",
    keywords=["artificial intelligence", "attention mechanism", "transformers"],
    install_requires=["torch>=1.6", "einops>=0.7.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
