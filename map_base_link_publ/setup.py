from setuptools import find_packages, setup

package_name = 'map_base_link_publ'

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
    maintainer='cpsuser',
    maintainer_email='cpsuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'map_base_link_publ = map_base_link_publ.map_base_link_publ:main'
        ],
    },
)
