BINDINGS = $(patsubst bindings/%,%,$(shell find bindings -type f))

check: $(patsubst %,check/%.diff,$(BINDINGS))
check: check/kernel_version

check/kernel_version: .git/modules/linux/refs/heads/master
	if [ $$(date -d "last week" +%s) -gt $$(git -C linux show --format=%at | head -n1) ]; then echo "Linux is too old"; exit 1; fi

check/%.diff: bindings/% linux/Documentation/devicetree/bindings/%
	diff -u $^

check/%.diff: bindings/%
