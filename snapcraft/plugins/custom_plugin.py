import snapcraft

"""
See http://snapcraft.io/docs/build-snaps/plugins
    for more information on creating custom plugins
"""

class Barf(snapcraft.BasePlugin):

    @classmethod
    def schema(cls):
        """ This method defines the parameters passed to
            the plugin
        """
        schema = super().schema()

        #
        # For example, the following code adds
        # "config-parameters" as a required property:
        #
        # schema["properties"]["config-parameters"] = {
        #    "type": "array",
        #    "minitems": 1,
        #    "uniqueItems": True,
        #    "items": {
        #        "type": "string",
        #    },
        #    "default": [],
        # }
        #
        # schema["required"].append("config-parameters")
        #

        return schema

    def build(self):
        """ This method controls the build process; override
            or extend it to replace or add custom functionality
        """
        super().build()

        #
        # For example, the following code
        # runs a custom make-based install:
        #
        # config_command = ["./config"]
        # config_command.extend(self.options.config_parameters)
        # self.run(config_command)
        # self.run(["make"])
        # self.run(["make", "test"])
        # self.run(["make", "install"])
        #


