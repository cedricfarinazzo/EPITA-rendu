CURRENT_DIR=$(shell pwd)
SOURCE_DIR=/src/
BIN_DIR=/bin/
TMP_DIR=/tmp/

PY_NAME=epitarendu.py
APP_NAME=epitarendu

OK=yes


.PHONY: check update build clean clean-tmp clean-portable build-simple build-portable

update:
	git pull

check:
	@type python3 > /dev/null 2>&1 || (OK=no; echo "python3 not found. Please install python")
	@type nuitka3 > /dev/null 2>&1 || (OK=no; echo "nuitka3 not found. Please install nuitka3")
	
clean: clean-tmp
	rm -rf $(CURRENT_DIR)$(SOURCE_DIR)__pycache__
	rm -rf $(CURRENT_DIR)$(BIN_DIR)*

clean-tmp:
	rm -rf $(CURRENT_DIR)$(TMP_DIR)	

clean-portable:
	rm -rf $(CURRENT_DIR)$(BIN_DIR)portable/*

build-portable: clean-tmp clean-portable check
	mkdir -p $(CURRENT_DIR)$(TMP_DIR)
	mkdir -p $(CURRENT_DIR)$(BIN_DIR)portable/
	cp $(CURRENT_DIR)$(SOURCE_DIR)* $(CURRENT_DIR)$(TMP_DIR)
	@cd $(CURRENT_DIR)$(TMP_DIR) && nuitka3 --recurse-all --show-progress --standalone $(CURRENT_DIR)$(TMP_DIR)$(PY_NAME)
	cd $(CURRENT_DIR)
	cp $(CURRENT_DIR)$(TMP_DIR)$(APP_NAME).dist/* $(CURRENT_DIR)$(BIN_DIR)portable/
	$(shell make clean-tmp)

build-simple: clean check
	mkdir -p $(CURRENT_DIR)$(TMP_DIR)
	mkdir -p $(CURRENT_DIR)$(BIN_DIR)
	cp $(CURRENT_DIR)$(SOURCE_DIR)* $(CURRENT_DIR)$(TMP_DIR)
	@cd $(CURRENT_DIR)$(TMP_DIR) && nuitka3 --recurse-all --show-progress $(CURRENT_DIR)$(TMP_DIR)$(PY_NAME)
	cd $(CURRENT_DIR)
	cp $(CURRENT_DIR)$(TMP_DIR)$(APP_NAME).exe $(CURRENT_DIR)$(BIN_DIR)$(APP_NAME)
	$(shell make clean-tmp)

build: build-simple build-portable
