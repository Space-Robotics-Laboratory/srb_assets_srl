# [Space Robotics Bench](https://github.com/AndrejOrsula/space_robotics_bench) — Assets

This repository contains assets for the [**Space Robotics Bench**](https://github.com/AndrejOrsula/space_robotics_bench) initiative. It includes 3D models, textures, HDRIs, and other resources for creating realistic space environments. Some assets feature procedural pipelines that allow for the generation of near-infinite variations of geometry and materials.

## Usage

Although these assets are primarily intended for use within the Space Robotics Bench initiative, they are purposefully separated into this repository to allow for their independent use in other projects.

### Am I allowed to use these assets in my project?

Before using any of the assets, please refer to the [Attributions](#attributions) and [License](#license) sections below. In general, you can follow these guidelines for using the assets:

1. Review the [full list of attributions](https://AndrejOrsula.github.io/space_robotics_bench/misc/attributions.html) and check if the asset you want to use is based on third-party resources.
   - If the asset is based on third-party resources and refers to the original license, make sure to comply with the original license terms. In most cases, you will need to give appropriate credit to the original author and indicate the changes made by you and the contributors of this repository (similar to the entry in the list). It is not necessary to provide attribution to the contributors of this repository because the modifications are licensed under the [CC0 1.0 Universal](LICENSE-CC0) license (although credit is always appreciated).
   - If the asset is based on third-party resources but does not refer to any original license, it does not fall under any restrictions. It is licensed under the [CC0 1.0 Universal](LICENSE-CC0) license. You can use it freely in your projects without attribution requirements (although credit is always appreciated).
   - If the asset is unlisted, it was created by contributors of this repository and is licensed under the [CC0 1.0 Universal](LICENSE-CC0) license. You can use it freely in your projects without any restrictions or attribution requirements (although credit is always appreciated).
1. Clone the entire repository or download the assets you want to use.
1. For static assets (e.g. 3D models, textures, HDRIs), you can use them directly in your project. For procedural pipelines, you can follow the instructions below to generate individual assets.

### How to use procedural pipelines?

All procedural pipelines included in this repository are based on [Blender](https://www.blender.org), where [Geometry Nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/introduction.html) generate procedural geometry and [Shader Nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/introduction.html) create procedural materials. These pipelines are distributed as Python scripts that can be used either within the Blender GUI or via standalone scripts.

#### Generate Assets inside Blender GUI

To use a procedural pipeline inside Blender GUI, follow these steps:

1. Open the Blender application using either a new or existing project.
1. Switch to the `Scripting` workspace or create a new Text Editor panel.
1. Add your desired Python script to the Text Editor panel by either opening the script file via the `Open` button or pasting the script content into a `New` text block.
1. Run the script by pressing the "Play" button. It will construct the appropriate Geometry Nodes or Shader Nodes in the current Blender project.
1. Use the procedural geometry or material in your project as needed.
   - For procedural geometry, you can create a new empty object and add the appropriate Geometry Nodes modifier to it. You can then adjust the parameters of the Geometry Nodes setup to generate the desired geometry.
   - For procedural materials, you can assign the material to the desired object.
1. Export the 3D model as needed.

#### Generate Assets using Standalone Scripts

Procedural assets can also be generated using standalone scripts that require close integration with Blender's Python API `bpy`. You can either write your own script that performs the steps outlined above or use the [`procgen_assets.py`](scripts/blender/procgen_assets.py) as a starting point. This script provides an automated pipeline for generating procedural 3D models with baked textures into one of many supported formats (ABC, FBX, GLTF, OBJ, PLY, SDF, STL, USD).

## Attributions

Some of the included assets are based on modified third-party resources. For more information, please refer to the [full list of attributions](https://AndrejOrsula.github.io/space_robotics_bench/misc/attributions.html).

<p>
  <a href="https://AndrejOrsula.github.io/space_robotics_bench/misc/attributions.html"> <img alt="HTML" src="https://github.com/AndrejOrsula/awesome-space-robotics/assets/22929099/3c8accf7-5acb-4bcd-9553-bf49cc622abe" width="96" height="96"></a>
</p>

## License

All assets created by contributors of this repository and those generated from the included procedural pipelines are licensed under the [CC0 1.0 Universal](LICENSE-CC0) license.

<a href="https://creativecommons.org/publicdomain/zero/1.0"><img src="https://licensebuttons.net/l/zero/1.0/88x31.png" width="88" height="31"></a>
