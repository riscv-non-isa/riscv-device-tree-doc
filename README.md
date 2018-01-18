# RISC-V device tree documentation [![(build status)](https://travis-ci.org/riscv/riscv-device-tree-doc.svg?branch=master)](https://travis-ci.org/riscv/riscv-device-tree-doc)

This repository is a collection of [device tree][dt] bindings, for RISC-V
emulators and hardware.

Device tree bindings specify the meaning of the properties in a device tree
node.


## Adding a new binding file

- Add your binding file under the [bindings directory].
- If your binding is already present in Linux's
  [Documentation/devicetree/bindings][linux-bindings] directory, make sure you
  use the same file name and relative path.
- If your binding is not present in Linux, add its name (including the path
  leading up to it) to [bindings/not-in-linux.txt].
- If your vendor prefix is not yet in [vendor-prefixes.txt], make sure to add
  it as soon as possible to avoid collisions and inconsistencies.
- Make a pull request


## Checking consistency with Linux

If you want to check the devicetree bindings in this repo against those in
Linux's `Documentation/devicetree/bindings` directory, there's [a script] for
that. You can use it like this:

```sh
scripts/check-against-linux.py bindings \
                               /path/to/linux/Documentation/devicetree/bindings
```

Note that [Travis-CI] runs this script on every commit and pull request.


## License

[GPLv2], unless stated otherwise. This ensures that binding files can be
exchanged between Linux and this repository without issues.


[dt]: https://www.devicetree.org/
[bindings directory]: bindings
[linux-bindings]: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings
[vendor-prefixes.txt]: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings/vendor-prefixes.txt
[a script]: scripts/check-against-linux.py
[Travis-CI]: https://travis-ci.org/riscv/riscv-device-tree-doc
[GPLv2]: GPL-2.0.license
