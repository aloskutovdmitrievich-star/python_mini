from setuptools import setup, find_packages

def readme():
    with open("README.md", "r") as f:
        return f.read()
    

setup(name="python_mini",
      version="0.0.2", 
      author="ARFIII",
      author_email="a.loskutov.dmitrievich@gmail.com",
      long_description=readme(),
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=["requests>=2.25.1"],
      classifiers=[
          "Programming Language :: Python :: 3.13",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      project_urls={
          "GitHub" : "https://github.com/aloskutovdmitrievich-star/python_mini",
          "Render" : "https://render.com"

      })
