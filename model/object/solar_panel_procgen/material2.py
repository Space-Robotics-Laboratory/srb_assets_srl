import bpy
import mathutils

mat = bpy.data.materials.new(name="SolarPanelGold")
mat.use_nodes = True


# initialize SolarPanelGoldShader node group
def solarpanelgoldshader_node_group():
    solarpanelgoldshader = bpy.data.node_groups.new(
        type="ShaderNodeTree", name="SolarPanelGoldShader"
    )

    solarpanelgoldshader.color_tag = "NONE"
    solarpanelgoldshader.description = ""
    solarpanelgoldshader.default_group_node_width = 140

    # solarpanelgoldshader interface
    # Socket Shader
    shader_socket = solarpanelgoldshader.interface.new_socket(
        name="Shader", in_out="OUTPUT", socket_type="NodeSocketShader"
    )
    shader_socket.attribute_domain = "POINT"

    # Socket Scale
    scale_socket = solarpanelgoldshader.interface.new_socket(
        name="Scale", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e38
    scale_socket.max_value = 3.4028234663852886e38
    scale_socket.subtype = "NONE"
    scale_socket.attribute_domain = "POINT"

    # Socket Metallic
    metallic_socket = solarpanelgoldshader.interface.new_socket(
        name="Metallic", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = "FACTOR"
    metallic_socket.attribute_domain = "POINT"

    # Socket Color 1
    color_1_socket = solarpanelgoldshader.interface.new_socket(
        name="Color 1", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_1_socket.default_value = (1.0, 0.3528609871864319, 0.06422899663448334, 1.0)
    color_1_socket.attribute_domain = "POINT"

    # Socket Color 2
    color_2_socket = solarpanelgoldshader.interface.new_socket(
        name="Color 2", in_out="INPUT", socket_type="NodeSocketColor"
    )
    color_2_socket.default_value = (
        0.01960499957203865,
        0.01960499957203865,
        0.01960499957203865,
        1.0,
    )
    color_2_socket.attribute_domain = "POINT"

    # Socket Grid Visibility
    grid_visibility_socket = solarpanelgoldshader.interface.new_socket(
        name="Grid Visibility", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    grid_visibility_socket.default_value = 0.30000001192092896
    grid_visibility_socket.min_value = 0.0
    grid_visibility_socket.max_value = 1.0
    grid_visibility_socket.subtype = "FACTOR"
    grid_visibility_socket.attribute_domain = "POINT"

    # Socket Roughness
    roughness_socket = solarpanelgoldshader.interface.new_socket(
        name="Roughness", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = "NONE"
    roughness_socket.attribute_domain = "POINT"

    # Socket Bump Strength
    bump_strength_socket = solarpanelgoldshader.interface.new_socket(
        name="Bump Strength", in_out="INPUT", socket_type="NodeSocketFloat"
    )
    bump_strength_socket.default_value = 0.20000000298023224
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = "FACTOR"
    bump_strength_socket.attribute_domain = "POINT"

    # initialize solarpanelgoldshader nodes
    # node Group Output
    group_output = solarpanelgoldshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Group Input
    group_input = solarpanelgoldshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Principled BSDF
    principled_bsdf = solarpanelgoldshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = "MULTI_GGX"
    principled_bsdf.subsurface_method = "RANDOM_WALK"
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[9].default_value = (
        1.0,
        0.20000000298023224,
        0.10000000149011612,
    )
    # Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    # Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    # Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    # node Brick Texture
    brick_texture = solarpanelgoldshader.nodes.new("ShaderNodeTexBrick")
    brick_texture.name = "Brick Texture"
    brick_texture.offset = 1.0
    brick_texture.offset_frequency = 2
    brick_texture.squash = 1.0
    brick_texture.squash_frequency = 2
    # Color1
    brick_texture.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    # Color2
    brick_texture.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    # Mortar
    brick_texture.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    # Scale
    brick_texture.inputs[4].default_value = 5.0
    # Mortar Size
    brick_texture.inputs[5].default_value = 0.019999999552965164
    # Mortar Smooth
    brick_texture.inputs[6].default_value = 0.10000000149011612
    # Bias
    brick_texture.inputs[7].default_value = 0.0
    # Brick Width
    brick_texture.inputs[8].default_value = 0.5
    # Row Height
    brick_texture.inputs[9].default_value = 0.25

    # node Mapping
    mapping = solarpanelgoldshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = "POINT"
    # Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    # node Texture Coordinate
    texture_coordinate = solarpanelgoldshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    # node Brick Texture.001
    brick_texture_001 = solarpanelgoldshader.nodes.new("ShaderNodeTexBrick")
    brick_texture_001.name = "Brick Texture.001"
    brick_texture_001.offset = 1.0
    brick_texture_001.offset_frequency = 2
    brick_texture_001.squash = 1.0
    brick_texture_001.squash_frequency = 2
    # Color1
    brick_texture_001.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    # Color2
    brick_texture_001.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    # Mortar
    brick_texture_001.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    # Scale
    brick_texture_001.inputs[4].default_value = 20.0
    # Mortar Size
    brick_texture_001.inputs[5].default_value = 0.019999999552965164
    # Mortar Smooth
    brick_texture_001.inputs[6].default_value = 0.4000000059604645
    # Bias
    brick_texture_001.inputs[7].default_value = 0.0
    # Brick Width
    brick_texture_001.inputs[8].default_value = 0.5
    # Row Height
    brick_texture_001.inputs[9].default_value = 0.25

    # node Brick Texture.002
    brick_texture_002 = solarpanelgoldshader.nodes.new("ShaderNodeTexBrick")
    brick_texture_002.name = "Brick Texture.002"
    brick_texture_002.offset = 1.0
    brick_texture_002.offset_frequency = 2
    brick_texture_002.squash = 1.0
    brick_texture_002.squash_frequency = 2
    # Color1
    brick_texture_002.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    # Color2
    brick_texture_002.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    # Mortar
    brick_texture_002.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    # Scale
    brick_texture_002.inputs[4].default_value = 120.0
    # Mortar Size
    brick_texture_002.inputs[5].default_value = 0.17000000178813934
    # Mortar Smooth
    brick_texture_002.inputs[6].default_value = 0.0
    # Bias
    brick_texture_002.inputs[7].default_value = 0.0
    # Brick Width
    brick_texture_002.inputs[8].default_value = 0.5
    # Row Height
    brick_texture_002.inputs[9].default_value = 0.5

    # node Mix
    mix = solarpanelgoldshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = "DARKEN"
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = "RGBA"
    mix.factor_mode = "UNIFORM"

    # node Mix.001
    mix_001 = solarpanelgoldshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = "DARKEN"
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = "RGBA"
    mix_001.factor_mode = "UNIFORM"
    # B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    # node Mix.002
    mix_002 = solarpanelgoldshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = "MIX"
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = "RGBA"
    mix_002.factor_mode = "UNIFORM"

    # node Bump
    bump = solarpanelgoldshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    # Distance
    bump.inputs[1].default_value = 1.0
    # Normal
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)

    # node Noise Texture
    noise_texture = solarpanelgoldshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = "3D"
    noise_texture.noise_type = "FBM"
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 50.0
    # Detail
    noise_texture.inputs[3].default_value = 15.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.6000000238418579
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # node Color Ramp
    color_ramp = solarpanelgoldshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = "RGB"
    color_ramp.color_ramp.hue_interpolation = "NEAR"
    color_ramp.color_ramp.interpolation = "LINEAR"

    # initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.26633164286613464
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (
        0.47251400351524353,
        0.47251400351524353,
        0.47251400351524353,
        1.0,
    )

    # node Hue/Saturation/Value
    hue_saturation_value = solarpanelgoldshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    # Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    # Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    # Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    # node Reroute
    reroute = solarpanelgoldshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    # node Mapping.001
    mapping_001 = solarpanelgoldshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = "POINT"
    # Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_001.inputs[3].default_value = (0.5, 0.5, 0.5)

    # Set locations
    group_output.location = (1036.668701171875, 90.20903778076172)
    group_input.location = (-832.8428344726562, -371.71112060546875)
    principled_bsdf.location = (783.4300537109375, 97.9495620727539)
    brick_texture.location = (-265.26287841796875, -376.85113525390625)
    mapping.location = (-674.0972290039062, -135.64739990234375)
    texture_coordinate.location = (-833.2088012695312, -138.69146728515625)
    brick_texture_001.location = (-263.9830322265625, 1.7639760971069336)
    brick_texture_002.location = (-265.26287841796875, 382.56854248046875)
    mix.location = (-79.95376586914062, -107.19638061523438)
    mix_001.location = (81.97224426269531, 102.55508422851562)
    mix_002.location = (614.9027709960938, 230.31039428710938)
    bump.location = (608.4172973632812, -172.93162536621094)
    noise_texture.location = (73.22274017333984, -150.87039184570312)
    color_ramp.location = (235.66050720214844, -118.16915893554688)
    hue_saturation_value.location = (602.0847778320312, -1.08966064453125)
    reroute.location = (-360.4981994628906, -170.269287109375)
    mapping_001.location = (-517.1841430664062, -138.0630340576172)

    # initialize solarpanelgoldshader links
    # reroute.Output -> brick_texture_002.Vector
    solarpanelgoldshader.links.new(reroute.outputs[0], brick_texture_002.inputs[0])
    # brick_texture_001.Color -> mix.A
    solarpanelgoldshader.links.new(brick_texture_001.outputs[0], mix.inputs[6])
    # mix_001.Result -> mix_002.Factor
    solarpanelgoldshader.links.new(mix_001.outputs[2], mix_002.inputs[0])
    # brick_texture.Color -> mix.B
    solarpanelgoldshader.links.new(brick_texture.outputs[0], mix.inputs[7])
    # bump.Normal -> principled_bsdf.Normal
    solarpanelgoldshader.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    # mix.Result -> mix_001.A
    solarpanelgoldshader.links.new(mix.outputs[2], mix_001.inputs[6])
    # reroute.Output -> noise_texture.Vector
    solarpanelgoldshader.links.new(reroute.outputs[0], noise_texture.inputs[0])
    # brick_texture_002.Color -> mix_001.Factor
    solarpanelgoldshader.links.new(brick_texture_002.outputs[0], mix_001.inputs[0])
    # mix_001.Result -> bump.Height
    solarpanelgoldshader.links.new(mix_001.outputs[2], bump.inputs[2])
    # mix_002.Result -> principled_bsdf.Base Color
    solarpanelgoldshader.links.new(mix_002.outputs[2], principled_bsdf.inputs[0])
    # color_ramp.Color -> hue_saturation_value.Color
    solarpanelgoldshader.links.new(
        color_ramp.outputs[0], hue_saturation_value.inputs[4]
    )
    # reroute.Output -> brick_texture.Vector
    solarpanelgoldshader.links.new(reroute.outputs[0], brick_texture.inputs[0])
    # hue_saturation_value.Color -> principled_bsdf.Roughness
    solarpanelgoldshader.links.new(
        hue_saturation_value.outputs[0], principled_bsdf.inputs[2]
    )
    # texture_coordinate.Object -> mapping.Vector
    solarpanelgoldshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    # noise_texture.Fac -> color_ramp.Fac
    solarpanelgoldshader.links.new(noise_texture.outputs[0], color_ramp.inputs[0])
    # reroute.Output -> brick_texture_001.Vector
    solarpanelgoldshader.links.new(reroute.outputs[0], brick_texture_001.inputs[0])
    # principled_bsdf.BSDF -> group_output.Shader
    solarpanelgoldshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    # group_input.Scale -> mapping.Scale
    solarpanelgoldshader.links.new(group_input.outputs[0], mapping.inputs[3])
    # group_input.Metallic -> principled_bsdf.Metallic
    solarpanelgoldshader.links.new(group_input.outputs[1], principled_bsdf.inputs[1])
    # group_input.Color 1 -> mix_002.A
    solarpanelgoldshader.links.new(group_input.outputs[2], mix_002.inputs[6])
    # group_input.Color 2 -> mix_002.B
    solarpanelgoldshader.links.new(group_input.outputs[3], mix_002.inputs[7])
    # group_input.Grid Visibility -> mix.Factor
    solarpanelgoldshader.links.new(group_input.outputs[4], mix.inputs[0])
    # group_input.Roughness -> hue_saturation_value.Value
    solarpanelgoldshader.links.new(
        group_input.outputs[5], hue_saturation_value.inputs[2]
    )
    # group_input.Bump Strength -> bump.Strength
    solarpanelgoldshader.links.new(group_input.outputs[6], bump.inputs[0])
    # mapping_001.Vector -> reroute.Input
    solarpanelgoldshader.links.new(mapping_001.outputs[0], reroute.inputs[0])
    # mapping.Vector -> mapping_001.Vector
    solarpanelgoldshader.links.new(mapping.outputs[0], mapping_001.inputs[0])
    return solarpanelgoldshader


solarpanelgoldshader = solarpanelgoldshader_node_group()


# initialize SolarPanelGold node group
def solarpanelgold_node_group():
    solarpanelgold = mat.node_tree
    # start with a clean node tree
    for node in solarpanelgold.nodes:
        solarpanelgold.nodes.remove(node)
    solarpanelgold.color_tag = "NONE"
    solarpanelgold.description = ""
    solarpanelgold.default_group_node_width = 140

    # solarpanelgold interface

    # initialize solarpanelgold nodes
    # node Material Output
    material_output = solarpanelgold.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = "ALL"
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # node Group
    group = solarpanelgold.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = solarpanelgoldshader
    # Socket_1
    group.inputs[0].default_value = 1.0
    # Socket_2
    group.inputs[1].default_value = 1.0
    # Socket_3
    group.inputs[2].default_value = (1.0, 0.3528609871864319, 0.06422899663448334, 1.0)
    # Socket_4
    group.inputs[3].default_value = (
        0.01960499957203865,
        0.01960499957203865,
        0.01960499957203865,
        1.0,
    )
    # Socket_5
    group.inputs[4].default_value = 0.30000001192092896
    # Socket_6
    group.inputs[5].default_value = 1.0
    # Socket_7
    group.inputs[6].default_value = 0.20000000298023224

    # Set locations
    material_output.location = (989.0977172851562, 506.0550231933594)
    group.location = (735.8889770507812, 512.1011962890625)

    # initialize solarpanelgold links
    # group.Shader -> material_output.Surface
    solarpanelgold.links.new(group.outputs[0], material_output.inputs[0])
    return solarpanelgold


solarpanelgold = solarpanelgold_node_group()
