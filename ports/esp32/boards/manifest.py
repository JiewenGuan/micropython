freeze("$(PORT_DIR)/modules")
include("$(MPY_DIR)/extmod/uasyncio")

include("$(MPY_DIR)/lib/microdot/libs/common/utemplate")

# Useful networking-related packages.
require("bundle-networking")

# Require some micropython-lib modules.
require("dht")                           
require("ds18x20")   
require("neopixel")
require("onewire")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")

require("pyjwt")
require("urequests")
require("datetime")
require("errno")
require("hmac")
require("pickle")
require("threading")
require("types")
require("unittest")
require("sdcard")

freeze("$(MPY_DIR)/lib/microdot/src")
