# NetTango Models (Preliminary) Library
A preliminary version of a "Models Library" for NetTango models. To browse the library, please [visit our current library directory](https://github.com/NetLogo/nt-models/blob/main/LIBRARY.md).

NetTango is a tool that allows you to build blocks-based programming environments for [NetLogo](https://www.github.com/NetLogo/NetLogo) models. For more information on building your own NetTango models, visit the [documentation for the NetTango Builder](https://github.com/NetLogo/Galapagos/wiki/NetTango-Builder).

## Playable vs. Editable
NetTango allows you to share two different versions of a model:
1. Playable - A NetTango model whose blocks spaces are interactive, but the blocks and model themselves are not editable.
2. Editable - A NetTango model whos blocks spaces and model content are fully editable.
In the library directory, the default link is to the Playable version with a separate link provided to the Editable version.

## Hot-Linking Models
The easiest way to access or link to one of these models is to "hot-link" the hosted NetTango JSON files hosted here using the current live version of NetTango.
- To share for editing, use `https://netlogoweb.org/nettango-builder?netTangoModel=$LINK_TO_YOUR_MODEL`
- To share in play mode without editing features, use `https://netlogoweb.org/nettango-player?playMode=true&netTangoModel=$LINK_TO_YOUR_MODEL`.

For examples of these, check out our [current library directory](https://github.com/NetLogo/nt-models/blob/main/LIBRARY.md).

## Important Note
Users should think of this as a centralized repository for NetTango models developed by the CCL and *NOT* as a formal Models Library like [NetLogo/models](https://www.github.com/NetLogo/NetLogo). NetTango is under active development right now and many things are subject to change, including the details here. We are not currently accepting submissions for inclusion into this particular library.

Future additions to this repository will include a NetTango model Style Guide, automated testing suites, and a more fully featured browser and directory structure.

## Usage
To re-generate the models `LIBRARY.md` and `library.json` files run `python ./src/LibraryGenerator.py`.  You'll need some version of Python installed, preferrably Python 3.

## Questions?
Send us an email at [czars@ccl.northwestern.edu](mailto:czars@ccl.northwestern.edu).
