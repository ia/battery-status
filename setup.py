#!/usr/bin/env python


#* part of battery-status project
#* battery-status - applet/indicator with battery information
#* Copyright (c) 2010 Ivan Zorin <ivan.a.zorin@gmail.com>
#* see README for more information


"""applet/indicator with battery status for the GNOME panel""";


from distutils.core import setup;
from distutils.command.install_data import install_data;


class InstallData(install_data):
	def run(self):
		install_data.run(self);


setup(
	name = "battery-status",
	version = "0.1.1",
	maintainer = "Ivan Zorin",
	maintainer_email = "ivan.a.zorin@gmail.com",
	description = "battery status",
	license = "GNU GPL v3",
	scripts = [],
	url = "http://live.gnome.org/BatteryApplet",
	package_dir = {},
	packages = [],
	data_files=[('/usr/lib/battery-status', ['battery-status']),
		('/usr/lib/bonobo/servers', ['Battery_Applet.server']),
		('/usr/share/gconf/schemas', ['battery-status.schemas']),
	],
	cmdclass={'install_data': InstallData}
)
