# RISC-V device tree documentation

This repository is a collection of [device tree][dt] bindings, for RISC-V
emulators and hardware.

Device tree bindings specify the meaning of the properties in a device tree
node.


## Adding a new binding file

- Add your binding file under the [bindings directory].
- If your binding is already present in Linux's
  [Documentation/devicetree/bindings][linux-bindings] directory, make sure you
  use the same file name and relative path.
- If your vendor prefix is not yet in [vendor-prefixes.txt], make sure to add
  it as soon as possible to avoid collisions and inconsistencies.
- Make a pull request


## License

[GPLv2], unless stated otherwise. This ensures that binding files can be
exchanged between Linux and this repository without issues.


[dt]: https://www.devicetree.org/
[bindings directory]: bindings
[linux-bindings]: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings
[vendor-prefixes.txt]: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings/vendor-prefixes.txt
[GPLv2]: GPL-2.0.license
