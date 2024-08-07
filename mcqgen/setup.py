from setuptools import find_packages, setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Sriram',
    author_email='sriramsri230@gmail.com',
    install_requires=["groq","langchain","langchain-core","langchain-community","langchain-groq","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)