from setuptools import find_packages, setup

package_name = 'rt2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lonlec',
    maintainer_email='seanalmeidaofficial@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'string_publisher = rt2_py.publisher_node:main',
        'palindrome_checker = rt2_py.checker_node:main',
        'result_responder = rt2_py.responder_node:main',
    ],
},
)
