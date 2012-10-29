TARBALL = build/rtklibsample.zip
TARBALL_URL = http://www.rtklib.com/prog/rtklibsample.zip
INITIAL_DIR = build/rtklibsample
SOURCE_DIR = sample
MD5SUM_FILE = rtklibsample.zip.md5sum
UNPACK_CMD = unzip

include $(shell rospack find mk)/download_unpack_build.mk
include $(shell rospack find mk)/cmake.mk

rtklib_samples: $(SOURCE_DIR)/unpacked