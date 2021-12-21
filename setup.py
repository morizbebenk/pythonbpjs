import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="pythonbpjs",
	version="0.0.4",
	author="Moriz",
	author_email="morizbebenk@gmail.com",
	description="Aplikasi Python yang digunakan untuk menangani proses dekripsi respon data dari bridging BPJS VClaim v2.0 (Encrypted Version). Support VClaim v1 / v1.1 dan Antrean RS.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/morizbebenk/pythonbpjs",
    project_urls={
        "Bug Tracker": "https://github.com/morizbebenk/pythonbpjs/issues",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license="MIT",
    keywords="bpjs vclaim vclaim-rest vclaim-encrypted",
    install_requires=["lzstring", "requests", "pycryptodome"]
)